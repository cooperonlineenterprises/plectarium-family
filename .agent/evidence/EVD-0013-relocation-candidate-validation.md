---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0013",
  "title": "Relocated family repository candidate validation",
  "task": "TASK-0008",
  "recorded_at": "2026-09-15",
  "subject_revision_or_fingerprint": "pre-evidence source fingerprint 90293e55ead3c8d1547aadd7766835aa46f12968d3cc4fcac5d565cf897dd331; exact candidate commit pending",
  "result": "pass_pending_independent_review",
  "fresh_until": null,
  "supersedes": null
}
---

From `/Users/jamesryancooper/Projects/plectarium/repos/plectarium-family`:

- the family packet validator passed with zero errors and warnings;
- the harness and dossier structural check passed;
- all 15 mutation tests passed;
- the designated harness integrity refresh completed and the following
  read-only check passed;
- strict JSON parsing and `git diff --check` passed;
- the family packet source and generated packet integrity did not change;
- the checkout retained the expected remote and independent Git boundary.

The tracked packet command uses the explicit
`PLECTARIUM_PACKET_PYTHON` binding with a `python3` fallback; the current local
binding selected Python 3.14 with pre-existing PyYAML and jsonschema. No
dependency was installed. No push, remote mutation, publication, deployment,
or product action occurred.

Adding this evidence and updating task routing necessarily changes the harness
source fingerprint. The designated refresh and final read-only checks are run
again after this record; independent review binds the exact committed
candidate and reports any discrepancy.
