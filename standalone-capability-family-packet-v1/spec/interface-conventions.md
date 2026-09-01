# Interface Conventions

**Status:** Shared semantic principles `ESTABLISHED`; command naming is reference guidance

## Identity and technical naming

User-facing prose, help, Agent Skills, UI, and reports SHOULD use the canonical character identities defined in `canonical-character-identities.md`. Machine-facing capability IDs remain descriptive, exact repositories follow `family-identity-and-repository-map.md`, and CLI, package, image, schema, skill, and protocol identifiers remain separate capability decisions. An interface MUST NOT invent nicknames or imply that a character identity carries authority.

Machine-facing discovery and durable-result identity MUST carry
`family_id: standalone-capability-family` alongside the descriptive
`capability_id` and version. The exact repository identity is established
separately and MUST NOT substitute for the family/capability/version tuple.

## CLI

The CLI is the preferred direct human/machine interface. It SHOULD support noninteractive structured input/output, version reporting, discovery, inspectable planning, execution, completion, result inspection, and diagnostics. Direct argv is preferred; stdout carries requested primary output and stderr carries progress/diagnostics.

## CI

CI owns checkout, credentials, permissions, scheduling, cache/artifact infrastructure, and merge/deployment enforcement. The capability owns subject/scope semantics, planning, evidence, completion, conclusions, result identity, and gate evaluation. Fork contexts default to no secrets and no trusted-cache writes.

## MCP

MCP exposes typed operations/resources over the same engine. It MUST NOT add generic shell, arbitrary file write, hidden installation, credential administration, or automatic downstream action. Equivalent CLI/MCP requests should be semantically equivalent.

## OCI

OCI provides isolated distribution and reproducible tool bundles. Images should be non-root, read-only-root where feasible, capability-dropped, network-denied by default, resource-limited, without Docker socket or inherited home credentials, and accompanied by SBOM, provenance, checksums/signatures as policy requires.

## Agent Skill

Skills teach intent routing, operation/mode selection, permission review, canonical invocation, completion inspection, evidence interpretation, truthful language, escalation, and downstream handoff. They do not contain analyzer implementation or create authority.

## Harness adapter

A harness adapter translates the harness’s trust/authority/invocation records to the capability’s normal manifest/request/plan/result contracts. It SHOULD record a durable result reference rather than duplicate capability truth.

## Future HTTP/API

A service interface remains optional. It uses the same engine semantics and must add authentication, tenancy, queueing, artifact storage, cancellation, retention, and network policy without weakening local-first operation.

## No transport privilege

The permission envelope is invariant across transport. An OCI or CI invocation is not implicitly more trusted; MCP is not implicitly interactive authority; an Agent Skill is not an installation permission.
