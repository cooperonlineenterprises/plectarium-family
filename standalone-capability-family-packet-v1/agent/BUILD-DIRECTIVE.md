# AI-Team Build Directive for the Capability Family

This repository is an architectural authority and project-generation substrate, not a capability implementation monorepo.

## Governing workflow

```text
understand the family boundary
        ↓
identify established vs provisional authority
        ↓
work within one declared family or capability surface
        ↓
produce evidence for every claimed improvement
        ↓
surface cross-authority conflicts
        ↓
validate the whole packet
```

## Primary mission

- keep the harness small and specialist capabilities strong;
- preserve the established canonical character identities and their no-alias, no-authority-expansion rules;
- preserve `family_id: standalone-capability-family`, exact character repository mappings, and downstream family commit/manifest/seed-path provenance requirements;
- preserve independent usability and evidence-not-authority;
- give every future project a substantive, safe seed and generation prompt;
- learn from real capability implementations rather than inventing a platform;
- maintain machine-readable relationships and validation.

## Do not do

- implement capability engines here;
- create a shared capability SDK/runtime;
- silently promote v0 conventions;
- copy UCA domain semantics into unrelated seeds;
- add action authority to evidence capabilities;
- claim conversation coverage or validation not actually achieved;
- invent alternate character names or silently replace descriptive machine identifiers with character names;
- copy third-party skill/source text without deliberate license compliance.

## Project-generation protocol

1. Select `capabilities/<id>/PROJECT-GENERATION-PROMPT.md`.
2. Supply this family packet and the capability seed to a fresh generation agent.
3. Require primary-source research and source/license verification.
4. Generate a separate repository build packet with capability-specific constitution, specifications, schemas, task graph, skills, evaluation, and release criteria.
5. Validate it independently.
6. Record any conflict with family provisional conventions as evidence for a family ADR.

## Completion claim

An agent may say a family change is complete only after the validator passes, manifest/checksums are refreshed, relationship and ID checks pass, and the internal consistency review is updated for material architecture changes.
