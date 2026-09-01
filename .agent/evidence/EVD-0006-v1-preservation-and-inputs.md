---
{"schema_version":"harness.evidence.v1","id":"EVD-0006","title":"V1 preservation and successor input validation","task":"TASK-0005","source_refs":["SRC-0005"],"recorded_at":"2026-08-31","subject_revision_or_fingerprint":"v1 five-file hashes plus unchanged Verity/Titra/Ortha published commits","result":"pass","fresh_until":null,"supersedes":null}
---

All five v1 checkpoint hashes match their pre-v2 values. Verity, Titra, and
Ortha remain clean at commits `271dde6`, `58cfe83`, and `daeaa7e`;
no capability worktree changed. V2 references the same immutable packet
digests and performs no family-schema conformance claim for Verity.
