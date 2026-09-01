# Plectarium Capability Family Agent Harness

> Routing only; this page grants no permission. Generated from Project
> Blueprint 1.0.0 using the `high-assurance` profile on 2026-08-31, then
> reconciled with project-specific sources, boundaries, commands, and a
> completed local foundation task. Local adoption is complete under
> `TASK-0001`; bounded publication is complete under `TASK-0002`, with its
> closure-commit equality retained as direct post-commit handoff evidence.

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

Generated integrity is expected to be stale during authorized source edits.
Use the packet and harness refresh commands only after source work is frozen,
then finish with the read-only harness check. No publication task is active;
the consumed `TASK-0002` authority cannot authorize implementation or later
pushes.
