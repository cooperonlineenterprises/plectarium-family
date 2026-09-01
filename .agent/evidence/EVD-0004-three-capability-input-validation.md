---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0004",
  "title": "Published Verity, Titra, and Ortha input validation",
  "task": "TASK-0003",
  "source_refs": ["SRC-0004"],
  "recorded_at": "2026-08-31",
  "subject_revision_or_fingerprint": "Verity 271dde603f4c35ba4c0b051365ba66efdba7a370; Titra 58cfe8388d267bb4d0c746aff8c7d6dfceb2e8bb; Ortha daeaa7ee8e32c64af6337d7e2f8701bb0727e16a",
  "result": "pass_with_runtime_limitation",
  "fresh_until": null,
  "supersedes": null
}
---

## Method and result

- Verified each local root, `main`, HEAD, `origin/main`, exact origin URL,
  and clean worktree without network.
- Verified all six packet manifest/checksum digests.
- Titra and Ortha packet/harness checks passed; each mutation suite passed
  15/15.
- Verity exact-byte safe preflight, setup check, harness check, and 92-test
  suite passed. Its default safe-wrapper runtime lacks PyYAML; the full packet
  validator passed with zero errors/warnings under the existing Python 3.14
  runtime.
- No source byte was changed in any capability.

Exact locks and command receipts are in
`project-dossier/conformance/three-capability-conventions-v1/`.

## Limitations

No live remote-ref query, product execution, network, dependency installation,
security evaluation, or implemented compatibility test was performed.
