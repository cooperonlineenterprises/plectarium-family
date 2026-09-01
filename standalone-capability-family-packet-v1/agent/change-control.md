# Family Architectural Change Control

## Changes requiring a family ADR

- family invariants or authority hierarchy;
- shared permission semantics;
- top-level completion meaning;
- imported-evidence preservation;
- result-envelope or manifest stabilization;
- interface authority behavior;
- shared capability classes becoming normative;
- extraction of an SDK/runtime/framework/registry;
- Octon provider-class semantics;
- addition of an action-capable rather than evidence-only family member.
- canonical `family_id`, portfolio source ownership, or suite/family boundary;
- exact character-to-repository mapping;

## Canonical identity supersession

The character mapping and no-alias rule established by `FAM-034` and `spec/canonical-character-identities.md` may change only through an explicit successor family architecture decision with identity, product, routing, compatibility, migration, and authority analysis. A change that also affects a family invariant requires a family ADR.

The canonical family identifier, Plectarium relationship, source-ownership
map, and character repository mapping established by `FAM-035`, `FAM-036`,
and `ADR-013` require the same successor-decision discipline. Downstream
consumers must migrate by immutable family version/commit rather than editing a
forked canonical contract.

## Process

```text
detect conflict or repeated need
        ↓
collect implementation evidence
        ↓
state capability-specific impact
        ↓
propose alternatives and migration
        ↓
architecture + security review
        ↓
accept/reject ADR
        ↓
update all normative and generated artifacts
        ↓
revalidate affected capability projects
```

Convenience, code reuse, or aesthetic uniformity alone are insufficient evidence for a shared abstraction.
