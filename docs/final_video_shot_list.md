# Final Video Shot List

The video must be under five minutes. Judges are not required to watch beyond five minutes, so every shot needs to prove a scoring point.

## Rule

UiPath-first.

Do not start from Vercel. Vercel is the worker and visual companion. UiPath is the platform that makes the system judgeable.

Judge-taste rule:

```text
For Taqi Jaffri, show enterprise-governed agentic automation: external agents plus UiPath-native agents, Action Center, API Workflow, traceability, and enforcement.
For Ingo Philipp, show risk-driven agentic testing: what should be tested, why it matters, failure analysis, targeted re-test, and incident memory.
```

## 0:00-0:25 - Studio Web / API Workflow control-plane start

Screen:

- Studio Web / API Workflow project
- Control Plane Run Trigger or existing API Workflow debug panel
- `/uipath-one-click-runbook`

Narration:

```text
This starts from UiPath. API Workflow is the control-plane trigger that calls the Agentic Test Swarm worker and routes the result into Test Cloud, Action Center, and runtime enforcement.
The permit is not the product; the product is the testing swarm that produces risk-revealing evidence.
```

## 0:25-0:55 - Show the unsafe AI workflow under test

Screen:

- `live-swarm-view`
- captured AI trace / Marketing Outreach Agent asking Customer Data Agent for VIP emails

Narration:

```text
The workflow under test is an AI agent calling another AI agent for raw customer PII. Prompt review alone cannot prove this is safe.
```

## 0:55-1:35 - AI testing swarm generates and selects tests

Screen:

- Policy Miner / Red-Team / Test Designer / Test Selector cards
- TC-001 through TC-006 evidence
- UiPath-native agent depth pack: `/uipath-native-agent-pack`
- Optional Studio Web / Agent Builder specs for Policy Miner Agent, Red-Team Agent, and Test Designer Agent

Narration:

```text
The testing agents turn policy and trace evidence into adversarial tests, then select the tests by risk, coverage, change impact, and failure history.
The UiPath-native agent depth is explicit: Policy Miner, Red-Team, and Test Designer have Agent Builder specs, and Failure Analyst is already debugged as a Studio Web Autonomous Agent.
```

## 1:35-2:10 - Test Manager / Test Cloud evidence

Screen:

- Test Manager / Test Cloud project `PVACPOV91`
- `PermitOps Certification Evidence`
- `Static Assignment (6)` with live `PVACPOV91:76 / TC006 incident memory blocks phone-number export`
- Fresh execution `PermitOps Certification Evidence - 20260522.1544`
- `Finished`, `6 passed / 0 failed / 0 not executed`

Narration:

```text
Test Cloud is where the swarm output becomes managed certification evidence. This is not a local console-only test run.
```

## 2:10-2:45 - Failure Analyst and Repair Agent

Screen:

- failure analysis
- repair summary
- after-repair result showing `deny_and_suspend`
- optional UiPath-native Studio Web Agent draft: `assets/uipath_failure_analyst_agent_no_issues.png`
- optional UiPath-native Studio Web Agent debug success: `assets/uipath_failure_analyst_agent_debug_success.png`

Narration:

```text
When the raw PII test fails, the Failure Analyst explains why, and the coding-agent-backed Repair Agent proposes a guardrail. The repair is not trusted until targeted re-tests pass.
```

If time allows, briefly show the UiPath-native Failure Analyst Agent draft:

```text
This role also exists as a UiPath Studio Web Autonomous Agent. The model and prompt are configured in UiPath, the unneeded template issue-tracker tool was removed, and Health Analyzer reports no issues.
It was also debugged successfully inside Studio Web, with an execution trace showing an LLM call and a completed certification failure analysis output.
```

If there is only time for one native-agent shot, show the Failure Analyst debug trace. If there is time for a second shot, show the `/uipath-native-agent-pack` payload and say:

```text
The other testing roles are also ready for UiPath Agent Builder: Policy Miner Agent, Red-Team Agent, and Test Designer Agent all have prompt contracts, input variables, expected JSON outputs, and Test Cloud evidence links.
```

## 2:45-3:20 - Action Center gate

Screen:

- Action Center task `#3545796`
- restricted runtime permit summary

Narration:

```text
High-impact approval stays human accountable. The restricted permit remains pending until Action Center approval.
```

If recording the final version, click Approve here. If recording a dry run, do not click approval.

## 3:20-4:10 - API Workflow runtime enforcement

Screen:

- API Workflow / Licensed Tool Proxy
- raw email export request
- response `deny_and_suspend`

Narration:

```text
At runtime, the repeated agent-to-agent raw PII request goes through API Workflow. The tested permit blocks it and suspends the session.
```

## 4:10-4:40 - TC-006 incident memory

Screen:

- `TC-006` incident-memory evidence
- Live Test Manager row `PVACPOV91:76`
- phone-number export tool-surface change

Narration:

```text
The system is not a static test suite. When a new raw phone-number export surface appears, the Test Selector creates TC-006 as permanent incident-to-regression coverage.
```

Show the live Test Manager row `PVACPOV91:76` and the `Static Assignment (6)` test set if the browser session is available.

## 4:40-5:00 - Closing claim

Screen:

- deck title or README scorecard
- hash metadata if visible

Narration:

```text
Agentic Test Swarm turns AI-generated tests into enforceable production permissions. UiPath owns the workflow state, Test Cloud evidence, human approval, and runtime enforcement.
```

## Recording checklist

- Show UiPath before Vercel.
- Show Test Manager / Test Cloud before local JSON evidence.
- Show Action Center before claiming an active restricted permit.
- Show `deny_and_suspend`.
- Show `TC-006`.
- Show UiPath-native agent depth: Failure Analyst Agent debug trace plus Policy Miner Agent / Red-Team Agent / Test Designer Agent specs or `/uipath-native-agent-pack`.
- Keep the video under five minutes.
