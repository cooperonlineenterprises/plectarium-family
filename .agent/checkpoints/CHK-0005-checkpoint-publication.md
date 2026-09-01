---
{"schema_version":"harness.checkpoint.v1","id":"CHK-0005","title":"Family checkpoint publication candidate","created_at":"2026-09-01","task":"TASK-0004","source_revision_or_fingerprint":"parent git 0b6c476682e416bd4fb770622c56758f5a380f09; checkpoint v2 status sha256 54549f741304b37aece4fd5ef774e0c8ad8073751534ebdc53f41486961367c2","supersedes":"CHK-0004","decision_refs":["DEC-0002","DEC-0003"],"evidence_refs":["EVD-0006","EVD-0007","EVD-0008"],"limitations":["Cannot attest the later push of the commit containing it."]}
---

The exact next operation is one normal fast-forward push of the reviewed
checkpoint commit to the existing private family `origin/main`, followed by
direct equality and clean-worktree verification. No second checkpoint push is
authorized.
