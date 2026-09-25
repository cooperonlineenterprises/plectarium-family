---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0019",
  "title": "Verified Eupora registration and scoped commit candidate",
  "task": "TASK-0011",
  "recorded_at": "2026-09-25",
  "subject_revision_or_fingerprint": "EUPORA_IDENTITY.md sha256 897831f662569a2c9fda4b4789474ceb5d3e3c0d73375ed2cca8850c0184a90f",
  "result": "passed_precommit_checks_with_existing_task_cwd_limitation",
  "fresh_until": null,
  "supersedes": null
}
---

## Observed state and authority

Supported project listing independently verified project
`c9f59fba-755e-4099-8a38-8974ad9f66c2` as `eupora` at
`/Users/jamesryancooper/Projects/plectarium/projects/eupora`. The project ID is
unchanged. Eupora's catalog status/current_path are now registered_project_home
and projects/eupora; its predecessor remains history and it is absent from the
stale-design index.

Supported task reads show old cwds for tasks
`01a0d957-6528-7533-8441-6cb23b6221b3` (Rename Option Space Model) and
`01a0d967-5e08-7ea1-aac0-4a328ae3af0d` (Document Eupora naming decision).
Enabled controls have no applicable retarget operation for these non-Git tasks.
Future implementation MUST start as a new task in the updated saved project.
No task was created and no internal app state was directly rewritten.

Direct user message `01a0d998-4ddc-79e2-80a7-4851c774ffec` authorized scoped
local commits and prohibited push, publication, and implementation. The exact
owner/branch/one-commit boundary is recorded in TASK-0011.

## Validation and review

- Reviewed pending diffs and exact file scope before editing.
- Harness check PASS; 15 existing tests PASS on the isolated source candidate.
- Family packet check PASS (0 errors, 0 warnings); historical workspace check PASS.
- All 35 imported Eupora source files match the pre-move SHA-256 inventory.
- Prior EVD-0017, its task and decisions remain byte-identical; the
  versioned family packet and historical imports are unchanged.
- Generated records are refreshed only with the designated harness writer.
  This evidence/task metadata is followed by a final refresh and read-only check.

Concurrent Gnomia shared-file edits were coordinated with their owning task,
which held writes. This commit candidate uses the pre-Gnomia source boundary;
Gnomia additions remain outside the commit and are preserved in the working
tree. Live topology is checked against the merged current catalog, with dirty
working-tree reports distinguished from catalog/path errors. Noerovia work is
untouched. Review is self-review, not independent assurance.

## Commit receipt and limits

The candidate was prepared in a temporary detached worktree of this existing
repository. The exact source snapshots are staged for the authorized local
commit on main. A commit cannot attest its own hash or post-commit status;
Eupora's `RENAME_CLEANUP.md` records those observations after execution.
No push, publication, remote modification, runtime, or family-contract promotion
is performed. Existing task cwds remain a documented limitation.
