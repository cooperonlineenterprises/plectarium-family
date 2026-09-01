# Standalone Capability Pattern

A standalone capability is a real domain product, not a plugin callback or prompt collection.

```text
Standalone Capability
│
├── Domain Engine
├── Canonical CLI
├── Durable Result Contract
├── Capability Manifest
├── Evidence / Completion Semantics
├── Specialist Adapters
├── Agent Skill
├── MCP / CI / OCI Interfaces
├── Harness Provider Adapter
└── Optional Future Service
```

## Qualification criteria

Standalone status is justified when several conditions hold:

- deep domain logic or specialist tooling;
- independent utility outside a harness;
- meaningful evidence and completion semantics;
- significant permissions or execution isolation;
- long-running or resource-intensive work;
- independent version/release lifecycle;
- reusable value across projects;
- substantial evaluation and security burden.

A small helper, formatter, one-project script, or thin adapter should not be promoted into a product without evidence.

## Extraction discipline

```text
Build UCA
  → observe real outer conventions
  → build Verification Assurance
  → compare differences and duplication
  → build Specification Conformance
  → stabilize only what survives all three
```

Common code is not automatically a common semantic contract. Prefer local duplication to a premature abstraction when capability meanings are still evolving.
