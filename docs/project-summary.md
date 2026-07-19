# Project Summary

## Project name

AI Business Loan Onboarding Portfolio

## One-line summary

A controlled AI-assisted business loan onboarding workflow that uses Camunda for process control, FastAPI for integration logic, and AI extraction outputs for document verification support.

## Project purpose

This project demonstrates how AI can be safely introduced into a sensitive business workflow without giving the AI system uncontrolled decision-making authority.

The workflow models a business loan onboarding process where applicant evidence is reviewed, validated, routed, and escalated when necessary.

The core design principle is:

AI extracts. Workflow decides. Human reviews.

## Problem addressed

Business loan onboarding often requires reviewing documents, checking company information, handling mismatches, and deciding whether a case should proceed, pause, or be escalated.

A weak AI implementation might allow the model to approve, reject, or route applications directly.

This project avoids that risk by separating responsibilities across AI extraction, API validation, workflow routing, and human review.

## What I built

This project includes:

- A Camunda BPMN workflow for loan onboarding
- Four tested workflow routes
- A human evidence review form
- AI guardrails and decision rules
- Sample AI extraction outputs
- A FastAPI mapping service
- Pydantic validation
- Automated pytest tests
- Docker support for the API service
- A Camunda integration contract
- A Mermaid architecture diagram
- GitHub documentation and screenshots

## Workflow routes tested

| Scenario | Signal | Camunda route |
|---|---|---|
| Clean evidence | `EVIDENCE_MATCHED` | `CLEAN_CASE` |
| Weak or expired document | `DOCUMENT_EXPIRED_OR_WEAK` | `REQUEST_NEW_DOCUMENT` |
| Mismatched evidence | `MISMATCH_REQUIRES_REVIEW` | `HUMAN_REVIEW` |
| Registry issue | `REGISTRY_REQUIRES_INVESTIGATION` | `MANUAL_INVESTIGATION` |

## Architecture

The project follows this flow:

```text
Applicant evidence
→ AI extraction output
→ FastAPI validation and mapping
→ Camunda workflow variables
→ BPMN gateway routing
→ final review, document request, human review, or manual investigation
