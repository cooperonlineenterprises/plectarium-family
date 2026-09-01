# Supply-Chain Intelligence Charter Seed

**Status:** Project-generation authority seed; a generated project charter must refine it without weakening family invariants.

## Canonical character identity

**Genea** is the established character identity. It is used directly without nicknames or alternate names, remains distinct from descriptive machine identifiers, and does not create project or execution authority.

## Purpose

Build a provenance-aware inventory of direct, transitive, vendored, build, runtime, optional, and image dependencies; combine vulnerability, lifecycle, license, signature, provenance, and substitution evidence without pretending presence equals exploitability.

## Governing question

> What external software, artifacts, build inputs, dependencies, and supply-chain risks does this project actually carry?

## Intended users

- humans responsible for the subject and its risks;
- CI systems needing repeatable evidence;
- Octon Mini and other harnesses governing invocation and downstream work;
- coding agents using the canonical Agent Skill;
- sibling capabilities consuming a durable result where appropriate.

## Primary subjects

- repository and lockfiles
- SBOM
- container image
- release artifact
- build provenance
- dependency graph

## Product ambition

A multi-ecosystem component and provenance intelligence engine with interoperable SBOM support, contextual vulnerability prioritization, offline operation, signed evidence, lifecycle and license analysis, and stable comparison across releases.

## Product philosophy

- produce domain-specific evidence rather than generic advice;
- declare what was and was not exercised;
- separate raw evidence, interpretation, conclusion, completion, and authority;
- integrate mature tools where they are stronger than a new implementation;
- remain local-first and independently usable;
- build a full production-shaped product in dependency order.

## Authority limit

The capability may conclude using states such as `inventory_complete`, `inventory_partial`, `vulnerability_observed`, `provenance_verified`, `provenance_missing`, `license_attention_required`, `lifecycle_risk`, `investigation_required`. Those states never authorize downstream actions. A user, CI policy, or harness must make the project decision under its own authority.

## Inherited authority


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
