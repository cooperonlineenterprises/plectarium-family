---
{"schema_version":"harness.decision.v1","id":"DEC-0003","status":"accepted","previous_status":"proposed","title":"Use profile-qualified packet comparison for second-wave sequencing","created_at":"2026-08-31","authority_source":"current operator three-capability successor checkpoint instruction","source_refs":["SRC-0005"],"supersedes":"DEC-0002","successor":null}
---

## Limited successor scope

This decision supersedes DEC-0002 only where DEC-0002 blocked second-wave
packet generation. DEC-0002 remains controlling for no-promotion and
SDK/runtime deferral.

Profile Verity as `legacy_pre_family_1_2` by exact immutable coordinates and
make no family-schema conformance claim. Qualify schemas by repository,
commit, packet path, schema path, and digest; prohibit bare cross-packet IDs.
Treat reference-to-import conversion as a consumer-owned verified bundle
transformation with compatibility unknown until implementation.

Genea, Echo, Harmia, Iris, Janus, and Atlas packet generation may proceed.
All shared contracts remain provisional/unresolved. Sibyl remains last. No
family packet, capability, runtime, SDK, or publication authority changes.
