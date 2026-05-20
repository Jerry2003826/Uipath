# Devpost Pitch: Agentic Test Swarm

## One-Liner

Agentic Test Swarm is a UiPath-orchestrated team of AI testing agents that attacks, repairs, re-tests, and certifies enterprise AI workflows.

## Problem

Enterprise AI agents are starting to call other agents, internal APIs, and sensitive business tools. A policy document alone cannot prove that an agent behaves safely. A prompt review alone cannot stop a risky runtime call.

The risky moment is concrete: a Marketing Outreach Agent asks a Customer Data Agent to export 500 VIP customer emails after claiming urgent executive approval.

## Solution

Agentic Test Swarm creates a testing loop:

```text
AI trace -> Policy Miner -> Red-Team Agent -> Test Designer -> Test Selector
-> Test Cloud evidence -> Failure Analyst -> Repair Agent -> targeted re-test
-> Quality Governor -> runtime permit -> API Workflow enforcement
```

The hero scenario uses a Marketing Outreach Agent that attempts to call a Customer Data Agent to export raw customer PII. A captured AI trace shows the unsafe behavior. A Policy Miner Agent extracts obligations from the raw PII policy. A Red-Team Agent generates adversarial scenarios. A Test Designer Agent turns those attacks into Test Cloud certification cases. A Test Selector Agent chooses the critical tests by risk, coverage, and changed tool scope.

When the first certification run catches the raw PII export failure, a Failure Analyst Agent explains the root cause and recommends a targeted repair. A coding-agent-backed Repair Agent proposes the guardrail candidate. The system re-tests the affected path, records the evidence in UiPath Test Cloud / Test Manager, routes a restricted runtime permit to Action Center for human approval, and enforces that permit through a UiPath API Workflow proxy.

The permit is the output, not the product. The product is the testing swarm.

V11 adds a live agentic testing loop. The demo includes a deterministic Customer Data Agent under test. Before repair, it accepts an executive-override prompt and returns raw customer emails. The Test Selector reacts to a changed tool schema by adding a new phone-number export regression test, `TC-006`. The Failure Analyst explains the raw PII failure, the Repair Agent proposes a guardrail, and the same attack is re-run. After repair, the Customer Data Agent returns `deny_and_suspend`.

The runtime incident also becomes memory: a production-style raw phone export event is converted into a permanent antibody regression test. That turns the system from a one-time certification demo into a quality memory loop.

## Why UiPath

Agentic Test Swarm maps naturally onto UiPath Automation Cloud:

- UiPath Test Cloud records generated tests, selected tests, failure evidence, and re-test evidence.
- UiPath Maestro / Studio Web models the test-swarm lifecycle.
- UiPath Action Center gates the restricted production permit.
- UiPath API Workflow enforces the tested permit at runtime.
- Coding agents generate adversarial scenarios and repair candidates, while deterministic oracles and UiPath evidence decide what is trusted.

That combination makes the system more than a local testing framework. It becomes an auditable enterprise testing and governance workflow.

## What Is New

Most AI-agent governance demos start with permissions and approval. Agentic Test Swarm starts with testing.

The system treats an AI worker as something that must be attacked, repaired, re-tested, and certified before it can touch production tools. It combines:

- policy-to-test generation
- red-team prompt-injection scenarios
- risk and coverage based test selection
- failure analysis
- coding-agent repair suggestions
- targeted re-tests
- Test Cloud evidence
- human approval
- runtime API Workflow enforcement
- incident-to-regression "antibody" tests

The final PermitOps Runtime Permit includes:

- `compiler_rules_hash`
- `evidence_hash`
- `license_hash`

Those hashes connect the runtime denial back to the Test Cloud evidence and approved governance rules.

## Demo Moment

After the swarm completes certification, the Marketing Outreach Agent tries raw VIP email export again. The UiPath API Workflow proxy checks the restricted permit and returns `deny_and_suspend`.

That denial is not arbitrary. It is backed by red-team scenarios, Test Cloud evidence, a repair candidate, targeted re-tests, Action Center approval, and hash-linked runtime metadata.

The second demo moment is `TC-006`: a new raw phone-number export surface appears, and the Test Selector automatically adds an antibody test rather than running the same static test set forever.

## Impact

Agentic Test Swarm gives QA, platform, and automation teams a practical pattern for validating AI-infused workflows. It does not claim to solve all compliance or sandboxing problems. It demonstrates one focused loop for turning risky observed AI-agent behavior into tested, repaired, approved, and enforceable runtime access.
