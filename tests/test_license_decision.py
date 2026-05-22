from datetime import datetime, timedelta, timezone

from permitops_worker.engine.compiler import compile_license
from permitops_worker.engine.license_decision import decide
from permitops_worker.schemas import AgentToolCall, TestResult


def _license(status="active"):
    result = TestResult(
        test_id="TC-001",
        status="passed",
        expected_decision="deny",
        actual_decision="deny",
        evidence_ref="TC-001",
    )
    license_doc = compile_license(
        case_id="case_001",
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        before_results=[result],
        after_results=[result],
        human_approved=True,
    )
    license_doc.status = status
    return license_doc


def test_blocked_raw_email_export_denies_and_suspends():
    license_doc = _license()
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="export_raw_customer_emails",
        payload={"segment": "VIP", "count": 500, "data_type": "raw_email"},
    )

    result = decide(call, license_doc)

    assert result["decision"] == "deny_and_suspend"
    assert result["license_status"] == "suspended"
    assert result["previous_license_status"] == "active"
    assert result["next_license_level"] == "SX_suspended"
    assert license_doc.status == "active"
    assert license_doc.license_level == "L2_aggregate_access"


def test_aggregate_segment_count_is_allowed_by_license():
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="get_aggregate_segment_count",
        payload={"segment": "VIP", "data_type": "aggregate"},
    )

    result = decide(call, _license())

    assert result["decision"] == "allow"
    assert result["license_status"] == "active"


def test_inactive_license_denies():
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="get_aggregate_segment_count",
        payload={"segment": "VIP", "data_type": "aggregate"},
    )

    result = decide(call, _license(status="pending_human_approval"))

    assert result["decision"] == "deny"
    assert result["reason"] == "license_not_active"


def test_expired_license_denies():
    license_doc = _license()
    issued = datetime.now(timezone.utc) - timedelta(days=400)
    license_doc.license_metadata.issued_at = issued.isoformat().replace("+00:00", "Z")
    license_doc.license_metadata.valid_until = (issued + timedelta(days=365)).isoformat().replace("+00:00", "Z")
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="get_aggregate_segment_count",
        payload={"segment": "VIP", "data_type": "aggregate"},
    )

    result = decide(call, license_doc)

    assert result["decision"] == "deny"
    assert result["reason"] == "license_expired"
