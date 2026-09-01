# Cross-Capability Imported Evidence

**Authority:** Normative interoperability principles  
**Status:** `ESTABLISHED` preservation rules; exact schemas `PROVISIONAL`

When Capability B consumes Capability A’s result, B must validate and preserve:

1. family ID, capability ID, and product version;
2. result identity and bundle/schema version;
3. subject identity and scope;
4. completion state and node limitations;
5. original evidence class and producer;
6. provenance, checksums, and signature status where relevant;
7. production time and source freshness semantics;
8. compatibility assessment performed by B;
9. any transformation or aggregation applied by B.

B may derive new evidence, but the derived record references the upstream evidence and declares its inference distance. B cannot upgrade `partial` upstream evidence to complete native evidence merely because B completed its own aggregation.

Direct in-process engine coupling SHOULD be avoided when an immutable result reference is sufficient. Release Assurance is the planned primary experiment for this model.

For this family the source `family_id` is
`standalone-capability-family`. A missing namespace is invalid under packet
1.2.0's provisional contracts and MUST NOT be inferred from the character,
repository, result location, transport, or Plectarium catalog placement.
