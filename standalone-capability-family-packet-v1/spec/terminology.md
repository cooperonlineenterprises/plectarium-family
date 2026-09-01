# Family Terminology

**Authority:** Normative shared vocabulary where marked; capability-specific vocabularies may refine it.

| Term | Meaning |
|---|---|
| **Standalone capability** | Independently usable, independently versioned specialist product with its own semantic engine and durable result. |
| **Family ID** | Stable machine namespace for a capability family. This family uses `standalone-capability-family`; the value is identity only and carries no authority. |
| **Canonical character identity** | Established user-facing specialist identity mapped one-to-one to a descriptive capability. It is not a nickname, machine identifier, or source of authority. |
| **Harness** | External governance/orchestration system that controls trust, authority, project policy, invocation, evidence use, and downstream work. |
| **Capability engine** | Single authoritative implementation of domain semantics beneath all interfaces. |
| **Application service** | Discover, plan, execute/analyze, inspect, compare, report, doctor, or another domain operation exposed by the engine. |
| **Capability manifest** | `PROVISIONAL` machine-readable discovery metadata describing namespaced family/capability/version identity, operations, interfaces, permissions, result types, and limitations. |
| **Subject** | Exact entity or state analyzed: repository revision, claim, artifact, API, runtime, infrastructure plan, migration, UI environment, etc. |
| **Scope** | Declared subset and boundaries of the subject actually analyzed. |
| **Plan** | Inspectable, immutable description of intended providers, tools, permissions, resources, outputs, and limitations. |
| **Permission** | Explicitly named access or effect required for an operation. It is not authority to exceed the accepted plan. |
| **Evidence** | Attributable observation or assertion with producer, subject, scope, time/freshness, class, and provenance. |
| **Conclusion** | Capability-specific interpreted outcome supported by evidence; may be a finding, claim status, conformance status, readiness result, or investigation result. |
| **Completion** | Truthful account of whether requested work completed, with limitations and node outcomes. |
| **Durable result** | Checksummed, inspectable capability-specific artifact containing the shared envelope and domain payload. |
| **Result envelope** | `PROVISIONAL` common metadata around a capability-specific payload. |
| **Result reference** | Immutable identity, location, checksum, schema, completion, and producer data sufficient for a consumer to validate a durable result. |
| **Imported evidence** | Evidence consumed from another capability or system while retaining original identity and limitations. |
| **Agent Skill** | Portable instruction layer teaching an agent when and how to use the capability; not the engine. |
| **Adapter** | Explicit provider boundary to a specialist external tool, format, runtime, or service. |
| **Capability class** | `PROVISIONAL` descriptive category based on execution/evidence behavior; not an authority tier. |
| **Authority** | Permission to make or enact project/external decisions; capability evidence does not create it. |
| **Mature v1** | First production-grade release satisfying the capability’s full v1 release criteria, not merely an architectural prototype. |
| **Minimum Complete Architecture** | Integration checkpoint proving the foundational lifecycle and contracts before broad parallel depth. |
| **Shared convention** | Family-level behavior expected across products; exact status may be ESTABLISHED, ACCEPTED, or PROVISIONAL. |
| **Capability-specific refinement** | Domain rule that extends or specializes a shared convention without silently violating family invariants. |
