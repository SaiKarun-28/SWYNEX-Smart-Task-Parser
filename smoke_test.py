"""Ponytail self-check for the Smart To-do Categoriser.

No frameworks, no API key, no network. Fails loudly if the schema, enum
coercion, prompt assembly, or ambiguity logic regresses.

Run:  python smoke_test.py
"""

import json

from categoriser import (
    AMBIGUITY_THRESHOLD,
    FEW_SHOTS,
    SYSTEM_PROMPT,
    _finalise,
    build_messages,
)
from models import Category, Priority, Task


def _check(cond, msg):
    if not cond:
        raise AssertionError(msg)


# 1. Schema round-trips and enforces enums.
t = Task(task_description="Buy milk", category="Shopping",
         priority="Medium", deadline=None, confidence=0.9, is_ambiguous=False)
_check(t.category is Category.Shopping, "category should coerce to enum")
_check(t.priority is Priority.Medium, "priority should coerce to enum")
_dump = json.loads(t.model_dump_json())
_check(_dump["category"] == "Shopping", "enum must serialise as plain string")
_check(_dump["deadline"] is None, "null deadline must stay null")

# 2. Invalid enum / missing field / out-of-range confidence all fail loudly.
for bad in [
    {"task_description": "x", "category": "Teleporting", "priority": "Medium",
     "deadline": None, "confidence": 0.9, "is_ambiguous": False},
    {"task_description": "x", "category": "Shopping", "priority": "Medium",
     "deadline": None, "confidence": 9.0, "is_ambiguous": False},
    {"category": "Shopping", "priority": "Medium",
     "deadline": None, "confidence": 0.9},  # missing required task_description
]:
    try:
        Task(**bad)
    except Exception:
        pass
    else:
        raise AssertionError(f"expected validation failure: {bad}")

# 3. Prompt + few-shots are well-formed and the schema matches the model.
messages = build_messages("Buy milk before Thursday")
_check(messages[0]["role"] == "user", "first message must be the system instruction")
_check(messages[-1]["role"] == "user", "last message must be the user task")
_check(len(messages) == 1 + len(FEW_SHOTS),
       "few-shot count must be preserved")
schema = Task.model_json_schema()
for prop in ("task_description", "category", "priority", "deadline",
             "confidence", "is_ambiguous"):
    _check(prop in schema["properties"], f"schema missing field {prop}")

# 4. Ambiguity threshold logic.
low = Task(task_description="d", category=Category.Other, priority=Priority.Low,
           deadline=None, confidence=0.4, is_ambiguous=False)
final = _finalise(low)
_check(final.is_ambiguous is True, "low confidence must flag ambiguous")
high = Task(task_description="d", category=Category.Work, priority=Priority.High,
            deadline=None, confidence=0.95, is_ambiguous=False)
_check(_finalise(high).is_ambiguous is False, "high confidence must not flag ambiguous")
_check(0.0 <= AMBIGUITY_THRESHOLD <= 1.0, "threshold must be in range")

# 5. Schema normaliser is a no-op on valid input and strips Pydantic keys.
from categoriser import _normalise_schema
clean = _normalise_schema(Task.model_json_schema())
_check("title" not in clean, "normaliser must strip Pydantic 'title'")
_check("description" not in clean, "normaliser must strip Pydantic 'description'")
_check("properties" in clean, "normaliser must preserve schema structure")

print("smoke_test: OK")


if __name__ == "__main__":
    pass