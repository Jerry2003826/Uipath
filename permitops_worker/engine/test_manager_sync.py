import json
import os
from pathlib import Path

from permitops_worker.engine.policy_to_test import generate_certification_tests


class MissingUiPathConfigurationError(RuntimeError):
    pass


REQUIRED_ENV = [
    "UIPATH_TEST_MANAGER_BASE_URL",
    "UIPATH_ORG_NAME",
    "UIPATH_TENANT_NAME",
    "UIPATH_ACCESS_TOKEN",
    "UIPATH_TEST_PROJECT_ID",
]


def _write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _missing_env() -> list[str]:
    return [key for key in REQUIRED_ENV if not os.environ.get(key)]


def sync_test_cases(case_id: str, evidence_root: Path | str = "evidence", dry_run: bool = True) -> dict:
    evidence_root = Path(evidence_root)
    case_dir = evidence_root / case_id
    tests = generate_certification_tests(case_id)
    payload = {
        "case_id": case_id,
        "test_cases": [test.model_dump(mode="json") for test in tests],
    }
    _write_json(case_dir / "test_manager_sync_payload.json", payload)

    if dry_run:
        result = {
            "mode": "dry_run",
            "test_case_count": len(tests),
            "payload_path": str(case_dir / "test_manager_sync_payload.json"),
        }
        _write_json(case_dir / "test_manager_sync_result.json", result)
        return result

    missing = _missing_env()
    if missing:
        raise MissingUiPathConfigurationError(
            "Missing UiPath Test Manager configuration: " + ", ".join(missing)
        )

    result = {
        "mode": "real",
        "test_case_count": len(tests),
        "status": "ready_to_send",
        "base_url": os.environ["UIPATH_TEST_MANAGER_BASE_URL"],
        "project_id": os.environ["UIPATH_TEST_PROJECT_ID"],
    }
    _write_json(case_dir / "test_manager_sync_result.json", result)
    return result


def sync_test_results(case_id: str, evidence_root: Path | str = "evidence", dry_run: bool = True) -> dict:
    return sync_test_cases(case_id, evidence_root=evidence_root, dry_run=dry_run)


def sync_license_evidence(case_id: str, evidence_root: Path | str = "evidence", dry_run: bool = True) -> dict:
    return sync_test_cases(case_id, evidence_root=evidence_root, dry_run=dry_run)
