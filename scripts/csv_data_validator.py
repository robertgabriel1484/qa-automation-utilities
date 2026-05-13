#!/usr/bin/env python3
"""Validate invoice CSV data for common QA/data-quality issues."""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path


REQUIRED_COLUMNS = {"invoice_id", "vendor_id", "invoice_amount", "tax_amount", "status"}


def validate_invoice_csv(path: Path) -> list[str]:
    issues: list[str] = []

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            return ["CSV file is missing a header row."]

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing_columns:
            issues.append(f"Missing required columns: {', '.join(sorted(missing_columns))}")
            return issues

        seen_invoice_ids: set[str] = set()

        for row_number, row in enumerate(reader, start=2):
            invoice_id = row["invoice_id"].strip()

            if not invoice_id:
                issues.append(f"Row {row_number}: invoice_id is blank.")
            elif invoice_id in seen_invoice_ids:
                issues.append(f"Row {row_number}: duplicate invoice_id {invoice_id}.")
            else:
                seen_invoice_ids.add(invoice_id)

            for money_field in ["invoice_amount", "tax_amount"]:
                value = row[money_field].strip()
                try:
                    amount = Decimal(value)
                    if amount < 0:
                        issues.append(f"Row {row_number}: {money_field} cannot be negative.")
                except InvalidOperation:
                    issues.append(f"Row {row_number}: {money_field} is not a valid decimal.")

            if row["status"].strip().upper() not in {"OPEN", "PAID", "DISPUTED"}:
                issues.append(f"Row {row_number}: invalid status {row['status']}.")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate invoice CSV data.")
    parser.add_argument("csv_file", type=Path, help="Path to invoice CSV file.")
    args = parser.parse_args()

    issues = validate_invoice_csv(args.csv_file)

    if not issues:
        print("CSV validation passed. No issues found.")
        return

    print("CSV Validation Issues")
    print("---------------------")
    for issue in issues:
        print(f"- {issue}")


if __name__ == "__main__":
    main()
