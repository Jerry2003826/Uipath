# Coding Agent Evidence

Agentic Test Swarm uses coding agents as assistants inside a broader UiPath-governed testing system. They support red-team scenario generation, repair drafting, documentation, and evidence summarization.

Coding agents are not approval authorities. Their outputs must be reviewed, tested, and connected to deterministic evidence in UiPath Test Cloud.

## Evidence principles

- Preserve the original prompt or task given to the coding agent.
- Preserve the generated output or a stable reference to it.
- Record whether the output affected tests, repair candidates, documentation, or demo materials.
- Record the human review decision.
- Link accepted output to deterministic oracle results and Test Cloud evidence.
- Never treat a coding-agent patch or generated scenario as approved until it passes the certification loop.

## Evidence log schema

Recommended fields:

- `entry_id`
- `timestamp`
- `agent_role`
- `task`
- `input_summary`
- `output_summary`
- `files_or_artifacts_touched`
- `human_review_status`
- `deterministic_oracle_status`
- `test_cloud_reference`
- `evidence_hash`
- `notes`

## Swarm roles that use coding-agent output

- `Red-Team Agent`: generates adversarial prompt-injection and agent-to-agent misuse scenarios.
- `Test Designer Agent`: converts accepted red-team scenarios into Test Cloud case drafts.
- `Failure Analyst Agent`: summarizes root cause and re-test scope from failed evidence.
- `Repair Agent`: proposes guardrail repairs after a failed certification test.

The deterministic oracle and Quality Governor remain non-LLM control points.

## Current evidence entries

### CAE-001 - Red-Team Scenario Generation

- `agent_role`: Red-Team Agent
- `task`: Generate adversarial policy-test scenarios for a Marketing Outreach Agent attempting to export VIP customer emails.
- `input_summary`: Hero scenario, raw PII policy, Customer Data Agent tool schema, captured trace.
- `output_summary`: Generated executive override, agent-to-agent misuse, high-volume PII, safe aggregate control, and regression replay scenarios.
- `files_or_artifacts_touched`: `evidence/case_001/red_team_scenarios.json`
- `human_review_status`: required before final submission
- `deterministic_oracle_status`: expected decisions supplied by deterministic oracle
- `test_cloud_reference`: `PermitOps V9.1 Agent Certification`
- `notes`: Coding-agent scenarios increase coverage but do not decide pass/fail.

### CAE-002 - Repair Candidate Drafting

- `agent_role`: Repair Agent
- `task`: Draft a raw PII export guardrail after TC-001 fails.
- `input_summary`: Failed trace replay, raw email export policy violation, allowed aggregate alternatives.
- `output_summary`: Proposed blocking raw email export unless the runtime permit contains explicit raw PII export scope.
- `files_or_artifacts_touched`: `evidence/case_001/repair_summary.md`
- `human_review_status`: required before final approval
- `deterministic_oracle_status`: verified by TC-001 and TC-005 after repair
- `test_cloud_reference`: `PermitOps Certification Evidence`
- `notes`: Repair candidates must be replayed through targeted tests.

### CAE-003 - Documentation Package

- `agent_role`: documentation coding agent
- `task`: Reframe the submission from PermitOps licensing-first to Agentic Test Swarm testing-first.
- `input_summary`: Official Track 3 prompt, user feedback, existing PermitOps platform evidence.
- `output_summary`: README, Devpost pitch, demo scripts, coding-agent evidence, and submission readiness updated around the testing swarm.
- `files_or_artifacts_touched`: `README.md`, `docs/devpost_pitch.md`, `docs/demo_script_5min.md`, `docs/demo_script_3min.md`, `docs/coding_agent_evidence.md`, `docs/submission_readiness.md`, `docs/agentic_test_swarm.md`
- `human_review_status`: pending reviewer acceptance
- `deterministic_oracle_status`: not applicable to documentation
- `test_cloud_reference`: not applicable to documentation
- `notes`: Documentation only; platform evidence remains in UiPath Test Manager, Action Center, Studio Web, and API Workflow.

## Review checklist

Before accepting coding-agent output into the evidence chain:

- Confirm generated scenarios map to explicit policy rules.
- Confirm expected results come from deterministic oracle logic.
- Confirm generated scenarios are represented in Test Cloud or Test Manager evidence.
- Confirm any repair candidate is re-tested.
- Confirm Action Center approval exists before permit activation.
- Confirm runtime enforcement references the approved permit.
- Confirm permit metadata includes `compiler_rules_hash`, `evidence_hash`, and `license_hash`.
