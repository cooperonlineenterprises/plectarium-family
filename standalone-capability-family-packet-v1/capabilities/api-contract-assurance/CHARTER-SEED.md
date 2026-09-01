# API / Contract Assurance Charter Seed

**Status:** Project-generation authority seed; a generated project charter must refine it without weakening family invariants.

## Canonical character identity

**Harmia** is the established character identity. It is used directly without nicknames or alternate names, remains distinct from descriptive machine identifiers, and does not create project or execution authority.

## Purpose

Assess declared and observed interface compatibility across schema changes, consumer/provider expectations, stateful workflows, version policies, and behavior evidence.

## Governing question

> Are interfaces, protocols, consumers, providers, schemas, and service boundaries behaviorally and evolutionarily compatible?

## Intended users

- humans responsible for the subject and its risks;
- CI systems needing repeatable evidence;
- Octon Mini and other harnesses governing invocation and downstream work;
- coding agents using the canonical Agent Skill;
- sibling capabilities consuming a durable result where appropriate.

## Primary subjects

- API schema
- consumer contract
- provider implementation
- event schema
- SDK surface
- protocol version
- interface change

## Product ambition

A protocol-agnostic compatibility engine that combines static schema analysis with consumer/provider and stateful behavioral evidence, supports compatibility windows, and produces stable contract conclusions across releases.

## Product philosophy

- produce domain-specific evidence rather than generic advice;
- declare what was and was not exercised;
- separate raw evidence, interpretation, conclusion, completion, and authority;
- integrate mature tools where they are stronger than a new implementation;
- remain local-first and independently usable;
- build a full production-shaped product in dependency order.

## Authority limit

The capability may conclude using states such as `compatible`, `compatible_with_conditions`, `breaking_change`, `behavioral_mismatch`, `undeclared_behavior`, `unverified`, `incomplete`. Those states never authorize downstream actions. A user, CI policy, or harness must make the project decision under its own authority.

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
