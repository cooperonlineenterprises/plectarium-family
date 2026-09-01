---
{"schema_version":"harness.checkpoint.v1","id":"CHK-0007","title":"Checkpoint v3 corrective publication candidate","created_at":"2026-09-01","task":"TASK-0007","source_revision_or_fingerprint":"parent git 02d61dc63791d45885d48c280d3ff27ce76e56f7; checkpoint v3 status sha256 303b76893c32f06ccc32fefc037b00b87b5cc7821be8b705b18020dcc128309d","supersedes":"CHK-0006","decision_refs":["DEC-0003","DEC-0004"],"evidence_refs":["EVD-0009","EVD-0010","EVD-0011"],"limitations":["This commit-local checkpoint cannot attest its own later push.","Shared contracts remain provisional/unresolved; SDK/runtime remains deferred; Sibyl remains last."]}
---

The next and only authorized external operation is one normal fast-forward push
of the reviewed corrective commit to the existing private family
`origin/main`, followed by direct equality and clean-worktree verification. No
later family push is authorized.
