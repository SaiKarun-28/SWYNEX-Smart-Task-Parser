"""Command-line entry point for the Smart To-do Categoriser."""

import argparse
import json
import sys

from categoriser import categorise
from models import Task

AMBIGUOUS_EXIT = 3


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="smart-todo",
        description="Parse a natural-language task into a structured task object.",
    )
    p.add_argument("task", help="The task string, e.g. 'Buy milk before Thursday'")
    p.add_argument("--provider", default="gemini", choices=["gemini"],
                   help="LLM provider (default: gemini)")
    p.add_argument("--json", action="store_true",
                   help="Print raw JSON instead of a pretty summary")
    p.add_argument("--dry-run", action="store_true",
                   help="Print the messages that would be sent and exit (no API call)")
    return p


def _pretty(task: Task) -> str:
    flag = " [AMBIGUOUS]" if task.is_ambiguous else ""
    deadline = task.deadline or "none"
    return (f"{task.task_description}\n"
            f"  category:    {task.category.value}\n"
            f"  priority:    {task.priority.value}\n"
            f"  deadline:    {deadline}\n"
            f"  confidence:  {task.confidence:.2f}{flag}")


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result: Task = categorise(args.task, provider=args.provider,
                                  dry_run=args.dry_run)
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result.model_dump(), indent=2) if args.json
          else _pretty(result))
    return AMBIGUOUS_EXIT if result.is_ambiguous else 0


if __name__ == "__main__":
    sys.exit(main())