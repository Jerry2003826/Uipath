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

## Evidence Files

- `assets/studio_api_workflow_created.png`
- `assets/maestro_home_accessible.png`
- `assets/test_manager_not_enabled_404.png`
- `evidence/case_001/raw_llm_response.json`
- `evidence/case_001/trace_metadata.json`
- `evidence/case_001/normalized_ai_trace.json`
- `evidence/case_001/test_cases.json`
- `evidence/case_001/test_results_before.json`
- `evidence/case_001/test_results_after.json`
- `evidence/case_001/license.json`
- `evidence/case_001/runtime_decision.json`
- `evidence/case_001/license_card.html`

## Current Blockers

### Test Manager / Test Cloud

Direct navigation to `https://cloud.uipath.com/scortlandyard/testmanager_/` returned:

```json
{ "statusCode": 404, "message": "Resource not found" }
```

This likely means Test Manager/Test Cloud is not enabled in the current tenant yet, or the final UiPath Labs sandbox entitlement has not arrived.

Plan C remains ready: the local deterministic runner writes Test Manager dry-run payloads to `evidence/case_001/test_manager_sync_payload.json` and `evidence/case_001/test_manager_sync_result.json`.

### Action Center

Action Center has not yet been verified live. The repository contains the approval task schema and payload template; live task creation should be the next platform task after tenant services are confirmed.

## Next Platform Steps

1. Confirm UiPath Labs sandbox entitlement email has arrived.
2. Re-check Test Manager/Test Cloud availability from the product launcher or tenant services.
3. Create the `PermitOps V9.1 Agent Certification` Test Manager project/plan.
4. Map TC-001 through TC-005 using `evidence/case_001/test_manager_sync_payload.json`.
5. Create the Action Center approval task and save the live approval screenshot.
6. Configure the Studio Web API Workflow to call the deployed worker endpoint.
