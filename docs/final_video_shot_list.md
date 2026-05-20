# Final Video Shot List

The video must be under five minutes. Judges are not required to watch beyond five minutes, so every shot needs to prove a scoring point.

## Rule

UiPath-first.

Do not start from Vercel. Vercel is the worker and visual companion. UiPath is the platform that makes the system judgeable.

## 0:00-0:25 - Studio Web / API Workflow control-plane start

Screen:

- Studio Web / API Workflow project
- Control Plane Run Trigger or existing API Workflow debug panel
- `/uipath-one-click-runbook`

Narration:

```text
This starts from UiPath. API Workflow is the control-plane trigger that calls the Agentic Test Swarm worker and routes the result into Test Cloud, Action Center, and runtime enforcement.
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

Narration:

```text
The testing agents turn policy and trace evidence into adversarial tests, then select the tests by risk, coverage, change impact, and failure history.
```

## 1:35-2:10 - Test Manager / Test Cloud evidence

Screen:

- Test Manager / Test Cloud project `PVACPOV91`
- `PermitOps Certification Evidence`
- `Static Assignment (6)` with live `PVACPOV91:76 / TC006 incident memory blocks phone-number export`
- Existing historical execution with five passed overridden results

Narration:

```text
Test Cloud is where the swarm output becomes managed certification evidence. This is not a local console-only test run.
```

## 2:10-2:45 - Failure Analyst and Repair Agent

Screen:

- failure analysis
- repair summary
- after-repair result showing `deny_and_suspend`

Narration:

```text
When the raw PII test fails, the Failure Analyst explains why, and the coding-agent-backed Repair Agent proposes a guardrail. The repair is not trusted until targeted re-tests pass.
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
- Keep the video under five minutes.
