# Three-Capability Conventions Checkpoint v1

**Owner:** Plectarium Capability Family  
**Mode:** Read-only comparison of published Verity, Titra, and Ortha foundations  
**Outcome:** `INCOMPLETE`  
**Authority effect:** None

## Scope

This checkpoint compares published packet contracts and repository
foundations. It does not compare implemented engine behavior because product
implementation remains absent. It does not promote a provisional convention,
change the family packet, edit a capability, or authorize a shared runtime,
SDK, package, schema binding, or downstream action.

Published inputs are locked in `INPUT-LOCKS.json`. Exact field-by-field
classification is in `CONTRACT-SURFACE-MATRIX.json`; all divergences and
dispositions are in `DIVERGENCES.json`.

## Result

All three repositories are independent, clean `main` roots whose local HEAD
and `origin/main` match their recorded final commits. Packet manifests and
checksum ledgers match the published digests. Titra and Ortha packet, harness,
and 15-test suites pass. Verity's safe byte preflight, setup check, harness
check, and 92-test suite pass; its full packet validator passes with zero
errors and warnings under the already configured Python 3.14 runtime.

Engine ownership, completion honesty, repository boundaries, and no-action
semantics pass. The checkpoint preconditions do not: Verity lacks the
established FAM-036 machine tuple and immutable family source lock. Native
result references cannot yet feed the imported-result contracts without
undeclared enrichment, and Titra/Ortha reuse relative schema IDs for different
bytes. These are second-wave blockers under this checkpoint's declared pass
criteria.

The checkpoint is not a clean-contract convergence result:

- Verity predates family packet 1.2.0 and lacks a packet-local family namespace,
  `universal-code-audit` machine tuple, and immutable family source lock.
- Verity uses legacy permission and evidence-class tokens.
- Verity has a prose result-reference contract rather than a standalone
  generic result-reference schema.
- Titra and Ortha capability manifests do not conform to the pinned family v0
  manifest schema; they are packet-specific provisional experiments.
- Completion payloads differ, and Titra/Ortha relative schema IDs collide by
  name while identifying different bytes.
- Verity lacks a governed combined writer declaration and machine readiness
  status; all three lack proven reference-to-import interoperability.
- The default Verity safe-wrapper runtime lacks PyYAML even though its safe
  preflight and the configured Python 3.14 validator path succeed.

These items remain unresolved or provisional and block stabilization of the
affected shared contracts. They do not justify editing Verity from this
checkpoint.

## Family status report

| Element | Status after checkpoint | Disposition |
| --- | --- | --- |
| Independent usability and harness agnosticism | `ESTABLISHED` | Preserved across all three packets. |
| One authoritative engine per capability | `ESTABLISHED` | Preserved; domain engines remain independent. |
| Evidence and conclusions are not authority | `ESTABLISHED` | Preserved across interfaces and results. |
| Explicit effects and default-deny posture | `ESTABLISHED` | Preserved with intentional domain-specific security profiles. |
| Truthful top-level completion | `ESTABLISHED` | Five-state meaning aligns; payload shapes remain capability-specific. |
| Imported evidence preserves source semantics | `ESTABLISHED` principle | Titra/Ortha have strict schemas; Verity projection evidence remains incomplete. |
| Character identities and repository mapping | `ESTABLISHED` but incomplete | Family ledger maps all three, but Verity packet lacks the machine tuple required to prove packet alignment. |
| Durable result per capability | `ACCEPTED` | All packets define canonical content identity and distinct transport identity. |
| Thin CLI/CI/MCP/OCI/skill/harness projections | `ACCEPTED` | Interface sets differ without semantic ownership transfer. |
| Shared capability manifest/discovery | `PROVISIONAL` | Verity lacks the family tuple; Titra/Ortha manifests each fail the pinned family v0 manifest schema and remain packet-specific. |
| Shared permission vocabulary | `PROVISIONAL` | Legacy Verity vocabulary requires explicit mapping. |
| Shared result envelope/reference shape | `PROVISIONAL` | Common meaning exists; exact shape does not converge. |
| Shared lifecycle convention | `PROVISIONAL` | Outer lifecycle aligns; domain nodes and payloads differ. |
| Capability classes | `PROVISIONAL` | Security profiles demonstrate why classes cannot grant permission. |
| Public schema namespace and generated bindings | `UNRESOLVED` | Absolute and project-local schema-ID policies differ. |
| Verity family 1.2.0 provenance projection | `UNRESOLVED` | Future Verity-owned migration required before common lock claims. |
| Hosted family service or marketplace | `DEFERRED` | No evidence changes the prior decision. |
| Shared SDK/runtime | `DEFERRED` | Packet similarity is insufficient; implementation evidence and a later ADR remain mandatory. |
| Capability monolith or shared domain model | `REJECTED` | No evidence supports reconsideration. |
| Skill-only capability or automatic downstream action | `REJECTED` | No evidence supports reconsideration. |

No status was promoted merely because two or three packet documents look
similar.

## Second-wave gate

The checkpoint procedure is executed, but its sequencing gate is
`INCOMPLETE`. Genea, Echo, Harmia, Iris, Janus, and Atlas packet generation
must not proceed until separately authorized, owner-scoped work resolves the
Verity family identity/provenance projection and the cross-packet schema and
reference/import blockers, followed by a successor checkpoint. No capability
or family packet is modified by this finding.

## Limitations

- The comparison is packet/foundation evidence, not implemented behavioral
  equivalence.
- No network or live remote-ref query was performed.
- External research, security efficacy, performance, legal/compliance status,
  release, and production readiness remain unassessed.
- A future family contract promotion requires change control and evidence
  beyond this checkpoint.

## Publication boundary

This local checkpoint changes the family repository after its authorized
foundation and closure pushes were consumed. No current authority permits
another push. Publishing these checkpoint records requires exactly one
additional normal push to
`https://github.com/cooperonlineenterprises/plectarium-family.git` after
separate explicit authorization, validation, review, and local/remote equality
checks. Repository tasks and files do not grant that authority.
