# FastAPI Integration Service Prototype

This folder contains a prototype API service for the AI Business Loan Onboarding Portfolio project.

## Purpose

The service acts as a bridge between AI extraction output and Camunda workflow variables.

It receives structured AI extraction JSON, validates the fields, maps `workflow_signal` to `verificationRoute`, and returns clean variables that can be passed into Camunda.

## Design principle

AI extracts. Workflow decides. Human reviews.

## Endpoint

```text
POST /map-to-camunda-variables
```

## Run locally

From inside the `api-service` folder, run:

```bash
python -m uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Run automated tests

This service includes automated tests for the workflow signal mapping logic.

Run tests from inside the `api-service` folder:

```bash
python -m pytest
```

Expected result:

```text
5 passed
```

The tests confirm that:

| Test case | workflow_signal | Expected verificationRoute |
|---|---|---|
| APP-001 | `DOCUMENT_EXPIRED_OR_WEAK` | `REQUEST_NEW_DOCUMENT` |
| APP-002 | `MISMATCH_REQUIRES_REVIEW` | `HUMAN_REVIEW` |
| APP-003 | `EVIDENCE_MATCHED` | `CLEAN_CASE` |
| APP-004 | `REGISTRY_REQUIRES_INVESTIGATION` | `MANUAL_INVESTIGATION` |
| Unsupported signal | `UNKNOWN_SIGNAL` | 400 error |

## Current status

The API service prototype validates AI extraction output, maps workflow signals to Camunda routes, and includes automated tests for all four workflow outcomes plus unsupported signal handling.

