---
{
  "schema_version": "harness.decision.v1",
  "id": "DEC-0001",
  "status": "accepted",
  "previous_status": "proposed",
  "title": "Adopt the family repository boundary and high-assurance harness posture",
  "created_at": "2026-08-31",
  "authority_source": "authority:current-operator-plectarium-portfolio-setup-v2",
  "source_refs": ["SRC-0001", "SRC-0003"],
  "supersedes": null,
  "successor": null
}
---

## Context

The family constitution and shared contracts affect multiple independently
versioned capability repositories. Foundation work spans multiple sessions and
concurrent agents, preserves consequential source provenance, and includes a
tightly bounded remote-publication sequence. A generic generated baseline does
not define the repository's actual ownership or security posture.

## Decision

Adopt this repository as the independent authority home for the capability
family constitution, invariants, narrow interoperability contracts, schemas,
conformance fixtures, relationship graphs, generation seeds, and family
release records.

Use the Project Blueprint 1.0.0 `high-assurance` profile because cross-project
impact, concurrent work, provenance, auditability, integrity recovery, and
external-effect gates are material. Treat the generated snapshot as a
project-local structure that is being adopted through `TASK-0001`, not as a
source of project facts, permission, approval, or readiness.

Maintain these ownership boundaries:

- the family packet owns family-level normative and provisional contracts;
- Plectarium's separate repository owns the suite product and optional control
  plane;
- each capability repository owns its one authoritative semantic engine and
  domain payloads;
- the workspace repository owns non-authoritative developer bootstrap and
  portfolio-status views; and
- Octon and other harnesses retain their own governance responsibilities.

The repository must not contain capability engines, suite implementation, a
universal runtime, a plugin marketplace, sibling source imports, or shared
mutable domain state. Generated harness policy and the dossier remain
non-authorizing and may only record or narrow current higher authority.

## Consequences

- Benefits: one explicit family authority boundary; reproducible source and
  integrity evidence; safe multi-session handoff; less cross-repository drift.
- Costs: task, decision, evidence, review, refresh, and source-provenance
  discipline are required for material changes.
- Risks: repository-local integrity remains self-attested; independent remote
  controls and review are still required where warranted.
- What remains undecided: whether a shared protocol SDK will ever be extracted;
  that remains deferred until the evidence threshold and a later ADR are met.

## Validation and rollback

- Evidence: `EVD-0001` records current structure, runtime, and byte-identity
  observations; final adoption evidence will be added only after execution.
- Reversal or successor path: materially changing the family ownership or
  harness posture requires a successor decision that preserves this record.
