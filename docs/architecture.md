# Architecture

This project separates AI interpretation from workflow control.

## Main design principle

AI extracts. Workflow decides. Human reviews.

## Component roles

### Camunda

Camunda controls the business process, routing rules, gateway decisions, process state, and human review tasks.

### AI extraction agent

The AI extraction agent is responsible for reading business evidence and returning structured document information.

The AI does not approve or reject loan applications.

### Human reviewer

Human reviewers handle uncertain, mismatched, expired, or sensitive cases.

## Why this architecture matters

Loan onboarding involves sensitive business decisions. For that reason, AI should support the workflow but should not make uncontrolled final decisions.

This design keeps the process auditable, explainable, and safer.