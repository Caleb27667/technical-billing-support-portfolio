# Subscription Proration Engine

A small calculation exercise for subscription upgrades and downgrades during an active billing period.

## Demonstrates
- Signed upgrade charges and downgrade credits
- Timezone-aware billing-period boundaries
- Start-inclusive, end-exclusive period handling
- Decimal arithmetic and rounding to integer minor currency units
- Validation of invalid prices and timestamps

## Run
The Python implementation and tests are in the companion expansion pack. Run `python -m unittest discover -s tests -v` from the project directory.

This is an intentionally simplified model. Real billing systems may apply calendar-day rules, taxes, coupons, minimum charges, or provider-specific rounding. All sample amounts are fictional.
