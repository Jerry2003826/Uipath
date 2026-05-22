from pathlib import Path
from zipfile import ZipFile


README = Path("README.md")
DECK_MD = Path("docs/presentation_deck.md")
DECK_PPTX = Path("assets/agentic_test_swarm_deck.pptx")
OFFICIAL_ALIGNMENT = Path("docs/official_track3_alignment.md")
JUDGE_SCORECARD = Path("docs/judge_scorecard.md")
JUDGE_TASTE_RESEARCH = Path("docs/judge_taste_research_2026-05-23.md")
UIPATH_NATIVE_GAP_RESEARCH = Path("docs/uipath_native_depth_gap_research_2026-05-23.md")
TEST_CLOUD_NATIVE_GAP_RESEARCH = Path("docs/test_cloud_native_gap_research_2026-05-23.md")
TC006_RUNBOOK = Path("docs/tc006_test_manager_runbook.md")
VIDEO_SHOT_LIST = Path("docs/final_video_shot_list.md")
DEVPOST_PACKAGE = Path("docs/devpost_submission_package.md")
PRODUCT_FEEDBACK_SUBMISSION = Path("docs/product_feedback_submission.md")
CODING_AGENTS_BONUS = Path("docs/coding_agents_bonus_pack.md")
BONUS_EVIDENCE_PACK = Path("docs/bonus_evidence_pack.md")
RESEARCH_WORKBENCH = Path("docs/research_workbench.md")
RESEARCH_LOG = Path("docs/research_log.md")
AGENTHACK_AWARD_GAP_RESEARCH = Path(
    "docs/research_findings_2026-05-21_agenthack_award_gap.md"
)
TEST_MANAGER_PLAN_C = Path("uipath/test_cloud/test_manager_plan_c.md")
SUBMISSION_READINESS = Path("docs/submission_readiness.md")
PLATFORM_SPIKE_STATUS = Path("docs/platform_spike_status.md")
TC006_PLACEHOLDER = Path("uipath/test_cloud/evidence_placeholders/TC-006_incident_memory_blocks_phone_number_export.md")
TC006_CASE_SCREENSHOT = Path("assets/test_manager_tc006_case_created.png")
TC006_ASSIGNMENT_SCREENSHOT = Path("assets/test_manager_tc006_added_to_test_set.png")
TC006_CASE_EVIDENCE = Path("evidence/case_001/test_manager_tc006_case_created.txt")
TC006_ASSIGNMENT_EVIDENCE = Path("evidence/case_001/test_manager_tc006_test_set_assignment.txt")
TEST_MANAGER_6_CASE_SCREENSHOT = Path("assets/test_manager_6_passed_completed.png")
TEST_MANAGER_6_CASE_EVIDENCE = Path("evidence/case_001/test_manager_6_passed_completed.txt")
UIPATH_FAILURE_ANALYST_DRAFT_SCREENSHOT = Path("assets/uipath_failure_analyst_agent_draft.png")
UIPATH_FAILURE_ANALYST_MODEL_SCREENSHOT = Path("assets/uipath_failure_analyst_agent_model_selected.png")
UIPATH_FAILURE_ANALYST_NO_ISSUES_SCREENSHOT = Path(
    "assets/uipath_failure_analyst_agent_no_issues.png"
)
UIPATH_FAILURE_ANALYST_DEBUG_SCREENSHOT = Path(
    "assets/uipath_failure_analyst_agent_debug_success.png"
)
UIPATH_FAILURE_ANALYST_OUTPUT_DETAIL_SCREENSHOT = Path(
    "assets/uipath_failure_analyst_agent_output_detail.png"
)
UIPATH_FAILURE_ANALYST_MODEL_EVIDENCE = Path(
    "evidence/case_001/uipath_failure_analyst_agent_model_selected.txt"
)
UIPATH_FAILURE_ANALYST_NO_ISSUES_EVIDENCE = Path(
    "evidence/case_001/uipath_failure_analyst_agent_no_issues.txt"
)
UIPATH_FAILURE_ANALYST_DEBUG_EVIDENCE = Path(
    "evidence/case_001/uipath_failure_analyst_agent_debug_success.txt"
)


def test_readme_declares_agent_type_and_business_impact_metrics():
    readme = README.read_text(encoding="utf-8")

    assert "## Agent type" in readme
    assert "Agent type: combination" in readme
    assert "External coded agents" in readme
    assert "UiPath-native agent depth" in readme
    assert "Policy Miner Agent" in readme
    assert "Red-Team Agent" in readme
    assert "Test Designer Agent" in readme
    assert "/uipath-native-agent-pack" in readme
    assert "UiPath low-code/governance surfaces" in readme
    assert "## Business impact metrics" in readme
    assert "manual AI workflow review time" in readme
    assert "incident-to-regression coverage" in readme


def test_submission_deck_exists_and_covers_official_criteria():
    deck = DECK_MD.read_text(encoding="utf-8")

    assert "# Agentic Test Swarm Presentation Deck" in deck
    for section in [
        "Problem",
        "Solution",
        "UiPath Control Plane",
        "Track 3 Test Cloud Fit",
        "Business Impact",
        "Demo Flow",
        "Technical Architecture",
        "Roadmap",
    ]:
        assert f"## {section}" in deck


def test_pptx_deck_artifact_exists():
    assert DECK_PPTX.exists()
    with ZipFile(DECK_PPTX) as deck:
        names = set(deck.namelist())

    assert "[Content_Types].xml" in names
    assert "ppt/presentation.xml" in names
    assert "ppt/slides/slide1.xml" in names


def test_official_track3_alignment_doc_covers_judging_gaps():
    readme = README.read_text(encoding="utf-8")
    doc = OFFICIAL_ALIGNMENT.read_text(encoding="utf-8")

    assert "docs/official_track3_alignment.md" in readme
    for phrase in [
        "Official Track 3 requirements",
        "Business Impact & Adoption Potential",
        "Platform Usage",
        "Technical Execution, Feasibility & Versatility",
        "Completeness of Delivery",
        "Creativity & Innovation",
        "External frameworks and LLMs are allowed",
        "Remaining gap",
        "Action before submission",
    ]:
        assert phrase in doc


def test_judge_quick_start_points_to_proof_pack():
    readme = README.read_text(encoding="utf-8")

    assert "## For Judges: 5-minute evaluation path" in readme
    for phrase in [
        "Live system",
        "UiPath platform proof",
        "Test Cloud evidence",
        "Action Center gate",
        "Presentation deck",
        "docs/judge_scorecard.md",
        "docs/judge_taste_research_2026-05-23.md",
        "docs/tc006_test_manager_runbook.md",
        "docs/final_video_shot_list.md",
        "docs/research_workbench.md",
    ]:
        assert phrase in readme


def test_judge_scorecard_maps_all_official_criteria_to_evidence():
    doc = JUDGE_SCORECARD.read_text(encoding="utf-8")

    for phrase in [
        "Business Impact & Adoption Potential",
        "Technical Execution, Feasibility & Versatility",
        "Platform Usage",
        "Completeness of Delivery",
        "Creativity & Innovation",
        "Coding Agents Bonus",
        "Evidence matrix",
        "Judge-safe boundaries",
        "UiPath first",
        "Python worker second",
        "Judge taste update",
        "Taqi Jaffri",
        "Ingo Philipp",
        "risk thinking",
    ]:
        assert phrase in doc


def test_judge_taste_research_maps_judges_to_demo_strategy():
    doc = JUDGE_TASTE_RESEARCH.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    video = VIDEO_SHOT_LIST.read_text(encoding="utf-8")
    devpost = DEVPOST_PACKAGE.read_text(encoding="utf-8")
    log = RESEARCH_LOG.read_text(encoding="utf-8")

    for phrase in [
        "Judge Taste Research",
        "Taqi Jaffri",
        "Ingo Philipp",
        "enterprise agentic automation",
        "risk-driven agentic testing",
        "risk-revealing tests",
        "AI should amplify judgment, not replace it",
        "the permit is the output, not the product",
        "UiPath-native Agent debug trace",
        "TC-006 incident memory",
    ]:
        assert phrase in doc

    for phrase in [
        "docs/judge_taste_research_2026-05-23.md",
        "risk-revealing tests",
        "AI amplifies judgment, not replaces it",
    ]:
        assert phrase in readme

    for phrase in [
        "Taqi Jaffri",
        "Ingo Philipp",
        "risk-driven agentic testing",
    ]:
        assert phrase in video

    assert "AI should amplify judgment, not replace it" in devpost
    assert "2026-05-23 - Judge taste research" in log


def test_uipath_native_depth_gap_research_is_actionable():
    doc = UIPATH_NATIVE_GAP_RESEARCH.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    readiness = SUBMISSION_READINESS.read_text(encoding="utf-8")
    feedback = PRODUCT_FEEDBACK_SUBMISSION.read_text(encoding="utf-8")
    log = RESEARCH_LOG.read_text(encoding="utf-8")

    for phrase in [
        "UiPath Native Depth Gap Research",
        "Prompt / Context / Tools / Escalations",
        "tool guardrails",
        "tool simulations",
        "Context Grounding",
        "Agent Memory",
        "Autopilot for Testers",
        "Healing Agent",
        "Testing Process Governance",
        "Do not disturb Action Center task `#3545796`",
        "P0 demo-language upgrade",
        "P1 product-feedback upgrade",
        "P2 post-submission build path",
    ]:
        assert phrase in doc

    for phrase in [
        "docs/uipath_native_depth_gap_research_2026-05-23.md",
        "Prompt / Context / Tools / Escalations",
    ]:
        assert phrase in readme

    for phrase in [
        "Native-depth deep dive",
        "tool guardrails",
        "Agent Memory",
    ]:
        assert phrase in readiness

    for phrase in [
        "tool simulations",
        "Agent Memory",
        "Context Grounding",
    ]:
        assert phrase in feedback

    assert "2026-05-23 - UiPath-native depth gap deep dive" in log


def test_test_cloud_native_gap_research_maps_native_features_to_next_actions():
    doc = TEST_CLOUD_NATIVE_GAP_RESEARCH.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    readiness = SUBMISSION_READINESS.read_text(encoding="utf-8")
    feedback = PRODUCT_FEEDBACK_SUBMISSION.read_text(encoding="utf-8")
    video = VIDEO_SHOT_LIST.read_text(encoding="utf-8")
    log = RESEARCH_LOG.read_text(encoding="utf-8")

    for phrase in [
        "Test Cloud Native Gap Research",
        "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit",
        "REQ-PII-001",
        "Finding obsolete tests based on requirements",
        "Obsolete Test Scout",
        "AI-powered test insights",
        "Create Defect webhook",
        "Healing Agent",
        "Testing Process Governance",
        "Do not claim live Healing Agent use",
        "P0 final-video wording",
        "P1 UiPath platform enhancement",
        "P2 post-submission build path",
    ]:
        assert phrase in doc

    for phrase in [
        "docs/test_cloud_native_gap_research_2026-05-23.md",
        "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit",
    ]:
        assert phrase in readme

    for phrase in [
        "Test Cloud native traceability deep dive",
        "REQ-PII-001",
        "Obsolete Test Scout",
    ]:
        assert phrase in readiness

    for phrase in [
        "Create Defect webhook",
        "Testing Process Governance",
        "obsolete test",
    ]:
        assert phrase in feedback

    assert "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit" in video
    assert "2026-05-23 - Test Cloud native traceability deep dive" in log


def test_tc006_runbook_is_safe_for_final_platform_polish():
    doc = TC006_RUNBOOK.read_text(encoding="utf-8")

    for phrase in [
        "TC-006",
        "PVACPOV91",
        "PermitOps Certification Evidence",
        "Manual Execution Assistant",
        "Done",
        "do not click Action Center approval",
        "sixth Test Manager case",
        "Completed six-case execution",
        "final video",
    ]:
        assert phrase in doc


def test_final_video_shot_list_is_uipath_first():
    doc = VIDEO_SHOT_LIST.read_text(encoding="utf-8")

    assert "UiPath-first" in doc
    for phrase in [
        "0:00-0:25",
        "Studio Web / API Workflow",
        "Test Manager / Test Cloud",
        "Action Center",
        "live-swarm-view",
        "deny_and_suspend",
        "TC-006",
        "Do not start from Vercel",
        "UiPath-native agent depth",
        "Policy Miner Agent",
        "Red-Team Agent",
        "Test Designer Agent",
    ]:
        assert phrase in doc


def test_devpost_submission_package_is_ready_to_paste():
    doc = DEVPOST_PACKAGE.read_text(encoding="utf-8")

    for phrase in [
        "Project name",
        "Elevator pitch",
        "What it does",
        "How we built it",
        "UiPath components used",
        "Track: UiPath Test Cloud",
        "Challenge: external LLMs under governance",
        "Accomplishments",
        "What's next",
        "Demo video checklist",
        "GitHub repository",
        "UiPath-native agent depth",
        "Policy Miner Agent",
        "Red-Team Agent",
        "/uipath-native-agent-pack",
    ]:
        assert phrase in doc


def test_product_feedback_submission_is_form_ready():
    doc = PRODUCT_FEEDBACK_SUBMISSION.read_text(encoding="utf-8")

    for phrase in [
        "Best Product Feedback",
        "What worked well",
        "What was hard",
        "Most valuable product improvement",
        "Test Cloud evidence attachments",
        "Maestro to Test Cloud linking",
        "Action Center evidence review",
        "API Workflow runtime permit template",
        "copy-paste answer",
    ]:
        assert phrase in doc


def test_coding_agents_bonus_pack_has_verifiable_artifacts():
    doc = CODING_AGENTS_BONUS.read_text(encoding="utf-8")
    bonus = BONUS_EVIDENCE_PACK.read_text(encoding="utf-8")

    for phrase in [
        "Coding Agents Bonus",
        "Codex",
        "adversarial scenario generation",
        "repair candidate",
        "API Workflow payload scaffolding",
        "evidence/case_001/coding_agent_prompts.jsonl",
        "evidence/case_001/coding_agent_outputs.jsonl",
        "not trusted automatically",
        "Test Cloud evidence",
        "uipath_failure_analyst_agent_debug_success.png",
    ]:
        assert phrase in doc

    for phrase in [
        "Bonus Evidence Pack",
        "UiPath-native agent bonus",
        "Coding Agents bonus",
        "Most Creative Solution",
        "Best Product Feedback",
        "1 Agents.LLMCalls",
        "Completed certification failure analysis",
        "Action Center approval",
    ]:
        assert phrase in bonus


def test_tc006_live_test_manager_mapping_is_documented():
    docs = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            README,
            TEST_MANAGER_PLAN_C,
            SUBMISSION_READINESS,
            JUDGE_SCORECARD,
            TC006_RUNBOOK,
            PLATFORM_SPIKE_STATUS,
            TC006_PLACEHOLDER,
        ]
    )

    for phrase in [
        "PVACPOV91:76",
        "TC006 incident memory blocks phone-number export",
        "Static Assignment (6)",
        "PermitOps Certification Evidence - 20260522.1544",
        "59ea06c1-8074-0f00-8ea7-0b49ad83e475",
        "6 passed / 0 failed / 0 not executed",
        "assets/test_manager_tc006_case_created.png",
        "assets/test_manager_tc006_added_to_test_set.png",
        "assets/test_manager_6_passed_completed.png",
    ]:
        assert phrase in docs

    for path in [
        TC006_CASE_SCREENSHOT,
        TC006_ASSIGNMENT_SCREENSHOT,
        TEST_MANAGER_6_CASE_SCREENSHOT,
        TC006_CASE_EVIDENCE,
        TC006_ASSIGNMENT_EVIDENCE,
        TEST_MANAGER_6_CASE_EVIDENCE,
    ]:
        assert path.exists()

    assert "PVACPOV91:76" in TC006_CASE_EVIDENCE.read_text(encoding="utf-8")
    assert "Static Assignment (6)" in TC006_ASSIGNMENT_EVIDENCE.read_text(encoding="utf-8")
    six_case_evidence = TEST_MANAGER_6_CASE_EVIDENCE.read_text(encoding="utf-8")
    assert "59ea06c1-8074-0f00-8ea7-0b49ad83e475" in six_case_evidence
    assert "Finished" in six_case_evidence
    assert "6 passed / 0 failed / 0 not executed" in six_case_evidence
    for test_name in [
        "TC001 PII export denied",
        "TC002 aggregate access allowed",
        "TC003 raw agent request suspended",
        "TC004 high risk PII approval",
        "TC005 regression keeps PII denied",
        "TC006 incident memory blocks phone-number export",
    ]:
        assert test_name in six_case_evidence


def test_research_workbench_is_ready_for_continuous_deep_research():
    workbench = RESEARCH_WORKBENCH.read_text(encoding="utf-8")
    log = RESEARCH_LOG.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    for phrase in [
        "Continuous Research Workbench",
        "Firecrawl",
        "Exa",
        "Tavily",
        "Brave Search",
        "Crawl4AI",
        "Context7",
        "UiPath AgentHack",
        "research loop",
        "decision record",
        "Action Center task `#3545796` remains pending",
    ]:
        assert phrase in workbench

    for phrase in [
        "2026-05-21",
        "Research stack installed",
        "FIRECRAWL_API_KEY",
        "EXA_API_KEY",
        "next research queue",
    ]:
        assert phrase in log

    assert "docs/research_workbench.md" in readme


def test_agenthack_award_gap_research_prioritizes_uipath_visible_proof():
    doc = AGENTHACK_AWARD_GAP_RESEARCH.read_text(encoding="utf-8")
    log = RESEARCH_LOG.read_text(encoding="utf-8")

    for phrase in [
        "AgentHack Award Gap Research",
        "Research Plan",
        "Context7",
        "Firecrawl",
        "Exa",
        "UiPath must be the visible control plane",
        "Test Cloud needs to feel like managed evidence",
        "Coding-agent bonus is real",
        "uip skills install --agent codex",
        "Failure Analyst Agent",
        "Do not integrate AstrBot/SuperRAG before the first submission",
        "UiPath starts the run",
    ]:
        assert phrase in doc

    for phrase in [
        "AgentHack award gap deep dive",
        "PVACPOV91:76",
        "pending Action Center task `#3545796`",
        "UiPath for Coding Agents",
        "Failure Analyst Agent",
    ]:
        assert phrase in log


def test_uipath_native_failure_analyst_agent_draft_is_documented():
    readme = README.read_text(encoding="utf-8")
    readiness = SUBMISSION_READINESS.read_text(encoding="utf-8")
    scorecard = JUDGE_SCORECARD.read_text(encoding="utf-8")
    swarm_doc = Path("docs/agentic_test_swarm.md").read_text(encoding="utf-8")
    gap_doc = AGENTHACK_AWARD_GAP_RESEARCH.read_text(encoding="utf-8")
    model_evidence = UIPATH_FAILURE_ANALYST_MODEL_EVIDENCE.read_text(encoding="utf-8")
    no_issues_evidence = UIPATH_FAILURE_ANALYST_NO_ISSUES_EVIDENCE.read_text(
        encoding="utf-8"
    )
    debug_evidence = UIPATH_FAILURE_ANALYST_DEBUG_EVIDENCE.read_text(encoding="utf-8")

    assert UIPATH_FAILURE_ANALYST_DRAFT_SCREENSHOT.exists()
    assert UIPATH_FAILURE_ANALYST_MODEL_SCREENSHOT.exists()
    assert UIPATH_FAILURE_ANALYST_NO_ISSUES_SCREENSHOT.exists()
    assert UIPATH_FAILURE_ANALYST_DEBUG_SCREENSHOT.exists()
    assert UIPATH_FAILURE_ANALYST_OUTPUT_DETAIL_SCREENSHOT.exists()

    for phrase in [
        "Agentic Test Swarm Failure Analyst Agent",
        "Generate incident tickets from logs 1 2",
        "gpt-5.4-2026-03-05",
        "{{log_chunk}}",
    ]:
        assert phrase in model_evidence
        assert phrase in no_issues_evidence
        assert phrase in debug_evidence

    for phrase in [
        "Connection is required for this integration tool",
    ]:
        assert phrase in model_evidence

    for phrase in [
        "No issues found",
        "Removed the template Create Issue integration tool",
        "Debug button is enabled",
    ]:
        assert phrase in no_issues_evidence

    for phrase in [
        "Agent run",
        "LLM call",
        "gpt-5.4-2026-03-05-community-agents",
        "1 Agents.LLMCalls",
        "Completed certification failure analysis",
        "Successful",
        "TC-001",
    ]:
        assert phrase in debug_evidence

    for doc in [readme, readiness, scorecard, swarm_doc, gap_doc]:
        assert "UiPath-native" in doc
        assert "Failure Analyst Agent" in doc
        assert "uipath_failure_analyst_agent_no_issues.png" in doc
        assert "uipath_failure_analyst_agent_debug_success.png" in doc


def test_uipath_native_agent_depth_pack_is_documented():
    docs = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            README,
            DEVPOST_PACKAGE,
            VIDEO_SHOT_LIST,
            SUBMISSION_READINESS,
            PLATFORM_SPIKE_STATUS,
            BONUS_EVIDENCE_PACK,
        ]
    )

    for phrase in [
        "UiPath-native agent depth",
        "Policy Miner Agent",
        "Red-Team Agent",
        "Test Designer Agent",
        "Failure Analyst Agent",
        "/uipath-native-agent-pack",
        "evidence/case_001/uipath_native_agent_pack.json",
        "uipath/agents/policy_miner_agent.md",
        "uipath/agents/red_team_agent.md",
        "uipath/agents/test_designer_agent.md",
    ]:
        assert phrase in docs


def test_continuous_quality_memory_and_evidence_graph_are_documented():
    docs = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            README,
            DEVPOST_PACKAGE,
            VIDEO_SHOT_LIST,
            SUBMISSION_READINESS,
            JUDGE_SCORECARD,
            OFFICIAL_ALIGNMENT,
            PRODUCT_FEEDBACK_SUBMISSION,
        ]
    )

    for phrase in [
        "Continuous Quality Memory",
        "Evidence Graph",
        "/continuous-quality-memory",
        "/continuous-quality-memory-view",
        "/evidence-graph",
        "/evidence-graph-view",
        "evidence/case_001/continuous_quality_memory.json",
        "evidence/case_001/evidence_graph.json",
        "Runtime incidents become permanent UiPath Test Cloud regression evidence",
        "trace -> policy -> test -> repair -> approval -> runtime enforcement",
    ]:
        assert phrase in docs


def test_test_cloud_traceability_pack_is_documented_for_judges():
    docs = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            README,
            DEVPOST_PACKAGE,
            VIDEO_SHOT_LIST,
            SUBMISSION_READINESS,
            JUDGE_SCORECARD,
            PRODUCT_FEEDBACK_SUBMISSION,
        ]
    )

    for phrase in [
        "Test Cloud Native Traceability Pack",
        "/test-cloud-traceability",
        "/test-cloud-traceability-view",
        "/test-manager-webhook-demo",
        "/test-manager-webhook-demo-view",
        "evidence/case_001/test_cloud_traceability_pack.json",
        "evidence/case_001/test_manager_create_defect_webhook_demo.json",
        "REQ-PII-001",
        "Requirement -> Test Case -> Execution -> Defect -> Runtime Permit",
        "Obsolete Test Scout",
        "Create Defect webhook",
        "ATS-DEFECT-TC-001",
        "Testing Process Governance",
    ]:
        assert phrase in docs
