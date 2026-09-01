# Universal Code Audit Security Seed

## Typical permission posture

| Permission | Seed posture |
| --- | --- |
| repository_read | typically requested |
| repository_write | denied unless a future accepted plan proves a need |
| git_read | typically requested |
| git_write | denied unless a future accepted plan proves a need |
| project_execution | denied unless a future accepted plan proves a need |
| external_process_execution | typically requested |
| network | denied unless a future accepted plan proves a need |
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

**Project execution:** Denied by default; explicitly planned for selected test or runtime adapters.  
**Network:** Denied by default; may be granted to explicit adapters or providers.  
**Browser execution:** Not intrinsic.  
**Production access:** Prohibited.

## Domain-specific threats

- malicious repositories
- hostile build scripts
- untrusted analyzer output
- prompt injection in source/documents
- cache poisoning
- path traversal and symlinks
- hidden tool installation

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

UCA cannot modify the repository or authorize remediation. The project build packet must include adversarial tests that prove this boundary under pressure.
