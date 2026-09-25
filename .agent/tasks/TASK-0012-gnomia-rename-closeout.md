---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0012",
  "title": "Close Gnomia rename and prepare scoped local commit",
  "status": "completed",
  "previous_status": "review",
  "authority_basis": "Current user closeout instruction delegated from voice task 01a0d97f-ac0f-7d43-b9d6-8f9d40d13e0b on 2026-09-25 authorizes one scoped local Gnomia rename/registration commit in each existing owner repository; pushes, publication, implementation-repository initialization, and product development are forbidden.",
  "owner": "plectarium-family",
  "created_at": "2026-09-25",
  "updated_at": "2026-09-25",
  "dependencies": [
    "TASK-0010"
  ],
  "supersedes": null,
  "closure_evidence": [
    "EVD-0021"
  ],
  "external_effects": "Exactly one scoped local commit on main in plectarium-family/repo. No push, publication, remote mutation, repository initialization, or implementation.",
  "limitations": [
    "Existing task cwds remain stale; next product work requires a fresh task in the corrected Gnomia saved project.",
    "Self-review; exact commit and post-commit status require the non-Git receipt."
  ]
}
---

## Scope and current authority

Close the already accepted Gnomia rename and verified saved-project
registration in this owning repository. Preserve the earlier naming decision,
rename tasks/evidence, Eupora commits and current registration, Noerovia, and
all historical source and packet bytes.

The current user request permits exactly one local commit on `main` in
`plectarium-family/repo`, subject “Record accepted Gnomia design-stage identity”, containing only the reviewed
Gnomia files below. This records and narrows the current instruction; it does
not grant later commit or remote authority. No push, publication, remote
change, Gnomia implementation-repository initialization, or product work.

## Acceptance and validation

- [x] Review the exact pending Gnomia source and staging scope.
- [x] Preserve the DDM import, family packet, prior evidence, and sibling work.
- [x] Validate the frozen source with designated writers and required checks.
- [x] Prepare the scoped local commit and non-Git post-commit receipt handoff.

## Exact commit allowlist

- `.agent/context.json`
- `.agent/decisions/DEC-0006-gnomia-local-identity.md`
- `.agent/evidence/EVD-0018-gnomia-local-rename.md`
- `.agent/evidence/EVD-0020-gnomia-registration-reconciliation.md`
- `.agent/evidence/EVD-0021-gnomia-rename-closeout.md`
- `.agent/generated/manifest.json`
- `.agent/generated/validation-report.json`
- `.agent/state/current.json`
- `.agent/tasks/TASK-0010-gnomia-local-rename.md`
- `.agent/tasks/TASK-0012-gnomia-rename-closeout.md`
- `GNOMIA_IDENTITY.md`
- `README.md`
- `project-dossier/CHECKSUMS.sha256`
- `project-dossier/MANIFEST.json`

## Receipt and limitations

This repository record covers source review and pre-commit checks. A commit
cannot attest its own hash or post-commit status. The exact local commit,
remaining status, and final topology observations will be verified after the
commit in Gnomia's non-Git `RENAME_CLOSEOUT.md`. The overall cleanup is not
complete until both receipts are verified there.

Existing Gnomia voice and rename tasks retain the former working directory;
next product work requires a fresh task under the corrected saved project.
No implementation task is created during closeout. Review is self-review.


Source review, required checks, and the 14-file commit allowlist are complete.
The final metadata is followed by designated integrity refresh and exact-tree
checks. The authorized commit carries this source record; the overall
closeout is completed only after its non-Git post-commit receipt is verified.
