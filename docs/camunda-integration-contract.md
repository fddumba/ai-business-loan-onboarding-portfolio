# Camunda Integration Contract

This document explains how the FastAPI integration service connects AI extraction output to the Camunda workflow in the AI Business Loan Onboarding Portfolio project.

## Integration goal

The goal is to convert structured AI extraction output into Camunda-ready workflow variables.

The integration follows this flow:

```text
LangFlow AI extraction output
→ FastAPI validation and mapping
→ Camunda workflow variables
→ BPMN gateway routing
→ human or automated workflow path
```

## Design principle

AI extracts. Workflow decides. Human reviews.

The AI agent does not approve or reject applications. It extracts evidence and produces a controlled `workflow_signal`.

The FastAPI service validates the AI output and maps `workflow_signal` to the Camunda variable `verificationRoute`.

Camunda uses `verificationRoute` to control the BPMN exclusive gateway.

## Input contract

The FastAPI service expects structured JSON from the AI extraction layer.

Example input:

```json
{
  "application_id": "APP-002",
  "document_readable": true,
  "document_type": "Utility bill",
  "company_name_extracted": "Green Valley Trading Ltd",
  "address_extracted": "72 Industrial Way",
  "document_date": "2026-06-18",
  "company_name_match": false,
  "address_match": false,
  "missing_or_unclear_fields": [],
  "extraction_summary": "The document is readable, but the extracted company name and address do not match the application and registry details.",
  "workflow_signal": "MISMATCH_REQUIRES_REVIEW"
}
```

## Output contract

The FastAPI service returns Camunda-ready variables.

Example output:

```json
{
  "applicationId": "APP-002",
  "documentReadable": true,
  "documentType": "Utility bill",
  "extractedCompanyName": "Green Valley Trading Ltd",
  "extractedAddress": "72 Industrial Way",
  "documentDate": "2026-06-18",
  "companyNameMatch": false,
  "addressMatch": false,
  "missingOrUnclearFields": [],
  "aiExtractionSummary": "The document is readable, but the extracted company name and address do not match the application and registry details.",
  "workflowSignal": "MISMATCH_REQUIRES_REVIEW",
  "verificationRoute": "HUMAN_REVIEW"
}
```

## Signal-to-route mapping

| workflow_signal | Camunda verificationRoute | Meaning |
|---|---|---|
| `EVIDENCE_MATCHED` | `CLEAN_CASE` | Evidence matches application and registry details |
| `DOCUMENT_EXPIRED_OR_WEAK` | `REQUEST_NEW_DOCUMENT` | Document is readable but outdated, weak, or insufficient |
| `MISMATCH_REQUIRES_REVIEW` | `HUMAN_REVIEW` | Evidence mismatch requires human review |
| `REGISTRY_REQUIRES_INVESTIGATION` | `MANUAL_INVESTIGATION` | Registry issue requires manual investigation |

## Camunda BPMN gateway contract

The BPMN exclusive gateway uses the variable:

```text
verificationRoute
```

Expected route values:

```text
CLEAN_CASE
REQUEST_NEW_DOCUMENT
HUMAN_REVIEW
MANUAL_INVESTIGATION
```

The gateway routes the application as follows:

| verificationRoute | BPMN path |
|---|---|
| `CLEAN_CASE` | Proceed to final review |
| `REQUEST_NEW_DOCUMENT` | Request new document from applicant |
| `HUMAN_REVIEW` | Send evidence to human reviewer |
| `MANUAL_INVESTIGATION` | Send application to manual investigation |

## Error handling

If the FastAPI service receives an unsupported `workflow_signal`, it returns an error instead of guessing a route.

Example unsupported signal:

```json
{
  "workflow_signal": "UNKNOWN_SIGNAL"
}
```

Expected result:

```text
400 error
```

This prevents unclear AI outputs from silently entering the workflow.

## Why this contract matters

This contract separates AI interpretation from workflow control.

The AI layer extracts facts and provides a controlled signal.

The FastAPI layer validates and maps that signal.

The Camunda layer controls the process route.

This reduces risk because sensitive business decisions are handled by explicit workflow logic rather than uncontrolled AI reasoning.

## Current implementation status

Implemented:

- FastAPI mapping service
- Pydantic validation
- Signal-to-route mapping
- Sample request JSON files
- Automated pytest coverage
- Docker support for the API service

Future improvement:

- Replace manual API testing with a live Camunda service-task integration
- Add authentication for API calls
- Store request and response logs
- Add monitoring for latency, errors, and cost