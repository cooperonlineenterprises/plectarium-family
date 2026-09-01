---
{"schema_version":"harness.decision.v1","id":"DEC-0004","status":"accepted","previous_status":"proposed","title":"Correct the checkpoint family checksum lock without changing v1 or v2","created_at":"2026-09-01","authority_source":"current operator checkpoint-v3 erratum instruction","source_refs":["SRC-0007"],"supersedes":"DEC-0003","successor":null}
---

This decision supersedes DEC-0003 only for the v2 family checksum lock and
resulting sequencing validity. V1/v2 bytes remain historical evidence.

Use family commit `02d61dc63791d45885d48c280d3ff27ce76e56f7`, packet manifest
`54116db...`, and checksum ledger
`e0134782dff26755d450f2aa2117d4a8d8afebbf53578e51c9dbbb809fabf4ee`.

All v2 profile, no-promotion, second-wave, Sibyl-last, and SDK-deferral rules
remain. No packet/capability/implementation/publication authority changes.
