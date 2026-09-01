# Infrastructure Assurance — Full Product Build Packet Generation Directive

Act as the principal product architect, domain specialist, systems architect, security architect, evidence-systems architect, developer-tooling architect, Agent Skill architect, verification architect, AI-team operating-model designer, specification editor, and technical program lead for **Infrastructure Assurance**.

Your job is not to implement the product yet. Generate a canonical, production-grade **Product Constitution + Executable Specification + AI Build Packet** for a new independent repository.

## Established character identity

The canonical character identity is **Atlas**. Preserve Atlas consistently in user-facing documentation, Agent Skills, help, UI, harness projections, and reports. Do not introduce nicknames or competing character names. Preserve the descriptive capability ID and the exact repository identity established by the family map; treat CLI, package, image, schema, skill, and protocol identifiers as separate decisions. Anthropomorphic language never grants project, execution, or downstream authority.

## Authoritative inputs

1. The complete Standalone Capability Family Packet v1, packet version 1.2.0, from its exact published family Git commit.
2. The seed directory `capabilities/infrastructure-assurance/`.
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

> **Is this infrastructure or configuration change coherent, secure, compatible, and sufficiently understood before application?**

**Purpose:** Analyze infrastructure definitions and plans for destructive changes, privilege expansion, exposure, drift, policy violations, replacement, rollback, and cost-impact signals without applying changes.

**Mature target:** A multi-format infrastructure assurance engine that safely parses or generates plans, models resource and privilege change, integrates policy tools, detects destructive/exposure changes, and operates without apply authority.

The product owns:

- infrastructure subject identity
- plan/config parsing
- change-impact model
- policy and graph evidence
- simulation/import orchestration
- Infrastructure Assurance Bundle

The product does not own:

- infrastructure apply
- production credentials by default
- cloud resource mutation
- deployment authority
- organization policy governance

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

Do not mechanically copy UCA’s candidate/finding model. Define the domain model appropriate to Infrastructure Assurance. Candidate/refutation may be used when useful; explicit claim, obligation, readiness-criterion, or investigation models may be stronger.

## Subject, evidence, and conclusion specifications

Define exact identity and scope for:

- Terraform/OpenTofu plan
- Kubernetes manifests
- Helm chart
- IAM policy
- container/deployment configuration
- cloud policy
- infrastructure diff

Primary evidence to operationalize:

- plan changes
- resource graph
- privilege deltas
- exposure changes
- destructive/replacement operations
- policy results
- drift indicators
- rollback and cost indicators

Explore and stabilize conclusion/status semantics beginning from:

- `coherent`
- `coherent_with_conditions`
- `policy_violation`
- `destructive_change`
- `privilege_expansion`
- `exposure_change`
- `high_risk`
- `incomplete`

For each state define what it means, what it does not prove, minimum evidence, conflicting/unknown evidence, freshness, lifecycle, comparison, and presentation. Avoid fake probability and exaggerated proof language.

## Durable result

Design the **Infrastructure Assurance Bundle**. Use the family `result-envelope.v0` only as a provisional experiment. Define capability-specific payloads, schemas, evidence inventories, completion, raw artifacts, interoperability formats, provenance, checksums/content identity, corruption detection, comparison, retention, privacy, and migration.

Cross-capability imports must preserve source identity, version, result ID/schema, subject/scope, completion, evidence class, provenance, freshness, and limitations.

## Permissions and security

Typical permissions that may be needed:

- repository_read
- external_process_execution
- infrastructure_read
- output_write
- cache_write
- temporary_write

**Project execution:** Plan generation may execute providers or configuration; explicit controlled environment required.  
**Network:** Denied by default; provider/schema access or read-only cloud queries require explicit authorization.  
**Browser:** Not intrinsic.  
**Production:** Infrastructure apply and mutation strictly prohibited.

Threat-model at least:

- provider code execution
- cloud credential theft
- state-file secrets
- plan manipulation
- destructive apply confusion
- remote-state access
- untrusted custom policies

Define exact plan-time permission declarations, default denies, process/OCI isolation, credential and secret handling, network destinations/data classes, output/cache/temp writes, cancellation/resource limits, malicious inputs, compromised adapters, forged results, and domain-specific authority pressure.

## External tool and standards research

Begin with current primary research into:

- OpenTofu/Terraform planning
- OPA/Rego
- Checkov
- Trivy config
- Kubernetes validation
- IAM analysis
- infrastructure drift and cost analysis

Candidate external tools/standards include:

- OpenTofu/Terraform plan
- OPA
- Checkov
- Trivy config
- Kubernetes validators
- IAM analyzers
- cloud policy tools

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

Create the canonical skill(s): `infrastructure-assurance`. The skill teaches when and how to use the engine, mode/operation selection, permission review, completion inspection, truthful claims, evidence interpretation, escalation, and downstream handoff. It does not become the engine.

Evaluate triggers, negative routing, sibling-skill collisions, permission pressure, missing tools, partial completion, no-skill baseline, and authority separation. Generate platform-specific adapters from one canonical source.

## Evaluation and release proof

Create golden, near-miss, adversarial, partial, corrupt-result, permission-denied, timeout, cache, reproducibility, cross-interface, security, large-subject, and performance fixtures.

The mature product must establish:

- known destructive plans
- near-miss safe changes
- privilege-delta accuracy
- state/secret redaction
- no-apply proof
- provider/network isolation

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

- When is live read-only cloud state required?
- How should provider execution be isolated?
- How should cost estimates be represented without false precision?

Record each remaining issue as `OPEN QUESTION` with impact, evidence, owner, and whether implementation may proceed.

## Critical boundary

Do not clone UCA mechanically. Preserve the family outer architecture while developing the evidence, conclusion, execution, security, and evaluation semantics that this domain actually requires.

The final project packet succeeds only if a fresh AI engineering team can begin implementation without the original conversation and can state precisely what it is building, what it may access, what its result means, what it cannot authorize, and what proof is required before mature v1.
