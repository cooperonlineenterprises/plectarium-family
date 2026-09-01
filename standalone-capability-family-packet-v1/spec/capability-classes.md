# Provisional Capability Classes

**Status:** `PROVISIONAL`; descriptive only

| Class | Description | Typical examples |
|---|---|---|
| `read_only_evidence_producer` | Primarily analyzes declared inputs without project execution or controlled-environment mutation. | UCA core, Supply-Chain Intelligence, Specification Conformance |
| `execution_evidence_producer` | Executes project or test/runtime code under an accepted plan to produce evidence. | Verification Assurance, Runtime Investigation, API Assurance |
| `controlled_environment_evidence_producer` | Uses a browser, ephemeral database, cloud/infrastructure simulator, or other bounded environment. | UI Assurance, Migration Assurance, Infrastructure Assurance |
| `evidence_aggregator` | Consumes durable results and policies to derive a higher-level conclusion without reimplementing upstream work. | Release Assurance |

A capability may fit more than one class. Classes do not grant authority, determine trust, or replace explicit permissions. Stabilization requires evidence from real products.
