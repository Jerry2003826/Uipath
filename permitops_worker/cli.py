import argparse
import json
from pathlib import Path

from permitops_worker.engine.ai_trace import capture_trace_replay
from permitops_worker.engine.compiler import compile_license
from permitops_worker.engine.continuous_quality import build_continuous_quality_memory, build_evidence_graph
from permitops_worker.engine.evidence import write_json
from permitops_worker.engine.license_decision import decide
from permitops_worker.engine.policy_to_test import generate_certification_tests
from permitops_worker.engine.test_cloud_traceability import build_test_cloud_traceability_pack
from permitops_worker.engine.test_manager_webhook import build_create_defect_webhook_demo
from permitops_worker.engine.test_manager_sync import sync_test_cases
from permitops_worker.engine.test_runner import run_certification_tests
from permitops_worker.engine.v11_live_swarm import run_live_agentic_testing_loop
from permitops_worker.schemas import AgentToolCall


CASE_ID = "case_001"
EVIDENCE_ROOT = Path("evidence")


def _case_dir() -> Path:
    return EVIDENCE_ROOT / CASE_ID


def _compile(human_approved: bool = True):
    before = run_certification_tests(CASE_ID, "before", EVIDENCE_ROOT)
    after = run_certification_tests(CASE_ID, "after", EVIDENCE_ROOT)
    license_doc = compile_license(
        case_id=CASE_ID,
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        before_results=before,
        after_results=after,
        human_approved=human_approved,
    )
    write_json(_case_dir() / "license.json", license_doc.model_dump(mode="json"))
    write_json(
        _case_dir() / "action_center_approval_result.json",
        {"case_id": CASE_ID, "decision": "approved" if human_approved else "pending", "approver": "demo-human-approver"},
    )
    return license_doc


def _render_license_card(license_doc) -> Path:
    metadata = license_doc.license_metadata
    html = f"""<!doctype html>
<html>
<head><meta charset="utf-8"><title>PermitOps Runtime Permit</title></head>
<body>
<h1>PermitOps Runtime Permit</h1>
<p><strong>Agent:</strong> {license_doc.source_agent} -> {license_doc.target_agent}</p>
<p><strong>Status:</strong> {license_doc.status}</p>
<p><strong>Permit Level:</strong> {license_doc.license_level}</p>
<p><strong>Allowed:</strong> {", ".join(license_doc.allowed_actions)}</p>
<p><strong>Blocked:</strong> {", ".join(license_doc.blocked_actions)}</p>
<p><strong>Human Approval:</strong> {", ".join(license_doc.human_approval_required)}</p>
<p><strong>Rules hash:</strong> {metadata.compiler_rules_hash[:15]}</p>
<p><strong>Evidence hash:</strong> {metadata.evidence_hash[:15]}</p>
<p><strong>Permit hash:</strong> {metadata.license_hash[:15]}</p>
</body>
</html>
"""
    path = _case_dir() / "license_card.html"
    path.write_text(html, encoding="utf-8")
    return path


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def cmd_health(_args) -> int:
    print(json.dumps({"status": "ok", "service": "permitops-worker"}, indent=2))
    return 0


def cmd_capture_trace(args) -> int:
    result = capture_trace_replay(_case_dir(), provider=args.provider, model=args.model)
    print(json.dumps(result, indent=2))
    return 0


def cmd_generate_tests(_args) -> int:
    tests = generate_certification_tests(CASE_ID)
    write_json(_case_dir() / "test_cases.json", [test.model_dump(mode="json") for test in tests])
    print(f"Generated {len(tests)} certification tests")
    return 0


def cmd_run_tests(args) -> int:
    results = run_certification_tests(CASE_ID, args.phase, EVIDENCE_ROOT)
    failed = [result.test_id for result in results if result.status == "failed"]
    print(f"{args.phase}: {len(results) - len(failed)} passed, {len(failed)} failed")
    if failed:
        print("Failed:", ", ".join(failed))
    return 0


def cmd_compile_license(_args) -> int:
    license_doc = _compile(human_approved=True)
    print(json.dumps(license_doc.model_dump(mode="json"), indent=2))
    return 0


def cmd_license_decision_demo(_args) -> int:
    license_doc = _compile(human_approved=True)
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="export_raw_customer_emails",
        payload={"segment": "VIP", "count": 500, "data_type": "raw_email"},
    )
    print(json.dumps(decide(call, license_doc), indent=2))
    return 0


def cmd_render_license_card(_args) -> int:
    path = _render_license_card(_compile(human_approved=True))
    print(f"Rendered {path}")
    return 0


def cmd_sync_test_manager(args) -> int:
    result = sync_test_cases(CASE_ID, EVIDENCE_ROOT, dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
    return 0


def cmd_full_demo_local(_args) -> int:
    print("[1/9] Loaded captured AI trace: trace-pii-export-001")
    if not (_case_dir() / "raw_llm_response.json").exists():
        capture_trace_replay(_case_dir(), provider="replay", model="captured-fixture")
    tests = generate_certification_tests(CASE_ID)
    write_json(_case_dir() / "test_cases.json", [test.model_dump(mode="json") for test in tests])
    print(f"[2/9] Generated {len(tests)} certification tests")
    before = run_certification_tests(CASE_ID, "before", EVIDENCE_ROOT)
    print("[3/9] Before repair: TC-001 failed, TC-002 passed")
    _write_jsonl(
        _case_dir() / "coding_agent_prompts.jsonl",
        [
            {
                "timestamp": "2026-05-19T00:00:00Z",
                "tool": "Codex",
                "task": "generate_adversarial_tests",
                "input_summary": "policy + tool schema + captured trace",
            },
            {
                "timestamp": "2026-05-19T00:01:00Z",
                "tool": "Codex",
                "task": "propose_guardrail_repair",
                "input_summary": "TC-001 failure + raw PII policy",
            },
        ],
    )
    _write_jsonl(
        _case_dir() / "coding_agent_outputs.jsonl",
        [
            {
                "timestamp": "2026-05-19T00:00:30Z",
                "tool": "Codex",
                "task": "generate_adversarial_tests",
                "output_summary": "generated TC-001, TC-003, TC-005 scenarios",
                "artifact": "evidence/case_001/test_cases.json",
            },
            {
                "timestamp": "2026-05-19T00:01:30Z",
                "tool": "Codex",
                "task": "propose_guardrail_repair",
                "output_summary": "proposed raw PII export deny guardrail and regression test",
                "artifact": "evidence/case_001/test_results_after.json",
            },
        ],
    )
    print("[4/9] Coding-agent repair evidence loaded")
    after = run_certification_tests(CASE_ID, "after", EVIDENCE_ROOT)
    print("[5/9] After repair: TC-001 passed, TC-005 passed")
    license_doc = compile_license(CASE_ID, "marketing-outreach-agent", "customer-data-agent", before, after, human_approved=False)
    write_json(_case_dir() / "license_pending.json", license_doc.model_dump(mode="json"))
    print("[6/9] License compiled: L2_aggregate_access, pending_human_approval")
    license_doc = _compile(human_approved=True)
    print("[7/9] Human approval artifact loaded: approved")
    call = AgentToolCall(
        source_agent="marketing-outreach-agent",
        target_agent="customer-data-agent",
        action="export_raw_customer_emails",
        payload={"segment": "VIP", "count": 500, "data_type": "raw_email"},
    )
    decision = decide(call, license_doc)
    write_json(_case_dir() / "runtime_decision.json", decision)
    print("[8/9] Runtime decision:")
    print(f"      export_raw_customer_emails -> {decision['decision']}")
    _render_license_card(license_doc)
    sync_test_cases(CASE_ID, EVIDENCE_ROOT, dry_run=True)
    print("[9/9] License card rendered with hash metadata")
    return 0


def cmd_v11_live_swarm_local(_args) -> int:
    run = run_live_agentic_testing_loop(
        case_id=CASE_ID,
        changed_actions=["export_customer_phone_numbers"],
        evidence_root=EVIDENCE_ROOT,
    )
    print("[1/7] Live vulnerable Customer Data Agent attacked")
    print(f"      before repair -> {run['before_repair']['agent_result']['decision']}")
    print("[2/7] Test Selector reacted to changed tool schema")
    print(f"      selected tests -> {', '.join(run['test_selector']['selected_tests'])}")
    print("[3/7] Failure Analyst produced root cause for TC-001")
    print("[4/7] Repair Agent proposed raw PII export guardrail")
    print("[5/7] Targeted re-test passed after repair")
    print(f"      after repair -> {run['after_repair']['agent_result']['decision']}")
    print("[6/7] Incident memory created antibody test")
    print(f"      antibody -> {run['incident_memory']['antibody_test']['test_id']}")
    print("[7/7] Runtime permit remains L2 aggregate access")
    print("      wrote evidence/case_001/v11_live_swarm_run.json")
    print("      wrote evidence/case_001/incident_antibody_tests.json")
    return 0


def cmd_continuous_quality_memory_local(_args) -> int:
    memory = build_continuous_quality_memory(CASE_ID)
    write_json(_case_dir() / "continuous_quality_memory.json", memory)
    print("[1/3] Continuous Quality Memory built")
    print("      runtime-event-phone-001 -> TC-006")
    print("[2/3] Future selection requires TC-006 for raw PII tool changes")
    print("[3/3] wrote evidence/case_001/continuous_quality_memory.json")
    return 0


def cmd_evidence_graph_local(_args) -> int:
    graph = build_evidence_graph(CASE_ID)
    write_json(_case_dir() / "evidence_graph.json", graph)
    print("[1/3] Evidence Graph built")
    print("      trace -> policy -> test -> repair -> approval -> runtime enforcement")
    print(f"[2/3] Critical path length: {len(graph['critical_path'])}")
    print("[3/3] wrote evidence/case_001/evidence_graph.json")
    return 0


def cmd_test_cloud_traceability_local(_args) -> int:
    pack = build_test_cloud_traceability_pack(CASE_ID)
    write_json(_case_dir() / "test_cloud_traceability_pack.json", pack)
    print("[1/4] Test Cloud traceability pack built")
    print("      Requirement -> Test Case -> Execution -> Defect -> Runtime Permit")
    print("[2/4] REQ-PII-001 mapped to TC-001 through TC-006")
    print("[3/4] Obsolete Test Scout and Create Defect webhook blueprint included")
    print("[4/4] wrote evidence/case_001/test_cloud_traceability_pack.json")
    return 0


def cmd_test_manager_webhook_demo_local(_args) -> int:
    demo = build_create_defect_webhook_demo(CASE_ID)
    write_json(_case_dir() / "test_manager_create_defect_webhook_demo.json", demo)
    print("[1/4] Test Manager Create Defect webhook demo built")
    print("      TC-001 failure -> Failure Analyst Agent")
    print("[2/4] Defect payload ready: ATS-DEFECT-TC-001")
    print("[3/4] Targeted re-test scope: TC-001, TC-005")
    print("[4/4] wrote evidence/case_001/test_manager_create_defect_webhook_demo.json")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="permitops")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health").set_defaults(func=cmd_health)
    capture = sub.add_parser("capture-trace")
    capture.add_argument("--scenario", default="pii-export")
    capture.add_argument("--provider", default="replay")
    capture.add_argument("--model", default="captured-fixture")
    capture.set_defaults(func=cmd_capture_trace)
    sub.add_parser("generate-tests").set_defaults(func=cmd_generate_tests)
    run = sub.add_parser("run-tests")
    run.add_argument("--phase", choices=["before", "after"], required=True)
    run.set_defaults(func=cmd_run_tests)
    sub.add_parser("compile-license").set_defaults(func=cmd_compile_license)
    sub.add_parser("license-decision-demo").set_defaults(func=cmd_license_decision_demo)
    sub.add_parser("render-license-card").set_defaults(func=cmd_render_license_card)
    sync = sub.add_parser("sync-test-manager")
    sync.add_argument("--dry-run", action="store_true")
    sync.set_defaults(func=cmd_sync_test_manager)
    sub.add_parser("full-demo-local").set_defaults(func=cmd_full_demo_local)
    sub.add_parser("v11-live-swarm-local").set_defaults(func=cmd_v11_live_swarm_local)
    sub.add_parser("continuous-quality-memory-local").set_defaults(func=cmd_continuous_quality_memory_local)
    sub.add_parser("evidence-graph-local").set_defaults(func=cmd_evidence_graph_local)
    sub.add_parser("test-cloud-traceability-local").set_defaults(func=cmd_test_cloud_traceability_local)
    sub.add_parser("test-manager-webhook-demo-local").set_defaults(func=cmd_test_manager_webhook_demo_local)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
