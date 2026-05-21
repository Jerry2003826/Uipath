# Coding Agents Bonus Pack

This document is for the AgentHack coding agents bonus. It explains which coding agents were used, what they contributed, and how their output is governed by UiPath and deterministic tests.

## Coding Agents Bonus

Agentic Test Swarm uses Codex-style coding agents as supporting workers inside a UiPath-governed testing lifecycle.

The important claim is not "a coding agent wrote code." The important claim is:

```text
Coding agents generate adversarial tests and repair candidates, but UiPath Test Cloud evidence, deterministic oracles, and Action Center approval decide what is trusted.
```

## Tool used

- Codex
- Codex subagents for repository inspection and official requirement gap checks
- UiPath for Coding Agents is referenced in the architecture as the intended enterprise bridge for coding-agent work against UiPath skills and workflows

## Where coding agents contributed

### 1. adversarial scenario generation

Coding-agent role:

```text
Red-Team Agent
```

Contribution:

- generated executive override attacks;
- generated agent-to-agent misuse cases;
- generated raw PII exfiltration scenarios;
- generated regression replay scenarios.

Evidence:

- `evidence/case_001/red_team_scenarios.json`
- `evidence/case_001/coding_agent_prompts.jsonl`
- `evidence/case_001/coding_agent_outputs.jsonl`

### 2. repair candidate

Coding-agent role:

```text
Repair Agent
```

Contribution:

- proposed raw PII export guardrail;
- mapped the guardrail to Customer Data Agent behavior;
- connected the repair to targeted re-tests TC-001 and TC-005;
- recommended API Workflow proxy enforcement.

Evidence:

- `evidence/case_001/repair_summary.md`
- `evidence/case_001/failure_analysis.json`
- `evidence/case_001/test_results_after.json`

### 3. API Workflow payload scaffolding

Coding-agent role:

```text
API Workflow scaffolding assistant
```

Contribution:

- wrote request/response payloads for `/license-decision`;
- wrote one-click runbook payloads for `/uipath-one-click-runbook`;
- documented Control Plane Run Trigger and Licensed Tool Proxy specs.

Evidence:

- `uipath/api_workflows/control_plane_run_trigger.yaml`
- `uipath/api_workflows/licensed_tool_proxy.yaml`
- `uipath/api_workflows/evidence_placeholders/api_demo_transcripts.md`

### 4. submission and review agents

Coding-agent role:

```text
submission packaging assistant
```

Contribution:

- built judge scorecard;
- built final video shot list;
- built Product Feedback copy;
- ran tests that enforce submission completeness.

Evidence:

- `docs/judge_scorecard.md`
- `docs/final_video_shot_list.md`
- `docs/product_feedback_submission.md`
- `tests/test_submission_artifacts.py`

## Trust boundary

Coding-agent output is not trusted automatically.

It must pass this chain:

```text
coding-agent suggestion
-> deterministic expected oracle
-> Test Cloud evidence
-> Action Center approval for high-impact access
-> Quality Governor permit decision
-> API Workflow runtime enforcement
```

That trust boundary is the core enterprise pattern.

## Demo narration

Use this short line in the final video:

```text
Codex-style coding agents generate attacks and repair candidates, but the system does not trust them automatically. UiPath Test Cloud records the evidence, Action Center keeps humans accountable, and API Workflow enforces only the tested permit.
```

## Evidence checklist

- Show `docs/coding_agent_evidence.md`.
- Show `evidence/case_001/coding_agent_prompts.jsonl`.
- Show `evidence/case_001/coding_agent_outputs.jsonl`.
- Show `evidence/case_001/repair_summary.md`.
- Show `assets/uipath_failure_analyst_agent_debug_success.png` to prove a UiPath-native testing agent ran inside Studio Web.
- Show Test Manager / Test Cloud evidence after the repair.
- Show runtime `deny_and_suspend` through API Workflow.

## UiPath-native agent bonus proof

The strongest new bonus proof is not just a screenshot of an agent definition. The `Agentic Test Swarm Failure Analyst Agent` now has a successful Studio Web debug trace.

Evidence:

```text
assets/uipath_failure_analyst_agent_debug_success.png
evidence/case_001/uipath_failure_analyst_agent_debug_success.txt
```

The trace shows:

```text
Agent run
LLM call
Model run: gpt-5.4-2026-03-05-community-agents
License usage: 1 Agents.LLMCalls
Input: TC-001 failure evidence through log_chunk
Output: Completed certification failure analysis
Status: Successful
```

Use this line in judging:

```text
The Failure Analyst is not only represented as Python logic; it also exists as a UiPath Studio Web Autonomous Agent and successfully analyzed TC-001 evidence inside the UiPath platform.
```
