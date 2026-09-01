# Verification Assurance — Full Product Build Packet Generation Directive

Act as the principal product architect, domain specialist, systems architect, security architect, evidence-systems architect, developer-tooling architect, Agent Skill architect, verification architect, AI-team operating-model designer, specification editor, and technical program lead for **Verification Assurance**.

Your job is not to implement the product yet. Generate a canonical, production-grade **Product Constitution + Executable Specification + AI Build Packet** for a new independent repository.

## Established character identity

The canonical character identity is **Titra**. Preserve Titra consistently in user-facing documentation, Agent Skills, help, UI, harness projections, and reports. Do not introduce nicknames or competing character names. Preserve the descriptive capability ID and the exact repository identity established by the family map; treat CLI, package, image, schema, skill, and protocol identifiers as separate decisions. Anthropomorphic language never grants project, execution, or downstream authority.

## Authoritative inputs

1. The complete Standalone Capability Family Packet v1, packet version 1.2.0, from its exact published family Git commit.
2. The seed directory `capabilities/verification-assurance/`.
3. Current primary-source research performed during generation.
4. The UCA Full Product Build Packet as a reference for outer architecture only where relevant.

Before claiming the generated packet is complete, record the exact published
family Git commit, packet version `1.2.0`, SHA-256 of that commit's
`PACKET-MANIFEST.json`, and every family and seed path actually used. Do not
invent a commit or digest when the family repository has not yet been
published. These pins establish reproducible input provenance only; they do
not transfer authority, trust, compatibility, or readiness.

Apply authority in this order:

```text
Family Constitution, established invariants, and canonical character identities
        ↓
This capability seed and capability-specific owner decisions
        ↓
Shared provisional contracts
        ↓
Current primary research
        ↓
Reasonable labeled architectural inference
```

If the domain conflicts with a provisional family convention, preserve the conflict, propose an ADR, and refine the capability-specific design. Do not violate established family invariants silently.

## Product definition

**Governing question:**

> **What evidence demonstrates that this implementation, change, behavior, or system actually works as claimed?**

**Purpose:** Represent explicit claims, discover available proof mechanisms, execute a reviewed verification plan, and return supporting, contradicting, missing, and mutation-sensitivity evidence without overstating ordinary testing as mathematical proof.

**Mature target:** A claim-centered verification engine that can plan and execute proof portfolios across major languages, preserve negative and missing evidence, quantify exercised scope, detect test weakness through mutation/property methods, and provide stable claim status across revisions.

The product owns:

- claim model
- proof-mechanism discovery
- verification planning
- controlled test/build execution
- claim-evidence mapping
- contradiction handling
- verification completion
- Verification Bundle

The product does not own:

- product requirement definition
- automatic bug fixing
- test authoring authority by default
- release authority
- production deployment
- code-quality auditing as a whole

The capability produces evidence and bounded conclusions. It never acquires downstream project authority merely because its result is high confidence.

## Mandatory architecture

Design one authoritative semantic engine beneath:

```text
canonical CLI
CI integration
MCP surface
OCI/container execution
canonical Agent Skill
thin harness provider adapter
future optional HTTP/service interface
```

The product must remain independently usable without Octon Mini, MCP, AI, network access where offline operation is feasible, or a hosted service.

Use the family lifecycle as a starting point:

```text
discover
→ plan
→ review permissions
→ execute/analyze
→ produce evidence
→ capability-specific reasoning/validation
→ truthful completion
→ durable result
→ inspect/compare/report
```

Do not mechanically copy UCA’s candidate/finding model. Define the domain model appropriate to Verification Assurance. Candidate/refutation may be used when useful; explicit claim, obligation, readiness-criterion, or investigation models may be stronger.

## Subject, evidence, and conclusion specifications

Define exact identity and scope for:

- implementation claim
- change set
- behavior or invariant
- build artifact
- scenario
- system version

Primary evidence to operationalize:

- compiler/type-check evidence
- unit/integration/acceptance results
- property-based results
- mutation outcomes
- fuzz reproductions
- contract checks
- runtime assertions
- scenario replay
- benchmark budget observations

Explore and stabilize conclusion/status semantics beginning from:

- `proven_within_scope`
- `strongly_supported`
- `partially_supported`
- `unproven`
- `contradicted`
- `not_testable`
- `verification_incomplete`

For each state define what it means, what it does not prove, minimum evidence, conflicting/unknown evidence, freshness, lifecycle, comparison, and presentation. Avoid fake probability and exaggerated proof language.

## Durable result

Design the **Verification Bundle**. Use the family `result-envelope.v0` only as a provisional experiment. Define capability-specific payloads, schemas, evidence inventories, completion, raw artifacts, interoperability formats, provenance, checksums/content identity, corruption detection, comparison, retention, privacy, and migration.

Cross-capability imports must preserve source identity, version, result ID/schema, subject/scope, completion, evidence class, provenance, freshness, and limitations.

## Permissions and security

Typical permissions that may be needed:

- repository_read
- git_read
- project_execution
- external_process_execution
- output_write
- cache_write
- temporary_write

**Project execution:** Core capability; every command and environment must be explicit in the plan.  
**Network:** Denied by default; selectively allowed for integration environments or external services.  
**Browser:** Optional through delegated UI Assurance or a scoped browser adapter.  
**Production:** Prohibited by default; production observations should normally be imported rather than generated.

Threat-model at least:

- hostile tests and build scripts
- test environments exfiltrating secrets
- flaky/non-deterministic tests
- false proof from tautological tests
- stale test evidence
- unsafe integration credentials

Define exact plan-time permission declarations, default denies, process/OCI isolation, credential and secret handling, network destinations/data classes, output/cache/temp writes, cancellation/resource limits, malicious inputs, compromised adapters, forged results, and domain-specific authority pressure.

## External tool and standards research

Begin with current primary research into:

- mutation testing
- property-based testing
- model-based testing
- test-impact analysis
- flaky-test detection
- coverage semantics
- fuzzing
- verification provenance

Candidate external tools/standards include:

- native compilers and test runners
- Stryker
- PIT
- cargo-mutants
- Hypothesis/QuickCheck-style tools
- fuzzers
- coverage tools
- test-impact analysis tools

For each substantial capability classify: build in engine, integrate existing tool, provide adapter abstraction, or defer. Do not silently install tools. Define static manifest, probe, invocation, version compatibility, permissions, offline behavior, output validation, normalization, cache identity, provenance, and adapter tests.

## Interfaces

Specify:

- CLI command model, structured request, plan digest, stdout/stderr, exit/completion semantics, config precedence, doctor, schemas, adapters, cache, inspection and comparison;
- CI ownership split, fork safety, artifacts, caches, gates, and result upload;
- MCP typed operations/resources with no generic shell/write/installation authority;
- OCI image family, mounts, non-root/read-only/network/resource policy, tool pinning, SBOM, signing, and provenance;
- thin generic-harness and Octon Mini provider integration;
- future service abstractions without making hosted operation required.

## Agent Skill

Create the canonical skill(s): `verification-assurance`. The skill teaches when and how to use the engine, mode/operation selection, permission review, completion inspection, truthful claims, evidence interpretation, escalation, and downstream handoff. It does not become the engine.

Evaluate triggers, negative routing, sibling-skill collisions, permission pressure, missing tools, partial completion, no-skill baseline, and authority separation. Generate platform-specific adapters from one canonical source.

## Evaluation and release proof

Create golden, near-miss, adversarial, partial, corrupt-result, permission-denied, timeout, cache, reproducibility, cross-interface, security, large-subject, and performance fixtures.

The mature product must establish:

- known-claim support/contradiction recall
- false proof rejection
- mutation sensitivity
- flaky-test handling
- scope honesty
- claim-to-evidence traceability

Translate every major release claim into a claim-proof matrix. Passing generic tests is not enough; tests must establish declared product behavior. Report artifact complexity separately from agent/process cost and disclose benchmark limits.

## AI-team build packet

Produce:

- charter, invariants, terminology, architecture, security, lifecycle, authority and execution model;
- normative schemas for requests/plans/subject/scope/evidence/conclusions/completion/result/manifest/adapters/imports;
- capability matrix and depth claims;
- decisions and consequential ADRs;
- workstreams, dependency graph, task packets, change control, validation contract;
- Agent Skill sources and evaluation cases;
- research, source, license, conversation coverage, provenance and source maps;
- roadmap from constitution through Minimum Complete Architecture to mature v1;
- mature-v1 release criteria;
- validator, packet manifest, checksums, ZIP, extracted-copy validation, and integrity report.

## Open questions

Carry forward and investigate these without silently answering them:

- What minimum claim language is expressive without becoming a formal-methods DSL?
- How should mutation-equivalent cases be represented?
- When may imported CI results count as fresh verification?

Record each remaining issue as `OPEN QUESTION` with impact, evidence, owner, and whether implementation may proceed.

## Critical boundary

Do not clone UCA mechanically. Preserve the family outer architecture while developing the evidence, conclusion, execution, security, and evaluation semantics that this domain actually requires.

The final project packet succeeds only if a fresh AI engineering team can begin implementation without the original conversation and can state precisely what it is building, what it may access, what its result means, what it cannot authorize, and what proof is required before mature v1.
