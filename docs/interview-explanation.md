# Interview Explanation

This document provides a short explanation of the AI Business Loan Onboarding Portfolio project for interviews, resumes, and LinkedIn discussions.

## 30-second explanation

I built an AI-assisted business loan onboarding workflow using Camunda. The project shows how AI can support document verification while keeping final decision control inside a deterministic workflow. The system separates AI extraction, workflow routing, and human review to make the process safer, auditable, and easier to explain.

## 60-second explanation

This project models a business loan onboarding process where an applicant submits business evidence for verification.

The workflow was built in Camunda and includes four routing outcomes: clean case, request new document, human evidence review, and manual investigation.

The core design principle is:

AI extracts. Workflow decides. Human reviews.

The AI extraction agent is responsible for reading business documents and returning structured outputs such as document type, company name, address, document date, and match indicators.

Camunda is responsible for applying deterministic routing rules using the `verificationRoute` variable.

Human reviewers handle mismatched, unclear, or higher-risk cases.

I tested all four workflow paths and documented the evidence using screenshots, test data, workflow files, form files, AI guardrails, decision rules, and sample AI output.

## What the project demonstrates

This project demonstrates:

- Business process modeling with Camunda
- Human-in-the-loop workflow design
- Responsible AI architecture
- Workflow routing using variables
- Documentation of test evidence
- AI prompt design
- Structured JSON output design
- GitHub repository organization

## Why this project matters

Many organizations want to use AI in business processes, but they need control, auditability, and human oversight.

This project shows how AI can be introduced into a sensitive process like loan onboarding without giving the model uncontrolled decision-making power.

The architecture keeps AI in a support role and keeps final process control inside the workflow.

## Technical components

| Component | Role |
|---|---|
| Camunda | Workflow orchestration, routing, process state, human review |
| AI extraction agent | Document interpretation and structured extraction |
| Human reviewer | Handles uncertain or mismatched evidence |
| Test data | Validates routing scenarios |
| GitHub documentation | Makes the project explainable and reviewable |

## Interview talking points

If asked what I built:

I built a controlled AI-assisted loan onboarding workflow using Camunda, with documented routing rules, human review, AI guardrails, sample AI outputs, and GitHub evidence.

If asked why AI does not make the final decision:

Because loan onboarding involves sensitive financial decisions. The AI extracts evidence, but deterministic workflow rules and human reviewers control the final routing.

If asked what I would improve next:

The next improvement is to connect the AI extraction agent through an API so that extracted JSON outputs can automatically become Camunda workflow variables.

## Next improvement path

Future improvements include:

- Connecting LangFlow or an AI extraction API to Camunda
- Adding FastAPI as an integration service
- Persisting applications and verification results in PostgreSQL
- Adding applicant upload forms
- Adding automated tests
- Adding logging and error handling
- Deploying the solution as a documented demo
