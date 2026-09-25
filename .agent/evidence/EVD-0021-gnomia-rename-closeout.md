---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0021",
  "title": "Reviewed Gnomia rename and local commit source",
  "task": "TASK-0012",
  "recorded_at": "2026-09-25",
  "subject_revision_or_fingerprint": "GNOMIA_IDENTITY.md sha256 ddb77bc113176a111ccf4e1f437e157838e45d86676d3beb48d3fb8c311d0b70",
  "result": "passed_precommit_checks_with_existing_task_cwd_limitation",
  "fresh_until": null,
  "supersedes": null
}
---

## Observed scope

The current user instruction authorizes one scoped local commit on `main` in
`plectarium-family/repo`, subject “Record accepted Gnomia design-stage identity”. The 14-file allowlist in TASK-0012 contains
only the pending Gnomia identity/registration records, active navigation/status,
and required generated integrity. The existing index was empty. The previous
Eupora commit remains intact at `3ba2728551688cebde869d5c26f5fdc29c8c5956`; no amendment or rewrite is used.

The saved Gnomia project remains the same ID
`132c3923-707a-4873-aa8d-3dabe06a3f95`, label `gnomia`, home
`/Users/jamesryancooper/Projects/plectarium/projects/gnomia`. Catalog status is
`registered_project_home`; `previous_project_id` is history. The existing
voice/rename task cwds remain at the removed old home. Next product work must
start in a fresh task under the corrected saved project. No task is created
by this closeout.

## Validation and preservation

- Both repository harness checks passed after designated refresh.
- Existing tests passed: 47 workspace tests and 15 family tests.
- Family packet validation passed with 0 errors and 0 warnings.
- Workspace historical prompt/state/report integrity passed.
- The live pre-commit topology check reported only dirty workspace/family
  trees; no catalog, registration, path, branch, or origin mismatch.
- All 66 imported DDM files match the original rename baseline, with all
  65 supplied checksum entries passing. In total, 335 DDM source and family
  packet/import files remain unchanged. Gnomia still has no `repo/` or `.git`.
- Earlier accepted decisions, closed tasks/evidence, Eupora's catalog entry,
  and every existing Git-repository catalog entry are preserved. Noerovia
  source or state is modified.

Closeout metadata is followed by a final designated integrity refresh,
read-only harness checks, and exact staging review. The packet itself is not
refreshed because its source and integrity records have not changed.
Review is self-review, not independent assurance. No product code was run and
no dependencies were installed for closeout.

## Post-commit receipt

A commit cannot attest its own hash or the resulting cleanliness. Gnomia's
non-Git `RENAME_CLOSEOUT.md` and `archive/closeout-2026-09-25/` record both exact
commits, their parent/allowlist checks, remaining status, final topology, and
preservation after execution. Those receipts determine actual completion;
this source record attests the reviewed pre-commit state only.

The one-commit allowance is consumed by success. No push, publication, remote
change, Gnomia implementation-repository initialization, or product development
is permitted. The separate kickoff prompt is a handoff, not execution.
