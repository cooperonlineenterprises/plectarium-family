# Three-Capability Conventions Checkpoint v2

**Owner:** Plectarium Capability Family  
**Outcome:** `PASS_WITH_PROVISIONAL_DIVERGENCE`  
**Successor scope:** Sequencing disposition only  
**Authority effect:** None

## Correction

Version 1 remains immutable evidence. Its `INCOMPLETE` outcome applied
shared-contract stabilization criteria as hard packet-generation preconditions.
Version 2 narrows the audit to the portfolio sequencing question while
preserving every v1 finding as a compatibility/stabilization limitation.

Verity is explicitly profiled as `legacy_pre_family_1_2` at its exact
repository, commit, packet, manifest digest, and checksum digest. The profile
does not claim that Verity implements the family v0 manifest, carries a
packet-local family source lock, or conforms to post-1.2 schemas.

Titra and Ortha are packet-specific family-1.2 profiles. Their manifests are
not represented as family-v0 schema instances.

## Qualified schema identity

A schema is identified by:

```text
repository + full commit + packet path + schema path + schema SHA-256
```

A bare relative `$id` is never used as a cross-packet registry key. Combined
registries must reject unqualified IDs. This makes the existing relative-ID
reuse a known packaging constraint, not a packet-generation blocker.

## Result-reference and import boundary

Cross-capability consumption follows:

```text
immutable result reference
  -> resolve and verify exact bundle bytes/schema/producer/subject/scope
  -> consumer-owned imported-result transformation
  -> compatibility remains unknown until implemented and tested
```

A native result reference is not itself an imported-result record. Enrichment
is explicit, attributable, and cannot upgrade completion, provenance,
freshness, evidence class, limitations, trust, permissions, or authority.

## Status disposition

- Engine independence, evidence-not-authority, repository isolation, and
  truthful top-level completion remain established/accepted principles.
- Shared manifests, discovery, plans, permissions, result references,
  imported-result shapes, completion payloads, evidence tokens, and lifecycle
  details remain `PROVISIONAL` or `UNRESOLVED`.
- Completion refinements remain capability-specific.
- Public schema namespace policy remains unresolved.
- Shared SDK/runtime remains `DEFERRED`.
- No similarity caused promotion.

## Sequencing result

Genea, Echo, Harmia, Iris, Janus, and Atlas packet generation may proceed with
the exact v2 profiles and limitations.

Sibyl remains last. This checkpoint does not satisfy or waive its need for real
published upstream packet/result contracts and aggregation evidence.

## Limits

This is packet/foundation comparison, not implemented interoperability,
security efficacy, product compatibility, release, or production readiness.
No capability or family packet was edited. No network, commit, or push was
performed.

## Publication boundary

Both family setup pushes remain consumed. Publishing v1 and v2 checkpoint
records requires separate explicit authority for exactly one additional normal
family commit/push to `origin/main`, followed by equality and clean-worktree
verification. `TASK-0004` and repository files grant no such authority.

