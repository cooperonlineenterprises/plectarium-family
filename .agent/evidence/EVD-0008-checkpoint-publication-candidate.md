---
{"schema_version":"harness.evidence.v1","id":"EVD-0008","title":"Authorized family checkpoint publication candidate","task":"TASK-0004","source_refs":["SRC-0006"],"recorded_at":"2026-09-01","subject_revision_or_fingerprint":"parent git 0b6c476682e416bd4fb770622c56758f5a380f09; candidate source fingerprint 75337bd21ab564ed46860f6cafa41dce46b037b05ace60e66db206fc938991cd","result":"pass_with_post_commit_verification","fresh_until":null,"supersedes":null}
---

## Scope and result

- Operator authorized exactly one family checkpoint commit and one normal
  fast-forward push to the existing private `origin/main`.
- Candidate contains checkpoint v1/v2, lifecycle, dossier, review/evidence,
  handoff, and designated generated root-integrity updates only.
- Family packet bytes are unchanged.
- Harness/dossier check, 15 mutation tests, and family packet check pass.
- `git diff --check` passes and no capability repository changed.

## Direct-verification boundary

This evidence is inside the authorized checkpoint commit. It cannot attest
that commit's later push. After the one normal push, the primary agent must
verify local HEAD, `origin/main`, remote `refs/heads/main`, and a clean
worktree directly. No additional evidence commit is authorized.
