# Family Research Agenda

| Capability | Primary systems and research categories |
| --- | --- |
| Universal Code Audit | existing UCA Full Product Build Packet v1; code-quality research; agent-skill evaluation patterns; repository graph systems; specialist analyzer ecosystems |
| Verification Assurance | mutation testing; property-based testing; model-based testing; test-impact analysis; flaky-test detection; coverage semantics; fuzzing; verification provenance |
| Specification Conformance | requirements traceability; architecture conformance; policy-as-code; spec-to-code systems; ADR tooling; formal/semi-formal specifications; requirements authority models |
| Supply-Chain Intelligence | Syft; Grype; OSV; Trivy; OpenSSF Scorecard; Sigstore; SLSA; CycloneDX; SPDX; VEX; package lifecycle intelligence |
| Runtime Investigation | OpenTelemetry; native profilers; continuous profiling; eBPF; race detectors; query analyzers; fault injection; causal performance analysis |
| API / Contract Assurance | Schemathesis; Pact; OpenAPI diff systems; GraphQL compatibility; protobuf compatibility; AsyncAPI/event compatibility; SDK/API evolution tools |
| UI / Browser Assurance | Playwright; axe-core; Lighthouse; visual regression systems; browser tracing; accessibility evaluation; secure browser containers |
| Database / Migration Assurance | Ariga Atlas; Liquibase/Flyway; gh-ost; Percona Toolkit; zero-downtime migration patterns; database locking; schema compatibility; backfill and dual-write strategies |
| Infrastructure Assurance | OpenTofu/Terraform planning; OPA/Rego; Checkov; Trivy config; Kubernetes validation; IAM analysis; infrastructure drift and cost analysis |
| Release Assurance | release policy systems; artifact attestation; SLSA/Sigstore; multi-evidence aggregation; release-readiness gates; software promotion models |

## Cross-family research

- manifest/result interoperability and content identity;
- permission and sandbox semantics across operating systems and OCI;
- Agent Skills portability and routing evaluation;
- capability result signing, attestation, freshness, and cache reuse;
- generic-harness and Octon provider experiments;
- cross-interface semantic equivalence;
- when duplicated code justifies a shared SDK versus local implementations.
