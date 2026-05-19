import pytest

from permitops_worker.engine.test_manager_sync import (
    MissingUiPathConfigurationError,
    sync_test_cases,
)


def test_dry_run_writes_test_manager_payload(tmp_path):
    result = sync_test_cases(case_id="case_001", evidence_root=tmp_path, dry_run=True)

    assert result["mode"] == "dry_run"
    assert result["test_case_count"] >= 3
    assert (tmp_path / "case_001" / "test_manager_sync_payload.json").exists()


def test_real_mode_without_credentials_raises_clear_configuration_error(tmp_path, monkeypatch):
    for key in [
        "UIPATH_TEST_MANAGER_BASE_URL",
        "UIPATH_ORG_NAME",
        "UIPATH_TENANT_NAME",
        "UIPATH_ACCESS_TOKEN",
        "UIPATH_TEST_PROJECT_ID",
    ]:
        monkeypatch.delenv(key, raising=False)

    with pytest.raises(MissingUiPathConfigurationError, match="UIPATH_ACCESS_TOKEN"):
        sync_test_cases(case_id="case_001", evidence_root=tmp_path, dry_run=False)
