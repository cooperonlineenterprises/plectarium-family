# Runtime Investigation — Project Seed

**Capability ID:** `runtime-investigation`  
**Family ID:** `standalone-capability-family`  
**Canonical descriptive name:** Runtime Behavior and Performance Investigation  
**Canonical character identity:** **Echo**  
**Working CLI:** `runtime-investigate` (`PROPOSED`)  
**Repository:** `echo` — `https://github.com/cooperonlineenterprises/echo.git` (`ESTABLISHED`)  
**Project creation priority:** 5  
**Seed status:** `PROJECT SEED`

## Governing question

> **What is this system actually doing while it runs, and what evidence explains the observed behavior?**

## Product purpose

Plan and conduct hypothesis-driven runtime investigations using profiles, traces, logs, metrics, queries, concurrency observations, and controlled experiments while binding conclusions to workload and environment.

## Mature target

A workload- and environment-bound investigation engine that can import and collect multi-signal telemetry, correlate runtime evidence to code and operations, test causal hypotheses, compare investigations, and preserve uncertainty.

## Durable result

The capability should produce a **Runtime Investigation Bundle** with a provisional shared result envelope and capability-specific payloads. The result is evidence and conclusion, never project authority.

## Start here

1. Read `CHARTER-SEED.md` and `PRODUCT-BOUNDARY.md`.
2. Read `CAPABILITY-MODEL.md`, `EVIDENCE-MODEL-SEED.md`, and `SECURITY-SEED.md`.
3. Review `RESEARCH-AGENDA.md` and resolve or preserve `OPEN-QUESTIONS.md`.
4. Use `PROJECT-GENERATION-PROMPT.md` to create the capability’s independent Product Constitution + Executable Specification + AI Build Packet.

Before generation can be completed, record the exact published family Git
commit, packet version `1.2.0`, SHA-256 of `PACKET-MANIFEST.json`, and every
family/seed path used. These are provenance pins, not permission or readiness.

## Inherited family rules


This project inherits these binding family rules:

- independently usable and harness agnostic;
- one authoritative semantic engine;
- evidence/conclusions are not project authority;
- explicit permissions and no hidden installation/network/execution;
- truthful completion and durable result artifacts;
- AI remains optional and distinguishable;
- thin CLI/CI/MCP/OCI/Agent Skill/harness interfaces;
- imported evidence preserves source identity, completion, provenance, class, freshness, and limitations;
- no shared family framework or SDK may be assumed implemented.


## Reference relationship

This is a future independent product. UCA may provide outer architectural reference, but UCA-specific candidates, findings, graphs, reduction semantics, and bundle internals must not be copied mechanically.
