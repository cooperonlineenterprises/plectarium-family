# Future Family and Project-Generation Fixtures

This packet does not contain executable capability engines. Future family-level fixtures should test:

- project-generation prompts in clean agent contexts;
- capability-seed completeness and boundary preservation;
- shared manifest/result-envelope compatibility experiments;
- imported-result provenance and partial-completion preservation;
- Agent Skill routing and authority pressure;
- generic harness and Octon provider invocation records;
- malicious seed/source input and prompt-injection resistance.

`provisional-contracts/` contains family-owned positive and negative examples
for the packet 1.2.0 namespace migration. Files ending in `.valid.json` MUST
validate against the matching provisional schema. Files ending in
`.invalid.json` intentionally represent pre-1.2.0 unnamespaced shapes and MUST
be rejected. They are conformance fixtures, not product output or a stable
protocol promise.

Capability implementation fixtures belong in their separate future repositories. This directory documents the intended boundary and prevents test assets from being mistaken for product implementations.
