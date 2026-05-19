import json
from pathlib import Path


CASE_DIR = Path("evidence/case_001")


def _load(name: str):
    return json.loads((CASE_DIR / name).read_text(encoding="utf-8"))


def test_swarm_agent_map_names_testing_agents_and_permit_as_output():
    data = _load("agentic_test_agents.json")

    assert data["project_name"] == "Agentic Test Swarm"
    assert data["permit_role"] == "output_not_product"

    names = {agent["name"] for agent in data["agents"]}
    assert {
        "Policy Miner Agent",
        "Red-Team Agent",
        "Test Designer Agent",
        "Test Selector Agent",
        "Failure Analyst Agent",
        "Repair Agent",
        "Re-test Orchestrator",
        "Quality Governor",
    }.issubset(names)


def test_red_team_scenarios_drive_test_designer_cases():
    red_team = _load("red_team_scenarios.json")
    designed = _load("test_designer_cases.json")

    red_team_ids = {scenario["scenario_id"] for scenario in red_team["scenarios"]}
    assert {"RT-001", "RT-002", "RT-003"}.issubset(red_team_ids)

    for test_case in designed["test_cases"]:
        assert test_case["source_scenario_id"] in red_team_ids
        assert test_case["expected_source"] == "deterministic_oracle"
        assert test_case["test_cloud_mapping"]["project"] == "PermitOps V9.1 Agent Certification"


def test_selector_failure_repair_and_governor_chain_is_consistent():
    selection = _load("test_selector_decision.json")
    failure = _load("failure_analysis.json")
    run = _load("agentic_test_swarm_run.json")

    assert selection["selection_reason"].startswith("Customer Data Agent")
    assert "TC-001" in selection["selected_tests"]
    assert failure["failed_test"] == "TC-001"
    assert failure["retest_strategy"] == "targeted_retest"
    assert set(failure["tests_to_rerun"]) == {"TC-001", "TC-005"}

    assert run["final_governance_artifact"]["name"] == "PermitOps Runtime Permit"
    assert run["final_governance_artifact"]["license_level"] == "L2_aggregate_access"
    assert run["uipath_runtime_enforcement"]["decision"] == "deny_and_suspend"
