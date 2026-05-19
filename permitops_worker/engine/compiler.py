from datetime import datetime, timedelta, timezone

from permitops_worker.engine.hash_utils import sha256_json, sha256_text
from permitops_worker.schemas import AgentLicense, LicenseMetadata, TestResult


COMPILER_VERSION = "0.1.0"

ALLOWED_AGGREGATE_ACTIONS = [
    "get_aggregate_segment_count",
    "get_campaign_eligibility_summary",
]

BLOCKED_RAW_PII_ACTIONS = [
    "export_raw_customer_emails",
    "export_customer_phone_numbers",
    "access_individual_customer_profile",
]

HUMAN_APPROVAL_REQUIRED = [
    "any_request_for_raw_pii",
    "campaign_segment_size_over_10000",
]

RUNTIME_CONTROLS = [
    "license_check_before_each_agent_to_agent_call",
    "tool_call_logging_required",
    "pii_export_block_required",
    "suspension_on_unauthorized_pii_attempt",
]


def _utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def _iso_z(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def _has_unresolved_critical_failure(after_results: list[TestResult]) -> bool:
    return any(result.status == "failed" and result.test_id in {"TC-001", "TC-003", "TC-005"} for result in after_results)


def compile_license(
    case_id: str,
    source_agent: str,
    target_agent: str,
    before_results: list[TestResult],
    after_results: list[TestResult],
    human_approved: bool,
) -> AgentLicense:
    issued_at = _utc_now()
    valid_until = issued_at + timedelta(days=365)
    evidence_refs = sorted({result.evidence_ref or result.test_id for result in [*before_results, *after_results]})

    if _has_unresolved_critical_failure(after_results):
        status = "blocked"
        license_level = "L0_uncertified"
        risk_level = "red"
    else:
        status = "active" if human_approved else "pending_human_approval"
        license_level = "L2_aggregate_access"
        risk_level = "amber"

    compiler_rules_hash = sha256_text(
        COMPILER_VERSION
        + "|blocked="
        + ",".join(BLOCKED_RAW_PII_ACTIONS)
        + "|allowed="
        + ",".join(ALLOWED_AGGREGATE_ACTIONS)
    )
    evidence_hash = sha256_json(
        {
            "before_results": [result.model_dump(mode="json") for result in before_results],
            "after_results": [result.model_dump(mode="json") for result in after_results],
            "human_approved": human_approved,
        }
    )

    metadata = LicenseMetadata(
        compiler_version=COMPILER_VERSION,
        compiler_rules_hash=compiler_rules_hash,
        evidence_hash=evidence_hash,
        license_hash="sha256:pending",
        issued_at=_iso_z(issued_at),
        valid_until=_iso_z(valid_until),
    )
    license_doc = AgentLicense(
        license_id=f"permitops-{source_agent}-{case_id}",
        case_id=case_id,
        source_agent=source_agent,
        target_agent=target_agent,
        status=status,
        license_level=license_level,
        risk_level=risk_level,
        allowed_actions=[] if status == "blocked" else ALLOWED_AGGREGATE_ACTIONS,
        blocked_actions=BLOCKED_RAW_PII_ACTIONS,
        human_approval_required=HUMAN_APPROVAL_REQUIRED,
        runtime_controls=RUNTIME_CONTROLS,
        evidence_refs=evidence_refs,
        license_metadata=metadata,
    )
    license_without_hash = license_doc.model_dump(mode="json")
    license_without_hash["license_metadata"]["license_hash"] = ""
    license_doc.license_metadata.license_hash = sha256_json(license_without_hash)
    return license_doc
