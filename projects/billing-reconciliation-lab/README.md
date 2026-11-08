# Billing Reconciliation Lab

A fictional billing investigation exercise for comparing invoice totals, usage charges, credits, payments, and ledger entries.

## What it demonstrates

- Recalculating invoice totals from line items
- Detecting duplicate, missing, or mismatched payment records
- Distinguishing invoice balance from payment settlement
- Using SQL to investigate billing records
- Producing an evidence-based discrepancy report

## Run

Requires Python 3.10+.

```bash
python -m unittest discover -s tests -v
python src/reconcile.py
```

The script uses only Python's standard library and seeded fictional records. No database server or credentials are needed.

## Investigation rules

1. Sum invoice line items using integer minor currency units (for example, cents) to avoid floating-point rounding errors.
2. Compare the calculated total with the recorded invoice total.
3. Treat only confirmed successful payments as settled.
4. Compare the settled amount with the invoice amount after credits and adjustments.
5. Flag duplicate payment references and unexplained differences for review.

## SQL

See `sql/investigations.sql` for SQLite queries that locate invoice discrepancies, unmatched payments, and duplicate provider references.
