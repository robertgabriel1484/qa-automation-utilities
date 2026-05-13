#!/usr/bin/env python3
"""Classify failed tests using simple keyword rules for QA triage."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


CLASSIFICATION_RULES = {
    "locator": [r"\bno such element\b", r"\blocator\b", r"\bselector\b", r"\belement not found\b"],
    "timeout": [r"\btimeout\b", r"\btimed out\b", r"\bwaiting\b"],
    "assertion": [r"\bexpected\b", r"\bactual\b", r"\bassert\b", r"\bmismatch\b"],
    "environment": [r"\bconnection refused\b", r"\bserver error\b", r"\b503\b", r"\b500\b", r"\bunavailable\b"],
    "data": [r"\bmissing data\b", r"\bduplicate\b", r"\binvalid data\b", r"\bnull value\b"],
}


def classify_message(message: str) -> str:
    lower_message = message.lower()

    for category, patterns in CLASSIFICATION_RULES.items():
        if any(re.search(pattern, lower_message) for pattern in patterns):
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
