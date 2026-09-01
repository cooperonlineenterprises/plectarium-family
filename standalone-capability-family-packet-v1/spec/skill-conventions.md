# Agent Skill Conventions

**Status:** `ACCEPTED`

## 1. Default packaging

Prefer one primary canonical Agent Skill per capability. Add another only when a materially distinct cognitive workflow demonstrates routing or behavioral benefit—UCA’s `uca-simplify` is the reference example.

## 2. Character identity

Canonical Agent Skills MUST preserve the character mapping in `canonical-character-identities.md`, recognize natural requests using either the character identity or descriptive capability name, and use the canonical identity directly without nicknames or alternate character names. Technical skill package IDs MAY remain descriptive. Character language MUST remain evidence-centered and MUST NOT imply approval, execution, or downstream authority.

## 3. Skill responsibilities

A skill teaches:

- when the capability is relevant;
- which operation/mode/lens to select;
- how to establish subject and scope;
- how to obtain and review a plan;
- how to review permissions and effects;
- how to invoke CLI or MCP without installing tools;
- how to inspect completion before claims;
- how to distinguish evidence, interpretation, and authority;
- when to escalate or obtain missing evidence;
- how to present concise, referenced conclusions;
- how to hand downstream work to the normal project process.

## 4. Skill prohibitions

A skill MUST NOT:

- reimplement the domain engine in prose;
- silently run project code, network, browsers, infrastructure, databases, or production systems;
- install the capability or specialist tools;
- claim a partial result is complete;
- convert a conclusion into implementation/deployment/publication authority;
- maintain divergent semantic copies across platforms.

## 5. Canonical source and generation

Use an Agent Skills-compatible canonical source with focused references. Generate thin host-specific plugin/command metadata. CI should regenerate, compare, validate installation, test routing, and verify invariant content digests.

## 6. Evaluation

Evaluate the skill separately from the engine: descriptive-name and character-identity trigger positives, negatives, collisions, no-alias behavior, mode selection, permission awareness, canonical invocation, completion truth, evidence/authority separation, pressure cases, non-mutation, and downstream handoff. Include a no-skill baseline.
