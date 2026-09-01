# Project Generation Guide

A capability seed is not a prompt fragment; it is inherited authority.

## Inputs to a project-generation run

- this family packet;
- the chosen capability directory;
- current primary-source research;
- the UCA Full Product Build Packet when it provides relevant reference patterns;
- explicit owner decisions about open questions, licensing, technical identifiers, and v1 scope.

The canonical character identity is already established by `spec/canonical-character-identities.md`; project generation MUST preserve it, MUST NOT introduce aliases, and MUST keep it distinct from descriptive capability IDs, repository names, CLI commands, skill package IDs, and protocols.

The canonical family identifier is `standalone-capability-family`, and the
exact repository mapping is established by
`spec/family-identity-and-repository-map.md`. A generated packet MUST preserve
the descriptive capability ID while using the exact repository identity. CLI,
package, image, schema, skill, and protocol names remain separate decisions.

## Expected output

A separate downloadable Product Constitution + Executable Specification + AI Build Packet containing:

- capability charter and invariants;
- canonical character identity and evidence-centered usage guidance;
- production-shaped target architecture;
- capability-specific schemas and durable bundle;
- permissions/execution/security model;
- external adapter architecture;
- CLI/CI/MCP/OCI/skill/harness contracts;
- claim/candidate/finding/conclusion and completion semantics;
- evaluation corpus and claim-proof matrix;
- AI-team workstreams/tasks;
- roadmap and mature-v1 release criteria;
- source/license/provenance records;
- immutable provenance pins for the published family Git commit, packet
  version, `PACKET-MANIFEST.json` SHA-256, and exact family/seed paths used;
- validator, manifest, checksums, and archive integrity.

## Quality test

A fresh engineering agent must be able to answer what it owns, does not own, may access, produces, must prove, and may not silently change without reconstructing the parent conversation.
