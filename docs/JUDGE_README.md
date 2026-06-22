# Judge README

Use this page when a reviewer has only a few minutes.

## Project

**Agentic Test Swarm** - UiPath Test Cloud agents that attack, repair, re-test, and certify enterprise AI workflows before they can touch production tools.

Primary track: **UiPath Test Cloud**

## Fastest Proof Path

1. Open the judge evidence matrix:
   `https://permitops-uipath.vercel.app/judge-evidence-matrix-view`
2. Open the live swarm view:
   `https://permitops-uipath.vercel.app/live-swarm-view`
3. Open the before/after execution evidence:
   `https://permitops-uipath.vercel.app/before-after-execution-evidence-view`
4. Open Test Cloud traceability:
   `https://permitops-uipath.vercel.app/test-cloud-traceability-view`
5. Review the UiPath proof screenshots listed in `docs/submission_readiness.md`.

## What Is Live In UiPath

- UiPath Test Manager project: `PermitOps V9.1 Agent Certification` (`PVACPOV91`)
- Test set: `PVACPOV91:6 - PermitOps Certification Evidence`
- TC-006 incident memory case: `PVACPOV91:76`
- Six-case execution: `59ea06c1-8074-0f00-8ea7-0b49ad83e475`
- Result: `6 passed / 0 failed / 0 not executed`
- Action Center task: `#3545796`, pending until final approval recording
- API Workflow proof: raw PII export returns `deny_and_suspend`
- UiPath-native Failure Analyst Agent debug proof exists in screenshots and evidence files

## What Is Deterministic Demo Evidence

- `/run-live-swarm`
- `/live-swarm-view`
- `/before-after-execution-evidence-view`
- `/test-manager-webhook-demo-view`
- `/evidence-graph-view`
- `/continuous-quality-memory-view`

These prove the worker behavior and narrative, but they do not replace the live UiPath tenant proof.

Run A / Run B split:

```text
Run A: Attack Detection - Before Repair -> 0 passed / 1 failed / 0 not executed
Run B: PermitOps Certification Evidence - 20260522.1544 -> 6 passed / 0 failed / 0 not executed
```

## Do Not Overclaim

- `REQ-PII-001` is currently a traceability target unless it is created in the tenant before submission.
- The Create Defect webhook endpoint is webhook-compatible demo evidence unless it is configured in Test Manager before submission.
- The six-case `6 passed` execution is the after-repair certification run, not the failure trigger.
- The public endpoints use synthetic data and carry no production credentials or real customer PII.

## Final Positioning

Agentic Test Swarm turns Test Cloud evidence into runtime permissions for AI workflows. AI agents propose attacks and repairs; deterministic oracles decide expected behavior; UiPath Test Cloud records evidence; Action Center gates approval; API Workflow enforces the final permit.
