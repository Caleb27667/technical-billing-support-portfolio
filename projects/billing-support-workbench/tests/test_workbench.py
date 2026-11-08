import unittest

from src.workbench import triage


class WorkbenchTests(unittest.TestCase):
    def test_duplicate_charge_is_high_priority_escalation(self):
        plan = triage("possible_duplicate_charge")
        self.assertEqual(plan.priority, "high")
        self.assertTrue(plan.escalate)

    def test_pending_payment_warns_against_second_payment(self):
        plan = triage("payment_pending")
        self.assertIn("do not ask the customer to pay again", plan.first_action)

    def test_usage_mismatch_collects_usage_window(self):
        self.assertIn("usage_window", triage("usage_mismatch").evidence)

    def test_ledger_mismatch_escalates(self):
        self.assertTrue(triage("ledger_mismatch").escalate)

    def test_unknown_case_is_not_silently_assumed(self):
        plan = triage("something_else")
        self.assertEqual(plan.category, "unclassified")
        self.assertTrue(plan.escalate)


if __name__ == "__main__":
    unittest.main()
