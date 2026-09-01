---
{"schema_version":"harness.evidence.v1","id":"EVD-0011","title":"Authorized checkpoint v3 corrective publication candidate","task":"TASK-0007","source_refs":["SRC-0008"],"recorded_at":"2026-09-01","subject_revision_or_fingerprint":"parent git 02d61dc63791d45885d48c280d3ff27ce76e56f7; checkpoint v3 status sha256 303b76893c32f06ccc32fefc037b00b87b5cc7821be8b705b18020dcc128309d","result":"pass_with_direct_post_commit_verification_required","fresh_until":null,"supersedes":null}
---

## Scope and result

- The operator authorized exactly one corrective commit on `main` and exactly
  one normal fast-forward push to the existing private family `origin/main`.
- The candidate contains only the validated checkpoint-v3 erratum, lifecycle,
  provenance, handoff, review/evidence, and designated generated root-integrity
  records.
- Checkpoint v1 and v2, all capability repositories, and the family packet are
  unchanged.
- The family packet locks remain manifest SHA-256
  `54116db0e4f518ffe793df3d3ebd2b87064f00aab10b373bf1909f9126b24867`
  and checksum-file SHA-256
  `e0134782dff26755d450f2aa2117d4a8d8afebbf53578e51c9dbbb809fabf4ee`.
- The harness check, all 15 mutation tests, packet check, `git diff --check`,
  and zero packet diff passed on the candidate source tree.
- Live preflight observed local HEAD, `origin/main`, and remote `main` all at
  `02d61dc63791d45885d48c280d3ff27ce76e56f7`; GitHub reported the exact
  repository private with default branch `main`.

## Direct-verification boundary

This evidence is inside the corrective commit and cannot attest that commit's
later push. After the one normal push, the primary agent must verify local
HEAD, `origin/main`, live remote `refs/heads/main`, and a clean worktree
directly. No additional family evidence commit is authorized.
