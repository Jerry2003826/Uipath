# Continuous Research Workbench

Purpose: keep Agentic Test Swarm under active research instead of treating the
current demo as finished. Every deep-research pass should produce a decision
record, a source-backed finding, or a concrete repo/platform update.

## Installed Research Stack

Use this stack in layers:

| Layer | Tool | Use |
| --- | --- | --- |
| Broad discovery | Brave Search | Find news, forums, Devpost-style projects, and competitor language. |
| Deep web research | Tavily | Find current sources and summarize multi-source research questions. |
| Page extraction | Crawl4AI | Extract clean content from docs, blogs, and JS-heavy pages. |
| Web-data MCP | Firecrawl | Scrape, search, map, crawl, and extract sites when a research pass needs more than snippets. |
| Semantic discovery | Exa | Find conceptually similar projects and articles even when they do not share exact keywords. |
| Current docs | Context7 | Fetch current SDK, API, framework, and cloud-service documentation. |
| Repo evidence | GitHub MCP | Inspect open-source implementations, issues, and comparable project proof. |
| Browser proof | Browser / Chrome / Playwright | Capture UiPath, Vercel, Devpost, and competitor screenshots when visible proof matters. |
| Reasoning | Sequential Thinking + Superpowers | Turn raw sources into strategy, risks, implementation plans, and verification steps. |

Firecrawl and Exa are configured in the local Codex MCP config. They need real
API keys before live tool calls:

```text
FIRECRAWL_API_KEY
EXA_API_KEY
```

## Research Loop

Use this research loop for every serious research pass:

1. Define one question.
2. Discover sources with Brave Search, Tavily, or Exa.
3. Extract full content with Crawl4AI or Firecrawl when snippets are not enough.
4. Verify current technical docs with Context7 when APIs, SDKs, or cloud services are involved.
5. Compare findings against the UiPath AgentHack judging criteria.
6. Write a decision record in `docs/research_log.md`.
7. Convert the decision into one of:
   - README / Devpost copy update;
   - demo script update;
   - deck update;
   - new UiPath evidence target;
   - backlog item with a rejection reason.
8. Run local verification before claiming completion.

## Research Targets

Prioritize these questions:

- What does UiPath currently emphasize about AgentHack, Test Cloud, Maestro, API Workflows, Action Center, and coding agents?
- What proof would make UiPath feel indispensable rather than decorative?
- What agentic testing examples are already common, and how do we avoid looking like a generic AI test generator?
- What are the strongest real-world pain points in AI-infused workflow testing?
- What competitor or industry examples support the need for evidence-backed agent governance?
- Which claims should be removed because they sound like legal compliance, full runtime sandboxing, or unsupported production readiness?

## Decision Record Format

Append a decision record to `docs/research_log.md` using this structure:

```markdown
## YYYY-MM-DD - short title

Question:

Sources:

Findings:

Impact on Agentic Test Swarm:

Decision:

Action taken:

Open risk:
```

## Guardrails

- Action Center task `#3545796` remains pending until the final live demo approval moment.
- Preserve the fresh six-case Test Manager execution proof; do not overwrite it while recording.
- Do not reframe Python as the orchestration layer. UiPath remains the control plane.
- Do not claim legal compliance certification.
- Do not claim coding-agent repairs are trusted automatically.
- Prefer source-backed decisions over speculative feature additions.
