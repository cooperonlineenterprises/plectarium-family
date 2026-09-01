# Executive Project Definition

## Project identity

- Name: Plectarium Capability Family
- Slug: `plectarium-family`
- Repository: `cooperonlineenterprises/plectarium-family` (private, published
  on `main` under completed `TASK-0002`)
- Definition status: adopted for repository foundation under `DEC-0001`

## Problem

Independent capability repositories need one bounded authority home for the
family constitution and the narrow contracts that allow independently usable,
versioned, and released specialists to interoperate without sharing domain
engines or mutable state.

## Intended outcome

Maintain a versioned, validated family packet that defines family identity,
invariants, architecture, narrow common contracts, conformance fixtures,
relationship graphs, project-generation seeds, and release records while
preserving each capability's semantic and release independence.

## Scope

### In scope

- family charter, invariants, terminology, architecture, and decisions;
- identity, discovery, planning, permission, completion, provenance, durable
  result-reference, and bundle-verification contract surfaces;
- capability seeds, relationship/dependency graphs, schemas, conformance
  fixtures, evaluation criteria, and family release records;
- packet change control, validation, generated integrity, and provenance; and
- repository-local governance, dossier, evidence, and handoff.

### Out of scope

- Plectarium suite product or control-plane implementation;
- capability engines, domain payload semantics, and capability releases;
- a universal runtime, plugin marketplace, or premature shared SDK;
- sibling-repository source imports or shared mutable domain state;
- Octon or another harness's governance responsibilities; and
- product, security, compliance, release, or production-readiness claims based
  only on repository structure.

## Stakeholders and owners

- Operator: supplies current task and external-effect authority.
- Family maintainers: own family constitution and packet change control.
- Capability maintainers: consume and refine family contracts without
  transferring capability semantics into this repository.
- Plectarium maintainers: consume family discovery/contracts while keeping
  suite orchestration separate.
- Reviewers: independently assess contract integrity, provenance, and boundary
  preservation.

## Success measures

- The versioned family packet passes its own structural, schema, reference,
  manifest, and checksum checks.
- Repository-level instructions, harness, dossier, tasks, decisions, evidence,
  and handoff are coherent and resumable.
- Current family sources and historical imports have explicit ownership,
  provenance, and change routes.
- No capability engine or Plectarium suite implementation appears in this
  repository.
- Publication evidence, when executed, is bounded to the exact authorized
  private remote and shows local/tracking/remote equality.

These are repository-foundation measures, not product-readiness measures.
