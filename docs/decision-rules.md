# Decision Rules

This document explains the routing rules used in the AI Business Loan Onboarding Portfolio project.

## Core principle

AI extracts facts from the business evidence.

Camunda applies deterministic routing rules.

Human reviewers handle uncertain, mismatched, or high-risk cases.

## Routing variable

The workflow gateway uses the variable:

`verificationRoute`

## Route values

| verificationRoute | Meaning | Workflow outcome |
|---|---|---|
| `CLEAN_CASE` | The submitted evidence appears consistent with the application and registry information. | Proceed to final review |
| `REQUEST_NEW_DOCUMENT` | The submitted document is expired, weak, unreadable, or insufficient. | Request a new document |
| `HUMAN_REVIEW` | The evidence is unclear or does not match the application details. | Send to human evidence review |
| `MANUAL_INVESTIGATION` | Registry information is missing, suspicious, or requires deeper investigation. | Send to manual investigation |

## Example rules

### Clean case

Use `CLEAN_CASE` when:

- The company name matches the application.
- The address matches the application or registry.
- The proof document is readable.
- There is no obvious mismatch or missing evidence.

### Request new document

Use `REQUEST_NEW_DOCUMENT` when:

- The document is expired.
- The document is unreadable.
- The document is not strong enough for verification.
- Required fields are missing.

### Human review

Use `HUMAN_REVIEW` when:

- The company name does not match.
- The address does not match.
- The AI extraction result is uncertain.
- The case requires human judgment.

### Manual investigation

Use `MANUAL_INVESTIGATION` when:

- Company registry information is missing.
- Company registry information conflicts with the application.
- The case appears higher risk.
- The workflow cannot safely continue without investigation.

## Why deterministic rules matter

Loan onboarding involves sensitive financial decisions. AI can support document review, but final routing should be controlled by deterministic workflow rules and human oversight.

This makes the process more auditable, explainable, and safer.