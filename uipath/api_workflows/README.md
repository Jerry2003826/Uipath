# Agentic Test Swarm API Workflow Specifications

This folder contains documentation-only specifications for the UiPath API
Workflow layer. These specs describe inputs, downstream Python service calls,
and deterministic demo responses. They do not implement Python code.

The API Workflow enforces the PermitOps Runtime Permit produced by the Agentic
Test Swarm evidence chain.

## Workflows

| Workflow | Purpose |
| --- | --- |
| Control Plane Run Trigger | One-click Studio Web/API Workflow entrypoint that starts the Agentic Test Swarm run and returns the platform runbook. |
| Certification Worker Gateway | Receives a certification case and orchestrates risk scan, test generation, and license compilation. |
| Licensed Tool Proxy | Intercepts runtime agent tool calls and asks the PermitOps Runtime Permit decision service whether the call is allowed. |
| Live Swarm Runner | Calls `/run-live-swarm` to show the vulnerable Customer Data Agent, repair candidate, targeted re-test, and TC-006 incident memory. |

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
