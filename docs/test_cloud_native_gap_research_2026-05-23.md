# Test Cloud Native Gap Research - 2026-05-23

Question:

```text
After the UiPath-native agent pack and six-case Test Manager execution, what is
still missing if judges inspect specifically for Test Cloud-native depth?
```

## Sources checked

- UiPath AgentHack Track 3 guidance: https://uipath-agenthack.devpost.com/details/tracks
- UiPath AgentHack rules and coding-agent bonus: https://uipath-agenthack.devpost.com/rules
- UiPath Test Manager docs, Quality-check requirements: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/evaluating-requirement-quality
- UiPath Test Manager docs, Generate tests for requirements: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/generating-manual-test-cases
- UiPath Test Manager docs, Finding obsolete tests based on requirements: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/finding-obsolete-tests-based-on-requirements
- UiPath Test Manager docs, AI-powered test insights: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/ai-powered-test-insights-best-practices
- UiPath Test Manager docs, Webhooks: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/webhooks
- UiPath Test Manager docs, Test Manager API integration: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/test-manager-api-integration
- UiPath Test Manager docs, Enabling Healing Agent: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/enabling-healing-agent
- UiPath Test Manager docs, Testing Process Governance: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/testing-process-governance
- UiPath Python SDK docs through Context7: `/uipath/uipath-python`

## Executive finding

The project is already strong on Track 3 story and visible Test Manager proof:

```text
captured AI trace
-> generated red-team tests
-> TC-001 through TC-006
-> six-case Test Manager execution
-> Action Center approval gate
-> API Workflow runtime denial
```

The remaining native-depth gap is not "more tests." It is making Test Cloud feel
like the system of record for the full lifecycle:

```text
Requirement -> Test Case -> Execution -> Defect -> Runtime Permit
```

This is the cleanest answer to "why UiPath is indispensable." UiPath should own
the managed quality object, not only the screenshot of a completed run.

## Official signal map

### 1. Requirements are a first-class Test Manager object

Official signal:

```text
Autopilot for Testers can evaluate requirements for clarity, completeness, and
consistency, and Test Manager can generate manual test cases from requirements.
```

Project status:

```text
We have policy obligations and generated test cases, but the live Test Manager
proof currently starts at test cases. It does not show a live requirement object.
```

Best next object:

```text
REQ-PII-001 - Marketing agents must not export raw customer PII unless a tested
permit grants that scope and human approval exists.
```

Why it matters:

```text
REQ-PII-001 lets judges see the chain starts in Test Cloud-native requirement
management, not only in our Python policy file.
```

P0 final-video wording:

```text
Say: "The Test Cloud-native chain is Requirement -> Test Case -> Execution ->
Defect -> Runtime Permit. Our current live proof has Test Case -> Execution ->
Runtime Permit; the next platform polish is creating REQ-PII-001 as the managed
requirement linked to TC-001 through TC-006."
```

P1 UiPath platform enhancement:

```text
Create REQ-PII-001 in Test Manager and link TC-001 through TC-006 to it.
```

P2 post-submission build path:

```text
Add a small sync command that creates or updates REQ-PII-001 through the Test
Manager API integration path, then maps generated tests to that requirement.
```

## 2. Obsolete tests are a direct Track 3 scoring lever

Official signal:

```text
Track 3 explicitly calls out fragile or outdated tests. Test Manager provides
Finding obsolete tests based on requirements through Autopilot for Testers.
```

Project status:

```text
The Test Selector handles risk, coverage, change impact, and incident memory.
It does not yet have an explicit obsolete-test detector.
```

Recommended feature name:

```text
Obsolete Test Scout
```

Behavior:

```text
Input: updated REQ-PII-001, tool schema diff, TC-001 through TC-006 metadata.
Output: tests to keep, tests to update, tests to retire, and coverage gaps.
```

Example:

```text
If Customer Data Agent removes export_customer_phone_numbers, TC-006 should not
be deleted silently. Obsolete Test Scout should label it as "monitoring-only" or
"retire candidate" and explain which requirement change made it obsolete.
```

P0 final-video wording:

```text
Say: "TC-006 is continuous quality memory. The next Test Cloud-native upgrade is
Obsolete Test Scout: when requirements or tool schemas change, the swarm tells
Test Manager which tests are still valuable, which are stale, and which coverage
gaps remain."
```

P1 UiPath platform enhancement:

```text
Add Obsolete Test Scout output to the Test Selector evidence package and show it
as a product-feedback extension against Test Manager obsolete-test support.
```

P2 post-submission build path:

```text
Create a small `obsolete_test_scout.json` artifact and eventually sync labels to
Test Manager when API access is stable.
```

## 3. AI-powered test insights should frame the Failure Analyst

Official signal:

```text
Test Manager's AI-powered test insights report focuses on overview, top failing
tests, common errors, error patterns, and recommendations.
```

Project status:

```text
Failure Analyst Agent already analyzes TC-001 and recommends a guardrail plus
targeted re-test. It should be narrated as a custom AI-powered test insight for
AI-agent workflows, not just a local JSON explanation.
```

Recommended language:

```text
Failure Analyst produces the same shape of insight a tester expects from Test
Cloud: failed test, common error family, risk impact, root cause,
recommendation, and targeted re-test scope.
```

P0 final-video wording:

```text
Use "AI-powered test insights" when showing Failure Analyst output.
```

P1 UiPath platform enhancement:

```text
Ask for a way to attach custom agentic insight reports directly to Test Manager
executions, with fields for trace ID, policy ID, repair ID, and re-test scope.
```

P2 post-submission build path:

```text
Render the Failure Analyst output into the five insight sections:
Overview, Top Failing Tests, Common Errors, Error Patterns, Recommendations.
```

## 4. Webhooks can close the defect loop

Official signal:

```text
Test Manager webhooks support Create Defect and Defect KPI events. The Create
Defect webhook can send test execution and test case log identifiers to an
external system, which can use the REST API to fetch failed-test details.
```

Project status:

```text
We have failure analysis and repair recommendations, but no visible Test Manager
defect loop.
```

Recommended extension:

```text
Create Defect webhook -> Failure Analyst Agent -> repair candidate -> linked
defect URL -> Test Manager result log.
```

Why this is high-leverage:

```text
It gives Test Cloud an operational response path when a certification test
fails. That makes the project feel closer to an enterprise testing system.
```

P0 final-video wording:

```text
Say: "If this were a production Test Cloud project, the failed TC-001 log would
trigger a Create Defect webhook into the Failure Analyst and Repair Agent loop."
```

P1 UiPath platform enhancement:

```text
Add a product-feedback request for a native Agent Builder target on Test Manager
Create Defect webhooks, so failure analysis can run without an external bridge.
```

P2 post-submission build path:

```text
Expose `/test-manager-webhook/create-defect` and map a TC-001 failure payload to
the existing Failure Analyst JSON.
```

## 5. Healing Agent is adjacent, not something to overclaim

Official signal:

```text
Healing Agent can provide debugging suggestions and optional self-healing for
Test Manager executions, but it has licensing and Robot/UI Automation version
requirements.
```

Project status:

```text
We did not use live Healing Agent. We built a custom Repair Agent for AI-agent
guardrails and a UiPath-native Failure Analyst Agent.
```

Boundary:

```text
Do not claim live Healing Agent use.
```

Correct positioning:

```text
Healing Agent fixes execution instability in UiPath automated tests.
Agentic Test Swarm fixes unsafe AI-agent workflow behavior and then asks Test
Cloud to preserve the evidence.
```

P0 final-video wording:

```text
Say: "We do not claim live Healing Agent use. Healing Agent would complement
this by healing UI automation execution issues, while our Repair Agent handles
AI workflow guardrails."
```

P1 UiPath platform enhancement:

```text
Ask UiPath to expose Healing Agent recommendations as structured evidence that
can feed the same Evidence Graph.
```

P2 post-submission build path:

```text
If licensing permits, enable Healing Agent on a UI automation test set and show
how its execution-healing evidence differs from AI-agent policy repair.
```

## 6. Testing Process Governance can sign the test artifacts themselves

Official signal:

```text
Testing Process Governance transitions governed test objects through In Work,
In Review, and Signed states. In Review locks the object while approvers comment,
sign, or reject.
```

Project status:

```text
Action Center gates the runtime permit, but Test Manager Governance is not yet
enabled on TC-001 through TC-006.
```

Best interpretation:

```text
Action Center approves production permit activation.
Testing Process Governance signs the testing artifacts.
```

P0 final-video wording:

```text
Say: "Action Center is the runtime permit approval. Testing Process Governance
would be the native way to sign off the test cases themselves."
```

P1 UiPath platform enhancement:

```text
Create a product-feedback ask for linking Test Manager governed signatures to
Action Center permit approval and API Workflow enforcement.
```

P2 post-submission build path:

```text
Enable governance for TC-001 through TC-006, move them to In Review, and capture
the Signed state if the tenant allows it without disturbing final video assets.
```

## Updated scoring interpretation

| Official Test Cloud lever | Current proof | Gap | Best action |
| --- | --- | --- | --- |
| Requirements to tests | Policy Miner and Test Designer generate cases | No live Test Manager requirement | Add REQ-PII-001 and link TC-001 through TC-006 |
| Outdated / fragile tests | Test Selector and TC-006 incident memory | No obsolete-test agent | Add Obsolete Test Scout |
| Failure insights | Failure Analyst Agent | Not explicitly mapped to Test Insights sections | Narrate as AI-powered test insights and later render sections |
| Repair suggestions | Coding-agent Repair Agent | Strong enough | Keep as core demo |
| Risk / coverage / change impact | Test Selector | Strong enough with TC-006 | Show TC-006 early |
| AI-infused workflow validation | Marketing Agent -> Customer Data Agent | Strong enough | Keep hero scenario |
| Test Cloud governance | Six-case execution | No governed test-case signatures | Keep Action Center now; add governance feedback |
| Defect workflow | None visible | No webhook loop | Add Create Defect webhook roadmap |
| Healing | Not used | Add-on/license boundary | Do not overclaim |

## Recommendation

Do not add another risky live UiPath feature before recording. The highest-value
next platform work is:

```text
1. Create REQ-PII-001 in Test Manager and link TC-001 through TC-006.
2. Add Obsolete Test Scout as a documented agentic testing role.
3. Add a Test Manager Create Defect webhook extension plan.
4. Treat Testing Process Governance as the test-artifact sign-off counterpart
   to Action Center's runtime permit approval.
```

Final one-line upgrade:

```text
Agentic Test Swarm makes Test Cloud the system of record for the whole chain:
Requirement -> Test Case -> Execution -> Defect -> Runtime Permit.
```
