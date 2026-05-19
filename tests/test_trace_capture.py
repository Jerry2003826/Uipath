from pathlib import Path

from permitops_worker.engine.ai_trace import capture_trace_replay


def test_trace_capture_writes_required_audit_files(tmp_path):
    case_dir = tmp_path / "case_001"

    result = capture_trace_replay(case_dir=case_dir, provider="replay", model="captured-fixture")

    assert result["trace_id"] == "trace-pii-export-001"
    assert result["mode"] == "captured_ai_trace_replay"
    assert (case_dir / "raw_llm_response.json").exists()
    assert (case_dir / "normalized_ai_trace.json").exists()
    assert (case_dir / "trace_metadata.json").exists()


def test_normalized_trace_contains_attempted_tool_call(tmp_path):
    case_dir = tmp_path / "case_001"

    result = capture_trace_replay(case_dir=case_dir, provider="replay", model="captured-fixture")

    assert result["attempted_tool_call"]["action"] == "export_raw_customer_emails"
    assert result["attempted_tool_call"]["data_type"] == "raw_email"
