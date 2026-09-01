# Family Packet Definition of Done

**Authority:** Normative packet release criteria

This family packet is complete only when fresh validation proves all criteria below.

## Family authority

- `FAMILY-CHARTER.md`, `spec/family-invariants.md`, authority hierarchy, and change control agree.
- canonical character identities match `spec/canonical-character-identities.md`, use no aliases, and do not replace technical identifiers or create authority;
- Plectarium relationship and portfolio source ownership match `ADR-013` and do not create runtime coupling or authority transfer;
- canonical `family_id` and exact character repository mappings match `FAM-036` without replacing descriptive capability IDs;
- Established and provisional conventions are visibly distinguished.
- No capability or interface has acquired project authority.
- No universal capability framework or shared SDK is represented as implemented.

## Capability seeds

- all ten required capability directories exist;
- every seed contains all required substantive files plus a machine-readable `capability.yaml`;
- every seed defines its product boundary, authority limits, evidence, permissions, security extensions, interfaces, Agent Skill behavior, evaluation, release criteria, roadmap, research agenda, and open questions;
- every seed and project-generation directive preserves its exact canonical character identity;
- every seed records the exact repository identity and requires downstream
  provenance pins for family Git commit, packet version, manifest digest, and
  used seed paths without inventing unpublished values;
- every `PROJECT-GENERATION-PROMPT.md` can be used without the original conversation;
- UCA seed preserves the validated UCA packet and does not weaken its decisions.

## Shared architecture

- relationship graph distinguishes hard, optional, aggregation, peer, and future relationships;
- no circular mandatory dependency exists;
- imported evidence preserves source identity, completion, provenance, evidence class, freshness, and limitations;
- top-level completion cannot misrepresent unavailable or partial work;
- transport cannot silently escalate authority.

## Security

- permission vocabulary includes repository, Git, project execution, external processes, network, browser, infrastructure, database, production, writes, credentials, secrets, publication, deployment, issue creation, and communication;
- default-deny posture is explicit;
- domain-specific threats exist in every seed;
- Infrastructure Assurance cannot apply infrastructure;
- Migration Assurance cannot mutate production data;
- Release Assurance cannot publish;
- UI Assurance cannot escape declared browser/origin controls;
- Runtime Investigation cannot execute or observe production without explicit authority.

## Evaluation and provenance

- family and skill evaluation specifications include baselines and honest-claim rules;
- source and licensing registers cover the inherited UCA research and primary domain ecosystems;
- conversation coverage is truthful and excludes inaccessible/internal material;
- manifest, checksums, validator, source maps, and internal consistency review exist.

## Integrity

- required files exist;
- all JSON and YAML parse;
- provisional JSON Schemas pass Draft 2020-12 structural checks and valid/legacy-negative namespace fixtures produce the expected acceptance/rejection outcomes;
- deterministic Markdown projections exactly match their canonical YAML sources;
- capability/relationship/decision/ADR identifiers are unique and resolve;
- no substantive seed contains empty placeholder text or unclassified `TODO` markers;
- packet checksums validate;
- ZIP opens, passes integrity testing, extracts cleanly, and the extracted copy passes validation;
- ZIP SHA-256 is recorded in the external delivery integrity sidecar and final delivery response; the in-packet integrity report explains the archive self-reference boundary.
