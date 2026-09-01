# Shared Evidence Conventions

**Status:** Core provenance distinctions `ESTABLISHED`; class vocabulary `PROVISIONAL`

## 1. Minimum evidence properties

Material evidence SHOULD identify:

- evidence ID and schema version;
- source capability/adapter/tool/human/model;
- exact subject and scope;
- observed or produced time;
- validity/freshness basis;
- evidence class;
- raw artifact or source references;
- assumptions and limitations;
- reproducibility posture;
- sensitivity/retention classification where relevant.

## 2. Provisional evidence classes

| Class | Meaning | Common limitation |
|---|---|---|
| `deterministic_static` | Deterministic analysis of non-executed subject content. | May miss dynamic/runtime behavior. |
| `deterministic_contract` | Direct check against an explicit contract or schema. | Contract may be incomplete or wrong. |
| `external_tool_deterministic` | Deterministic output from an identified specialist tool/config. | Tool extraction and blind spots remain material. |
| `heuristic` | Reproducible or probabilistic candidate-producing inference. | Requires validation and may be noisy. |
| `historical` | Evidence from version, incident, ownership, or change history. | History quality and filters affect interpretation. |
| `runtime_observed` | Observation under an identified workload/environment/time. | Does not automatically generalize beyond that scope. |
| `imported_human` | Human assertion, review, decision, or classification. | Must not be represented as tool observation. |
| `ai_interpretation` | Model-derived interpretation over bounded context. | Model/context dependent; generally advisory. |
| `derived_fusion` | New evidence derived from identified source evidence and rules. | Inference distance and conflicts must remain visible. |
| `absence_or_unavailability` | Missing, denied, unsupported, stale, or failed evidence source. | Indicates uncertainty, never a clean/pass result. |

Capabilities MAY refine classes, but a refinement must map to the shared class when results cross capability boundaries.

## 3. Contradictions

Conflicting evidence is represented explicitly with supporting and contradicting references, applicability, resolution rule if any, and unresolved impact. Consumers MUST NOT silently average contradictory evidence into false certainty.

## 4. Imported evidence

An imported result remains an external source. The consumer may validate compatibility and derive new conclusions, but it preserves upstream completion, class, provenance, subject/scope, freshness, and limitations. See `imported-evidence.md`.

## 5. AI evidence

AI interpretations require provider/model/context identity, structured output, evidence references, privacy/network policy, and human-review posture. Model self-confidence is metadata, not calibrated evidence confidence.
