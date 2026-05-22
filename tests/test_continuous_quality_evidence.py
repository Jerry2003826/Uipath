import json
from pathlib import Path

from fastapi.testclient import TestClient

import permitops_worker.app as worker_app
from permitops_worker.cli import build_parser
from permitops_worker.engine.continuous_quality import build_continuous_quality_memory, build_evidence_graph


CASE_DIR = Path("evidence/case_001")


def test_continuous_quality_memory_turns_incident_into_future_gate():
    memory = build_continuous_quality_memory("case_001")

    assert memory["system_name"] == "Continuous Quality Memory"
    assert memory["claim"] == "Runtime incidents become permanent UiPath Test Cloud regression evidence."
    assert [step["stage"] for step in memory["lifecycle"]] == [
        "Runtime incident captured",
        "Incident Memory Agent creates antibody test",
        "Test Selector prioritizes antibody coverage",
        "Test Cloud stores managed evidence",
        "Quality Governor blocks unsafe permits if antibody fails",
    ]
    assert memory["antibody_tests"][0]["test_id"] == "TC-006"
    assert memory["antibody_tests"][0]["test_cloud_case_key"] == "PVACPOV91:76"
    assert "TC-006" in memory["future_selection"]["required_tests"]
    assert memory["governor_gate"]["if_antibody_fails"] == "block_or_recertify"
    assert memory["uipath_surfaces"] == [
        "API Workflow",
        "Agent Builder / Studio Web",
        "Test Cloud / Test Manager",
        "Action Center",
        "Maestro / Studio Web",
    ]


def test_evidence_graph_links_trace_to_runtime_enforcement():
    graph = build_evidence_graph("case_001")

    assert graph["graph_name"] == "Agentic Test Swarm Evidence Graph"
    node_ids = {node["id"] for node in graph["nodes"]}
    assert {
        "trace-pii-export-001",
        "policy-pii-raw-export",
        "rt-001",
        "tc-001",
        "before-failure",
        "failure-analysis",
        "repair-candidate",
        "tc-005-retest",
        "tc-006-memory",
        "action-center-3545796",
        "runtime-permit",
        "api-workflow-deny-suspend",
    }.issubset(node_ids)

    edge_pairs = {(edge["from"], edge["to"], edge["relation"]) for edge in graph["edges"]}
    assert ("trace-pii-export-001", "rt-001", "inspires_attack") in edge_pairs
    assert ("tc-006-memory", "runtime-permit", "gates_future_permit") in edge_pairs
    assert ("runtime-permit", "api-workflow-deny-suspend", "enforced_by") in edge_pairs

    assert graph["critical_path"] == [
        "trace-pii-export-001",
        "policy-pii-raw-export",
        "rt-001",
        "tc-001",
        "before-failure",
        "failure-analysis",
        "repair-candidate",
        "tc-005-retest",
        "action-center-3545796",
        "runtime-permit",
        "api-workflow-deny-suspend",
    ]


def test_api_exposes_continuous_quality_and_evidence_graph():
    client = TestClient(worker_app.app)

    memory_response = client.get("/continuous-quality-memory")
    graph_response = client.get("/evidence-graph")
    memory_view = client.get("/continuous-quality-memory-view")
    graph_view = client.get("/evidence-graph-view")

    assert memory_response.status_code == 200
    assert memory_response.json()["system_name"] == "Continuous Quality Memory"
    assert graph_response.status_code == 200
    assert graph_response.json()["graph_name"] == "Agentic Test Swarm Evidence Graph"
    assert memory_view.status_code == 200
    assert "Continuous Quality Memory" in memory_view.text
    assert graph_view.status_code == 200
    assert "Agentic Test Swarm Evidence Graph" in graph_view.text


def test_cli_exposes_continuous_quality_commands():
    parser = build_parser()

    memory_args = parser.parse_args(["continuous-quality-memory-local"])
    graph_args = parser.parse_args(["evidence-graph-local"])

    assert memory_args.func.__name__ == "cmd_continuous_quality_memory_local"
    assert graph_args.func.__name__ == "cmd_evidence_graph_local"


def test_static_continuous_quality_evidence_files_exist_after_generation():
    for filename, expected_key in [
        ("continuous_quality_memory.json", "Continuous Quality Memory"),
        ("evidence_graph.json", "Agentic Test Swarm Evidence Graph"),
    ]:
        path = CASE_DIR / filename
        assert path.exists()
        data = json.loads(path.read_text(encoding="utf-8"))
        assert expected_key in {data.get("system_name"), data.get("graph_name")}
