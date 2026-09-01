# Database / Migration Assurance — Project Seed

**Capability ID:** `database-migration-assurance`  
**Family ID:** `standalone-capability-family`  
**Canonical descriptive name:** Database Schema and Data Migration Assurance  
**Canonical character identity:** **Janus**  
**Working CLI:** `migration-assure` (`PROPOSED`)  
**Repository:** `janus` — `https://github.com/cooperonlineenterprises/janus.git` (`ESTABLISHED`)  
**Project creation priority:** 8  
**Seed status:** `PROJECT SEED`

## Governing question

> **Can this schema or data migration be deployed safely under the declared operational conditions?**

## Product purpose

Analyze migration semantics, application-version overlap, locking, rewrite and backfill behavior, data integrity, sequencing, rollback, and operational conditions without possessing production database mutation authority.

## Mature target

A database-aware migration assurance engine with dialect-specific adapters, staged-rollout modeling, application-version compatibility, dry-run and representative-data evidence, data-loss protections, and no production mutation authority.

## Durable result

The capability should produce a **Migration Assurance Bundle** with a provisional shared result envelope and capability-specific payloads. The result is evidence and conclusion, never project authority.

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
