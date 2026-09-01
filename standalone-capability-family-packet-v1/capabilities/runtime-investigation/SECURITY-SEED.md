# Runtime Investigation Security Seed

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
| credential_access | typically requested |
| secret_access | denied unless a future accepted plan proves a need |
| artifact_publish | denied unless a future accepted plan proves a need |
| deployment | denied unless a future accepted plan proves a need |
| issue_creation | denied unless a future accepted plan proves a need |
| external_communication | denied unless a future accepted plan proves a need |

**Project execution:** Central; explicit workload, command, environment, resource, and stop conditions are mandatory.  
**Network:** Denied by default; may be required for distributed systems or telemetry endpoints.  
**Browser execution:** Optional for browser/runtime investigations, preferably delegated to UI Assurance.  
**Production access:** Read-only production observation may be supported only by explicit high-assurance policy; mutation is prohibited.

## Domain-specific threats

- production data leakage
- instrumentation overhead
- credential exposure
- unsafe fault injection
- network exfiltration
- host compromise through profilers
- unrepresentative workloads

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
