import json
from pathlib import Path

from fastapi.testclient import TestClient

import permitops_worker.app as worker_app


CASE_DIR = Path("evidence/case_001")
PACK = CASE_DIR / "uipath_native_agent_pack.json"
AGENT_SPECS = [
    Path("uipath/agents/policy_miner_agent.md"),
    Path("uipath/agents/red_team_agent.md"),
    Path("uipath/agents/test_designer_agent.md"),
]


def test_uipath_native_agent_specs_are_platform_ready():
    for spec_path in AGENT_SPECS:
        text = spec_path.read_text(encoding="utf-8")
        for phrase in [
            "UiPath surface",
            "Agent Builder purpose",
            "Input variables",
            "System prompt",
            "Expected JSON output",
            "Test Cloud evidence link",
            "Judge demo line",
        ]:
            assert phrase in text


def test_uipath_native_agent_pack_names_multiple_native_agents():
    pack = json.loads(PACK.read_text(encoding="utf-8"))

    assert pack["pack_name"] == "UiPath-Native Agent Depth Pack"
    assert pack["worker_endpoint"] == "/uipath-native-agent-pack"
    assert pack["positioning"] == "UiPath-native agents deepen the testing swarm; the permit remains the output."

    names = {agent["name"] for agent in pack["agents"]}
    assert {
        "UiPath Policy Miner Agent",
        "UiPath Red-Team Agent",
        "UiPath Test Designer Agent",
        "UiPath Failure Analyst Agent",
    }.issubset(names)

    for agent in pack["agents"]:
        assert agent["runtime"] == "uipath_native_orchestrated"
        assert agent["uipath_surface"] in {"Studio Web Autonomous Agent", "Agent Builder / Studio Web"}
        assert agent["input_contract"]
        assert agent["output_contract"]
        assert agent["test_cloud_evidence"]


def test_agentic_test_agents_distinguish_uipath_native_roles():
    data = json.loads((CASE_DIR / "agentic_test_agents.json").read_text(encoding="utf-8"))
    agents = {agent["name"]: agent for agent in data["agents"]}

    assert agents["Policy Miner Agent"]["uipath_native_candidate"] is True
    assert agents["Red-Team Agent"]["uipath_native_candidate"] is True
    assert agents["Test Designer Agent"]["uipath_native_candidate"] is True
    assert agents["Failure Analyst Agent"]["uipath_native_implemented"] is True
    assert "evidence/case_001/uipath_native_agent_pack.json" in data["native_agent_depth_evidence"]


def test_api_exposes_uipath_native_agent_pack():
    client = TestClient(worker_app.app)

    response = client.get("/uipath-native-agent-pack")

    assert response.status_code == 200
    payload = response.json()
    assert payload["pack_name"] == "UiPath-Native Agent Depth Pack"
    assert {agent["name"] for agent in payload["agents"]} >= {
        "UiPath Policy Miner Agent",
        "UiPath Red-Team Agent",
        "UiPath Test Designer Agent",
        "UiPath Failure Analyst Agent",
    }
