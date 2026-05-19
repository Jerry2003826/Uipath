# Evidence Placeholder: PERMITOPS-CASE-001 State Trace

Use this file as the attachment placeholder for the Maestro Case state history.

| Sequence | Timestamp | State | Actor/System | Evidence to attach |
| --- | --- | --- | --- | --- |
| 1 | TBD | Submitted | Certification Worker Gateway | Intake payload with `case_id`, `trace_id`, `source_agent`, and `target_agent`. |
| 2 | TBD | Test Cloud Evidence | Test Manager/Test Cloud | TC-001 through TC-005 case result links and evidence hash. |
| 3 | TBD | Pending Human Approval | Action Center | Pre-open approval task snapshot. |
| 4 | TBD | Licensed | Action Center/Maestro | Human approval click, license hash, and allowed/blocked actions. |
| 5 | TBD | Suspended | Licensed Tool Proxy | Runtime denial transcript for raw VIP email export. |

## Demo Notes

- Keep the pre-open Action Center task visible before the live approval click.
- After approval, show the case entering `Licensed`.
- Trigger the Licensed Tool Proxy with the VIP/raw-email payload.
- Attach the proxy result showing `deny_and_suspend` and case state `Suspended`.
