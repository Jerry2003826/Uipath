from fastapi.testclient import TestClient

import permitops_worker.app as worker_app
from permitops_worker.cli import build_parser
from permitops_worker.engine.execution_timeline import build_before_after_execution_evidence


def test_before_after_execution_evidence_separates_failure_from_final_certification():
    evidence = build_before_after_execution_evidence("case_001")

    before, after = evidence["runs"]

    assert evidence["system_name"] == "Before / After Repair Execution Evidence"
    assert before["phase"] == "before_repair"
    assert before["status"] == "DETERMINISTIC FAILED RUN"
    assert before["result_summary"] == "0 passed / 1 failed / 0 not executed"
    assert before["failed_tests"] == ["TC-001"]
    assert after["phase"] == "after_repair"
    assert after["status"] == "LIVE TENANT PROOF"
    assert after["result_summary"] == "6 passed / 0 failed / 0 not executed"
    assert after["execution_id"] == "59ea06c1-8074-0f00-8ea7-0b49ad83e475"
    assert evidence["judge_line"].startswith("Do not present the six passed execution")


def test_before_after_execution_evidence_api_and_view():
    client = TestClient(worker_app.app)

    json_response = client.get("/before-after-execution-evidence")
    view_response = client.get("/before-after-execution-evidence-view")

    assert json_response.status_code == 200
    assert json_response.json()["runs"][0]["failed_tests"] == ["TC-001"]
    assert view_response.status_code == 200
    assert "Before / After Repair Execution Evidence" in view_response.text
    assert "DETERMINISTIC FAILED RUN" in view_response.text
    assert "LIVE TENANT PROOF" in view_response.text


def test_cli_exposes_before_after_execution_evidence_generation():
    parser = build_parser()

    args = parser.parse_args(["before-after-execution-evidence-local"])

    assert args.func.__name__ == "cmd_before_after_execution_evidence_local"
