# Architecture Diagram

This document provides a visual overview of the AI Business Loan Onboarding Portfolio project.

## System architecture

```mermaid
flowchart LR
    A[Applicant submits business evidence] --> B[LangFlow AI extraction agent]

    B --> C[Structured AI extraction JSON]

    C --> D[FastAPI integration service]

    D --> E[Pydantic validation]

    E --> F[workflow_signal to verificationRoute mapping]

    F --> G[Camunda workflow variables]

    G --> H[Camunda BPMN exclusive gateway]

    H --> I[Clean case: Proceed to final review]
    H --> J[Weak or expired document: Request new document]
    H --> K[Mismatched evidence: Human evidence review]
    H --> L[Registry issue: Manual investigation]

    K --> M[Human reviewer decision]
```

## Responsibility separation

| Component | Responsibility |
|---|---|
| Applicant | Submits business evidence |
| LangFlow AI extraction agent | Extracts facts from the document |
| FastAPI integration service | Validates JSON and maps signals |
| Camunda | Controls workflow routing |
| Human reviewer | Handles uncertain or mismatched evidence |

## Core design principle

AI extracts. Workflow decides. Human reviews.

## Why this architecture matters

This architecture prevents AI from making uncontrolled business decisions.

The AI layer produces structured evidence.

The FastAPI layer validates and maps the evidence.

Camunda controls the workflow route.

Human reviewers handle sensitive or uncertain cases.