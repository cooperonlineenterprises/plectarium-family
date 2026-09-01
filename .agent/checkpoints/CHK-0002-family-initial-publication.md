---
{"schema_version":"harness.checkpoint.v1","id":"CHK-0002","title":"Family initial publication and closure-candidate checkpoint","created_at":"2026-08-31","task":"TASK-0002","source_revision_or_fingerprint":"git:8d3fb0f93b222bb955b40636bd6aa48c90e17f1e","supersedes":"CHK-0001","decision_refs":["DEC-0001"],"evidence_refs":["EVD-0002","EVD-0003"],"limitations":["The checkpoint cannot attest the later push of the closure commit containing it."]}
---

## Anchored state

- Exact remote: `https://github.com/cooperonlineenterprises/plectarium-family.git`
- Visibility/default branch: private / `main`
- Foundation commit: `8d3fb0f93b222bb955b40636bd6aa48c90e17f1e`
- First-push equality: verified
- Packet version and manifest digest: `1.2.0` /
  `54116db0e4f518ffe793df3d3ebd2b87064f00aab10b373bf1909f9126b24867`

## Final handoff gate

Push the closure commit normally exactly once, then directly verify local,
tracking, and remote equality plus a clean worktree. Do not create a third
evidence commit under this task.
