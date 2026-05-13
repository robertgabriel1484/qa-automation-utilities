import unittest

from scripts.release_checklist_generator import generate_release_checklist


class ReleaseChecklistGeneratorTests(unittest.TestCase):
    def test_release_checklist_contains_core_sections(self):
        checklist = generate_release_checklist("Demo Release")

        self.assertIn("Release: Demo Release", checklist)
        self.assertIn("QA Validation", checklist)
        self.assertIn("Defect Review", checklist)
        self.assertIn("Release Decision", checklist)


if __name__ == "__main__":
    unittest.main()
