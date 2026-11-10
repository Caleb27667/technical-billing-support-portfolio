# PostgreSQL Billing Investigation Pack

A set of PostgreSQL investigation exercises for tracing a support case across projects, subscriptions, usage events, invoices, payment attempts, and webhook deliveries.

## Demonstrates
- Joining billing records across related tables
- Recalculating invoice lines and reconciling totals
- Distinguishing pending, failed, and settled payment attempts
- Using explicit half-open time windows to avoid double counting
- Investigating webhook delivery history and duplicate events

## Run
The schema, synthetic seed data, and investigation queries are in the companion expansion pack. Execute the schema first, then the seed data, then selected sections of the investigation queries in PostgreSQL or the Supabase SQL Editor.

All records are fictional. Never use real customer secrets, card data, or sensitive payloads in a portfolio database.
