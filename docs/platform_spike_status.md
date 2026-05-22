# Agentic Test Swarm Platform Spike Status

Date: 2026-05-19 Australia/Melbourne

Note: the live UiPath artifacts below still use the original PermitOps names.
They now serve as platform proof for Agentic Test Swarm, with PermitOps scoped to
the final runtime permit module.

## Completed

- UiPath Automation Cloud login succeeded for the available account.
- Studio Web is accessible.
- A Studio Web API Workflow project/editor was opened and captured as evidence.
- Maestro is accessible in the `DefaultTenant` tenant.
- Local deterministic worker is implemented and tested.
- Local `full-demo-local` produces the PermitOps runtime-permit evidence chain.
- A real OpenAI Responses API call was captured and stored as `evidence/case_001/raw_llm_response.json`.
- A public FastAPI worker was deployed for UiPath API Workflow HTTP integration.
- Vercel alias: `https://permitops-uipath.vercel.app`
- A Studio Web API Workflow HTTP Request activity was configured through UiPath Autopilot.
- Studio Web Debug successfully called the public worker and returned `decision: deny_and_suspend`.
- A Maestro Agentic Process project was created as `PermitOps V9.1 Certification`.
- UiPath Autopilot generated the PermitOps V9.1 BPMN certification flow in `Process.bpmn`.
- The generated BPMN has 0 validation issues in Studio Web.
- Tenant services were updated to include Actions and Test Manager.
- Test Manager is accessible at project prefix `PVACPOV91`.
- Test Manager project `PermitOps V9.1 Agent Certification` was created.
- Five PermitOps certification test cases were created in Test Manager.
- Test set `PermitOps Certification Evidence` was created with the original five cases and later expanded to six with TC-006.
- Action Center is accessible and shows the pending-task inbox.

## 2026-05-20 follow-up

- Added the official Track 3 alignment document at `docs/official_track3_alignment.md`.
- Added the presentation deck draft at `assets/agentic_test_swarm_deck.pptx`.
- Re-checked the Studio Web designer URL from a fresh automated browser tab. The tab redirected to UiPath account login, so no new one-click control-plane screenshot was captured in that automation pass.
- Preserve the existing Studio Web API Workflow proof for `deny_and_suspend`; capture the one-click runbook trigger from the authenticated browser during the final recording.

## Evidence Files

- `assets/studio_api_workflow_created.png`
- `assets/uipath_api_workflow_debug_url_blocker.png`
- `assets/uipath_api_workflow_success_deny_suspend.png`
- `assets/maestro_home_accessible.png`
- `assets/maestro_permitops_agentic_process_created.png`
- `assets/maestro_permitops_bpmn_autopilot.png`
- `assets/test_manager_not_enabled_404.png`
- `assets/action_center_orchestrator_not_enabled.png`
- `assets/uipath_services_actions_test_manager_enabled.png`
- `assets/test_manager_permitops_5_test_cases.png`
- `assets/test_manager_permitops_test_set_assigned.png`
- `assets/action_center_enabled_empty_inbox.png`
- `evidence/case_001/raw_llm_response.json`
- `evidence/case_001/trace_metadata.json`
- `evidence/case_001/normalized_ai_trace.json`
- `evidence/case_001/test_cases.json`
- `evidence/case_001/test_results_before.json`
- `evidence/case_001/test_results_after.json`
- `evidence/case_001/license.json`
- `evidence/case_001/runtime_decision.json`
- `evidence/case_001/license_card.html`

## Public Worker Checks

Health endpoint:

```text
GET https://permitops-uipath.vercel.app/health
```

Runtime license decision endpoint:

```text
POST https://permitops-uipath.vercel.app/license-decision
```

Demo payload:

```json
{
  "case_id": "case_001",
  "source_agent": "marketing-outreach-agent",
  "target_agent": "customer-data-agent",
  "action": "export_raw_customer_emails",
  "payload": {
    "segment": "VIP",
    "count": 500,
    "data_type": "raw_email"
  }
}
```

Verified live through UiPath Studio Web Debug:

```json
{
  "content": {
    "decision": "deny_and_suspend",
    "evidence_ref": "runtime-event-001",
    "license_status": "suspended",
    "reason": "blocked_action_attempted"
  },
  "statusCode": 200
}
```

The successful run is captured in `assets/uipath_api_workflow_success_deny_suspend.png`.

## Maestro Agentic Process

Studio Web created a Maestro Agentic Process solution named:

```text
PermitOps V9.1 Certification
```

UiPath Autopilot was then asked to generate the PermitOps V9.1 certification model. It accepted the BPMN diff and reported:

```text
Autopilot updated the diagram: 27 added, 1 removed.
```

The generated flow includes:

- Start Certification
- Captured AI trace intake
- Risk scanning
- Generate policy tests
- Record Test Cloud evidence
- Pass/Fail? exclusive gateway
- Human approval in Action Center
- Propose coding-agent repair
- Re-test
- Compile restricted license
- Enforce license through API Workflow
- Suspend unauthorized raw PII export
- End Certification

Studio Web showed `Validation issues (0)`.

Evidence:

- `assets/maestro_permitops_agentic_process_created.png`
- `assets/maestro_permitops_bpmn_autopilot.png`

## Test Manager / Test Cloud

Initially, direct navigation to `https://cloud.uipath.com/scortlandyard/testmanager_/` returned:

```json
{ "statusCode": 404, "message": "Resource not found" }
```

This was resolved by opening the tenant Services page and adding `Test Manager` to `DefaultTenant`.

Live Test Manager artifacts now exist:

- Project: `PermitOps V9.1 Agent Certification`
- Prefix: `PVACPOV91`
- Test cases:
  - `PVACPOV91:1` - `TC001 PII export denied`
  - `PVACPOV91:2` - `TC002 aggregate access allowed`
  - `PVACPOV91:3` - `TC003 raw agent request suspended`
  - `PVACPOV91:4` - `TC004 high risk PII approval`
  - `PVACPOV91:5` - `TC005 regression keeps PII denied`
  - `PVACPOV91:76` - `TC006 incident memory blocks phone-number export`
- Test set: `PVACPOV91:6` - `PermitOps Certification Evidence`
- Static assignment count: `Static Assignment (6)`

Evidence:

- `assets/test_manager_permitops_5_test_cases.png`
- `assets/test_manager_permitops_test_set_assigned.png`
- `assets/test_manager_permitops_execution_5_passed_viewport.png`
- `assets/test_manager_permitops_execution_5_passed_fullpage.png`
- `assets/test_manager_tc006_case_created.png`
- `assets/test_manager_tc006_added_to_test_set.png`
- `assets/test_manager_6_passed_completed.png`
- `evidence/case_001/test_manager_manual_execution_result.json`
- `evidence/case_001/test_manager_tc006_case_created.txt`
- `evidence/case_001/test_manager_tc006_test_set_assignment.txt`
- `evidence/case_001/test_manager_6_passed_completed.txt`

Fresh six-case manual execution evidence now exists:

- Execution: `PermitOps Certification Evidence - 20260522.1544`
- Execution ID: `59ea06c1-8074-0f00-8ea7-0b49ad83e475`
- Result summary: `6 passed / 0 failed / 0 not executed`
- Current status label: `Finished`
- Test set: `PVACPOV91:6`
- Includes live TC-006: `PVACPOV91:76`

Historical five-case execution evidence is preserved:

- Execution: `PermitOps Certification Evidence - 20260519.0911`
- Execution ID: `c66f6554-4b30-0f00-4375-0b49aa4d0fd9`
- Result summary: `5 passed / 0 failed / 0 not executed`
- Result entry path: `More Options -> Override Result`
- Current status label: `Running`

Note: the historical result evidence is real and visible in Test Manager, but it is no
longer the primary judge-facing Test Cloud proof. Use the fresh six-case execution for
the final video.

## Action Center

Initially, Action Center was checked at the tenant URL:

```text
https://cloud.uipath.com/scortlandyard/DefaultTenant/actions_/tasks?status=Pending
```

The tenant returned:

```text
Actions is not enabled for this tenant.
Actions requires the UiPath Automation Cloud. Please contact your administrator to enable it.
```

This was resolved by opening the tenant Services page and adding `Actions` to `DefaultTenant`.

Action Center is now accessible at:

```text
https://cloud.uipath.com/scortlandyard/DefaultTenant/actions_/tasks?status=Pending
```

Current state:

```text
Inbox - Action Center
Pending: Approve PermitOps Restricted Agent License #3545796
Unassigned: no tasks after completion
Completed: Approve PermitOps Restricted Agent License #3545494
```

Evidence:

- `assets/action_center_enabled_empty_inbox.png`
- `assets/studio_web_create_external_task_success.png`
- `assets/action_center_permitops_unassigned_task_3545494_clean.png`
- `assets/action_center_permitops_completed_task_3545494.png`
- `assets/action_center_permitops_pending_assigned_task_3545796.png`

### Live task creation result

A Studio Web RPA Workflow was created with the Persistence activity `Create External Task`.
The workflow was configured with:

```text
Task Title: Approve PermitOps Restricted Agent License
Task Priority: High
Orchestrator folder path: Shared
Task Catalog: PermitOps Approvals
```

The cloud debug run succeeded and Studio Web logged:

```text
Task created with Id 3545494
```

The task is visible in Action Center under `Unassigned`:

```text
Approve PermitOps Restricted Agent License
#3545494 - PermitOps Approvals
Priority: High
```

The task was then completed from Action Center. The `Completed` tab now shows:

```text
Approve PermitOps Restricted Agent License
#3545494 - PermitOps Approvals
Priority: High
```

An assignment step was then added after `Create External Task` using the Persistence `Assign Tasks` activity.

Important Studio Web implementation notes:

```text
Assign Tasks -> Task Id: taskObjectOutput.Id.Value
Assign Tasks -> Assignment criteria: User
Assign Tasks -> User Name or Email: current UiPath demo user
Assign Tasks -> Task Assignment Type: Assign
```

The `Task Id` expression must be created through the VB Expression editor. The `Create External Task` output property is nullable (`Long?`), while `Assign Tasks` requires `Int64`, so the expression must use `.Value`. The raw `taskObjectOutput.Id` expression fails validation with an Option Strict nullable-to-non-nullable conversion error.

After the assignment step was added, Studio Web reported `No issues found`. The cloud debug run succeeded and logged:

```text
Task created with Id 3545796
Create External Task: Successful
Assign Tasks: Successful
RPA Workflow execution ended
```

The new task is visible in Action Center under the current user's `Pending` inbox:

```text
Approve PermitOps Restricted Agent License
#3545796 - PermitOps Approvals
Priority: High
Status bucket: Pending
```

Important Studio Web implementation note:

```text
The Task Title field must be saved through the field menu -> Text builder -> Save.
Typing directly into the inline field can display text without satisfying Studio Web validation.
```

## UiPath-native Failure Analyst Agent draft

Sandbox access now exposes UiPath Agents / Studio Web agent templates.

Created and configured:

```text
Project: Generate incident tickets from logs 1 2
Surface: UiPath Studio Web Autonomous Agent
Role: Agentic Test Swarm Failure Analyst Agent
Model: gpt-5.4-2026-03-05
Input: {{log_chunk}} evidence package
```

The system prompt asks the agent to analyze failed UiPath Test Cloud certification evidence, identify root cause and risk impact, recommend a repair, and choose a targeted re-test strategy.

Evidence:

```text
assets/uipath_failure_analyst_agent_draft.png
assets/uipath_failure_analyst_agent_model_selected.png
assets/uipath_failure_analyst_agent_no_issues.png
evidence/case_001/uipath_failure_analyst_agent_model_selected.txt
evidence/case_001/uipath_failure_analyst_agent_no_issues.txt
```

Resolved issue: the template `Create Issue` integration tool was removed because this Failure Analyst Agent only needs to return structured analysis. Health Analyzer now reports `No issues found`, the draft is saved, and the `Debug` action is available. Action Center task `#3545796` was not approved during this work.

## Current Blockers

### Action Center assigned pending task

Resolved. The assigned pending task evidence is captured at:

```text
assets/action_center_permitops_pending_assigned_task_3545796.png
```

## Next Platform Steps

1. Optional: complete task `#3545796` during the final demo recording so the video shows Pending -> Completed.
2. Preserve the fresh six-case Test Manager execution during recording; do not overwrite it unless a new final take is intentionally created.
3. Publish or package the Studio Web API Workflow after the sandbox/service entitlement is stable.
