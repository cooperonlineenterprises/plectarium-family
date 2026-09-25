---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0018",
  "title": "Gnomia local rename and identity validation",
  "task": "TASK-0010",
  "recorded_at": "2026-09-25",
  "subject_revision_or_fingerprint": "GNOMIA_IDENTITY.md sha256 ddb77bc113176a111ccf4e1f437e157838e45d86676d3beb48d3fb8c311d0b70; local Gnomia changes remain uncommitted",
  "result": "pass_scoped_changes_with_live_cleanliness_limitation",
  "fresh_until": null,
  "supersedes": null
}
---

## Method and results

The user explicitly authorized the Gnomia rename and accepted the manual
Codex project/task-path follow-up. The project moved from
`projects/deliberative-decision-model/` to `projects/gnomia/` without an alias.
Before-state documents and inventories are retained in Gnomia's
`archive/rename-2026-09-25/`; its `RENAME_MIGRATION.md` records exact mappings.

- This repository's harness check passed after its designated refresh.
- This repository's existing tests passed: 15 tests.
- Family packet validation passed with 0 errors and 0 warnings.
- Workspace historical prompt/state/report integrity passed.
- All 66 DDM source files retained their names, sizes, and SHA-256 hashes;
  all 65 supplied checksum entries passed. Only the project's two intended
  active documents changed among the 69 original files.
- All 269 existing family packet/import files retained their bytes.
- The checked migration/identity/navigation documents' local links resolved.
- The local config changed only the old project-path header to the new one;
  reversing that header reproduces its complete pre-edit hash.
- The strict workspace topology check found only uncommitted owner changes;
  no path, catalog, schema, origin, or branch mismatch was reported.

## Concurrent work and review

Eupora and Noerovia work was already present. During this task, the separate
Eupora cleanup verified its saved-project registration and performed its own
user-authorized scoped local commits. A coordinated no-write window kept
Gnomia changes out of those commits and preserved the combined working trees.
The Eupora registration update is attributed to its owning cleanup task;
Gnomia did not restore stale Eupora metadata or change Noerovia code.

Self-review inspected the bounded changes, preservation checks, local links,
authority boundaries, and remaining app state. It is not independent review.
Final state/evidence edits are followed by a designated integrity refresh and
read-only harness checks; those exact outcomes are recorded in the Gnomia
migration handoff. No packet refresh is needed because packet bytes did not
change.

## Limits and effects

The supported Codex list still reports project
`132c3923-707a-4873-aa8d-3dabe06a3f95` at the old label/path; supported task
reads still report the old cwd for the voice and rename tasks. The available
API cannot update those paths and computer use disallows control of Codex.
The user accepted this manual follow-up. Commands after relocation use an
explicit valid new workdir; saved task metadata has not been changed.

Gnomia remains design-only and unpromoted. Its identity note does not admit
a normative packet member or establish implementation, qualification,
contract publication, or release. This Gnomia task makes no commit, push,
remote mutation, deployment, product execution, or publication. A globally
clean portfolio is not claimed; Gnomia changes remain local for review.
