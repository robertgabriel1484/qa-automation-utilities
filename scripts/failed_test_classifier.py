#!/usr/bin/env python3
"""Classify failed tests using simple keyword rules for QA triage."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


CLASSIFICATION_RULES = {
    "locator": ["no such element", "locator", "selector", "element not found"],
    "timeout": ["timeout", "timed out", "waiting"],
    "assertion": ["expected", "actual", "assert", "mismatch"],
    "environment": ["connection refused", "server error", "503", "500", "unavailable"],
    "data": ["missing data", "duplicate", "invalid data", "null value"],
}


def classify_message(message: str) -> str:
    lower_message = message.lower()

    for category, keywords in CLASSIFICATION_RULES.items():
        if any(keyword in lower_message for keyword in keywords):
            return category

    return "unclassified"


def classify_failed_tests(path: Path) -> dict[str, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    counts: Counter[str] = Counter()

    for test in data.get("tests", []):
        if test.get("status", "").lower() == "failed":
            category = classify_message(test.get("message", ""))
            counts[category] += 1

    return dict(counts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify failed tests from a JSON test result file.")
    parser.add_argument("results_file", type=Path, help="Path to JSON test results.")
    args = parser.parse_args()

    counts = classify_failed_tests(args.results_file)

    print("Failed Test Classification")
    print("--------------------------")
    for category, count in sorted(counts.items()):
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
