---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0003",
  "status": "completed",
  "previous_status": "review",
  "title": "Complete the Verity, Titra, and Ortha conventions checkpoint",
  "authority_basis": "current operator instruction for a local read-only family checkpoint",
  "owner": "primary_agent",
  "created_at": "2026-08-31",
  "updated_at": "2026-08-31",
  "dependencies": ["TASK-0002"],
  "source_refs": ["SRC-0004"],
  "decision_refs": ["DEC-0001", "DEC-0002"],
  "supersedes": null,
  "closure_evidence": ["EVD-0004", "EVD-0005"],
  "external_effects": "none; family-local checkpoint records and designated root integrity only",
  "limitations": [
    "no capability or family packet was changed",
    "no network or live remote-ref query was performed",
    "packet comparison is not implemented behavioral compatibility",
    "checkpoint publication is separately blocked under TASK-0004"
  ]
}
---

## Scope

- Lock exact published Verity, Titra, and Ortha repositories and packet bytes.
- Run read-only packet, harness, and mutation checks.
- Compare family/provenance locks, identity, engine and interface ownership,
  discovery, plans, permissions, completion, result references, schemas,
  writers, repository roots, readiness, security, imports, and naming.
- Classify every compared element structurally and by family status.
- Record provisional and unresolved divergence without auto-promotion.
- Keep shared SDK/runtime extraction deferred.

Out of scope: capability or packet edits, implementation, external research,
network access, Git commits/pushes, family contract promotion, or SDK/runtime
creation.

## Acceptance criteria

- [x] All three published inputs are exact, clean, validated, and immutable.
- [x] Five required checkpoint artifacts exist and validate structurally.
- [x] Every matrix row has one structural classification and one family status.
- [x] Divergences have dispositions; three second-wave blockers and ten
      shared-contract stabilization blockers are explicit.
- [x] No status is promoted by similarity.
- [x] Shared runtime/SDK remains deferred.
- [x] Evidence, independent review, checkpoint, limitations, and external
      effects are recorded.

## Validation and handoff

The final family packet remains byte-identical. Root harness/dossier integrity
is refreshed only after these records freeze, then packet, harness, and
mutation checks are rerun. Local checkpoint completion does not authorize
publication. `TASK-0004` records the exact blocked publication need.
