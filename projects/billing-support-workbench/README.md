# Billing Support Workbench

A lightweight case-triage workflow using fictional support tickets. It models the first steps of a technical billing support investigation: categorise the issue, identify evidence to collect, and decide whether specialist escalation is appropriate.

## What it demonstrates

- Consistent case classification and priority
- Evidence checklists tailored to the reported symptom
- Escalation triggers for data inconsistencies and duplicate-charge concerns
- Clear separation between verified facts and customer-reported symptoms

## Run

```bash
python -m unittest discover -s tests -v
python src/workbench.py
```

## Workflow

1. Read the customer's reported symptom.
2. Classify the issue and identify affected records.
3. Gather the minimum evidence required.
4. Avoid risky actions such as blind retries or unverified refunds.
5. Escalate record inconsistencies with identifiers and timestamps.
6. Send a factual update and document the next step.
