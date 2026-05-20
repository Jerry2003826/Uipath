from fastapi.testclient import TestClient

import permitops_worker.app as worker_app
from permitops_worker.engine.v11_live_swarm import (
    build_uipath_one_click_runbook,
    create_antibody_test,
    run_live_agentic_testing_loop,
    select_tests_for_change,
    simulate_customer_data_agent,
)
from permitops_worker.schemas import AgentToolCall


def _raw_email_call() -> AgentToolCall:
    return AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="export_raw_customer_emails",
        payload={"segment": "VIP", "count": 500, "data_type": "raw_email"},
    )


def test_customer_data_agent_is_vulnerable_before_repair():
    result = simulate_customer_data_agent(_raw_email_call(), guardrail_enabled=False)

    assert result["decision"] == "allow"
    assert result["guardrail"] == "missing"
    assert result["contains_raw_pii"] is True
    assert result["sample_output"]["emails"][0].endswith("@example.com")


def test_customer_data_agent_denies_raw_email_after_repair_but_allows_aggregate():
    raw_result = simulate_customer_data_agent(_raw_email_call(), guardrail_enabled=True)
    aggregate_result = simulate_customer_data_agent(
        AgentToolCall(
            source_agent="marketing-outreach-agent",
            target_agent="customer-data-agent",
            action="get_aggregate_segment_count",
            payload={"segment": "VIP", "count": 500, "data_type": "aggregate"},
        ),
        guardrail_enabled=True,
    )

    assert raw_result["decision"] == "deny_and_suspend"
    assert raw_result["guardrail"] == "raw_pii_export_block"
    assert aggregate_result["decision"] == "allow"
    assert aggregate_result["sample_output"] == {"segment": "VIP", "eligible_count": 500}


def test_test_selector_adds_phone_antibody_for_changed_customer_data_tool():
    selection = select_tests_for_change(
        changed_actions=["export_customer_phone_numbers"],
        recent_failures=["TC-001"],
        coverage_tags=["PII", "agent-to-agent"],
    )

    assert "TC-006" in selection["selected_tests"]
    assert selection["generated_antibody_tests"] == ["TC-006"]
    assert selection["change_impact"] == "new_raw_pii_tool_surface"


def test_incident_memory_turns_runtime_violation_into_antibody_test():
    antibody = create_antibody_test(
        {
            "event_id": "runtime-event-phone-001",
            "action": "export_customer_phone_numbers",
            "payload": {"segment": "VIP", "count": 500, "data_type": "raw_phone"},
        }
    )

    assert antibody["test_id"] == "TC-006"
    assert antibody["source_event_id"] == "runtime-event-phone-001"
    assert antibody["expected_decision"] == "deny_and_suspend"
    assert antibody["memory_type"] == "incident_to_regression_test"


def test_v11_live_loop_attacks_repairs_retests_and_records_antibody():
    run = run_live_agentic_testing_loop(
        case_id="case_001",
        changed_actions=["export_customer_phone_numbers"],
    )

    assert run["version"] == "V11 Award Upgrade"
    assert run["before_repair"]["agent_result"]["decision"] == "allow"
    assert run["failure_analysis"]["failed_test"] == "TC-001"
    assert run["repair_candidate"]["guardrail"] == "raw_pii_export_block"
    assert run["after_repair"]["agent_result"]["decision"] == "deny_and_suspend"
    assert "TC-006" in run["test_selector"]["selected_tests"]
    assert run["incident_memory"]["antibody_test"]["test_id"] == "TC-006"
    assert run["permit_output"]["license_level"] == "L2_aggregate_access"
    assert run["uipath_control_plane"]["claim"] == "UiPath is the no-code orchestration and governance layer."
    assert [artifact["component"] for artifact in run["uipath_control_plane"]["artifacts"]] == [
        "Maestro / Studio Web",
        "Test Cloud / Test Manager",
        "Action Center",
        "API Workflow",
        "Automation Cloud",
    ]
    assert run["uipath_control_plane"]["operator_actions"][0]["no_code_action"] == "Approve restricted permit"


def test_uipath_one_click_runbook_links_platform_surfaces():
    runbook = build_uipath_one_click_runbook("case_001")

    assert runbook["runbook_name"] == "UiPath One-Click Agentic Test Swarm Run"
    assert runbook["trigger"]["uipath_surface"] == "Studio Web / API Workflow"
    assert runbook["trigger"]["worker_call"]["path"] == "/run-live-swarm"
    assert [step["uipath_surface"] for step in runbook["sequence"]] == [
        "Studio Web / API Workflow",
        "Test Cloud / Test Manager",
        "Action Center",
        "API Workflow",
        "Test Cloud",
    ]
    assert "TC-006" in runbook["test_cloud_delta"]["mapped_tests"]
    assert runbook["action_center"]["task_id"] == "3545796"
    assert runbook["runtime_enforcement"]["expected_decision"] == "deny_and_suspend"


def test_run_live_swarm_api_writes_evidence(monkeypatch, tmp_path):
    monkeypatch.setattr(worker_app, "API_EVIDENCE_ROOT", tmp_path / "api_evidence")
    client = TestClient(worker_app.app)

    response = client.post(
        "/run-live-swarm",
        json={"case_id": "api_live_case", "changed_actions": ["export_customer_phone_numbers"]},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["after_repair"]["agent_result"]["decision"] == "deny_and_suspend"
    assert (tmp_path / "api_evidence" / "api_live_case" / "uipath_one_click_runbook.json").exists()
    assert (tmp_path / "api_evidence" / "api_live_case" / "v11_live_swarm_run.json").exists()


def test_uipath_one_click_runbook_endpoint_writes_evidence(monkeypatch, tmp_path):
    monkeypatch.setattr(worker_app, "API_EVIDENCE_ROOT", tmp_path / "api_evidence")
    client = TestClient(worker_app.app)

    response = client.get("/uipath-one-click-runbook", params={"case_id": "api_live_case"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["trigger"]["operator_action"] == "Click Run in UiPath"
    assert payload["runtime_enforcement"]["worker_call"]["path"] == "/license-decision"
    assert (tmp_path / "api_evidence" / "api_live_case" / "uipath_one_click_runbook.json").exists()


def test_live_swarm_view_renders_browser_demo(monkeypatch, tmp_path):
    monkeypatch.setattr(worker_app, "API_EVIDENCE_ROOT", tmp_path / "api_evidence")
    client = TestClient(worker_app.app)

    response = client.get(
        "/live-swarm-view",
        params={"case_id": "browser_case", "changed_actions": "export_customer_phone_numbers"},
    )

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Agentic Test Swarm" in response.text
    assert "UiPath No-Code Control Plane" in response.text
    assert "One-Click UiPath Runbook" in response.text
    assert "/uipath-one-click-runbook" in response.text
    assert "Approve restricted permit" in response.text
    assert "Live Public Endpoint Simulation" in response.text
    assert "deny_and_suspend" in response.text
    assert "TC-006" in response.text
    assert "PermitOps Runtime Permit" in response.text
