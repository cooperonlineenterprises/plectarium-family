---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0004",
  "status": "completed",
  "previous_status": "review",
  "title": "Publish the local three-capability checkpoint records",
  "authority_basis": "current operator authorization on 2026-09-01 for exactly one additional family checkpoint commit and one normal fast-forward push",
  "owner": "primary_agent",
  "created_at": "2026-08-31",
  "updated_at": "2026-09-01",
  "dependencies": ["TASK-0005"],
  "source_refs": ["SRC-0004", "SRC-0005", "SRC-0006"],
  "decision_refs": ["DEC-0002", "DEC-0003"],
  "supersedes": null,
  "closure_evidence": ["EVD-0008"],
  "external_effects": "One checkpoint commit and one normal fast-forward push to the exact private family origin/main, with direct final equality and cleanliness verification.",
  "limitations": [
    "the checkpoint commit cannot attest its own later push",
    "the additional one-commit/one-push authority is consumed after final equality verification",
    "no later push or family-packet/capability change is authorized",
    "repository files and task status cannot grant future authority"
  ]
}
---

## Required effect

After separate explicit operator authorization, publish v1 and v2 together:

1. inspect the exact checkpoint candidate and clean pre-task Git state;
2. stage only validated family checkpoint and lifecycle records;
3. create one intent-focused checkpoint commit;
4. push exactly once, normally, to
   `https://github.com/cooperonlineenterprises/plectarium-family.git`
   `main`;
5. verify local HEAD, `origin/main`, remote `main`, and clean worktree.

No force push, alternate branch/name, packet rewrite, capability change,
release, or later push is included.

## Closure

- Evidence: `EVD-0008`; review: `REV-0005`; checkpoint: `CHK-0005`.
- The commit containing these records cannot attest its own later push.
- Final local/tracking/remote equality and cleanliness are direct post-commit
  handoff evidence.
- The one additional commit/push authority is consumed; no later push is
  authorized by this task.
