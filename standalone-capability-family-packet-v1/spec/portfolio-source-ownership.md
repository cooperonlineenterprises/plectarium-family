# Portfolio Source Ownership

**Status:** `ESTABLISHED`  
**Authority:** Family-level ownership boundary  
**Decision:** `FAM-035`; `ADR-013`

## Ownership map

| Owner | Authoritative for | Explicitly not authoritative for |
| --- | --- | --- |
| Plectarium suite repository | suite product semantics, catalog/control-plane contracts, supported-version bill of materials, runner coordination, suite security/evaluation/operations | capability-domain conclusions or algorithms; family invariants; harness authority |
| Family repository | family charter, invariants, `family_id`, character registry, provisional shared contracts, capability seeds, relationship graphs, family conformance and change control | Plectarium implementation; capability engines; suite bill of materials; project authority |
| Each capability repository | its domain engine, capability payload schemas, interfaces, adapters, evaluation, security model, release contract and version lifecycle | portfolio orchestration; sibling source; mutable family authority; downstream action authority |
| Workspace repository | desired local checkout map, safe bootstrap diagnostics, observed setup/publication state, portfolio report | product truth; compatibility guarantees; implementations; credentials; replayable GitHub authority |
| Octon or another harness | trust, project policy, invocation governance, evidence routing and separately authorized downstream action | capability-domain semantics; Plectarium product semantics; family contract ownership |

## Relationship rules

- The formal suite brand is **Plectarium**, not “Octon Plectarium.”
- “Part of the Octon ecosystem” is a product relationship, not a runtime
  dependency, inheritance rule, or authority transfer.
- Plectarium is not an eleventh family capability.
- No repository may duplicate a mutable fact it does not own. A consumer may
  reference or pin an immutable family commit, packet version, manifest digest,
  or durable result reference.
- Plectarium may support additional families. Its catalog therefore consumes
  the full `(family_id, capability_id, version)` identity rather than assuming
  that this family or its initial ten members is the permanent universe.
- A transport or integration surface cannot strengthen authority.

## Shared runtime threshold

A shared protocol SDK or runtime remains deferred until Verity, Titra, and
Ortha demonstrate materially equivalent implemented semantics and a later
accepted family ADR authorizes extraction. This packet defines contracts and
generation inputs, not a runtime, registry service, marketplace, or plugin
framework.
