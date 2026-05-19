from pathlib import Path

from fastapi.testclient import TestClient

import permitops_worker.app as worker_app


def test_api_routes_write_runtime_evidence_to_configured_tmp_root(monkeypatch, tmp_path):
    case_id = "api_regression_case"
    api_root = tmp_path / "api_evidence"
    monkeypatch.setattr(worker_app, "API_EVIDENCE_ROOT", api_root)
    client = TestClient(worker_app.app)

    run_response = client.post("/run-certification-tests", json={"case_id": case_id, "phase": "after"})
    assert run_response.status_code == 200
    assert (api_root / case_id / "test_results_after.json").exists()
    assert (api_root / case_id / "test_cases.json").exists()

    compile_response = client.post("/compile-license", json={"case_id": case_id, "human_approved": True})
    assert compile_response.status_code == 200
    assert compile_response.json()["license_level"] == "L2_aggregate_access"

    decision_response = client.post(
        "/license-decision",
        json={
            "case_id": case_id,
            "source_agent": "marketing-outreach-agent",
            "target_agent": "customer-data-agent",
            "action": "export_raw_customer_emails",
            "payload": {"segment": "VIP", "count": 500, "data_type": "raw_email"},
        },
    )
    assert decision_response.status_code == 200
    assert decision_response.json()["decision"] == "deny_and_suspend"

    trace_response = client.post("/capture-trace", json={"case_id": case_id, "provider": "replay", "model": "captured-fixture"})
    assert trace_response.status_code == 200
    assert (api_root / case_id / "raw_llm_response.json").exists()
    assert not (Path("evidence") / case_id).exists()


def test_api_rejects_case_id_path_traversal(monkeypatch, tmp_path):
    monkeypatch.setattr(worker_app, "API_EVIDENCE_ROOT", tmp_path / "api_evidence")
    client = TestClient(worker_app.app)

    response = client.post("/capture-trace", json={"case_id": "../escape"})

    assert response.status_code == 400
    assert response.json() == {"detail": "case_id must contain only letters, numbers, hyphen, or underscore"}
    assert not (tmp_path / "escape").exists()
