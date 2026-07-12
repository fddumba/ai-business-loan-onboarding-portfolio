# AI Guardrails

This document explains the guardrails used in the AI Business Loan Onboarding Portfolio project.

## Main principle

The AI system supports the workflow, but it does not control final business decisions.

The project follows this principle:

AI extracts. Workflow decides. Human reviews.

## What AI is allowed to do

The AI extraction agent may:

- Read business proof documents.
- Identify the document type.
- Extract company names.
- Extract business addresses.
- Extract document dates.
- Identify missing or unclear fields.
- Compare extracted information with application and registry details.
- Return structured JSON output.

## What AI is not allowed to do

The AI extraction agent must not:

- Approve a loan.
- Reject a loan.
- Make a final financial decision.
- Make an uncontrolled workflow routing decision.
- Invent missing document information.
- Ignore mismatches.
- Override human review requirements.

## Why these guardrails matter

Loan onboarding involves sensitive business and financial decisions.

If AI is allowed to make uncontrolled decisions, the process may become difficult to audit, explain, or challenge.

This project avoids that risk by separating responsibilities:

| Component | Responsibility |
|---|---|
| AI extraction agent | Extracts document facts |
| Camunda workflow | Applies routing logic |
| Human reviewer | Handles uncertain or high-risk cases |

## Human-in-the-loop control

Cases are routed to human review when:

- Evidence is mismatched.
- Evidence is unclear.
- Required fields are missing.
- The case requires judgment.
- The system cannot safely continue automatically.

## Safer AI design

This architecture makes the AI system:

- More explainable
- More auditable
- Easier to control
- Better suited for enterprise workflows
- Safer for sensitive onboarding decisions