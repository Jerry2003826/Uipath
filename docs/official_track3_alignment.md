# Official Track 3 Alignment

This file maps Agentic Test Swarm to the official UiPath AgentHack Track 3 prompt and judging criteria. It is written for reviewers who need to quickly see why the project is an agentic testing solution rather than a standalone Python app with UiPath screenshots attached.

## Official Track 3 requirements

Track 3 asks for agents that use UiPath Test Cloud to reimagine how software testing is designed, automated, executed, and managed across enterprise environments.

Agentic Test Swarm aligns to that by making the AI testing agents the main product:

- Policy Miner turns business requirements into test obligations.
- Red-Team Agent generates adversarial AI-workflow scenarios.
- Test Designer Agent converts attacks into Test Cloud certification cases.
- Test Selector Agent chooses tests by risk, coverage, tool-surface change, and failure history.
- Failure Analyst Agent explains failing evidence and recommends repair scope.
- Repair Agent proposes a coding-agent-backed guardrail patch.
- Re-test Orchestrator runs targeted regression evidence.
- Quality Governor converts passed evidence into a restricted runtime permit.

The permit is the output of the test swarm, not the product.

## Business Impact & Adoption Potential

Enterprise teams increasingly need to decide whether AI agents can call tools, APIs, and other agents that expose customer data. Manual prompt review does not create repeatable evidence.

Agentic Test Swarm targets these business outcomes:

- reduce manual AI workflow review from hours to a short Test Cloud and Action Center evidence review;
- improve coverage when new tool surfaces appear, such as `TC-006` for phone-number export;
- turn runtime incidents into permanent regression coverage;
- preserve human accountability for high-risk access through Action Center;
- give QA, automation, and platform teams a reusable certification pattern for AI-infused workflows.

The Continuous Quality Memory layer makes this explicit:

```text
Runtime incidents become permanent UiPath Test Cloud regression evidence.
```

## Platform Usage

UiPath is the control plane:

- Test Cloud / Test Manager stores generated tests, selected tests, failed evidence, and re-test evidence.
- Studio Web / Maestro models the swarm lifecycle and makes the operator path visible.
- API Workflow is the governed runtime proxy and one-click run trigger.
- Action Center gates the restricted runtime permit before activation.
- Automation Cloud keeps the workflow, tests, approval, and proxy inside one governed tenant.

External frameworks and LLMs are allowed, but they are supporting workers. They propose attacks and repairs; UiPath orchestrates, records, gates, and enforces the outcome.

## Technical Execution, Feasibility & Versatility

The worker service is deterministic for demo reliability and production explainability:

- expected results come from a deterministic oracle, not an LLM opinion;
- the Quality Governor compiles permits from evidence, approval, and policy rules;
- `/license-decision` denies or suspends blocked raw PII actions;
- `/continuous-quality-memory` shows how runtime incidents become future Test Cloud gates;
- `/evidence-graph` links trace -> policy -> test -> repair -> approval -> runtime enforcement;
- evidence hashes connect runtime decisions back to the certified test evidence;
- the public Vercel worker exposes browser-friendly and API-friendly endpoints for UiPath to call.

The project handles the core edge case the demo is built around: a prompt-injected agent-to-agent raw PII export request.

## Completeness of Delivery

Current delivery artifacts:

- public GitHub repository with README and setup instructions;
- public deployed endpoint at `https://permitops-uipath.vercel.app`;
- working local pytest suite;
- Test Manager / Test Cloud evidence screenshots;
- Action Center pending approval evidence;
- Studio Web / API Workflow debug evidence;
- Continuous Quality Memory evidence at `evidence/case_001/continuous_quality_memory.json`;
- Evidence Graph evidence at `evidence/case_001/evidence_graph.json`;
- Devpost pitch and demo scripts;
- presentation deck draft at `assets/agentic_test_swarm_deck.pptx`.

## Creativity & Innovation

Most AI governance demos start with permissions. Agentic Test Swarm starts with testing.

The novel framing is:

```text
AI testing agents attack, repair, re-test, and certify an AI workflow.
The runtime permit is only the final governance artifact.
```

That framing keeps the project in Track 3 while still showing production-grade governance.

## Coding-agent bonus

The project documents coding-agent usage in the README and `docs/coding_agent_evidence.md`.

Coding agents contribute to:

- adversarial scenario generation;
- repair candidate design;
- API Workflow payload scaffolding;
- documentation and demo packaging.

Their output is not trusted automatically. It must pass deterministic expected-oracle checks and become Test Cloud evidence before the Quality Governor can use it.

## Remaining gap

The strongest remaining gap is live platform polish, not backend capability.

The repo already contains the public worker, local deterministic run, Test Cloud evidence, Action Center evidence, and API Workflow proof. The final video should make the UiPath surfaces visible in this order:

1. Studio Web / API Workflow starts the one-click runbook.
2. Test Manager / Test Cloud shows certification evidence and TC-006 incident memory.
3. Action Center shows the restricted permit approval task.
4. API Workflow shows runtime denial with `deny_and_suspend`.

## Action before submission

Before final Devpost submission:

- record a fresh under-five-minute demo with UiPath screens first and the Vercel page second;
- keep Action Center task `#3545796` pending until the live approval moment;
- show live TC-006 in Test Manager as `PVACPOV91:76` and `Static Assignment (6)`;
- include the deck, README, setup instructions, coding-agent evidence, and product feedback notes.
