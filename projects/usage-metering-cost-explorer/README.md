# Usage Metering & Cost Explorer

A billing investigation exercise for aggregating usage events, applying included quotas, estimating overage, and identifying unusual daily usage changes.

## Demonstrates
- PostgreSQL usage-event aggregation by billing period
- Explicit UTC and half-open time windows
- Configurable plan allowances and fictional rate cards
- Integer minor-unit pricing and decimal-safe rounding
- Duplicate source-event and usage-spike investigation

## Run
The Python calculator, tests, PostgreSQL schema, seed data, and investigation queries are in the companion expansion pack. Run the Python tests with `python -m unittest discover -s tests -v`. Execute the SQL scripts in PostgreSQL or a local Supabase project.

All prices and records are fictional and are not Supabase's current rates.
