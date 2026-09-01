# Architecture or Outcome Model

## Context

This repository is one authority plane in a multi-repository portfolio. It
defines family-level contracts while keeping suite orchestration, capability
semantics, developer bootstrap, and harness governance in their independent
homes.

## Actors and stakeholders

- family maintainers and reviewers;
- independent capability repository maintainers;
- Plectarium suite maintainers;
- workspace/bootstrap maintainers; and
- automation that validates or consumes version-pinned packet artifacts.

## Components, capabilities, or workstreams

| Component | Role | Authority boundary |
|---|---|---|
| `standalone-capability-family-packet-v1/` | Versioned family constitution, contracts, seeds, schemas, graphs, and release records | Family-level intent only |
| `imports/historical/` | Preserved source bytes and provenance | Historical data; no instruction or permission |
| `.agent/` | Repository-local governance and current work | Inherits current higher authority; cannot create it |
| `.agents/` | Constrained review/change capabilities | May narrow the active task only |
| `project-dossier/` | Intended/current/conformance/plan/provenance separation | Documentation only |
| sibling repositories | Suite, capability, and workspace ownership planes | No source imports or shared mutable domain state |

## Boundaries and invariants

- Plectarium is the suite, not a capability and not this repository.
- Plectarium is part of the Octon ecosystem; its formal brand is not prefixed
  with “Octon.”
- Each capability remains independently usable, versioned, releasable, and
  callable through its canonical CLI without Plectarium, Octon, MCP, AI, or a
  hosted service.
- Each capability owns one semantic engine; projections and adapters remain
  thin.
- Common family contracts stay narrow; domain payloads remain
  capability-specific.
- Cross-capability consumption uses immutable durable-result references rather
  than sibling imports, shared domain tables, or in-process engine coupling.
- A shared SDK remains deferred until at least Verity, Titra, and Ortha show
  materially equivalent semantics and a later ADR authorizes extraction.
- Transport choice never expands authority.

## Relationships and flows

```text
historical sources -> provenance -> family packet -> versioned contract/seed
                                              |-> capability repositories
                                              |-> Plectarium catalog/control plane
                                              |-> workspace compatibility views
```

Consumers pin immutable packet or release identities. They do not treat a
mutable sibling checkout as a production compatibility guarantee.

## Open design decisions

- Portable packet-validator dependency bootstrap remains unresolved; the
  adoption host currently uses a preconfigured Python 3.14 runtime.
- Shared protocol SDK extraction remains deferred to the three-capability
  conventions checkpoint and a separate accepted ADR.
- Any additional common contract surface requires packet change control and
  evidence that it is truly cross-domain.
