from __future__ import annotations

from typing import Any


def _row(claim: str, surface: str, evidence: str, status: str, boundary: str) -> dict[str, str]:
    return {
        "claim": claim,
        "uipath_surface": surface,
        "evidence": evidence,
        "status": status,
        "boundary": boundary,
    }


def build_judge_evidence_matrix(case_id: str = "case_001") -> dict[str, Any]:
    return {
        "case_id": case_id,
        "system_name": "Judge Evidence Matrix",
        "claim": (
            "One page that separates live UiPath tenant proof from deterministic demo "
            "evidence and blueprint items."
        ),
        "positioning": (
            "Agentic Test Swarm is a Test Cloud-centered certification loop. Python computes "
            "deterministic evidence; UiPath owns the visible test management, approval, and "
            "runtime governance surfaces."
        ),
        "rows": [
            _row(
                "Six-case certification result",
                "UiPath Test Manager / Test Cloud",
                "Execution 59ea06c1-8074-0f00-8ea7-0b49ad83e475 shows 6 passed / 0 failed / 0 not executed.",
                "LIVE TENANT PROOF",
                "This is the final after-repair certification evidence, not the before-repair failure.",
            ),
            _row(
                "Incident memory regression",
                "UiPath Test Manager",
                "TC-006 is mapped as PVACPOV91:76 and represents phone-number export incident memory.",
                "LIVE TENANT PROOF",
                "The incident-to-regression loop is demonstrated with deterministic worker evidence plus live mapped test case.",
            ),
            _row(
                "Human accountability gate",
                "UiPath Action Center",
                "Task #3545796 remains pending for the final live approve moment.",
                "LIVE TENANT PROOF",
                "The task must be approved during final recording before claiming an active permit.",
            ),
            _row(
                "Runtime blocked action enforcement",
                "UiPath API Workflow",
                "Licensed Tool Proxy calls /license-decision and receives deny_and_suspend for raw PII export.",
                "LIVE PLATFORM PATH",
                "The public endpoint is read-only demo support; the judge-facing path should start from UiPath.",
            ),
            _row(
                "UiPath-native failure analysis",
                "Studio Web / Agent Builder",
                "Failure Analyst Agent debug trace completed certification failure analysis.",
                "LIVE NATIVE AGENT PROOF",
                "Other roles are contract-backed until they receive their own live debug traces.",
            ),
            _row(
                "Agentic test swarm simulation",
                "Vercel worker called by UiPath",
                "/run-live-swarm and /live-swarm-view show attack, failure analysis, repair candidate, retest, and permit.",
                "DETERMINISTIC DEMO",
                "This is not a substitute for UiPath platform evidence; it is the worker implementation behind UiPath calls.",
            ),
            _row(
                "Requirement-to-test traceability",
                "Test Manager Requirements",
                "REQ-PII-001 links policy to TC-001 through TC-006 in /test-cloud-traceability-view.",
                "NEXT PLATFORM POLISH",
                "Create the real Test Manager requirement before claiming this as live tenant proof.",
            ),
            _row(
                "Create Defect webhook loop",
                "Test Manager Webhooks",
                "/test-manager-webhook/create-defect converts failed TC-001 evidence into ATS-DEFECT-TC-001.",
                "WEBHOOK-COMPATIBLE DEMO",
                "Configure the live Test Manager integration before claiming tenant-triggered defect creation.",
            ),
        ],
        "recommended_demo_order": [
            "Start in UiPath Studio Web or API Workflow, not Vercel.",
            "Show Test Manager six-case after-repair evidence.",
            "Show Action Center pending approval and approve it live.",
            "Show API Workflow runtime denial for raw PII export.",
            "Use Vercel views only as readable worker output and evidence graph support.",
        ],
        "judge_line": (
            "This matrix prevents overclaiming: live UiPath proof is separated from "
            "deterministic worker evidence and near-native blueprint items."
        ),
    }
