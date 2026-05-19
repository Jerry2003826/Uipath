from permitops_worker.engine.policy_to_test import generate_certification_tests


def test_generated_tests_include_core_certification_cases():
    tests = generate_certification_tests(case_id="case_001")
    ids = {test.test_id for test in tests}

    assert {"TC-001", "TC-002", "TC-005"}.issubset(ids)


def test_pii_attack_test_uses_deterministic_expected_deny():
    tests = {test.test_id: test for test in generate_certification_tests(case_id="case_001")}

    assert tests["TC-001"].expected_decision == "deny"
    assert tests["TC-001"].expected_reason == "raw_pii_export_not_permitted_without_license"
    assert tests["TC-001"].input_payload.action == "export_raw_customer_emails"


def test_aggregate_test_expected_allow_and_generated_source_present():
    tests = {test.test_id: test for test in generate_certification_tests(case_id="case_001")}

    assert tests["TC-002"].expected_decision == "allow"
    assert "coding-agent" in tests["TC-002"].llm_generated_scenario
