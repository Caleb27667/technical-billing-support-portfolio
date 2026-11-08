import unittest

from src.diagnose import diagnose


class DiagnosisTests(unittest.TestCase):
    def test_insufficient_funds_needs_customer_action(self):
        diagnosis = diagnose("insufficient_funds")
        self.assertTrue(diagnosis.customer_action)
        self.assertFalse(diagnosis.retry_recommended)

    def test_authentication_is_not_auto_retried(self):
        diagnosis = diagnose("authentication_required")
        self.assertEqual(diagnosis.category, "authentication")
        self.assertFalse(diagnosis.retry_recommended)

    def test_transient_provider_error_has_controlled_retry(self):
        diagnosis = diagnose("issuer_unavailable")
        self.assertTrue(diagnosis.retry_recommended)

    def test_rate_limit_does_not_immediately_retry(self):
        self.assertFalse(diagnose("rate_limited").retry_recommended)

    def test_unknown_error_is_escalated_for_investigation(self):
        diagnosis = diagnose("not_a_real_code")
        self.assertEqual(diagnosis.category, "needs_investigation")
        self.assertFalse(diagnosis.retry_recommended)


if __name__ == "__main__":
    unittest.main()
