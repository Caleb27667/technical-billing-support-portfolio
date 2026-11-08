# Billing Investigation Playbook

A repeatable workflow for diagnosing billing questions without jumping to conclusions.

## 1. Establish the reported symptom

Capture the customer's exact description, affected project or account, relevant invoice/payment identifiers, amount, currency, and dates including timezone. Avoid asking for full card numbers, passwords, one-time codes, or other secrets.

## 2. Define the expected result

Identify the subscription plan, billing interval, usage period, applicable tax, discount or credit, payment method status, and any recent plan or project changes. State the expected amount or state and the rule used to calculate it.

## 3. Gather evidence

Use the smallest useful set of records:
- Invoice and invoice line items
- Subscription state and billing period
- Usage records and aggregation window
- Credits, adjustments, taxes, and discounts
- Payment attempts and provider response category
- Ledger or reconciliation entries

Record the source, timestamp, and identifier for each observation. Distinguish verified facts from hypotheses.

## 4. Reconcile

Recalculate totals independently. Confirm units, currency, sign conventions, rounding, time boundaries, and whether a record is pending, succeeded, failed, refunded, or voided. Never count a pending payment as settled cash.

## 5. Choose a safe next action

- Retry only when the failure category and provider state make retry safe.
- Do not create a second charge to test whether a first payment worked.
- Do not advise repeated retries for authentication or invalid payment details.
- Escalate suspected duplicate charges, inconsistent ledger states, unexplained adjustments, or data-integrity problems with evidence.

## 6. Communicate

Explain what was checked, what the records show, what remains uncertain, and the next action. Avoid blame and do not promise a refund, reversal, or resolution until it is confirmed.

## 7. Close the loop

Document the root cause, action, confirmation reference, customer update, and any follow-up required. Remove unnecessary personal data from notes and screenshots.
