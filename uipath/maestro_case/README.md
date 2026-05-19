# PermitOps Maestro Case Specification

PermitOps uses a UiPath Maestro Case as the primary certification lifecycle
orchestrator for enterprise AI-agent licensing decisions. The case owns the
state machine, evidence references, approval routing, and runtime suspension
record for a requested agent-to-agent capability.

## Hero Scenario

- Project: PermitOps
- Platform track: UiPath Test Cloud
- Source agent: Marketing Outreach Agent
- Target agent: Customer Data Agent
- Requested capability: Export 500 VIP customer emails
- Sensitive action: `export_raw_customer_emails`
- Runtime outcome: Deny and suspend unauthorized raw PII export

## Case Role

The Maestro Case coordinates these responsibilities:

1. Receive the certification submission for an agent capability.
2. Route the submission through risk scanning and deterministic test generation.
3. Attach Test Cloud/Test Manager evidence from local deterministic execution.
4. Propose repair candidates when certification fails.
5. Compile a license recommendation for human approval.
6. Store the approved license, rules hash, evidence hash, and license hash.
7. Monitor licensed runtime calls and suspend attempts that violate the license.

## Full Case State Model

| State | Purpose |
| --- | --- |
| Submitted | Intake has created the case and captured source/target/action metadata. |
| Risk Scanning | Risk scan is running against the requested agent capability. |
| Test Generation | Deterministic test scenarios are being generated from the risk result. |
| Test Cloud Evidence | Test cases, results, and evidence are mapped into Test Manager/Test Cloud. |
| Certification Failed | One or more required tests failed or a critical policy breach was found. |
| Repair Candidate Proposed | PermitOps proposes a constrained repair or safer capability scope. |
| Re-test Evidence | Repaired candidate is re-run and evidence is attached. |
| License Recommendation | A recommended license tier and policy envelope are compiled. |
| Pending Human Approval | Action Center approval task is open for a human decision. |
| Licensed | Approved license is active and available for runtime decisions. |
| Runtime Monitoring | Runtime calls are evaluated against the approved license. |
| Suspended | Runtime violation has denied the call and suspended the license/case. |
| Recertification Required | Changed behavior, rules, or evidence requires a fresh certification cycle. |

## Minimum Demo State Path

The live demo only needs to show this reduced path:

1. Submitted
2. Test Cloud Evidence
3. Pending Human Approval
4. Licensed
5. Suspended

## Case Keys

| Field | Demo value |
| --- | --- |
| Case ID | `PERMITOPS-CASE-001` |
| Trace ID | `trace-vip-500-demo` |
| Source Agent | `Marketing Outreach Agent` |
| Target Agent | `Customer Data Agent` |
| Requested Capability | `export_raw_customer_emails` |
| Requested Segment | `VIP` |
| Requested Count | `500` |
| Requested Data Type | `raw_email` |
| Risk Level | `critical` |
| Recommended License | `L2_aggregate_access` |
| Final Runtime Decision | `deny_and_suspend` |

## Evidence Attachments

The case should link to the following evidence groups:

- API Workflow transcript for Certification Worker Gateway.
- Test Manager/Test Cloud mapped cases TC-001 through TC-005.
- Action Center approval task snapshot.
- Licensed Tool Proxy runtime denial and suspension transcript.
- Hash set: rules hash, evidence hash, license hash.
