---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0011",
  "title": "Close Eupora rename registration and scoped local commit",
  "status": "completed",
  "previous_status": "review",
  "authority_basis": "Direct user message 01a0d998-4ddc-79e2-80a7-4851c774ffec in task 01a0d957-6528-7533-8441-6cb23b6221b3: reconcile registration and create scoped local commits; no push, publication, or implementation.",
  "owner": "plectarium-family",
  "created_at": "2026-09-25",
  "updated_at": "2026-09-25",
  "dependencies": [
    "TASK-0009"
  ],
  "supersedes": null,
  "closure_evidence": [
    "EVD-0019"
  ],
  "external_effects": "Exactly one scoped local commit on main in this existing repository; no push, remote modification, publication or implementation.",
  "limitations": [
    "Existing rename task cwds remain stale; future implementation requires a new task in the updated saved project.",
    "Noerovia ongoing work is outside this commit scope."
  ]
}
---

## Scope and authority

Reconcile the verified saved-project update and review this repository's
pending rename changes. The accepted identity and prior decisions are unchanged.
Preserve TASK-0009 and EVD-0017 as dated records. This task is their
cleanup successor, not a rewrite of their observed state.

The user authorizes one local commit in `plectarium-family/repo` on `main`,
subject “Record accepted Eupora design-stage identity”, containing only reviewed rename/catalog files and the
necessary owner evidence and generated integrity. No remote/visibility change,
push, publication, implementation, or Noerovia repository mutation is authorized.
This record narrows current user authority; it does not create a later grant.

## Acceptance and validation

- [x] Verify app/catalog consistency and document exact existing-task limits.
- [x] Preserve imported source bytes and dated prior evidence.
- [x] Review the exact commit allowlist; refresh using designated writers.
- [x] Run required checks and record limits separately from catalog/path errors.

The exact local commit hash and post-commit cleanliness receipt belong in
Eupora's non-Git `RENAME_CLEANUP.md`, because a commit cannot contain its own
hash. No implementation task is created by this cleanup.

Source review and required pre-commit checks are complete. This record is
carried by the authorized local commit; its exact hash and resulting status
are verified afterward in the non-Git cleanup receipt. Review is self-review.
