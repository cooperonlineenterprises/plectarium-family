# Standalone Capability Family — Canonical Character Identities

**Status:** ESTABLISHED  
**Version:** 1.0  
**Scope:** Standalone Capability Family  
**Authority:** Family-level naming and identity convention  
**Supersedes:** Earlier exploratory naming candidates and directions discussed during capability-family design

---

## 1. Decision

The standalone capability family will use the following canonical character identities:

| Capability | Canonical Character Identity |
|---|---|
| Universal Code Audit | **Verity** |
| Verification Assurance | **Titra** |
| Specification Conformance | **Ortha** |
| Supply-Chain Intelligence | **Genea** |
| Runtime Investigation | **Echo** |
| API / Contract Assurance | **Harmia** |
| UI / Browser Assurance | **Iris** |
| Infrastructure Assurance | **Atlas** |
| Database / Migration Assurance | **Janus** |
| Release Assurance | **Sibyl** |

These names are canonical. They are not abbreviations, acronyms, nicknames, or informal aliases.

The family MUST NOT introduce alternate short forms, nicknames, or competing character names for these capabilities unless this decision is explicitly superseded through the family architecture decision process.

---

## 2. Governing Naming Principle

Each capability is represented by a distinct character identity whose meaning reflects **how the capability behaves and produces evidence**.

The family naming rule is:

> **Use an existing classical character when its archetype is unusually isomorphic to the capability. Otherwise, personify the strongest classical, linguistic, or scientific concept underlying how the capability produces evidence.**

Names should generally be:

- short and pronounceable;
- memorable as independent identities;
- natural in conversational use;
- behaviorally or epistemically connected to the capability;
- compatible with the capability's authority boundaries;
- cohesive with the family without being mechanically uniform.

The family deliberately does **not** require every identity to come from the same morphology. Some are mythological figures, some are classical concepts personified as characters, and some are scientific mechanisms personified as characters.

The commonality is behavioral meaning.

---

## 3. Canonical Identities

### 3.1 Verity — Universal Code Audit

**Capability:** Universal Code Audit  
**Identity:** Verity  
**Origin:** Verity; truth; conformity to fact.

Verity represents the capability whose central concern is:

> **What does the available evidence permit us to say is true about this codebase?**

Verity examines repository structure, history, architecture, dependencies, complexity, duplication, findings, and opportunities for safe reduction. She distinguishes observation from inference, preserves uncertainty and contradictory evidence, and does not represent incomplete analysis as certainty.

Verity may identify risk, defect, inconsistency, unnecessary complexity, or simplification opportunities.

Verity does **not** possess authority to modify the repository or approve remediation.

**Characteristic question:**

> What is actually true?

**Natural usage:**

- “Run this through Verity.”
- “What did Verity find?”
- “Verity found a recurring architectural hotspot.”
- “Verity completed with limitations.”

---

### 3.2 Titra — Verification Assurance

**Capability:** Verification Assurance  
**Identity:** Titra  
**Origin:** Personification of titration.

Titration determines an unknown through controlled application of a known challenge until an observable endpoint is reached.

Titra represents the capability whose central concern is:

> **What evidence demonstrates that this claim actually holds within the declared scope?**

Titra converts claims into explicit verification questions, identifies available proof mechanisms, constructs a verification plan, exercises those mechanisms, captures supporting and contradicting evidence, and reports what has or has not been demonstrated.

The analogy is structural:

```text
claim
  ↓
controlled challenge
  ↓
observable evidence
  ↓
support / contradiction
  ↓
bounded verification conclusion
```

Titra does not treat “tests passed” as sufficient without understanding what those tests establish.

Titra does **not** grant authority to accept, merge, deploy, or release a change.

**Characteristic question:**

> Show me what proves it.

**Natural usage:**

- “Run that claim through Titra.”
- “Ask Titra whether rollback actually works.”
- “Titra found the behavior strongly supported but not fully exercised.”
- “Titra could not complete verification because the integration environment was unavailable.”

---

### 3.3 Ortha — Specification Conformance

**Capability:** Specification Conformance  
**Identity:** Ortha  
**Origin:** Personification derived from Greek *orthos*: straight, right, correct, or properly aligned.

Ortha represents the capability whose central concern is:

> **Does the implementation remain correctly aligned with the governing specification and intent?**

Ortha compares implementation against requirements, architecture, ADRs, schemas, acceptance criteria, policies, and other declared authorities.

She distinguishes:

- implementation non-conformance;
- specification ambiguity;
- conflicting authorities;
- superseded requirements;
- unverified conformance.

Ortha does not decide what the specification ought to be when authoritative sources conflict. She exposes the conflict.

**Characteristic question:**

> Is this still aligned with what governs it?

**Natural usage:**

- “Ask Ortha whether this conforms to ADR-17.”
- “Run the implementation through Ortha.”
- “Ortha found two deviations and one ambiguous requirement.”
- “Ortha cannot determine conformance until the conflicting specifications are resolved.”

---

### 3.4 Genea — Supply-Chain Intelligence

**Capability:** Supply-Chain Intelligence  
**Identity:** Genea  
**Origin:** Greek *genea*: generation, lineage, descent; related conceptually to genealogy.

Genea represents the capability whose central concern is:

> **Where did this software come from, what does it descend from, and what inherits risk from that lineage?**

Software supply chains form genealogies of:

- source projects;
- packages;
- direct and transitive dependencies;
- build inputs;
- artifacts;
- images;
- registries;
- signers;
- attestations;
- releases.

Genea reconstructs ancestry and descent, preserving provenance and identifying how upstream characteristics propagate downstream.

She can reason both backward toward origin and forward toward affected descendants.

Genea does **not** silently replace dependencies, upgrade packages, or authorize supply-chain changes.

**Characteristic question:**

> What is its lineage?

**Natural usage:**

- “Ask Genea where this artifact came from.”
- “Run the image through Genea.”
- “Genea traced the vulnerable ancestor through four transitive dependencies.”
- “Genea found six downstream artifacts that inherit the affected component.”

---

### 3.5 Echo — Runtime Investigation

**Capability:** Runtime Investigation  
**Identity:** Echo  
**Origin:** Greek mythological Echo and the physical phenomenon of reflected signals.

Echo represents the capability whose central concern is:

> **What is the running system telling us about what is happening beneath the visible surface?**

Runtime activity produces observable signals:

- traces;
- profiles;
- logs;
- metrics;
- latency;
- allocations;
- I/O;
- contention;
- queries;
- failures;
- retries;
- races;
- resource behavior.

Echo listens to those emitted signals and uses them to reconstruct hidden runtime behavior and investigate causal hypotheses.

Echo is not merely passive monitoring. Her role is investigative: observed effects are used to infer and test explanations of underlying behavior.

Runtime execution remains permission-gated.

Echo does **not** gain project-execution or production-access authority merely because additional runtime evidence would be useful.

**Characteristic question:**

> What do the signals tell us happened?

**Natural usage:**

- “Ask Echo what caused the latency spike.”
- “Run this scenario through Echo.”
- “Echo traced the stalls to lock contention.”
- “Echo cannot establish the cause without authorized runtime evidence.”

---

### 3.6 Harmia — API / Contract Assurance

**Capability:** API / Contract Assurance  
**Identity:** Harmia  
**Origin:** Personified compression inspired by Harmonia, the classical personification of harmony and concord.

Harmia represents the capability whose central concern is:

> **Do independently evolving systems still agree well enough to interact correctly?**

Harmia examines compatibility across:

- consumers and providers;
- schemas;
- APIs;
- protocols;
- events;
- SDKs;
- versions;
- behavioral expectations;
- failure semantics;
- compatibility windows.

Her concept of harmony is stronger than simple structural equality. Two sides may have compatible schemas and still disagree behaviorally.

Harmia identifies where agreement holds, where it fails, and what assumptions remain unverified.

Harmia does **not** authorize interface changes or force consumers/providers to migrate.

**Characteristic question:**

> Do both sides still agree?

**Natural usage:**

- “Ask Harmia whether v3 breaks existing consumers.”
- “Run the contract through Harmia.”
- “Harmia found structural compatibility but behavioral disagreement.”
- “Harmia says the compatibility window is incomplete.”

---

### 3.7 Iris — UI / Browser Assurance

**Capability:** UI / Browser Assurance  
**Identity:** Iris  
**Origin:** Greek Iris; the iris of the eye; visual perception and mediation.

Iris represents the capability whose central concern is:

> **What does the user actually see, perceive, and experience through the delivered interface?**

Iris exercises and observes real user-facing behavior through controlled browser environments, including:

- journeys;
- navigation;
- forms;
- authentication;
- responsive layouts;
- accessibility;
- keyboard behavior;
- browser errors;
- visual state;
- network failures;
- performance;
- rendered output.

Iris is concerned with delivered experience, not merely static UI source.

Browser execution remains explicitly controlled and permission-aware.

Iris does **not** gain unrestricted browser, credential, production, or external-communication authority.

**Characteristic question:**

> What does the user actually experience?

**Natural usage:**

- “Ask Iris to check checkout on mobile.”
- “Run the signup journey through Iris.”
- “Iris reproduced the failure in Safari.”
- “Iris completed Chrome and Firefox coverage; Safari was unavailable.”

---

### 3.8 Atlas — Infrastructure Assurance

**Capability:** Infrastructure Assurance  
**Identity:** Atlas  
**Origin:** Greek Atlas; bearer of the heavens; also associated with mapping a world and its relationships.

Atlas represents the capability whose central concern is:

> **What supports this system, how is that underlying world structured, and what happens if it changes?**

Atlas examines:

- infrastructure topology;
- resources;
- IAM;
- network boundaries;
- trust relationships;
- replacement effects;
- privilege expansion;
- destructive operations;
- exposure;
- dependencies;
- blast radius;
- rollback considerations.

The identity carries two complementary ideas:

1. the structure that bears the system;
2. the map needed to understand that structure.

Atlas may analyze or simulate infrastructure change.

Atlas does **not** possess production apply authority.

**Characteristic question:**

> What is carrying this system, and what moves if this changes?

**Natural usage:**

- “Ask Atlas to assess the infrastructure plan.”
- “Run the Terraform plan through Atlas.”
- “Atlas found an unexpected privilege expansion.”
- “Atlas says this resource is load-bearing for three services.”

---

### 3.9 Janus — Database / Migration Assurance

**Capability:** Database / Migration Assurance  
**Identity:** Janus  
**Origin:** Roman Janus; thresholds, gateways, transitions, beginnings and endings, with backward- and forward-looking perspective.

Janus represents the capability whose central concern is:

> **Can the system safely cross from the current state to the intended future state?**

Migration assurance must reason about both sides of a transition simultaneously:

```text
old application ↔ old schema
old application ↔ new schema
new application ↔ old schema
new application ↔ new schema
```

Janus examines:

- destructive changes;
- locks;
- rewrites;
- nullability;
- index changes;
- backfills;
- rollout sequencing;
- version overlap;
- forward compatibility;
- backward compatibility;
- rollback;
- irreversible transformations;
- dual-read/write transitions.

Janus may evaluate a migration plan and its declared operating conditions.

Janus does **not** possess production database mutation authority.

**Characteristic question:**

> Is the passage safe on both sides of the transition?

**Natural usage:**

- “Ask Janus to review the migration.”
- “Run this schema change through Janus.”
- “Janus says the destination is valid, but the transition is unsafe while old application instances remain.”
- “Janus requires a staged rollout.”

---

### 3.10 Sibyl — Release Assurance

**Capability:** Release Assurance  
**Identity:** Sibyl  
**Origin:** Classical Sibyl; interpreter of signs and conditions who offers foresight without possessing execution authority.

Sibyl represents the capability whose central concern is:

> **What do all available signs indicate about the readiness of this exact release candidate?**

Sibyl is primarily an evidence aggregator and readiness interpreter.

She may consume durable results from sibling capabilities, including:

```text
Verity
Titra
Ortha
Genea
Echo
Harmia
Iris
Atlas
Janus
```

as well as artifact identity, provenance, release policy, and other declared evidence.

Sibyl synthesizes those signs into bounded readiness conclusions such as:

- ready;
- ready with exceptions;
- not ready;
- incomplete;
- indeterminate.

Sibyl's identity intentionally preserves the distinction between **foresight** and **authority**.

Sibyl may assess whether conditions favor proceeding.

Sibyl does **not** publish, tag, deploy, submit, roll out, or otherwise authorize release.

**Characteristic question:**

> What do all the signs tell us about proceeding?

**Natural usage:**

- “Ask Sibyl about RC-12.”
- “What does Sibyl say about the release?”
- “Sibyl reports ready with exceptions.”
- “Sibyl cannot establish readiness because Janus is incomplete.”

---

## 4. Family Character Model

The canonical identities form a family of specialist evidence-producing characters:

```text
Verity
    seeks truth.

Titra
    demands demonstration.

Ortha
    checks alignment.

Genea
    reconstructs lineage.

Echo
    interprets emitted signals.

Harmia
    tests agreement across boundaries.

Iris
    experiences what the user perceives.

Atlas
    understands the supporting world.

Janus
    examines both sides of transition.

Sibyl
    reads the accumulated signs.
```

The characters are intentionally differentiated.

They MUST NOT be treated as autonomous project authorities merely because they are anthropomorphized.

Character identity is a product and interaction device.

Architectural authority remains governed by the capability-family rules:

> **Capabilities determine domain-specific evidence. Harnesses determine trust, authority, project meaning, and downstream action.**

---

## 5. Conversational Usage

Character names MAY be used as the primary conversational identity of a capability.

Preferred forms include:

```text
Ask Verity to audit the repository.
Run that claim through Titra.
Have Ortha check the implementation against the ADR.
Ask Genea where the package came from.
Have Echo investigate the latency spike.
Run the API change through Harmia.
Ask Iris to test the checkout journey.
Have Atlas assess the infrastructure plan.
Run the migration through Janus.
Ask Sibyl whether the release evidence is complete.
```

Avoid constructions that incorrectly imply authority, such as:

```text
Verity approved the fix.
Titra authorized the merge.
Atlas approved the infrastructure apply.
Janus authorized the migration.
Sibyl approved the release.
```

Preferred language is evidence-centered:

```text
Verity found...
Titra demonstrated...
Ortha identified...
Genea traced...
Echo observed...
Harmia detected...
Iris reproduced...
Atlas assessed...
Janus concluded...
Sibyl reports...
```

---

## 6. No Nicknames or Aliases

The family intentionally uses the canonical names directly.

The following practices are not part of the naming model:

- nickname forms;
- abbreviated character names;
- alternate mythological names;
- internal versus external character names;
- formal-name/informal-name pairs;
- acronym expansions retrofitted onto character identities.

Examples:

```text
Verity  — not "Vera"
Titra   — not "Tit"
Ortha   — not "Ort"
Genea   — not "Gen"
Harmia  — not "Harmony"
```

This rule preserves identity consistency across:

- documentation;
- Agent Skills;
- CLI help and projections where character naming is used;
- harness integrations;
- UI;
- reports;
- capability-family documentation;
- future product materials.

Technical capability IDs, repository names, CLI commands, and protocol identifiers MAY remain descriptive rather than character-based where that improves machine clarity.

For example:

```text
Character identity:
Verity

Technical capability:
Universal Code Audit

Possible capability ID:
universal-code-audit

Possible CLI:
uca
```

Character identity MUST NOT make machine-facing contracts less explicit.

---

## 7. Identity Versus Product Authority

Anthropomorphic identities MUST NOT weaken the family authority model.

A character may say, in product language:

```text
"Janus found the migration unsafe under the declared rollout conditions."
```

That statement means:

```text
The Database / Migration Assurance capability produced evidence
and a conclusion under its declared scope and completion state.
```

It does not mean:

```text
Janus possesses authority over the database.
```

Likewise:

```text
"Sibyl says the release is ready."
```

means:

```text
Release Assurance found that the declared readiness criteria were
satisfied by the available evidence.
```

It does not mean:

```text
The release has been authorized.
```

All normal requirements concerning provenance, completion, permissions, limitations, and evidence remain controlling.

---

## 8. Cohesion Rule for Future Capabilities

Future standalone capabilities SHOULD follow the same naming philosophy, but MUST NOT force a weak classical or mythological mapping merely for family uniformity.

A future identity should satisfy most of the following:

1. **Behavioral correspondence** — the underlying figure, concept, or mechanism behaves meaningfully like the capability.
2. **Epistemic correspondence** — the identity helps explain how the capability comes to know what it knows.
3. **Distinct identity** — it feels like an individual member of the family.
4. **Conversational naturalness** — “Ask ___” and “Run this through ___” sound natural.
5. **Pronounceability** — normally two to three syllables, unless a stronger identity clearly justifies otherwise.
6. **Authority correctness** — the archetype does not imply powers the capability does not possess.
7. **Semantic durability** — the rationale should remain meaningful as the capability matures.

The goal is not stylistic sameness.

The goal is a family in which each character feels **inevitable once its role is understood**.

---

## 9. Canonical Family Statement

The identities should reinforce, not replace, the governing architecture:

> **Keep the harness small. Make external intelligence strong. Connect them through narrow, evidence-centered contracts.**

> **Capabilities determine domain-specific evidence. Harnesses determine trust, authority, project meaning, and downstream action.**

> **Verity, Titra, Ortha, Genea, Echo, Harmia, Iris, Atlas, Janus, and Sibyl are specialist identities—not autonomous authorities.**
