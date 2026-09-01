# Specification Conformance Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative Specification Conformance engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
Conformance Bundle
```

## Capability-specific core

The engine should own:

- source-authority inventory
- requirement identity
- traceability graph
- conformance planning
- ambiguity and conflict records
- conformance status
- Conformance Bundle

Its primary evidence domain includes:

- specification excerpts with identity
- implementation mappings
- architecture-rule results
- verification imports
- unimplemented obligation evidence
- ambiguity/conflict records
- supersession lineage

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write Conformance Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| architecture test systems | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| policy-as-code engines | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| requirements/traceability tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| schema validators | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| UCA and Verification result importers | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
