# UiPath-Native Agent Depth Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Agentic Test Swarm visibly deeper on UiPath-native agents by adding Policy Miner and Red-Team Agent specs, evidence artifacts, a worker endpoint for Studio Web, and judge-facing documentation.

**Architecture:** Keep Python as the deterministic worker. Add UiPath-native agent evidence as platform-facing specs and reusable payload packs that Studio Web / Agent Builder can consume. The final story becomes: UiPath-native agents mine policy and generate attacks, Test Cloud stores evidence, Action Center gates approval, and API Workflow enforces runtime decisions.

**Tech Stack:** FastAPI, pytest, static JSON evidence, UiPath Studio Web / Agent Builder specs, Test Manager evidence docs.

---

### Task 1: Add UiPath-Native Agent Evidence Pack

**Files:**
- Create: `uipath/agents/policy_miner_agent.md`
- Create: `uipath/agents/red_team_agent.md`
- Create: `uipath/agents/test_designer_agent.md`
- Create: `evidence/case_001/uipath_native_agent_pack.json`
- Modify: `evidence/case_001/agentic_test_agents.json`
- Test: `tests/test_uipath_native_agent_depth.py`

- [ ] **Step 1: Write tests for required UiPath-native agent artifacts**

Run: `pytest tests/test_uipath_native_agent_depth.py -q`

Expected before implementation: fail because the new files do not exist.

- [ ] **Step 2: Add agent specs**

Each spec must include:
- UiPath surface;
- Agent Builder purpose;
- input variable schema;
- system prompt;
- expected output JSON;
- Test Cloud evidence link;
- demo line for judges.

- [ ] **Step 3: Add evidence pack JSON**

The JSON must name `Policy Miner Agent`, `Red-Team Agent`, `Test Designer Agent`, and existing `Failure Analyst Agent`, mark their runtime as `uipath_native_orchestrated`, and include exact Studio Web setup notes.

- [ ] **Step 4: Run tests**

Run: `pytest tests/test_uipath_native_agent_depth.py -q`

Expected: pass.

### Task 2: Add Worker Endpoint for UiPath Native Agent Pack

**Files:**
- Modify: `permitops_worker/app.py`
- Test: `tests/test_api_routes.py`

- [ ] **Step 1: Add failing API test**

Add a test that calls `GET /uipath-native-agent-pack` and asserts it returns UiPath-native agent specs for Policy Miner, Red-Team, Test Designer, and Failure Analyst roles.

- [ ] **Step 2: Implement endpoint**

Endpoint returns static pack JSON from `evidence/case_001/uipath_native_agent_pack.json`; if missing, raise HTTP 404 with a clear message.

- [ ] **Step 3: Run test**

Run: `pytest tests/test_api_routes.py -q`

Expected: pass.

### Task 3: Update Judge-Facing Documentation

**Files:**
- Modify: `README.md`
- Modify: `docs/devpost_submission_package.md`
- Modify: `docs/final_video_shot_list.md`
- Modify: `docs/submission_readiness.md`
- Modify: `docs/platform_spike_status.md`
- Modify: `docs/bonus_evidence_pack.md`
- Test: `tests/test_submission_artifacts.py`

- [ ] **Step 1: Add assertions for UiPath-native agent depth**

Tests should require:
- `UiPath-native agent depth`;
- `Policy Miner Agent`;
- `Red-Team Agent`;
- `/uipath-native-agent-pack`;
- `Failure Analyst Agent`.

- [ ] **Step 2: Update docs**

Docs must explain that PermitOps now has more than one UiPath-native AI role: Policy Miner, Red-Team, Test Designer, and Failure Analyst.

- [ ] **Step 3: Run docs tests**

Run: `pytest tests/test_submission_artifacts.py -q`

Expected: pass.

### Task 4: Verify Whole Project

**Files:**
- No new files.

- [ ] **Step 1: Run full test suite**

Run: `pytest -q`

Expected: all tests pass.

- [ ] **Step 2: Verify public endpoint shape locally**

Run: `python -m permitops_worker.cli v11-live-swarm-local`

Expected: command completes and writes evidence files without UiPath credentials.

- [ ] **Step 3: Browser check**

Use in-app browser to inspect the deployed or local endpoint if a server is available. Do not approve Action Center task `#3545796`.
