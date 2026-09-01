# Verification Assurance Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative Verification Assurance engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
Verification Bundle
```

## Capability-specific core

The engine should own:

- claim model
- proof-mechanism discovery
- verification planning
- controlled test/build execution
- claim-evidence mapping
- contradiction handling
- verification completion
- Verification Bundle

Its primary evidence domain includes:

- compiler/type-check evidence
- unit/integration/acceptance results
- property-based results
- mutation outcomes
- fuzz reproductions
- contract checks
- runtime assertions
- scenario replay
- benchmark budget observations

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write Verification Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| native compilers and test runners | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Stryker | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| PIT | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| cargo-mutants | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Hypothesis/QuickCheck-style tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| fuzzers | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| coverage tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| test-impact analysis tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
