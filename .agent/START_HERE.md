# Plectarium Capability Family Agent Harness

> Routing only; this page grants no permission. Generated from Project
> Blueprint 1.0.0 using the `high-assurance` profile on 2026-08-31, then
> reconciled with project-specific sources, boundaries, commands, and a
> completed local foundation task. Local adoption is complete under
> `TASK-0001`; bounded foundation publication is complete under `TASK-0002`;
> checkpoint v1/v2 publication is complete under `TASK-0004`; direct
> verification closed the checkpoint-v3 corrective publication under
> `TASK-0007`; project-family relocation source and local-main integration are
> complete under `TASK-0008`, `REV-0009`, and `EVD-0016`. No current push
> authority exists.

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
- Completed local integration task:
  `.agent/tasks/TASK-0008-project-family-relocation.md`
- Current erratum decision: `.agent/decisions/DEC-0004-checkpoint-lock-erratum.md`
- Preserved checkpoint-v3 validation and publication-candidate evidence:
  `.agent/evidence/EVD-0009-checkpoint-v3-lock-verification.md`,
  `.agent/evidence/EVD-0010-checkpoint-v3-validation.md`, and
  `.agent/evidence/EVD-0011-checkpoint-v3-publication-candidate.md`
- Preserved review and checkpoint:
  `.agent/reviews/REV-0007-checkpoint-v3-publication.md` and
  `.agent/checkpoints/CHK-0007-checkpoint-v3-publication.md`

Generated integrity is expected to be stale during authorized source edits.
Use the harness refresh command only after source work is frozen, then finish
with the read-only harness check. `SRC-0008` is consumed historical authority;
the current relocation authorizes local, recoverable workspace changes only.
Repository records cannot authorize a later push or any broader effect.
