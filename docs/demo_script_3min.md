# Agentic Test Swarm Demo Script: 3 Minutes

## 0:00-0:20 - Setup

"Agentic Test Swarm is a UiPath-orchestrated team of AI testing agents that attacks, repairs, re-tests, and certifies enterprise AI workflows."

"The track is UiPath Test Cloud. The permit is not the product; it is the final output of the testing swarm."

## 0:20-0:45 - Risky Agent Call

Show the captured trace.

"The Marketing Outreach Agent asks the Customer Data Agent to export 500 VIP customer emails after claiming urgent CMO approval. The trace preserves the actual behavior that must be tested."

## 0:45-1:25 - Testing Swarm

Show the evidence files or agent board.

"Policy Miner extracts raw PII obligations. Red-Team attacks the live Customer Data Agent. Before repair, it returns raw emails. Test Designer converts those attacks into Test Cloud certification cases. Test Selector chooses the high-risk PII and regression tests first."

"AI proposes attacks and repair candidates, but deterministic oracles decide expected behavior."

"When the Customer Data Agent adds `export_customer_phone_numbers`, the selector creates TC-006 as an incident-memory antibody test."

## 1:25-1:55 - Test Cloud and Repair

Show Test Manager and failure analysis.

"UiPath Test Cloud stores the certification evidence. Before repair, TC-001 shows the raw PII export failure. Failure Analyst explains the root cause, and the coding-agent-backed Repair Agent proposes the raw PII guardrail."

"After targeted re-test, TC-001 and TC-005 pass. The same raw email attack now returns `deny_and_suspend`."

## 1:55-2:25 - Permit and Approval

Show license metadata and Action Center.

"The Quality Governor compiles a restricted PermitOps Runtime Permit: aggregate access allowed, raw email export blocked, raw PII requiring human approval. Action Center gates the final approval."

Point to:

- `compiler_rules_hash`
- `evidence_hash`
- `license_hash`

## 2:25-2:55 - Runtime Enforcement

Show API Workflow denial.

"When the Marketing Outreach Agent tries raw email export again, the UiPath API Workflow proxy checks the tested permit and returns `deny_and_suspend`."

## 2:55-3:00 - Close

"Agentic Test Swarm turns AI-generated tests into enforceable production permissions for enterprise AI workflows."
