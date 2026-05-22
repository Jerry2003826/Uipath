import json
from pathlib import Path

from fastapi.testclient import TestClient

import permitops_worker.app as worker_app
from permitops_worker.cli import build_parser
from permitops_worker.engine.test_manager_webhook import (
    build_create_defect_webhook_demo,
    handle_create_defect_webhook,
)


CASE_DIR = Path("evidence/case_001")


def _payload() -> dict:
    return {
        "testExecutionId": "59ea06c1-8074-0f00-8ea7-0b49ad83e475",
        "testCaseId": "TC-001",
        "variationId": "default",
        "linkToTestCaseLog": "https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/testexecutions/59ea06c1-8074-0f00-8ea7-0b49ad83e475",
    }


def test_create_defect_webhook_turns_failed_test_into_repair_defect():
    result = handle_create_defect_webhook("case_001", _payload())

    assert result["event_name"] == "Test Manager Create Defect webhook"
    assert result["source"]["testExecutionId"] == "59ea06c1-8074-0f00-8ea7-0b49ad83e475"
    assert result["detected_failed_test"] == "TC-001"
    assert result["failure_analysis"]["root_cause"].startswith("The captured Marketing Outreach Agent behavior")
    assert result["defect_payload"]["external_id"] == "ATS-DEFECT-TC-001"
    assert result["defect_payload"]["severity"] == "critical"
    assert "raw PII export guardrail" in result["defect_payload"]["summary"]
    assert "targeted_retest" in result["defect_payload"]["recommended_next_action"]
    assert "TC-005" in result["defect_payload"]["tests_to_rerun"]
    assert result["uipath_response"]["status"] == "defect_ready_for_external_tracker"


def test_create_defect_webhook_demo_preserves_test_cloud_context():
    demo = build_create_defect_webhook_demo("case_001")

    assert demo["demo_name"] == "Test Manager Create Defect Webhook Demo"
    assert demo["incoming_test_manager_payload"]["testCaseId"] == "TC-001"
    assert demo["webhook_response"]["defect_payload"]["external_id"] == "ATS-DEFECT-TC-001"
    assert demo["traceability"]["requirement_id"] == "REQ-PII-001"
    assert demo["traceability"]["test_cloud_chain"] == "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit"
    assert demo["judge_line"].startswith("Test Manager can trigger")


def test_api_exposes_create_defect_webhook_and_demo_view():
    client = TestClient(worker_app.app)

    response = client.post("/test-manager-webhook/create-defect", json=_payload())
    demo = client.get("/test-manager-webhook-demo")
    view = client.get("/test-manager-webhook-demo-view")

    assert response.status_code == 200
    assert response.json()["defect_payload"]["external_id"] == "ATS-DEFECT-TC-001"
    assert demo.status_code == 200
    assert demo.json()["demo_name"] == "Test Manager Create Defect Webhook Demo"
    assert view.status_code == 200
    assert "Test Manager Create Defect Webhook Demo" in view.text
    assert "ATS-DEFECT-TC-001" in view.text
    assert "Failure Analyst Agent" in view.text


def test_cli_exposes_test_manager_webhook_demo_generation():
    parser = build_parser()

    args = parser.parse_args(["test-manager-webhook-demo-local"])

    assert args.func.__name__ == "cmd_test_manager_webhook_demo_local"


def test_static_webhook_demo_evidence_exists_after_generation():
    path = CASE_DIR / "test_manager_create_defect_webhook_demo.json"

    assert path.exists()
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["demo_name"] == "Test Manager Create Defect Webhook Demo"
    assert payload["webhook_response"]["defect_payload"]["external_id"] == "ATS-DEFECT-TC-001"
