# Family Decision Ledger

## FAM-001 — Standalone specialist capability boundary

**Status:** `ESTABLISHED`  
**Decision:** Heavy domain intelligence is implemented in independently versioned capabilities rather than accumulated inside Octon Mini.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Embed specialist features directly in Octon Mini; use ad-hoc scripts per project.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-002 — Harness-agnostic core

**Status:** `ESTABLISHED`  
**Decision:** No capability core may require Octon Mini or another agent harness.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-003 — One authoritative engine per capability

**Status:** `ESTABLISHED`  
**Decision:** CLI, CI, MCP, OCI, Agent Skills, harness adapters, and future HTTP must not create divergent semantic engines.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Allow each transport to implement its own semantics.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-004 — Evidence is not authority

**Status:** `ESTABLISHED`  
**Decision:** Capability results never authorize repository, production, publication, deployment, database, infrastructure, or project actions.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-005 — Explicit permissions and effects

**Status:** `ESTABLISHED`  
**Decision:** Capabilities declare execution, network, credential, write, and controlled-resource requirements before use.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-006 — No hidden installation or network

**Status:** `ESTABLISHED`  
**Decision:** Capabilities do not silently install specialist tools or enable network access.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-007 — Truthful completion

**Status:** `ESTABLISHED`  
**Decision:** Unavailable, denied, stale, unsupported, failed, timed-out, or partial work cannot appear complete or passed.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-008 — Agent Skills orchestrate engines

**Status:** `ESTABLISHED`  
**Decision:** Skills teach intent routing, invocation, completion inspection, interpretation, and handoff; they do not implement domain intelligence.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-009 — Durable result per capability

**Status:** `ACCEPTED`  
**Decision:** Every material capability produces an inspectable, provenance-aware durable result artifact.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Return conversational summaries only.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-010 — Shared result envelope v0

**Status:** `PROVISIONAL`  
**Decision:** A small common envelope carries capability identity, subject, permission, completion, provenance, and payload references; domain payloads remain capability-specific.

**Rationale:** The convention appears useful from UCA and family design, but has not yet survived multiple independently implemented capabilities.

**Alternatives considered:** Force every capability into the UCA Audit Bundle; have no common metadata at all.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation. Classified cautiously because only UCA has a mature build packet.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-011 — Standalone capability manifest v0

**Status:** `PROVISIONAL`  
**Decision:** A shared discovery manifest is defined for experimentation and is not yet a stable universal standard.

**Rationale:** The convention appears useful from UCA and family design, but has not yet survived multiple independently implemented capabilities.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation. Classified cautiously because only UCA has a mature build packet.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-012 — Shared permission vocabulary

**Status:** `PROVISIONAL`  
**Decision:** The family uses a common permission vocabulary while allowing capability-specific refinements through explicit extension.

**Rationale:** The convention appears useful from UCA and family design, but has not yet survived multiple independently implemented capabilities.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation. Classified cautiously because only UCA has a mature build packet.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-013 — Shared lifecycle convention

**Status:** `PROVISIONAL`  
**Decision:** Discover, plan, permission review, execute/analyze, evidence, completion, durable result, inspect/compare is a reference lifecycle rather than a mandatory identical workflow.

**Rationale:** The convention appears useful from UCA and family design, but has not yet survived multiple independently implemented capabilities.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation. Classified cautiously because only UCA has a mature build packet.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-014 — Capability classes

**Status:** `PROVISIONAL`  
**Decision:** Four descriptive classes are used for seed comparison but are not yet a stabilized taxonomy.

**Rationale:** The convention appears useful from UCA and family design, but has not yet survived multiple independently implemented capabilities.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation. Classified cautiously because only UCA has a mature build packet.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-015 — External specialist tool preference

**Status:** `ESTABLISHED`  
**Decision:** Capabilities integrate mature specialist tools through explicit adapters when ownership would not create differentiated value.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-016 — Out-of-process or OCI adapter boundary

**Status:** `ACCEPTED`  
**Decision:** Specialist adapters should normally run out of process or in OCI rather than as arbitrary in-process plugins.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-017 — AI is optional evidence and interpretation

**Status:** `ESTABLISHED`  
**Decision:** AI may reason over evidence but does not become project authority, execution authority, or the sole engine.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-018 — Imported evidence preserves provenance

**Status:** `ESTABLISHED`  
**Decision:** Cross-capability evidence retains source capability/version/result/completion/class/limitations and does not silently become native evidence.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-019 — No mandatory capability dependency cycles

**Status:** `ESTABLISHED`  
**Decision:** Family relationships are optional evidence or aggregation unless a capability constitution explicitly establishes a hard dependency.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-020 — UCA is reference implementation, not universal mold

**Status:** `ESTABLISHED`  
**Decision:** UCA proves the first pattern but its code-audit semantics are not assumed universal.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-021 — No universal capability framework yet

**Status:** `ESTABLISHED`  
**Decision:** Shared runtime/framework/SDK extraction is deferred until at least three real capabilities demonstrate stable common needs.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Build a universal framework before capability implementations.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-022 — Verification Assurance is capability two

**Status:** `ACCEPTED`  
**Decision:** Verification tests whether the outer lifecycle and execution evidence model survive beyond UCA.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-023 — Specification Conformance is capability three

**Status:** `ACCEPTED`  
**Decision:** Conformance tests aggregation, traceability, authority conflict, and imported evidence after UCA and Verification.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-024 — Release Assurance is a late aggregator

**Status:** `ACCEPTED`  
**Decision:** Release Assurance is built after upstream result interoperability has real evidence.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Build Release Assurance first as a monolith.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-025 — Generated platform skill adapters

**Status:** `ACCEPTED`  
**Decision:** Canonical skill sources generate thin platform packages with drift and behavior tests.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-026 — No interface authority escalation

**Status:** `ESTABLISHED`  
**Decision:** Transport choice cannot silently grant stronger permissions or authority.

**Rationale:** The decision supports production-shaped independent capabilities and narrow evidence-centered interoperability.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-027 — Production-shaped products in dependency order

**Status:** `ACCEPTED`  
**Decision:** Each capability targets a mature v1; Minimum Complete Architecture is an integration checkpoint rather than the product ambition.

**Rationale:** This preserves the governing separation between lightweight orchestration and strong specialist intelligence, and prevents domain implementation or action authority from leaking across boundaries.

**Alternatives considered:** Ship deliberately tiny MVPs with likely redesign later.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-028 — Shared family SDK

**Status:** `DEFERRED`  
**Decision:** Manifest/result/completion/provenance helpers may be extracted only after demonstrated duplication.

**Rationale:** The likely value is acknowledged, but implementation now would generalize ahead of evidence and could create a framework before real products prove the need.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation. Classified cautiously because only UCA has a mature build packet.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-029 — Hosted capability service or marketplace

**Status:** `DEFERRED`  
**Decision:** No central service, registry, or marketplace is required by the family architecture.

**Rationale:** The likely value is acknowledged, but implementation now would generalize ahead of evidence and could create a framework before real products prove the need.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation. Classified cautiously because only UCA has a mature build packet.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-030 — Octon capability monolith

**Status:** `REJECTED`  
**Decision:** Octon Mini will not absorb specialist analysis implementations.

**Rationale:** The alternative would increase coupling, hidden authority, duplicated semantics, or maintenance weight without improving capability evidence.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-031 — Capability mega-engine

**Status:** `REJECTED`  
**Decision:** No single capability should absorb all testing, runtime, supply chain, browser, infrastructure, migration, and release intelligence.

**Rationale:** The alternative would increase coupling, hidden authority, duplicated semantics, or maintenance weight without improving capability evidence.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-032 — Skill-only capabilities

**Status:** `REJECTED`  
**Decision:** A prompt or skill cannot substitute for an independently usable engine and durable result.

**Rationale:** The alternative would increase coupling, hidden authority, duplicated semantics, or maintenance weight without improving capability evidence.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-033 — Automatic downstream action

**Status:** `REJECTED`  
**Decision:** Capability conclusions do not automatically create issues, mutate projects, deploy, publish, apply infrastructure, or migrate databases.

**Rationale:** The alternative would increase coupling, hidden authority, duplicated semantics, or maintenance weight without improving capability evidence.

**Alternatives considered:** Capability-specific or harness-embedded alternatives were considered and remain available only through an explicit ADR if new evidence warrants them.

**Consequences:** Capability project packets and implementations must align or surface a conflict through change control.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `ARCHITECTURE.md`, capability seeds, relationship matrix, and relevant interfaces.

**Source/provenance:** Current family generation directive and established UCA/Octon conversation.

**Reconsideration trigger:** Material evidence from at least two implemented capabilities that the decision creates more total complexity, weakens safety, or blocks a legitimate domain need.

## FAM-034 — Canonical character identities

**Status:** `ESTABLISHED`  
**Decision:** The ten capabilities use Verity, Titra, Ortha, Genea, Echo, Harmia, Iris, Atlas, Janus, and Sibyl as their canonical character identities. The exact mapping and usage rules are governed by `spec/canonical-character-identities.md`. Alternate short forms, nicknames, and competing character names are prohibited unless this decision is explicitly superseded through family architecture change control.

**Rationale:** Each identity expresses how its capability behaves and produces evidence while remaining distinct, pronounceable, conversationally natural, and compatible with the family authority boundary.

**Alternatives considered:** Retain descriptive working names as the only user-facing identity; use abbreviations or acronym-derived names; require a single mythological or morphological naming system; maintain formal and informal name pairs.

**Consequences:** Documentation, Agent Skills, user-facing help and projections, harness integrations, UI, reports, and future product materials use the canonical identity consistently. Technical capability IDs remain descriptive. `FAM-036` subsequently establishes exact character repository mappings while leaving CLI, package, image, schema, skill, and protocol identifiers to separate decisions. Anthropomorphism never grants project or execution authority.

**Affected artifacts:** `FAMILY-CHARTER.md`, `spec/canonical-character-identities.md`, capability matrix, capability seeds, Agent Skill seeds, project-generation directives, interface guidance, evaluation gates, and family documentation.

**Source/provenance:** Operator-finalized `capability-family-canonical-character-identities.md`, version 1.0, status `ESTABLISHED`, provided 2026-08-31 and incorporated verbatim as the packet naming specification.

**Reconsideration trigger:** Explicit family architecture supersession supported by identity, product, routing, and compatibility evidence.

## FAM-035 — Plectarium relationship and portfolio source ownership

**Status:** `ESTABLISHED`  
**Decision:** Plectarium is the suite brand and part of the Octon ecosystem
without becoming an Octon-prefixed product, runtime dependency, authority
transfer, eleventh capability, or owner of family and capability semantics.
Suite, family, capability, workspace, and harness source ownership remain
separate.

**Rationale:** A cohesive suite can improve discovery and operation without
collapsing product meaning into a monorepo or allowing the suite and harness to
compete with the family and capability repositories as canonical sources.

**Alternatives considered:** Make Octon the formal product prefix; make
Plectarium the family or an eleventh capability; let the suite own shared
contracts and domain semantics; duplicate mutable ownership across repositories.

**Consequences:** `spec/portfolio-source-ownership.md` governs the exact map.
Plectarium owns suite semantics and its bill of materials; the family owns
family contracts and seeds; each capability owns its engine and domain
payloads; the workspace owns local operational state; harnesses retain trust
and downstream authority. “Part of the Octon ecosystem” grants no authority.

**Affected artifacts:** `FAMILY-CHARTER.md`, `ARCHITECTURE.md`,
`spec/portfolio-source-ownership.md`, capability generation prompts, and
Plectarium consumer contracts.

**Source/provenance:** Operator-issued Plectarium portfolio foundation prompt,
2026-08-31; `ADR-013`.

**Reconsideration trigger:** A successor portfolio architecture proves that an
ownership boundary prevents legitimate behavior and supplies migration,
compatibility, and authority analysis.

## FAM-036 — Namespaced family identity and character repository mapping

**Status:** `ESTABLISHED`  
**Decision:** The canonical `family_id` is
`standalone-capability-family`. Provisional manifest and result identities carry
it alongside descriptive `capability_id` and capability version. Each
capability repository uses its exact lowercase canonical character name:
`verity`, `titra`, `ortha`, `genea`, `echo`, `harmia`, `iris`, `janus`,
`atlas`, and `sibyl`. Downstream consumers pin the published family commit and
packet-manifest digest instead of forking family contracts.

**Rationale:** Plectarium is designed to support future families, so capability
IDs require a stable family namespace. Exact repository identity removes the
old mismatch between canonical product characters and provisional descriptive
repository names while preserving descriptive IDs for machine contracts.

**Alternatives considered:** Assume one global capability-ID namespace; use
repository or character names as protocol identity; let every consumer choose
a family prefix; leave repositories provisional; copy schemas into Plectarium.

**Consequences:** Packet 1.2.0 updates still-provisional v0 manifest, envelope,
and result-reference schemas and supplies explicit migration fixtures.
Repository identity is established separately from CLI, package, image,
schema, skill, and protocol naming. A namespace is not permission, trust, or a
compatibility claim.

**Affected artifacts:** `spec/family-identity-and-repository-map.md`,
`spec/provisional-manifest.md`, `spec/result-envelope.md`, provisional schemas,
fixtures, capability metadata and generation provenance, validators, manifest,
and checksums.

**Source/provenance:** Operator-issued Plectarium portfolio foundation prompt,
2026-08-31; `ADR-013`.

**Reconsideration trigger:** A successor decision supplies collision,
compatibility, routing, migration, and published-consumer impact analysis.
