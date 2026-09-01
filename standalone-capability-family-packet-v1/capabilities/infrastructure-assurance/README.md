# Infrastructure Assurance — Project Seed

**Capability ID:** `infrastructure-assurance`  
**Family ID:** `standalone-capability-family`  
**Canonical descriptive name:** Infrastructure-as-Code and Configuration Assurance  
**Canonical character identity:** **Atlas**  
**Working CLI:** `infra-assure` (`PROPOSED`)  
**Repository:** `atlas` — `https://github.com/cooperonlineenterprises/atlas.git` (`ESTABLISHED`)  
**Project creation priority:** 9  
**Seed status:** `PROJECT SEED`

## Governing question

> **Is this infrastructure or configuration change coherent, secure, compatible, and sufficiently understood before application?**

## Product purpose

Analyze infrastructure definitions and plans for destructive changes, privilege expansion, exposure, drift, policy violations, replacement, rollback, and cost-impact signals without applying changes.

## Mature target

A multi-format infrastructure assurance engine that safely parses or generates plans, models resource and privilege change, integrates policy tools, detects destructive/exposure changes, and operates without apply authority.

## Durable result

The capability should produce a **Infrastructure Assurance Bundle** with a provisional shared result envelope and capability-specific payloads. The result is evidence and conclusion, never project authority.

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
