# Billing API Diagnostics Toolkit

A decision aid for interpreting HTTP failures during billing and developer-support investigations.

## Demonstrates
- Separating authentication, authorization, validation, conflict, rate-limit, and server errors
- Preserving server-provided `Retry-After` values
- Considering HTTP method and idempotency keys before recommending retries
- Redacting credentials and session cookies from diagnostic headers

## Run
The Python implementation and unit tests are in the companion expansion pack. Run `python -m unittest discover -s tests -v` from the project directory.

This toolkit does not inspect a live API or guarantee that an operation is safe to retry. Confirm endpoint semantics and provider documentation before taking action.
