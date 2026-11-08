"""Rule-based triage for fictional technical billing support cases."""
from dataclasses import dataclass


@dataclass(frozen=True)
class CasePlan:
    category: str
    priority: str
    evidence: tuple[str, ...]
    escalate: bool
    first_action: str


PLANS = {
    "unexpected_invoice": CasePlan(
        "invoice_query", "normal",
        ("invoice_id", "line_items", "billing_period", "subscription_plan"),
        False,
        "Recalculate the invoice from its line items and explain the total.",
    ),
    "payment_pending": CasePlan(
        "payment_status", "normal",
        ("payment_attempt_id", "provider_status", "created_at", "currency", "amount"),
        False,
        "Verify final provider state; do not ask the customer to pay again while pending.",
    ),
    "possible_duplicate_charge": CasePlan(
        "duplicate_charge", "high",
        ("payment_attempt_ids", "provider_references", "timestamps", "settlement_status"),
        True,
        "Preserve evidence and escalate; do not promise a reversal before confirmation.",
    ),
    "usage_mismatch": CasePlan(
        "usage_query", "normal",
        ("project_id", "usage_metric", "usage_window", "aggregation", "invoice_line_item"),
        False,
        "Compare the usage window and aggregation with the billed line item.",
    ),
    "ledger_mismatch": CasePlan(
        "data_integrity", "high",
        ("invoice_id", "ledger_entries", "payment_references", "timestamps"),
        True,
        "Escalate the inconsistent records with a concise evidence summary.",
    ),
}


def triage(issue: str) -> CasePlan:
    return PLANS.get(
        issue.strip().lower(),
        CasePlan(
            "unclassified", "normal",
            ("customer_summary", "affected_resource", "timestamps"),
            True,
            "Clarify the symptom and gather evidence before taking billing action.",
        ),
    )


if __name__ == "__main__":
    for issue in (
        "unexpected_invoice",
        "possible_duplicate_charge",
        "payment_pending",
        "unknown",
    ):
        print(f"\n{issue}:\n{triage(issue)}")
