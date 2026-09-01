# Future Shared SDK and Framework Policy

**Status:** `DEFERRED`

Potential extraction areas include manifest parsing, result-envelope types, completion and permission types, provenance/hash utilities, bundle verification, MCP scaffolding, OCI helpers, and Agent Skill generation.

Extraction requires all of:

1. at least three implemented capabilities use materially equivalent semantics;
2. the shared module is smaller and clearer than local implementations;
3. it does not create runtime coupling or a second harness;
4. it has independent compatibility/version policy;
5. capability-specific extensions remain possible;
6. migration costs and ownership are explicit;
7. conformance tests prove cross-capability benefit;
8. an accepted family ADR authorizes it.

No shared SDK is included in this packet.
