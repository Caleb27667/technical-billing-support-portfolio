import unittest

from src.reconcile import Invoice, LineItem, Payment, demo_invoice, reconcile


class ReconciliationTests(unittest.TestCase):
    def test_demo_invoice_calculates_and_counts_only_successful(self):
        result = reconcile(demo_invoice())
        self.assertEqual(result["calculated_total_minor"], 1299)
        self.assertEqual(result["settled_payment_minor"], 1299)
        self.assertEqual(result["outstanding_minor"], 0)
        self.assertEqual(result["status"], "paid")

    def test_invoice_mismatch_is_flagged(self):
        invoice = Invoice("I2", "USD", 900, (LineItem("Plan", 1000),), ())
        result = reconcile(invoice)
        self.assertFalse(result["invoice_total_matches"])
        self.assertEqual(result["status"], "review")

    def test_pending_payment_is_not_settled(self):
        invoice = Invoice(
            "I3", "USD", 500, (LineItem("Plan", 500),),
            (Payment("P1", 500, "pending"),),
        )
        self.assertEqual(reconcile(invoice)["settled_payment_minor"], 0)

    def test_duplicate_successful_reference_is_flagged(self):
        invoice = Invoice(
            "I4", "USD", 500, (LineItem("Plan", 500),),
            (
                Payment("P1", 250, "succeeded"),
                Payment("P1", 250, "succeeded"),
            ),
        )
        result = reconcile(invoice)
        self.assertEqual(result["duplicate_successful_payment_refs"], ["P1"])
        self.assertEqual(result["status"], "review")


if __name__ == "__main__":
    unittest.main()
