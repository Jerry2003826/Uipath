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

## Next Research Queue

Label: next research queue

1. Capture UiPath for Coding Agents setup evidence if `uip` login works.
2. If sandbox exposes Agent Builder, create one visible `Failure Analyst Agent`.
3. Compare top Devpost AI-agent/testing projects and extract what makes their demos feel judge-ready.
4. Search for real-world failures in AI-generated tests, prompt injection, and agent-to-agent data leakage.
5. Audit the demo script against official judging criteria after every major source-backed finding.
6. Decide whether a fresh six-case Manual Execution Assistant run is worth the risk before recording.
