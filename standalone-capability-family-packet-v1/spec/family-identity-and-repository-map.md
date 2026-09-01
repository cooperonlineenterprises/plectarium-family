# Family Identity and Capability Repository Map

**Status:** `ESTABLISHED`  
**Authority:** Family machine identity and repository identity registry  
**Decision:** `FAM-036`; `ADR-013`

## Canonical family identity

The canonical machine identifier for this family is:

```text
standalone-capability-family
```

Provisional discovery and durable-result contracts MUST carry this literal as
`family_id` alongside the descriptive `capability_id` and applicable
capability version. Consumers MUST compare the full family/capability/version
tuple. A matching character name or repository name is insufficient.

`family_id` is identity metadata, not a trust root, compatibility guarantee,
tenant boundary, permission, or authority grant.

## Exact repository mapping

| Capability ID | Character | Repository | GitHub repository |
| --- | --- | --- | --- |
| `universal-code-audit` | Verity | `verity` | `cooperonlineenterprises/verity` |
| `verification-assurance` | Titra | `titra` | `cooperonlineenterprises/titra` |
| `specification-conformance` | Ortha | `ortha` | `cooperonlineenterprises/ortha` |
| `supply-chain-intelligence` | Genea | `genea` | `cooperonlineenterprises/genea` |
| `runtime-investigation` | Echo | `echo` | `cooperonlineenterprises/echo` |
| `api-contract-assurance` | Harmia | `harmia` | `cooperonlineenterprises/harmia` |
| `ui-browser-assurance` | Iris | `iris` | `cooperonlineenterprises/iris` |
| `database-migration-assurance` | Janus | `janus` | `cooperonlineenterprises/janus` |
| `infrastructure-assurance` | Atlas | `atlas` | `cooperonlineenterprises/atlas` |
| `release-assurance` | Sibyl | `sibyl` | `cooperonlineenterprises/sibyl` |

The repository mapping is exact and established for product identity. It does
not establish publication state, visibility observations, credentials, CLI
names, package names, OCI image names, schema identifiers, skill package IDs,
or protocol identifiers.

## Downstream provenance contract

Every capability build packet generated from a seed MUST record:

1. the exact published family Git commit;
2. packet name `standalone-capability-family-packet-v1`;
3. the exact packet version;
4. SHA-256 of that commit's `PACKET-MANIFEST.json`;
5. every family and seed path actually used.

The family commit must exist before a downstream packet can truthfully fill
that pin. A generator MUST leave generation gated rather than invent a commit
or digest. Plectarium and other consumers pin and consume the published family
contract; they MUST NOT maintain a competing mutable copy as canonical.
