# Provisional Family Namespace Migration — Packet 1.2.0

**Status:** `REQUIRED` for consumers of the packet's `PROVISIONAL` v0 schemas  
**Decision:** `FAM-036`; `ADR-013`

## Why this is an in-place v0 change

The v0 manifest, result envelope, and result reference have never been
stabilized. Plectarium must support more than one family, and an unnamespaced
`capability_id` is ambiguous. Packet 1.2.0 therefore makes the breaking change
while retaining the `PROVISIONAL` v0 schema names. This is not evidence that a
published stable engine protocol has been migrated.

## Exact changes

| Document | Pre-1.2.0 shape | Packet 1.2.0 shape |
| --- | --- | --- |
| capability manifest | top-level `capability_id`, `version` | add required top-level `family_id: standalone-capability-family` |
| result envelope | `capability.id`, `capability.version` | replace `id` with `family_id`, `capability_id`, and `version` |
| result reference | top-level `capability_id`, `capability_version` | add required top-level `family_id: standalone-capability-family` |
| imported result | source result reference without namespace | source inherits the updated namespaced result-reference schema |

## Consumer behavior

1. Validate the full document before routing or importing it.
2. Reject missing, unknown, or mismatched `family_id`; do not infer it from a
   character, repository, location, transport, or catalog placement.
3. Compare the full family/capability/version identity tuple.
4. Preserve the tuple through result imports and derived evidence.
5. Treat namespace validity as identity validation only. Trust, compatibility,
   signature policy, freshness, permission, and authority remain separate.

## Producer behavior

New documents generated from packet 1.2.0 MUST emit the namespaced shape.
Producers with legacy local experimental documents may translate only when the
producer family is known from authenticated configuration or an explicit
operator decision; content alone is insufficient. The translation must be
recorded as a migration and must not rewrite immutable historical results.

## Fixtures

`fixtures/provisional-contracts/` includes one valid example per affected
schema and three deliberately invalid legacy examples. The packet validator
checks both acceptance and rejection so removal of the namespace cannot pass
as a compatible edit.
