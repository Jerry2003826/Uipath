# Evidence Placeholder: PERMITOPS-CASE-001 State Trace

Use this file as the attachment placeholder for the Maestro Case state history.

| Sequence | Timestamp | State | Actor/System | Evidence to attach |
| --- | --- | --- | --- | --- |
| 1 | 2026-05-19 | Submitted | Certification Worker Gateway | Intake payload in `uipath/api_workflows/certification_worker_gateway.yaml` and trace replay in `evidence/case_001/normalized_ai_trace.json`. |
| 2 | 2026-05-19 | Test Cloud Evidence | Test Manager/Test Cloud | Test Manager execution `c66f6554-4b30-0f00-4375-0b49aa4d0fd9` records `5 passed / 0 failed / 0 not executed`; evidence hash `sha256:13e6a6965d1ee4cd64d2c2e75fe96151d0aa4b9ed76fc7b897d07a68744f81c4`. |
| 3 | 2026-05-19 | Pending Human Approval | Action Center | Pre-open approval task `#3545796` in `assets/action_center_permitops_pending_assigned_task_3545796.png`. |
| 4 | 2026-05-19 | Licensed | Action Center/Maestro | Completed approval task `#3545494`, active license `evidence/case_001/license.json`, license hash `sha256:9ee59ad09498851741f61cadfdb71cfec736b880cc9ebf8cb4807a6a4355f6d4`. |
| 5 | 2026-05-19 | Suspended | Licensed Tool Proxy | Runtime denial transcript in `evidence/case_001/runtime_decision.json` and screenshot `assets/uipath_api_workflow_success_deny_suspend.png`. |

## Demo Notes

- Keep the pre-open Action Center task visible before the live approval click.
- After approval, show the case entering `Licensed`.
- Trigger the Licensed Tool Proxy with the VIP/raw-email payload.
- Attach the proxy result showing `deny_and_suspend` and case state `Suspended`.

## Live Maestro Modeling Evidence

Studio Web project:

```text
PermitOps V9.1 Certification
```

Autopilot-generated BPMN flow:

```text
Start Certification
Captured AI trace intake
Risk scanning
Generate policy tests
Record Test Cloud evidence
Pass/Fail?
Human approval in Action Center
Propose coding-agent repair
Re-test
Compile restricted license
Enforce license through API Workflow
Suspend unauthorized raw PII export
End Certification
```

Evidence screenshot:

- `assets/maestro_permitops_bpmn_autopilot.png`
