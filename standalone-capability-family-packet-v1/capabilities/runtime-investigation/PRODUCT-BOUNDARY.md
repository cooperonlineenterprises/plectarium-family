# Runtime Investigation Product Boundary

## The capability owns

- investigation hypothesis
- workload identity
- instrumentation plan
- runtime evidence ingestion
- causal candidate validation/refutation
- runtime conclusion
- Runtime Investigation Bundle

## The capability explicitly does not own

- production remediation
- always-on observability platform
- deployment authority
- unbounded production access
- static code audit as a whole

## External ownership

- a harness owns trust, accepted permissions, project policy, task/decision lifecycle, and downstream work;
- specialist tools own their domain algorithms and raw output formats unless the project intentionally builds differentiated native analysis;
- CI owns checkout, credentials, runner isolation, scheduling, artifact retention, and enforcement infrastructure;
- humans own unresolved product, legal, operational, and risk decisions;
- sibling capabilities own their own evidence and result semantics.

## Independence test

The generated product must pass this thought experiment:

> If Octon Mini, MCP, and every AI provider disappeared, could a human still install the product, inspect its capabilities and permissions, invoke its CLI, receive a truthful Runtime Investigation Bundle, and integrate it with another system?

The required answer is yes.

## Monolith prevention

The project must not absorb sibling domains merely because related evidence is useful. It should import a durable sibling result or create a narrow adapter when possible. In particular, it must not silently become a release system, project harness, automatic remediation engine, or universal scanner aggregator.
