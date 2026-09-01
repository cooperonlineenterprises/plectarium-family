# Standalone Capability Family Packet v1

**Packet version:** 1.2.0  
**Generated:** 2026-08-31  
**Status:** Canonical family constitution and project-generation substrate

> **Keep the harness small. Make external intelligence strong. Connect them through narrow, evidence-centered contracts.**

This package defines the emerging architecture for ten independently valuable, independently versioned, skill-backed specialist capabilities. It is the authoritative parent context for generating separate project constitutions and build packets; it is not a shared runtime implementation and does not create a universal plugin framework. Each capability also has an established canonical character identity governed by `spec/canonical-character-identities.md`.

The canonical machine family identifier is `standalone-capability-family`. The
family participates in the **Plectarium** suite, which is part of the Octon
ecosystem, but neither relationship creates a runtime dependency or transfers
authority. `spec/family-identity-and-repository-map.md` owns the family
namespace and exact character-to-repository mapping;
`spec/portfolio-source-ownership.md` owns the repository responsibility map.

## Governing separation

```text
Harness
    governs trust, invocation, permissions, evidence use,
    project meaning, decisions, downstream work, and authority

Standalone capability
    owns domain intelligence, specialist tooling, capability-specific
    planning/execution, evidence production, completion, durable results,
    inspection, and comparison
```

A capability result can be highly confident and still remain non-authorizing. “Ready,” “safe,” “verified,” or “conformant” means that the capability produced a bounded conclusion under its declared scope and evidence—not that publication, deployment, infrastructure apply, database migration, code modification, or another project action is authorized.

## Initial family

| Creation order | Capability | Character identity | Repository | Governing question | Durable result |
| --- | --- | --- | --- | --- | --- |
| 1 | Universal Code Audit | **Verity** | `verity` | What appears risky, defective, inconsistent, costly, structurally unhealthy, unnecessarily complicated, or safely removable in this codebase? | UCA Audit Bundle |
| 2 | Verification Assurance | **Titra** | `titra` | What evidence demonstrates that this implementation, change, behavior, or system actually works as claimed? | Verification Bundle |
| 3 | Specification Conformance | **Ortha** | `ortha` | Does the implementation actually conform to the intended requirements, architecture, decisions, contracts, and acceptance criteria? | Conformance Bundle |
| 4 | Supply-Chain Intelligence | **Genea** | `genea` | What external software, artifacts, build inputs, dependencies, and supply-chain risks does this project actually carry? | Supply-Chain Intelligence Bundle |
| 5 | Runtime Investigation | **Echo** | `echo` | What is this system actually doing while it runs, and what evidence explains the observed behavior? | Runtime Investigation Bundle |
| 6 | API / Contract Assurance | **Harmia** | `harmia` | Are interfaces, protocols, consumers, providers, schemas, and service boundaries behaviorally and evolutionarily compatible? | Contract Assurance Bundle |
| 7 | UI / Browser Assurance | **Iris** | `iris` | Does the delivered user experience actually function correctly across the declared browser and UI scope? | UI Assurance Bundle |
| 8 | Database / Migration Assurance | **Janus** | `janus` | Can this schema or data migration be deployed safely under the declared operational conditions? | Migration Assurance Bundle |
| 9 | Infrastructure Assurance | **Atlas** | `atlas` | Is this infrastructure or configuration change coherent, secure, compatible, and sufficiently understood before application? | Infrastructure Assurance Bundle |
| 10 | Release Assurance | **Sibyl** | `sibyl` | Does this exact release candidate possess sufficient evidence to satisfy the declared release-readiness criteria? | Release Assurance Bundle |

Character identities are canonical user-facing identities, not aliases for machine contracts. Descriptive capability IDs remain explicit in machine-facing contracts. Repository names are the exact established character-name projections above; they do not establish future CLI, package, image, schema, skill, or protocol names.

## Authority hierarchy

```text
Family Constitution
       ↓
Family Invariants
       ↓
Canonical Character Identities
       ↓
Shared Provisional Contracts
       ↓
Capability Constitution
       ↓
Capability Invariants
       ↓
Capability Normative Specifications
       ↓
Accepted ADRs
       ↓
Capability Matrix / Release Criteria
       ↓
Workstream Plans
       ↓
Task Instructions
       ↓
Agent Implementation Choices
```

Lower-level work MUST surface a conflict with higher authority rather than silently weaken it.

## How to use this packet

1. Read `FAMILY-CHARTER.md`, `spec/family-invariants.md`, `spec/canonical-character-identities.md`, `spec/family-identity-and-repository-map.md`, `spec/portfolio-source-ownership.md`, and `ARCHITECTURE.md`.
2. Select a capability under `capabilities/<id>/`.
3. Read that seed's boundary, model, security, evaluation, and open questions.
4. Use its `PROJECT-GENERATION-PROMPT.md` to generate the capability’s own production-grade build packet.
5. Preserve `PROVISIONAL` status for shared manifest, envelope, capability-class, and SDK conventions until real implementations justify stabilization.
6. Implement each capability in a separate repository unless an accepted ADR establishes another boundary.

## Normative language

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are used in the RFC 2119/8174 sense when capitalized. The packet distinguishes normative contracts from reference architecture and implementation suggestions.

## Packet integrity

Run:

```bash
python scripts/validate-packet.py
python scripts/validate-packet.py --json
python scripts/validate-packet.py --refresh-projections --write-manifest --refresh-checksums
```

The first two commands are read-only. The final command is the designated
writer for deterministic Markdown projections, the packet manifest, and the
checksum ledger. The validator checks required files, capability seeds,
JSON/YAML, provisional schemas and fixtures, family/capability identities,
repository mappings, downstream provenance requirements, relationship graphs,
decisions, ADRs, projection drift, checksums, manifest integrity, substantive
content, and explicit-open-question handling.

## UCA reference implementation

The validated `uca-full-product-build-packet-v1.zip` is the most mature reference. Its SHA-256 at family-packet generation was:

```text
8409ea03117ad8b5dff1e32b0760ce0fc761775dd70a5254e708ff9fe9949570
```

This packet preserves UCA’s established decisions while refusing to assume that every UCA-specific semantic model belongs in sibling capabilities.
