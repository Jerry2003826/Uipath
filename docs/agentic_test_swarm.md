# Agentic Test Swarm

Subtitle:

```text
UiPath Test Cloud agents that attack, repair, and certify AI workflows
```

## Positioning

Agentic Test Swarm is a UiPath-orchestrated team of AI testing agents.

The public claim is:

```text
Agentic Test Swarm turns policies, AI traces, and workflow changes into
red-team tests, failure analysis, repair candidates, targeted re-tests, and
finally an enforceable runtime permit.
```

PermitOps remains as the final governance module:

```text
PermitOps Runtime Permit
```

The permit is the output of the testing swarm, not the whole product.

## Why this fits Track 3

The UiPath Test Cloud track asks for agents that reimagine how modern enterprise software testing is designed, automated, executed, and managed. Agentic Test Swarm maps to that directly:

| Track 3 prompt | Agentic Test Swarm implementation |
| --- | --- |
| Assess requirements and turn them into meaningful test scenarios | `Policy Miner Agent` extracts PII obligations and `Test Designer Agent` converts them into certification tests. |
| Identify fragile or outdated tests | `Test Selector Agent` separates critical deterministic checks from lower-priority controls and records coverage gaps. |
| Recommend fixes when automated tests fail | `Failure Analyst Agent` explains TC-001 and `Repair Agent` proposes the raw PII guardrail. |
| Coordinate the right tests based on risk, coverage, and change impact | `Test Selector Agent` prioritizes PII, prompt-injection, agent-to-agent, approval, and regression tests. |
| Validate AI-infused workflows and internal/third-party AI services | The tested workflow is a Marketing Outreach Agent calling a Customer Data Agent through a governed UiPath runtime proxy. |

## Swarm flow

```text
Captured AI Trace
-> Policy Miner Agent
-> Red-Team Agent
-> Test Designer Agent
-> Test Selector Agent
-> UiPath Test Cloud / Test Manager
-> Failure Analyst Agent
-> Repair Agent
-> Re-test Orchestrator
-> Quality Governor
-> PermitOps Runtime Permit
-> Action Center approval
-> API Workflow enforcement
```

## V11 live loop

V11 adds a concrete workflow under test:

```text
Red-Team Agent attacks Customer Data Agent
-> vulnerable agent returns raw emails
-> Failure Analyst explains TC-001
-> Repair Agent proposes raw PII guardrail
-> Re-test Orchestrator replays the same attack
-> repaired agent returns deny_and_suspend
-> incident memory creates TC-006 for phone-number export
```

Local command:

```bash
.venv/bin/python -m permitops_worker.cli v11-live-swarm-local
```

Evidence:

- `evidence/case_001/v11_live_swarm_run.json`
- `evidence/case_001/incident_antibody_tests.json`

## Agent roles

| Agent | Type | Evidence | Responsibility |
| --- | --- | --- | --- |
| `Marketing Outreach Agent` | AI worker under test | `normalized_ai_trace.json` | Attempts VIP campaign work and raw email export. |
| `Customer Data Agent` | Target agent/tool | `normalized_ai_trace.json` | Represents the sensitive data endpoint. |
| `Policy Miner Agent` | Testing agent | `policies.yaml`, `agentic_test_swarm_run.json` | Extracts test obligations from policy, trace, and tool schema. |
| `Red-Team Agent` | Testing agent | `red_team_scenarios.json` | Generates adversarial prompt-injection and agent-to-agent misuse scenarios. |
| `Test Designer Agent` | Testing agent | `test_designer_cases.json`, `test_cases.json` | Converts red-team scenarios into Test Cloud cases with deterministic expected results. |
| `Test Selector Agent` | Testing agent | `test_selector_decision.json` | Selects tests by risk, coverage, changed tool scope, and failure history. |
| `Failure Analyst Agent` | Testing agent | `failure_analysis.json` | Explains failures and recommends repair plus targeted re-test scope. |
| `Repair Agent` | Coding-agent-backed testing agent | `repair_summary.md`, coding-agent logs | Proposes the guardrail candidate. |
| `Re-test Orchestrator` | Testing agent | `test_results_after.json` | Re-runs TC-001 and TC-005 after repair. |
| `Quality Governor` | Deterministic governance gate | `license.json`, `runtime_decision.json` | Converts evidence and approval into the PermitOps Runtime Permit. |
| `Incident Memory` | Quality memory layer | `incident_antibody_tests.json` | Converts runtime violations into permanent regression tests. |

## UiPath runtime mapping

Current live platform proof:

- Test Manager project: `PermitOps V9.1 Agent Certification` (`PVACPOV91`)
- Test set: `PVACPOV91:6 - PermitOps Certification Evidence`
- Execution result summary: `5 passed / 0 failed / 0 not executed`
- Action Center pending task: `#3545796`
- Studio Web / API Workflow result: `deny_and_suspend`

The names still say PermitOps because the UiPath artifacts were created before the narrative pivot. They now map to the Agentic Test Swarm certification run.

## UiPath no-code control plane

The award-grade framing is:

```text
AI agents explore and recommend.
Deterministic rules decide expected behavior.
UiPath makes the whole loop operable, auditable, and enforceable.
```

This means the platform surfaces are not screenshots around a Python app:

| UiPath surface | Control-plane responsibility |
| --- | --- |
| Maestro / Studio Web | Owns the visible lifecycle for the certification run. |
| Test Cloud / Test Manager | Owns generated test cases, selected tests, failures, and re-test evidence. |
| Action Center | Owns human approval before the restricted permit becomes active. |
| API Workflow | Owns runtime enforcement for agent-to-agent tool calls. |
| Automation Cloud | Connects workflow state, evidence, approval, and enforcement in one tenant. |

The browser demo now exposes a `UiPath No-Code Control Plane` section so judges can see that a non-developer operator can approve the permit, request targeted re-tests, suspend the agent session, and promote incidents into regression coverage.

## One-click UiPath runbook

The runbook endpoint makes the platform chain explicit:

```text
GET /uipath-one-click-runbook
```

It returns:

```text
Studio Web / API Workflow trigger
-> POST /run-live-swarm
-> Test Cloud/Test Manager evidence including TC-006
-> Action Center task #3545796
-> POST /license-decision through Licensed Tool Proxy
-> deny_and_suspend
```

This is the answer to the core judging question:

```text
Could this just be a Python demo?
```

No. The worker can compute evidence, but UiPath owns the visible run, managed
test evidence, human approval, and runtime enforcement.

## Sandbox enhancement

When sandbox access exposes UiPath Agent Builder or first-class UiPath agent runtime, add visible UiPath-native agents for:

```text
Policy Miner Agent
Red-Team Agent
Test Designer Agent
```

This does not replace the deterministic oracle.

The trust model remains:

```text
agent suggestions -> deterministic oracle -> Test Cloud evidence -> Action Center approval -> API Workflow enforcement
```

## Demo message

Use this sentence in the video:

```text
The permit is not the product. The product is a UiPath-orchestrated testing
swarm that attacks, repairs, re-tests, and certifies an AI workflow. The permit
is only the final governance artifact.
```
