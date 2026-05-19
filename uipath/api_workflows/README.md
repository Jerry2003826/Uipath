# Agentic Test Swarm API Workflow Specifications

This folder contains documentation-only specifications for the UiPath API
Workflow layer. These specs describe inputs, downstream Python service calls,
and deterministic demo responses. They do not implement Python code.

The API Workflow enforces the PermitOps Runtime Permit produced by the Agentic
Test Swarm evidence chain.

## Workflows

| Workflow | Purpose |
| --- | --- |
| Certification Worker Gateway | Receives a certification case and orchestrates risk scan, test generation, and license compilation. |
| Licensed Tool Proxy | Intercepts runtime agent tool calls and asks the PermitOps Runtime Permit decision service whether the call is allowed. |

## Demo IDs

- Case ID: `PERMITOPS-CASE-001`
- Trace ID: `trace-vip-500-demo`
- Source agent: `Marketing Outreach Agent`
- Target agent: `Customer Data Agent`
- Recommended license: `L2_aggregate_access`
- Runtime violation decision: `deny_and_suspend`
