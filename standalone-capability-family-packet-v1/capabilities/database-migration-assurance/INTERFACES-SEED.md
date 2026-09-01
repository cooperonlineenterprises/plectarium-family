# Database / Migration Assurance Interface Seed

## Canonical CLI

Working CLI name: `migration-assure` (`PROPOSED`). The generated project should define commands appropriate to its domain while preserving discover, plan, execute/analyze, inspect, compare, report, doctor, version, and schema/adapter diagnostics where useful.

The CLI must support structured noninteractive operation, truthful exit/completion semantics, exact plan identity, stdout/stderr discipline, and durable-result output.

## CI

CI invokes the same engine and owns runner permissions, checkout, secrets, scheduling, caches, artifact upload, and enforcement. The capability owns subject/scope, evidence, conclusions, completion, and result identity.

## MCP

MCP is a thin typed surface over the engine. It must not expose arbitrary shell, generic file writes, installation, credential management, or domain actions outside the product boundary.

## OCI

OCI should support high-assurance execution where practical. Candidate mounts:

```text
/workspace or /input  read-only
/out                  writable
/cache                writable
/tmp                  writable and bounded
```

Images should be non-root, capability-dropped, network-denied by default, resource-limited, signed/provenance-aware as policy requires, and must not inherit host credentials.

## Harness adapter

The adapter conveys the normal request/plan/result contracts and exact permission envelope. It must not translate a conclusion into project authority.

## Future HTTP

Optional and deferred until the local product is mature. It must use the same engine and add tenancy/authentication/retention rather than divergent semantics.
