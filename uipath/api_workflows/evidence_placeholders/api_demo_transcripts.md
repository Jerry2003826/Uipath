# Evidence Placeholder: API Workflow Demo Transcripts

Use this file to paste or link the live demo request/response captures.

## Certification Worker Gateway

Request payload:

```json
{
  "case_id": "PERMITOPS-CASE-001",
  "trace_id": "trace-vip-500-demo",
  "source_agent": "Marketing Outreach Agent",
  "target_agent": "Customer Data Agent"
}
```

Expected response:

```json
{
  "case_id": "PERMITOPS-CASE-001",
  "trace_id": "trace-vip-500-demo",
  "risk_level": "critical",
  "generated_tests": 5,
  "license_recommendation": "L2_aggregate_access",
  "next_state": "Pending Human Approval"
}
```

Evidence capture placeholder:

- Request screenshot/link: `assets/uipath_api_workflow_success_deny_suspend.png`
- Response screenshot/link: `assets/uipath_api_workflow_success_deny_suspend.png`
- Maestro Case update link: modeled in `assets/maestro_permitops_bpmn_autopilot.png`; live Maestro case state is not available in the current tenant.

## Control Plane Run Trigger

Request:

```http
GET /uipath-one-click-runbook?case_id=case_001
```

Expected response summary:

```json
{
  "runbook_name": "UiPath One-Click Agentic Test Swarm Run",
  "trigger": {
    "operator_action": "Click Run in UiPath",
    "uipath_surface": "Studio Web / API Workflow"
  },
  "test_cloud_delta": {
    "mapped_tests": ["TC-001", "TC-002", "TC-003", "TC-004", "TC-005", "TC-006"],
    "new_or_highlighted_test": "TC-006"
  },
  "action_center": {
    "task_id": "3545796"
  },
  "runtime_enforcement": {
    "expected_decision": "deny_and_suspend"
  }
}
```

Evidence capture placeholder:

- Studio Web trigger screenshot/link: capture during final recording.
- Response screenshot/link: use `https://permitops-uipath.vercel.app/live-swarm-view` if Studio Web debug panel is not visible enough.
- Structured evidence: `evidence/case_001/uipath_one_click_runbook.json`.

## Licensed Tool Proxy

Request payload:

```json
{
  "source_agent": "Marketing Outreach Agent",
  "target_agent": "Customer Data Agent",
  "action": "export_raw_customer_emails",
  "payload": {
    "segment": "VIP",
    "count": 500,
    "data_type": "raw_email"
  }
}
```

Expected response:

```json
{
  "decision": "deny_and_suspend",
  "case_state": "Suspended"
}
```

Evidence capture placeholder:

- Runtime call screenshot/link: `assets/uipath_api_workflow_success_deny_suspend.png`
- Denial response screenshot/link: `assets/uipath_api_workflow_success_deny_suspend.png`
- Suspended Maestro Case screenshot/link: modeled in `assets/maestro_permitops_bpmn_autopilot.png`; live suspension state is represented by the API Workflow response and local `evidence/case_001/runtime_decision.json`.

Live Studio Web Debug output captured on 2026-05-19:

```json
{
  "content": {
    "decision": "deny_and_suspend",
    "evidence_ref": "runtime-event-001",
    "license_status": "suspended",
    "reason": "blocked_action_attempted"
  },
  "statusCode": 200,
  "vendorProcessingTimeMs": 2664
}
```
