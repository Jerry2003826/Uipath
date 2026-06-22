from pathlib import Path
from html import escape
import json
import re
from tempfile import gettempdir

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, Response

from permitops_worker.engine.ai_trace import capture_trace_replay
from permitops_worker.engine.compiler import compile_license
from permitops_worker.engine.continuous_quality import build_continuous_quality_memory, build_evidence_graph
from permitops_worker.engine.execution_timeline import build_before_after_execution_evidence
from permitops_worker.engine.judge_evidence import build_judge_evidence_matrix
from permitops_worker.engine.license_decision import decide
from permitops_worker.engine.policy_to_test import generate_certification_tests
from permitops_worker.engine.risk_scan import scan_risk
from permitops_worker.engine.test_cloud_traceability import build_test_cloud_traceability_pack
from permitops_worker.engine.test_manager_webhook import build_create_defect_webhook_demo, handle_create_defect_webhook
from permitops_worker.engine.test_runner import run_certification_tests
from permitops_worker.engine.v11_live_swarm import build_uipath_one_click_runbook, run_live_agentic_testing_loop
from permitops_worker.schemas import AgentToolCall, TestResult

app = FastAPI(title="PermitOps Worker", version="0.1.0")


API_EVIDENCE_ROOT = Path(gettempdir()) / "permitops_evidence"
CASE_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")
STATIC_EVIDENCE_ROOT = Path("evidence")


def _render_home_page() -> str:
    links = [
        ("/live-swarm-view", "Live swarm browser demo"),
        ("/run-live-swarm", "Live swarm JSON demo"),
        ("/test-cloud-traceability-view", "Test Cloud traceability view"),
        ("/before-after-execution-evidence-view", "Before / after repair evidence"),
        ("/judge-evidence-matrix-view", "Judge evidence matrix"),
        ("/continuous-quality-memory-view", "Continuous quality memory"),
        ("/evidence-graph-view", "Evidence graph"),
        ("/uipath-native-agent-pack", "UiPath-native agent pack JSON"),
        ("/health", "Health check"),
    ]
    link_items = "\n".join(
        f'<a class="link" href="{escape(href)}"><strong>{escape(label)}</strong><span>{escape(href)}</span></a>'
        for href, label in links
    )
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Agentic Test Swarm</title>
  <style>
    :root {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #13202e; background: #f4f7fb; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; }}
    main {{ max-width: 980px; margin: 0 auto; padding: 46px 24px; }}
    .kicker {{ color: #2457d6; font-weight: 800; font-size: 13px; letter-spacing: .08em; text-transform: uppercase; }}
    h1 {{ margin: 10px 0 12px; font-size: 42px; line-height: 1.05; letter-spacing: 0; }}
    p {{ color: #4b5f76; font-size: 16px; line-height: 1.55; max-width: 830px; }}
    .grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-top: 28px; }}
    .link {{ display: block; min-height: 118px; padding: 16px; border: 1px solid #d8e1ec; border-radius: 8px; background: #fff; color: #13202e; text-decoration: none; box-shadow: 0 6px 18px rgba(15, 23, 42, .05); }}
    .link strong {{ display: block; font-size: 15px; margin-bottom: 12px; }}
    .link span {{ display: block; color: #2463eb; font: 12px ui-monospace, SFMono-Regular, Menlo, monospace; overflow-wrap: anywhere; }}
    .note {{ margin-top: 24px; padding: 14px 16px; border: 1px solid #fed7aa; background: #fff7ed; color: #9a3412; border-radius: 8px; }}
    @media (max-width: 820px) {{ .grid {{ grid-template-columns: 1fr; }} h1 {{ font-size: 34px; }} }}
  </style>
</head>
<body>
  <main>
    <div class="kicker">UiPath AgentHack · Test Cloud Track</div>
    <h1>Agentic Test Swarm</h1>
    <p>UiPath Test Cloud agents that attack, repair, re-test, and certify enterprise AI workflows before they can touch production tools.</p>
    <p>This homepage exists so judges do not land on a raw FastAPI 404. Use the links below for the live demo, Test Cloud traceability, before/after repair evidence, and UiPath-native agent pack.</p>
    <section class="grid">{link_items}</section>
    <div class="note">If a JSON endpoint returns <code>{{"detail":"Not Found"}}</code>, that URL is not a registered route. Start here or use <code>/live-swarm-view</code>.</div>
  </main>
</body>
</html>"""


def _case_id_from_payload(payload: dict) -> str:
    case_id = payload.get("case_id", "case_001")
    if not isinstance(case_id, str) or not CASE_ID_PATTERN.fullmatch(case_id):
        raise HTTPException(status_code=400, detail="case_id must contain only letters, numbers, hyphen, or underscore")
    return case_id


@app.get("/", response_class=HTMLResponse)
def home_page() -> HTMLResponse:
    return HTMLResponse(_render_home_page())


def _render_live_swarm_view(run: dict) -> str:
    before = run["before_repair"]["agent_result"]
    after = run["after_repair"]["agent_result"]
    selector = run["test_selector"]
    failure = run["failure_analysis"]
    repair = run["repair_candidate"]
    antibody = run["incident_memory"]["antibody_test"]
    control_plane = run["uipath_control_plane"]
    runbook = run["uipath_one_click_runbook"]
    permit = run["permit_output"]
    selected_tests = " + ".join(selector["selected_tests"])
    coverage_tags = "".join(f"<span class='tag'>{escape(tag)}</span>" for tag in selector["inputs"]["coverage_tags"])
    platform_cards = "".join(
        (
            "<div class='platform-card'>"
            f"<strong>{escape(artifact['component'])}</strong>"
            f"<p>{escape(artifact['platform_role'])}</p>"
            f"<span>{escape(artifact['visible_artifact'])}</span>"
            f"<em>{escape(artifact['why_uipath'])}</em>"
            "</div>"
        )
        for artifact in control_plane["artifacts"]
    )
    action_cards = "".join(
        (
            "<div class='action-card'>"
            f"<strong>{escape(action['no_code_action'])}</strong>"
            f"<p>{escape(action['uipath_surface'])}</p>"
            f"<span>{escape(action['effect'])}</span>"
            "</div>"
        )
        for action in control_plane["operator_actions"]
    )
    sequence_cards = "".join(
        (
            "<div class='runbook-step'>"
            f"<strong>{step['step']}. {escape(step['uipath_surface'])}</strong>"
            f"<p>{escape(step['visible_action'])}</p>"
            f"<span>{escape(step['platform_evidence'])}</span>"
            "</div>"
        )
        for step in runbook["sequence"]
    )
    raw_json = json.dumps(run, indent=2)

    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Agentic Test Swarm - Live Vercel Simulation</title>
  <style>
    :root {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #16202a; background: #eef2f6; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: #eef2f6; }}
    .page {{ max-width: 1220px; margin: 0 auto; padding: 34px; }}
    .header {{ display: flex; align-items: flex-start; justify-content: space-between; gap: 24px; margin-bottom: 22px; }}
    .kicker {{ font-size: 13px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: #2463eb; margin-bottom: 8px; }}
    h1 {{ margin: 0; font-size: 38px; line-height: 1.05; letter-spacing: 0; color: #111827; }}
    .sub {{ margin: 10px 0 0; color: #4b5563; font-size: 16px; line-height: 1.45; max-width: 850px; }}
    .endpoint {{ background: #111827; color: #d1fae5; padding: 14px 16px; border-radius: 8px; font: 13px ui-monospace, SFMono-Regular, Menlo, monospace; min-width: 370px; box-shadow: 0 10px 30px rgba(15,23,42,.12); }}
    .banner {{ padding: 12px 14px; border: 1px solid #bfdbfe; background: #eff6ff; color: #1e3a8a; border-radius: 8px; font-size: 14px; margin: 16px 0 6px; }}
    .demo-warning {{ padding: 12px 14px; border: 1px solid #fed7aa; background: #fff7ed; color: #9a3412; border-radius: 8px; font-size: 14px; margin: 10px 0 6px; }}
    .grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin: 18px 0; }}
    .card {{ background: #fff; border: 1px solid #d9e0ea; border-radius: 8px; padding: 18px; box-shadow: 0 6px 18px rgba(15,23,42,.06); }}
    .card h2 {{ font-size: 15px; margin: 0 0 12px; color: #111827; }}
    .value {{ font-size: 22px; font-weight: 800; margin: 0; color: #111827; }}
    .muted {{ font-size: 13px; color: #64748b; line-height: 1.45; margin-top: 8px; }}
    .danger {{ color: #b91c1c; }}
    .ok {{ color: #047857; }}
    .amber {{ color: #b45309; }}
    .blue {{ color: #1d4ed8; }}
    .wide {{ grid-column: span 2; }}
    .full {{ grid-column: 1 / -1; }}
    .flow {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; align-items: stretch; margin-top: 8px; }}
    .step {{ border: 1px solid #dbe3ee; background: #f8fafc; border-radius: 8px; padding: 13px; min-height: 114px; }}
    .step strong {{ display: block; font-size: 14px; color: #0f172a; margin-bottom: 8px; }}
    .step p {{ margin: 0; color: #475569; font-size: 13px; line-height: 1.35; }}
    .tagrow {{ display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px; }}
    .tag {{ border: 1px solid #cbd5e1; border-radius: 999px; padding: 5px 9px; background: #fff; font-size: 12px; color: #334155; }}
    .pill {{ display: inline-block; padding: 5px 9px; border-radius: 999px; background: #e0f2fe; color: #075985; font-weight: 700; font-size: 12px; margin-right: 6px; }}
    .license {{ display: grid; grid-template-columns: 1.2fr 1fr; gap: 14px; }}
    .list {{ margin: 0; padding-left: 18px; color: #334155; font-size: 14px; line-height: 1.55; }}
    .code {{ background: #101827; color: #e5e7eb; border-radius: 8px; padding: 18px; overflow: auto; font: 12px ui-monospace, SFMono-Regular, Menlo, monospace; max-height: 420px; line-height: 1.45; }}
    .platform {{ background: #0f172a; color: #e5e7eb; border-color: #1e293b; }}
    .platform h2 {{ color: #f8fafc; font-size: 20px; }}
    .platform .muted {{ color: #b6c4d7; }}
    .platform-grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 16px; }}
    .platform-card {{ border: 1px solid #334155; background: #111c2f; border-radius: 8px; padding: 13px; min-height: 170px; }}
    .platform-card strong, .action-card strong {{ display: block; color: #f8fafc; font-size: 14px; margin-bottom: 8px; }}
    .platform-card p, .action-card p {{ margin: 0 0 8px; color: #cbd5e1; font-size: 13px; line-height: 1.35; }}
    .platform-card span, .action-card span {{ display: block; color: #93c5fd; font-size: 12px; line-height: 1.35; }}
    .platform-card em {{ display: block; color: #a7f3d0; font-style: normal; font-size: 12px; line-height: 1.35; margin-top: 10px; }}
    .operator-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 12px; }}
    .action-card {{ border: 1px solid #315176; background: #172554; border-radius: 8px; padding: 13px; }}
    .runbook {{ background: #fefce8; border-color: #fde68a; }}
    .runbook-grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 14px; }}
    .runbook-step {{ border: 1px solid #fde68a; background: #fffdf2; border-radius: 8px; padding: 13px; min-height: 150px; }}
    .runbook-step strong {{ display: block; color: #713f12; font-size: 13px; margin-bottom: 8px; }}
    .runbook-step p {{ margin: 0 0 8px; color: #422006; font-size: 13px; line-height: 1.35; }}
    .runbook-step span {{ display: block; color: #854d0e; font-size: 12px; line-height: 1.35; }}
  </style>
</head>
<body>
  <main class="page">
    <div class="header">
      <div>
        <div class="kicker">Live Public Endpoint Simulation</div>
        <h1>Agentic Test Swarm</h1>
        <p class="sub">UiPath-orchestrated testing agents attack an AI workflow, analyze the failure, propose a repair, select targeted re-tests, create incident-memory regression coverage, and output a runtime permit.</p>
      </div>
      <div class="endpoint">POST /run-live-swarm<br>Status: 200 OK<br>Case: {escape(run["case_id"])}<br>Version: {escape(run["version"])}</div>
    </div>
    <div class="banner">This normal HTTPS page renders the same V11 live swarm result that the POST endpoint returns as JSON.</div>
    <div class="demo-warning"><strong>DEMO_ONLY:</strong> public worker output uses synthetic data and contains no production UiPath credentials or real customer PII. UiPath tenant evidence is separated in the Judge Evidence Matrix.</div>
    <section class="grid">
      <div class="card"><h2>Before Repair</h2><p class="value danger">{escape(before["decision"])}</p><div class="muted">The vulnerable agent accepts the executive override and returns raw PII.</div></div>
      <div class="card"><h2>Failure Analyst</h2><p class="value danger">{escape(failure["failed_test"])}</p><div class="muted">{escape(failure["root_cause"])}</div></div>
      <div class="card"><h2>After Repair</h2><p class="value ok">{escape(after["decision"])}</p><div class="muted">Guardrail: {escape(after["guardrail"])}</div></div>
      <div class="card"><h2>Incident Memory</h2><p class="value blue">{escape(antibody["test_id"])}</p><div class="muted">{escape(antibody["reason"])}</div></div>
      <div class="card wide"><h2>Test Selector Agent</h2><p class="value">{escape(selected_tests)}</p><div class="muted">{escape(selector["selection_reason"])}</div><div class="tagrow">{coverage_tags}</div></div>
      <div class="card wide"><h2>Repair Agent Candidate</h2><p><span class="pill">{escape(repair["agent"])}</span><span class="pill">{escape(repair["guardrail"])}</span></p><div class="muted">Trusted only after Test Cloud evidence, Action Center approval, and deterministic Quality Governor.</div></div>
      <div class="card full platform">
        <h2>UiPath No-Code Control Plane</h2>
        <div class="muted">{escape(control_plane["claim"])} The Python worker only computes deterministic evidence; UiPath owns the visible workflow, human gate, test evidence, and runtime enforcement.</div>
        <div class="platform-grid">{platform_cards}</div>
        <h2 style="margin-top: 18px;">No-code operator actions</h2>
        <div class="operator-grid">{action_cards}</div>
      </div>
      <div class="card full runbook">
        <h2>One-Click UiPath Runbook</h2>
        <p class="muted">GET <code>/uipath-one-click-runbook</code> returns the platform runbook that a Studio Web / API Workflow trigger can use. The run starts in UiPath, records Test Cloud evidence including TC-006, waits for Action Center, and then enforces the permit through API Workflow.</p>
        <div class="tagrow"><span class="tag">{escape(runbook["trigger"]["operator_action"])}</span><span class="tag">{escape(runbook["test_cloud_delta"]["new_or_highlighted_test"])}</span><span class="tag">{escape(runbook["action_center"]["task_id"])}</span><span class="tag">{escape(runbook["runtime_enforcement"]["expected_decision"])}</span></div>
        <div class="runbook-grid">{sequence_cards}</div>
      </div>
      <div class="card full"><h2>Agentic Testing Loop</h2><div class="flow"><div class="step"><strong>1. Red-Team Attack</strong><p>Marketing Agent requests raw VIP customer emails using executive override language.</p></div><div class="step"><strong>2. Test Selection</strong><p>Risk, coverage, change impact, and recent failures select critical tests.</p></div><div class="step"><strong>3. Failure Analysis</strong><p>TC-001 root cause: raw PII exfiltration from AI-infused workflow.</p></div><div class="step"><strong>4. Repair + Re-test</strong><p>Guardrail patch blocks raw PII export and targeted re-test passes.</p></div><div class="step"><strong>5. Permit + Enforcement</strong><p>Runtime permit allows aggregate insight and blocks raw PII exports.</p></div></div></div>
      <div class="card full license"><div><h2>PermitOps Runtime Permit</h2><p class="value amber">{escape(permit["license_level"])}</p><div class="muted">License hash: {escape(permit["license_hash"][:19])}...</div></div><div><h2>Runtime Permissions</h2><ul class="list"><li>Allowed: {escape(", ".join(permit["allowed_actions"]))}</li><li>Blocked: {escape(", ".join(permit["blocked_actions"]))}</li><li>Runtime raw PII export result: {escape(after["decision"])}</li></ul></div></div>
      <div class="card full"><h2>Raw JSON Response</h2><pre class="code">{escape(raw_json)}</pre></div>
    </section>
  </main>
</body>
</html>"""


def _render_evidence_view(title: str, claim: str, items: list[dict], raw: dict) -> str:
    cards = "".join(
        (
            "<div class='card'>"
            f"<strong>{escape(item['label'])}</strong>"
            f"<span>{escape(item['owner'])}</span>"
            f"<p>{escape(item['evidence'])}</p>"
            "</div>"
        )
        for item in items
    )
    raw_json = json.dumps(raw, indent=2)
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{escape(title)}</title>
  <style>
    :root {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #142033; background: #f5f7fb; }}
    body {{ margin: 0; }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 34px; }}
    h1 {{ margin: 0; font-size: 36px; letter-spacing: 0; }}
    .claim {{ color: #475569; line-height: 1.45; max-width: 860px; }}
    .grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin: 22px 0; }}
    .card {{ background: #fff; border: 1px solid #dbe3ee; border-radius: 8px; padding: 16px; min-height: 132px; box-shadow: 0 6px 18px rgba(15,23,42,.06); }}
    .card strong {{ display: block; color: #0f172a; font-size: 15px; margin-bottom: 8px; }}
    .card span {{ display: inline-block; color: #1d4ed8; background: #eff6ff; border-radius: 999px; padding: 4px 8px; font-size: 12px; font-weight: 700; margin-bottom: 10px; }}
    .card p {{ margin: 0; color: #475569; line-height: 1.4; font-size: 13px; }}
    pre {{ background: #101827; color: #e5e7eb; border-radius: 8px; padding: 18px; overflow: auto; font: 12px ui-monospace, SFMono-Regular, Menlo, monospace; line-height: 1.45; }}
  </style>
</head>
<body>
  <main>
    <h1>{escape(title)}</h1>
    <p class="claim">{escape(claim)}</p>
    <section class="grid">{cards}</section>
    <pre>{escape(raw_json)}</pre>
  </main>
</body>
</html>"""


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "permitops-worker"}


@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> Response:
    return Response(status_code=204)


@app.post("/scan-risk")
def scan_risk_endpoint(call: AgentToolCall) -> dict:
    return scan_risk(call)


@app.post("/generate-test-scenarios")
def generate_test_scenarios(payload: dict) -> dict:
    case_id = _case_id_from_payload(payload)
    tests = generate_certification_tests(case_id)
    return {"case_id": case_id, "test_count": len(tests), "tests": [test.model_dump(mode="json") for test in tests]}


@app.post("/expected-oracle")
def expected_oracle_endpoint(call: AgentToolCall) -> dict:
    from permitops_worker.engine.expected_oracle import expected_decision_for_tool_call

    return expected_decision_for_tool_call(call)


@app.post("/run-certification-tests")
def run_certification_tests_endpoint(payload: dict) -> dict:
    case_id = _case_id_from_payload(payload)
    phase = payload.get("phase", "after")
    if phase not in {"before", "after"}:
        raise HTTPException(status_code=400, detail="phase must be before or after")
    results = run_certification_tests(case_id=case_id, phase=phase, evidence_root=API_EVIDENCE_ROOT)
    return {"case_id": case_id, "phase": phase, "results": [result.model_dump(mode="json") for result in results]}


@app.post("/compile-license")
def compile_license_endpoint(payload: dict) -> dict:
    case_id = _case_id_from_payload(payload)
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
    case_id = _case_id_from_payload(payload)
    call = AgentToolCall(
        source_agent=payload["source_agent"],
        target_agent=payload["target_agent"],
        action=payload["action"],
        payload=payload.get("payload", {}),
    )
    before = run_certification_tests(case_id, "before", evidence_root=API_EVIDENCE_ROOT)
    after = run_certification_tests(case_id, "after", evidence_root=API_EVIDENCE_ROOT)
    license_doc = compile_license(
        case_id=case_id,
        source_agent=call.source_agent,
        target_agent=call.target_agent,
        before_results=before,
        after_results=after,
        human_approved=True,
    )
    return decide(call, license_doc)


@app.post("/capture-trace")
def capture_trace_endpoint(payload: dict) -> dict:
    case_id = _case_id_from_payload(payload)
    case_path = API_EVIDENCE_ROOT / case_id
    return capture_trace_replay(case_path, provider=payload.get("provider", "replay"), model=payload.get("model", "captured-fixture"))


@app.post("/run-live-swarm")
def run_live_swarm_endpoint(payload: dict) -> dict:
    case_id = _case_id_from_payload(payload)
    changed_actions = payload.get("changed_actions", [])
    if not isinstance(changed_actions, list) or not all(isinstance(action, str) for action in changed_actions):
        raise HTTPException(status_code=400, detail="changed_actions must be a list of strings")
    return run_live_agentic_testing_loop(case_id=case_id, changed_actions=changed_actions, evidence_root=API_EVIDENCE_ROOT)


@app.get("/run-live-swarm")
def run_live_swarm_get(case_id: str = "case_001", changed_actions: str = "export_customer_phone_numbers") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    actions = [action.strip() for action in changed_actions.split(",") if action.strip()]
    return run_live_agentic_testing_loop(
        case_id=validated_case_id,
        changed_actions=actions,
        evidence_root=API_EVIDENCE_ROOT,
    )


@app.get("/uipath-one-click-runbook")
def uipath_one_click_runbook(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    runbook = build_uipath_one_click_runbook(validated_case_id)
    case_dir = API_EVIDENCE_ROOT / validated_case_id
    case_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / "uipath_one_click_runbook.json").write_text(json.dumps(runbook, indent=2), encoding="utf-8")
    return runbook


@app.get("/uipath-native-agent-pack")
def uipath_native_agent_pack(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    pack_path = STATIC_EVIDENCE_ROOT / validated_case_id / "uipath_native_agent_pack.json"
    if not pack_path.exists():
        raise HTTPException(status_code=404, detail=f"UiPath-native agent pack not found for {validated_case_id}")
    return json.loads(pack_path.read_text(encoding="utf-8"))


@app.get("/continuous-quality-memory")
def continuous_quality_memory(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    return build_continuous_quality_memory(validated_case_id)


@app.get("/continuous-quality-memory-view", response_class=HTMLResponse)
def continuous_quality_memory_view(case_id: str = "case_001") -> HTMLResponse:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    memory = build_continuous_quality_memory(validated_case_id)
    items = [
        {"label": step["stage"], "owner": step["uipath_surface"], "evidence": step["description"]}
        for step in memory["lifecycle"]
    ]
    return HTMLResponse(_render_evidence_view(memory["system_name"], memory["claim"], items, memory))


@app.get("/evidence-graph")
def evidence_graph(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    return build_evidence_graph(validated_case_id)


@app.get("/evidence-graph-view", response_class=HTMLResponse)
def evidence_graph_view(case_id: str = "case_001") -> HTMLResponse:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    graph = build_evidence_graph(validated_case_id)
    return HTMLResponse(_render_evidence_view(graph["graph_name"], graph["claim"], graph["nodes"], graph))


@app.get("/test-cloud-traceability")
def test_cloud_traceability(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    return build_test_cloud_traceability_pack(validated_case_id)


@app.get("/test-cloud-traceability-view", response_class=HTMLResponse)
def test_cloud_traceability_view(case_id: str = "case_001") -> HTMLResponse:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    pack = build_test_cloud_traceability_pack(validated_case_id)
    items = [
        {
            "label": f"{pack['requirement']['requirement_id']} / {pack['requirement'].get('uipath_key', 'external')}",
            "owner": pack["requirement"]["uipath_surface"],
            "evidence": pack["requirement"]["description"],
        },
        *[
            {
                "label": case["test_id"],
                "owner": case["test_manager_key"],
                "evidence": f"{case['name']} -> expected {case['expected']}",
            }
            for case in pack["test_cases"]
        ],
        {
            "label": pack["execution"]["name"],
            "owner": pack["execution"]["uipath_surface"],
            "evidence": pack["execution"]["result_summary"],
        },
        {
            "label": "Create Defect webhook",
            "owner": pack["defect_webhook_blueprint"]["uipath_surface"],
            "evidence": pack["defect_webhook_blueprint"]["result"],
        },
        {
            "label": pack["obsolete_test_scout"]["agent_name"],
            "owner": pack["obsolete_test_scout"]["uipath_surface"],
            "evidence": pack["obsolete_test_scout"]["future_schema_change_rule"],
        },
        {
            "label": "Testing Process Governance",
            "owner": pack["testing_process_governance"]["uipath_surface"],
            "evidence": pack["testing_process_governance"]["relationship_to_action_center"],
        },
        {
            "label": "Runtime Permit",
            "owner": pack["runtime_permit"]["uipath_surface"],
            "evidence": f"API Workflow runtime decision: {pack['runtime_permit']['decision']}",
        },
    ]
    return HTMLResponse(_render_evidence_view(pack["system_name"], pack["claim"], items, pack))


@app.post("/test-manager-webhook/create-defect")
def test_manager_create_defect_webhook(payload: dict, case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    return handle_create_defect_webhook(validated_case_id, payload)


@app.get("/test-manager-webhook-demo")
def test_manager_webhook_demo(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    return build_create_defect_webhook_demo(validated_case_id)


@app.get("/test-manager-webhook-demo-view", response_class=HTMLResponse)
def test_manager_webhook_demo_view(case_id: str = "case_001") -> HTMLResponse:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    demo = build_create_defect_webhook_demo(validated_case_id)
    response = demo["webhook_response"]
    items = [
        {
            "label": "Incoming Test Manager payload",
            "owner": "Test Manager Webhooks",
            "evidence": (
                f"{demo['incoming_test_manager_payload']['logicalTestId']} "
                f"({demo['incoming_test_manager_payload']['testCaseId']}) from execution "
                f"{demo['incoming_test_manager_payload']['testExecutionId']}"
            ),
        },
        {
            "label": response["failure_analysis"]["agent"],
            "owner": "UiPath-native / worker-backed analysis",
            "evidence": response["failure_analysis"]["root_cause"],
        },
        {
            "label": response["defect_payload"]["external_id"],
            "owner": "Create Defect webhook response",
            "evidence": response["defect_payload"]["summary"],
        },
        {
            "label": "Targeted re-test",
            "owner": "Test Cloud / Test Manager",
            "evidence": ", ".join(response["defect_payload"]["tests_to_rerun"]),
        },
        {
            "label": "Traceability",
            "owner": "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit",
            "evidence": response["traceability"]["defect_to_repair"],
        },
    ]
    return HTMLResponse(_render_evidence_view(demo["demo_name"], demo["judge_line"], items, demo))


@app.get("/judge-evidence-matrix")
def judge_evidence_matrix(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    return build_judge_evidence_matrix(validated_case_id)


@app.get("/judge-evidence-matrix-view", response_class=HTMLResponse)
def judge_evidence_matrix_view(case_id: str = "case_001") -> HTMLResponse:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    matrix = build_judge_evidence_matrix(validated_case_id)
    items = [
        {
            "label": row["claim"],
            "owner": f"{row['status']} - {row['uipath_surface']}",
            "evidence": f"{row['evidence']} Boundary: {row['boundary']}",
        }
        for row in matrix["rows"]
    ]
    return HTMLResponse(_render_evidence_view(matrix["system_name"], matrix["claim"], items, matrix))


@app.get("/before-after-execution-evidence")
def before_after_execution_evidence(case_id: str = "case_001") -> dict:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    return build_before_after_execution_evidence(validated_case_id)


@app.get("/before-after-execution-evidence-view", response_class=HTMLResponse)
def before_after_execution_evidence_view(case_id: str = "case_001") -> HTMLResponse:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    evidence = build_before_after_execution_evidence(validated_case_id)
    items = [
        {
            "label": run["name"],
            "owner": f"{run['status']} - {run['uipath_surface']}",
            "evidence": f"{run['result_summary']} Purpose: {run['purpose']}",
        }
        for run in evidence["runs"]
    ]
    return HTMLResponse(_render_evidence_view(evidence["system_name"], evidence["claim"], items, evidence))


@app.get("/live-swarm-view", response_class=HTMLResponse)
def live_swarm_view(case_id: str = "case_001", changed_actions: str = "export_customer_phone_numbers") -> HTMLResponse:
    validated_case_id = _case_id_from_payload({"case_id": case_id})
    action_list = [action.strip() for action in changed_actions.split(",") if action.strip()]
    run = run_live_agentic_testing_loop(
        case_id=validated_case_id,
        changed_actions=action_list,
        evidence_root=API_EVIDENCE_ROOT,
    )
    return HTMLResponse(_render_live_swarm_view(run))
