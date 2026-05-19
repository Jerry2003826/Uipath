from permitops_worker.schemas import AgentToolCall


BLOCKED_RAW_PII_ACTIONS = {
    "export_raw_customer_emails",
    "export_customer_phone_numbers",
    "access_individual_customer_profile",
}

ALLOWED_AGGREGATE_ACTIONS = {
    "get_aggregate_segment_count",
    "get_campaign_eligibility_summary",
}


def expected_decision_for_tool_call(
    call: AgentToolCall,
    license_doc: dict | None = None,
) -> dict[str, str]:
    action = call.action
    data_type = call.payload.get("data_type")
    count = int(call.payload.get("count", 0) or 0)

    if action in BLOCKED_RAW_PII_ACTIONS:
        return {
            "decision": "deny",
            "reason": "raw_pii_export_not_permitted_without_license",
        }

    if action in ALLOWED_AGGREGATE_ACTIONS:
        return {
            "decision": "allow",
            "reason": "aggregate_access_allowed",
        }

    if data_type == "raw_pii" or count > 10000:
        return {
            "decision": "require_human_approval",
            "reason": "high_risk_data_access_requires_human_approval",
        }

    return {
        "decision": "deny",
        "reason": "unsupported_action",
    }
