# Judge Scorecard

This document maps the official AgentHack judging criteria to concrete Agentic Test Swarm proof. Use it as the submission checklist and as the structure for the final demo narration.

## Judge taste update

Current visible judges:

```text
Taqi Jaffri - enterprise agentic automation, coded agents, interoperability, governance, observability.
Ingo Philipp - agentic testing, risk thinking, useful evidence, avoiding coverage theater.
```

Operational implication:

```text
The demo should not sell "more AI-generated tests."
It should sell a UiPath-governed quality system that uses AI agents to find risk, explain failure, propose repair, re-test, and enforce only evidence-backed runtime permissions.
```

Detailed research: `docs/judge_taste_research_2026-05-23.md`.

## Scorecard summary

| Criterion | What judges need to see | Agentic Test Swarm proof |
| --- | --- | --- |
| Business Impact & Adoption Potential | A real enterprise problem with adoption value. | AI agents need repeatable certification before touching customer-data tools; business impact metrics are in `README.md`. |
| Technical Execution, Feasibility & Versatility | Working software, edge cases, reliable execution, and reproducible setup. | Public worker, deterministic pytest suite, captured trace replay, permit hashes, live swarm endpoint, and `/license-decision`. |
| Platform Usage | UiPath used deeply as the orchestration/governance layer. | Studio Web / API Workflow, Test Manager / Test Cloud evidence, Action Center approval, Maestro/Studio Web lifecycle model. |
| Completeness of Delivery | Public repo, README, setup, video path, deck, screenshots, license. | MIT license, README, setup commands, `assets/agentic_test_swarm_deck.pptx`, Devpost pitch, screenshots, test evidence. |
| Creativity & Innovation | A novel agentic testing idea, not a generic approval workflow. | AI testing agents attack, repair, re-test, and certify an AI workflow; runtime permit is only the final artifact. |

## Business Impact & Adoption Potential

The business problem is not simply "AI safety." The concrete problem is that enterprise teams are being asked to let AI workers call tools, APIs, and other agents that expose sensitive customer data.

Agentic Test Swarm shows adoption potential because it fits the existing enterprise QA and automation operating model:

- QA owners review Test Cloud evidence instead of reading raw logs.
- Automation owners keep runtime enforcement inside API Workflow.
- Business approvers use Action Center for human accountability.
- Platform teams can reuse the certification loop for future AI workflows.

Target metrics are in `README.md`: manual AI workflow review time, new tool-surface coverage, repeatability, high-risk raw PII calls, and audit readiness.

## Technical Execution, Feasibility & Versatility

Proof:

- `pytest -q` validates deterministic behavior.
- `/health` proves the public worker is running.
- `/run-live-swarm` proves the vulnerable AI workflow, repair candidate, and targeted re-test loop.
- `/uipath-one-click-runbook` proves the intended UiPath control-plane sequence.
- `/license-decision` proves raw PII export enforcement with `deny_and_suspend`.
- `/continuous-quality-memory` proves runtime incidents become permanent UiPath Test Cloud regression evidence.
- `/evidence-graph` proves the chain from trace -> policy -> test -> repair -> approval -> runtime enforcement.
- Evidence hashes in `evidence/case_001/license.json` tie runtime decisions to the certified evidence chain.

Important design choice: AI proposes tests and repairs; deterministic rules decide expected behavior. That makes the system demo-friendly and enterprise-auditable.

## Platform Usage

UiPath first, Python worker second.

The final video should say this explicitly:

```text
UiPath owns the visible workflow state, test evidence, human approval, and runtime enforcement.
The Python worker only provides deterministic evidence and decisions when UiPath calls it.
```

Platform proof:

- Studio Web / API Workflow: `assets/uipath_api_workflow_success_deny_suspend.png`
- UiPath-native Agent Builder / Studio Web agent: `assets/uipath_failure_analyst_agent_no_issues.png`
- Test Cloud / Test Manager: `assets/test_manager_permitops_execution_5_passed_viewport.png`
- Action Center: `assets/action_center_permitops_pending_assigned_task_3545796.png`
- Maestro/Studio Web lifecycle: `assets/maestro_permitops_bpmn_autopilot.png`
- Services enabled: `assets/uipath_services_actions_test_manager_enabled.png`

## Completeness of Delivery

Required submission artifacts:

- Public GitHub repository: `Jerry2003826/Uipath`
- Open-source license: `LICENSE` uses MIT.
- README: project description, UiPath components, agent type, setup instructions, live endpoint, and evidence links.
- Demo video: record with `docs/final_video_shot_list.md`.
- Presentation deck: `assets/agentic_test_swarm_deck.pptx`.
- Product feedback: `docs/product_feedback_notes.md`.
- Devpost package: `docs/devpost_submission_package.md`.
- Product Feedback copy-paste form: `docs/product_feedback_submission.md`.

## Creativity & Innovation

The creative move is to make the testing agents the main character:

```text
Policy -> Red-Team Agent -> Test Designer -> Test Selector -> Test Cloud evidence
-> Failure Analyst -> Repair Agent -> Re-test -> Quality Governor -> runtime permit
```

Most projects will generate tests or approve agents. Agentic Test Swarm shows a continuous testing memory loop: when a new raw phone-number export surface appears, `TC-006` becomes incident-to-regression coverage.

The extra creative proof is the Evidence Graph:

```text
trace -> policy -> test -> repair -> approval -> runtime enforcement
```

That graph makes the system auditable instead of just plausible.

## Coding Agents Bonus

Coding agents contribute to adversarial scenario generation, repair candidate drafting, API Workflow payload scaffolding, and documentation packaging.

Evidence:

- `docs/coding_agent_evidence.md`
- `docs/coding_agents_bonus_pack.md`
- `evidence/case_001/coding_agent_prompts.jsonl`
- `evidence/case_001/coding_agent_outputs.jsonl`

Final video should include one visible mention of UiPath for Coding Agents / Codex-style repair generation if there is time. The narration should make clear that coding-agent output is not trusted until deterministic expected-oracle checks and Test Cloud evidence validate it.

## Evidence matrix

| Claim | Evidence |
| --- | --- |
| Runs publicly | `https://permitops-uipath.vercel.app/health` |
| Live AI workflow test | `https://permitops-uipath.vercel.app/live-swarm-view` |
| Continuous Quality Memory | `https://permitops-uipath.vercel.app/continuous-quality-memory`, `evidence/case_001/continuous_quality_memory.json` |
| Evidence Graph | `https://permitops-uipath.vercel.app/evidence-graph`, `evidence/case_001/evidence_graph.json` |
| UiPath runtime proxy works | `assets/uipath_api_workflow_success_deny_suspend.png` |
| UiPath-native Failure Analyst Agent runs in Studio Web | `assets/uipath_failure_analyst_agent_debug_success.png`, `assets/uipath_failure_analyst_agent_output_detail.png`, `evidence/case_001/uipath_failure_analyst_agent_debug_success.txt` |
| UiPath-native Failure Analyst Agent draft has no analyzer issues | `assets/uipath_failure_analyst_agent_no_issues.png`, `evidence/case_001/uipath_failure_analyst_agent_no_issues.txt` |
| Test Cloud evidence exists | `assets/test_manager_permitops_execution_5_passed_viewport.png` |
| Human approval gate exists | `assets/action_center_permitops_pending_assigned_task_3545796.png` |
| TC-006 incident memory exists | `PVACPOV91:76`, `assets/test_manager_tc006_case_created.png`, `assets/test_manager_tc006_added_to_test_set.png`, `evidence/case_001/incident_antibody_tests.json` |
| Deck exists | `assets/agentic_test_swarm_deck.pptx` |
| Setup is reproducible | `README.md` local setup commands |

## Judge-safe boundaries

Do not overclaim:

- TC-006 is now a live Test Manager case (`PVACPOV91:76`) assigned to `PVACPOV91:6` under `Static Assignment (6)`.
- The primary Test Manager execution is now the fresh six-case run `PermitOps Certification Evidence - 20260522.1544`, which shows `Finished` and `6 passed / 0 failed / 0 not executed`.
- The older `20260519.0911` execution can still show `Running`; keep it as historical evidence only.
- Do not click Action Center approval before the final recording.
- Do not claim the UiPath-native Failure Analyst Agent replaces Test Cloud or the deterministic oracle; it is advisory failure analysis inside UiPath, and Test Cloud evidence remains the source of certification truth.
- Do not claim legal compliance certification.
- Do not claim coding-agent repairs are automatically trusted.
