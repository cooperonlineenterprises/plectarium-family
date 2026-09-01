# Requirements and Constraints

## Active requirements

- `REQ-0001` — Preserve the family authority boundary.
- `REQ-0002` — Preserve independent capability semantics and narrow shared
  contracts.
- `REQ-0003` — Preserve canonical identity-source provenance and bytes.
- `REQ-0004` — Keep repository-foundation work implementation-free.
- `REQ-0005` — Validate and refresh integrity through designated commands.

The authoritative structured definitions, bases, owners, and validation
methods are in `../machine-readable/requirements.json`.

## Proposed requirements

No additional repository-level requirement is currently proposed. Packet
requirements and provisional contracts retain their statuses in the packet;
this dossier does not silently promote them.

## Hard boundaries

- The dossier does not grant permission.
- Current-state claims require direct evidence.
- Unknown project facts remain unknown.
- Real secrets and unnecessary personal data do not belong in the dossier.
- The repository must not implement suite or capability-domain behavior.
- Sibling source imports and shared mutable domain state are prohibited.
- Generated integrity may be written only by the designated packet or harness
  writer after source edits are frozen.
- Remote effects remain exact, private, consumable, and task-scoped; this
  dossier cannot grant them.
