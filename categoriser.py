"""Prompt design, schema normalisation, and LLM inference for the
Smart To-do Categoriser.

Provider: Google Gemini 2.5 Flash (free tier), using native structured
output (`response_schema`). The API guarantees the response conforms to the
schema, so parsing is a backstop rather than the main path.
"""

import json
import os
from typing import Any

from google import genai
from google.api_core import exceptions as google_exceptions
from google.genai import types
from pydantic import ValidationError

from models import Category, Priority, Task

MODEL = "gemini-2.5-flash"
TIMEOUT_S = 10.0
AMBIGUITY_THRESHOLD = 0.7

SYSTEM_PROMPT = """You are a task parser. Convert the user's natural-language task
into a structured JSON object with exactly these fields:
- task_description: the core task, de-noised, in the user's own words.
- category: ONE of Personal, Work, Shopping, Errands, Finance, Health, Social, Home, Other.
- priority: ONE of High, Medium, Low, inferred from urgency cues and deadline.
- deadline: an ISO 8601 date or datetime if a time expression is present, otherwise null.
- confidence: a number 0.0-1.0 for how sure you are about category and priority.
- is_ambiguous: true when category or priority cannot be inferred with high confidence.

Rules:
- If no deadline is stated, set deadline to null.
- If the category is a guess, lower confidence and set is_ambiguous true.
- Prefer the most specific category that fits; use Other only when nothing fits.
- Priority cues: explicit deadlines or urgency words = High; recurring or soon = Medium; no cue = Low.
"""

# Messages in Gemini's Content shape: role + parts (not OpenAI's role/content).
FEW_SHOTS = [
    {"role": "user", "parts": [{"text": "Buy milk before Thursday"}]},
    {"role": "model", "parts": [{"text": json.dumps({
        "task_description": "Buy milk",
        "category": "Shopping",
        "priority": "Medium",
        "deadline": "2026-11-05",
        "confidence": 0.9,
        "is_ambiguous": False,
    })}]},
    {"role": "user", "parts": [{"text": "Schedule dentist appointment"}]},
    {"role": "model", "parts": [{"text": json.dumps({
        "task_description": "Schedule a dentist appointment",
        "category": "Health",
        "priority": "Low",
        "deadline": None,
        "confidence": 0.6,
        "is_ambiguous": True,
    })}]},
    {"role": "user", "parts": [{"text": "Submit quarterly report to the board"}]},
    {"role": "model", "parts": [{"text": json.dumps({
        "task_description": "Submit the quarterly report to the board",
        "category": "Work",
        "priority": "High",
        "deadline": None,
        "confidence": 0.85,
        "is_ambiguous": False,
    })}]},
]


def build_messages(task: str) -> list[dict]:
    """Assemble the full message list sent to the model, in Gemini's
    Content shape (role + parts)."""
    return [{"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
            *FEW_SHOTS,
            {"role": "user", "parts": [{"text": task}]}]


def _normalise_schema(schema: Any) -> Any:
    """Strip Pydantic-specific keys and recurse so the schema is a clean
    JSON Schema that Gemini's `response_schema` accepts."""
    if isinstance(schema, dict):
        schema = {k: v for k, v in schema.items()
                  if k not in ("title", "description", "default")}
        for key, value in schema.items():
            schema[key] = _normalise_schema(value)
    elif isinstance(schema, list):
        return [_normalise_schema(item) for item in schema]
    return schema


def _finalise(task: Task) -> Task:
    """Re-derive the ambiguity flag from the threshold as a safety net."""
    task.is_ambiguous = task.is_ambiguous or task.confidence < AMBIGUITY_THRESHOLD
    return task


def _heuristic_fallback(task: str) -> Task:
    """Local-only result used by --dry-run (no network)."""
    return _finalise(Task(
        task_description=task.strip(),
        category=Category.Other,
        priority=Priority.Low,
        deadline=None,
        confidence=0.3,
        is_ambiguous=True,
    ))


def categorise(task: str, provider: str = "gemini", dry_run: bool = False) -> Task:
    """Parse a natural-language task into a validated Task object."""
    if not task or not task.strip():
        raise RuntimeError("task input is empty")

    messages = build_messages(task)

    if dry_run:
        print(json.dumps(messages, indent=2))
        return _heuristic_fallback(task)

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")

    schema = _normalise_schema(Task.model_json_schema())
    config = types.GenerateContentConfig(
        temperature=0,
        response_mime_type="application/json",
        response_schema=schema,
    )
    # Timeout lives on the HTTP layer, not the API call.
    http_options = types.HttpOptions(timeout=int(TIMEOUT_S * 1000))
    client = genai.Client(api_key=api_key, http_options=http_options)

    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents=messages,
            config=config,
        )
    except google_exceptions.DeadlineExceeded:
        raise RuntimeError(f"inference timed out after {TIMEOUT_S}s")
    except google_exceptions.ResourceExhausted as exc:
        raise RuntimeError(f"rate limited: {exc}") from exc
    except Exception as exc:
        raise RuntimeError(f"API error: {exc}") from exc

    try:
        return _finalise(Task.model_validate(json.loads(resp.text)))
    except (ValidationError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"schema validation failed: {exc}") from exc


__all__ = [
    "SYSTEM_PROMPT",
    "FEW_SHOTS",
    "build_messages",
    "categorise",
    "_finalise",
    "MODEL",
    "TIMEOUT_S",
    "AMBIGUITY_THRESHOLD",
]