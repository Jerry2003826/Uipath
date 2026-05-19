# Devpost Pitch: PermitOps V9.1

## One-Liner

PermitOps is UiPath-governed licensing for enterprise AI agents: it turns captured agent behavior into Test Cloud evidence, human approval, and runtime API Workflow enforcement.

## Problem

Enterprise AI agents are starting to call internal tools, other agents, and sensitive business APIs. A policy document alone cannot prove that an agent behaved safely. A prompt review alone cannot stop a bad runtime call.

The risky moment is concrete: an agent asks another agent for raw customer data, then tries to export it.

## Solution

PermitOps creates a governed certification loop:

AI trace -> policy test -> Test Cloud evidence -> repair candidate -> re-test -> human approval -> restricted license -> API Workflow runtime enforcement.

The hero scenario uses a Marketing Outreach Agent that attempts to call a Customer Data Agent to export 500 VIP customer emails. PermitOps captures the real raw response, generates policy tests, records evidence in UiPath Test Cloud, routes approval through UiPath Action Center, compiles a restricted license, and enforces the license through a UiPath API Workflow proxy.

## Why UiPath

PermitOps maps naturally onto UiPath Automation Cloud:

- UiPath Maestro orchestrates the certification lifecycle.
- UiPath Test Cloud records the certification evidence.
- UiPath Action Center gates human approval.
- UiPath API Workflow enforces the license at runtime.

That combination makes the system more than a static policy checker. It becomes an auditable operational workflow.

## What Is New

PermitOps treats AI-agent authorization as a testable, evidence-backed license.

The system preserves the real captured AI trace, including the raw response. It uses coding-agent generated adversarial scenarios for breadth, but relies on a deterministic oracle for pass/fail decisions. Then it links the final runtime license to the evidence package using:

- `compiler_rules_hash`
- `evidence_hash`
- `license_hash`

## Demo Moment

The strongest demo moment is the runtime denial.

After the certification loop completes, the Marketing Outreach Agent tries the raw VIP email export again. The UiPath API Workflow proxy checks the restricted license and denies or suspends the request. The denial is not arbitrary; it is connected to Test Cloud evidence, Action Center approval, and license hash metadata.

## Impact

PermitOps gives platform teams a practical governance pattern for enterprise AI agents. It does not claim to solve all compliance or sandboxing problems. It shows a focused, repeatable loop for turning risky observed behavior into tested, approved, restricted runtime access.
