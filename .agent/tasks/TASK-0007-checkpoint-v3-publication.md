---
{"schema_version":"harness.task.v1","id":"TASK-0007","status":"review","previous_status":"validating","title":"Publish the checkpoint v3 corrective record set","authority_basis":"current operator authorization recorded by SRC-0008 for exactly one corrective commit and one normal fast-forward push","owner":"primary_agent","created_at":"2026-09-01","updated_at":"2026-09-01","dependencies":["TASK-0006"],"source_refs":["SRC-0007","SRC-0008"],"decision_refs":["DEC-0004"],"supersedes":null,"closure_evidence":[],"external_effects":"pending: one corrective commit on main and one normal fast-forward push to the exact private family origin/main, followed by direct equality and clean-worktree verification","limitations":["the corrective commit cannot attest its own later push","the single-use authority is consumed only after the authorized commit, push, and direct final verification complete","no later family push or family-packet/capability change is authorized","repository records grant no future authority"]}
---

## Publication candidate

- Candidate evidence: `EVD-0011`; review: `REV-0007`; checkpoint:
  `CHK-0007`.
- Stage only validated v3/lifecycle/dossier/generated records, create one
  corrective family commit, push once normally to `origin/main`, then verify
  local/tracking/remote equality and a clean worktree.
- The commit containing these records cannot attest its own later push; final
  completion, authority consumption, equality, and cleanliness must be direct
  post-commit handoff evidence.
- No packet/capability/release/later push is included.
