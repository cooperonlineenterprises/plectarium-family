# Supply-Chain Intelligence Product Boundary

## The capability owns

- component identity reconciliation
- dependency graph
- SBOM generation/import
- vulnerability and lifecycle intelligence
- license obligations
- provenance/signature verification
- Supply-Chain Intelligence Bundle

## The capability explicitly does not own

- automatic dependency upgrades
- package installation
- license legal advice
- release authority
- code-quality analysis unrelated to supply chain

## External ownership

- a harness owns trust, accepted permissions, project policy, task/decision lifecycle, and downstream work;
- specialist tools own their domain algorithms and raw output formats unless the project intentionally builds differentiated native analysis;
- CI owns checkout, credentials, runner isolation, scheduling, artifact retention, and enforcement infrastructure;
- humans own unresolved product, legal, operational, and risk decisions;
- sibling capabilities own their own evidence and result semantics.

## Independence test

The generated product must pass this thought experiment:

> If Octon Mini, MCP, and every AI provider disappeared, could a human still install the product, inspect its capabilities and permissions, invoke its CLI, receive a truthful Supply-Chain Intelligence Bundle, and integrate it with another system?

The required answer is yes.

## Monolith prevention

The project must not absorb sibling domains merely because related evidence is useful. It should import a durable sibling result or create a narrow adapter when possible. In particular, it must not silently become a release system, project harness, automatic remediation engine, or universal scanner aggregator.
