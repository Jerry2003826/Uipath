from fastapi.testclient import TestClient

import permitops_worker.app as worker_app
from permitops_worker.engine.judge_evidence import build_judge_evidence_matrix


def test_judge_evidence_matrix_separates_live_demo_and_blueprint_statuses():
    matrix = build_judge_evidence_matrix("case_001")

    statuses = {row["status"] for row in matrix["rows"]}
    claims = {row["claim"] for row in matrix["rows"]}

    assert "LIVE TENANT PROOF" in statuses
    assert "DETERMINISTIC DEMO" in statuses
    assert "NEXT PLATFORM POLISH" in statuses
    assert "WEBHOOK-COMPATIBLE DEMO" in statuses
    assert "Six-case certification result" in claims
    assert "Requirement-to-test traceability" in claims
    assert matrix["judge_line"].startswith("This matrix prevents overclaiming")


def test_api_exposes_judge_evidence_matrix_view():
    client = TestClient(worker_app.app)

    json_response = client.get("/judge-evidence-matrix")
    view_response = client.get("/judge-evidence-matrix-view")

    assert json_response.status_code == 200
    assert json_response.json()["system_name"] == "Judge Evidence Matrix"
    assert view_response.status_code == 200
    assert "LIVE TENANT PROOF" in view_response.text
    assert "WEBHOOK-COMPATIBLE DEMO" in view_response.text
