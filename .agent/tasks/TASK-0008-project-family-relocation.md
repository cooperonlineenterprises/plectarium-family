---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0008",
  "status": "completed",
  "previous_status": "review",
  "title": "Adopt the relocated Plectarium project-family workspace",
  "authority_basis": "Current operator request dated 2026-09-15 for local Plectarium architectural remediation and workspace migration",
  "owner": "primary_agent",
  "created_at": "2026-09-15",
  "updated_at": "2026-09-15",
  "dependencies": [],
  "supersedes": null,
  "closure_evidence": ["EVD-0013"],
  "external_effects": "Local non-overwriting filesystem relocation, tracked host-neutral command updates, validation, commits, and review only; no push or other remote effect.",
  "limitations": [
    "This task does not alter the family packet, shared-contract status, capability semantics, product implementation, or readiness.",
    "Historical task, evidence, receipt, review, and checkpoint bytes are preserved.",
    "Codex application registration is outside repository authority and may require a supported manual action."
  ]
}
---

## Scope

- Preserve the independent family authority boundary while its canonical
  checkout moves to `repos/plectarium-family`.
- Replace current committed workstation interpreter paths with an explicit
  local binding and host-neutral tracked commands.
- Replace stale current routing with a successor view while preserving
  historical publication records byte-for-byte.
- Refresh only designated generated integrity after source freeze.

## Acceptance

- Repository identity, history, remote, immutable packet bytes, and refs are
  unchanged by relocation.
- Packet, harness, mutation, JSON, link, integrity, and `git diff --check`
  validation pass on the exact candidate.
- An independent T1 reviewer approves the exact committed source candidate.
- No external action occurs and the repository remains independently usable.

## Candidate handoff

Independent review `REV-0008` approved the exact source candidate. Final
closure adds only the review record, task/current routing, and designated
generated integrity; the resulting evidence-bearing head requires a final
read-only review before integration.
