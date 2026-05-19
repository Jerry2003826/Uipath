from pathlib import Path
from tempfile import gettempdir

from fastapi import FastAPI, HTTPException

from permitops_worker.engine.ai_trace import capture_trace_replay
from permitops_worker.engine.compiler import compile_license
from permitops_worker.engine.license_decision import decide
from permitops_worker.engine.policy_to_test import generate_certification_tests
from permitops_worker.engine.risk_scan import scan_risk
from permitops_worker.engine.test_runner import run_certification_tests
from permitops_worker.schemas import AgentToolCall, TestResult

app = FastAPI(title="PermitOps Worker", version="0.1.0")


API_EVIDENCE_ROOT = Path(gettempdir()) / "permitops_evidence"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "permitops-worker"}


@app.post("/scan-risk")
def scan_risk_endpoint(call: AgentToolCall) -> dict:
    return scan_risk(call)


@app.post("/generate-test-scenarios")
def generate_test_scenarios(payload: dict) -> dict:
    case_id = payload.get("case_id", "case_001")
    tests = generate_certification_tests(case_id)
    return {"case_id": case_id, "test_count": len(tests), "tests": [test.model_dump(mode="json") for test in tests]}


@app.post("/expected-oracle")
def expected_oracle_endpoint(call: AgentToolCall) -> dict:
    from permitops_worker.engine.expected_oracle import expected_decision_for_tool_call

    return expected_decision_for_tool_call(call)


@app.post("/run-certification-tests")
def run_certification_tests_endpoint(payload: dict) -> dict:
    case_id = payload.get("case_id", "case_001")
    phase = payload.get("phase", "after")
    if phase not in {"before", "after"}:
        raise HTTPException(status_code=400, detail="phase must be before or after")
    results = run_certification_tests(case_id=case_id, phase=phase, evidence_root=API_EVIDENCE_ROOT)
    return {"case_id": case_id, "phase": phase, "results": [result.model_dump(mode="json") for result in results]}


@app.post("/compile-license")
def compile_license_endpoint(payload: dict) -> dict:
    case_id = payload.get("case_id", "case_001")
    source_agent = payload.get("source_agent", "marketing-outreach-agent")
    target_agent = payload.get("target_agent", "customer-data-agent")
    before = [TestResult(**item) for item in payload.get("before_results", [])] or run_certification_tests(
        case_id, "before", evidence_root=API_EVIDENCE_ROOT
    )
    after = [TestResult(**item) for item in payload.get("after_results", [])] or run_certification_tests(
        case_id, "after", evidence_root=API_EVIDENCE_ROOT
    )
    license_doc = compile_license(
        case_id=case_id,
        source_agent=source_agent,
        target_agent=target_agent,
        before_results=before,
        after_results=after,
        human_approved=bool(payload.get("human_approved", False)),
    )
    return license_doc.model_dump(mode="json")


@app.post("/license-decision")
def license_decision_endpoint(payload: dict) -> dict:
    call = AgentToolCall(
        source_agent=payload["source_agent"],
        target_agent=payload["target_agent"],
        action=payload["action"],
        payload=payload.get("payload", {}),
    )
    before = run_certification_tests(payload.get("case_id", "case_001"), "before", evidence_root=API_EVIDENCE_ROOT)
    after = run_certification_tests(payload.get("case_id", "case_001"), "after", evidence_root=API_EVIDENCE_ROOT)
    license_doc = compile_license(
        case_id=payload.get("case_id", "case_001"),
        source_agent=call.source_agent,
        target_agent=call.target_agent,
        before_results=before,
        after_results=after,
        human_approved=True,
    )
    return decide(call, license_doc)


@app.post("/capture-trace")
def capture_trace_endpoint(payload: dict) -> dict:
    case_id = payload.get("case_id", "case_001")
    case_path = API_EVIDENCE_ROOT / case_id
    return capture_trace_replay(case_path, provider=payload.get("provider", "replay"), model=payload.get("model", "captured-fixture"))
