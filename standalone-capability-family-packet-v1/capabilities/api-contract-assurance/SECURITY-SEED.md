# API / Contract Assurance Security Seed

## Typical permission posture

| Permission | Seed posture |
| --- | --- |
| repository_read | typically requested |
| repository_write | denied unless a future accepted plan proves a need |
| git_read | denied unless a future accepted plan proves a need |
| git_write | denied unless a future accepted plan proves a need |
| project_execution | typically requested |
| external_process_execution | typically requested |
| network | typically requested |
| browser_execution | denied unless a future accepted plan proves a need |
| infrastructure_read | denied unless a future accepted plan proves a need |
| infrastructure_apply | denied unless a future accepted plan proves a need |
| database_read | denied unless a future accepted plan proves a need |
| database_write | denied unless a future accepted plan proves a need |
| production_access | denied unless a future accepted plan proves a need |
| output_write | typically requested |
| cache_write | typically requested |
| temporary_write | typically requested |
| credential_access | denied unless a future accepted plan proves a need |
| secret_access | denied unless a future accepted plan proves a need |
| artifact_publish | denied unless a future accepted plan proves a need |
| deployment | denied unless a future accepted plan proves a need |
| issue_creation | denied unless a future accepted plan proves a need |
| external_communication | denied unless a future accepted plan proves a need |

**Project execution:** Often required for provider verification or API testing; explicitly planned.  
**Network:** Denied by default; local or isolated endpoints preferred.  
**Browser execution:** Not intrinsic, though UI-facing API flows may coordinate with UI Assurance.  
**Production access:** Production traffic mutation prohibited; read-only schema imports require policy.

## Domain-specific threats

- unsafe API fuzzing
- production endpoint targeting
- credential leakage
- schema poisoning
- consumer data exposure
- false compatibility from schema-only checks

## Required safe defaults

- deny undeclared permissions and destinations;
- use direct argv and sanitized environments;
- never install or update tools automatically;
- isolate project execution and controlled resources;
- treat input, repository, tool output, browser content, telemetry, schemas, policies, and prompts as untrusted data;
- redact secrets and sensitive source/evidence in reports;
- bound time, CPU, memory, process count, output, archives, and external data;
- record actual permissions/effects in the durable result;
- prohibit downstream authority not explicitly owned by the product boundary.

## Capability-specific authority statement

The capability conclusion cannot itself authorize the action it evaluates. The project build packet must include adversarial tests that prove this boundary under pressure.
