from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

__test__ = False


Decision = Literal["allow", "deny", "require_human_approval", "deny_and_suspend"]


class AgentToolCall(BaseModel):
    source_agent: str
    target_agent: str
    action: str
    payload: dict[str, Any]


class CapturedTraceMetadata(BaseModel):
    trace_id: str
    captured_at: str
    model: str
    provider: str
    request_id: Optional[str] = None
    mode: Literal["captured_ai_trace_replay"]
    source_agent: str
    target_agent: str


class Policy(BaseModel):
    policy_id: str
    policy_text: str
    risk_level: Literal["low", "medium", "high", "critical"]
    blocked_actions: list[str] = Field(default_factory=list)
    requires_human_approval_for: list[str] = Field(default_factory=list)


class TestScenario(BaseModel):
    __test__ = False

    test_id: str
    name: str
    policy_id: str
    llm_generated_scenario: str
    input_payload: AgentToolCall
    expected_decision: Decision
    expected_reason: str


class TestResult(BaseModel):
    __test__ = False

    test_id: str
    status: Literal["passed", "failed"]
    expected_decision: Decision
    actual_decision: Decision
    failure_reason: Optional[str] = None
    evidence_ref: Optional[str] = None


class LicenseMetadata(BaseModel):
    compiler_version: str
    compiler_rules_hash: str
    evidence_hash: str
    license_hash: str
    issued_at: str
    valid_until: str


class AgentLicense(BaseModel):
    license_id: str
    case_id: str
    source_agent: str
    target_agent: str
    status: Literal["pending_human_approval", "active", "suspended", "blocked"]
    license_level: Literal[
        "L0_uncertified",
        "L1_observation",
        "L2_aggregate_access",
        "L3_restricted_action",
        "SX_suspended",
    ]
    risk_level: Literal["green", "amber", "red"]
    allowed_actions: list[str]
    blocked_actions: list[str]
    human_approval_required: list[str]
    runtime_controls: list[str]
    evidence_refs: list[str]
    license_metadata: LicenseMetadata
