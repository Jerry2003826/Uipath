# Bonus Evidence Pack

This file is the quick reference for bonus and special-award material.

## 1. UiPath-native agent bonus

The project now includes a UiPath Studio Web Autonomous Agent proof, not only an external worker.

Artifact:

```text
Generate incident tickets from logs 1 2
```

Configured role:

```text
Agentic Test Swarm Failure Analyst Agent
```

Evidence:

```text
assets/uipath_failure_analyst_agent_no_issues.png
evidence/case_001/uipath_failure_analyst_agent_no_issues.txt
assets/uipath_failure_analyst_agent_debug_success.png
assets/uipath_failure_analyst_agent_output_detail.png
evidence/case_001/uipath_failure_analyst_agent_debug_success.txt
```

Judging claim:

```text
A UiPath-native Autonomous Agent ingests TC-001 Test Cloud evidence through log_chunk, calls gpt-5.4-2026-03-05-community-agents inside Studio Web, and returns a completed certification failure analysis.
```

What the trace proves:

```text
- Health Analyzer: No issues found
- Agent run executed
- LLM call executed
- Model run executed
- License usage: 1 Agents.LLMCalls
- Output: Completed certification failure analysis
- Status: Successful
```

Boundary:

```text
This agent is advisory. Deterministic oracle rules, Test Cloud evidence, Action Center approval, and API Workflow enforcement still decide what is trusted.
```

## 2. Coding Agents bonus

Evidence:

```text
docs/coding_agents_bonus_pack.md
docs/coding_agent_evidence.md
evidence/case_001/coding_agent_prompts.jsonl
evidence/case_001/coding_agent_outputs.jsonl
evidence/case_001/repair_summary.md
```

Judging claim:

```text
Codex-style coding agents generate adversarial scenarios, repair candidates, and API Workflow payload scaffolding, but their output is not trusted until validated by Test Cloud evidence and deterministic rules.
```

## 3. Most Creative Solution angle

Use this framing:

```text
Most projects test an app. Agentic Test Swarm tests whether AI workers are allowed to touch enterprise tools at all.
```

Creative mechanism:

```text
AI testing agents attack another AI workflow, repair the failure, re-test it, and convert evidence into a runtime permit that UiPath API Workflow can enforce.
```

## 4. Best Product Feedback angle

Evidence:

```text
docs/product_feedback_submission.md
docs/product_feedback_notes.md
```

Main feedback:

```text
UiPath should expose a first-class AI workflow certification evidence object that links Test Cloud evidence, Action Center approval, API Workflow runtime decisions, and Maestro / Studio Web case state.
```

## 5. Final video bonus shots

If time allows, insert a 5-8 second shot after the Failure Analyst section:

```text
Show assets/uipath_failure_analyst_agent_debug_success.png or the live Studio Web execution trace.
Narrate: This Failure Analyst role also runs as a UiPath-native Autonomous Agent; the trace shows an LLM call and successful certification failure analysis inside Studio Web.
```

Do not click Action Center approval except during the final recording.
