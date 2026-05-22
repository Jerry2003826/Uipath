# Product Feedback Submission

Use this document for the Best Product Feedback form. Each section includes a copy-paste answer.

## Best Product Feedback

Agentic Test Swarm is a UiPath Test Cloud project that exposed several strong product fits and a few workflow gaps across Test Manager, Maestro / Studio Web, Action Center, and API Workflows.

## What worked well

copy-paste answer:

```text
UiPath Automation Cloud gave the project a credible enterprise control plane. Test Manager / Test Cloud was the right home for generated certification tests and result evidence. Action Center mapped naturally to the human approval gate before activating a restricted runtime permit. API Workflow worked well as the runtime enforcement bridge between an AI agent tool call and a deterministic permit decision. Studio Web / Maestro made the agentic testing lifecycle understandable to business users rather than burying it in Python logs.
```

## What was hard

copy-paste answer:

```text
The hardest part was linking evidence across UiPath products. Agentic Test Swarm produces a chain: captured AI trace, policy obligation, red-team scenario, Test Cloud case, failure result, repair candidate, targeted re-test, Action Center approval, and API Workflow runtime denial. Today that chain can be represented with screenshots, attachments, links, and custom notes, but it is not a single first-class evidence object. For a production version, reviewers need to move quickly from a failed AI workflow test to the exact trace, repair, re-test, approval, and runtime enforcement event.

Our Evidence Graph endpoint models this chain as trace -> policy -> test -> repair -> approval -> runtime enforcement, but today that graph lives outside the UiPath product surface.
```

## Most valuable product improvement

copy-paste answer:

```text
The most valuable improvement would be a first-class cross-product "AI workflow certification evidence" object. It should connect Test Cloud evidence, Action Center approvals, API Workflow runtime decisions, and Maestro case state. That would let a reviewer inspect one certification record and see the original AI trace, generated tests, deterministic expected result, failed result, repair candidate, re-test result, human approval, runtime permit, and final enforcement log.

The same object should support Continuous Quality Memory so runtime incidents become permanent UiPath Test Cloud regression evidence without manually re-linking every artifact.
```

## Test Cloud evidence attachments

copy-paste answer:

```text
For AI-infused workflow testing, Test Cloud evidence attachments should support structured provenance fields: trace ID, raw response hash, policy pack version, red-team scenario ID, deterministic oracle version, repair candidate ID, evidence hash, Action Center task ID, and runtime permit ID. Agentic Test Swarm currently stores this in repository evidence files and screenshots; first-class Test Cloud support would make the chain easier to audit.

It would also be useful for Test Cloud to display a native Evidence Graph: trace -> policy -> test -> repair -> approval -> runtime enforcement.
```

## Agent Builder guardrails, simulations, and memory

copy-paste answer:

```text
Agent Builder already gives a strong conceptual model for Prompt, Context, Tools, and Escalations. For AI workflow testing, the next high-value bridge would be a way to promote Test Cloud evidence directly into Agent Builder tool guardrails and tool simulations. In Agentic Test Swarm, a failed raw PII export test should be able to create or update a Customer Data Agent tool guardrail, then create a simulation that replays the same executive-override attack before the agent can be trusted again.

Agent Memory and Context Grounding are also important for this pattern. Runtime incidents should update a governed memory or context object so future agent decisions know which tool paths previously failed, which tests became permanent regressions, and which Action Center approvals were required.
```

## Maestro to Test Cloud linking

copy-paste answer:

```text
The strongest workflow is cross-product: Maestro or Studio Web starts the test-swarm run, Test Cloud records generated tests and re-test evidence, Action Center gates approval, and API Workflow enforces the result. A built-in Maestro activity or template for creating/updating Test Cloud cases and linking them back to the current case would make this pattern much easier to build.
```

## Action Center evidence review

copy-paste answer:

```text
Action Center is a strong fit for high-impact AI approval, but the approval form should make evidence review faster. The task should be able to show the original risky prompt, selected tests, failed tests, repair summary, passing re-test, Test Cloud evidence link, proposed permit restrictions, and permit hash metadata in one approval surface.
```

## API Workflow runtime permit template

copy-paste answer:

```text
API Workflow worked well as the runtime proxy concept. A reusable runtime permit template would help: permit lookup, active/expired check, allowed action check, blocked action denial, human-approval-required response, suspension event, and audit log output. This would make it easier to turn Test Cloud evidence into enforceable production permissions.
```

## Demo reliability

copy-paste answer:

```text
For hackathons and customer demos, sample projects would help a lot: a Test Cloud sample project with evidence attachments, a Maestro test-swarm workflow template, an Action Center approval task template, and an API Workflow permit-check template. This would reduce setup risk while still showing real UiPath product usage.
```
