# Database / Migration Assurance Product Boundary

## The capability owns

- migration identity
- schema/data change analysis
- compatibility-window model
- controlled dry-run/simulation
- lock/rewrite evidence
- rollout-condition conclusions
- Migration Assurance Bundle

## The capability explicitly does not own

- production migration execution
- database credentials by default
- data repair authority
- deployment sequencing authority
- application code changes

## External ownership

- a harness owns trust, accepted permissions, project policy, task/decision lifecycle, and downstream work;
- specialist tools own their domain algorithms and raw output formats unless the project intentionally builds differentiated native analysis;
- CI owns checkout, credentials, runner isolation, scheduling, artifact retention, and enforcement infrastructure;
- humans own unresolved product, legal, operational, and risk decisions;
- sibling capabilities own their own evidence and result semantics.

## Independence test

The generated product must pass this thought experiment:

> If Octon Mini, MCP, and every AI provider disappeared, could a human still install the product, inspect its capabilities and permissions, invoke its CLI, receive a truthful Migration Assurance Bundle, and integrate it with another system?

The required answer is yes.

## Monolith prevention

The project must not absorb sibling domains merely because related evidence is useful. It should import a durable sibling result or create a narrow adapter when possible. In particular, it must not silently become a release system, project harness, automatic remediation engine, or universal scanner aggregator.
