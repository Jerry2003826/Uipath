from pathlib import Path
from zipfile import ZipFile


README = Path("README.md")
DECK_MD = Path("docs/presentation_deck.md")
DECK_PPTX = Path("assets/agentic_test_swarm_deck.pptx")
OFFICIAL_ALIGNMENT = Path("docs/official_track3_alignment.md")
JUDGE_SCORECARD = Path("docs/judge_scorecard.md")
TC006_RUNBOOK = Path("docs/tc006_test_manager_runbook.md")
VIDEO_SHOT_LIST = Path("docs/final_video_shot_list.md")


def test_readme_declares_agent_type_and_business_impact_metrics():
    readme = README.read_text(encoding="utf-8")

    assert "## Agent type" in readme
    assert "Agent type: combination" in readme
    assert "External coded agents" in readme
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
        "docs/tc006_test_manager_runbook.md",
        "docs/final_video_shot_list.md",
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
    ]:
        assert phrase in doc


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
        "fallback narration",
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
    ]:
        assert phrase in doc
