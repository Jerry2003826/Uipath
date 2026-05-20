# Agentic Test Swarm Submission Readiness

Last updated: 2026-05-19

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
- Test Manager execution exists: `PermitOps Certification Evidence - 20260519.0911`.
- Test Manager result evidence shows `5 passed / 0 failed / 0 not executed`.
- Action Center task `#3545796` is assigned to the current demo user and visible under `My Tasks > Pending`.
- Agentic Test Swarm design exists at `docs/agentic_test_swarm.md`.
- Structured swarm evidence exists at `evidence/case_001/agentic_test_agents.json`.

Known boundary:

- The live UiPath artifacts still use PermitOps names because they were created before the public narrative pivot. In the demo, explain that PermitOps is now the final runtime permit module.
- The Test Manager execution still shows status `Running` because the five results were recorded through `Override Result` from the execution grid. The official Manual Execution Assistant `Done` path was not used because UiPath warned that re-execution could overwrite existing results.
- A fresh automated browser tab redirected to UiPath login on 2026-05-20, so the new one-click Studio Web trigger screenshot remains a final-recording task. The existing API Workflow debug screenshot still proves UiPath can call the public worker and receive `deny_and_suspend`.

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
- `assets/action_center_permitops_pending_assigned_task_3545796.png`
- `assets/action_center_permitops_completed_task_3545494.png`
- `assets/maestro_debug_human_approval_completed.png`

## Recording plan

Recommended live path:

1. Start from the UiPath control-plane run: Studio Web / API Workflow trigger calls `/uipath-one-click-runbook`.
2. Show the runbook chain: `/run-live-swarm`, Test Cloud evidence, Action Center task `#3545796`, API Workflow runtime proxy.
3. Show the captured Marketing Outreach Agent trace.
4. Show Policy Miner, Red-Team, Test Designer, Test Selector, Failure Analyst, Repair Agent, Re-test Orchestrator, and Quality Governor.
5. Show V11 live loop: before repair `allow`, after repair `deny_and_suspend`.
6. Show TC-006 incident-memory antibody test for phone-number export.
7. Show Maestro/Studio Web BPMN as the certification lifecycle.
8. Show Test Manager project, test set, and execution result summary.
9. Show Action Center task `#3545796` in `Pending`.
10. Click approval live only during the final recording.
11. Show PermitOps Runtime Permit hash metadata from `evidence/case_001/license.json`.
12. Show API Workflow debug result: `deny_and_suspend`.

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
- Optionally add `TC-006` as a sixth live Test Manager case; otherwise present it honestly as structured incident-memory evidence ready to map.

Not required for the current non-sandbox completion:

- Waiting for any extra sandbox entitlement.
- Building a full legal compliance product.
- Building a universal runtime sandbox.
- Wiring `astrbot_orchestrator` or `superrag` into the main demo path.
