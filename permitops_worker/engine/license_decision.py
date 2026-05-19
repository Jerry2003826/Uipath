from datetime import datetime, timezone

from permitops_worker.schemas import AgentLicense, AgentToolCall


def _parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _response(decision: str, reason: str, license_status: str, evidence_ref: str | None = None) -> dict[str, str]:
    output = {
        "decision": decision,
        "reason": reason,
        "license_status": license_status,
    }
    if evidence_ref:
        output["evidence_ref"] = evidence_ref
    return output


def decide(call: AgentToolCall, license_doc: AgentLicense) -> dict[str, str]:
    if license_doc.status != "active":
        return _response("deny", "license_not_active", license_doc.status)

    if _parse_utc(license_doc.license_metadata.valid_until) <= datetime.now(timezone.utc):
        return _response("deny", "license_expired", license_doc.status)

    if call.action in license_doc.blocked_actions:
        license_doc.status = "suspended"
        license_doc.license_level = "SX_suspended"
        return _response("deny_and_suspend", "blocked_action_attempted", "suspended", "runtime-event-001")

    if call.action in license_doc.allowed_actions:
        return _response("allow", "allowed_by_license", license_doc.status)

    if call.payload.get("data_type") in {"raw_email", "raw_pii"}:
        return _response("require_human_approval", "raw_pii_requires_human_approval", license_doc.status)

    return _response("deny", "unsupported_action", license_doc.status)
