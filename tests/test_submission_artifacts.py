from pathlib import Path
from zipfile import ZipFile


README = Path("README.md")
DECK_MD = Path("docs/presentation_deck.md")
DECK_PPTX = Path("assets/agentic_test_swarm_deck.pptx")
OFFICIAL_ALIGNMENT = Path("docs/official_track3_alignment.md")


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
