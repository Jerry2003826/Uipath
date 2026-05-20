# Agentic Test Swarm API Workflow Specifications

This folder contains the API Workflow specifications and the live evidence
notes for the UiPath API Workflow layer. These specs describe inputs,
downstream worker calls, expected outputs, and the Studio Web proof that should
be shown in the final recording. They do not implement Python code.

The API Workflow enforces the PermitOps Runtime Permit produced by the Agentic
Test Swarm evidence chain.

## Workflows

| Workflow | Purpose |
| --- | --- |
| Control Plane Run Trigger | One-click Studio Web/API Workflow entrypoint that starts the Agentic Test Swarm run and returns the platform runbook. |
| Certification Worker Gateway | Receives a certification case and orchestrates risk scan, test generation, and license compilation. |
| Licensed Tool Proxy | Intercepts runtime agent tool calls and asks the PermitOps Runtime Permit decision service whether the call is allowed. |
| Live Swarm Runner | Calls `/run-live-swarm` to show the vulnerable Customer Data Agent, repair candidate, targeted re-test, and TC-006 incident memory. |

## Evidence status

| Workflow | Evidence status |
| --- | --- |
| Licensed Tool Proxy | Live Studio Web debug evidence captured in `assets/uipath_api_workflow_success_deny_suspend.png`; response returned `statusCode: 200` and `deny_and_suspend`. |
| Control Plane Run Trigger | Public endpoint and structured runbook evidence exist in `evidence/case_001/uipath_one_click_runbook.json`; final Studio Web trigger screenshot still needs to be captured from an authenticated UiPath browser session. |
| Live Swarm Runner | Public Vercel endpoint and browser view exist at `/run-live-swarm` and `/live-swarm-view`; final recording should show this as a UiPath-triggered run, not as the main control plane. |

## Demo IDs

- Case ID: `PERMITOPS-CASE-001`
- Trace ID: `trace-vip-500-demo`
- Source agent: `Marketing Outreach Agent`
- Target agent: `Customer Data Agent`
- Recommended license: `L2_aggregate_access`
- Runtime violation decision: `deny_and_suspend`
- One-click runbook endpoint: `/uipath-one-click-runbook`
- V11 live swarm endpoint: `/run-live-swarm`

## One-click run path

```text
Studio Web/API Workflow trigger
-> GET /uipath-one-click-runbook
-> POST /run-live-swarm
-> Test Cloud/Test Manager evidence including TC-006
-> Action Center task #3545796
-> POST /license-decision through Licensed Tool Proxy
-> deny_and_suspend
```
