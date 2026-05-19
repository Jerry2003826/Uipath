# Evidence Placeholder: Pre-open Action Center Approval Task

Use this file to capture the pre-open Action Center task shown in the demo.

| Field | Value |
| --- | --- |
| Case ID | `PERMITOPS-CASE-001` |
| Source Agent | `Marketing Outreach Agent` |
| Target Agent | `Customer Data Agent` |
| Requested Capability | `export_raw_customer_emails` |
| Recommended License | `L2_aggregate_access` |
| Risk Level | `critical` |
| Decision shown | `Approve` |

## Evidence To Attach

- Pre-open task screenshot/link: TBD
- Live approval click screenshot/link: TBD
- Post-approval Maestro Case state screenshot/link: TBD
- License hash capture: TBD
- Action Center enabled screenshot/link: `assets/action_center_enabled_empty_inbox.png`

## Required Visible Fields

- Case ID
- Source Agent
- Target Agent
- Requested Capability
- Recommended License
- Allowed Actions
- Blocked Actions
- Risk Level
- Evidence Summary
- Rules Hash
- Evidence Hash
- License Hash
- Decision

## Current Live State

Action Center has been added to `DefaultTenant` and is accessible at:

```text
https://cloud.uipath.com/scortlandyard/DefaultTenant/actions_/tasks?status=Pending
```

The current live task state is:

```text
Task: Approve PermitOps Restricted Agent License
Task ID: 3545494
Catalog: PermitOps Approvals
Priority: High
Status bucket: Unassigned
```

Created from Studio Web:

```text
RPA Workflow -> Create External Task
Cloud debug log: Task created with Id 3545494
```

Evidence:

- `assets/studio_web_create_external_task_success.png`
- `assets/action_center_permitops_unassigned_task_3545494_clean.png`

Remaining work: add an assignment step so the task appears in the current user's `Pending` inbox, then capture the approval completion transition.
