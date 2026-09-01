---
{
  "schema_version": "harness.decision.v1",
  "id": "DEC-0002",
  "status": "accepted",
  "previous_status": "proposed",
  "title": "Record packet convergence without promoting shared contracts or extracting a runtime",
  "created_at": "2026-08-31",
  "authority_source": "current operator three-capability checkpoint instruction",
  "source_refs": ["SRC-0004"],
  "supersedes": null,
  "successor": "DEC-0003"
}
---

## Context

Published Verity, Titra, and Ortha packets demonstrate common outer meanings
and intentional domain differences. They do not demonstrate three implemented
engines, stable shared code, migration cost, or lower total complexity from an
extracted runtime.

## Decision

Accept the local checkpoint outcome `INCOMPLETE`.

- Preserve all existing family statuses.
- Do not promote the shared manifest, result-reference shape, permission
  vocabulary, lifecycle, capability classes, evidence-class tokens, or schema
  namespace policy.
- Treat Verity's missing packet-local family 1.2.0 lock, machine identity tuple,
  governed writer/readiness projections, and structured generic
  result-reference projection as blocking checkpoint evidence gaps.
- Treat reused relative schema IDs and missing native-reference-to-import
  enrichment contracts as blocking cross-packet ambiguities.
- Keep second-wave packet generation blocked pending owner-scoped remediation
  and a successor checkpoint.
- Keep `FAM-028` and every shared SDK/runtime/package/schema-binding
  extraction deferred.
- Require a later implementation-backed family ADR before any extraction.

This decision records checkpoint disposition only. It does not change the
family packet, capability semantics, permissions, implementation state, or
publication authority.

## Reconsideration

A successor requires implemented multi-capability evidence, independently
versioned compatibility ownership, migrations, conformance tests,
capability-specific extension support, and proof that extraction reduces total
complexity.
