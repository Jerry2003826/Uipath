# UiPath Native Depth Gap Research - 2026-05-23

Question:

```text
After adding the UiPath-native Failure Analyst Agent and native agent pack, what
is still missing if judges look specifically for UiPath-native agent depth and
no-code platform value?
```

## Sources checked

- UiPath AgentHack official page: https://uipath-agenthack.devpost.com/
- UiPath AgentHack FAQ: https://community.uipath.com/agenthack-faq/
- UiPath Test Cloud agentic testing page: https://www.uipath.com/platform/agentic-testing
- UiPath Forrester agentic testing webinar page: https://www.uipath.com/resources/automation-webinars/forrester-agentic-testing-webinar
- UiPath Agents docs, About UiPath Agents: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/about-uipath-agents
- UiPath Agents docs, Building an agent in Studio Web: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/building-an-agent
- UiPath Agents docs, Tools: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/tools-agent-builder
- UiPath Agents docs, Escalations and Agent Memory: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/escalations-agent-builder
- UiPath Agents docs, Best practices for building agents: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/best-practices-for-building-agents
- UiPath Test Manager docs, Generate tests for requirements: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/generating-manual-test-cases
- UiPath Test Manager docs, Testing Process Governance: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/testing-process-governance
- UiPath Python SDK docs through Context7: `/uipath/uipath-python`
- UiPath LangChain SDK docs through Context7: `/uipath/uipath-langchain-python`
- Taqi Jaffri hybrid automation interview: https://diginomica.com/uipath-explains-hybrid-automation-architecture-why-agents-need-workflows-not-other-way-around
- Ingo Philipp agentic testing session listing: https://conference.eurostarsoftwaretesting.com/event/2026/accelerate-the-agentic-enterprise-with-agentic-testing/

## Source-backed signals

### 1. UiPath-native agents are made of Prompt / Context / Tools / Escalations

The AgentHack FAQ and Agents docs consistently describe agents as more than
LLM prompts. The native shape is:

```text
Prompt / Context / Tools / Escalations
```

Project status:

```text
Prompt: strong
Tools: medium-strong
Escalations: strong
Context: medium
```

Evidence already present:

- Prompt: the Failure Analyst Agent prompt and the Policy Miner / Red-Team /
  Test Designer specs.
- Tools: API Workflow runtime proxy and worker endpoints.
- Escalations: Action Center task `#3545796`.
- Context: captured trace, policy pack, Test Cloud evidence, and Evidence Graph.

Gap:

```text
Context Grounding and Agent Memory are currently represented as a design pattern,
not a live UiPath-native configuration.
```

Recommendation:

```text
Do not block final submission on live Context Grounding setup.
Instead, explicitly narrate that Agentic Test Swarm implements the same native
agent shape: Prompt / Context / Tools / Escalations.
```

## 2. Tool guardrails and tool simulations are a strong UiPath-native angle

The Agents docs emphasize that tools turn reasoning into action, and that tool
guardrails and tool simulations help test agent behavior before using real
systems.

Project status:

```text
We already have an external runtime guardrail:
API Workflow -> /license-decision -> deny_and_suspend
```

Gap:

```text
We do not yet have a live UiPath Agent Builder tool guardrail or tool simulation
screen for the Customer Data Agent.
```

Recommendation:

P0 demo-language upgrade:

```text
Say: "In production this maps naturally to UiPath Agent Builder tool guardrails
and tool simulations. In the current prototype, the same tested policy is
enforced by the UiPath API Workflow proxy."
```

P1 product-feedback upgrade:

```text
Ask UiPath for a first-class way to promote Test Cloud evidence into Agent
Builder tool guardrails and simulations.
```

P2 post-submission build path:

```text
Create a Customer Data Agent in Agent Builder with:
- tool: Licensed Tool Proxy API Workflow
- guardrail: block raw PII export unless permit scope allows it
- simulation: executive override raw email export
- escalation: raw PII approval via Action Center
```

Do not disturb Action Center task `#3545796` for this before the final recording.

## 3. Test Cloud native Autopilot and Healing Agent should be positioned, not forced

UiPath Test Cloud messaging highlights Autopilot for Testers, custom testing
agents with Agent Builder, test management, traceability, analytics, self-healing,
and managed evidence.

Project status:

```text
We use Test Manager / Test Cloud as the managed certification evidence layer.
We implement our own testing agents for policy mining, red-team generation,
test design, failure analysis, repair recommendation, and targeted re-test.
```

Gap:

```text
We are not using built-in Autopilot for Testers or Healing Agent as the main
execution engine.
```

Recommendation:

Do not pivot. The official page welcomes external frameworks and LLMs. Our
stronger story is:

```text
Autopilot and Healing Agent are UiPath's built-in testing agents.
Agentic Test Swarm shows the custom-agent pattern for AI workflow certification:
custom testing agents create the evidence, Test Cloud manages it, and UiPath
governs the result.
```

This keeps Track 3 alignment without claiming features we did not run.

## 4. Test Manager governance is a product-fit angle

Test Manager includes Testing Process Governance concepts, while AgentHack asks
for humans to remain in the loop for high-impact decisions.

Project status:

```text
We use Action Center as the human accountability gate.
We use Test Manager as the evidence repository.
```

Gap:

```text
We do not have Test Manager governed test case approval turned on for TC-001
through TC-006.
```

Recommendation:

Do not enable extra governance settings right before final recording unless the
sandbox is stable and reversible.

Instead, frame the current workflow as:

```text
Test Manager stores test evidence.
Action Center owns human approval.
Evidence Graph links both.
```

P1 product-feedback upgrade:

```text
Request a native "AI workflow certification evidence" object that spans Test
Manager governance, Action Center approval, API Workflow runtime decisions, and
Agent Builder traces.
```

## 5. Taqi and Ingo taste alignment

Taqi-oriented implication:

```text
Agents need workflows because enterprise risk needs constraints, auditability,
and human approval. Our demo must show UiPath as the workflow constraint, not
only as a screenshot.
```

Ingo-oriented implication:

```text
Agentic testing should help testers design meaningful tests, assess risk, and
deliver insight. Our demo should emphasize TC-001, TC-006, targeted re-test, and
Failure Analyst output more than the permit YAML.
```

## Final gap matrix

| Area | Current strength | Remaining gap | Action |
| --- | --- | --- | --- |
| Prompt | Strong | None | Show native Failure Analyst prompt briefly. |
| Context | Medium | No live Context Grounding / Agent Memory screen | Explain captured trace + Evidence Graph as context package; add product feedback. |
| Tools | Medium-strong | No live Agent Builder tool guardrail/simulation | Show API Workflow proxy now; mention native guardrail/simulation mapping. |
| Escalations | Strong | Final approval not clicked yet by design | Keep `#3545796` pending until recording. |
| Test Cloud | Strong | Built-in Autopilot/Healing Agent not used | Position as custom Test Cloud agent pattern, not built-in Autopilot clone. |
| Governance | Strong | Cross-product evidence object is external | Use Evidence Graph and product feedback. |

## Decision

Do not add another large runtime feature before the final video.

The highest score gain is a precise UiPath-native framing:

```text
Agentic Test Swarm follows UiPath's native agent shape:
Prompt / Context / Tools / Escalations.

The swarm uses prompts to define testing roles, context from captured traces and
Test Cloud evidence, tools through API Workflow and worker endpoints, and
escalations through Action Center.

The remaining product opportunity is to make Test Cloud evidence directly
promotable into Agent Builder tool guardrails, tool simulations, Agent Memory,
and cross-product evidence graphs.
```

## Demo script insertion

Use this after the UiPath-native Failure Analyst Agent shot:

```text
This is not just an external LLM demo. UiPath-native agents are built from
prompt, context, tools, and escalations. Our Failure Analyst runs in Studio Web.
Its context is the captured trace and Test Cloud evidence. Its tools are the
API Workflow and worker endpoints. Its escalation path is Action Center. The
runtime guardrail is enforced by API Workflow, and the Evidence Graph links the
whole chain.
```
