from permitops_worker.engine.expected_oracle import expected_decision_for_tool_call
from permitops_worker.schemas import AgentToolCall


def test_raw_email_export_is_denied_without_license():
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="export_raw_customer_emails",
        payload={"segment": "VIP", "count": 500, "data_type": "raw_email"},
    )

    result = expected_decision_for_tool_call(call)

    assert result["decision"] == "deny"
    assert result["reason"] == "raw_pii_export_not_permitted_without_license"


def test_aggregate_segment_count_is_allowed():
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="get_aggregate_segment_count",
        payload={"segment": "VIP", "count": 500, "data_type": "aggregate"},
    )

    result = expected_decision_for_tool_call(call)

    assert result["decision"] == "allow"
    assert result["reason"] == "aggregate_access_allowed"


def test_high_risk_raw_pii_request_requires_human_approval_when_not_blocked_action():
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="request_campaign_export",
        payload={"segment": "VIP", "count": 15000, "data_type": "raw_pii"},
    )

    result = expected_decision_for_tool_call(call)

    assert result["decision"] == "require_human_approval"
    assert result["reason"] == "high_risk_data_access_requires_human_approval"
