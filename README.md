# Technical Billing Support Portfolio

![Portfolio tests](https://github.com/Caleb27667/-technical-billing-support-portfolio/actions/workflows/tests.yml/badge.svg?branch=main)

Independent, hands-on case studies demonstrating technical billing support, payment troubleshooting, reconciliation, SQL investigation, Python testing, and customer communication.

> These are original portfolio exercises using synthetic data. They are not Supabase internal tools, production systems, or representations of private customer data.

## Projects

### 1. [Billing Reconciliation Lab](./projects/billing-reconciliation-lab/)
Recalculate invoice totals, compare payment records, identify duplicate references, and investigate billing discrepancies with Python and SQLite.

### 2. [Payment Failure Diagnostics](./projects/payment-failure-diagnostics/)
Classify payment failures, distinguish customer-actionable errors from transient provider issues, and select safe support next steps.

### 3. [Billing Support Workbench](./projects/billing-support-workbench/)
Triage billing cases, gather targeted evidence, identify escalation triggers, and document a clear first action.

## Investigation workflow demonstrated

1. Understand the customer's reported symptom and define the expected outcome.
2. Gather relevant invoice, subscription, usage, payment, and ledger evidence.
3. Recalculate or query the underlying records rather than guessing.
4. Separate verified facts from hypotheses.
5. Choose a safe next step, avoiding blind retries or unverified adjustments.
6. Explain the findings in plain language and escalate with useful evidence when needed.

## Skills demonstrated

- Billing and invoice investigation
- Subscription and usage-based billing concepts
- Payment failure triage and retry safety
- SQL querying and data validation
- Python scripting and automated tests
- Customer communication and case documentation
- Escalation judgement and evidence collection

## Automated checks

GitHub Actions runs the unit tests for all three projects on pushes to `main` and pull requests. The current suite contains 14 tests across the three projects.

## Getting started

Each project has its own README with setup instructions and examples. Requires Python 3.10+; the code uses only the Python standard library. The SQL exercise uses SQLite. No paid services, API keys, or credentials are required.

## Scope and integrity

All customers, project identifiers, invoice values, payment references, and provider outcomes are fictional. These projects are demonstrations of investigation methods and support judgement, not claims of access to Supabase systems or prior work inside Supabase.

---
*Independent technical billing support portfolio.*
