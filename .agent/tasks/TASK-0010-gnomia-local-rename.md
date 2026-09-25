---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0010",
  "title": "Accepted Gnomia design-stage identity",
  "status": "completed",
  "previous_status": "review",
  "authority_basis": "User request in voice task 01a0d97f-ac0f-7d43-b9d6-8f9d40d13e0b on 2026-09-25: implement the finalized Gnomia name change; bounded family/catalog/config updates are authorized. The user accepted responsibility for the manual Codex project and task-path follow-up.",
  "owner": "Gnomia rename task 01a0d98e-2c3a-7533-8123-0534534683fe",
  "created_at": "2026-09-25",
  "updated_at": "2026-09-25",
  "dependencies": [],
  "supersedes": null,
  "closure_evidence": [
    "EVD-0018"
  ],
  "external_effects": "Local recoverable project-home rename and active documentation/catalog/config-path updates only. No commit, push, remote mutation, publication, product execution, new repository, or normative packet promotion.",
  "limitations": [
    "Manual Codex project and existing-task-path update is an acknowledged user-owned follow-up.",
    "Existing Eupora and Noerovia work is uncommitted and must be preserved.",
    "Review will be self-review."
  ]
}
---

## Scope

Apply the current user-authorized Gnomia identity and local navigation changes
in this owning repository. Preserve the normative packet, imported sources,
historical evidence, and unrelated current work. The Gnomia project home moves
from `projects/deliberative-decision-model/` to `projects/gnomia/`.

## Acceptance criteria

- [x] Apply the bounded local identity and navigation changes.
- [x] Run the owning repository's declared checks and preserve source bytes.
- [x] Record the observed app state, accepted user follow-up, and actual limits.

## Validation and recovery

Use `.agent/validators.json`, refreshing only harness integrity with its
designated writer after source freeze. No packet edits require packet refresh.
The Gnomia recovery archive contains the before-state documents, inventory,
and project backup. Reversal is a checked non-overwriting move with targeted
catalog/config reversal; never replace later concurrent work wholesale.

## Closure

EVD-0018 records preservation, executed checks, self-review, and the
acknowledged user-owned app follow-up. The local scope is complete; saved
Codex project/task-path updates remain with the user. Gnomia changes are
uncommitted, with no push or product implementation.
