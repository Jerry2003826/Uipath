# Agentic Test Swarm Action Center Approval Task Specification

Agentic Test Swarm uses UiPath Action Center for the required human approval
step before activating the recommended PermitOps Runtime Permit. The primary
demo path is a pre-open task followed by a live Approve click.

## Demo Task

| Field | Demo value |
| --- | --- |
| Case ID | `PERMITOPS-CASE-001` |
| Source Agent | `Marketing Outreach Agent` |
| Target Agent | `Customer Data Agent` |
| Requested Capability | `export_raw_customer_emails` |
| Recommended Permit | `L2_aggregate_access` |
| Allowed Actions | `get_aggregate_segment_count`, `get_campaign_eligibility_summary` |
| Blocked Actions | `export_raw_customer_emails`, `export_customer_phone_numbers`, `access_individual_customer_profile` |
| Risk Level | `critical` |
| Evidence Summary | `5 deterministic tests mapped to UiPath Test Manager/Test Cloud; raw VIP email export denied; aggregate access allowed.` |
| Rules Hash | `sha256:4ecd9d107251ab758479655d3637eb5f615a5e80a4041e3fe7902f94abe9eb33` |
| Evidence Hash | `sha256:13e6a6965d1ee4cd64d2c2e75fe96151d0aa4b9ed76fc7b897d07a68744f81c4` |
| Permit Hash | `sha256:7e927bef7a7b2e4fd5c9cd131fc82fd88a05475f0fadeda3967180442f44d04c` |
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
`L2_aggregate_access` permit, which allows aggregate marketing analysis and
blocks raw customer email export.
