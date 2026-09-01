# Plectarium Capability Family Agent Harness

> Routing only; this page grants no permission. Generated from Project
> Blueprint 1.0.0 using the `high-assurance` profile on 2026-08-31, then
> reconciled with project-specific sources, boundaries, commands, and a
> completed local foundation task. Local adoption is complete under
> `TASK-0001`; bounded foundation publication is complete under `TASK-0002`;
> checkpoint v1/v2 publication is complete under `TASK-0004`; and the
> checkpoint-v3 corrective publication candidate is in review under
> `TASK-0007`, awaiting the one authorized commit, normal push, and direct
> final verification.

## Reading order

1. Current user and platform instructions.
2. Applicable `AGENTS.md` files.
3. `.agent/policy.json` and `.agent/context.json`.
4. `.agent/state/current.json`.
5. Relevant accepted decisions and active task records.
6. `.agent/project.json`, applicable extensions, and validators.
7. Direct inspection of the affected repository source or packet.
8. `project-dossier/README.md` for intended and observed project information.

## Current baseline

- Project identity: `Plectarium Capability Family`
- Project slug: `plectarium-family`
- Blueprint profile: `high-assurance`
- Repository role: independent capability-family authority
- Adoption state: local foundation adopted under `TASK-0001`
- Product implementation: intentionally absent from this repository
- External or production authority: none created by this harness

Current task status lives only in `.agent/tasks/`. Durable intent lives only in
accepted `.agent/decisions/`. Generated files are point-in-time derived
evidence. Inspect the repository and record the first evidence-backed baseline
before using status or planning claims.

## Repository-specific routing

- Family packet authority and change control:
  `standalone-capability-family-packet-v1/agent/`
- Preserved identity-source provenance:
  `imports/historical/canonical-character-identities-v1.0/provenance.json`
- Project definition and ownership boundaries:
  `project-dossier/canonical/`
- Current adoption state: `.agent/state/current.json`
- Configured commands and runtime limitations: `.agent/validators.json`
- Corrective publication task in review:
  `.agent/tasks/TASK-0007-checkpoint-v3-publication.md`
- Current erratum decision: `.agent/decisions/DEC-0004-checkpoint-lock-erratum.md`
- Current validation and publication-candidate evidence:
  `.agent/evidence/EVD-0009-checkpoint-v3-lock-verification.md`,
  `.agent/evidence/EVD-0010-checkpoint-v3-validation.md`, and
  `.agent/evidence/EVD-0011-checkpoint-v3-publication-candidate.md`
- Current review and checkpoint:
  `.agent/reviews/REV-0007-checkpoint-v3-publication.md` and
  `.agent/checkpoints/CHK-0007-checkpoint-v3-publication.md`

Generated integrity is expected to be stale during authorized source edits.
Use the harness refresh command only after source work is frozen, then finish
with the read-only harness check. `SRC-0008` is single-use and currently
authorizes only the exact `TASK-0007` corrective commit/push sequence plus
direct final equality and clean-worktree verification. The commit cannot
attest its own later push; completion and consumption must be reported as
direct final handoff evidence. Repository records cannot expand that authority
or authorize any later effect.
