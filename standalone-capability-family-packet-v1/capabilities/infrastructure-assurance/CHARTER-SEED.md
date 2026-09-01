# Infrastructure Assurance Charter Seed

**Status:** Project-generation authority seed; a generated project charter must refine it without weakening family invariants.

## Canonical character identity

**Atlas** is the established character identity. It is used directly without nicknames or alternate names, remains distinct from descriptive machine identifiers, and does not create project or execution authority.

## Purpose

Analyze infrastructure definitions and plans for destructive changes, privilege expansion, exposure, drift, policy violations, replacement, rollback, and cost-impact signals without applying changes.

## Governing question

> Is this infrastructure or configuration change coherent, secure, compatible, and sufficiently understood before application?

## Intended users

- humans responsible for the subject and its risks;
- CI systems needing repeatable evidence;
- Octon Mini and other harnesses governing invocation and downstream work;
- coding agents using the canonical Agent Skill;
- sibling capabilities consuming a durable result where appropriate.

## Primary subjects

- Terraform/OpenTofu plan
- Kubernetes manifests
- Helm chart
- IAM policy
- container/deployment configuration
- cloud policy
- infrastructure diff

## Product ambition

A multi-format infrastructure assurance engine that safely parses or generates plans, models resource and privilege change, integrates policy tools, detects destructive/exposure changes, and operates without apply authority.

## Product philosophy

- produce domain-specific evidence rather than generic advice;
- declare what was and was not exercised;
- separate raw evidence, interpretation, conclusion, completion, and authority;
- integrate mature tools where they are stronger than a new implementation;
- remain local-first and independently usable;
- build a full production-shaped product in dependency order.

## Authority limit

The capability may conclude using states such as `coherent`, `coherent_with_conditions`, `policy_violation`, `destructive_change`, `privilege_expansion`, `exposure_change`, `high_risk`, `incomplete`. Those states never authorize downstream actions. A user, CI policy, or harness must make the project decision under its own authority.

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
