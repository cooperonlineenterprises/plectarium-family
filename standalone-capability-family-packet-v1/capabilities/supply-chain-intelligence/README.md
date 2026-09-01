# Supply-Chain Intelligence — Project Seed

**Capability ID:** `supply-chain-intelligence`  
**Family ID:** `standalone-capability-family`  
**Canonical descriptive name:** Software Supply-Chain and Dependency Intelligence  
**Canonical character identity:** **Genea**  
**Working CLI:** `supply-chain-intel` (`PROPOSED`)  
**Repository:** `genea` — `https://github.com/cooperonlineenterprises/genea.git` (`ESTABLISHED`)  
**Project creation priority:** 4  
**Seed status:** `PROJECT SEED`

## Governing question

> **What external software, artifacts, build inputs, dependencies, and supply-chain risks does this project actually carry?**

## Product purpose

Build a provenance-aware inventory of direct, transitive, vendored, build, runtime, optional, and image dependencies; combine vulnerability, lifecycle, license, signature, provenance, and substitution evidence without pretending presence equals exploitability.

## Mature target

A multi-ecosystem component and provenance intelligence engine with interoperable SBOM support, contextual vulnerability prioritization, offline operation, signed evidence, lifecycle and license analysis, and stable comparison across releases.

## Durable result

The capability should produce a **Supply-Chain Intelligence Bundle** with a provisional shared result envelope and capability-specific payloads. The result is evidence and conclusion, never project authority.

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
