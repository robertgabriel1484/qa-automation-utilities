import unittest
from pathlib import Path

from scripts.csv_data_validator import validate_invoice_csv


class CsvDataValidatorTests(unittest.TestCase):
    def test_sample_invoice_csv_returns_expected_issues(self):
        issues = validate_invoice_csv(Path("sample_data/sample_invoices.csv"))

        self.assertTrue(any("duplicate invoice_id" in issue for issue in issues))
        self.assertTrue(any("cannot be negative" in issue for issue in issues))
        self.assertTrue(any("not a valid decimal" in issue for issue in issues))
        self.assertTrue(any("invalid status" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
