# PermitOps Platform Spike Status

Date: 2026-05-19 Australia/Melbourne

## Completed

- UiPath Automation Cloud login succeeded for the available account.
- Studio Web is accessible.
- A Studio Web API Workflow project/editor was opened and captured as evidence.
- Maestro is accessible in the `DefaultTenant` tenant.
- Local deterministic worker is implemented and tested.
- Local `full-demo-local` produces the PermitOps evidence chain.
- A real OpenAI Responses API call was captured and stored as `evidence/case_001/raw_llm_response.json`.
- A public FastAPI worker was deployed for UiPath API Workflow HTTP integration.
- Vercel alias: `https://permitops-uipath.vercel.app`
- A Studio Web API Workflow HTTP Request activity was configured through UiPath Autopilot.
- Studio Web Debug successfully called the public worker and returned `decision: deny_and_suspend`.

## Evidence Files

- `assets/studio_api_workflow_created.png`
- `assets/uipath_api_workflow_debug_url_blocker.png`
- `assets/uipath_api_workflow_success_deny_suspend.png`
- `assets/maestro_home_accessible.png`
- `assets/test_manager_not_enabled_404.png`
- `assets/action_center_orchestrator_not_enabled.png`
- `evidence/case_001/raw_llm_response.json`
- `evidence/case_001/trace_metadata.json`
- `evidence/case_001/normalized_ai_trace.json`
- `evidence/case_001/test_cases.json`
- `evidence/case_001/test_results_before.json`
- `evidence/case_001/test_results_after.json`
- `evidence/case_001/license.json`
- `evidence/case_001/runtime_decision.json`
- `evidence/case_001/license_card.html`

## Public Worker Checks

Health endpoint:

```text
GET https://permitops-uipath.vercel.app/health
```

Runtime license decision endpoint:

```text
POST https://permitops-uipath.vercel.app/license-decision
```

Demo payload:

```json
{
  "case_id": "case_001",
  "source_agent": "marketing-outreach-agent",
  "target_agent": "customer-data-agent",
  "action": "export_raw_customer_emails",
  "payload": {
    "segment": "VIP",
    "count": 500,
    "data_type": "raw_email"
  }
}
```

Verified live through UiPath Studio Web Debug:

```json
{
  "content": {
    "decision": "deny_and_suspend",
    "evidence_ref": "runtime-event-001",
    "license_status": "suspended",
    "reason": "blocked_action_attempted"
  },
  "statusCode": 200
}
```

The successful run is captured in `assets/uipath_api_workflow_success_deny_suspend.png`.

## Current Blockers

### Test Manager / Test Cloud

Direct navigation to `https://cloud.uipath.com/scortlandyard/testmanager_/` returned:

```json
{ "statusCode": 404, "message": "Resource not found" }
```

This likely means Test Manager/Test Cloud is not enabled in the current tenant yet, or the final UiPath Labs sandbox entitlement has not arrived.

Plan C remains ready: the local deterministic runner writes Test Manager dry-run payloads to `evidence/case_001/test_manager_sync_payload.json` and `evidence/case_001/test_manager_sync_result.json`.

### Action Center

Action Center was checked at the tenant URL:

```text
https://cloud.uipath.com/scortlandyard/DefaultTenant/actions_/tasks?status=Pending
```

The tenant returned:

```text
Actions is not enabled for this tenant.
Actions requires the UiPath Automation Cloud. Please contact your administrator to enable it.
```

The repository still contains the approval task schema and payload template. Live task creation remains blocked until Actions is enabled for the tenant or the UiPath Labs sandbox entitlement arrives.

## Next Platform Steps

1. Confirm UiPath Labs sandbox entitlement email has arrived.
2. Re-check Test Manager/Test Cloud availability from the product launcher or tenant services.
3. Create the `PermitOps V9.1 Agent Certification` Test Manager project/plan.
4. Map TC-001 through TC-005 using `evidence/case_001/test_manager_sync_payload.json`.
5. Create the Action Center approval task and save the live approval screenshot.
6. Publish or package the Studio Web API Workflow after the sandbox/service entitlement is stable.
