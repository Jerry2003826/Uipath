# Judge Taste Research - 2026-05-23

Question:

```text
What will the visible UiPath AgentHack judges likely reward, and how should Agentic Test Swarm adapt its final demo and submission?
```

## Current visible judges

The official Devpost page currently lists two judges:

- Taqi Jaffri, VP Product Management, UiPath.
- Ingo Philipp, VP Product Management, UiPath.

Source:

- https://uipath-agenthack.devpost.com/

## What the official page tells us

Official taste signal:

```text
Working solution, not a concept.
UiPath Automation Cloud must be the orchestration and execution layer.
The demo must show depth and deliberateness of UiPath platform usage.
Coding-agent bonus matters when the submission shows how coding agents combine with low-code components or UiPath-native agents.
```

Judging criteria:

```text
Business Impact & Adoption Potential
Platform Usage
Technical Execution, Feasibility & Versatility
Completeness of Delivery
Creativity & Innovation
Presentation
Bonus Points: Coding Agents
```

Important implication:

```text
The final video cannot feel like a local Python service with UiPath screenshots.
It must feel like UiPath is the enterprise control plane.
```

Sources:

- https://uipath-agenthack.devpost.com/
- https://uipath-agenthack.devpost.com/rules
- https://uipath-agenthack.devpost.com/details/tracks

## Taqi Jaffri taste profile

Observed public themes:

- Enterprise agentic automation, not toy agents.
- External frameworks are welcome, but enterprise deployment, orchestration, monitoring, security, and governance are the reason UiPath matters.
- Coded agents and pro-code frameworks are strongest when they plug into UiPath workflows and become auditable, testable, and upgradable.
- Agents need tools and actions, not only chat outputs.
- The durable story is hybrid: external/pro-code agents plus low-code/UiPath-native governance.

What he is likely to reward:

```text
1. Clear proof that an external or coded agent participates in a UiPath-governed business workflow.
2. Governance and observability language: audit logs, human-in-the-loop, deployment, rollback, traceability.
3. A demo where UiPath handles orchestration, monitoring, human approval, and enforcement.
4. A practical enterprise scenario with sensitive data, business rules, and failure handling.
```

What he is likely to dislike:

```text
1. A standalone LLM demo with UiPath as decoration.
2. A chatbot that only advises but never governs or executes.
3. A complex multi-agent story without operational controls.
4. Claims of autonomy that ignore human accountability and auditability.
```

Sources:

- https://www.uipath.com/blog/taqi-jaffri/
- https://www.uipath.com/blog/product-and-updates/llamaindex-fast-tracks-enterprise-grade-agentic-automation-development
- https://www.uipath.com/blog/product-and-updates/langgraph-uipath-advancing-agentic-automation-together
- https://siliconangle.com/2024/10/29/agentic-automation-uipathforward-2/
- https://www.thecube.net/events/uipath/uipath-fusion-2025/agenda

## Ingo Philipp taste profile

Observed public themes:

- Agentic testing should move testers from mechanical automation toward risk thinking, better questions, and quality insight.
- AI test generation volume is not enough; the system must avoid the illusion of coverage.
- The strongest testing work identifies what matters, why it matters, and which risks remain.
- Agentic testing should cover the lifecycle: design, automation, execution, management, failure analysis, and repair.
- Test Cloud plus Agent Builder plus Maestro becomes compelling when it creates a continuous, governed testing flow rather than isolated AI helpers.

What he is likely to reward:

```text
1. Risk-driven test selection over generic test generation.
2. Clear distinction between AI suggestions and trusted evidence.
3. Failure analysis and repair recommendations tied to concrete test results.
4. Human judgment and Action Center approval for high-impact decisions.
5. A small set of risk-revealing tests, not a large pile of shallow AI-generated tests.
```

What he is likely to dislike:

```text
1. "AI generated many tests" without explaining why those tests matter.
2. Coverage theater: dashboards that look green but do not expose the real risk.
3. Treating testing like a factory line instead of an investigation.
4. Removing testers/humans from judgment rather than amplifying them.
```

Sources:

- https://www.uipath.com/blog/ingo-philipp/
- https://www.uipath.com/blog/ai/how-ai-is-changing-software-testing
- https://www.uipath.com/blog/product-and-updates/how-uipath-test-cloud-paves-way-for-agentic-autonomous-qa
- https://www.uipath.com/blog/product-and-updates/how-ai-agents-transforming-software-testing-technical-tuesday
- https://www.uipath.com/resources/automation-webinars/forrester-agentic-testing-webinar

## Prior AgentHack winners and finalists

Observed pattern from the 2025 finalist/winner posts:

- Winners and finalists leaned toward named enterprise problems: clinical trial review, healthcare claims, welfare analysis, procure-to-pay, flaky-test insights, synthetic test data, production support.
- Strong projects used multiple UiPath surfaces, not just one component.
- Agentic Testing finalists were often about reducing QA triage, identifying flakiness/redundancy, generating tests, synthetic test data, and production support.
- Special awards rewarded business readiness, innovative workflow, cross-platform integration, best Agent Builder use, and product feedback.

Source:

- https://forum.uipath.com/t/we-are-thrilled-to-unveil-the-uipath-agenthack-finalist-teams/3295981
- https://forum.uipath.com/t/here-are-the-uipath-agenthack-2025-winners/3586396
- https://forum.uipath.com/t/anomaly-detection-redundancy-elimination-flaky-test-insights-with-uipath-agents/2878943
- https://forum.uipath.com/t/uipath-agentic-ai-hackathon-team-deepprompt-genesis-flow/2878773

Implication for Agentic Test Swarm:

```text
Our project should not present as "AI safety research."
It should present as enterprise QA/productivity infrastructure:
testing AI workers before they can touch production tools.
```

## How Agentic Test Swarm currently matches the taste

Strong matches:

- Taqi fit: external coded agents plus UiPath-native Agent Builder proof plus API Workflow runtime enforcement.
- Taqi fit: Action Center approval, evidence hashes, runtime permit, and `deny_and_suspend` make governance visible.
- Ingo fit: risk-driven tests, TC-006 incident-to-regression memory, failure analysis, repair candidate, targeted re-test.
- Ingo fit: deterministic oracle prevents trusting AI-generated tests blindly.
- Official fit: Test Manager project, Action Center task, API Workflow proof, Studio Web Agent debug proof, public repo, and live endpoint.

Weak spots:

- The live Test Manager execution is still historical five-case evidence, while TC-006 is assigned but not in a fresh completed six-case execution.
- The demo can still become too Vercel-heavy if it starts from `live-swarm-view`.
- Some existing copy says "permit/license" too early. For Ingo, the testing swarm should be the product; the permit is the output.
- The business metric story needs to be spoken in the video, not just written in README.

## Judge-specific demo strategy

### First 30 seconds

Do not start with:

```text
We built a license system.
```

Start with:

```text
We built a UiPath-orchestrated testing swarm for AI workers. It attacks an AI workflow, records Test Cloud evidence, analyzes the failure, repairs and re-tests the risk, gates approval in Action Center, and then enforces the result through API Workflow.
```

Why:

- Taqi hears: UiPath governs external and native agents.
- Ingo hears: testing is risk investigation, not test generation volume.

### Taqi-oriented shots

Must show:

```text
1. Studio Web / API Workflow as the start.
2. UiPath-native Failure Analyst Agent debug success.
3. Action Center pending approval.
4. API Workflow runtime `deny_and_suspend`.
```

Narration:

```text
External agents propose tests and repairs, but UiPath owns orchestration, evidence, human approval, and runtime enforcement.
```

### Ingo-oriented shots

Must show:

```text
1. TC-001 raw PII failure.
2. Test Selector choosing critical tests by risk/change impact.
3. Failure Analyst explaining why the failure matters.
4. TC-006 incident memory for new phone-number export surface.
```

Narration:

```text
The swarm does not maximize test count. It selects the smallest risk-revealing set and turns incidents into permanent regression evidence.
```

## Final video edits to prioritize

P0:

- Start on UiPath, not Vercel.
- Say "risk-revealing tests" once.
- Say "the permit is the output, not the product" once.
- Show the UiPath-native Agent debug trace with `1 Agents.LLMCalls`.
- Show Action Center task `#3545796` pending before claiming enforcement.
- Show API Workflow `deny_and_suspend`.

P1:

- If there is time, record a fresh six-case Manual Execution Assistant run including TC-006.
- If not, narrate clearly that TC-006 is live and assigned under `Static Assignment (6)`, while the historical execution is five-case evidence.

P2:

- Add one sentence to Devpost:

```text
Agentic Test Swarm follows the testing principle that AI should amplify judgment, not replace it: agents generate attack ideas and repair candidates, deterministic oracles define expected behavior, Test Cloud records evidence, and Action Center keeps humans accountable.
```

## Recommended final positioning

Use this exact framing:

```text
Agentic Test Swarm is not a generic AI test generator.
It is a UiPath-governed quality system for AI workers.
It turns risky AI-agent behavior into risk-revealing tests, targeted repairs, managed Test Cloud evidence, human approval, and enforceable runtime permissions.
```

## Decision

Do not add a new large feature.

The highest expected score gain is:

```text
1. Judge-tailored demo narration.
2. UiPath-first screen order.
3. Explicit risk-thinking language.
4. Show UiPath-native Agent debug success.
5. Keep product feedback polished.
```

This aligns with both visible judges: Taqi gets enterprise agentic automation with governance; Ingo gets risk-driven agentic testing with evidence-backed judgment.
