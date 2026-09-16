---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0015",
  "title": "Family migration local-main integration",
  "task": "TASK-0008",
  "recorded_at": "2026-09-16",
  "subject_revision_or_fingerprint": "reviewed pre-integration head b6592251e3d6d8267fce45b6ad313e24db410cd3; local main fast-forwarded exactly to that head",
  "result": "pass_pending_final_integrated_head_review",
  "fresh_until": null,
  "supersedes": null
}
---

After independent approval, the primary integrator serially fast-forwarded
`plectarium-family` local `main` from the published baseline to reviewed head
`b6592251e3d6d8267fce45b6ad313e24db410cd3`. The candidate branch remains
preserved. The checkout was clean, had one canonical worktree, retained its
expected origin, and local `origin/main` remained at the pre-migration remote
revision because nothing was pushed.

After every repository was integrated and switched to `main`, the workspace
strict topology, historical evidence, harness, and 35-test suite passed. This
repository's packet, harness, 15 tests, integrity, and diff checks also pass.
No remote or product effect occurred. Final integrated-head T1 review is still
required before `TASK-0008` may complete.
