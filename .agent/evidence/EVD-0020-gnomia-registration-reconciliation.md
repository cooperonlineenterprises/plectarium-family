---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0020",
  "title": "Verified Gnomia saved project and unchanged existing task paths",
  "task": "TASK-0010",
  "recorded_at": "2026-09-25",
  "subject_revision_or_fingerprint": "Supported project 132c3923-707a-4873-aa8d-3dabe06a3f95 and direct reads of voice/rename task cwd metadata after the user update",
  "result": "pass_saved_project_observation_with_existing_task_cwd_limitation",
  "fresh_until": null,
  "supersedes": null
}
---

## Successor observation

The user reported completion of the previously agreed manual saved-project
update. Supported `list_projects` inspection confirms the same local, non-Git
project ID `132c3923-707a-4873-aa8d-3dabe06a3f95`, now labeled `gnomia` at
`/Users/jamesryancooper/Projects/plectarium/projects/gnomia`.

Supported `read_thread` inspection confirms that voice task
`01a0d97f-ac0f-7d43-b9d6-8f9d40d13e0b` and rename task
`01a0d98e-2c3a-7533-8123-0534534683fe` still report the former
`projects/deliberative-decision-model` cwd. Next product work must start in a
fresh task under the corrected project and verify its working directory.
No task was created or retargeted by this follow-up.

The Gnomia catalog now records `registered_project_home` with current and
desired paths `projects/gnomia`; only Gnomia is removed from the stale-design
index. The predecessor ID remains historical context. Eupora and Noerovia
records retain their existing values.

This succeeds only the earlier app-registration observation; earlier naming,
rename tasks, integrity evidence, and archived pre-update app data are not
rewritten. Accepted intent and design-stage maturity are unchanged. The
successor receipt is Gnomia's
`archive/rename-2026-09-25/app-observation-registered.json`.

## Focused validation and scope

This is a bounded status reconciliation under the completed rename task,
not a change to accepted intent. Source freeze is followed by the designated
harness integrity writer and read-only checks. Workspace catalog/topology,
configured workspace tests, local links, and preservation checks are scoped
to this change; exact executed results are in Gnomia's
`archive/rename-2026-09-25/registration-verification.json`.

The strict portfolio cleanliness gate may still report existing uncommitted
owner work. Imported DDM sources, the family packet, prior archives, code,
and schemas remain untouched. No product runtime or packet test rerun,
implementation, new task, commit, push, publication, or app database mutation
is included. The original tasks' historical closure records are retained.
