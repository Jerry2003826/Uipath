import json
from pathlib import Path

from fastapi.testclient import TestClient

import permitops_worker.app as worker_app
from permitops_worker.cli import build_parser
from permitops_worker.engine.test_cloud_traceability import build_test_cloud_traceability_pack


CASE_DIR = Path("evidence/case_001")


def test_traceability_pack_links_requirement_to_permit():
    pack = build_test_cloud_traceability_pack("case_001")

    assert pack["system_name"] == "Test Cloud Native Traceability Pack"
    assert pack["claim"] == "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit"
    assert pack["requirement"]["requirement_id"] == "REQ-PII-001"
    assert pack["requirement"]["uipath_surface"] == "Test Manager Requirements"
    assert pack["execution"]["execution_id"] == "59ea06c1-8074-0f00-8ea7-0b49ad83e475"
    assert pack["execution"]["result_summary"] == "6 passed / 0 failed / 0 not executed"
    assert pack["runtime_permit"]["decision"] == "deny_and_suspend"

    test_ids = {case["test_id"] for case in pack["test_cases"]}
    assert {"TC-001", "TC-002", "TC-003", "TC-004", "TC-005", "TC-006"} == test_ids

    edge_pairs = {(edge["from"], edge["to"], edge["relation"]) for edge in pack["traceability_edges"]}
    assert ("REQ-PII-001", "TC-001", "validated_by") in edge_pairs
    assert ("TC-001", "defect-webhook-blueprint", "can_trigger") in edge_pairs
    assert ("test-execution-20260522-1544", "permitops-runtime-permit", "supports") in edge_pairs
    assert ("permitops-runtime-permit", "api-workflow-deny-suspend", "enforced_by") in edge_pairs


def test_obsolete_test_scout_is_a_native_test_cloud_extension():
    pack = build_test_cloud_traceability_pack("case_001")
    scout = pack["obsolete_test_scout"]

    assert scout["agent_name"] == "Obsolete Test Scout"
    assert scout["uipath_surface"] == "Test Manager Optimize coverage / Find obsolete tests"
    assert scout["current_decision"] == "no_obsolete_tests_in_current_scope"
    assert scout["future_schema_change_rule"] == (
        "When requirements or Customer Data Agent tool schemas change, classify tests as keep, update, retire_candidate, or coverage_gap."
    )
    assert {"TC-001", "TC-006"}.issubset(set(scout["tests_to_keep"]))
    assert "REQ-PII-001" in scout["inputs"]


def test_api_exposes_traceability_pack_and_view():
    client = TestClient(worker_app.app)

    response = client.get("/test-cloud-traceability")
    view = client.get("/test-cloud-traceability-view")

    assert response.status_code == 200
    assert response.json()["claim"] == "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit"
    assert response.json()["requirement"]["requirement_id"] == "REQ-PII-001"
    assert view.status_code == 200
    assert "Test Cloud Native Traceability Pack" in view.text
    assert "REQ-PII-001" in view.text
    assert "Obsolete Test Scout" in view.text


def test_cli_exposes_traceability_pack_generation():
    parser = build_parser()

    args = parser.parse_args(["test-cloud-traceability-local"])

    assert args.func.__name__ == "cmd_test_cloud_traceability_local"


def test_static_traceability_pack_exists_after_generation():
    path = CASE_DIR / "test_cloud_traceability_pack.json"

    assert path.exists()
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["system_name"] == "Test Cloud Native Traceability Pack"
    assert payload["requirement"]["requirement_id"] == "REQ-PII-001"
