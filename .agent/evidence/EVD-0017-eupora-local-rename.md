---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0017",
  "title": "Eupora intended identity validation",
  "task": "TASK-0009",
  "recorded_at": "2026-09-25",
  "subject_revision_or_fingerprint": "EUPORA_IDENTITY.md sha256 897831f662569a2c9fda4b4789474ceb5d3e3c0d73375ed2cca8850c0184a90f; local uncommitted tree",
  "result": "pass_scoped_changes_with_live_cleanliness_limitation",
  "fresh_until": null,
  "supersedes": null
}
---

## Method and results

The originating user authorized the rename and both catalog corrections.
Both owner repositories were clean before this task. Fresh source inspection,
Git queries, supported project-list observations, checksums, and relative-link
resolution were used; no remote or product execution was performed.

- Repository harness check: PASS after designated integrity refresh.
- Existing repository tests: 15 passed after refresh; initial integrity-only
  failures were resolved by the writer, with no disabled checks.
- Family packet validator: PASS, 0 errors and 0 warnings.
- Workspace historical prompt/state/report integrity check: PASS.
- Catalog schema and semantic validation: PASS for the Eupora predecessor
  mapping and Noerovia Git-backed entry. Live path/origin/branch metadata matches.
- Five added workspace test cases cover rename/app transitions, invalid
  predecessor paths and active-identity collisions, and exact SSH origins.
- All 35 Eupora imported-package file hashes, the entire existing family
  archive, family packet, and sibling DDM source bytes are unchanged.
- All 26 checked relative links in active overviews and identity/migration
  documents resolve. The former workspace path is absent with no symlink alias.
- The local config retains the same project setting at Eupora's new path;
  unrelated concurrent config additions were preserved.

## Scope and review

Eupora moved from `projects/option-space-model/` to `projects/eupora/`.
Noerovia's existing repository, `main`, SSH origin and owner routes replaced
its stale design-only catalog entry. No Noerovia implementation file was
modified. Its active task was contacted about shared metadata and dirty state.
The family addition is an accepted intended-identity note outside the versioned
packet; no operational member, seed, or shared contract was invented.

Self-review checked the diff, ownership boundaries, source preservation,
negative validator cases, and truthful app status. It is not independent review.
Final source changes are followed by another designated integrity refresh and
read-only checks; final command outcomes are reported in the migration handoff.

## Limitations and external effects

The strict portfolio `--check` reports dirty working trees while this task's
workspace/family changes and Noerovia's active implementation work are in
progress. This is a cleanliness gate, not either prior catalog mismatch; no
checker was weakened to make a working tree appear clean. No global clean
portfolio pass is claimed. Changes are uncommitted for review.

The supported Codex project list still reports saved project
`c9f59fba-755e-4099-8a38-8974ad9f66c2` at the old name/path. The user accepted
the manual update. No app database or conversation log was directly edited,
and existing task working directories have not been changed by a supported API.
No commit, push, remote mutation, publication, deployment, new repository,
qualification, or product implementation occurred in this task.
