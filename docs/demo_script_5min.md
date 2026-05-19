# PermitOps V9.1 Demo Script: 5 Minutes

## 0:00-0:30 - Opening

"This is PermitOps, UiPath-governed licensing for enterprise AI agents. The project runs on UiPath Automation Cloud. Maestro orchestrates the certification lifecycle, Test Cloud records certification evidence, Action Center gates human approval, and an API Workflow enforces the runtime license."

"The track is UiPath Test Cloud. The key idea is that an agent does not get sensitive runtime access because we trust a prompt. It gets access only after a captured behavior trace becomes replayable evidence."

## 0:30-1:05 - Hero Risk

"Our hero scenario is a Marketing Outreach Agent calling a Customer Data Agent. The Marketing Agent asks for an export of 500 VIP customer emails."

Show the risky request.

"That is exactly the kind of cross-agent action enterprises need to govern. The agent can do useful marketing work, but raw PII export needs stronger controls."

## 1:05-1:45 - Captured AI Trace

Show the captured trace.

"PermitOps preserves the real raw model or tool response. We do not only save a summary. The raw response is part of the evidence chain because tests should replay what actually happened."

Point out:

- requesting agent
- target agent
- requested fields
- raw response
- trace ID
- trace hash

## 1:45-2:35 - Policy-to-Test Generation

Show generated policy tests.

"Next, PermitOps turns the trace into policy tests. Coding agents help generate adversarial scenarios, such as nested email exports, CSV exports, partially masked outputs, or contact IDs that are actually email addresses."

"But coding-agent output is not trusted automatically. A deterministic oracle decides pass or fail against explicit policy rules."

Show the initial failure for raw customer email export.

"The initial behavior fails because raw customer email addresses are being exported for marketing outreach without an approved restricted license."

## 2:35-3:15 - Test Cloud Evidence

Show UiPath Test Cloud / Test Manager.

"Here is the Test Cloud evidence. The plan is PermitOps V9.1 Agent Certification, and the suite is Marketing Outreach Agent - Customer Data Export."

Point out:

- failed pre-repair run
- replay fixture ID
- policy pack version
- deterministic oracle result
- evidence attachment or hash

"This is the center of the Test Cloud track: certification is recorded as evidence, not just a local console result."

## 3:15-3:50 - Repair and Re-Test

Show the repair candidate and passing re-test.

"PermitOps can propose a repair candidate, such as replacing raw emails with approved segments, aggregate counts, or masked references. The repaired candidate is then replayed through the same policy tests."

"The repaired behavior passes because it no longer exports raw PII outside the allowed scope."

## 3:50-4:25 - Action Center Approval and License

Show the Action Center task.

"Passing tests are still not enough. Maestro sends the evidence to Action Center. A human reviewer sees the original risky request, Test Cloud evidence, repair summary, and proposed license restrictions."

Show approval, then license metadata.

"After approval, the license compiler emits a restricted runtime license. The important metadata is `compiler_rules_hash`, `evidence_hash`, and `license_hash`. Those connect the runtime decision back to the evidence and compiler rules."

## 4:25-5:00 - Runtime Enforcement

Show the API Workflow proxy decision.

"Now the Marketing Outreach Agent tries the raw VIP email export again. This time the call goes through the UiPath API Workflow runtime proxy."

"The proxy checks the license and denies or suspends unauthorized raw PII export. Approved lower-risk operations can still continue, but this request is blocked."

Close:

"PermitOps demonstrates one governed certification loop: AI trace, policy test, Test Cloud evidence, repair candidate, re-test, human approval, restricted license, and API Workflow runtime enforcement."
