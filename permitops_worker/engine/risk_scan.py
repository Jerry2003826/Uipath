from permitops_worker.schemas import AgentToolCall


def scan_risk(call: AgentToolCall) -> dict:
    if call.action == "export_raw_customer_emails" or call.payload.get("data_type") in {"raw_email", "raw_pii"}:
        return {
            "risk_level": "critical",
            "risk": "raw_pii_export_without_license",
            "policy_id": "pii.raw_export.requires_license",
            "recommended_state": "Test Generation",
        }

    if call.action.startswith("get_aggregate"):
        return {
            "risk_level": "medium",
            "risk": "aggregate_customer_data_access",
            "policy_id": "pii.aggregate_access.allowed",
            "recommended_state": "Test Generation",
        }

    return {
        "risk_level": "high",
        "risk": "unsupported_agent_tool_call",
        "policy_id": "runtime.unauthorized_access.suspend",
        "recommended_state": "Test Generation",
    }
