# Continuous Quality Evidence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Continuous Quality Memory and Evidence Graph proof layers so Agentic Test Swarm reads as a UiPath-governed continuous quality system, not a one-time testing demo.

**Architecture:** Add deterministic engine functions that build JSON artifacts for the quality-memory loop and cross-product evidence graph. Expose both through FastAPI JSON and HTML endpoints, generate repo evidence through CLI commands, and update judge-facing docs. Keep UiPath Action Center task `#3545796` pending.

**Tech Stack:** FastAPI, pytest, static JSON evidence, existing Vercel deployment, UiPath Test Manager evidence references.

---

### Task 1: Continuous Quality Memory

**Files:**
- Create: `permitops_worker/engine/continuous_quality.py`
- Create: `tests/test_continuous_quality_evidence.py`
- Modify: `permitops_worker/app.py`
- Modify: `permitops_worker/cli.py`
- Create: `evidence/case_001/continuous_quality_memory.json`

- [ ] Write failing tests for the memory lifecycle.
- [ ] Implement `build_continuous_quality_memory(case_id)`.
- [ ] Add `GET /continuous-quality-memory`.
- [ ] Add `GET /continuous-quality-memory-view`.
- [ ] Add CLI command `continuous-quality-memory-local`.
- [ ] Generate evidence JSON.

### Task 2: Evidence Graph

**Files:**
- Modify: `permitops_worker/engine/continuous_quality.py`
- Modify: `permitops_worker/app.py`
- Modify: `permitops_worker/cli.py`
- Create: `evidence/case_001/evidence_graph.json`

- [ ] Write failing tests for trace -> policy -> test -> repair -> approval -> enforcement graph.
- [ ] Implement `build_evidence_graph(case_id)`.
- [ ] Add `GET /evidence-graph`.
- [ ] Add `GET /evidence-graph-view`.
- [ ] Add CLI command `evidence-graph-local`.
- [ ] Generate evidence JSON.

### Task 3: Judge-Facing Docs

**Files:**
- Modify: `README.md`
- Modify: `docs/devpost_submission_package.md`
- Modify: `docs/final_video_shot_list.md`
- Modify: `docs/submission_readiness.md`
- Modify: `docs/judge_scorecard.md`
- Modify: `docs/official_track3_alignment.md`
- Modify: `docs/product_feedback_submission.md`
- Modify: `tests/test_submission_artifacts.py`

- [ ] Add assertions for `Continuous Quality Memory`, `Evidence Graph`, `/continuous-quality-memory`, and `/evidence-graph`.
- [ ] Update docs to say continuous quality memory is the strongest Track 3 story after Test Manager evidence.
- [ ] Keep the permit as output, not the product.

### Task 4: Verification and Deployment

- [ ] Run `pytest -q`.
- [ ] Run `python -m permitops_worker.cli continuous-quality-memory-local`.
- [ ] Run `python -m permitops_worker.cli evidence-graph-local`.
- [ ] Verify local endpoints in in-app browser.
- [ ] Commit, push, deploy to Vercel, and verify public endpoints.
