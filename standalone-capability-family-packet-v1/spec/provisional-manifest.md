# Standalone Capability Manifest v0

**Status:** `PROVISIONAL`  
**Schema:** `spec/schemas/standalone-capability-manifest.v0.schema.json`

The manifest supports static discovery without executing arbitrary code. It is an experiment to be validated by at least UCA, Verification Assurance, and Specification Conformance.

It describes or may describe:

- canonical `family_id`, capability ID, descriptive name, optional canonical character identity, product version, protocol version, and description;
- operations and interfaces;
- result-envelope and capability-specific schemas;
- supported subjects and environments;
- requested permissions and effect posture;
- network, project execution, external processes, and writable paths;
- credentials and controlled-resource categories;
- provisional capability classes;
- completion-model reference;
- artifact/provenance identity;
- compatibility and limitations.

Static discovery MUST NOT imply trust, installation, adoption, or permission acceptance.

For this packet the required `family_id` literal is
`standalone-capability-family`. Consumers compare `family_id`,
`capability_id`, and `version` together and reject an unnamespaced document.
The namespace does not imply trust, compatibility, adoption, or permission.

The optional `character_identity` field is user-facing metadata. It does not replace `family_id` or `capability_id`, change protocol identity, or create authority.

Packet 1.2.0 changed the still-provisional v0 experiment to add this namespace.
See `migrations/provisional-family-namespace-1.2.0.md` and the fixtures under
`../fixtures/provisional-contracts/`.
