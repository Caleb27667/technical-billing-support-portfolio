# Billing Reconciliation Lab

A fictional billing investigation exercise for comparing invoice totals, usage charges, credits, payments, and ledger entries.

## What it demonstrates

- Recalculating invoice totals from line items
- Detecting duplicate, missing, or mismatched payment records
- Distinguishing invoice balance from payment settlement
- Using SQL to investigate billing records
- Producing an evidence-based discrepancy report

## Run the Python example and tests

Requires Python 3.10+.

```bash
python -m unittest discover -s tests -v
python src/reconcile.py
```

The Python script uses only the standard library and seeded fictional records. No database server or credentials are needed.

## Run the SQL investigation

The sample schema and data are provided so the investigation queries can be reproduced locally with SQLite:

```bash
sqlite3 demo.db < sql/schema_and_sample_data.sql
sqlite3 demo.db < sql/investigations.sql
```

The sample data includes a line-item total mismatch, a repeated successful provider reference, a pending payment, and an unpaid invoice. The queries are read-only SELECT statements.

## Investigation rules

1. Sum invoice line items using integer minor currency units (for example, cents) to avoid floating-point rounding errors.
2. Compare the calculated total with the recorded invoice total.
3. Treat only confirmed successful payments as settled.
4. Compare the settled amount with the recorded invoice total.
5. Flag duplicate payment references and unexplained differences for review.

All records are synthetic and for learning purposes only.
