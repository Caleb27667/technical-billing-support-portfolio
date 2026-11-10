# Billing Issue Reproduction & Regression Suite

A fixture-driven test exercise that turns support findings into repeatable checks.

## Demonstrates
- Invoice arithmetic and reconciliation checks
- Settled-payment totals that exclude pending attempts
- Webhook event uniqueness
- Usage-window aggregation and timestamp validation
- Preserving failing examples to verify fixes

## Run
The runner, JSON fixtures, and tests are in the companion expansion pack. Run `python -m unittest discover -s tests -v`, then `python src/regression_runner.py fixtures/cases.json`.

The sample data is synthetic. The runner does not modify billing data or call an external payment provider.
