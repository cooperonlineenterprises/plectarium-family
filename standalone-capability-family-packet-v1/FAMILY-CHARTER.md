# Standalone Capability Family Charter

**Authority:** Highest family-level product authority  
**Status:** `ESTABLISHED`

## 1. Purpose

The Standalone Capability Family exists to let humans, CI systems, agents, Octon Mini, and other harnesses use deep specialist intelligence without embedding that intelligence into the harness. Each capability is a real product with its own engine, lifecycle, evidence semantics, security posture, versioning, result artifact, interfaces, and release quality.

> **Capabilities determine domain-specific evidence. Harnesses determine trust, authority, project meaning, and downstream action.**

## 2. Product-family ambition

The family aims to produce mature tools for code health, verification, specification conformance, supply-chain intelligence, runtime investigation, interface compatibility, user-interface assurance, infrastructure assurance, migration assurance, and release readiness. A mature family should make a lightweight harness dramatically more capable without making the harness a domain monolith.

### 2.1 Canonical character identities

The family uses the canonical character identities **Verity**, **Titra**, **Ortha**, **Genea**, **Echo**, **Harmia**, **Iris**, **Atlas**, **Janus**, and **Sibyl** for its ten specialist capabilities. `spec/canonical-character-identities.md` governs the exact mapping, meaning, usage, and no-alias rule.

Character identity is a product and interaction device. It does not replace explicit capability IDs or descriptive names in machine-facing contracts, and it does not grant project, execution, or downstream authority.

### 2.2 Family and suite identity

The canonical machine family identifier is
`standalone-capability-family`. Provisional discovery and durable-result
contracts identify a producer with both that `family_id` and a descriptive
`capability_id`, plus the applicable capability version. A family identifier
prevents collisions when a suite or consumer supports more than one family;
it does not create trust, compatibility, adoption, or permission.

**Plectarium** is the cohesive suite and optional control-plane product through
which this family may be discovered and used. Plectarium is part of the Octon
ecosystem, but the suite, the family, each capability, and every harness remain
separate authority and implementation boundaries. Plectarium is not an
eleventh capability and MUST NOT absorb specialist domain semantics.

Repository and source ownership are governed by
`spec/portfolio-source-ownership.md`. Exact character-to-repository identity
is governed by `spec/family-identity-and-repository-map.md`.

## 3. Intended consumers

- human developers, architects, reviewers, operators, and release owners;
- local and hosted CI systems;
- Octon Mini and other governance/orchestration harnesses;
- coding agents using canonical Agent Skills;
- MCP clients;
- custom automation using CLI, OCI, or future HTTP interfaces;
- downstream capability aggregators such as Release Assurance.

## 4. Family philosophy

1. **Independent utility.** Every capability is useful without Octon Mini or another harness.
2. **Domain excellence without governance capture.** A specialist capability becomes excellent at its domain without becoming a project authority system.
3. **Narrow integration.** Harnesses consume explicit requests, plans, completion records, durable result references, and evidence—not internal implementation APIs.
4. **Durable truth.** Material results are inspectable, provenance-aware artifacts rather than transient conversations.
5. **Explicit effects.** Execution, network, credentials, browsers, infrastructure, databases, production access, and writes are declared before use.
6. **Truthful limits.** Partial or unavailable analysis remains partial or unavailable.
7. **Interface unity.** Transport and presentation do not create semantic forks.
8. **Tool leverage.** Mature specialist tools are integrated when UCA-family ownership would add weight without differentiated value.
9. **AI discipline.** AI may interpret and synthesize evidence but does not become project authority or hidden execution.
10. **Evidence-led generalization.** Build real capabilities first; generalize only what survives real use.

## 5. Family non-goals

This family is not:

- a universal plugin runtime;
- a capability marketplace;
- an agent harness;
- a replacement for Octon Mini governance;
- a single mega-engine;
- a generic workflow language;
- an automatic remediation platform;
- an infrastructure, database, deployment, or publishing authority;
- a hidden specialist-tool installer;
- a requirement that all capabilities use one implementation language or identical payload schema;
- a reason to force every helper into a standalone product.

## 6. When standalone status is justified

A function is a strong capability candidate when several are true:

- substantial domain logic;
- specialist external tooling;
- domain-specific evidence semantics;
- meaningful execution/security requirements;
- long-running analysis;
- independent use outside Octon Mini;
- distinct release/version lifecycle;
- reusable value across projects and harnesses;
- substantial evaluation burden;
- context or tooling too expensive to live in a lightweight harness.

Ordinary adapters, formatting helpers, tiny validators, and project-specific scripts SHOULD remain inside the product or harness that owns them unless real evidence supports extraction.

## 7. What remains in Octon Mini

Harness-native concerns include trust, authority, project policy, task and decision lifecycle, evidence routing, instruction/context routing, invocation governance, receipts, downstream authorization, resumability, and handoff. A capability MUST NOT move those responsibilities into itself.

## 8. Development philosophy

Each project should target a production-shaped mature v1 and proceed in dependency order:

```text
real product architecture
        ↓
stable foundational contracts
        ↓
minimum complete architecture
        ↓
parallel domain depth
        ↓
continuous integration and evaluation
        ↓
production hardening
        ↓
mature v1
```

The Minimum Complete Architecture is an integration checkpoint—not a license to freeze a deliberately underpowered product. AI can accelerate implementation breadth, but generated breadth MUST NOT outrun architectural understanding, verification, security, or maintainability.

## 9. Change authority

Family invariants may change only through an explicit family ADR. A capability may refine provisional shared conventions. If a real domain need conflicts with a shared convention, the correct response is to surface the conflict and determine whether the shared convention was over-generalized—not to hide a divergence.

The Plectarium product constitution may narrow how the suite consumes family
contracts, but it cannot redefine this family's identifier, capability
identities, result semantics, or authority model. Downstream repositories pin
an immutable published family commit and packet-manifest digest; they do not
fork family-owned contracts into competing canonical sources.
