# PermitOps Submission Readiness

Last updated: 2026-05-19

Current GitHub evidence commit: `6196be2`

## Platform Proof

Completed:

- UiPath Automation Cloud tenant: `scortlandyard / DefaultTenant`.
- Studio Web API Workflow proof returns `deny_and_suspend` for raw VIP email export.
- Maestro/Studio Web model exists for `PermitOps V9.1 Certification`.
- Test Manager project exists: `PermitOps V9.1 Agent Certification` (`PVACPOV91`).
- Test set exists: `PVACPOV91:6 - PermitOps Certification Evidence`.
- Test Manager execution exists: `PermitOps Certification Evidence - 20260519.0911`.
- Test Manager result evidence shows `5 passed / 0 failed / 0 not executed`.
- Action Center task `#3545796` is assigned to the current demo user and visible under `My Tasks > Pending`.

Known boundary:

- The Test Manager execution still shows status `Running` because the five results were recorded through `Override Result` from the execution grid. The official Manual Execution Assistant `Done` path was not used because UiPath warned that re-execution could overwrite existing results.

## Engineering Proof

Completed:

- FastAPI worker endpoints and deterministic engine are implemented.
- Captured trace replay artifacts exist in `evidence/case_001/`.
- Policy-to-test output exists for TC-001 through TC-005.
- Before/after deterministic test evidence exists.
- Active and pending licenses include `compiler_rules_hash`, `evidence_hash`, and `license_hash`.
- Runtime decision evidence exists for raw PII denial/suspension.
- Test suite passes locally.

Latest verification:

```text
.venv/bin/python -m pytest -q
19 passed
```

## Demo Assets

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

## Recording Plan

Recommended live path:

1. Start from the captured AI trace and local evidence.
2. Show Maestro/Studio Web BPMN as the certification lifecycle.
3. Show Test Manager project, test set, and execution result summary.
4. Show Action Center task `#3545796` in `Pending`.
5. Click approval live only during the final recording.
6. Show license hash metadata from `evidence/case_001/license.json`.
7. Show API Workflow debug result: `deny_and_suspend`.

Do not re-run the Test Manager execution during the recording unless you intentionally want a new run and accept the overwrite warning.

## Remaining Submission Work

Still needed before Devpost final submission:

- Record the 5-minute demo video.
- Export or upload the demo video.
- Make sure the GitHub repository is public.
- Complete the Devpost project page.
- Submit the UiPath Product Feedback form.

Not required for the current non-sandbox completion:

- Waiting for any extra sandbox entitlement.
- Building a full legal compliance product.
- Building a universal runtime sandbox.
