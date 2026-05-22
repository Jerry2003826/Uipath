# Research Log

## 2026-05-21 - Research stack installed

Question:

How should we equip Codex to keep deeply researching Agentic Test Swarm instead
of only reacting to one-off prompts?

Sources:

- UiPath AgentHack rules: https://uipath-agenthack.devpost.com/rules
- UiPath AgentHack homepage: https://uipath-agenthack.devpost.com/
- UiPath AgentHack resources: https://uipath-agenthack.devpost.com/resources
- UiPath for Coding Agents launch: https://www.uipath.com/newsroom/uipath-for-coding-agents-launch
- UiPath Test Cloud May 2026 release notes: https://docs.uipath.com/test-cloud/automation-cloud/latest/release-notes/dedicated-may-2026
- Firecrawl MCP Server docs: https://github.com/firecrawl/firecrawl-mcp-server
- Exa MCP Server docs: https://github.com/exa-labs/exa-mcp-server

Findings:

- The project needs a research stack that can cover broad discovery, semantic
  discovery, full-page extraction, current technical docs, repo inspection, and
  visible browser proof.
- The machine already had Brave Search, Tavily, Crawl4AI, Context7, GitHub MCP,
  Playwright, Browser/Chrome, Sequential Thinking, Superpowers, and Trail of
  Bits skills.
- Firecrawl and Exa fill the remaining research gaps: multi-page extraction and
  semantic discovery.
- Both Firecrawl and Exa require API keys for live tool calls:
  `FIRECRAWL_API_KEY` and `EXA_API_KEY`.

Impact on Agentic Test Swarm:

- Future research can compare official UiPath messaging, competitor examples,
  Devpost patterns, agentic testing articles, and security/governance research
  without losing conclusions in chat history.
- Firecrawl should be used when a page or domain needs clean extraction.
- Exa should be used when keyword search misses conceptually related projects.

Decision:

Install/configure Firecrawl and Exa MCP entries in local Codex config, install
Firecrawl project skills, and make this research log the persistent decision
record for future deep-research passes.

Action taken:

- Added local Codex MCP entries for `firecrawl` and `exa`.
- Installed Firecrawl build skills into `.agents/skills/`.
- Added `docs/research_workbench.md`.
- Added this initial `docs/research_log.md`.

Open risk:

- Firecrawl and Exa are configured but not fully live until valid
  `FIRECRAWL_API_KEY` and `EXA_API_KEY` values are supplied.

## 2026-05-21 - AgentHack award gap deep dive

Question:

What does Agentic Test Swarm still need in order to look like an award-grade
UiPath Test Cloud submission rather than a Python demo with UiPath evidence
around it?

Sources:

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

Findings:

- Track 3 rewards the testing swarm narrative: requirements to tests, fragile
  or risky test selection, failure analysis, repair recommendation, targeted
  re-test, and validation of AI-infused workflows.
- External LLMs and frameworks are allowed, but UiPath must remain the
  execution, orchestration, and governance layer.
- The current project already has strong platform proof: Test Manager project
  `PVACPOV91`, test set `PVACPOV91:6`, live `PVACPOV91:76`, pending Action Center task `#3545796`, API Workflow `deny_and_suspend`, and Studio Web/Maestro lifecycle screenshots.
- The current weakest bonus area is UiPath for Coding Agents evidence. Codex
  artifacts exist, but a captured `uip skills install --agent codex` or
  equivalent UiPath-skills transcript would make the bonus claim stronger.
- If sandbox exposes Agent Builder, the highest-leverage native agent is a
  `Failure Analyst Agent` because it maps directly to Track 3 repair guidance.

Impact on Agentic Test Swarm:

- Keep `Agentic Test Swarm` as the public name and keep `PermitOps Runtime
  Permit` as the final output only.
- The final demo must start from UiPath screens rather than the Vercel worker.
- Test Cloud should be described as managed certification evidence, not just
  screenshot proof.
- Do not add AstrBot/SuperRAG before first submission because it would dilute
  Track 3 clarity.

Decision:

Make the next submission-hardening pass focus on UiPath-visible evidence:
demo ordering, coding-agent bonus proof, and one optional Agent Builder
Failure Analyst if sandbox access permits it.

Action taken:

- Added `docs/research_findings_2026-05-21_agenthack_award_gap.md`.
- Added a regression test so the research finding remains part of the
  submission proof pack.

Open risk:

- The repo still needs live `uip` CLI / UiPath for Coding Agents installation
  evidence before we can claim the strongest possible coding-agent bonus.

## 2026-05-23 - Judge taste research

Question:

What are the visible UiPath AgentHack judges likely to reward, and how should
the final Agentic Test Swarm demo adapt?

Sources:

- AgentHack homepage and judge list: https://uipath-agenthack.devpost.com/
- AgentHack official rules: https://uipath-agenthack.devpost.com/rules
- AgentHack Track 3 guidance: https://uipath-agenthack.devpost.com/details/tracks
- Taqi Jaffri UiPath profile: https://www.uipath.com/blog/taqi-jaffri/
- Taqi Jaffri LlamaIndex article: https://www.uipath.com/blog/product-and-updates/llamaindex-fast-tracks-enterprise-grade-agentic-automation-development
- Taqi Jaffri LangGraph article: https://www.uipath.com/blog/product-and-updates/langgraph-uipath-advancing-agentic-automation-together
- Ingo Philipp UiPath profile: https://www.uipath.com/blog/ingo-philipp/
- Ingo Philipp testing article: https://www.uipath.com/blog/ai/how-ai-is-changing-software-testing
- Ingo Philipp Test Cloud article: https://www.uipath.com/blog/product-and-updates/how-uipath-test-cloud-paves-way-for-agentic-autonomous-qa
- AgentHack 2025 winners: https://forum.uipath.com/t/here-are-the-uipath-agenthack-2025-winners/3586396
- AgentHack 2025 finalists: https://forum.uipath.com/t/we-are-thrilled-to-unveil-the-uipath-agenthack-finalist-teams/3295981

Findings:

- Taqi Jaffri's public product writing points toward enterprise-grade agentic
  automation: external/pro-code agents are valuable, but UiPath should provide
  deployment, orchestration, monitoring, security, auditability, and
  human-in-the-loop governance.
- Ingo Philipp's public testing writing points toward risk thinking rather than
  test-volume theater: AI should help testers ask what matters and why, not just
  generate more checks.
- Prior AgentHack winners/finalists tended to have concrete enterprise use
  cases, named business pain, multiple UiPath surfaces, and clear community or
  product value.

Impact on Agentic Test Swarm:

- Keep the testing swarm as the product and the permit as the output.
- In the video, say "risk-revealing tests" and "AI amplifies judgment, not
  replaces it."
- Show the UiPath-native Failure Analyst Agent debug trace because it speaks to
  Taqi's native/external-agent blend and Ingo's failure-analysis lifecycle.
- Use TC-006 as the strongest Ingo-oriented proof: incident-to-regression memory
  for a new phone-number export surface.

Decision:

Do not add a new large feature. The highest expected score gain is judge-tailored
demo narration and proof ordering.

Action taken:

- Added `docs/judge_taste_research_2026-05-23.md`.
- Linked the research from README and `docs/judge_scorecard.md`.
- Updated `docs/final_video_shot_list.md` and
  `docs/devpost_submission_package.md` with judge-tuned phrasing.

Open risk:

- If the final video starts from Vercel instead of UiPath, the Taqi/platform
  usage score can still suffer despite strong backend proof.

## 2026-05-23 - UiPath-native depth gap deep dive

Question:

What is still missing if judges look specifically for UiPath-native agent depth
and no-code platform value?

Sources:

- AgentHack official page: https://uipath-agenthack.devpost.com/
- AgentHack FAQ: https://community.uipath.com/agenthack-faq/
- UiPath Test Cloud agentic testing page: https://www.uipath.com/platform/agentic-testing
- UiPath Forrester agentic testing webinar: https://www.uipath.com/resources/automation-webinars/forrester-agentic-testing-webinar
- UiPath Agents docs, About Agents: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/about-uipath-agents
- UiPath Agents docs, Tools: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/tools-agent-builder
- UiPath Agents docs, Escalations and Agent Memory: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/escalations-agent-builder
- UiPath Agents docs, Best practices: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/best-practices-for-building-agents
- UiPath Test Manager docs, Testing Process Governance: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/testing-process-governance
- UiPath Python SDK and LangChain SDK docs via Context7.
- Taqi Jaffri hybrid automation interview: https://diginomica.com/uipath-explains-hybrid-automation-architecture-why-agents-need-workflows-not-other-way-around
- Ingo Philipp agentic testing session listing: https://conference.eurostarsoftwaretesting.com/event/2026/accelerate-the-agentic-enterprise-with-agentic-testing/

Findings:

- UiPath-native agents should be explained as Prompt / Context / Tools /
  Escalations, not just "an LLM in Studio Web."
- Agentic Test Swarm is strongest on Prompt, Tools, and Escalations:
  native Failure Analyst prompt, API Workflow runtime proxy, and Action Center
  approval task `#3545796`.
- The remaining native-depth gaps are Context Grounding / Agent Memory, Agent
  Builder tool guardrails, and tool simulations. These are good product-feedback
  items and post-submission extensions, but they should not disturb the final
  Action Center recording path.
- Test Cloud Autopilot for Testers and Healing Agent should be positioned as
  related UiPath-native capabilities. The project is a custom Test Cloud agent
  pattern rather than a claim that we used those built-ins.

Impact on Agentic Test Swarm:

- Add the Prompt / Context / Tools / Escalations framing to README and demo
  narration.
- Add product feedback asking for Test Cloud evidence to become Agent Builder
  tool guardrails, tool simulations, Agent Memory, and cross-product evidence
  graphs.
- Keep final recording stable: do not click Action Center task `#3545796` until
  the final video.

Decision:

Do not add another risky live UiPath feature before recording. The score gain is
highest from clearer native-depth framing plus product feedback.

Action taken:

- Added `docs/uipath_native_depth_gap_research_2026-05-23.md`.
- Updated README, submission readiness, and product feedback wording.

## 2026-05-23 - Test Cloud native traceability deep dive

Question:

What still needs to be added if judges specifically inspect Agentic Test Swarm
for Test Cloud-native depth, not only general UiPath platform usage?

Sources:

- AgentHack Track 3 guidance: https://uipath-agenthack.devpost.com/details/tracks
- AgentHack rules and coding-agent bonus: https://uipath-agenthack.devpost.com/rules
- UiPath Test Manager docs, Quality-check requirements: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/evaluating-requirement-quality
- UiPath Test Manager docs, Generate tests for requirements: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/generating-manual-test-cases
- UiPath Test Manager docs, Finding obsolete tests based on requirements: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/finding-obsolete-tests-based-on-requirements
- UiPath Test Manager docs, AI-powered test insights: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/ai-powered-test-insights-best-practices
- UiPath Test Manager docs, Webhooks: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/webhooks
- UiPath Test Manager docs, Test Manager API integration: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/test-manager-api-integration
- UiPath Test Manager docs, Enabling Healing Agent: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/enabling-healing-agent
- UiPath Test Manager docs, Testing Process Governance: https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/testing-process-governance
- UiPath Python SDK docs through Context7.

Findings:

- The clearest remaining native-depth story is not adding more tests. It is
  making Test Cloud the visible system of record for the whole path:
  `Requirement -> Test Case -> Execution -> Defect -> Runtime Permit`.
- Current proof covers the middle and end of that chain: TC-001 through TC-006,
  a six-case Test Manager execution, Action Center approval gate, and API
  Workflow runtime denial.
- The most valuable next live Test Manager object is `REQ-PII-001`, linked to
  TC-001 through TC-006.
- The best new testing-agent role is `Obsolete Test Scout`, because official
  Track 3 and Test Manager docs both emphasize outdated / obsolete tests.
- Test Manager `Create Defect webhook` support is the cleanest way to connect a
  failed test result to Failure Analyst and Repair Agent evidence.
- Healing Agent should be positioned carefully: useful adjacent capability, but
  not something we used live.
- Testing Process Governance should be described as test-artifact sign-off,
  while Action Center remains runtime permit approval.

Impact on Agentic Test Swarm:

- Add `docs/test_cloud_native_gap_research_2026-05-23.md`.
- Add README/readiness/product-feedback/video wording for the native traceability
  chain.
- Do not disturb the pending Action Center task `#3545796`.

Decision:

Do not add another risky live UiPath feature before recording. If there is one
more platform pass, create `REQ-PII-001` and link it to TC-001 through TC-006.
Otherwise, use this research as final-video narration and product feedback.

Action taken:

- Added `docs/test_cloud_native_gap_research_2026-05-23.md`.
- Updated README, submission readiness, product feedback, and final-video shot
  list.

## Next Research Queue

Label: next research queue

1. Create Test Manager requirement `REQ-PII-001` and link TC-001 through TC-006.
2. Add Obsolete Test Scout evidence when requirements or tool schemas change.
3. Capture UiPath for Coding Agents setup evidence if `uip` login works.
4. Compare top Devpost AI-agent/testing projects and extract what makes their demos feel judge-ready.
5. Search for real-world failures in AI-generated tests, prompt injection, and agent-to-agent data leakage.
6. Audit the demo script against official judging criteria after every major source-backed finding.
7. Use the completed six-case Test Manager execution as the primary Test Cloud proof in final video review.
