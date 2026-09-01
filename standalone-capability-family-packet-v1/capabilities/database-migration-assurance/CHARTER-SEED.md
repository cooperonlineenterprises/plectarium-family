# Database / Migration Assurance Charter Seed

**Status:** Project-generation authority seed; a generated project charter must refine it without weakening family invariants.

## Canonical character identity

**Janus** is the established character identity. It is used directly without nicknames or alternate names, remains distinct from descriptive machine identifiers, and does not create project or execution authority.

## Purpose

Analyze migration semantics, application-version overlap, locking, rewrite and backfill behavior, data integrity, sequencing, rollback, and operational conditions without possessing production database mutation authority.

## Governing question

> Can this schema or data migration be deployed safely under the declared operational conditions?

## Intended users

- humans responsible for the subject and its risks;
- CI systems needing repeatable evidence;
- Octon Mini and other harnesses governing invocation and downstream work;
- coding agents using the canonical Agent Skill;
- sibling capabilities consuming a durable result where appropriate.

## Primary subjects

- migration files
- schema diff
- database model
- backfill plan
- application versions
- deployment topology
- representative database

## Product ambition

A database-aware migration assurance engine with dialect-specific adapters, staged-rollout modeling, application-version compatibility, dry-run and representative-data evidence, data-loss protections, and no production mutation authority.

## Product philosophy

- produce domain-specific evidence rather than generic advice;
- declare what was and was not exercised;
- separate raw evidence, interpretation, conclusion, completion, and authority;
- integrate mature tools where they are stronger than a new implementation;
- remain local-first and independently usable;
- build a full production-shaped product in dependency order.

## Authority limit

The capability may conclude using states such as `safe_within_declared_conditions`, `requires_staged_rollout`, `requires_runtime_validation`, `high_risk`, `unsafe`, `incomplete`. Those states never authorize downstream actions. A user, CI policy, or harness must make the project decision under its own authority.

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
