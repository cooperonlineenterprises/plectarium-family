# Generic Harness Integration

**Authority:** Normative boundary, reference transport

A harness should need a small evidence-centered contract:

```text
discover capability
      ↓
verify identity/version/provenance
      ↓
inspect operation and permission requirements
      ↓
construct or accept a plan
      ↓
authorize bounded execution
      ↓
run exact capability artifact
      ↓
receive and validate durable result reference
      ↓
inspect completion/scope/limitations
      ↓
consume evidence under project policy
      ↓
make a separately governed decision
```

The harness does not need to know the capability’s graph algorithms, test framework integrations, browser mechanics, vulnerability database, profiler formats, or migration semantics.

A harness MAY display the canonical character identity from a validated manifest or family mapping. It MUST continue to bind machine operations to the descriptive capability ID and MUST NOT infer trust or authority from the character identity.

## Minimum adapter responsibilities

- bind exact capability artifact/digest and manifest;
- translate harness subject/scope into capability request;
- preserve accepted permissions and plan identity;
- execute via native process, OCI, or supported remote interface;
- validate checksums, schemas, completion, subject identity, and provenance;
- store a durable result reference and limitations;
- route downstream work through normal harness authority.

## Prohibitions

A harness adapter must not:

- copy domain logic into the harness;
- reinterpret partial as complete;
- auto-install untrusted tools;
- create hidden network/credential rights;
- auto-convert conclusions to project actions;
- strip upstream provenance when routing evidence.
