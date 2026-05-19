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

The current inbox state is:

```text
No Pending tasks
```

Remaining work: create the live PermitOps approval task from a UiPath process activity, such as Action Center `Create Form Task`, or bind the Maestro `Human approval in Action Center` step to an executable task creation path.
