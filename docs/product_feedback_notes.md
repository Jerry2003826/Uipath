# Product Feedback Notes

These notes are written from the Agentic Test Swarm build perspective. The goal is to show where UiPath Automation Cloud, Maestro, Test Cloud, Action Center, and API Workflow already fit an agentic testing pattern for AI-infused workflows, and where the developer experience could be smoother.

## What Worked Well

- UiPath Automation Cloud provides a credible home for the full testing and governance story.
- Maestro / Studio Web is a natural fit for modeling a multi-step test-swarm lifecycle.
- Test Cloud / Test Manager is the right place to preserve generated tests, selected tests, failure evidence, and re-test evidence.
- Action Center maps cleanly to human approval before activating a restricted runtime permit.
- API Workflow is a practical runtime enforcement layer for agent-to-agent and agent-to-API calls.

## Feedback: Test Cloud Evidence Objects

Agentic Test Swarm needs a durable way to attach AI trace replay evidence and generated-test provenance to a test run.

Useful first-class fields would include:

- trace ID
- replay fixture ID
- raw response hash
- policy pack version
- red-team scenario ID
- deterministic oracle version
- evidence hash
- related Action Center task ID
- related runtime permit ID

Today, a demo can represent these through attachments, custom fields, exported results, or screenshots. First-class support would make the evidence chain easier to audit.

## Feedback: Maestro to Test Cloud Linking

The strongest Agentic Test Swarm flow is cross-product:

1. Maestro starts the swarm run.
2. Test Cloud records generated tests and evidence.
3. Action Center gates approval.
4. API Workflow enforces the approved runtime permit.

The developer experience would improve if Maestro had clearer templates or activities for creating, updating, and linking Test Cloud evidence records directly from an orchestration.

## Feedback: Action Center Evidence Review

The approval task should make evidence review fast. A reviewer should not need to manually cross-check many tabs.

Helpful approval-task fields:

- original risky agent request
- preserved raw response
- red-team scenarios
- selected tests and skipped tests
- failed policy tests
- passing targeted re-test
- Test Cloud evidence link
- proposed permit restrictions
- permit hash metadata

## Feedback: API Workflow Runtime Permit Templates

API Workflow works well as the runtime proxy concept. Agentic Test Swarm would benefit from reusable templates for:

- permit lookup
- permit status check
- operation allow/deny decision
- denied field-level data access
- suspension response
- audit event recording

The template should make it easy to display the connection between a runtime denial and the Test Cloud evidence that justified the permit restriction.

## Feedback: Hash Metadata Support

The PermitOps Runtime Permit uses three metadata hashes:

- `compiler_rules_hash`
- `evidence_hash`
- `license_hash`

It would be useful for UiPath governance workflows to have a standard way to store and display hash metadata across Test Cloud evidence, Action Center approvals, and API Workflow enforcement logs.

## Feedback: Demo Reliability

For hackathon and customer-demo settings, the ideal path would include:

- a Test Cloud sample project template
- a Maestro test-swarm workflow template
- an Action Center approval task template
- an API Workflow permit-check template
- sample evidence exports for offline fallback

This would reduce setup risk while still showing the real UiPath product flow.
