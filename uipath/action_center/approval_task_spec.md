# PermitOps Action Center Approval Task Specification

PermitOps uses UiPath Action Center for the required human approval step before
activating the recommended license. The primary demo path is a pre-open task
followed by a live Approve click.

## Demo Task

| Field | Demo value |
| --- | --- |
| Case ID | `PERMITOPS-CASE-001` |
| Source Agent | `Marketing Outreach Agent` |
| Target Agent | `Customer Data Agent` |
| Requested Capability | `export_raw_customer_emails` |
| Recommended License | `L2_aggregate_access` |
| Allowed Actions | `get_aggregate_segment_count`, `get_campaign_eligibility_summary` |
| Blocked Actions | `export_raw_customer_emails`, `export_customer_phone_numbers`, `access_individual_customer_profile` |
| Risk Level | `critical` |
| Evidence Summary | `5 deterministic tests mapped to UiPath Test Manager/Test Cloud; raw VIP email export denied; aggregate access allowed.` |
| Rules Hash | `rules_hash_TBD` |
| Evidence Hash | `evidence_hash_TBD` |
| License Hash | `license_hash_TBD` |
| Decision | `Approve` or `Reject` |

## Demo Path

1. Open the task before the presentation reaches the approval moment.
2. Show the evidence summary and hash fields.
3. Click `Approve` live.
4. Confirm Maestro Case state changes from `Pending Human Approval` to `Licensed`.
5. Trigger the Licensed Tool Proxy runtime call.
6. Confirm blocked raw email export changes the case to `Suspended`.

## Approval Semantics

Approving this task does not allow raw PII export. It approves the constrained
`L2_aggregate_access` license, which allows aggregate marketing analysis and
blocks raw customer email export.
