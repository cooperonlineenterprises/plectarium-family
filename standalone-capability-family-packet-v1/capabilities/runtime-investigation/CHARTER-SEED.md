# Runtime Investigation Charter Seed

**Status:** Project-generation authority seed; a generated project charter must refine it without weakening family invariants.

## Canonical character identity

**Echo** is the established character identity. It is used directly without nicknames or alternate names, remains distinct from descriptive machine identifiers, and does not create project or execution authority.

## Purpose

Plan and conduct hypothesis-driven runtime investigations using profiles, traces, logs, metrics, queries, concurrency observations, and controlled experiments while binding conclusions to workload and environment.

## Governing question

> What is this system actually doing while it runs, and what evidence explains the observed behavior?

## Intended users

- humans responsible for the subject and its risks;
- CI systems needing repeatable evidence;
- Octon Mini and other harnesses governing invocation and downstream work;
- coding agents using the canonical Agent Skill;
- sibling capabilities consuming a durable result where appropriate.

## Primary subjects

- running process
- service
- benchmark workload
- trace window
- profile
- incident scenario
- runtime environment

## Product ambition

A workload- and environment-bound investigation engine that can import and collect multi-signal telemetry, correlate runtime evidence to code and operations, test causal hypotheses, compare investigations, and preserve uncertainty.

## Product philosophy

- produce domain-specific evidence rather than generic advice;
- declare what was and was not exercised;
- separate raw evidence, interpretation, conclusion, completion, and authority;
- integrate mature tools where they are stronger than a new implementation;
- remain local-first and independently usable;
- build a full production-shaped product in dependency order.

## Authority limit

The capability may conclude using states such as `hypothesis_supported`, `hypothesis_contradicted`, `causal_link_indicated`, `bottleneck_confirmed_within_workload`, `insufficient_evidence`, `environment_incompatible`, `investigation_incomplete`. Those states never authorize downstream actions. A user, CI policy, or harness must make the project decision under its own authority.

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
