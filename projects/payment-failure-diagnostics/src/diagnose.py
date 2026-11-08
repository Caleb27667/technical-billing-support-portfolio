"""Classify synthetic payment failures and suggest safe support actions."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Diagnosis:
    category: str
    customer_action: bool
    retry_recommended: bool
    next_step: str


RULES = {
    "insufficient_funds": Diagnosis(
        "customer_action", True, False,
        "Ask the customer to check funds or use another payment method; do not auto-retry.",
    ),
    "authentication_required": Diagnosis(
        "authentication", True, False,
        "Direct the customer to complete authentication in the secure billing flow.",
    ),
    "invalid_payment_method": Diagnosis(
        "payment_method", True, False,
        "Ask the customer to update the payment method through the secure billing page.",
    ),
    "issuer_unavailable": Diagnosis(
        "transient_provider", False, True,
        "Verify the attempt state, then retry according to the provider's retry policy.",
    ),
    "rate_limited": Diagnosis(
        "transient_provider", False, False,
        "Wait for the provider's retry window; avoid repeated immediate attempts.",
    ),
    "unknown": Diagnosis(
        "needs_investigation", False, False,
        "Check provider details and final payment state before advising any retry.",
    ),
}


def diagnose(code: str) -> Diagnosis:
    return RULES.get(code.strip().lower(), RULES["unknown"])


if __name__ == "__main__":
    for code in (
        "insufficient_funds",
        "authentication_required",
        "issuer_unavailable",
        "mystery_error",
    ):
        print(code, "=>", diagnose(code))
