# Capability Project Seed Contract

Every seed directory MUST enable a future project-generation agent to determine:

- the canonical `family_id`, descriptive `capability_id`, exact character repository identity, and separation from other future machine identifiers;
- the capability's canonical character identity and its separation from descriptive machine identifiers;
- product purpose and governing question;
- product boundary and authority limits;
- inherited family invariants and provisional conventions;
- capability-specific lifecycle, evidence, completion, conclusions, and durable result;
- typical permissions and safe defaults;
- external tool integration strategy;
- CLI/MCP/CI/OCI/skill/harness interfaces;
- domain threat extensions;
- evaluation claims and fixtures;
- mature-v1 capability and release criteria;
- research agenda and licensing boundaries;
- open questions and whether work can proceed;
- project-generation instructions and source provenance.

`capability.yaml` carries `family_id: standalone-capability-family`, the
descriptive capability identity, exact canonical character identity, exact
established repository metadata, packet version, and downstream provenance
requirements. CLI, package, image, schema, skill, and protocol identifiers
remain separately provisional unless a capability-specific decision accepts
them.

A generated capability build packet MUST pin the exact published family Git
commit, packet version, SHA-256 of that commit's `PACKET-MANIFEST.json`, and all
family/seed paths used. A seed cannot supply the future family commit and MUST
NOT invent it. Missing publication identity gates completion of the provenance
record without blocking honest local generation work that remains explicitly
unpublished.

Required files, repository mappings, exact character mappings, and provenance
requirements are validated by `scripts/validate-packet.py`. Seeds are
authoritative inputs for generating project build packets; they are not
executable product implementations.
