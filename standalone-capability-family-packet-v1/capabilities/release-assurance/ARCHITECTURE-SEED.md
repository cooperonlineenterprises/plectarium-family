# Release Assurance Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative Release Assurance engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
Release Assurance Bundle
```

## Capability-specific core

The engine should own:

- candidate identity
- release-criteria interpretation
- upstream-result compatibility checks
- evidence aggregation
- exception accounting
- readiness conclusion
- Release Assurance Bundle

Its primary evidence domain includes:

- UCA results
- Verification Bundles
- Conformance Bundles
- Supply-Chain Bundles
- Contract/UI/Migration/Infrastructure results
- artifact identity
- SBOM
- provenance
- release policy

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write Release Assurance Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| result-bundle verifiers | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| signature/provenance validators | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| artifact identity tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| policy evaluators | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
