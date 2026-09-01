# AI-Team Authority Model

## Authority hierarchy

```text
Family Constitution
       ↓
Family Invariants
       ↓
Canonical Character Identities
       ↓
Shared Provisional Contracts
       ↓
Capability Constitution
       ↓
Capability Invariants
       ↓
Capability Normative Specifications
       ↓
Accepted ADRs
       ↓
Capability Matrix / Release Criteria
       ↓
Workstream Plans
       ↓
Task Instructions
       ↓
Agent Implementation Choices
```

An agent MUST surface a conflict with higher authority. It may propose an ADR; it may not silently redefine evidence, completion, authority, permissions, imported-result provenance, or capability boundaries.

## Family packet work

Family-level agents may:

- clarify seeds while preserving statuses;
- verify source and licensing information;
- improve project-generation prompts;
- add evaluation fixtures and validators;
- record new evidence from real capability implementations;
- propose promotion or rejection of provisional conventions.

They preserve the established mapping in `spec/canonical-character-identities.md`, use no alternate character names, and keep character identity separate from machine-facing IDs and authority.

They may not implement shared runtimes, capability engines, marketplaces, or SDKs inside the family packet.

## Capability project work

Capability-generation agents inherit family authority but own domain-specific architecture. They should challenge provisional conventions when the domain provides evidence, then record the conflict rather than conform mechanically.
