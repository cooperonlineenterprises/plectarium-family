---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0005",
  "title": "Three-capability contract comparison and divergence classification",
  "task": "TASK-0003",
  "source_refs": ["SRC-0004"],
  "recorded_at": "2026-08-31",
  "subject_revision_or_fingerprint": "three-capability-conventions-v1 artifacts under project-dossier/conformance",
  "result": "incomplete_with_blocking_divergence",
  "fresh_until": null,
  "supersedes": null
}
---

## Result

Thirty contract elements were classified with one structural class and one
family status. Engine ownership, completion, repository, security-boundary,
and no-action invariants pass, but FAM-036 packet identity/provenance evidence
is missing for Verity.

Thirteen divergences were recorded. They include missing legacy Verity family-lock
and structured result-reference evidence, permission/evidence token drift,
completion/schema-ID shape differences, and validator runtime portability.
Three block second-wave packet generation; ten block stabilization of affected
shared contracts.

The outcome is `INCOMPLETE`. No status was promoted.
No shared runtime, SDK, package, binding, or source extraction was created or
authorized.

## Limitations

This is published packet/foundation evidence only, not implemented behavioral
equivalence or product readiness.
