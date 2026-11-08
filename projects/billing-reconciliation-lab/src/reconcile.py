"""Reconcile fictional invoices and payments using integer minor currency units."""
from dataclasses import dataclass
from collections import Counter


@dataclass(frozen=True)
class LineItem:
    description: str
    amount_minor: int


@dataclass(frozen=True)
class Payment:
    reference: str
    amount_minor: int
    status: str


@dataclass(frozen=True)
class Invoice:
    invoice_id: str
    currency: str
    total_minor: int
    lines: tuple[LineItem, ...]
    payments: tuple[Payment, ...]


def reconcile(invoice: Invoice) -> dict:
    calculated = sum(item.amount_minor for item in invoice.lines)
    successful = [p for p in invoice.payments if p.status == "succeeded"]
    paid = sum(p.amount_minor for p in successful)
    refs = [p.reference for p in successful]
    duplicates = sorted(ref for ref, count in Counter(refs).items() if count > 1)
    return {
        "invoice_id": invoice.invoice_id,
        "currency": invoice.currency,
        "calculated_total_minor": calculated,
        "recorded_total_minor": invoice.total_minor,
        "invoice_total_matches": calculated == invoice.total_minor,
        "settled_payment_minor": paid,
        "outstanding_minor": invoice.total_minor - paid,
        "duplicate_successful_payment_refs": duplicates,
        "status": "review" if calculated != invoice.total_minor or duplicates else (
            "paid" if paid >= invoice.total_minor else "payment_outstanding"
        ),
    }


def demo_invoice() -> Invoice:
    return Invoice(
        invoice_id="INV-DEMO-1001",
        currency="USD",
        total_minor=1299,
        lines=(
            LineItem("Subscription", 1000),
            LineItem("Usage", 499),
            LineItem("Credit", -200),
        ),
        payments=(
            Payment("PAY-DEMO-A", 1299, "succeeded"),
            Payment("PAY-DEMO-B", 1299, "pending"),
        ),
    )


if __name__ == "__main__":
    from pprint import pprint
    pprint(reconcile(demo_invoice()))
