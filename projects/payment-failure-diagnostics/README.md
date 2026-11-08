# Payment Failure Diagnostics

A compact triage rules engine for classifying fictional payment outcomes and identifying safe support actions.

## What it demonstrates

- Separating actionable customer errors from temporary provider failures
- Recognising authentication and payment-method update requirements
- Avoiding unsafe retry advice
- Producing consistent, customer-friendly next steps
- Testing edge cases with Python's standard library

## Run

```bash
python -m unittest discover -s tests -v
python src/diagnose.py
```

No API keys, real payment gateway, or customer data are used.

## Important safety principle

A support agent should not infer retry safety from a vague error message alone. Verify the provider's final state and the payment attempt identifier first. Never ask a customer to send full card details, CVV, password, or one-time authentication code through support chat.
