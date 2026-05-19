# Product Feedback Notes

These notes are written from the PermitOps V9.1 build perspective. The goal is to show where UiPath Automation Cloud, Maestro, Test Cloud, Action Center, and API Workflow already fit the governed AI-agent certification pattern, and where the developer experience could be smoother.

## What Worked Well

- UiPath Automation Cloud provides a credible home for the full governance story.
- Maestro is a natural fit for orchestrating a certification lifecycle with multiple gates.
- Test Cloud / Test Manager is the right place to preserve certification evidence.
- Action Center maps cleanly to human approval before issuing a restricted license.
- API Workflow is a practical runtime enforcement layer for agent-to-agent and agent-to-API calls.

## Feedback: Test Cloud Evidence Objects

PermitOps needs a durable way to attach AI trace replay evidence to a test run.

Useful first-class fields would include:

- trace ID
- replay fixture ID
- raw response hash
- policy pack version
- deterministic oracle version
- evidence hash
- related Action Center task ID
- related runtime license ID

Today, a demo can represent these through attachments, custom fields, exported results, or screenshots. First-class support would make the evidence chain easier to audit.

## Feedback: Maestro to Test Cloud Linking

The strongest PermitOps flow is cross-product:

1. Maestro starts certification.
2. Test Cloud records evidence.
3. Action Center gates approval.
4. API Workflow enforces the approved license.

The developer experience would improve if Maestro had clearer templates or activities for creating, updating, and linking Test Cloud evidence records directly from an orchestration.

## Feedback: Action Center Evidence Review

The approval task should make evidence review fast. A reviewer should not need to manually cross-check many tabs.

Helpful approval-task fields:

- original risky agent request
- preserved raw response
- failed policy tests
- passing repaired re-test
- Test Cloud evidence link
- proposed license restrictions
- license hash metadata

## Feedback: API Workflow License Enforcement Templates

API Workflow works well as the runtime proxy concept. PermitOps would benefit from reusable templates for:

- license lookup
- license status check
- operation allow/deny decision
- denied field-level data access
- suspension response
- audit event recording

The template should make it easy to display the connection between a runtime denial and the Test Cloud evidence that justified the license restriction.

## Feedback: Hash Metadata Support

PermitOps uses three metadata hashes:

- `compiler_rules_hash`
- `evidence_hash`
- `license_hash`

It would be useful for UiPath governance workflows to have a standard way to store and display hash metadata across Test Cloud evidence, Action Center approvals, and API Workflow enforcement logs.

## Feedback: Demo Reliability

For hackathon and customer-demo settings, the ideal path would include:

- a Test Cloud sample project template
- a Maestro certification workflow template
- an Action Center approval task template
- an API Workflow license-check template
- sample evidence exports for offline fallback

This would reduce setup risk while still showing the real UiPath product flow.
