# AgentHack Award Gap Research - 2026-05-21

## Research Plan

Question:

What does Agentic Test Swarm still need in order to look like an award-grade UiPath Test Cloud submission rather than a Python demo with UiPath evidence around it?

Method:

1. Re-read official AgentHack rules, Track 3 language, and submission requirements.
2. Check UiPath's current Test Cloud, agentic testing, and coding-agents positioning.
3. Use Context7 for current UiPath SDK documentation and Firecrawl/Exa for source discovery.
4. Compare 2025 AgentHack winner patterns against our current artifacts.
5. Convert the findings into a prioritized action list.

Tools used:

- Superpowers: research planning and source-backed decision discipline.
- Context7: current UiPath SDK documentation.
- Firecrawl search: official and community source discovery.
- Exa semantic search: related AgentHack and agentic testing discovery.
- Web search: official Devpost, UiPath product pages, and community/winner pages.

## Source Snapshot

- AgentHack homepage: https://uipath-agenthack.devpost.com/
- AgentHack rules and judging criteria: https://uipath-agenthack.devpost.com/rules
- AgentHack Track 3 details: https://uipath-agenthack.devpost.com/details/tracks
- UiPath Community AgentHack announcement: https://forum.uipath.com/t/uipath-agenthack-is-live-50-000-in-prizes-three-tracks-and-7-weeks-to-build/5746132
- UiPath Test Cloud agentic testing page: https://www.uipath.com/platform/agentic-testing
- UiPath agentic QA blog: https://www.uipath.com/blog/product-and-updates/how-uipath-test-cloud-paves-way-for-agentic-autonomous-qa
- UiPath Agent Builder for testing: https://www.uipath.com/platform/agentic-testing/agent-builder-for-testers
- UiPath for Coding Agents: https://www.uipath.com/developers/coding-agents
- UiPath CLI with coding agents docs: https://docs.uipath.com/uipath-cli/standalone/latest/user-guide/coding-agents
- AgentHack 2025 recap: https://www.uipath.com/community-blog/community-news/uipath-community-annual-global-hackathon-2025
- AgentHack 2025 winners: https://forum.uipath.com/t/here-are-the-uipath-agenthack-2025-winners/3586396
- HyperHack 2024 winners: https://www.uipath.com/community-blog/community-news/uipath-community-hyper-hack-2024-winners

## Findings

### 1. Track 3 rewards a testing swarm, not a license dashboard

Official Track 3 asks for agents that evaluate requirements, create meaningful tests, identify fragile or outdated tests, recommend fixes, and coordinate tests based on risk, coverage, and change impact.

Agentic Test Swarm now matches that framing:

- `Policy Miner Agent` maps policy into obligations.
- `Red-Team Agent` generates adversarial AI workflow attacks.
- `Test Designer Agent` turns attacks into Test Cloud cases.
- `Test Selector Agent` picks the right tests by risk, coverage, changed tool scope, and failure history.
- `Failure Analyst Agent` explains failures.
- `Repair Agent` proposes a guardrail.
- `Re-test Orchestrator` re-runs targeted checks.
- `Incident Memory` converts a new raw phone-number export surface into `TC-006`.

Decision:

Keep the project name and public story as `Agentic Test Swarm`. Treat `PermitOps Runtime Permit` as the final artifact, not the product.

### 2. UiPath must be the visible control plane

Official language repeatedly says the solution must run on UiPath Automation Cloud, and external LLMs/frameworks are welcome only when UiPath is the execution, orchestration, and governance layer.

Agentic Test Swarm already has the right proof pieces:

- Test Manager project `PVACPOV91`.
- Test set `PVACPOV91:6 - PermitOps Certification Evidence`.
- Live `PVACPOV91:76 - TC006 incident memory blocks phone-number export`.
- Action Center pending task `#3545796`.
- API Workflow proof for `deny_and_suspend`.
- Studio Web / Maestro lifecycle proof.

Remaining risk:

If the demo starts on the Vercel page, judges may still read it as Python-first.

Decision:

The final video must start from UiPath screens: Studio Web or API Workflow, then Test Manager/Test Cloud, then Action Center, then API Workflow runtime enforcement. The Vercel page is supporting worker evidence, not the hero surface.

### 3. Test Cloud needs to feel like managed evidence, not a screenshot

UiPath's own Test Cloud messaging emphasizes agentic testing across lifecycle stages, including built-in/custom AI agents, API/UI testing, CI/CD and ALM integrations, governance, audit, and orchestration of agents, automations, and humans.

Our strongest Test Cloud proof is now:

- generated certification cases mapped in Test Manager;
- the five-case execution screenshot;
- `TC-006` live case and static assignment as incident-to-regression coverage;
- `test_selector_decision.json` and `incident_antibody_tests.json` explaining why the suite changed.

Decision:

Do not rerun or disturb Test Manager unless necessary. In the final video, explicitly say Test Cloud is where generated and selected tests become managed certification evidence. Show `Static Assignment (6)` because it proves the suite evolved after the incident.

### 4. Coding-agent bonus is real, but our current proof is not yet ideal

Official rules say up to 2 bonus points require documenting the tool used, how it contributed, and evidence that the output is meaningfully integrated into the working solution.

Our current proof:

- `docs/coding_agent_evidence.md`
- `docs/coding_agents_bonus_pack.md`
- `evidence/case_001/coding_agent_prompts.jsonl`
- `evidence/case_001/coding_agent_outputs.jsonl`
- red-team scenarios and repair summaries connected to Test Cloud evidence.

Gap:

This workstation currently has no visible `uip` CLI installation evidence, and the repo does not yet show a captured `uip skills install --agent codex` or verification transcript. The architecture references UiPath for Coding Agents, but the bonus would be stronger if we capture the UiPath skills setup and one Codex session that uses those skills for a UiPath artifact.

Decision:

Before submission, add a visible UiPath for Coding Agents proof pack:

1. Install or verify `@uipath/cli`.
2. Run `uip login` if the account session allows it.
3. Run `uip skills install --agent codex --local` in this repo.
4. Capture the generated `.agents/skills` content or command transcript.
5. Ask Codex to scaffold or validate a UiPath API Workflow payload using the installed UiPath skills.
6. Add the transcript to `docs/coding_agents_bonus_pack.md`.

### 5. A UiPath-native Agent Builder test agent would be the highest-leverage sandbox upgrade

UiPath's testing pages highlight Agent Builder for custom testing agents and use cases such as data retrievers, bug consolidators, results messengers, and compliance checkers.

Our current agents are clear in code and evidence, but most are external/coded worker agents rather than live UiPath-native Agent Builder agents.

Decision:

If sandbox access exposes Agent Builder, create exactly one UiPath-native testing agent first:

```text
Failure Analyst Agent
Input: Test Cloud result summary + captured trace + expected oracle result
Output: root cause, risk impact, recommended repair, targeted re-test list
```

Why this one:

- It maps directly to official Track 3 language about recommending fixes when automation breaks.
- It is easier to demo than a full red-team agent.
- It gives judges a visible low-code/no-code AI agent inside UiPath.
- It does not replace deterministic pass/fail logic.

### 6. Prior winners favor real business impact and complete demos

The 2025 recap says the event focused on Agent Builder, Maestro, and Coded Agents, with 400+ submissions from 50+ countries and winners across enterprise agents and agentic testing. The 2025 winners list highlights real production-grade problem framing, category clarity, and live demo completeness.

Decision:

Do not make the project bigger by adding unrelated systems such as AstrBot or SuperRAG before submission. They may be useful later, but they risk weakening Track 3 clarity. The current strongest business problem is controlled validation of AI-infused workflows that touch sensitive customer data.

## Priority Action List

P0 - Final demo ordering:

- Start in UiPath, not Vercel.
- Show Studio Web / API Workflow control-plane trigger.
- Show Test Manager/Test Cloud with `PVACPOV91:76` and `Static Assignment (6)`.
- Show Action Center task `#3545796` pending.
- Show API Workflow runtime `deny_and_suspend`.

P0 - Coding agents bonus hardening:

- Capture UiPath for Coding Agents setup evidence if `uip` can be installed and logged in.
- Add a short transcript showing Codex using UiPath-specific skills for workflow payload or validation work.

P1 - Sandbox enhancement:

- Completed partial sandbox proof: created/configured one UiPath-native Studio Web Autonomous Agent draft, `Generate incident tickets from logs 1 2`, as the `Agentic Test Swarm Failure Analyst Agent`.
- Selected UiPath model `gpt-5.4-2026-03-05`.
- Preserved the template `{{log_chunk}}` input so the agent can accept a Test Cloud evidence package without invalid prompt variables.
- Remaining platform blocker: the template `Create Issue` integration tool needs a connection before debug/publish.
- Evidence: `assets/uipath_failure_analyst_agent_model_selected.png` and `evidence/case_001/uipath_failure_analyst_agent_model_selected.txt`.

P1 - Submission copy:

- Add one line everywhere important: `External LLMs propose tests and repairs; UiPath orchestrates, records, approves, and enforces.`
- Keep `Agentic Test Swarm` as the main name and `PermitOps Runtime Permit` as the final output.

P2 - Do not expand scope:

- Do not integrate AstrBot/SuperRAG before the first submission unless the demo is already recorded and stable.
- Do not create a new Test Manager execution unless recording needs it.
- Do not approve Action Center task `#3545796` before the final demo.

## Bottom Line

Agentic Test Swarm is already directionally aligned with Track 3. The highest-score path is not adding more backend complexity. It is making the existing chain feel unmistakably UiPath-native:

```text
UiPath starts the run
-> AI testing agents generate and select tests
-> Test Cloud stores evidence
-> coding agent proposes repair
-> Action Center keeps human approval
-> API Workflow enforces the tested result
```
