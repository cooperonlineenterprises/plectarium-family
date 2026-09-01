---
{
  "schema_version": "harness.checkpoint.v1",
  "id": "CHK-0003",
  "title": "Verity, Titra, and Ortha conventions checkpoint",
  "created_at": "2026-08-31",
  "task": "TASK-0003",
  "source_revision_or_fingerprint": "published capability locks in INPUT-LOCKS.json; local family checkpoint tree",
  "supersedes": null,
  "decision_refs": ["DEC-0001", "DEC-0002"],
  "evidence_refs": ["EVD-0004", "EVD-0005"],
  "limitations": [
    "packet comparison is not implementation equivalence",
    "shared contracts remain at their prior statuses",
    "local checkpoint publication is blocked under TASK-0004"
  ]
}
---

## Anchored outcome

- Result: `INCOMPLETE`.
- Capability source mutations: none.
- Family packet mutations: none.
- Second-wave generation blockers: three.
- Shared-contract stabilization blockers: ten recorded divergences.
- Shared SDK/runtime: deferred; no extraction authorized.
- External effects: none.

Do not resume second-wave packet generation until owner-scoped remediation and
a successor checkpoint resolve the blocking evidence. Resume checkpoint
publication only after explicit authority for one additional normal family
push.
