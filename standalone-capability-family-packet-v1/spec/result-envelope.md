# Provisional Shared Result Envelope

**Status:** `PROVISIONAL v0` — intended for experimentation across UCA, Verification Assurance, and Specification Conformance

The shared envelope standardizes validation and routing metadata. It does not force domain payloads into one schema.

## Required conceptual fields

```text
schema_version
result_id
family ID, capability ID, and capability version
operation
request and plan identity
subject identity
scope reference/summary
requested and accepted permissions
execution environment
completion
produced and imported evidence inventories
conclusion/result payload references
limitations
provenance
tool/provider versions
timestamps
checksums
result content identity
```

## Canonical versus transport identity

The result content identity SHOULD derive from canonical semantic documents and referenced artifact digests. A ZIP, tarball, OCI artifact, directory, or object-store packaging has a transport identity distinct from the canonical result identity.

Producer identity is the tuple
`(family_id, capability_id, capability_version)`. For this family,
`family_id` is exactly `standalone-capability-family`. The nested `capability`
object in the envelope uses `family_id`, `capability_id`, and `version`.
Result references use the same semantics with `capability_version` as the
version field. Consumers reject legacy unnamespaced documents rather than
guessing a family from a repository, character, transport, or location.

## Domain bundles

Examples include:

- UCA Audit Bundle;
- Verification Bundle;
- Conformance Bundle;
- Supply-Chain Intelligence Bundle;
- Runtime Investigation Bundle;
- Contract Assurance Bundle;
- Release Assurance Bundle;
- UI Assurance Bundle;
- Infrastructure Assurance Bundle;
- Migration Assurance Bundle.

Each capability owns required payload sections, internal graph/profile/test formats, retention, and domain conclusion schemas.

## Current experiment

`spec/schemas/result-envelope.v0.schema.json` defines the smallest current experiment. Projects MUST treat it as provisional and version capability-specific payloads independently.

Packet 1.2.0 adds the family namespace in place because v0 remains
`PROVISIONAL`. Migration rules and positive/negative examples are in
`spec/migrations/provisional-family-namespace-1.2.0.md` and
`fixtures/provisional-contracts/`.
