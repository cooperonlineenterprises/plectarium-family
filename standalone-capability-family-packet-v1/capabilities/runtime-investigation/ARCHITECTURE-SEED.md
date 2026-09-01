# Runtime Investigation Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative Runtime Investigation engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
Runtime Investigation Bundle
```

## Capability-specific core

The engine should own:

- investigation hypothesis
- workload identity
- instrumentation plan
- runtime evidence ingestion
- causal candidate validation/refutation
- runtime conclusion
- Runtime Investigation Bundle

Its primary evidence domain includes:

- CPU profiles
- allocation and heap profiles
- traces
- logs
- metrics
- I/O and network observations
- query plans
- lock/contention observations
- race-detector results
- fault-injection outcomes

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write Runtime Investigation Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| OpenTelemetry | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| pprof | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| perf/eBPF tools | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| runtime-specific profilers | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| database query analyzers | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| race detectors | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| continuous profiling imports | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
