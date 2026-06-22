# Agentic Test Swarm Submission Readiness

Last updated: 2026-06-22

Current public positioning:

```text
Agentic Test Swarm - UiPath Test Cloud agents that attack, repair, and certify AI workflows
```

Internal governance artifact:

```text
PermitOps Runtime Permit
```

## Platform proof

Completed:

- UiPath Automation Cloud tenant: `scortlandyard / DefaultTenant`.
- Studio Web API Workflow proof returns `deny_and_suspend` for raw VIP email export.
- Public one-click runbook endpoint exists at `https://permitops-uipath.vercel.app/uipath-one-click-runbook`.
- Maestro / Studio Web model exists for `PermitOps V9.1 Certification`.
- Test Manager project exists: `PermitOps V9.1 Agent Certification` (`PVACPOV91`).
- Test set exists: `PVACPOV91:6 - PermitOps Certification Evidence`.
- Live TC-006 case exists: `PVACPOV91:76 - TC006 incident memory blocks phone-number export`.
- Test set `PVACPOV91:6` now shows `Static Assignment (6)` and includes `PVACPOV91:76`.
- Fresh Test Manager execution exists: `PermitOps Certification Evidence - 20260522.1544`.
- Fresh execution ID: `59ea06c1-8074-0f00-8ea7-0b49ad83e475`.
- Test Manager result evidence shows `Finished`, `6 passed / 0 failed / 0 not executed`.
- Action Center task `#3545796` is assigned to the current demo user and visible under `My Tasks > Pending`.
- Agentic Test Swarm design exists at `docs/agentic_test_swarm.md`.
- Structured swarm evidence exists at `evidence/case_001/agentic_test_agents.json`.
- UiPath-native Agent Builder / Studio Web draft exists: `Generate incident tickets from logs 1 2` is configured as the `Agentic Test Swarm Failure Analyst Agent`.
- The draft uses UiPath model `gpt-5.4-2026-03-05` and accepts the existing low-code `{{log_chunk}}` evidence-package input.
- The UiPath-native Failure Analyst Agent was debugged successfully inside Studio Web with TC-001 evidence. The trace shows an Agent run, LLM call, model run, `1 Agents.LLMCalls` usage, and output `Completed certification failure analysis`.
- UiPath-native agent depth pack exists at `evidence/case_001/uipath_native_agent_pack.json`.
- Policy Miner Agent setup spec exists at `uipath/agents/policy_miner_agent.md`.
- Red-Team Agent setup spec exists at `uipath/agents/red_team_agent.md`.
- Test Designer Agent setup spec exists at `uipath/agents/test_designer_agent.md`.
- Worker endpoint for the native pack exists at `/uipath-native-agent-pack`.
- Continuous Quality Memory exists at `/continuous-quality-memory` and `/continuous-quality-memory-view`.
- Evidence Graph exists at `/evidence-graph` and `/evidence-graph-view`.
- Test Cloud Native Traceability Pack exists at `/test-cloud-traceability` and `/test-cloud-traceability-view`.
- Test Manager Create Defect webhook demo exists at `/test-manager-webhook-demo` and `/test-manager-webhook-demo-view`.
- Judge evidence matrix exists at `/judge-evidence-matrix` and `/judge-evidence-matrix-view`.
- Before/after execution evidence exists at `/before-after-execution-evidence` and `/before-after-execution-evidence-view`.

Known boundary:

- The live UiPath artifacts still use PermitOps names because they were created before the public narrative pivot. In the demo, explain that PermitOps is now the final runtime permit module.
- Historical five-case execution `PermitOps Certification Evidence - 20260519.0911` can still show `Running` because it used result overrides. Use the fresh six-case execution `PermitOps Certification Evidence - 20260522.1544` for final video and judge-facing proof.
- A fresh automated browser tab redirected to UiPath login on 2026-05-20, so the new one-click Studio Web trigger screenshot remains a final-recording task. The existing API Workflow debug screenshot still proves UiPath can call the public worker and receive `deny_and_suspend`.
- The UiPath-native Failure Analyst Agent draft no longer has the template tool connection issue. The `Create Issue` integration tool was removed, and Health Analyzer reports `No issues found`.
- Policy Miner Agent, Red-Team Agent, and Test Designer Agent are currently specs plus endpoint-ready payloads, not yet separate live Studio Web debug traces. This is still useful for final judging because it shows the planned UiPath-native extension path without risking the existing Action Center gate.
- Native-depth deep dive: the project maps cleanly to UiPath's native agent
  shape, `Prompt / Context / Tools / Escalations`. Current proof is strongest
  for prompt, tools, and escalations; Context Grounding, Agent Memory, tool guardrails, and tool simulations should be framed as product-fit extensions rather than rushed into the final demo.
- Test Cloud native traceability deep dive: the strongest remaining platform
  upgrade is making `Requirement -> Test Case -> Execution -> Defect -> Runtime
  Permit` visible inside Test Manager/Test Cloud. Current live proof covers Test
  Case -> Execution -> Runtime Permit. The next safe UiPath additions are
  `REQ-PII-001`, an `Obsolete Test Scout`, and a Create Defect webhook plan.
  A deterministic evidence pack now exists at
  `evidence/case_001/test_cloud_traceability_pack.json`.
  A deterministic Create Defect webhook demo now exists at
  `evidence/case_001/test_manager_create_defect_webhook_demo.json` and returns
  defect payload `ATS-DEFECT-TC-001`.

## Engineering proof

Completed:

- FastAPI worker endpoints and deterministic engine are implemented.
- Captured trace replay artifacts exist in `evidence/case_001/`.
- Red-team scenarios exist at `evidence/case_001/red_team_scenarios.json`.
- Test Designer mapping exists at `evidence/case_001/test_designer_cases.json`.
- Test Selector decision exists at `evidence/case_001/test_selector_decision.json`.
- Failure analysis exists at `evidence/case_001/failure_analysis.json`.
- Repair summary exists at `evidence/case_001/repair_summary.md`.
- Swarm run summary exists at `evidence/case_001/agentic_test_swarm_run.json`.
- V11 live swarm evidence exists at `evidence/case_001/v11_live_swarm_run.json`.
- Incident antibody test evidence exists at `evidence/case_001/incident_antibody_tests.json`.
- UiPath one-click runbook evidence exists at `evidence/case_001/uipath_one_click_runbook.json`.
- UiPath-native agent depth evidence exists at `evidence/case_001/uipath_native_agent_pack.json`.
- Continuous Quality Memory evidence exists at `evidence/case_001/continuous_quality_memory.json`.
- Evidence Graph evidence exists at `evidence/case_001/evidence_graph.json`.
- Test Cloud Native Traceability Pack evidence exists at `evidence/case_001/test_cloud_traceability_pack.json`.
- Test Manager Create Defect webhook evidence exists at `evidence/case_001/test_manager_create_defect_webhook_demo.json`.
- Before/after execution evidence exists at `evidence/case_001/before_after_execution_evidence.json`.
- Before/after deterministic test evidence exists.
- Active and pending permits include `compiler_rules_hash`, `evidence_hash`, and `license_hash`.
- Runtime decision evidence exists for raw PII denial/suspension.
- Test suite passes locally.

Latest verification target:

```text
.venv/bin/python -m pytest -q
```

## Demo assets

Use these screenshots in the final video or Devpost gallery:

- `assets/maestro_permitops_bpmn_autopilot.png`
- `assets/studio_api_workflow_created.png`
- `assets/uipath_api_workflow_success_deny_suspend.png`
- `assets/test_manager_permitops_5_test_cases.png`
- `assets/test_manager_permitops_test_set_assigned.png`
- `assets/test_manager_permitops_execution_5_passed_viewport.png`
- `assets/test_manager_tc006_case_created.png`
- `assets/test_manager_tc006_added_to_test_set.png`
- `assets/test_manager_6_passed_completed.png`
- `assets/uipath_failure_analyst_agent_draft.png`
- `assets/uipath_failure_analyst_agent_model_selected.png`
- `assets/uipath_failure_analyst_agent_no_issues.png`
- `assets/uipath_failure_analyst_agent_debug_success.png`
- `assets/uipath_failure_analyst_agent_output_detail.png`
- `assets/action_center_permitops_pending_assigned_task_3545796.png`
- `assets/action_center_permitops_completed_task_3545494.png`
- `assets/maestro_debug_human_approval_completed.png`

## Recording plan

Recommended live path:

1. Start from the UiPath control-plane run: Studio Web / API Workflow trigger calls `/uipath-one-click-runbook`.
2. Show the runbook chain: `/run-live-swarm`, Test Cloud evidence, Action Center task `#3545796`, API Workflow runtime proxy.
3. Show the captured Marketing Outreach Agent trace.
4. Show Policy Miner, Red-Team, Test Designer, Test Selector, Failure Analyst, Repair Agent, Re-test Orchestrator, and Quality Governor.
5. Show UiPath-native agent depth: Failure Analyst Agent debug trace, then the Policy Miner Agent / Red-Team Agent / Test Designer Agent specs or `/uipath-native-agent-pack`.
6. Show V11 live loop: before repair `allow`, after repair `deny_and_suspend`.
7. Show Continuous Quality Memory: runtime incidents become permanent UiPath Test Cloud regression evidence.
8. Show Evidence Graph: trace -> policy -> test -> repair -> approval -> runtime enforcement.
9. Show Test Cloud Native Traceability Pack: Requirement -> Test Case -> Execution -> Defect -> Runtime Permit.
10. Show Before/After Execution Evidence: Run A failed TC-001 before repair, Run B is the after-repair six-case Test Manager execution.
11. Show Test Manager Create Defect webhook demo: failed TC-001 -> `ATS-DEFECT-TC-001` -> Failure Analyst -> Repair Agent -> targeted re-test.
12. Show TC-006 incident-memory antibody test for phone-number export.
13. Show Maestro/Studio Web BPMN as the certification lifecycle.
14. Show Test Manager project, test set, and execution result summary.
15. Show Action Center task `#3545796` in `Pending`.
16. Click approval live only during the final recording.
17. Show PermitOps Runtime Permit hash metadata from `evidence/case_001/license.json`.
18. Show API Workflow debug result: `deny_and_suspend`.

Key narration:

```text
The permit is not the product. The product is a UiPath-orchestrated testing
swarm that attacks, repairs, re-tests, and certifies an AI workflow.
```

Do not re-run the Test Manager execution during the recording unless you intentionally want a new run and accept the overwrite warning.

## Remaining submission work

Still needed before Devpost final submission:

- Record the 5-minute demo video.
- Export or upload the demo video.
- Make sure the GitHub repository is public.
- Complete the Devpost project page.
- Submit the UiPath Product Feedback form.
- Capture the Studio Web one-click runbook trigger if the authenticated UiPath session is available.
- If authenticated Test Manager is available, create `REQ-PII-001` and link TC-001 through TC-006.
- If authenticated Test Manager is available, create a before-repair failed execution for TC-001.
- If authenticated Test Manager settings are available, configure or screenshot the Create Defect webhook integration path.
- Use the fresh six-case Test Manager execution screenshot in the final video and Devpost gallery.

Ready-to-paste submission helpers now exist:

- `docs/devpost_submission_package.md`
- `docs/product_feedback_submission.md`
- `docs/coding_agents_bonus_pack.md`
- `docs/uipath_platform_finish_runbook.md`
- `docs/uipath_native_depth_gap_research_2026-05-23.md`
- `docs/test_cloud_native_gap_research_2026-05-23.md`

## 2026-05-21 platform attempt

Attempted to open the Test Manager project directly at:

```text
https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/testcases
```

The automated browser reached UiPath login, accepted the Google account and
password, then stopped at Google two-step verification. No Test Manager data was
changed, and Action Center task `#3545796` was not approved.

Not required for the current non-sandbox completion:

- Waiting for any extra sandbox entitlement.
- Building a full legal compliance product.
- Building a universal runtime sandbox.
- Wiring `astrbot_orchestrator` or `superrag` into the main demo path.
