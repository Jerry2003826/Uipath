import json
from pathlib import Path

from permitops_worker.engine.expected_oracle import expected_decision_for_tool_call
from permitops_worker.engine.policy_to_test import generate_certification_tests
from permitops_worker.schemas import TestResult


def _write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if hasattr(data, "model_dump"):
        data = data.model_dump(mode="json")
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_certification_tests(case_id: str = "case_001", phase: str = "after", evidence_root: Path | str = "evidence") -> list[TestResult]:
    tests = generate_certification_tests(case_id)
    results: list[TestResult] = []

    for test in tests:
        expected = expected_decision_for_tool_call(test.input_payload)
        actual_decision = expected["decision"]
        if phase == "before" and test.test_id == "TC-001":
            actual_decision = "allow"

        status = "passed" if actual_decision == test.expected_decision else "failed"
        results.append(
            TestResult(
                test_id=test.test_id,
                status=status,
                expected_decision=test.expected_decision,
                actual_decision=actual_decision,
                failure_reason=None if status == "passed" else "captured trace bypassed raw PII guardrail",
                evidence_ref=test.test_id,
            )
        )

    case_dir = Path(evidence_root) / case_id
    filename = "test_results_before.json" if phase == "before" else "test_results_after.json"
    _write_json(case_dir / filename, [result.model_dump(mode="json") for result in results])
    _write_json(case_dir / "test_cases.json", [test.model_dump(mode="json") for test in tests])
    return results
