# LangFlow and Camunda Integration Design

This document explains how the AI extraction agent can integrate with the Camunda workflow in the AI Business Loan Onboarding Portfolio project.

## Integration goal

The goal is to connect AI-assisted document extraction with deterministic workflow routing.

The AI extraction agent reads business evidence and returns structured JSON.

Camunda receives the extracted evidence and applies workflow routing rules.

The main design principle remains:

AI extracts. Workflow decides. Human reviews.

## Component roles

| Component | Role |
|---|---|
| LangFlow / AI extraction agent | Reads business documents and returns structured JSON |
| Integration service | Sends document/application data to the AI agent and receives JSON output |
| Camunda | Stores workflow variables, applies routing rules, and controls the process |
| Human reviewer | Reviews mismatched, unclear, or higher-risk cases |

## Future integration flow

```text
Applicant submits business evidence
→ Camunda starts the onboarding workflow
→ Integration service sends application and document data to LangFlow
→ LangFlow returns structured JSON
→ Integration service maps AI output to Camunda variables
→ Camunda gateway applies routing rules
→ Case moves to final review, new document request, human review, or manual investigation