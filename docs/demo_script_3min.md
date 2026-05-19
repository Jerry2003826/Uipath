# PermitOps V9.1 Demo Script: 3 Minutes

## 0:00-0:25 - Setup

"PermitOps is UiPath-governed licensing for enterprise AI agents. It runs on UiPath Automation Cloud. Maestro orchestrates certification, Test Cloud records evidence, Action Center gates approval, and an API Workflow enforces the runtime license."

"The track is UiPath Test Cloud."

## 0:25-0:55 - Risky Agent Call

"The hero scenario is a Marketing Outreach Agent trying to call a Customer Data Agent to export 500 VIP customer emails."

Show the risky request and captured trace.

"PermitOps preserves the real raw response so the certification test replays what actually happened."

## 0:55-1:35 - Policy Tests and Evidence

Show generated policy tests and Test Cloud.

"A coding agent helps generate adversarial scenarios, but a deterministic oracle decides pass or fail. The raw email export fails policy."

"The result is recorded in UiPath Test Cloud / Test Manager as certification evidence, including the replay fixture, policy pack, oracle result, and evidence hash."

## 1:35-2:10 - Repair, Re-Test, Approval

Show passing re-test and Action Center.

"PermitOps proposes a safer repair candidate, such as aggregate or masked customer data. The candidate is re-tested against the same policy tests."

"After the restricted version passes, Maestro sends the evidence to Action Center. A human reviewer approves the restricted license."

## 2:10-2:45 - Runtime License Enforcement

Show license metadata and API Workflow denial.

"The license compiler creates a restricted runtime license with `compiler_rules_hash`, `evidence_hash`, and `license_hash`."

"When the agent tries raw PII export again, the UiPath API Workflow proxy checks the license and denies or suspends the call."

## 2:45-3:00 - Close

"PermitOps does not claim to be a full compliance system or universal sandbox. It demonstrates one governed loop: AI trace, policy test, Test Cloud evidence, repair, re-test, human approval, restricted license, and runtime enforcement."
