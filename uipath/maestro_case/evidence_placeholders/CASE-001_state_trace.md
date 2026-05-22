# Evidence Placeholder: PERMITOPS-CASE-001 State Trace

Use this file as the attachment placeholder for the Maestro Case state history.

| Sequence | Timestamp | State | Actor/System | Evidence to attach |
| --- | --- | --- | --- | --- |
| 1 | 2026-05-19 | Submitted | Certification Worker Gateway | Intake payload in `uipath/api_workflows/certification_worker_gateway.yaml` and trace replay in `evidence/case_001/normalized_ai_trace.json`. |
| 2 | 2026-05-23 | Test Cloud Evidence | Test Manager/Test Cloud | Test Manager execution `59ea06c1-8074-0f00-8ea7-0b49ad83e475` records `Finished`, `6 passed / 0 failed / 0 not executed`, including live TC-006 incident-memory coverage. |
| 3 | 2026-05-19 | Pending Human Approval | Action Center | Pre-open approval task `#3545796` in `assets/action_center_permitops_pending_assigned_task_3545796.png`. |
| 4 | 2026-05-19 | Licensed | Action Center/Maestro | Completed approval task `#3545494`, active runtime permit `evidence/case_001/license.json`, permit hash `sha256:7e927bef7a7b2e4fd5c9cd131fc82fd88a05475f0fadeda3967180442f44d04c`. |
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
