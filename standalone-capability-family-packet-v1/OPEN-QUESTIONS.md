# Family Open Questions

**Authority:** Governance record

## FQ-001 — Shared manifest stabilization threshold

**Status:** `OPEN QUESTION`  
**Why open:** The exact number and maturity of capabilities required before `standalone-capability-manifest.v0` may become v1 is unresolved.  
**Decision affected:** Affects compatibility promises and potential SDK extraction.  
**Evidence required:** Evidence from production UCA, Verification Assurance, and Specification Conformance integrations.  
**Decision owner:** Family Architecture Lead with maintainers of the first three capabilities.  
**May implementation proceed?** Yes; use v0 with explicit provisional status.

## FQ-002 — Shared result-envelope field set

**Status:** `OPEN QUESTION`  
**Why open:** It is not yet proven which envelope fields are truly common versus UCA-derived.  
**Decision affected:** Affects cross-capability verification and Release Assurance.  
**Evidence required:** Two non-UCA bundle implementations and at least one aggregator consumer.  
**Decision owner:** Evidence Systems Lead.  
**May implementation proceed?** Yes; capability-specific bundles may include the v0 envelope.

## FQ-003 — Capability discovery transport

**Status:** `OPEN QUESTION`  
**Why open:** Filesystem manifests, CLI discovery, OCI labels, and registry metadata may all be needed.  
**Decision affected:** Affects installation and harness discovery.  
**Evidence required:** Real local, OCI, and Octon integrations across two capabilities.  
**Decision owner:** Interface Lead.  
**May implementation proceed?** Yes; seed projects implement CLI discovery and static manifest first.

## FQ-004 — CLI, package, image, skill, and protocol naming conventions

**Status:** `OPEN QUESTION`  
**Why open:** Canonical character and repository identities are established, but CLI, package, image, schema, skill, and protocol identifiers remain separate and provisional.  
**Decision affected:** Affects installation, discovery, routing, compatibility, and package names without reopening character or repository identity.  
**Evidence required:** Collision research, routing tests, ecosystem/package availability, and interface review.  
**Decision owner:** Capability Product Owner per project.  
**May implementation proceed?** Yes; use the character and repository identities in their canonical maps and preserve explicit descriptive machine identifiers until separately decided.

## FQ-005 — Result signing policy

**Status:** `OPEN QUESTION`  
**Why open:** Local development results and release/organizational results may require different signing expectations.  
**Decision affected:** Affects result trust and Release Assurance.  
**Evidence required:** Threat modeling plus real CI/Octon result flows.  
**Decision owner:** Security and Provenance Leads.  
**May implementation proceed?** Yes; checksums/provenance are required, signing remains capability policy.

## FQ-006 — Production read-only observation

**Status:** `OPEN QUESTION`  
**Why open:** Runtime, UI, infrastructure, and migration capabilities may need tightly controlled production reads.  
**Decision affected:** Affects authority vocabulary and sandboxing.  
**Evidence required:** Capability-specific threat models and pilot use under least privilege.  
**Decision owner:** Security Lead plus domain owner.  
**May implementation proceed?** Yes; production access remains denied by default.

## FQ-007 — Cross-capability evidence freshness

**Status:** `OPEN QUESTION`  
**Why open:** Different evidence types age according to different material changes.  
**Decision affected:** Affects aggregation and caching.  
**Evidence required:** Real release-assurance experiments and per-capability reuse policies.  
**Decision owner:** Evidence Systems Lead.  
**May implementation proceed?** Yes; consumers must preserve source freshness semantics rather than invent a universal TTL.

## FQ-008 — Common completion extensions

**Status:** `OPEN QUESTION`  
**Why open:** The five common top-level states may be sufficient, but domain-specific substatus needs are unproven.  
**Decision affected:** Affects result envelope and generic harness UI.  
**Evidence required:** At least three implemented capability completion models.  
**Decision owner:** Family Architecture Lead.  
**May implementation proceed?** Yes; top-level common states plus capability payload details.

## FQ-009 — Project implementation language defaults

**Status:** `OPEN QUESTION`  
**Why open:** Rust is strong for orchestration, while browser/scientific/runtime domains may need other languages.  
**Decision affected:** Affects repository scaffolding and shared tooling.  
**Evidence required:** Architecture spikes and ecosystem compatibility studies.  
**Decision owner:** Capability Architecture Lead.  
**May implementation proceed?** Yes; stable external contracts take precedence over language uniformity.

## FQ-010 — Generic harness provider contract version

**Status:** `OPEN QUESTION`  
**Why open:** Octon’s read-only evidence-provider contract may not fit execution-heavy capabilities unchanged.  
**Decision affected:** Affects Octon and other harness integrations.  
**Evidence required:** UCA plus Verification and UI/Runtime provider pilots.  
**Decision owner:** Octon Integration Lead and capability maintainers.  
**May implementation proceed?** Yes; use provider classes and explicit permissions provisionally.

## FQ-011 — Common Agent Skill packaging generator

**Status:** `OPEN QUESTION`  
**Why open:** The Agent Skills standard is useful, but host-specific metadata continues to evolve.  
**Decision affected:** Affects portability and drift.  
**Evidence required:** Install/routing tests in at least four agent hosts.  
**Decision owner:** Agent Interface Lead.  
**May implementation proceed?** Yes; canonical sources plus generated adapters remain the policy.

## FQ-012 — Family packet licensing

**Status:** `OPEN QUESTION`  
**Why open:** The eventual license for this family specification and generated seeds has not been selected.  
**Decision affected:** Affects redistribution and contributions.  
**Evidence required:** Owner decision after legal/IP review.  
**Decision owner:** Project Owner.  
**May implementation proceed?** Yes; source licensing observations are documented, and copied third-party text is avoided.
