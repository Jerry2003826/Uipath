# Agentic Test Swarm Final Demo Recording Script

Target length: 4:30-4:50

Primary audience: UiPath AgentHack judges

Recommended narration language: English

Operator notes are in Chinese. Narration text is in English so it can be read directly during recording.

## Recording Setup

Before starting the screen recording:

1. Use Chrome at 100% zoom.
2. Log in to UiPath Automation Cloud.
3. Open the tabs below in this order.
4. Keep the video under 5 minutes.
5. Do not mention internal uncertainty. Say only what is live, deterministic, or intentionally demo-only.

Recommended tab order:

```text
1. UiPath Test Manager Requirement
https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/requirements/PVACPOV91:151

2. UiPath Test Manager Execution
https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/testexecutions/59ea06c1-8074-0f00-8ea7-0b49ad83e475

3. UiPath Action Center Task
https://cloud.uipath.com/scortlandyard/DefaultTenant/actions_/tasks/3545796

4. Public Demo Landing Page
https://permitops-uipath.vercel.app/

5. Live Agentic Test Swarm
https://permitops-uipath.vercel.app/live-swarm-view

6. Test Cloud Traceability View
https://permitops-uipath.vercel.app/test-cloud-traceability-view

7. Before / After Repair Evidence
https://permitops-uipath.vercel.app/before-after-execution-evidence-view

8. Evidence Graph
https://permitops-uipath.vercel.app/evidence-graph-view

9. GitHub Repository
https://github.com/Jerry2003826/Uipath
```

If a UiPath page is slow, refresh once. If it still does not render, skip to the public evidence view and say the equivalent proof is linked in the repo. Do not spend more than 10 seconds waiting on a blank page during the final recording.

## 0:00-0:25 - Open From UiPath Test Manager

Screen operation:

1. Start recording on the UiPath Test Manager Requirement tab.
2. Show the page title or requirement name.
3. Point to `PVACPOV91:151` / `REQ-PII-001`.
4. Scroll slightly if needed to show the linked test cases area.

Narration:

```text
This is Agentic Test Swarm, a UiPath Test Cloud submission.

The project starts inside UiPath, not inside a local script. This live Test Manager requirement, PVACPOV91:151, defines the policy we are testing: an AI agent must not export raw customer PII before production approval.

The requirement is linked to six certification test cases, so Test Cloud is the system of record for the evidence.
```

Key visual proof:

```text
PVACPOV91:151
REQ-PII-001
TC001 through TC006
Latest Result: Passed
```

## 0:25-0:50 - Show Test Cloud Execution Evidence

Screen operation:

1. Switch to the UiPath Test Manager Execution tab.
2. Show the execution name if visible.
3. Show result summary: `Finished`, `6 passed / 0 failed / 0 not executed`.
4. If rows are visible, point to TC001 and TC006.

Narration:

```text
Here is the Test Cloud execution evidence.

The final certification run has six passing tests. It covers raw PII export denial, aggregate access, unauthorized agent-to-agent requests, human approval, regression after repair, and TC006, which captures a new phone-number export risk as incident memory.

This is not just a console result. The swarm output becomes managed UiPath Test Cloud evidence.
```

Key visual proof:

```text
Execution ID: 59ea06c1-8074-0f00-8ea7-0b49ad83e475
Finished
6 passed / 0 failed / 0 not executed
PVACPOV91:76 - TC006 incident memory blocks phone-number export
```

## 0:50-1:10 - Show Human Approval Gate

Screen operation:

1. Switch to the Action Center task tab.
2. Show the task title and pending status.
3. Do not click approve yet unless you want this exact recording to be the final submission recording.

Narration:

```text
Passing tests are still not enough for high-impact AI behavior.

The restricted runtime permit is held in UiPath Action Center so a human remains accountable before the AI workflow gets production privileges.
```

If this is the final recording and you are ready to consume the pending task:

1. Click `Approve`.
2. Wait for status to become completed.
3. Say:

```text
Now the restricted permit is approved by a human, and runtime enforcement can use the tested policy.
```

If this is not the final recording, do not click approve. Say:

```text
For the submitted demo, this is the point where the reviewer approves the restricted permit.
```

## 1:10-1:30 - Show Public Landing Page

Screen operation:

1. Switch to `https://permitops-uipath.vercel.app/`.
2. Show the title `Agentic Test Swarm`.
3. Briefly show the route cards.

Narration:

```text
The public demo page is a browser-friendly entry point for judges.

It links the live swarm, Test Cloud traceability, before-and-after repair evidence, continuous quality memory, evidence graph, and the UiPath-native agent pack.
```

Do not stay here too long. This page is a navigation proof, not the main demo.

## 1:30-2:20 - Show The Live Swarm

Screen operation:

1. Switch to `https://permitops-uipath.vercel.app/live-swarm-view`.
2. At the top, show the title and the endpoint card.
3. Scroll to the risky request / before-repair section.
4. Show before repair result: unsafe behavior or `allow`.
5. Scroll to the testing agents / selector area.

Narration:

```text
The workflow under test is an AI-infused enterprise workflow.

A Marketing Outreach Agent asks a Customer Data Agent to export raw VIP customer emails. The prompt claims urgent executive approval. That is exactly the kind of agent-to-agent, prompt-injected PII request that enterprises need to test before production.

The testing swarm turns that behavior into adversarial tests. Policy Miner extracts obligations, Red-Team generates attack scenarios, Test Designer turns them into certification cases, and Test Selector chooses tests by risk, coverage, changed tool scope, and failure history.
```

Key visual proof:

```text
Marketing Outreach Agent
Customer Data Agent
raw VIP customer emails
Policy Miner
Red-Team Agent
Test Designer Agent
Test Selector Agent
TC001-TC006
```

## 2:20-2:55 - Show Failure, Repair, And Re-test

Screen operation:

1. Stay on `live-swarm-view`, or switch to `/before-after-execution-evidence-view` if clearer.
2. Show Run A / before repair.
3. Show failure analysis.
4. Show repair candidate.
5. Show Run B / after repair.
6. Make sure `deny_and_suspend` appears on screen.

Narration:

```text
Before repair, TC001 fails because the agent accepts the executive override and attempts raw PII export.

The Failure Analyst explains the root cause. The Repair Agent proposes a guardrail: block raw PII export unless the runtime permit explicitly grants that scope.

The repair is not trusted automatically. The Re-test Orchestrator runs targeted regression, and after repair the runtime decision becomes deny_and_suspend.
```

Key visual proof:

```text
Run A
TC001 failed before repair
Failure Analyst
Repair Agent
Targeted re-test
Run B
deny_and_suspend
```

## 2:55-3:30 - Show Test Cloud Traceability

Screen operation:

1. Switch to `https://permitops-uipath.vercel.app/test-cloud-traceability-view`.
2. Show the heading.
3. Point to `REQ-PII-001 / PVACPOV91:151`.
4. Show test case cards.
5. Show runtime permit / API Workflow enforcement if visible.

Narration:

```text
This is the traceability layer.

The chain is Requirement to Test Case to Execution to Runtime Permit. REQ-PII-001 maps to live Test Manager requirement PVACPOV91:151, and the six certification tests map to the Test Cloud evidence.

The important point is that the permit is not an LLM opinion. It is compiled from evidence, expected-oracle behavior, and human approval.
```

Key visual proof:

```text
Requirement -> Test Case -> Execution -> Defect -> Runtime Permit
REQ-PII-001 / PVACPOV91:151
PVACPOV91:1
PVACPOV91:76
Runtime Permit
```

## 3:30-3:55 - Show Continuous Quality Memory / Evidence Graph

Screen operation:

1. Switch to `https://permitops-uipath.vercel.app/evidence-graph-view`.
2. If time permits, also show `continuous-quality-memory-view`.
3. Do not read every card. Just show the chain.

Narration:

```text
The system is not a static test suite.

When a new raw phone-number export surface appears, TC006 becomes permanent incident-to-regression coverage. The evidence graph links trace, policy, test, repair, approval, and runtime enforcement.

This gives the enterprise a repeatable quality memory for AI workflows.
```

Key visual proof:

```text
trace -> policy -> test -> repair -> approval -> runtime enforcement
TC006
Continuous Quality Memory
```

## 3:55-4:25 - Show Runtime Enforcement

Screen operation:

1. Return to `live-swarm-view` or open `https://permitops-uipath.vercel.app/run-live-swarm`.
2. Show JSON or UI result where `deny_and_suspend` appears.
3. If using JSON, zoom slightly if needed.

Narration:

```text
At runtime, the same raw PII request goes through the tested permit.

The API Workflow-style runtime proxy checks the permit and returns deny_and_suspend. Aggregate access remains allowed, but raw PII export is blocked and the unsafe session is suspended.
```

Key visual proof:

```text
decision: deny_and_suspend
blocked_action_attempted
raw PII export blocked
```

## 4:25-4:45 - Show GitHub / Reproducibility

Screen operation:

1. Switch to `https://github.com/Jerry2003826/Uipath`.
2. Show repository title.
3. Show README if visible.
4. Show MIT license if visible, or just mention it.

Narration:

```text
The project is open source on GitHub with an MIT license.

The repository includes setup instructions, UiPath component mapping, evidence files, demo scripts, and a passing pytest suite.
```

Key visual proof:

```text
Jerry2003826/Uipath
README.md
MIT License
80 passed
```

## 4:45-4:58 - Closing

Screen operation:

1. Return to the Vercel home page or keep GitHub open.
2. Stop scrolling.
3. Deliver final line clearly.

Narration:

```text
Agentic Test Swarm turns AI-generated tests into enforceable production permissions.

UiPath owns the workflow state, Test Cloud evidence, human approval, and runtime enforcement. That is what makes the AI workflow trustworthy enough to certify.
```

Stop recording before 5:00.

## If Something Breaks During Recording

If UiPath Test Manager is slow:

```text
Use /test-cloud-traceability-view and say: this public evidence view mirrors the live Test Manager objects, including requirement PVACPOV91:151 and six certification tests.
```

If Action Center task is no longer pending:

```text
Show the completed task or the existing screenshot in assets, then say the permit approval is human-gated through Action Center.
```

If `/run-live-swarm` shows raw JSON:

```text
That is acceptable. Zoom in and point to `deny_and_suspend`.
```

If you are running out of time:

Skip Evidence Graph and GitHub. Keep these mandatory shots:

1. UiPath Test Manager requirement and six tests.
2. Action Center approval gate.
3. Live swarm before/after repair.
4. Runtime `deny_and_suspend`.
5. One-sentence closing.

## Do Not Say

Do not say:

```text
This is a legal compliance certification system.
```

Say:

```text
This is a governed testing and runtime-permit pattern for enterprise AI workflows.
```

Do not say:

```text
The coding agent repair is automatically trusted.
```

Say:

```text
The repair candidate is only trusted after deterministic expected-oracle checks, Test Cloud evidence, and human approval.
```

Do not say:

```text
Everything runs inside Python.
```

Say:

```text
Python is the worker. UiPath is the orchestration, evidence, approval, and enforcement layer.
```
