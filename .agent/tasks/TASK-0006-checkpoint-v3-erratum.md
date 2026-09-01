---
{"schema_version":"harness.task.v1","id":"TASK-0006","status":"completed","previous_status":"review","title":"Create the three-capability checkpoint v3 lock erratum","authority_basis":"current operator local erratum instruction","owner":"primary_agent","created_at":"2026-09-01","updated_at":"2026-09-01","dependencies":["TASK-0004","TASK-0005"],"source_refs":["SRC-0007"],"decision_refs":["DEC-0003","DEC-0004"],"supersedes":null,"closure_evidence":["EVD-0009","EVD-0010"],"external_effects":"none; local family erratum and designated root integrity only","limitations":["v1/v2 preserved byte-for-byte","no family packet or capability edits","publication blocked under TASK-0007"]}
---

Created and validated five v3 artifacts correcting the v2 checksum lock. Outcome
remains `PASS_WITH_PROVISIONAL_DIVERGENCE`; second-wave packets may proceed,
Sibyl remains last, shared contracts stay provisional/unresolved, and
SDK/runtime remains deferred.
