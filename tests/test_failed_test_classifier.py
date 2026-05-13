import unittest

from scripts.failed_test_classifier import classify_message


class FailedTestClassifierTests(unittest.TestCase):
    def test_classifies_timeout_failure(self):
        self.assertEqual(classify_message("Timed out waiting for element"), "timeout")

    def test_classifies_assertion_failure(self):
        self.assertEqual(classify_message("Expected total to match actual total"), "assertion")

    def test_classifies_data_failure(self):
        self.assertEqual(classify_message("Missing data: invoice_id was null"), "data")

    def test_unclassified_failure(self):
        self.assertEqual(classify_message("Unexpected behavior occurred"), "unclassified")


if __name__ == "__main__":
    unittest.main()
