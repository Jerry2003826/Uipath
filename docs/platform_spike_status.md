# PermitOps Platform Spike Status

Date: 2026-05-19 Australia/Melbourne

## Completed

- UiPath Automation Cloud login succeeded for the available account.
- Studio Web is accessible.
- A Studio Web API Workflow project/editor was opened and captured as evidence.
- Maestro is accessible in the `DefaultTenant` tenant.
- Local deterministic worker is implemented and tested.
- Local `full-demo-local` produces the PermitOps evidence chain.
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
- Test set `PermitOps Certification Evidence` was created and assigned all five test cases.
- Action Center is accessible and shows the pending-task inbox.

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
- Test set: `PVACPOV91:6` - `PermitOps Certification Evidence`
- Static assignment count: `5`

Evidence:

- `assets/test_manager_permitops_5_test_cases.png`
- `assets/test_manager_permitops_test_set_assigned.png`

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

## Current Blockers

### Action Center assigned pending task

Resolved. The assigned pending task evidence is captured at:

```text
assets/action_center_permitops_pending_assigned_task_3545796.png
```

## Next Platform Steps

1. Optional: complete task `#3545796` during the final demo recording so the video shows Pending -> Completed.
2. Optionally execute the Test Manager test set manually or through automation to create live run results.
3. Publish or package the Studio Web API Workflow after the sandbox/service entitlement is stable.
