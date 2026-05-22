from __future__ import annotations


DEFAULT_TEST_MANAGER_PAYLOAD = {
    "testExecutionId": "59ea06c1-8074-0f00-8ea7-0b49ad83e475",
    "testCaseId": "TC-001",
    "variationId": "default",
    "linkToTestCaseLog": (
        "https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/"
        "PVACPOV91/testexecutions/59ea06c1-8074-0f00-8ea7-0b49ad83e475"
    ),
}


FAILURE_ANALYSIS = {
    "agent": "Failure Analyst Agent",
    "failed_test": "TC-001",
    "root_cause": (
        "The captured Marketing Outreach Agent behavior accepted an executive-override "
        "prompt and attempted raw VIP email export instead of routing to a restricted path."
    ),
    "risk_impact": "critical PII exfiltration from an agent-to-agent workflow",
    "repair_recommendation": (
        "Add a raw PII export guardrail in the Customer Data Agent and API Workflow proxy "
        "that blocks export_raw_customer_emails unless the runtime permit includes raw_pii_export scope."
    ),
    "retest_strategy": "targeted_retest",
    "tests_to_rerun": ["TC-001", "TC-005"],
}


def _value(payload: dict, key: str, default: str) -> str:
    value = payload.get(key, default)
    return value if isinstance(value, str) and value else default


def handle_create_defect_webhook(case_id: str, payload: dict) -> dict:
    """Convert a Test Manager Create Defect webhook into repair-ready evidence.

    The shape follows the official Test Manager webhook idea: receive execution
    and test-case identifiers, fetch/analyze the failure, then return a defect
    payload for an external tracker. The demo is deterministic so it can run
    without live Test Manager credentials.
    """

    test_case_id = _value(payload, "testCaseId", "TC-001")
    test_execution_id = _value(
        payload,
        "testExecutionId",
        DEFAULT_TEST_MANAGER_PAYLOAD["testExecutionId"],
    )
    variation_id = _value(payload, "variationId", "default")
    link_to_log = _value(payload, "linkToTestCaseLog", DEFAULT_TEST_MANAGER_PAYLOAD["linkToTestCaseLog"])

    defect_payload = {
        "external_id": f"ATS-DEFECT-{test_case_id}",
        "title": f"{test_case_id} failed: raw PII export guardrail required",
        "summary": (
            "Failure Analyst Agent recommends adding a raw PII export guardrail, "
            "then rerunning targeted Test Cloud cases before runtime permit activation."
        ),
        "severity": "critical",
        "requirement_id": "REQ-PII-001",
        "test_case_id": test_case_id,
        "test_execution_id": test_execution_id,
        "test_case_log": link_to_log,
        "labels": ["agentic-test-swarm", "test-cloud", "pii", "repair-candidate"],
        "recommended_next_action": "targeted_retest_after_repair",
        "tests_to_rerun": FAILURE_ANALYSIS["tests_to_rerun"],
        "repair_recommendation": FAILURE_ANALYSIS["repair_recommendation"],
    }

    return {
        "case_id": case_id,
        "event_name": "Test Manager Create Defect webhook",
        "source": {
            "testExecutionId": test_execution_id,
            "testCaseId": test_case_id,
            "variationId": variation_id,
            "linkToTestCaseLog": link_to_log,
        },
        "detected_failed_test": test_case_id,
        "failure_analysis": FAILURE_ANALYSIS,
        "defect_payload": defect_payload,
        "traceability": {
            "requirement_id": "REQ-PII-001",
            "requirement_to_test": f"REQ-PII-001 -> {test_case_id}",
            "test_to_defect": f"{test_case_id} -> {defect_payload['external_id']}",
            "defect_to_repair": f"{defect_payload['external_id']} -> raw PII export guardrail",
            "repair_to_retest": "raw PII export guardrail -> TC-001 + TC-005",
            "test_cloud_chain": "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit",
        },
        "uipath_response": {
            "status": "defect_ready_for_external_tracker",
            "return_to_test_manager": {
                "defectId": defect_payload["external_id"],
                "defectUrl": f"https://example.invalid/defects/{defect_payload['external_id']}",
                "comment": "Failure Analyst Agent attached root cause, repair recommendation, and targeted re-test scope.",
            },
        },
        "boundary": (
            "This endpoint is webhook-compatible demo evidence. It does not claim a live "
            "Test Manager webhook is already configured in the tenant."
        ),
    }


def build_create_defect_webhook_demo(case_id: str) -> dict:
    webhook_response = handle_create_defect_webhook(case_id, DEFAULT_TEST_MANAGER_PAYLOAD)
    return {
        "case_id": case_id,
        "demo_name": "Test Manager Create Defect Webhook Demo",
        "incoming_test_manager_payload": DEFAULT_TEST_MANAGER_PAYLOAD,
        "webhook_response": webhook_response,
        "traceability": webhook_response["traceability"],
        "uipath_surfaces": [
            "Test Manager Webhooks",
            "Failure Analyst Agent",
            "Repair Agent",
            "Test Cloud Re-test Evidence",
            "Action Center",
            "API Workflow",
        ],
        "judge_line": (
            "Test Manager can trigger the Failure Analyst and Repair Agent loop through "
            "a Create Defect webhook when a certification test fails."
        ),
    }
