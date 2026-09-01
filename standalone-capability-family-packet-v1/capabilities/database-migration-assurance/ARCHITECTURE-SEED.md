# Database / Migration Assurance Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative Database / Migration Assurance engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
Migration Assurance Bundle
```

## Capability-specific core

The engine should own:

- migration identity
- schema/data change analysis
- compatibility-window model
- controlled dry-run/simulation
- lock/rewrite evidence
- rollout-condition conclusions
- Migration Assurance Bundle

Its primary evidence domain includes:

- schema diffs
- destructive changes
- lock/rewrite estimates
- compatibility checks
- dry-run results
- backfill behavior
- rollback analysis
- data-integrity checks
- traffic and version assumptions

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write Migration Assurance Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| Ariga Atlas migration linting | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Liquibase/Flyway ecosystem imports | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| gh-ost | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| pt-online-schema-change | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| database-native explain/lock tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| ORM migration analyzers | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
