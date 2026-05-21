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

## Next Research Queue

Label: next research queue

1. Compare top Devpost AI-agent/testing projects and extract what makes their demos feel judge-ready.
2. Deep-read UiPath Test Cloud agentic testing docs and identify one more platform-native proof point.
3. Search for real-world failures in AI-generated tests, prompt injection, and agent-to-agent data leakage.
4. Audit the demo script against official judging criteria after every major source-backed finding.
5. Decide whether a fresh six-case Manual Execution Assistant run is worth the risk before recording.
