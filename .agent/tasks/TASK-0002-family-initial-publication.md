---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0002",
  "status": "in_progress",
  "previous_status": "ready",
  "title": "Create and initially publish the Plectarium family repository",
  "authority_basis": "authority:current-operator-plectarium-portfolio-setup-v2",
  "owner": "primary_agent",
  "created_at": "2026-08-31",
  "updated_at": "2026-08-31",
  "dependencies": ["TASK-0001"],
  "decision_refs": ["DEC-0001"],
  "supersedes": null,
  "closure_evidence": [],
  "external_effects": "Observed local effect: initialized this exact repository on branch main. Pending external effects: exact private repository creation plus at most one foundation push and one narrow closure-evidence push.",
  "limitations": [
    "remote state must be reinspected immediately before creation",
    "authorization expires after the two-push sequence and final equality verification"
  ]
}
---

## Scope

In scope:

- initialize this exact repository on local branch `main`;
- inspect the exact staged foundation and create one intent-focused commit;
- collision-check and create only private
  `cooperonlineenterprises/plectarium-family` without remote-generated content;
- push the foundation commit normally;
- record narrow publication evidence in one closure commit and push it
  normally; and
- verify local `HEAD`, `origin/main`, and remote `refs/heads/main` equality and
  a clean final worktree.

Out of scope: alternate names, public visibility, force push, history rewrite,
unexpected remote adoption, dependency installation, product implementation,
release, package, deployment, integration, secret, or organization changes.

## Acceptance criteria

- [ ] Local foundation validation and review remain current.
- [ ] Exact remote is confirmed absent without an authentication ambiguity.
- [ ] Initial staged inventory and diff check are clean and reviewed.
- [ ] Exact remote is private, empty before the first push, and uses `main`.
- [ ] Foundation and closure commits are pushed normally within the two-push limit.
- [ ] Final local, tracking, and remote refs are equal and the worktree is clean.
- [ ] Evidence lists every external effect and residual limitation without a readiness claim.

## Validation and failure handling

Stop on collision, unexpected history/content, authentication or permission
ambiguity, non-private visibility, or non-fast-forward rejection. Preserve any
partial effect; do not delete, repurpose, merge, rebase, or force.

## Current handoff

`TASK-0001`, `EVD-0002`, `REV-0001`, and `CHK-0001` establish the local
pre-creation boundary. This task grants nothing; it only narrows the current
operator authorization.
