---
{"schema_version":"harness.evidence.v1","id":"EVD-0009","title":"Checkpoint v3 lock and predecessor preservation verification","task":"TASK-0006","source_refs":["SRC-0007"],"recorded_at":"2026-09-01","subject_revision_or_fingerprint":"family 02d61dc; v1/v2 five-file hash sets; v3 corrected lock","result":"pass","fresh_until":null,"supersedes":null}
---

Direct `shasum -a 256` verified family packet manifest
`54116db...` and checksum ledger
`e0134782dff26755d450f2aa2117d4a8d8afebbf53578e51c9dbbb809fabf4ee`.
All v1/v2 hashes remained unchanged. Verity, Titra, and Ortha remained clean at
their published commits. No network or source mutation occurred.
