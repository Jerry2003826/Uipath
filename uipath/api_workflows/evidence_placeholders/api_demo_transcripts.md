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

- Request screenshot/link: TBD
- Response screenshot/link: TBD
- Maestro Case update link: TBD

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

- Runtime call screenshot/link: TBD
- Denial response screenshot/link: TBD
- Suspended Maestro Case screenshot/link: TBD
