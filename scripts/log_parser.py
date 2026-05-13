#!/usr/bin/env python3
"""Parse application logs and summarize errors/warnings for QA review."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path


def parse_log_file(path: Path) -> dict[str, object]:
    counts: Counter[str] = Counter()
    error_lines: list[str] = []

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        upper_line = line.upper()

        if "ERROR" in upper_line:
            counts["ERROR"] += 1
            error_lines.append(f"{line_number}: {line}")
        elif "WARN" in upper_line or "WARNING" in upper_line:
            counts["WARNING"] += 1
        elif "INFO" in upper_line:
            counts["INFO"] += 1

    return {
        "counts": dict(counts),
        "error_lines": error_lines,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse a log file and summarize QA-relevant issues.")
    parser.add_argument("log_file", type=Path, help="Path to the log file.")
    args = parser.parse_args()

    result = parse_log_file(args.log_file)

    print("Log Summary")
    print("-----------")
    for key in ["ERROR", "WARNING", "INFO"]:
        print(f"{key}: {result['counts'].get(key, 0)}")

    if result["error_lines"]:
        print("\nError Lines")
        print("-----------")
        for line in result["error_lines"]:
            print(line)


if __name__ == "__main__":
    main()
