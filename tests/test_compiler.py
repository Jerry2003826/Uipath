from datetime import datetime, timezone

from permitops_worker.engine.compiler import compile_license
from permitops_worker.schemas import TestResult


def _result(test_id, status, expected, actual):
    return TestResult(
        test_id=test_id,
        status=status,
        expected_decision=expected,
        actual_decision=actual,
        failure_reason=None if status == "passed" else "mismatched decision",
        evidence_ref=test_id,
    )


def test_unresolved_critical_failure_blocks_license():
    license_doc = compile_license(
        case_id="case_001",
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        before_results=[_result("TC-001", "failed", "deny", "allow")],
        after_results=[_result("TC-001", "failed", "deny", "allow")],
        human_approved=False,
    )

    assert license_doc.status == "blocked"
    assert license_doc.license_level == "L0_uncertified"


def test_repaired_pii_failure_with_human_approval_gets_l2_active_license():
    license_doc = compile_license(
        case_id="case_001",
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        before_results=[
            _result("TC-001", "failed", "deny", "allow"),
            _result("TC-002", "passed", "allow", "allow"),
        ],
        after_results=[
            _result("TC-001", "passed", "deny", "deny"),
            _result("TC-005", "passed", "deny", "deny"),
        ],
        human_approved=True,
    )

    assert license_doc.status == "active"
    assert license_doc.license_level == "L2_aggregate_access"
    assert "get_aggregate_segment_count" in license_doc.allowed_actions
    assert "export_raw_customer_emails" in license_doc.blocked_actions
    assert "any_request_for_raw_pii" in license_doc.human_approval_required


def test_license_metadata_hashes_and_validity_window_are_present():
    license_doc = compile_license(
        case_id="case_001",
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        before_results=[_result("TC-001", "failed", "deny", "allow")],
        after_results=[_result("TC-001", "passed", "deny", "deny")],
        human_approved=True,
    )

    metadata = license_doc.license_metadata
    assert metadata.compiler_rules_hash.startswith("sha256:")
    assert metadata.evidence_hash.startswith("sha256:")
    assert metadata.license_hash.startswith("sha256:")

    issued = datetime.fromisoformat(metadata.issued_at.replace("Z", "+00:00"))
    valid_until = datetime.fromisoformat(metadata.valid_until.replace("Z", "+00:00"))
    assert issued.tzinfo == timezone.utc
    assert (valid_until - issued).days == 365
