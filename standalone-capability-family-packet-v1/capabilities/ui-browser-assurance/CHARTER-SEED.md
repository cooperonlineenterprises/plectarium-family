# UI / Browser Assurance Charter Seed

**Status:** Project-generation authority seed; a generated project charter must refine it without weakening family invariants.

## Canonical character identity

**Iris** is the established character identity. It is used directly without nicknames or alternate names, remains distinct from descriptive machine identifiers, and does not create project or execution authority.

## Purpose

Execute controlled browser journeys and inspect functional, accessibility, visual, console, network, responsive, performance, and compatibility evidence in isolated browser environments.

## Governing question

> Does the delivered user experience actually function correctly across the declared browser and UI scope?

## Intended users

- humans responsible for the subject and its risks;
- CI systems needing repeatable evidence;
- Octon Mini and other harnesses governing invocation and downstream work;
- coding agents using the canonical Agent Skill;
- sibling capabilities consuming a durable result where appropriate.

## Primary subjects

- web application
- browser journey
- page/component
- declared browser matrix
- visual baseline
- accessibility scope

## Product ambition

A reproducible multi-browser assurance engine with isolated sessions, journey plans, accessibility and performance checks, visual evidence, stable baselines, rich traces, and strict origin/credential controls.

## Product philosophy

- produce domain-specific evidence rather than generic advice;
- declare what was and was not exercised;
- separate raw evidence, interpretation, conclusion, completion, and authority;
- integrate mature tools where they are stronger than a new implementation;
- remain local-first and independently usable;
- build a full production-shaped product in dependency order.

## Authority limit

The capability may conclude using states such as `journey_passed`, `journey_failed`, `accessibility_violation`, `visual_regression`, `browser_incompatibility`, `performance_budget_failed`, `incomplete`. Those states never authorize downstream actions. A user, CI policy, or harness must make the project decision under its own authority.

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
