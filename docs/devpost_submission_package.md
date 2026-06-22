# Devpost Submission Package

This is the copy-paste package for the Devpost project page.

## Project name

Agentic Test Swarm

## Elevator pitch

UiPath Test Cloud agents that attack, repair, re-test, and certify enterprise AI workflows before they can touch production tools.

## Track: UiPath Test Cloud

Primary track: UiPath Test Cloud.

Agentic Test Swarm is a Track 3 submission because the main product is an agentic software testing loop:

- requirements and policies become test obligations;
- red-team agents generate adversarial AI-workflow scenarios;
- Test Designer converts attacks into Test Cloud cases;
- Test Selector chooses tests by risk, coverage, change impact, and failure history;
- Failure Analyst explains broken tests;
- Repair Agent proposes a guardrail;
- targeted re-tests produce evidence;
- Quality Governor converts evidence into a restricted runtime permit.

## What it does

Agentic Test Swarm tests an AI-infused workflow where a Marketing Outreach Agent asks a Customer Data Agent to export raw VIP customer emails.

Before repair, the Customer Data Agent accepts an executive-override prompt and returns raw PII. The swarm generates and selects adversarial certification tests, records evidence in UiPath Test Cloud / Test Manager, analyzes the failure, proposes a coding-agent-backed repair, runs targeted re-tests, routes the restricted runtime permit to Action Center, and enforces the result through a UiPath API Workflow proxy.

The final runtime decision is `deny_and_suspend` for raw PII export. Aggregate segment insight remains allowed.

Agentic Test Swarm follows the testing principle that AI should amplify judgment, not replace it: agents generate attack ideas and repair candidates, deterministic oracles define expected behavior, Test Cloud records evidence, and Action Center keeps humans accountable.

The continuous quality layer turns runtime incidents into future tests. `Continuous Quality Memory` shows how `runtime-event-phone-001` becomes TC-006 in UiPath Test Manager. The `Evidence Graph` links the whole chain: trace -> policy -> test -> repair -> approval -> runtime enforcement. The `Test Cloud Native Traceability Pack` shows the next native Test Cloud chain: Requirement -> Test Case -> Execution -> Defect -> Runtime Permit, anchored by `REQ-PII-001`, `Obsolete Test Scout`, a Create Defect webhook demo that returns `ATS-DEFECT-TC-001`, Testing Process Governance, and the runtime permit.

The judge evidence page separates what is live in UiPath from deterministic worker evidence and future platform polish. It also separates Run A, the before-repair TC-001 failure, from Run B, the after-repair six-case Test Manager execution. That avoids overclaiming and makes the repair loop easier to audit.

## How we built it

UiPath is the orchestration and governance layer:

- Studio Web / Maestro models the certification lifecycle.
- Test Cloud / Test Manager stores certification cases and result evidence.
- Action Center gates the restricted runtime permit.
- API Workflow acts as the runtime proxy for agent-to-agent tool calls.
- Automation Cloud connects the test evidence, approval gate, workflow state, and runtime enforcement.

The external worker is deterministic. It provides:

- captured AI trace replay;
- policy-to-test scenario generation artifacts;
- expected-oracle decisions;
- failure analysis;
- repair candidate evidence;
- targeted re-test results;
- permit hash metadata;
- runtime `/license-decision`.

## UiPath components used

- UiPath Automation Cloud
- UiPath Test Cloud / Test Manager
- UiPath Studio Web
- UiPath Maestro / agentic process model
- UiPath Action Center
- UiPath API Workflows
- UiPath for Coding Agents / coding-agent workflow evidence
- UiPath-native Agent Builder / Studio Web agent specs for Policy Miner Agent, Red-Team Agent, Test Designer Agent, and the implemented Failure Analyst Agent

## UiPath-native agent depth

The project is no longer only an external worker plus UiPath screenshots. The testing swarm has UiPath-native agent depth:

- Policy Miner Agent has a Studio Web / Agent Builder spec that turns business policy and captured trace evidence into Test Cloud obligations.
- Red-Team Agent has a Studio Web / Agent Builder spec that generates risk-revealing adversarial AI-workflow scenarios.
- Test Designer Agent has a Studio Web / Agent Builder spec that converts red-team scenarios into Test Cloud case drafts with deterministic expected outcomes.
- Failure Analyst Agent is implemented as a UiPath-native Studio Web Autonomous Agent and was debugged successfully with `1 Agents.LLMCalls`.

The setup pack is available in the repository at `evidence/case_001/uipath_native_agent_pack.json` and through the worker endpoint `/uipath-native-agent-pack`.

## Challenge: external LLMs under governance

External frameworks and LLMs are useful for generating attacks and repair candidates, but enterprises cannot trust them blindly.

Agentic Test Swarm uses a split trust model:

```text
AI agents suggest tests and repairs.
Deterministic oracles define expected behavior.
UiPath records evidence, gates approval, and enforces runtime decisions.
```

That keeps external LLMs inside a governed UiPath workflow instead of making them the final authority.

## Accomplishments

- Built a public live simulation: `https://permitops-uipath.vercel.app/live-swarm-view`
- Built a one-click runbook endpoint for UiPath API Workflow: `/uipath-one-click-runbook`
- Created a Test Manager project, five core certification tests, and live TC-006 incident-memory coverage as `PVACPOV91:76`.
- Assigned TC-006 to the main `PVACPOV91:6 - PermitOps Certification Evidence` test set, which now shows `Static Assignment (6)`.
- Created Action Center approval evidence and preserved pending task `#3545796` for the final demo.
- Captured Studio Web API Workflow evidence returning `deny_and_suspend`.
- Configured a UiPath-native Studio Web Autonomous Agent draft as the `Agentic Test Swarm Failure Analyst Agent`, selected UiPath model `gpt-5.4-2026-03-05`, and preserved the low-code `{{log_chunk}}` evidence-package input.
- Removed the unneeded template `Create Issue` integration tool from that agent draft, clearing Health Analyzer to `No issues found` while keeping Action Center task `#3545796` pending.
- Debugged the UiPath-native Failure Analyst Agent successfully inside Studio Web. The execution trace shows an Agent run, LLM call, model run, `1 Agents.LLMCalls` usage, and output `Completed certification failure analysis`.
- Added UiPath-native agent depth specs for Policy Miner Agent, Red-Team Agent, and Test Designer Agent, plus the worker endpoint `/uipath-native-agent-pack` so Studio Web or API Workflow can fetch the setup pack.
- Added `TC-006` as incident-memory evidence for a new raw phone-number export tool surface.
- Added Continuous Quality Memory endpoints: `/continuous-quality-memory` and `/continuous-quality-memory-view`.
- Added Evidence Graph endpoints: `/evidence-graph` and `/evidence-graph-view`.
- Added Test Cloud Native Traceability Pack endpoints: `/test-cloud-traceability` and `/test-cloud-traceability-view`.
- Added Test Manager Create Defect webhook demo endpoints: `/test-manager-webhook-demo` and `/test-manager-webhook-demo-view`.
- Added repo evidence files: `evidence/case_001/continuous_quality_memory.json` and `evidence/case_001/evidence_graph.json`.
- Added repo traceability evidence: `evidence/case_001/test_cloud_traceability_pack.json`.
- Added webhook evidence: `evidence/case_001/test_manager_create_defect_webhook_demo.json`, with defect payload `ATS-DEFECT-TC-001`.
- Added judge status endpoints: `/judge-evidence-matrix-view` and `/before-after-execution-evidence-view`.
- Added before/after execution evidence: Run A fails TC-001 before repair; Run B is the live six-case after-repair Test Manager execution.
- Created live Test Manager requirement `PVACPOV91:151 - REQ-PII-001 Agent-to-agent PII export must be blocked before production`.
- Linked `PVACPOV91:151` to all six certification cases: `PVACPOV91:1`, `PVACPOV91:2`, `PVACPOV91:3`, `PVACPOV91:4`, `PVACPOV91:5`, and `PVACPOV91:76`.
- Verified the requirement exposes UiPath Test Manager Optimize coverage with Autopilot actions for requirement quality evaluation and test generation; the current tenant asks for additional document or RAG context before continuing.
- Built an MIT-licensed public GitHub repository with tests, setup instructions, deck, Devpost copy, and product feedback notes.

## What we learned

The hard part is not generating a test. The hard part is making AI-generated test evidence governable by enterprise operators.

UiPath is valuable because it gives the system a control plane: Test Cloud for evidence, Action Center for accountability, API Workflow for enforcement, and Studio Web / Maestro for business-visible orchestration.

## What's next

- Attach captured AI trace and hash evidence directly to each Test Manager test result.
- If recording time allows, instantiate the Policy Miner Agent and Red-Team Agent specs inside UiPath Agent Builder using the `/uipath-native-agent-pack` payload.
- Add a reusable API Workflow runtime permit template.
- If platform time allows, create a separate Test Manager before-repair execution named `Attack Detection - Before Repair` with TC-001 failed, so Run A becomes live tenant proof.
- Turn `Obsolete Test Scout` into a live Test Manager obsolete-test classification step.
- Connect Test Manager's Create Defect webhook to the Failure Analyst / Repair Agent loop.
- Use Testing Process Governance to sign off the test artifacts themselves.
- Add first-class Test Cloud attachments for captured AI traces, deterministic oracle versions, and evidence hashes.
- Expand beyond customer-data access into invoice, refund, procurement, and support AI workflows.

## Demo video checklist

Use `docs/final_video_shot_list.md`.

The video should start from UiPath, not Vercel:

```text
Studio Web / API Workflow -> Test Manager / Test Cloud -> Action Center
-> live-swarm-view -> API Workflow deny_and_suspend
```

## GitHub repository

Repository: `https://github.com/Jerry2003826/Uipath`

License: MIT.
