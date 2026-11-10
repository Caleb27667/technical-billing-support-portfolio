# Webhook Reliability & Replay Lab

A support-focused lab for investigating signed webhook delivery, duplicate events, late arrivals, and transient failures.

## Demonstrates
- HMAC-SHA256 signature verification against the raw request body
- Timestamp tolerance and replay rejection
- Idempotent event handling using a unique provider event ID
- Bounded exponential retry backoff
- A Supabase Edge Function receiver and PostgreSQL event table

## Run
The Python reference implementation and unit tests are in the companion expansion pack. Run `python -m unittest discover -s tests -v` from the project directory. The Edge Function requires a local Supabase project and server-side secrets; never expose a service-role key to a browser or commit credentials.

All events and payloads are synthetic. This is a learning implementation, not a production-ready universal webhook gateway.
