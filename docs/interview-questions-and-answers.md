# Interview Questions and Answers

This document contains interview-style questions and answers for the AI Business Loan Onboarding Portfolio project.

## 1. What did you build?

I built an AI-assisted business loan onboarding workflow using Camunda.

The project models how a business loan application can move through document verification, company registry checks, routing rules, human review, and final review.

The goal was to show how AI can support document verification without giving the AI uncontrolled decision-making power.

## 2. What problem does this project solve?

The project addresses the problem of safely using AI in a sensitive business process.

Loan onboarding often requires document review, company verification, and judgment about mismatched or incomplete evidence.

Instead of allowing AI to approve or reject applications directly, this project separates responsibilities:

AI extracts. Workflow decides. Human reviews.

## 3. Why did you use Camunda?

I used Camunda because it is designed for workflow orchestration and business process automation.

Camunda makes it possible to model the process, control routing decisions, manage process state, and include human review tasks.

This is useful in enterprise environments where decisions must be auditable, explainable, and controlled.

## 4. What role does AI play in the project?

The AI extraction agent reads business evidence and returns structured information.

For example, it can extract:

- Document type
- Company name
- Business address
- Document date
- Whether the company name matches
- Whether the address matches
- Missing or unclear fields

The AI does not approve loans, reject loans, or make final routing decisions.

## 5. Why does the AI not make the final decision?

The AI does not make the final decision because loan onboarding involves sensitive financial decisions.

If AI makes uncontrolled decisions, the process becomes harder to audit, explain, and challenge.

In this project, AI provides structured evidence, while Camunda applies deterministic rules and humans review uncertain cases.

## 6. What is the main design principle?

The main design principle is:

AI extracts. Workflow decides. Human reviews.

This means AI supports the workflow, but the workflow engine and human reviewers remain responsible for control and judgment.

## 7. What is the `verificationRoute` variable?

`verificationRoute` is the workflow variable used by the Camunda gateway to route the application.

The tested route values are:

| verificationRoute | Outcome |
|---|---|
| `CLEAN_CASE` | Proceed to final review |
| `REQUEST_NEW_DOCUMENT` | Request a new document |
| `HUMAN_REVIEW` | Send to human evidence review |
| `MANUAL_INVESTIGATION` | Send to manual investigation |

## 8. What workflow paths did you test?

I tested four workflow paths:

| Test case | Route | Result |
|---|---|---|
| APP-003 clean case | `CLEAN_CASE` | Passed |
| APP-001 weak document | `REQUEST_NEW_DOCUMENT` | Passed |
| APP-002 mismatch case | `HUMAN_REVIEW` | Passed |
| APP-004 registry issue | `MANUAL_INVESTIGATION` | Passed |

All four routes worked successfully.

## 9. What happens when evidence does not match?

When evidence does not match, the workflow routes the case to human review.

For example, if the company name or address extracted from the document does not match the application or registry details, the case should not proceed automatically.

A human reviewer inspects the evidence and decides the next action.

## 10. What happens when the document is weak or expired?

When the document is weak, expired, unreadable, or insufficient, the workflow routes the case to request a new document.

This keeps the process controlled and prevents poor-quality evidence from being accepted automatically.

## 11. What happens when there is a registry issue?

If company registry information is missing, conflicting, or suspicious, the workflow sends the case to manual investigation.

This is important because registry issues may require deeper review before the application can continue.

## 12. What is the human-in-the-loop part of the project?

The human-in-the-loop part is the human evidence review task.

This task allows a reviewer to inspect uncertain or mismatched evidence and make a controlled decision.

This prevents the AI system from making sensitive decisions alone.

## 13. What evidence proves the workflow works?

The repository includes:

- BPMN workflow file
- Human review form JSON
- Test cases CSV
- Screenshots of all workflow routes
- Operate variables screenshot
- Process version screenshot
- README documentation
- Decision rules
- AI guardrails
- Sample AI extraction output

## 14. What is the sample AI output used for?

The sample AI output shows the type of structured JSON the AI extraction agent is expected to return.

For example, the APP-002 output shows a readable document where the extracted company name and address do not match the application details.

The output includes a workflow signal:

`MISMATCH_REQUIRES_REVIEW`

This signal can later be used by workflow logic to route the case safely.

## 15. Why did you use `workflow_signal` instead of `recommended_workflow_route`?

I used `workflow_signal` because it is safer and more consistent with the architecture.

The AI should not recommend or decide the final workflow route.

Instead, it should provide a signal based on extracted evidence.

Camunda then applies the routing rules.

## 16. What makes this project production-minded?

The project is production-minded because it separates responsibilities clearly.

It includes:

- Structured repository folders
- Documentation
- Test cases
- Workflow files
- Human review design
- AI guardrails
- Sample JSON output
- Evidence screenshots

It is not yet a production system, but it follows a production-oriented design direction.

## 17. What is not production-ready yet?

The project is not fully production-ready because:

- LangFlow is not fully connected to Camunda yet
- There is no FastAPI integration service yet
- There is no PostgreSQL database yet
- There is no real applicant upload portal yet
- There are no automated tests yet
- There is no deployed demo yet

These are planned future improvements.

## 18. How would you improve the project next?

The next improvements would be:

1. Connect LangFlow or another AI extraction service through an API.
2. Add FastAPI as an integration layer.
3. Store applications and verification results in PostgreSQL.
4. Add automated tests.
5. Add logging and error handling.
6. Deploy the project as a documented demo.

## 19. How does this project relate to enterprise AI?

This project relates to enterprise AI because many companies want to use AI inside business workflows, but they need control, auditability, and human oversight.

This project shows how AI can be integrated into a real business process without giving the model uncontrolled authority.

## 20. How would you explain this project in one sentence?

I built a controlled AI-assisted loan onboarding workflow that uses Camunda for process control, AI for document extraction, and human review for uncertain cases.