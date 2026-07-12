# Test Summary

This document summarizes the workflow tests completed for the AI Business Loan Onboarding Portfolio project.

## Test objective

The objective was to confirm that the Camunda workflow gateway correctly routes business loan applications based on the `verificationRoute` variable.

## Tested workflow routes

| Test case | Company | verificationRoute | Expected outcome | Result |
|---|---|---|---|---|
| APP-003 | Bright Path Logistics Limited | `CLEAN_CASE` | Proceed to final review | Passed |
| APP-001 | Stock Trace Limited | `REQUEST_NEW_DOCUMENT` | Waiting for new document | Passed |
| APP-002 | Green Valley Foods Limited | `HUMAN_REVIEW` | Evidence sent for human review | Passed |
| APP-004 | Registry issue case | `MANUAL_INVESTIGATION` | Manual investigation required | Passed |

## What was validated

The tests confirmed that:

- The workflow gateway reads the `verificationRoute` variable.
- Each route sends the process to the expected path.
- Clean cases proceed to final review.
- Weak or expired documents trigger a new document request.
- Mismatched evidence goes to human review.
- Registry issues go to manual investigation.

## Human review validation

The human review route was tested using a Camunda Tasklist form.

The reviewer task allowed the reviewer to inspect the case and select a decision.

This confirms that the workflow supports human-in-the-loop review for uncertain or mismatched evidence.

## Evidence

Evidence for these tests is stored in the `screenshots` folder.

Key screenshots include:

- Full BPMN workflow
- Clean case route
- Request new document route
- Human review route in Tasklist
- Manual investigation route
- Operate variables
- Process version success

## Conclusion

All four workflow paths were successfully tested.

The current version proves that the workflow routing logic works and that the project has a solid foundation for future AI extraction and integration improvements.