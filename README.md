# AI Business Loan Onboarding Portfolio

This project demonstrates a controlled AI-assisted business loan onboarding workflow using Camunda as the workflow control system.

The project shows how AI can support document verification while keeping final process control inside deterministic workflow rules and human review. It is designed as a production-minded portfolio project for enterprise AI integration, business process automation, and human-in-the-loop decision support.

## What this project demonstrates

This project demonstrates:

- Business process modeling with Camunda
- AI-assisted document verification design
- Human-in-the-loop workflow control
- Deterministic routing rules for sensitive decisions
- Responsible AI guardrails
- Structured JSON output design
- Test evidence documentation
- GitHub-ready project organization
- Interview-ready technical explanation

## Tech stack

| Area | Tool or artifact |
|---|---|
| Workflow orchestration | Camunda |
| Workflow model | BPMN 2.0 |
| Human review | Camunda Tasklist form |
| AI extraction design | Prompt-based document extraction agent |
| Structured output | JSON |
| Test data | CSV |
| Documentation | Markdown |
| Version control / portfolio | GitHub |

## Project goal

The goal is to show how AI can support document verification without allowing AI to make uncontrolled final decisions.

The design principle is:

**AI extracts. Workflow decides. Human reviews.**

## Workflow summary

The process starts when a business loan application is submitted. The workflow then:

1. Receives the loan application.
2. Creates a traceable application record.
3. Checks company registry details.
4. Analyzes the proof document with AI.
5. Applies deterministic verification routing rules.
6. Sends the application to one of four outcomes:
   - Proceed to final review
   - Request a new document
   - Human evidence review
   - Manual investigation

   ## Repository structure

```text
ai-business-loan-onboarding-portfolio/
├── README.md
├── api-service/
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
├── data/
│   └── test-cases.csv
├── docs/
│   ├── ai-guardrails.md
    ├── architecture-diagram.md
│   ├── architecture.md
│   ├── decision-rules.md
│   ├── interview-explanation.md
│   ├── interview-questions-and-answers.md
│   ├── langflow-camunda-integration.md
│   └── test-summary.md
├── forms/
│   └── human-evidence-review-form.json
├── outputs/
│   ├── sample-extraction-output-app-001.json
│   ├── sample-extraction-output-app-002.json
│   ├── sample-extraction-output-app-003.json
│   └── sample-extraction-output-app-004.json
├── prompts/
│   └── document-extraction-agent-prompt.md
├── screenshots/
│   └── workflow, test, and FastAPI mapping evidence screenshots
└── workflows/
    └── ai-loan-onboarding-workflow.bpmn
```
## Routing logic

The gateway uses the variable `verificationRoute`.

Tested route values:

| verificationRoute | Expected route |
|---|---|
| `CLEAN_CASE` | Proceed to final review |
| `REQUEST_NEW_DOCUMENT` | Request new document |
| `HUMAN_REVIEW` | Human evidence review |
| `MANUAL_INVESTIGATION` | Manual investigation |

## Test evidence

All four workflow routes were tested successfully in Camunda Operate using manual test variables.

## Completed workflow tests

The workflow routing logic was tested in Camunda Operate using four controlled test cases.

| Test case | Route value | Expected outcome | Result |
|---|---|---|---|
| APP-003 clean case | `CLEAN_CASE` | Proceed to final review | Passed |
| APP-001 weak document | `REQUEST_NEW_DOCUMENT` | Waiting for new document | Passed |
| APP-002 mismatch case | `HUMAN_REVIEW` | Evidence sent for human review | Passed |
| APP-004 registry issue | `MANUAL_INVESTIGATION` | Manual investigation required | Passed |

These tests confirm that the workflow gateway correctly routes applications based on the `verificationRoute` variable.

## Screenshots

### Full BPMN workflow

![Full BPMN workflow](screenshots/01-bpmn-full-workflow.png)

### Clean case route

![Clean case route](screenshots/02-clean-case-route.png)

### Request new document route

![Request new document route](screenshots/03-request-new-document-route.png)

### Human review route in Tasklist

![Human review route in Tasklist](screenshots/04-human-review-route-tasklist.png)

### Manual investigation route

![Manual investigation route](screenshots/05-manual-investigation-route.png)

### Operate variables

![Operate variables](screenshots/06-operate-variables.png)

### README preview

![README preview](screenshots/07-readme-preview.png)

### Process version success

![Process version success](screenshots/08-process-version-success.png)

## Architecture idea

Camunda acts as the workflow brain: it controls routing, auditability, and process state.

AI acts as the extraction and interpretation brain: it reads business evidence and returns structured outputs.

Human reviewers handle uncertain, sensitive, or high-risk cases.

## Version history

| Version | Milestone | What was added |
|---|---|---|
| Version 1 | Camunda workflow evidence | Built the BPMN workflow, tested routing paths, captured screenshots, and uploaded the first GitHub version. |
| Version 2 | AI documentation and sample output | Added AI guardrails, decision rules, test summary, extraction prompt, and sample AI output. |
| Version 3 | Interview readiness | Added interview explanation and interview Q&A documentation. |
| Version 4 | README polish | Improved the project overview, tech stack, and recruiter-facing explanation. |
| Version 5 | LangFlow/Camunda integration design | Added integration design documentation and sample AI outputs for all four workflow routes. |
| Version 6 | FastAPI mapping service prototype | Added a FastAPI service that validates AI extraction JSON and maps `workflow_signal` to Camunda `verificationRoute`. |
| Version 7 | API service testing and polish | Added reusable sample request files, automated pytest coverage, API service documentation, updated requirements, and `.gitignore` for cleaner repository management.
| Version 8 | Docker support for FastAPI service | Added Dockerfile and `.dockerignore` for the FastAPI service so the API can be packaged and run in a clean, repeatable container environment.
| Version 9 | Camunda integration contract | Added a contract document explaining how FastAPI output maps into Camunda workflow variables and controls the BPMN gateway through `verificationRoute`. |
| Version 10 | Architecture diagram | Added a Mermaid architecture diagram showing how LangFlow, FastAPI, Camunda, workflow routing, and human review connect. |

## Current version

## Current version

Current version: `v10-architecture-diagram`

This version adds a visual architecture diagram showing how the AI extraction layer, FastAPI integration service, and Camunda workflow connect.

The current build now communicates the system visually:

```text
Applicant evidence
→ LangFlow AI extraction
→ FastAPI validation and mapping
→ Camunda workflow variables
→ BPMN gateway routing
→ final review, document request, human review, or manual investigation
```

This makes the project easier to understand for recruiters, technical reviewers, and interviewers.

## Future improvements

Future versions can add:

- LangFlow live API connection
- Camunda variable update integration
- Database or CRM case creation
- Applicant document upload form
- Email or portal notifications
- Dockerized API service
- Deployment to Azure
  