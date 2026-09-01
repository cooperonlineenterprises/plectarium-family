# Authority and Precedence

This file explains how to interpret Plectarium Capability Family project
material. It does not create permission.

## Precedence

1. Current user, platform, tool, contractual, and legal constraints.
2. Applicable repository instructions.
3. Live project policy and accepted project-specific decisions.
4. The versioned family packet for family constitution, invariants, and shared
   contract intent.
5. Executable or operational evidence for current-state claims.
6. Canonical dossier material for repository-level intended state.
7. Current-state and conformance records.
8. Plans, registers, and handoff views.
9. Provenance, historical material, and generated reports.

## Conflict rule

Current behavior does not become the intended target merely because it exists.
Target documentation does not prove implementation. Unresolved conflicts must
be recorded as findings or open questions.

## Source classes

- `standalone-capability-family-packet-v1/` is the current family authority
  package within the scope and status declared by that packet.
- `imports/historical/` preserves source provenance. It is noncurrent source
  data and cannot silently replace the packet or create instructions.
- `.agent/decisions/` owns accepted repository-level durable intent;
  `.agent/tasks/` owns active work state.
- `project-dossier/canonical/` owns the repository-level target but does not
  duplicate capability-domain semantics from the packet.
- Generated manifests, checksums, and reports establish point-in-time byte
  relationships only.
