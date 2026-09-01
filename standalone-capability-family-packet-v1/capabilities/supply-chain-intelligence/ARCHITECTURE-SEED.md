# Supply-Chain Intelligence Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative Supply-Chain Intelligence engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
Supply-Chain Intelligence Bundle
```

## Capability-specific core

The engine should own:

- component identity reconciliation
- dependency graph
- SBOM generation/import
- vulnerability and lifecycle intelligence
- license obligations
- provenance/signature verification
- Supply-Chain Intelligence Bundle

Its primary evidence domain includes:

- component inventory
- dependency paths
- advisories
- reachability/exposure context when supportable
- license declarations
- maintainer/lifecycle signals
- signatures and attestations
- registry/package origin

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write Supply-Chain Intelligence Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| Syft | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Grype | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| OSV-Scanner | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Trivy | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| OpenSSF Scorecard | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Sigstore/Cosign | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| SLSA tooling | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| CycloneDX | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| SPDX | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| package-manager metadata | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
