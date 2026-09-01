# Universal Code Audit Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative Universal Code Audit engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
UCA Audit Bundle
```

## Capability-specific core

The engine should own:

- repository identity and scope
- repository discovery
- history and graph intelligence
- audit planning
- candidate validation and attempted refutation
- stable findings
- Reduction/Simplification lens
- audit comparison
- UCA Audit Bundle

Its primary evidence domain includes:

- structural observations
- history and co-change observations
- dependency and architecture graphs
- analyzer imports
- validated or rejected candidates
- runtime evidence imports
- reduction safety-floor evidence

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write UCA Audit Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| Semgrep | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| CodeQL | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| OSV-Scanner | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Syft | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Trivy | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| native compilers/linters | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| coverage and mutation systems | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| profilers as imported evidence | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
