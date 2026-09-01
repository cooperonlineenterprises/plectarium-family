# UI / Browser Assurance Architecture Seed

## Reference architecture

```text
Interfaces
  CLI | CI | MCP | OCI | Agent Skill | Harness adapter | future HTTP
                         ↓
Application services
  discover | plan | execute/analyze | inspect | compare | report | doctor
                         ↓
Authoritative UI / Browser Assurance engine
  subject identity | scope | capability resolution | domain planning
  execution/evidence | domain reasoning | completion | result writing
                         ↓
Specialist adapters / native domain modules
                         ↓
UI Assurance Bundle
```

## Capability-specific core

The engine should own:

- browser-environment planning
- journey identity
- controlled browser execution
- screenshots/traces/DOM evidence
- accessibility and visual evidence
- UI Assurance Bundle

Its primary evidence domain includes:

- journey outcomes
- screenshots and videos
- Playwright traces
- DOM/accessibility-tree observations
- axe results
- console/network errors
- visual diffs
- Core Web Vitals and Lighthouse evidence

## Reference lifecycle

```text
discover
  → plan
  → permission review
  → execute/analyze
  → produce evidence
  → apply capability-specific validation/reasoning
  → compute completion
  → write UI Assurance Bundle
  → inspect/compare/report
```

Candidate/refutation semantics should be used only when the domain benefits. Do not force UCA’s finding model onto this project.

## External tools

| Candidate tool/standard | Architectural treatment |
| --- | --- |
| Playwright | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| axe-core | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| Lighthouse/Lighthouse CI | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| visual-diff engines | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |
| browser trace tooling | Research/integrate through an explicit adapter; verify current version, license, output formats, permissions, and limitations. |

## Internal freedom

The future engineering team may choose module/crate/package boundaries, graph/storage algorithms, concurrency model, and implementation language mix. Stable external contracts and authority/security semantics take precedence over forced internal uniformity.
