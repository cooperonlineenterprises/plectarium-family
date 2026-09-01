# API / Contract Assurance Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative API / Contract Assurance engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
Contract Assurance Bundle
```

## Capability-specific core

The engine should own:

- contract identity
- schema and semantic diff
- consumer/provider compatibility plan
- stateful/API property testing
- version-policy conformance
- Contract Assurance Bundle

Its primary evidence domain includes:

- schema diffs
- consumer/provider verification
- generated API tests
- stateful workflow results
- compatibility-tool reports
- observed behavior samples
- version-policy rules

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write Contract Assurance Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| Schemathesis | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Pact | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| OpenAPI/GraphQL/protobuf diff tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| JSON Schema validators | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| AsyncAPI tooling | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| language-native API compatibility tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
