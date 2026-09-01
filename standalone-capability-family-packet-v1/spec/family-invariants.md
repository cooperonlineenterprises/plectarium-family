# Family Architectural Invariants

**Authority:** Binding family invariants  
**Status:** `ESTABLISHED`

An implementation plan, task, capability seed, interface, or integration that conflicts with these invariants must surface the conflict and follow family change control.

## INV-001 — Independent usability

Every capability MUST remain usable without Octon Mini, another harness, MCP, AI, or a hosted service.

**Compliant:** a human can install the capability and use its canonical CLI to produce and inspect its durable result.  
**Violation:** capability core imports Octon task types or refuses to run without a harness connection.

## INV-002 — Harness agnosticism

No capability core may require the internal state model of Octon Mini or another harness. Harness adapters MUST remain thin and replaceable.

## INV-003 — Domain ownership

Substantial specialist intelligence belongs in the capability. Trust, project policy, authority, decisions, downstream work, and handoff belong in the harness or human process.

## INV-004 — One authoritative semantic engine

CLI, CI, MCP, OCI, Agent Skills, harness adapters, and future HTTP surfaces MUST reach the same capability semantics. Interfaces may differ in transport and presentation but MUST NOT independently redefine planning, evidence, conclusion, or completion.

## INV-005 — Evidence is not authority

Capability output MUST NOT authorize repository mutation, Git changes, issue creation, communication, artifact publication, deployment, infrastructure apply, database writes, production mutation, or another external action.

## INV-006 — Explicit permissions

Material execution and access requirements MUST be inspectable before execution. A capability MUST NOT silently widen subject scope, network, credentials, writes, project execution, browser access, infrastructure/database access, or production access.

## INV-007 — No hidden installation

Capabilities MUST NOT silently install or update specialist tools, language runtimes, browser binaries, packages, providers, plugins, or dependencies. They may diagnose and identify compatible artifacts.

## INV-008 — No hidden network

Network access is denied by default and must be declared by operation, purpose, destination class, and data category where practical.

## INV-009 — Truthful completion

Unavailable tools, denied permissions, unsupported environments, failures, timeouts, stale evidence, corrupt inputs, partial scope, or incomplete upstream evidence MUST remain visible. Absence of a detected problem is not proof that none exists outside analyzed scope.

## INV-010 — Distinguishable evidence

Static, contract, external-tool, heuristic, historical, runtime, imported-human, AI, derived, and unavailable/absence evidence MUST remain distinguishable when material to interpretation.

## INV-011 — AI optionality and limits

AI MUST NOT become the only engine, project authority, credential authority, hidden tool executor, production authority, or mutation path. AI-derived claims should cite supporting evidence and preserve provider/context provenance.

## INV-012 — Durable material results

Material capability outcomes SHOULD be written to inspectable, checksummed, provenance-aware result artifacts. Conversation text and CI annotations are projections, not canonical truth.

## INV-013 — Interface authority equivalence

A transport MUST NOT gain stronger rights merely because it is CI, MCP, OCI, HTTP, an Agent Skill, or a harness invocation. Permission decisions remain explicit and policy governed.

## INV-014 — Imported evidence provenance

A consuming capability MUST preserve upstream capability identity, version, result identity, completion, evidence class, scope, freshness, provenance, and limitations. Imported evidence MUST NOT silently become native evidence.

## INV-015 — No premature framework

The family MUST NOT construct a universal capability runtime, marketplace, plugin system, SDK, or policy language before multiple real capabilities demonstrate stable shared needs and an accepted ADR authorizes extraction.

## INV-016 — Capability-specific semantics remain legitimate

Shared conventions MUST NOT force unrelated domains into identical claim, candidate, finding, graph, prioritization, payload, or substatus models.

## INV-017 — No automatic downstream action

A conclusion may recommend or inform work but cannot automatically perform or authorize it. Release readiness cannot publish; infrastructure assurance cannot apply; migration assurance cannot write production data; UCA cannot refactor; verification cannot silently change tests.

## INV-018 — Full product in dependency order

Projects SHOULD target production-shaped mature v1 capabilities. A Minimum Complete Architecture is a contract-integration checkpoint, not the final product ambition.

## Changing an invariant

1. Identify the real capability conflict and affected artifacts.
2. Demonstrate why a capability-specific refinement is insufficient.
3. Draft a family ADR with alternatives, security/compatibility impact, migrations, and affected projects.
4. Obtain family architecture and security review.
5. Update charter/invariants/specifications, seeds, matrices, tests, and manifest in one governed change.
6. Never weaken an invariant solely to make implementation easier.
