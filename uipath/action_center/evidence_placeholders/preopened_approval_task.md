# Evidence Placeholder: Pre-open Action Center Approval Task

Use this file to capture the pre-open Action Center task shown in the demo.

| Field | Value |
| --- | --- |
| Case ID | `PERMITOPS-CASE-001` |
| Source Agent | `Marketing Outreach Agent` |
| Target Agent | `Customer Data Agent` |
| Requested Capability | `export_raw_customer_emails` |
| Recommended Permit | `L2_aggregate_access` |
| Risk Level | `critical` |
| Decision shown | `Approve` |

## Evidence To Attach

- Pre-open task screenshot/link: `assets/action_center_permitops_pending_assigned_task_3545796.png`
- Live approval click screenshot/link: `assets/action_center_permitops_completed_task_3545494.png`
- Post-approval Maestro/Studio evidence screenshot/link: `assets/maestro_debug_human_approval_completed.png`
- Permit hash capture: `sha256:7e927bef7a7b2e4fd5c9cd131fc82fd88a05475f0fadeda3967180442f44d04c`
- Action Center enabled screenshot/link: `assets/action_center_enabled_empty_inbox.png`

## Required Visible Fields

- Case ID
- Source Agent
- Target Agent
- Requested Capability
- Recommended Permit
- Allowed Actions
- Blocked Actions
- Risk Level
- Evidence Summary
- Rules Hash
- Evidence Hash
- Permit Hash
- Decision

## Current Live State

Action Center has been added to `DefaultTenant` and is accessible at:

```text
https://cloud.uipath.com/scortlandyard/DefaultTenant/actions_/tasks?status=Pending
```

The current live task state is:

```text
Task: Approve PermitOps Restricted Agent License
Task ID: 3545796
Catalog: PermitOps Approvals
Priority: High
Status bucket: Pending
```

Created from Studio Web:

```text
RPA Workflow -> Create External Task
RPA Workflow -> Assign Tasks
Cloud debug log: Task created with Id 3545796
Task Id binding: taskObjectOutput.Id.Value
```

Evidence:

- `assets/studio_web_create_external_task_success.png`
- `assets/action_center_permitops_unassigned_task_3545494_clean.png`
- `assets/action_center_permitops_completed_task_3545494.png`
- `assets/action_center_permitops_pending_assigned_task_3545796.png`

Completion result:

```text
Action Center snackbar: Task completed successfully
Completed tab: Approve PermitOps Restricted Agent License #3545494
```

The assigned-pending gap is resolved. Task `#3545796` appears under the current user's `My Tasks > Pending` inbox. The remaining optional demo step is to complete this assigned task live during recording so the video shows Pending -> Completed.
