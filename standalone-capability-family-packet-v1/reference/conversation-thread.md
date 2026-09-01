# Conversation Thread

**Classification:** Historical source material  
**Coverage:** See [`transcript-coverage.md`](transcript-coverage.md).  
**Authority:** Non-normative; later canonical artifacts supersede conversational wording where they differ.

## Turn 001

**Role:** User  
**Date/time:** Not available in retained visible message context

# Universal Codebase Quality, Maintainability, and Optimization Audit

Act as a senior software architect, staff/principal engineer, code-quality specialist, performance engineer, and software-maintainability researcher.

## Objective

Investigate the strongest **language- and framework-agnostic methods for systematically improving an arbitrary codebase** beyond conventional cyclomatic-complexity analysis.

I want to understand:

> **What analyses, metrics, heuristics, architectural audits, static/dynamic techniques, and engineering practices can be applied across almost any codebase to identify opportunities to make it simpler, cleaner, more maintainable, more modular, more efficient, more performant, more reliable, and easier to evolve?**

The goal is not to maximize abstract code-quality scores or mechanically enforce stylistic rules.

The goal is to identify techniques that reveal **real structural problems and high-value improvement opportunities** while avoiding premature optimization, unnecessary abstraction, over-engineering, metric gaming, or refactoring code that is already adequate.

---

# 1. Go Beyond Cyclomatic Complexity

Start with cyclomatic complexity as only one signal.

Identify complementary or superior techniques for detecting:

* overly complex functions;
* overly complex modules;
* difficult control flow;
* excessive branching;
* deeply nested logic;
* excessive state;
* difficult-to-understand execution paths;
* high cognitive burden;
* hidden coupling;
* architectural complexity that function-level metrics fail to expose.

Consider measures such as, where useful:

* cognitive complexity;
* NPath complexity;
* Halstead metrics;
* maintainability index;
* nesting depth;
* function/method length;
* parameter count;
* fan-in / fan-out;
* dependency depth;
* coupling;
* cohesion;
* instability;
* structural complexity;
* data-flow complexity;
* change complexity;
* entropy or concentration measures.

For each, explain what it actually reveals, its limitations, and whether it is worth using in modern engineering practice.

---

# 2. Code Smell and Structural Analysis

Determine which analyses can systematically detect problems such as:

* duplicated code;
* near-duplicate implementations;
* dead code;
* unreachable code;
* unused dependencies;
* unused exports or APIs;
* obsolete compatibility layers;
* unnecessary wrappers;
* excessive indirection;
* primitive obsession;
* shotgun surgery;
* feature envy;
* god classes/modules;
* overly large files;
* long parameter lists;
* excessive global/shared state;
* mutable state proliferation;
* inappropriate inheritance;
* unnecessary abstractions;
* leaky abstractions;
* speculative generality;
* repeated conditionals;
* inappropriate layering;
* poor responsibility boundaries.

Distinguish between reliably detectable problems and smells that require architectural or human judgment.

---

# 3. Modularity, Coupling, and Cohesion

Explain how to evaluate whether a codebase is decomposed appropriately.

Investigate techniques for measuring or identifying:

* module cohesion;
* inter-module coupling;
* dependency direction;
* dependency cycles;
* highly connected modules;
* unstable dependencies;
* inappropriate cross-layer access;
* package/module boundaries;
* architectural erosion;
* responsibility leakage;
* shared utility dumping grounds;
* inappropriate reuse;
* duplicated domain concepts;
* overly fragmented abstractions.

Include dependency-graph and graph-analysis techniques where useful.

Determine how to distinguish:

* healthy modularity;
* insufficient modularity;
* excessive fragmentation;
* unnecessary abstraction.

---

# 4. Architecture Fitness

Identify methods for testing whether the implementation still reflects the intended architecture.

Consider:

* dependency rules;
* architecture tests;
* fitness functions;
* layer enforcement;
* module boundary enforcement;
* API boundary validation;
* domain boundary validation;
* forbidden dependencies;
* dependency-cycle detection;
* architectural decision conformance;
* architecture drift detection.

Explain how these could become automated checks rather than occasional manual reviews.

---

# 5. Duplication and Reuse

Go beyond exact copy/paste detection.

Investigate approaches for finding:

* syntactic duplication;
* semantic duplication;
* duplicated business rules;
* duplicated schemas;
* duplicated validation logic;
* duplicated transformations;
* parallel abstractions that solve the same problem differently;
* redundant utilities;
* repeated configuration;
* similar code paths that should potentially converge.

Also explain when duplication is preferable to abstraction.

Avoid assuming that every duplicate should be generalized.

---

# 6. Dead Code and Codebase Reduction

Investigate techniques for discovering opportunities to **remove code entirely**.

Include:

* unreachable code;
* unused exports;
* unused functions/classes;
* unused dependencies;
* obsolete features;
* abandoned feature flags;
* stale configuration;
* compatibility code no longer required;
* redundant adapters;
* deprecated interfaces;
* redundant tests;
* obsolete scripts/tooling;
* generated artifacts accidentally committed;
* unnecessary transitive dependencies.

Treat **code deletion and simplification** as first-class optimization strategies.

---

# 7. Dependency Health

Develop a general-purpose dependency audit.

Consider:

* unnecessary dependencies;
* dependency duplication;
* overlapping libraries;
* excessively heavy dependencies;
* dependency trees;
* transitive dependency explosion;
* stale dependencies;
* unsupported dependencies;
* risky dependencies;
* vulnerable dependencies;
* circular dependencies;
* tight coupling to vendor/framework APIs;
* dependency substitution opportunities;
* functionality that could reasonably use standard-library/platform capabilities instead.

Distinguish dependency modernization from unnecessary upgrade churn.

---

# 8. Performance and Efficiency

Determine how to identify actual performance problems without relying on speculative micro-optimization.

Include:

* CPU profiling;
* memory profiling;
* allocation analysis;
* I/O profiling;
* database/query profiling;
* network profiling;
* concurrency analysis;
* lock contention;
* async/task bottlenecks;
* serialization/deserialization cost;
* caching effectiveness;
* algorithmic complexity;
* unnecessary repeated computation;
* N+1 operations;
* excessive copying;
* memory retention/leaks;
* startup time;
* build time;
* test-suite execution time;
* bundle/binary size where relevant.

Explain which issues can be found statically and which require runtime measurement.

Emphasize **measurement before optimization**.

---

# 9. Algorithmic and Data-Structure Analysis

Identify techniques for finding code where poor algorithmic choices create avoidable complexity or performance problems.

Evaluate:

* time complexity;
* space complexity;
* repeated traversals;
* inefficient searches;
* unnecessary sorting;
* nested iteration;
* inappropriate data structures;
* repeated parsing;
* redundant transformations;
* repeated database/network operations;
* excessive intermediate allocations.

Explain how automated tooling could identify likely hotspots without assuming every nested loop is problematic.

---

# 10. Data Flow and State Management

Analyze ways to detect unnecessary complexity caused by how information and state move through the system.

Look for:

* excessive mutable state;
* hidden state changes;
* excessive shared state;
* duplicated state;
* state synchronization;
* long data-transformation pipelines;
* unnecessary conversions;
* excessive serialization boundaries;
* global state;
* temporal coupling;
* implicit dependencies;
* unclear ownership;
* mutation across module boundaries.

Explain what architectural improvements these patterns may suggest.

---

# 11. API and Interface Quality

Develop methods for assessing internal and external interfaces.

Consider:

* unnecessarily large interfaces;
* too many parameters;
* poorly modeled return types;
* inconsistent APIs;
* leaking implementation details;
* excessive optional parameters;
* unclear contracts;
* weak invariants;
* duplicated interfaces;
* inconsistent error behavior;
* unstable APIs;
* inappropriate exposure of internals.

Include ways to identify APIs that are harder to use correctly than incorrectly.

---

# 12. Type and Domain Modeling Quality

Where applicable, assess whether the codebase represents domain concepts effectively.

Look for:

* excessive use of primitive types;
* weakly modeled states;
* invalid states that can be represented;
* excessive nullability;
* stringly typed logic;
* duplicated enums/constants;
* incomplete state machines;
* ambiguous data structures;
* overly generic dictionaries/maps/objects;
* domain rules scattered throughout the codebase.

Explain how stronger modeling can reduce both code volume and runtime defensive logic.

---

# 13. Error Handling and Reliability

Identify methods for finding:

* swallowed errors;
* overly broad exception handling;
* inconsistent error handling;
* retry storms;
* missing timeouts;
* missing cancellation;
* resource leaks;
* improper cleanup;
* silent partial failure;
* inconsistent transaction boundaries;
* unsafe fallback behavior;
* unhandled failure modes.

Include resilience and correctness rather than treating cleanliness as purely aesthetic.

---

# 14. Concurrency and Asynchronous Complexity

Where applicable, evaluate:

* race conditions;
* deadlocks;
* lock contention;
* improper shared state;
* blocking calls in async paths;
* excessive task/thread creation;
* unsafe cancellation;
* ordering assumptions;
* duplicated asynchronous work;
* poor backpressure handling.

Identify both static and dynamic approaches.

---

# 15. Testing Quality

Do not judge test quality only by line coverage.

Investigate:

* branch coverage;
* mutation testing;
* property-based testing;
* invariant testing;
* contract testing;
* integration testing;
* architecture testing;
* flaky-test detection;
* redundant tests;
* slow tests;
* test dependency coupling;
* excessive mocking;
* implementation-detail testing;
* missing edge cases.

Explain how to identify areas that are technically covered but poorly protected against regressions.

---

# 16. Changeability and Repository History

Explore how version-control history can reveal problems that static analysis cannot.

Consider:

* change frequency;
* defect frequency;
* churn;
* files frequently changed together;
* hotspots combining complexity and churn;
* temporal coupling;
* modules repeatedly involved in regressions;
* code ownership concentration;
* areas frequently reverted;
* long-lived unfinished migrations.

Pay particular attention to **complexity × churn** and similar combinations that better identify real maintenance risk than complexity alone.

---

# 17. Documentation and Comprehensibility

Develop methods for detecting areas where the implementation is unnecessarily difficult to understand.

Consider:

* unclear naming;
* excessive comments compensating for confusing code;
* missing explanation of architectural decisions;
* stale comments;
* stale documentation;
* undocumented invariants;
* undocumented public APIs;
* inconsistent terminology;
* duplicate concepts with different names;
* excessive conceptual vocabulary.

Do not assume that more comments or documentation automatically means better maintainability.

---

# 18. Build and Tooling Complexity

Treat the surrounding development system as part of the codebase.

Audit:

* build scripts;
* task runners;
* CI/CD configuration;
* code generation;
* environment setup;
* test infrastructure;
* local development tooling;
* deployment configuration;
* formatting/linting configuration;
* duplicated automation;
* unnecessary custom tooling.

Look for opportunities to reduce the number of moving parts required to understand, build, test, and ship the project.

---

# 19. Repository and Project Structure

Evaluate structural hygiene such as:

* unclear directory organization;
* excessively deep directory trees;
* dumping-ground folders;
* ambiguous module ownership;
* mixed concerns;
* inconsistent organization;
* generated code mixed with authored code;
* misplaced configuration;
* excessive root-level files;
* fragmented project configuration.

Explain when restructuring actually creates value versus merely rearranging files.

---

# 20. Security as a Quality Dimension

Include broadly applicable security-oriented code-quality analysis such as:

* unsafe input handling;
* injection risks;
* secret exposure;
* insecure defaults;
* unsafe deserialization;
* authentication/authorization boundary violations;
* excessive permissions;
* vulnerable dependencies;
* weak cryptographic usage;
* filesystem/path vulnerabilities;
* unsafe shell execution;
* SSRF and similar trust-boundary problems where relevant.

Focus on techniques that can be incorporated into general repository health auditing.

---

# 21. Observability and Diagnosability

Assess whether the system makes failures understandable.

Consider:

* structured logging;
* useful error context;
* metrics;
* traces;
* correlation IDs;
* excessive logging;
* missing diagnostic information;
* inconsistent instrumentation;
* instrumentation coupled too deeply to business logic.

Determine how diagnosability affects maintainability and operational quality.

---

# 22. Consistency and Standardization

Identify harmful inconsistency in:

* naming;
* patterns;
* error handling;
* data access;
* dependency injection;
* configuration;
* testing;
* logging;
* serialization;
* validation;
* API design;
* concurrency;
* module organization.

Distinguish valuable consistency from blindly enforcing a single pattern everywhere.

---

# 23. Detect Over-Engineering

Explicitly include analyses for the opposite problem: code that is **too abstract or too engineered**.

Look for:

* unnecessary interfaces;
* one-implementation abstractions;
* unnecessary factories;
* excessive indirection;
* premature generalization;
* excessive configuration;
* speculative extension points;
* unnecessary plugin systems;
* wrapper-on-wrapper architecture;
* unnecessary event systems;
* overly elaborate dependency injection;
* abstractions that increase rather than reduce cognitive load.

Treat **de-abstraction and collapsing unnecessary layers** as legitimate refactoring strategies.

---

# 24. Identify Simplification Opportunities

Develop a systematic way to ask:

> What could this codebase stop doing?

Look for opportunities to:

* delete code;
* merge concepts;
* collapse abstractions;
* consolidate modules;
* remove dependencies;
* eliminate configuration;
* replace custom implementations with platform capabilities;
* eliminate unnecessary layers;
* reduce state;
* reduce transformations;
* reduce interfaces;
* reduce deployment/build complexity;
* reduce the number of concepts a developer must understand.

Treat conceptual simplicity as an important optimization target.

---

# 25. Combine Signals Rather Than Ranking by One Metric

Determine which combinations of signals are especially powerful.

For example:

* complexity × churn;
* complexity × defect history;
* size × churn;
* coupling × change frequency;
* fan-in × instability;
* duplication × churn;
* dependency centrality × vulnerability;
* test weakness × change frequency;
* performance cost × execution frequency.

Develop a methodology for finding **high-value hotspots** rather than producing hundreds of low-priority warnings.

---

# 26. Automated vs. Judgment-Based Analysis

For every proposed technique, classify it as:

* fully automatable;
* mostly automatable;
* AI-assisted;
* human architectural judgment required.

Also identify which techniques are suitable for:

* static analysis;
* dynamic analysis;
* repository-history analysis;
* dependency-graph analysis;
* runtime profiling;
* test analysis;
* architecture analysis;
* LLM/agent-assisted semantic analysis.

---

# 27. Tooling Landscape

Identify strong tools or tool categories that implement these techniques across major ecosystems.

Prefer tools that are:

* mature;
* actively maintained;
* automatable;
* CI-compatible;
* machine-readable;
* usable locally;
* relatively language-independent where possible.

Do not simply produce a large tool catalog.

For each tool, explain which specific part of the methodology it addresses and whether the underlying technique could be implemented independently.

---

# 28. Develop a Universal Codebase Audit Framework

Synthesize the research into a practical framework that could be run against almost any repository.

Organize it into stages such as:

### Stage 1 — Repository Discovery

Understand the project, languages, frameworks, structure, tooling, and architecture.

### Stage 2 — Static Structural Analysis

Complexity, duplication, smells, dependencies, dead code, coupling, cohesion.

### Stage 3 — Architectural Analysis

Boundaries, dependency direction, modularity, responsibility allocation, architecture drift.

### Stage 4 — Historical Analysis

Churn, hotspots, temporal coupling, defect concentration.

### Stage 5 — Test and Correctness Analysis

Coverage quality, mutation resistance, flaky tests, missing invariants.

### Stage 6 — Runtime Analysis

CPU, memory, I/O, database, concurrency, startup/build/test performance.

### Stage 7 — Simplification Analysis

Code deletion, dependency reduction, abstraction collapse, consolidation.

### Stage 8 — Prioritization

Combine evidence into a ranked set of improvements.

---

# 29. Produce a Codebase Health Model

Develop a practical taxonomy such as:

* **Complexity**
* **Comprehensibility**
* **Cohesion**
* **Coupling**
* **Modularity**
* **Duplication**
* **Dead Weight**
* **Dependency Health**
* **Architecture**
* **Correctness**
* **Testability**
* **Reliability**
* **Performance**
* **Security**
* **Operability**
* **Changeability**
* **Consistency**
* **Simplicity**

Determine whether these dimensions are sufficient or should be changed.

Avoid reducing everything to a single misleading numeric score unless there is a defensible reason to do so.

---

# 30. Prioritization Model

For every detected issue, consider:

**Impact**

* correctness;
* maintainability;
* performance;
* reliability;
* security;
* developer productivity.

**Evidence**

* static evidence;
* runtime evidence;
* repository-history evidence;
* test evidence;
* architectural evidence.

**Cost**

* effort;
* migration risk;
* regression risk;
* architectural disruption.

**Confidence**

* confirmed;
* strongly indicated;
* speculative.

Develop a prioritization model approximately based on:

> **Priority = Expected Benefit × Evidence Confidence ÷ Cost and Risk**

Do not recommend refactoring merely because a metric crossed an arbitrary threshold.

---

# 31. Distinguish Findings From Recommendations

For every meaningful issue, report:

**Finding**
What was observed.

**Evidence**
Why it appears problematic.

**Consequence**
Why it matters.

**Recommendation**
What should change.

**Expected Benefit**
What improvement should result.

**Risk**
What could go wrong when changing it.

**Validation**
How to prove the change actually improved the system.

---

# 32. Final Deliverable

Produce:

1. **The strongest universally applicable codebase-improvement techniques**, ranked by usefulness.
2. **What each technique detects.**
3. **Where each technique produces false positives or misleading conclusions.**
4. **Whether it can be automated.**
5. **Recommended metrics and thresholds where defensible.**
6. **High-value combinations of metrics/signals.**
7. **Recommended open-source or commercial tooling where appropriate.**
8. **A language-independent repository audit workflow.**
9. **A prioritization system for converting findings into actionable work.**
10. **A reusable checklist or machine-executable audit specification.**
11. **A minimal version suitable for continuous CI use.**
12. **A deeper periodic audit suitable for architectural maintenance.**

Conclude with a proposed:

# Universal Codebase Improvement Stack

Organize the final recommendation into three tiers:

### Tier 1 — Continuous

Fast, deterministic checks appropriate for every commit or pull request.

### Tier 2 — Periodic

Deeper repository, dependency, architecture, and historical analysis run periodically.

### Tier 3 — Investigative

Profiling, semantic analysis, architectural review, and other expensive techniques triggered when evidence suggests a problem.

The resulting system should help answer not merely:

> **“Where is the code complicated?”**

but:

> **“Where is this codebase unnecessarily difficult, expensive, risky, slow, coupled, duplicated, fragile, or conceptually heavy—and what is the highest-value way to make it simpler?”**


---

## Turn 002

**Role:** Assistant  
**Date/time:** Not available

# Universal Codebase Quality, Maintainability, and Optimization Audit

## Executive conclusion

Cyclomatic complexity answers one narrow question:

> How many linearly independent control-flow paths exist here?

It does **not** tell you whether the code is frequently changed, defect-prone, architecturally misplaced, operationally important, performance-critical, duplicated, obsolete, over-abstracted, weakly tested, or difficult to diagnose.

A universal codebase audit therefore should not be a larger collection of isolated metrics. It should be an **evidence-fusion system** that answers four broader questions:

1. **Where is reasoning expensive?**
2. **Where does change propagate or repeatedly cause failure?**
3. **Where does runtime or operational cost concentrate?**
4. **What code, state, dependencies, layers, or concepts can be removed?**

Empirical work supports this multi-evidence approach. Structural metrics alone are imperfect predictors of understandability, and cognitive complexity does not eliminate that limitation. Dependency-network measures, change history, defect history, and runtime evidence often add information that local complexity measures miss. Test coverage has a similar limitation: it describes execution, not necessarily fault-detection strength. ([link.springer.com](https://link.springer.com/article/10.1007/s10664-023-10396-7))

The strongest universal model is therefore:

> **Metrics identify candidates. History, tests, runtime evidence, architecture, incidents, and human judgment determine whether change is warranted.**

### Governing principles

1. **Use metrics for ranking, not verdicts.** A threshold crossing is a reason to inspect code, not proof that it is bad.
2. **Use ratchets rather than absolute legacy gates.** Prevent new regressions while gradually reducing existing debt.
3. **Require multiple independent signals for expensive work.** Complexity plus churn is more meaningful than complexity alone.
4. **Treat deletion and de-abstraction as first-class outcomes.** The best refactoring may be to stop doing something.
5. **Measure before performance optimization.** Static suspicion is not runtime proof.
6. **Separate detection from authority.** A detector may nominate dead code, duplication, or an abstraction for removal; it should not automatically perform consequential deletion.
7. **Validate every recommendation.** A refactoring is not complete until maintainability, correctness, performance, or operational improvement has been demonstrated.

---

# 1. Strongest universally applicable techniques

The ranking below reflects broad applicability and likely decision value. The order should change when a repository’s risk profile demands it—for example, a safety-critical service should elevate correctness, security, and failure-path analysis above maintainability hotspots.

| Rank | Technique | What it detects | Why it is powerful | Main limitations | Automation |
|---:|---|---|---|---|---|
| 1 | **Complexity × churn hotspot analysis** | Difficult code that developers repeatedly touch | Focuses attention where maintenance effort actually occurs | History may be distorted by bots, formatting, generated files, vendoring, or migrations | Mostly automatable |
| 2 | **Representative runtime profiling and tracing** | Actual CPU, memory, I/O, database, network, lock, queue, and latency bottlenecks | Replaces speculation with workload evidence | Only valid for represented workloads and environments | Mostly automatable; interpretation required |
| 3 | **Dependency graph and architecture fitness analysis** | Cycles, boundary violations, unstable dependencies, central bottlenecks, architecture erosion | Finds system-level complexity invisible to function metrics | Static dependency extraction can miss reflection, runtime registration, generated wiring, and configuration | Mostly automatable once rules exist |
| 4 | **Failure-path and reliability analysis** | Swallowed errors, unbounded retries, missing deadlines, unsafe partial failure, cleanup failures | Directly targets outages, corruption, hangs, and misleading success | Correct behavior depends heavily on domain contracts | AI-assisted and human-led |
| 5 | **Test-effectiveness analysis** | Technically covered but weakly protected code | Combines branch coverage, mutation, properties, contracts, invariants, and flakiness | Mutation and state-space exploration can be expensive | Mostly automatable |
| 6 | **Reachability and dead-weight analysis** | Code, exports, dependencies, flags, adapters, scripts, and configuration that may be removable | Deletion improves nearly every quality dimension at once | Dynamic loading, reflection, external consumers, and rarely used features create false positives | Mostly automatable with validation |
| 7 | **Temporal coupling and defect-history analysis** | Files or modules that must change together, repeatedly regress, or are frequently reverted | Reveals hidden architectural dependencies and maintenance friction | Commit hygiene and issue-link quality affect precision | Mostly automatable |
| 8 | **Security trust-boundary and data-flow analysis** | Injection, secret exposure, unsafe deserialization, path or shell hazards, authorization bypasses | Treats security as structural quality rather than a separate late-stage check | Business-logic and authorization flaws often require contextual review | Automated plus human |
| 9 | **Multiplex modularity analysis** | Structural, semantic, evolutionary, ownership, and data coupling | Recognizes that coupling and cohesion are multidimensional | Graph boundaries and edge definitions materially affect results | Mostly automatable |
| 10 | **Multi-level duplication analysis** | Exact, near, semantic, business-rule, schema, validation, and configuration duplication | Finds divergence risk and redundant concepts beyond copy/paste | Similarity does not prove that abstraction is desirable | Automated candidate generation; judgment required |
| 11 | **Dependency-health and supply-chain analysis** | Vulnerable, unsupported, duplicative, heavy, unnecessary, or deeply transitive dependencies | Connects maintainability, security, performance, and operational risk | Presence of a vulnerable component does not prove exploitability | Mostly automatable |
| 12 | **State ownership and data-flow analysis** | Shared state, duplicated state, temporal coupling, unclear ownership, conversion pipelines | Often reveals the true source of apparently local complexity | State semantics are difficult to infer completely | AI-assisted and human-led |
| 13 | **API and domain-model analysis** | Weak invariants, primitive obsession, invalid representable states, inconsistent interfaces | Can eliminate defensive code and entire classes of misuse | Requires domain knowledge | AI-assisted and human-led |
| 14 | **Build, test, and delivery-system profiling** | Slow feedback, duplicate automation, cache misses, unnecessary generation, pipeline bottlenecks | Improves every developer interaction with the repository | Build environments can vary significantly | Mostly automatable |
| 15 | **Local structural metrics** | Complex, deeply nested, large, parameter-heavy functions and classes | Cheap, deterministic, and useful as a first-pass filter | Weak when isolated from change and behavioral evidence | Fully automatable |
| 16 | **AI-assisted semantic and simplification review** | Duplicated intent, obsolete compatibility, responsibility leakage, over-engineering, conceptual overload | Addresses problems not represented cleanly in syntax or graphs | Confidence and reproducibility must be managed explicitly | AI-assisted |
| 17 | **Diagnosability and observability analysis** | Failures that are hard to understand after deployment | Reduces time to isolate defects and performance problems | More telemetry can itself increase cost and complexity | Mostly automatable with design review |

History-based ranking is especially valuable: studies have repeatedly found that faults and maintenance effort are highly concentrated rather than evenly distributed. However, modern repositories should remove automated dependency updates, formatting-only changes, vendoring, generated artifacts, and bot activity before calculating churn or ownership signals. ([st.cs.uni-saarland.de](https://www.st.cs.uni-saarland.de/publications/details/kim-icse-2007/))

---

# 2. Complexity and structural metrics

## 2.1 What the major metrics actually reveal

| Metric | What it reveals | What it does not reveal | Modern recommendation |
|---|---|---|---|
| **Cyclomatic complexity** | Number of independent control-flow paths; approximate branch and test burden | Nesting burden, semantic difficulty, state complexity, architecture, change frequency | Retain as a basic function-level signal |
| **Cognitive complexity** | Nested and interrupted control flow that is likely to burden readers | Domain complexity, data coupling, historical difficulty, runtime cost | Useful for ranking; do not treat as a complete maintainability measure |
| **NPath complexity** | Approximate number of acyclic execution paths through a function | Whether paths are feasible, common, important, or already well tested | Use on extreme branching code, preferably log-scaled or percentile-ranked |
| **Maximum nesting depth** | Local control-flow indentation and stacked conditions | Whether nesting is inherently necessary or clearly modeled | One of the simplest and most useful review signals |
| **Function or method length** | Scope size and potential responsibility accumulation | Cohesion, readability, generated patterns, declarative structure | Combine with cohesion, churn, and complexity |
| **File or module size** | Possible responsibility concentration | Whether the module is stable, cohesive, generated, or a necessary table of data | Rank within repository and language rather than using one global limit |
| **Parameter count** | Interface burden, weak grouping, optional-mode explosion | Whether the parameters naturally form a single operation | Review long lists, especially repeated groups and booleans |
| **Halstead measures** | Token/operator/operand volume and derived effort estimates | Domain semantics, architecture, state ownership, actual comprehension | Secondary research or trend signal; not a CI gate |
| **Maintainability Index** | A composite derived from size, Halstead, and complexity, sometimes comments | A stable or universal notion of maintainability | Do not compare across tools, languages, or formula variants; never use alone |
| **Fan-in** | How many clients depend on an entity | Whether those dependencies are appropriate or stable | High fan-in may identify either a healthy core API or a dangerous blast-radius node |
| **Fan-out** | How many other entities an entity depends on | Whether dependencies are trivial, indirect, or aligned with its responsibility | Combine with churn, centrality, and boundary rules |
| **Coupling** | Cross-entity dependency strength | Why the dependency exists or whether it is harmful | Measure multiple coupling types, not only imports or calls |
| **Cohesion or LCOM-like metrics** | Whether members appear to operate on related data or concepts | True domain responsibility and external client usage | Candidate generation only; particularly noisy for utility, orchestration, and framework classes |
| **Instability** | Ratio of outgoing to total afferent/efferent dependencies | Whether the module is intentionally volatile or abstract | Useful for checking dependency direction and stable-core design |
| **Dependency depth** | Long chains between a client and underlying behavior | Whether each intermediary contributes meaningful policy | Stronger when combined with pass-through ratios and change amplification |
| **Strongly connected components** | Groups involved in dependency cycles | Whether a local cycle is acceptable or runtime-only | “No new cross-boundary cycles” is a defensible architecture gate |
| **Graph centrality** | Highly connected or bridging entities | Whether centrality represents essential infrastructure or poor design | Prioritize central nodes when they are also unstable, vulnerable, or frequently changed |
| **Entropy, Gini, or concentration measures** | Concentration of changes, ownership, defects, or dependencies | Quality by themselves | Useful for identifying hotspots and knowledge concentration |
| **Churn and change frequency** | Where development effort and instability concentrate | Whether change is healthy product evolution or problematic rework | Combine with complexity, defects, ownership, and reverts |
| **Defect frequency** | Where known failures have concentrated | Unreported or misclassified defects | High-value when issue linkage and incident data are trustworthy |

Research evaluating understandability metrics found that purely structural models leave substantial unexplained variation and that cognitive complexity should not be treated as a complete replacement for traditional measures. Maintainability Index also varies by formula and tooling, making cross-repository comparisons especially misleading. ([link.springer.com](https://link.springer.com/article/10.1007/s10664-023-10396-7))

## 2.2 Thresholds worth using—and thresholds worth resisting

### Defensible gates

These rules test concrete undesirable states rather than trying to define universal “good code”:

- No new compiler or type errors.
- No new architecture-rule violations.
- No new cross-boundary dependency cycles.
- No newly committed secrets.
- No new high-confidence security finding on a reachable, exposed path without an explicit waiver.
- No unexplained performance regression outside an agreed noise band under a representative benchmark.
- No new flaky test introduced by the change.
- No new unowned public API, dependency, deployment component, or feature flag.
- No increase in a budgeted artifact size without review.

### Useful review heuristics

The following are starting points, not universal laws:

| Signal | Review starting point | Stronger concern when |
|---|---:|---|
| Cyclomatic complexity | Above approximately 10 per changed function | Above 20, increasing, frequently changed, or weakly tested |
| Cognitive complexity | Above approximately 15 | Accompanied by nesting, state mutation, repeated conditionals, or defect history |
| Nesting depth | Four levels | Five or more levels, especially across error and state branches |
| Parameters | More than five to seven | Many booleans, optional values, repeated groups, or unclear ownership |
| Function length | Repository-local upper quartile or roughly 50–100 logical lines | Combined with multiple responsibilities, state mutation, or high churn |
| File or module size | Repository-local top 5–10% | Low cohesion, high fan-out, high change concentration |
| Fan-out | Repository-local upper percentile | Crosses layers or unstable/vendor boundaries |
| Churn | Repository-local upper percentile over a representative window | Also complex, defect-prone, or owned by very few people |

These numbers should trigger review rather than automatic rejection. Even tooling that provides default thresholds treats many of them as configurable conventions rather than universal empirical boundaries. Aggregate cognitive-complexity gates can also behave badly because a growing codebase can fail even when no individual function is unusually difficult. ([sonarsource.com](https://www.sonarsource.com/resources/cognitive-complexity/))

### Poor universal gates

Avoid repository-wide requirements such as:

- “Maintainability Index must exceed 80.”
- “Coverage must exceed 80% everywhere.”
- “Duplication must remain below 3%.”
- “No file may exceed 500 lines.”
- “Every interface must have multiple implementations.”
- “Every nested loop is a performance defect.”
- “Every duplicated block must be abstracted.”
- “Every dependency must be on its latest release.”

A better policy is:

> **No unreviewed regression in changed code, and evidence-based reduction of the most consequential existing hotspots.**

---

# 3. Code-smell and structural-detection reliability

Not all smells are equally automatable.

## 3.1 High-confidence deterministic detections

These can usually be reported as concrete findings:

- Unreachable statements.
- Unused locals, imports, private functions, and private fields.
- Exact code clones.
- Dependency cycles in the modeled graph.
- Explicit forbidden dependency violations.
- Excessive control-flow nesting.
- Broad or empty exception handlers matching precise patterns.
- Committed secrets matching validated detectors.
- Known vulnerable dependency versions.
- Duplicate keys or conflicting configuration.
- Generated or binary artifacts accidentally committed.
- Public API signature changes.
- Resource acquisition paths with mechanically provable missing cleanup.

## 3.2 Mostly automatable candidate detections

These require assumptions to be exposed:

- Unused exports and externally callable APIs.
- Whole-program dead functions or classes.
- Unused dependencies.
- Near-duplicate code.
- Abandoned feature flags.
- Repeated N+1 query shapes.
- Blocking calls in asynchronous paths.
- Missing cancellation propagation.
- Potential lock-order inversions.
- Race-prone check-then-act logic.
- Stale compatibility branches.
- Flaky tests.
- Redundant or overlapping dependencies.
- God classes or modules based on structural clustering.

Whole-program dead-code tools can be sound within a declared model while still missing dynamic registration, assembly linkage, reflection, external consumers, or other runtime mechanisms. Their results should therefore include the reachability root set and known blind spots. ([go.dev](https://go.dev/blog/deadcode))

## 3.3 AI-assisted or semantically inferred candidates

These are valuable but should carry explicit confidence:

- Duplicated business rules expressed differently.
- Parallel abstractions that solve the same problem.
- Primitive obsession.
- Feature envy.
- Responsibility leakage.
- Leaky or unnecessary abstractions.
- Inappropriate layering.
- Weak domain modeling.
- Excessive optionality.
- Speculative extension points.
- Obsolete compatibility behavior.
- Stale comments or architectural documentation.
- Inconsistent terminology for the same domain concept.
- Different concepts misleadingly using the same name.
- Tests that assert implementation details rather than behavior.
- Excessive conceptual vocabulary.

## 3.4 Human architectural judgment required

Human judgment remains authoritative for:

- Intended module and domain boundaries.
- Whether duplication is intentionally independent.
- Whether a central module is a healthy platform capability or a god module.
- Whether an interface represents a real policy boundary.
- Whether a compatibility layer can be removed.
- Whether a domain concept deserves a type.
- Whether a performance tradeoff is justified.
- Whether an error should fail open, fail closed, retry, compensate, or abort.
- Whether a module should be split, merged, relocated, or left alone.
- Whether a migration is sufficiently complete to remove its old path.

The correct model is not “automated versus manual.” It is:

> **Automated discovery → semantic interpretation → governed decision → validated change.**

---

# 4. Modularity, coupling, cohesion, and architecture fitness

## 4.1 Model the codebase as a multiplex graph

A single import graph is insufficient. Build several overlapping graphs whose nodes may be functions, types, files, packages, services, schemas, databases, build targets, or deployment units.

### Structural edges

- Imports and includes.
- Calls and method invocations.
- Type references.
- Inheritance and interface implementation.
- Field or data access.
- Event production and consumption.
- Database-table access.
- Schema dependencies.
- Configuration references.
- Build-target dependencies.
- Runtime service calls.

### Evolutionary edges

- Files changed in the same commit.
- Files changed under the same work item.
- Entities commonly involved in the same defect fix.
- Entities repeatedly reverted together.
- Entities modified during the same migration.

### Semantic edges

- Identifier and terminology similarity.
- Shared domain vocabulary.
- Similar validation or transformation behavior.
- Similar comments and documentation.
- Equivalent state transitions or business rules.

### Socio-technical edges

- Shared owners.
- Cross-team review requirements.
- Expertise concentration.
- Handoff frequency.
- Components maintained by a single individual or team.

Research comparing modularity signals finds that no single coupling concept dominates. Structural, evolutionary, semantic, ownership, inheritance, and clone relationships expose different aspects of the system. Combining them is generally more informative than optimizing one coupling metric. ([researchgate.net](https://www.researchgate.net/publication/221560364_On_the_congruence_of_modularity_and_code_coupling))

## 4.2 High-value graph analyses

### Strongly connected components

Use strongly connected components to find cycles and rank them by:

- Number of modules involved.
- Number and weight of internal edges.
- Churn.
- Defect history.
- ownership breadth.
- Runtime criticality.
- Whether the cycle crosses intended layers or domains.

A two-module cycle inside one tightly cohesive subsystem is different from a cycle joining UI, domain, persistence, and infrastructure.

### In-degree, out-degree, and centrality

Use:

- **High in-degree** to find widely depended-upon APIs.
- **High out-degree** to find coordinators or dependency-heavy modules.
- **Betweenness centrality** to find bridge modules through which many paths pass.
- **Eigenvector or influence centrality** to find nodes connected to other important nodes.
- **Articulation points** to find structural bottlenecks.
- **Reachability and transitive fan-out** to estimate change or failure blast radius.

Network measures have successfully identified defect-prone components missed by conventional complexity models in large systems, but replications also indicate that their value can be smaller in simpler projects. Use them as repository-scale prioritizers, not universal defect predictors. ([microsoft.com](https://www.microsoft.com/en-us/research/publication/predicting-defects-using-network-analysis-on-dependency-graphs/))

### Community detection

Compare algorithmically detected communities with declared package or service boundaries.

Investigate when:

- A declared module is consistently divided into several graph communities.
- One detected community spans several declared domains.
- Co-change communities disagree with import boundaries.
- Ownership communities cut across architectural boundaries.
- Methods within a large class form stable responsibility clusters.

Community detection is a candidate generator. It does not know the intended domain model.

### Dependency direction and instability

For a module:

\[
I=\frac{C_e}{C_a+C_e}
\]

where \(C_e\) is outgoing or efferent coupling and \(C_a\) is incoming or afferent coupling.

This is useful when interpreted directionally:

- Stable, widely depended-upon modules should usually avoid depending on volatile details.
- Volatile feature modules may depend on stable capabilities.
- A high-fan-in, high-churn, concrete module deserves review.
- A low-level module depending on UI, application orchestration, or vendor details may indicate inversion failure.

Do not attempt to maximize or minimize instability everywhere.

## 4.3 Healthy, insufficient, and excessive modularity

### Healthy modularity

Healthy boundaries tend to exhibit:

- Internally cohesive changes.
- Explicit, relatively small APIs.
- Intended dependency direction.
- Few or governed cycles.
- Clear ownership.
- Independently testable behavior.
- Independent rates of change where that matters.
- Encapsulated state and invariants.
- Vendor and framework details kept behind deliberate boundaries.
- Limited cross-team coordination for ordinary changes.

### Insufficient modularity

Common evidence includes:

- Shotgun surgery across unrelated directories.
- Frequent cross-boundary co-change.
- Layer reach-through.
- Shared mutable state.
- Circular dependencies.
- Direct access to another module’s storage or internals.
- Duplicate domain concepts in multiple modules.
- A central utility package that every feature modifies.
- Feature work requiring many teams for reasons unrelated to product scope.
- Repeated boundary exceptions.

### Excessive fragmentation

Warning signs include:

- Many modules with only one caller and no independent policy.
- One-line pass-through functions or wrapper chains.
- Deep dependency pathways.
- Interfaces that merely rename an underlying API.
- Factories that always choose one implementation.
- Configuration required to assemble a fixed object graph.
- Events used for simple in-process control flow.
- Numerous “manager,” “provider,” “handler,” “adapter,” and “service” concepts with indistinct responsibilities.
- A change requiring navigation across many tiny files without reducing coupling.
- Abstractions that do not support independent testing, replacement, security, ownership, or evolution.

A one-implementation interface is not automatically wasteful. It may represent a security boundary, external contract, test seam, platform port, ownership boundary, or deliberate dependency inversion. It becomes suspect when none of those benefits exists.

---

# 5. Automated architecture fitness

Architecture fitness functions turn architectural intent into executable constraints.

## 5.1 Rules worth automating

- Domain modules may not depend on presentation or deployment modules.
- Business logic may not import a web framework.
- Only repository or persistence adapters may access the database client.
- Feature modules may use another feature only through its public API.
- Internal packages may not be imported externally.
- Authorization checks must occur at designated trusted boundaries.
- Vendor SDKs may be referenced only from adapter modules.
- Generated code may not be modified manually.
- Service-to-service calls must pass through designated clients.
- Events must have declared owners and schemas.
- No new dependency cycles.
- No direct filesystem or process execution outside designated infrastructure modules.
- Deprecated APIs may not receive new callers.
- Only migration code may depend on both the old and new subsystems.
- Public APIs must have ownership and compatibility metadata.

Tools such as ArchUnit and ArchUnitNET let teams express dependency, layering, package, and cycle rules as executable tests. The same technique can be implemented independently by extracting a dependency graph and evaluating declarative predicates. ([archunit.org](https://www.archunit.org/))

## 5.2 Architecture-reflexion workflow

1. Declare the intended high-level model.
2. Map implementation entities to model elements.
3. Extract implementation dependencies.
4. Compare intended and actual relationships.
5. Classify:
   - **Convergence:** expected and present.
   - **Divergence:** present but forbidden or unexpected.
   - **Absence:** intended but not represented.
6. Baseline known divergences.
7. Prevent new divergences.
8. Periodically review whether the intended model itself is still correct.

This follows the software-reflexion-model approach: compare an explicit intended architecture with implementation evidence rather than assuming the package tree is the architecture. ([cs.ubc.ca](https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html))

## 5.3 Declare detector blind spots

Architecture checks should publish a coverage statement:

```yaml
dependency_model:
  sees:
    - imports
    - static_calls
    - type_references
    - inheritance
    - generated_sources
  does_not_see:
    - reflection
    - runtime_plugin_discovery
    - dependency_injection_by_configuration
    - database_stored_procedure_calls
    - dynamically_constructed_service_names
```

Research comparing architecture-compliance tools found meaningful differences in the dependency constructs each tool could identify. An architecture test is only as complete as its extraction model. ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/full/10.1002/spe.2421))

---

# 6. Duplication and reuse

## 6.1 Analyze duplication at several levels

| Level | Detection method | Example |
|---|---|---|
| Exact | Text, token, or normalized token matching | Copied function with formatting differences |
| Parameterized | Identifier and literal normalization | Same algorithm with renamed variables |
| Structural | Abstract syntax tree or control-flow similarity | Same branching structure expressed differently |
| Semantic | Program dependence, data flow, symbolic behavior, embeddings | Equivalent transformation with reordered statements |
| Business-rule | Rule extraction and semantic review | Same eligibility rule in API, batch job, and UI |
| Schema | Schema and type comparison | Customer address represented differently in several services |
| Validation | Constraint comparison | Different email or currency validation paths |
| Transformation | Source-to-target mapping comparison | Parallel JSON-to-domain conversion pipelines |
| Configuration | Normalized configuration and policy comparison | Repeated deployment or permission settings |
| Conceptual | Domain vocabulary and responsibility analysis | Two “pricing engines” with diverging behavior |

Clone research conventionally distinguishes exact, renamed, near-miss, and semantic clones. Syntax-only methods cannot reliably detect behaviorally similar implementations with reordered or differently structured control flow. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0167642309000367))

## 6.2 Rank duplication rather than eliminating it indiscriminately

A useful duplication-risk model is:

\[
D_r = Similarity \times Churn \times DivergenceRisk \times DefectEvidence \times OwnershipDistance
\]

High-value candidates have several of these properties:

- Both copies change repeatedly.
- One copy is fixed while another is missed.
- The copies implement a true invariant.
- They are maintained by different teams.
- They produce inconsistent externally visible behavior.
- They are part of a migration that should now converge.
- The abstraction already exists but is bypassed.

Low-value candidates include generated code, fixed tables, stable protocol bindings, tests intentionally duplicating behavior, or coincidentally similar code in independent domains.

## 6.3 When duplication is preferable

Keep duplication when:

- The concepts are only accidentally similar.
- Independent evolution is expected.
- Sharing would violate ownership or deployment boundaries.
- The proposed abstraction requires many modes, callbacks, flags, or conditionals.
- The duplicate is small and stable.
- Removal would create a remote dependency or runtime coupling.
- A migration temporarily needs both implementations.
- The abstraction would erase meaningful domain distinctions.
- The shared implementation would have a larger blast radius than the duplicated logic.

Empirical clone studies do not support the simplistic conclusion that every duplicate necessarily damages maintainability. The relevant issue is whether duplicated knowledge creates coordinated-change or divergence risk. ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/10.1155/2012/938296))

---

# 7. Dead code and codebase reduction

## 7.1 Search beyond unreachable statements

Audit for:

- Unreachable statements and branches.
- Unreferenced private functions, types, and fields.
- Unused exports.
- APIs with no known consumers.
- Unused direct dependencies.
- Transitive dependencies that disappear after a direct dependency is removed.
- Obsolete feature flags.
- Disabled experiments.
- Compatibility code for no-longer-supported versions.
- Deprecated interfaces with no remaining callers.
- Redundant adapters.
- Old migration paths.
- Stale environment variables.
- Unused configuration keys.
- Obsolete CI jobs and scripts.
- Redundant generated artifacts.
- Committed build output.
- Duplicate tests that protect no additional behavior.
- Old deployment manifests.
- Unused database columns, indexes, queues, topics, and scheduled jobs.
- Documentation for removed behavior.

## 7.2 Use an evidence ladder before deletion

1. **Static reachability:** no path from declared roots.
2. **Reference search:** no imports, calls, configuration references, registrations, or generated bindings.
3. **Consumer inventory:** no external or downstream consumer.
4. **Runtime observation:** no use over a representative time window.
5. **Ownership review:** responsible team confirms intended removal.
6. **Reversible disablement:** turn off behind a controlled flag or shadow path where appropriate.
7. **Deletion with tests:** remove code, configuration, dependency, and documentation together.
8. **Post-removal monitoring:** verify errors, traffic, performance, and support signals.
9. **Follow-up cleanup:** remove temporary flag, adapter, and rollback scaffolding.

A detector should report assumptions such as:

```yaml
reachability:
  roots:
    - production_entrypoints
    - cli_commands
    - scheduled_jobs
    - public_library_exports
    - plugin_registrations
  excluded:
    - tests
    - examples
  uncertainty:
    - reflection
    - external_library_consumers
    - runtime_generated_names
```

## 7.3 Measure deletion as an improvement

Useful reduction indicators include:

- Authored logical lines removed.
- Public API surface reduced.
- Dependencies removed.
- Configuration keys eliminated.
- Build targets or deployment units removed.
- State stores consolidated.
- Serialization boundaries eliminated.
- Runtime processes or queues removed.
- Concepts removed from onboarding documentation.
- Tests deleted because the underlying behavior no longer exists.
- Operational alerts and dashboards retired.

The goal is not maximum deletion. It is **less system to own while preserving required capability**.

---

# 8. Dependency health

## 8.1 Universal dependency audit

For every dependency, record:

- Direct, transitive, build-time, test-time, development-time, optional, bundled, or runtime status.
- Version and version constraint.
- Introduction path.
- Actual imported or invoked capabilities.
- Supported platforms.
- Maintainer and support status.
- End-of-life information.
- Known vulnerabilities.
- Exploit reachability.
- Runtime exposure and privilege.
- License and policy status.
- Download, artifact, or binary size.
- Number of transitive dependencies.
- Overlap with other libraries.
- Vendor or framework lock-in.
- Replacement and removal cost.
- Whether the platform or standard library already supplies the needed capability.

Standardized SBOM formats such as SPDX and CycloneDX provide machine-readable component and relationship inventories. SBOMs should be treated as inputs to dependency and vulnerability analysis, not as proof that the dependency set is safe or complete. ([nist.gov](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-supply-chain-security-guidance-20))

## 8.2 Prioritize vulnerability findings contextually

A vulnerable dependency is more urgent when:

- The vulnerable functionality is reachable.
- Untrusted input can reach it.
- The application is exposed.
- The component runs with significant privilege.
- Exploitation is known or likely.
- The affected path handles sensitive assets.
- Compensating controls are absent.
- The dependency is unsupported.
- The affected module has high centrality or broad deployment.

Do not prioritize only by severity score. Combine:

\[
VulnerabilityPriority =
Severity \times Reachability \times Exposure \times AssetImpact \times ExploitEvidence
\]

OSV provides a machine-readable vulnerability model and scanners that can inspect lockfiles, directories, SBOMs, and container-related artifacts. Syft can generate SBOM inventories, while Trivy can combine vulnerability, configuration, secret, and license-oriented scanning. ([google.github.io](https://google.github.io/osv-scanner/supported-languages-and-lockfiles/))

## 8.3 Dependency simplification opportunities

Look for:

- Two libraries used for the same purpose.
- Multiple versions of one library in a bundle.
- A large library used for one small utility.
- Framework APIs spread throughout domain logic.
- Direct vendor SDK usage outside adapters.
- A package retained only by dead code.
- A dependency whose replacement is already available in the platform.
- Compatibility shims for unsupported versions.
- Deep transitive trees created by development-only tooling.
- Plugins or extensions never enabled.
- Client libraries duplicated across services.
- Build tools that require an additional runtime solely for one step.

Replacing a library with platform functionality is beneficial only when it reduces total ownership cost. Reimplementing mature cryptography, protocol, parsing, or security-sensitive functionality is generally not a simplification.

## 8.4 Modernization without upgrade churn

Upgrade when there is evidence of:

- Security risk.
- End-of-support risk.
- Required platform compatibility.
- Material performance or reliability improvement.
- Removal of a custom workaround.
- Reduced dependency weight.
- Necessary interoperability.
- A planned migration window.

Defer when:

- The release has no relevant benefit.
- Migration risk exceeds the current risk.
- The dependency is isolated and supported.
- The upgrade would force unrelated architectural churn.
- The repository lacks tests needed to validate the transition.

Supply-chain provenance can be represented separately from dependency inventory. SLSA’s current specification describes incremental supply-chain guarantees and provenance practices; it complements rather than replaces SBOM and vulnerability analysis. ([slsa.dev](https://slsa.dev/blog/2025/11/announce-slsa-v1.2))

---

# 9. Performance and efficiency

## 9.1 Measurement-first workflow

1. **Define the user-visible or operational problem.**
   - Latency percentile.
   - Throughput.
   - Cost per operation.
   - Memory ceiling.
   - Startup time.
   - Build or test duration.
   - Battery, CPU, or network consumption.
2. **Characterize the workload.**
   - Input sizes.
   - Request mix.
   - Concurrency.
   - Warm versus cold behavior.
   - Cache state.
   - Success and failure paths.
3. **Measure the end-to-end path.**
   - Traces.
   - Service-level latency.
   - Queueing.
   - Database time.
   - External dependencies.
4. **Profile the constrained resource.**
5. **Form a causal hypothesis.**
6. **Change the smallest relevant mechanism.**
7. **Benchmark before and after.**
8. **Canary under representative load.**
9. **Verify that another dimension did not regress.**

The USE method—checking utilization, saturation, and errors for relevant resources—is a useful system-level starting point. It also warns that average utilization can hide bursts and queue saturation. ([brendangregg.com](https://www.brendangregg.com/usemethod.html))

## 9.2 Static versus dynamic performance evidence

| Concern | Static analysis can suggest | Runtime evidence needed |
|---|---|---|
| CPU | Nested work, repeated parsing, unnecessary sorting, expensive regexes | CPU profile, flame graph, instruction or sample distribution |
| Memory | Large retained structures, copying, unbounded collections | Heap profile, allocation profile, retention graph, GC behavior |
| I/O | Repeated file calls, synchronous calls in async paths | I/O latency, throughput, wait time, queue depth |
| Database | Loop-issued queries, missing batching, broad selection | Query traces, execution plans, row counts, lock waits, cache behavior |
| Network | Sequential fan-out, repeated serialization, missing pooling | Request traces, connection behavior, payload size, retry amplification |
| Concurrency | Lock nesting, unbounded tasks, shared state | Contention profile, wait graph, scheduler traces, load behavior |
| Serialization | Multiple conversions, broad objects, repeated parsing | CPU and allocation cost by payload and path |
| Caching | Duplicate computation and repeated calls | Hit rate, miss penalty, staleness, eviction, contention |
| Startup | Large initialization graphs, eager loading | Timeline, class/module loading, dependency initialization |
| Build | Deep target graph, duplicate generation | Critical-path timing, cache hit rate, incremental invalidation |
| Tests | Excessive integration setup, serial execution | Test-level timing, fixture setup, resource contention |
| Bundle or binary | Heavy dependency imports, duplicated packages | Built-artifact composition and runtime loading |

Official profiling case studies demonstrate why measurement matters: data-structure and allocation changes discovered through profiles can produce large improvements that would not be obvious from surface syntax alone. ([go.dev](https://go.dev/blog/pprof))

## 9.3 Algorithmic hotspot model

Do not flag every nested loop. Estimate:

\[
AlgorithmicRisk =
ComplexityGrowth \times ExpectedInputSize \times ExecutionFrequency \times CriticalPathWeight
\]

Investigate:

- Nested loops over independently growing collections.
- Repeated full traversals.
- Sorting when only minimum, maximum, or top-\(k\) is required.
- Linear search inside repeated operations.
- Repeated parsing or compilation.
- Repeated database or network calls.
- Rebuilding indexes or maps.
- Excessive intermediate collections.
- Copying large buffers.
- Recomputing invariant values.
- Repeated serialization across adjacent layers.
- Algorithms with adversarial worst cases on untrusted input.
- Unbounded result sets.
- Cartesian products.
- Cache operations whose coordination cost exceeds saved computation.

A nested loop over two arrays of size five may be ideal. A linear database query executed a million times may be the real problem.

## 9.4 Performance validation requirements

Every performance recommendation should state:

- Baseline workload and environment.
- Warm-up and cache conditions.
- Sample count.
- Distribution, not only mean.
- Noise or confidence interval.
- CPU and memory effects.
- Correctness equivalence.
- Tail-latency effect.
- Cost under failure or overload.
- Production validation.
- Rollback condition.

---

# 10. State, data flow, APIs, and domain modeling

## 10.1 State ownership audit

Create a state inventory:

| State | Owner | Writers | Readers | Invariants | Persistence | Synchronization | Derived from |
|---|---|---|---|---|---|---|---|

Then inspect:

- State with multiple writers.
- State with no clear owner.
- Derived state stored redundantly.
- The same fact stored in several services or caches.
- Mutation across module boundaries.
- State transitions represented by booleans.
- Required call ordering.
- Hidden mutation in getters, hooks, callbacks, or middleware.
- Shared mutable globals.
- Cache and source-of-truth divergence.
- State copied through many representations.
- Transactions that span incompatible systems.
- Data converted repeatedly between equivalent forms.
- Serialization boundaries inside one process.
- Update paths that bypass invariants.

Likely improvements include:

- Single-writer ownership.
- Immutable values.
- Explicit state machines.
- Derived-on-demand state.
- Transactional boundaries.
- Command/query separation where it clarifies ownership.
- Eliminating redundant stores.
- Moving invariants to constructors or types.
- Replacing global state with scoped dependencies.
- Passing stable values rather than mutable containers.

## 10.2 Temporal coupling

Temporal coupling exists when operations must occur in a hidden sequence:

```text
create → configure → initialize → start → use → stop → dispose
```

Detect it through:

- Boolean “initialized” or “started” checks.
- Exceptions caused by call ordering.
- Methods documented as “must call before.”
- Mutable builders surviving after construction.
- Partially initialized objects.
- Cleanup requiring knowledge of which earlier steps succeeded.
- State flags that encode a lifecycle.

Possible improvements:

- Constructor or factory establishes a valid object.
- Separate types represent separate lifecycle states.
- Scoped resource-management constructs.
- Explicit state machines.
- Atomic operations instead of multi-call protocols.
- Structured concurrency for task lifetimes.

## 10.3 API quality

An interface is difficult to use correctly when it permits:

- Invalid parameter combinations.
- Many optional parameters.
- Boolean mode flags.
- Ambiguous null or empty values.
- Generic maps or untyped objects.
- Inconsistent error behavior.
- Resource ownership without a close or lifetime contract.
- Retryable operations without idempotency.
- Security-sensitive defaults that are disabled.
- Return types that conceal partial failure.
- Exceptions and result values used inconsistently.
- Callers to depend on internal representations.
- Unversioned or unstable public contracts.
- Similar operations with different terminology.

Useful analyses include:

- Public-surface inventory.
- Call-site mining.
- Parameter-combination analysis.
- Error-contract comparison.
- Consumer-driven contract tests.
- Compatibility-diff analysis.
- Client usage clustering.
- Unsupported or unused method detection.
- Optionality and nullability propagation.
- Documentation-to-signature consistency.

A strong API should make the safe, valid, common operation the easiest one to express.

## 10.4 Domain modeling

Look for:

- Identifiers, currencies, units, paths, URLs, and dates represented as arbitrary strings.
- Multiple booleans encoding mutually exclusive states.
- Excessive nullability.
- Duplicate enums.
- String comparisons for workflow states.
- Maps carrying known structures.
- Domain validation repeated at many entry points.
- Invalid combinations representable in ordinary objects.
- Business rules split across UI, API, persistence, and scheduled jobs.
- Incomplete state machines.
- A large amount of defensive code protecting against invalid internal values.

Stronger modeling is most valuable when a concept is:

- High consequence.
- Frequently changed.
- Shared across boundaries.
- Security sensitive.
- Frequently validated.
- Used in branching logic.
- A common source of defects.

Do not create a type for every primitive. Create one when it carries invariants, semantics, ownership, or behavior.

---

# 11. Error handling, reliability, and concurrency

## 11.1 Failure-path audit

For every material operation, determine:

1. What may fail?
2. Who detects it?
3. Who handles it?
4. What state has already changed?
5. What resources are held?
6. Is retry safe?
7. Is the outcome known, unknown, or partial?
8. Who must be informed?
9. What telemetry is emitted?
10. How is recovery validated?

Inspect:

- Empty or overly broad catches.
- Exceptions logged and then ignored.
- Default values returned on required-data failure.
- Missing error checks.
- Lost error causes or stack context.
- Duplicate logging at every layer.
- Inconsistent typed and exception-based errors.
- Resource release on every exit path.
- Cleanup errors masking primary failures.
- Multi-step writes without atomicity or compensation.
- False success after partial completion.
- Unsafe fallback behavior.
- Ambiguous commit outcomes.
- Missing idempotency.
- Retry of non-idempotent side effects.
- Poison-message handling.
- Recovery after process termination.
- Data repair and reconciliation paths.

## 11.2 Timeouts, cancellation, and retries

Every blocking boundary should have one of:

- An explicit deadline.
- An inherited deadline.
- A documented reason it may wait indefinitely.

Audit:

- HTTP, RPC, database, queue, lock, file, and process waits.
- Whether a timeout cancels underlying work or merely abandons the result.
- Deadline propagation through nested calls.
- Cancellation-token propagation.
- Cleanup after cancellation.
- Retry limits.
- Backoff and jitter.
- Retry budgets.
- Stacked retries at several layers.
- Idempotency and deduplication.
- Circuit-breaking and admission control.
- Graceful shutdown ordering.

An empirical study of cancellation behavior across major Java, C#, and Go systems found bugs in cancellation initiation, propagation, completion, and cleanup; the failures included leaks, incorrect results, and data-related consequences. Static checkers could identify recurring anti-patterns, but complete correctness still depended on task and state semantics. ([microsoft.com](https://www.microsoft.com/en-us/research/publication/cancellation-in-systems-an-empirical-study-of-task-cancellation-patterns-and-failures/))

## 11.3 Concurrency and asynchronous complexity

### Static candidates

- Shared mutable state without a synchronization contract.
- Check-then-act logic.
- Inconsistent lock ordering.
- Locks held across asynchronous suspension.
- Blocking calls in asynchronous functions.
- Fire-and-forget tasks.
- Dropped futures or promises.
- Unbounded queues and channels.
- Unbounded task creation.
- Cancellation ignored in loops.
- Non-thread-safe containers shared across tasks.
- Shared connection pools with no capacity isolation.
- Callbacks that may execute concurrently.
- Unsynchronized lazy initialization.
- Transactions and external side effects separated by race windows.

### Dynamic approaches

- Race detectors.
- Thread sanitizers.
- Stress and soak tests.
- Deterministic scheduler exploration.
- Model checking for small state spaces.
- Lock and contention profiling.
- Wait-for graphs.
- Queue-depth and consumer-lag monitoring.
- Fault injection during cancellation and shutdown.
- Load testing with slow or failed dependencies.
- Repeated tests under randomized scheduling.

A concurrency finding should describe an actual interleaving or resource failure mode, not merely say that code “looks unsafe.”

---

# 12. Testing quality beyond line coverage

## 12.1 Testing dimensions

| Technique | What it tells you | Key limitation |
|---|---|---|
| Line coverage | Which lines executed | Assertions may be absent or ineffective |
| Branch coverage | Which branch outcomes executed | Does not prove boundary values or combinations |
| Condition or decision coverage | Which Boolean components were exercised | Can still miss meaningful state combinations |
| Mutation testing | Whether tests detect small behavioral changes | Equivalent mutants and runtime cost |
| Property-based testing | Whether general invariants hold across generated inputs | Good properties require domain understanding |
| State-machine or model-based testing | Whether workflows satisfy transition rules | State-space growth |
| Contract testing | Whether components agree on interfaces | Cannot prove internal correctness |
| Integration testing | Whether real components work together | Slower and harder to isolate |
| Fault injection | Whether failures are handled safely | Environment and scenario design are difficult |
| Differential testing | Whether two implementations agree | Shared defects can produce agreement |
| Fuzzing | Whether unexpected inputs cause failure or unsafe behavior | Requires useful oracles and corpus management |
| Architecture tests | Whether structural constraints hold | Limited by dependency extraction |
| Flake analysis | Whether outcomes vary without relevant changes | Requires repeated or historical evidence |

A large empirical study found only low-to-moderate relationships between coverage and fault detection after controlling for test-suite size. Coverage remains useful for locating unexercised code, but it is a weak standalone quality target. ([2014.icse-conferences.org](https://2014.icse-conferences.org/node/163/index.html))

Mutation testing provides a stronger indication that tests can detect behavioral changes. Research comparing mutants with real faults found meaningful correlation independent of coverage, though equivalent mutants and cost remain important limitations. ([cs.ubc.ca](https://www.cs.ubc.ca/award/2014/11/acm-sigsoft-distinguished-paper-award-fse))

## 12.2 Detecting technically covered but weakly protected code

Look for:

- High coverage but low mutation scores.
- Tests with no meaningful assertions.
- Assertions only that no exception occurred.
- Large snapshots that are rarely reviewed.
- Mocks that reproduce the implementation.
- The same algorithm used as both implementation and test oracle.
- No tests for failure or cancellation paths.
- No boundary, empty, malformed, or maximum-size inputs.
- No invariant or property tests.
- No tests for duplicate delivery or retry.
- No tests for transaction rollback.
- No concurrency stress.
- Heavy implementation-detail assertions.
- Tests that fail whenever internal structure changes but miss behavior regressions.
- Critical branches reached only incidentally by broad end-to-end tests.

Property-based tools such as Hypothesis and related QuickCheck-style frameworks generate examples around declared invariants, round trips, state transitions, and differential behavior. They are especially useful where hand-picked examples cover only a small input space. ([hypothesis.readthedocs.io](https://hypothesis.readthedocs.io/en/latest/))

## 12.3 Test-suite maintainability

Measure:

- Test duration by test and fixture.
- Setup and teardown cost.
- Parallelizability.
- Shared mutable fixtures.
- External-service reliance.
- Flake rate.
- Rerun pass rate.
- Failure-diagnosis quality.
- Tests changed with production code.
- Mock count and depth.
- Redundant test clusters.
- Coverage overlap.
- Quarantined-test age.
- Time from failure to actionable diagnosis.

Do not remove a “redundant” test solely because it executes the same lines. It may protect a different contract, integration path, or historical regression.

---

# 13. Repository history and changeability

## 13.1 History signals

Collect per function, file, module, and subsystem:

- Change count.
- Lines added and deleted.
- Distinct commits.
- Distinct work items.
- Defect-fix count.
- Revert count.
- Emergency-fix count.
- Contributors.
- Ownership concentration.
- Time since last meaningful change.
- Co-change relationships.
- Migration duration.
- Frequency of simultaneous production and test changes.
- Frequency of architecture-rule exceptions.

Normalize history by removing:

- Formatting-only commits.
- Renames.
- Generated output.
- Vendoring.
- Lockfile-only changes where appropriate.
- Automated version bumps.
- Bot-authored changes.
- Bulk license-header changes.
- Repository reorganizations.

## 13.2 High-value history patterns

### Complexity × churn

The classic maintenance hotspot:

\[
H = P_{complexity} \times P_{churn}
\]

where \(P\) is a repository-local percentile or normalized score.

### Temporal coupling

Two files that frequently change together may indicate:

- A hidden responsibility spanning both.
- An API that does not encapsulate change.
- Duplicated knowledge.
- A migration seam.
- Shared tests or configuration.
- A healthy intentional relationship.

Inspect pairs that co-change frequently **despite weak declared structural coupling**.

### Defect concentration

Combine:

- Defect fixes.
- Incident involvement.
- Reverts.
- Emergency patches.
- Security findings.
- Customer-reported failures.

### Ownership concentration

Use Gini, Herfindahl-style concentration, or simple contributor distribution to locate critical code whose knowledge is concentrated. Do not convert this into individual performance assessment.

### Long-lived migration detection

Search for:

- Old and new APIs both changing.
- Adapters growing rather than shrinking.
- Feature flags with no removal date.
- “Temporary” directories.
- Compatibility paths receiving new features.
- Repeated synchronization between old and new models.
- Duplicate tests and schemas.

---

# 14. Documentation, naming, and comprehensibility

## 14.1 Documentation audit

Check whether the repository explains:

- System purpose.
- Major components.
- Module ownership.
- Data stores and external dependencies.
- Trust boundaries.
- Build, test, deployment, and recovery.
- Architectural decisions.
- Important invariants.
- Public APIs and compatibility policy.
- Failure behavior.
- Migration state.
- Generated-code ownership.
- Local development setup.

Then test whether those explanations match implementation evidence.

## 14.2 Documentation smells

- Comments that paraphrase the code.
- Large comments explaining avoidable control flow.
- Stale names or paths.
- Comments contradicting behavior.
- Architecture diagrams with missing or renamed components.
- Several documents describing the same workflow differently.
- Important invariants mentioned only in issue discussions.
- Acronyms and internal vocabulary without definitions.
- Several names for one domain concept.
- One name used for several concepts.
- Public APIs with no error or ownership contract.
- Runbooks that do not match current deployment.

An excessive comment burden can be a symptom of confusing code. The desired outcome is not more documentation everywhere; it is the right explanation at the right level.

## 14.3 Conceptual vocabulary

Create a domain-term inventory from:

- Type and function names.
- API fields.
- Database schemas.
- Event names.
- Configuration.
- Documentation.
- User-visible terminology.

Use clustering and semantic review to find:

- Synonyms representing the same concept.
- Homonyms representing different concepts.
- Old terminology surviving migrations.
- Technical names leaking into domain APIs.
- Duplicate concepts with subtly different fields.
- Unnecessary vocabulary introduced by abstraction layers.

A useful simplification metric is:

> **How many distinct concepts must a developer understand to make a safe change?**

---

# 15. Build, tooling, CI/CD, and repository structure

## 15.1 Treat the delivery system as product code

Audit:

- Build definitions.
- Package managers.
- Task runners.
- Code generation.
- Local setup.
- Test infrastructure.
- CI workflows.
- Release scripts.
- Deployment manifests.
- Container builds.
- Formatting and lint configuration.
- Environment configuration.
- Schema migration tooling.
- Documentation generation.
- Artifact signing and provenance.

## 15.2 Measure the feedback path

Record:

- Fresh checkout to successful build.
- Fresh checkout to first passing test.
- Clean build duration.
- Incremental build duration.
- Test discovery and execution duration.
- Code-generation duration.
- Dependency-resolution duration.
- CI queue and execution time.
- Cache hit rate.
- Critical path through the pipeline DAG.
- Artifact and container size.
- Number of steps required for a local production-like run.
- Frequency of non-reproducible builds.
- Developer environment divergence.

## 15.3 Common simplification opportunities

- Merge overlapping scripts.
- Replace custom wrappers with standard build-tool functionality.
- Remove unused generators.
- Eliminate repeated configuration.
- Share immutable pipeline primitives without creating a pipeline framework.
- Make generated output reproducible and separate it from authored code.
- Remove redundant package managers or task runners.
- Consolidate environment-variable handling.
- Eliminate deployment stages that no longer provide independent assurance.
- Replace imperative setup documentation with executable environment definitions.
- Remove obsolete release pathways.

NIST guidance for supply-chain security recommends integrating SAST, dynamic testing where applicable, dependency analysis, secret detection, and evidence generation into automated CI/CD processes. The pipeline itself must therefore be included in repository-health analysis. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/204/d/final))

## 15.4 Repository structure

Restructure when doing so:

- Makes ownership visible.
- Aligns code with enforceable boundaries.
- Separates generated and authored artifacts.
- Removes ambiguous dumping grounds.
- Reduces navigation or configuration burden.
- Enables independent testing or deployment.
- Clarifies public and internal APIs.
- Makes dependency direction enforceable.

Do not reorganize merely to achieve a preferred directory aesthetic. Moving files without changing responsibility, dependency, or ownership creates churn without architectural value.

---

# 16. Security as a quality dimension

## 16.1 Continuous repository security checks

- Secret scanning, including history where practical.
- Static application security analysis.
- Taint and source-to-sink data flow.
- Dependency and container vulnerability scanning.
- Infrastructure and configuration scanning.
- License and provenance policy checks.
- Unsafe shell and process invocation.
- Unsafe path construction.
- Injection-prone query construction.
- Deserialization of untrusted data.
- Weak or custom cryptography.
- Insecure random generation.
- Excessive permissions.
- Debug and development functionality in production.
- Exposed internal APIs.
- Missing input-size and resource limits.

## 16.2 Architectural security review

Map:

- Entry points.
- Trust boundaries.
- Data classifications.
- Authentication.
- Authorization.
- Credential and token flow.
- Privileged operations.
- File and process access.
- Outbound network access.
- Administrative functionality.
- Third-party components with dangerous capabilities.
- Failure-open and failure-closed decisions.

OWASP’s secure-code-review guidance explicitly treats architecture, entry points, data flow, authentication, authorization, business logic, cryptography, error handling, configuration, and dependency review as complementary activities. Automated tools identify candidates; contextual business-logic and access-control review still require human assistance. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html))

## 16.3 Standards as baselines, not scorecards

NIST’s SSDF provides outcome-oriented secure-development practices intended to be tailored by risk and organizational context. OWASP ASVS 5.0 provides a current, machine-readable application-security verification baseline. Neither should be used as a mechanical substitute for threat modeling or domain-specific risk decisions. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final))

---

# 17. Observability and diagnosability

A maintainable system should make failures explainable without adding emergency instrumentation.

## 17.1 Minimum diagnosability model

For important operations, capture:

- Operation identity.
- Start and completion.
- Outcome category.
- Duration.
- Trace or correlation context.
- Relevant dependency.
- Retry count.
- Queue or asynchronous context.
- Bounded domain identifiers where safe.
- Error category and causal context.
- Version and deployment identity.
- Resource saturation where relevant.

OpenTelemetry standardizes traces, metrics, logs, context propagation, and semantic conventions. W3C Trace Context standardizes propagation identifiers across component and vendor boundaries. ([opentelemetry.io](https://opentelemetry.io/docs/concepts/signals/))

## 17.2 Observability smells

- Unstructured string-only logs.
- Different field names for the same concept.
- Missing trace propagation across queues or background tasks.
- Logging only at request entry and exit.
- Errors without dependency or operation context.
- Log-and-rethrow duplication.
- Secrets or sensitive payloads in telemetry.
- User IDs, request IDs, raw URLs, or exception messages used as metric dimensions.
- High-cardinality labels.
- Instrumentation embedded deeply in business rules.
- Metrics that cannot be connected to user-visible outcomes.
- Traces whose spans represent implementation trivia rather than logical operations.
- Silent fallback or partial success.
- Excessive debug logs that conceal meaningful events.
- No telemetry for queue depth, retries, cancellation, or resource exhaustion.

## 17.3 Validate diagnosability through incident exercises

For a sampled failure, ask whether the system can answer:

- What failed?
- Where did it first fail?
- Which users or operations were affected?
- When did it begin?
- What changed?
- Was the failure partial or complete?
- Were retries or fallbacks involved?
- What state may be inconsistent?
- Can the operation be replayed safely?
- How do we prove recovery?

Track time to isolate, time to identify the causal change, and the frequency with which an investigation requires adding new telemetry.

---

# 18. Consistency without dogma

Harmful inconsistency occurs when equivalent situations use different:

- Naming.
- Error models.
- Validation mechanisms.
- Serialization formats.
- Data-access patterns.
- Configuration sources.
- Dependency-injection patterns.
- Logging fields.
- Retry policies.
- Concurrency primitives.
- Test styles.
- Module structures.
- API pagination or versioning.
- Date, time, currency, or identifier representations.

Consistency is valuable when it reduces choice and enables tooling.

It becomes harmful when:

- Different domains require different semantics.
- A single pattern forces unnecessary layers.
- A standard is retained after the platform evolves.
- Consistency requires wrapping clear platform APIs.
- All code is forced into one architecture regardless of scale.
- Migration churn exceeds the benefit.
- Local exceptions are safer or clearer.

Standardize **decisions developers should not have to repeatedly make**. Preserve variation when it expresses real domain or operational differences.

---

# 19. Detecting over-engineering and de-abstraction opportunities

## 19.1 Over-engineering indicators

- Interface with one implementation, one consumer, and no policy boundary.
- Factory that always returns one concrete type.
- Strategy objects for behavior that never varies.
- Plugin systems with no external or independently owned plugins.
- Event buses for direct local calls.
- Generic repositories that hide useful database capabilities.
- Several dependency-injection layers around a fixed object graph.
- Wrapper-on-wrapper APIs.
- Configuration options never changed in any environment.
- Extension points with no known consumers.
- Generic frameworks maintained for one use case.
- Multiple “manager,” “provider,” “service,” or “handler” layers forwarding calls.
- Domain behavior expressed through reflection or metadata when ordinary code would be clearer.
- A large number of tiny types with no independent invariant.
- Abstractions whose implementations repeatedly inspect type or mode flags.
- Shared utility APIs whose callers use unrelated subsets.

## 19.2 Evidence for collapsing an abstraction

An abstraction is a strong collapse candidate when:

- It has one implementation and one caller.
- The interface changes whenever the implementation changes.
- Most methods are pass-through.
- It introduces no testing, ownership, security, runtime, or compatibility seam.
- It is not independently deployed or versioned.
- It requires configuration but does not enable useful variation.
- The implementation leaks through its API.
- Callers frequently downcast or bypass it.
- Its maintenance burden exceeds the change isolation it provides.
- Its original anticipated variants never appeared.

## 19.3 De-abstraction validation

Before and after collapsing, compare:

- Number of concepts.
- Number of files and modules.
- Dependency depth.
- Public API size.
- Configuration entries.
- Test setup.
- Change surface for representative tasks.
- Build and runtime effects.
- Ability to substitute, test, secure, or own the component independently.

The goal is not “fewer classes.” It is fewer **unnecessary decisions, relationships, and concepts**.

---

# 20. High-value signal combinations

Raw metric multiplication can be distorted by scale and outliers. Convert each signal to repository-local percentiles, robust z-scores, or bounded ordinal categories before combination.

| Combination | What it finds |
|---|---|
| **Complexity × churn** | Difficult code that repeatedly consumes maintenance effort |
| **Complexity × defect history** | Difficult code associated with observed failure |
| **Size × churn** | Growing responsibility centers |
| **Coupling × change frequency** | Dependencies that repeatedly propagate work |
| **Fan-in × instability** | Widely depended-upon code that changes or depends outward heavily |
| **Centrality × vulnerability** | Supply-chain or security risk with broad blast radius |
| **Duplication × churn** | Duplicated knowledge likely to diverge |
| **Duplication × defect asymmetry** | Copies where fixes are applied inconsistently |
| **Test weakness × change frequency** | Frequently modified code poorly protected against regression |
| **Mutation survivors × criticality** | Important behavior tests fail to distinguish |
| **Performance cost × execution frequency** | Optimization candidates with real aggregate impact |
| **Allocation cost × retention duration** | Memory-pressure candidates |
| **Queue growth × processing deficit** | Backpressure and overload problems |
| **Shared-state writers × concurrency** | Race and synchronization risk |
| **Serialization boundaries × payload volume** | Redundant transformation cost |
| **Ownership concentration × criticality** | Knowledge and operational continuity risk |
| **Build-step cost × invalidation frequency** | High-value build-system improvements |
| **Feature-flag age × branch divergence** | Abandoned experiments and permanent dual behavior |
| **Documentation drift × subsystem churn** | Stale comprehension aids in rapidly evolving areas |
| **API optionality × misuse defects** | Interfaces that permit invalid combinations |
| **Architecture violations × co-change** | Boundary erosion with observed maintenance consequences |
| **Dependency depth × failure frequency** | Fragile or opaque integration pathways |

A practical hotspot score might be:

\[
Hotspot =
0.25C +
0.25Ch +
0.15D +
0.15Co +
0.10T +
0.10O
\]

where:

- \(C\) = complexity percentile.
- \(Ch\) = churn percentile.
- \(D\) = defect or incident percentile.
- \(Co\) = coupling or centrality percentile.
- \(T\) = test weakness.
- \(O\) = ownership concentration.

The weights are policy, not science. Preserve the component signals in the report so the composite never conceals why an entity ranked highly.

---

# 21. Automation classification

## Fully automatable

- Language and build-file discovery.
- Compilation and type checking.
- Basic complexity, size, nesting, and parameter metrics.
- Exact token clones.
- Import and static dependency graphs.
- Strongly connected components.
- Explicit architecture rules.
- Unreachable statements.
- Unused locals, imports, and private symbols.
- Coverage collection.
- Secret scanning.
- Known-vulnerability matching.
- SBOM generation.
- Binary, bundle, and container composition.
- Benchmark comparison under fixed workloads.
- Public API signature diffing.
- Generated-artifact verification.

## Mostly automatable

- Whole-program dead code.
- Unused exports and dependencies.
- Near-duplicate detection.
- Mutation testing.
- Hotspot analysis.
- Temporal coupling.
- Defect concentration.
- Ownership concentration.
- Architecture reflexion.
- Profile comparison.
- Flaky-test identification.
- N+1 candidate detection.
- Feature-flag age and reference analysis.
- Documentation link and symbol validation.

## AI-assisted

- Semantic duplication.
- Business-rule extraction.
- Responsibility clustering.
- Obsolete compatibility inference.
- API usability analysis.
- Domain-model weakness.
- State ownership reconstruction.
- Over-engineering detection.
- Stale documentation.
- Terminology consistency.
- Architecture-intent reconstruction.
- Refactoring alternative generation.
- Consequence and validation-plan drafting.

## Human architectural judgment required

- Intended domain boundaries.
- Correct abstraction level.
- Acceptable duplication.
- Compatibility commitments.
- Failure and fallback policy.
- Security-risk acceptance.
- Performance and cost tradeoffs.
- Migration sequencing.
- Ownership and team boundaries.
- Whether a recommendation improves the system as a whole.

---

# 22. Curated tooling landscape

The best stack is not the one with the most dashboards. Prefer tools that expose machine-readable evidence and can be composed into one finding model.

| Capability | Strong options | What it contributes | Independently implementable technique |
|---|---|---|---|
| Extensible static and data-flow analysis | CodeQL; Semgrep; SonarQube/SonarCloud | Queryable syntax, control flow, taint, issue output, changed-code gates | Parse or consume compiler ASTs and implement graph/data-flow queries |
| Architecture tests | ArchUnit; ArchUnitNET; ecosystem import/dependency rule tools | Executable dependency and layer constraints | Extract a dependency graph and evaluate declarative predicates |
| Hotspot and change coupling | Git-based custom analysis; CodeScene | Churn, complexity, temporal coupling, code-health prioritization | Mine version-control history and join it with static metrics |
| Clone analysis | Token, AST, tree, and dependence-graph clone tools | Exact through near-semantic candidates | Normalize syntax trees and compare control/data-flow signatures |
| Coverage and mutation | Native coverage; PIT; Stryker family; ecosystem mutation tools | Exercise map and behavioral test strength | Mutate operators or AST nodes and run affected tests |
| Property testing | Hypothesis; QuickCheck-style libraries; fast-check and equivalents | Generated inputs, invariants, state models | Generate values from schemas and shrink failures |
| Supply chain | OSV-Scanner; Syft; Trivy; ecosystem package managers | Vulnerability, inventory, SBOM, configuration, and secret-related evidence | Parse lockfiles/build graphs and correlate packages with advisories |
| Runtime profiling | Native profilers, sampling profilers, heap tools, database plans, eBPF where appropriate | CPU, memory, allocation, I/O, lock, and query evidence | Sample stacks, instrument operations, and aggregate by symbol/path |
| Distributed observability | OpenTelemetry and compatible backends | Traces, metrics, logs, context propagation | Emit structured events with standardized context |
| Graph exploration | Compiler or language-server graphs plus NetworkX, Graphviz, Neo4j, or equivalents | Cycles, communities, centrality, reachability, impact analysis | Standard graph algorithms |
| Semantic review | Governed LLM or agent analysis over code, history, docs, and graph evidence | Intent-level duplication, simplification, responsibility and documentation analysis | Human review using the same evidence package |

CodeQL supports custom query development and machine-readable result workflows; Semgrep provides pattern and taint-oriented analysis; Sonar emphasizes analysis of new code and configurable quality gates. These are different implementations of reusable underlying techniques rather than mandatory platform choices. ([docs.github.com](https://docs.github.com/en/enterprise-server%403.17/code-security/how-tos/scan-code-for-vulnerabilities/scan-from-the-command-line/writing-and-sharing-custom-queries-for-the-codeql-cli))

CodeScene’s hotspot model deliberately combines development activity with code health, while change-coupling analysis mines entities that evolve together. A custom Git pipeline can implement the same core history techniques when a commercial platform is unnecessary. ([docs.enterprise.codescene.io](https://docs.enterprise.codescene.io/versions/6.4.28/guides/technical/hotspots.html))

Mutation tools such as PIT and the Stryker family operationalize mutation analysis across several ecosystems, but incremental or selected mutation is often necessary to keep feedback practical. ([stryker-mutator.io](https://stryker-mutator.io/docs/stryker-js/incremental/))

---

# 23. Universal eight-stage repository audit

## Stage 1 — Repository discovery

### Analyze

- Languages and versions.
- Frameworks.
- Build systems and package managers.
- Entry points.
- Generated and vendored code.
- Test frameworks.
- Runtime components.
- Databases, queues, external services, and deployment units.
- Public APIs.
- Architecture documents and decisions.
- Ownership.
- Release and migration state.

### Produce

- Repository manifest.
- Scope and exclusions.
- Generated-code map.
- Component inventory.
- Initial dependency graph.
- Architecture hypothesis.
- Analysis coverage and blind-spot declaration.

### Critical rule

Do not run metrics across generated, vendored, fixture, migration, and authored code as though they were equivalent.

---

## Stage 2 — Static structural analysis

### Analyze

- Complexity.
- Nesting.
- Size.
- Parameters.
- Exact and near clones.
- Dead and unreachable code.
- Imports and dependencies.
- Cycles.
- Fan-in and fan-out.
- Broad exception handling.
- Resource ownership.
- State mutation.
- Static security and data flow.
- Public API surface.
- Configuration duplication.

### Produce

- Entity metric table.
- Clone candidates.
- Reachability report.
- Dependency graph.
- Security candidates.
- Local-complexity candidates.
- Detector-assumption report.

---

## Stage 3 — Architectural analysis

### Analyze

- Intended versus actual boundaries.
- Dependency direction.
- Module APIs.
- Domain boundaries.
- Cross-layer access.
- Stable-core dependencies.
- Graph communities.
- Centrality.
- Shared-state boundaries.
- Framework and vendor isolation.
- Architecture decisions.
- Migration seams.

### Produce

- Architecture reflexion model.
- Boundary violations.
- Cycle ranking.
- Central and bridge-module ranking.
- Missing fitness functions.
- Suggested architecture tests.

---

## Stage 4 — Historical analysis

### Analyze

- Churn.
- Change frequency.
- Defects.
- Incidents.
- Reverts.
- Temporal coupling.
- Ownership concentration.
- Long-lived migrations.
- Repeated architecture exceptions.

### Produce

- Complexity × churn hotspots.
- Defect-prone areas.
- Co-change graph.
- Ownership-risk map.
- Migration-debt candidates.
- Historical evidence attached to structural findings.

---

## Stage 5 — Test and correctness analysis

### Analyze

- Line, branch, and condition coverage.
- Mutation resistance.
- Properties and invariants.
- Contracts.
- Integration pathways.
- Failure tests.
- Flakiness.
- Test speed.
- Mock coupling.
- Critical unprotected behavior.

### Produce

- Behavior-to-test map.
- Weakly protected hotspots.
- Mutation sample.
- Flake inventory.
- Missing invariant and failure-path tests.
- Test-suite cost profile.

---

## Stage 6 — Runtime analysis

### Analyze

- CPU.
- Memory and allocations.
- Retention.
- I/O.
- Database.
- Network.
- Serialization.
- Queues and backpressure.
- Locks and scheduling.
- Caching.
- Startup.
- Build and test execution.
- Bundle or binary composition.

### Produce

- Representative workload definition.
- Profiles and traces.
- Critical-path map.
- Resource bottlenecks.
- Performance hypotheses.
- Baselines and budgets.

---

## Stage 7 — Simplification analysis

Ask systematically:

> What could the system stop doing?

### Analyze

- Code candidates for deletion.
- Dependencies for removal.
- Concepts that can merge.
- Layers that can collapse.
- Configuration that can disappear.
- State that can be derived rather than stored.
- Duplicate transformations and schemas.
- Framework capabilities that replace custom infrastructure.
- Deployment units and pipelines that can consolidate.
- Compatibility paths and feature flags.

### Produce

- Deletion proposals.
- De-abstraction proposals.
- Consolidation proposals.
- Dependency-removal proposals.
- State-reduction proposals.
- Concept-count reduction.
- Reversibility and validation plans.

---

## Stage 8 — Prioritization

### Combine

- Consequence.
- Breadth.
- Frequency.
- Evidence confidence.
- Strategic leverage.
- Effort.
- Migration risk.
- Regression risk.
- Coordination cost.
- Reversibility.

### Produce

- Ranked findings.
- Immediate safety work.
- Low-risk simplifications.
- Architectural investments.
- Investigative items.
- Deferred and explicitly accepted debt.
- Expiring waivers.

---

# 24. Codebase health model

The user-proposed dimensions are strong, but several should be separated to avoid concealing distinct problems.

## Recommended dimensions

### Structural

1. **Local complexity**
2. **Comprehensibility and conceptual load**
3. **Cohesion and responsibility fit**
4. **Coupling and blast radius**
5. **Modularity and boundary quality**
6. **Duplication and knowledge divergence**
7. **Dead weight and simplicity**

### Behavioral

8. **Correctness and domain integrity**
9. **API usability and contract quality**
10. **Reliability and resilience**
11. **Concurrency and state safety**
12. **Performance and resource efficiency**
13. **Security and privacy**

### Evolutionary

14. **Architecture conformance and evolvability**
15. **Test effectiveness and testability**
16. **Changeability and historical risk**
17. **Consistency and standardization**
18. **Ownership and knowledge distribution**

### Operational and delivery

19. **Dependency and supply-chain health**
20. **Operability and diagnosability**
21. **Build, delivery, and developer feedback**
22. **Documentation and decision traceability**

## Do not collapse these into one default score

For each dimension, report:

```text
Status:      Healthy | Watch | Concern | Critical | Unknown
Confidence:  Low | Medium | High
Trend:       Improving | Stable | Deteriorating | Unknown
Evidence:    Static | History | Test | Runtime | Incident | Architecture | Human
Scope:       Repository | Component | Module | File | Function
```

A single composite score may be created for portfolio reporting, but it should never replace the dimension-level evidence. A repository with excellent formatting and coverage but a critical authorization flaw should not appear “84% healthy.”

---

# 25. Prioritization model

## 25.1 Estimate expected benefit

Score each factor from 1 to 5:

- **Consequence severity:** effect on correctness, security, reliability, performance, maintainability, or developer productivity.
- **Breadth:** affected users, operations, modules, or teams.
- **Recurrence:** how frequently the problem is encountered.
- **Persistence:** whether it is temporary, stable, or worsening.
- **Strategic leverage:** whether fixing it unlocks other improvements.

One model is:

\[
ExpectedBenefit =
Severity \times Breadth \times Recurrence \times
\left(1 + 0.25 \times StrategicLeverage\right)
\]

## 25.2 Weight evidence confidence

| Confidence | Weight | Meaning |
|---|---:|---|
| Speculative | 0.25 | Plausible smell or hypothesis |
| Indicated | 0.50 | One meaningful source of evidence |
| Strong | 0.75 | Several independent signals agree |
| Confirmed | 1.00 | Reproduction, profile, incident, test, or direct contract violation |

## 25.3 Estimate delivery burden

Score:

- Implementation effort.
- Migration risk.
- Regression risk.
- Coordination cost.
- Operational rollout complexity.

\[
DeliveryBurden =
Effort \times
\left(
1 +
0.25MigrationRisk +
0.25RegressionRisk +
0.15Coordination +
0.15RolloutComplexity
\right)
\]

## 25.4 Calculate decision priority

\[
Priority =
\frac{ExpectedBenefit \times EvidenceConfidence}
{DeliveryBurden}
\]

Do not present the resulting number as mathematical truth. Use it to produce bands:

- **P0 — Immediate:** active correctness, security, data-loss, or outage risk.
- **P1 — High:** confirmed recurring cost or broad architectural risk.
- **P2 — Planned:** strong evidence, moderate impact, manageable timing.
- **P3 — Opportunistic:** useful during adjacent work.
- **Investigate:** potentially significant but insufficient evidence.
- **Accept:** known issue whose remediation cost currently exceeds expected benefit.

### Tie-breakers

Prefer work that is:

- Reversible.
- Easy to validate.
- Deletion-oriented.
- Located in active hotspots.
- Needed for another strategic change.
- Capable of reducing several dimensions simultaneously.

---

# 26. Findings must be distinct from recommendations

Every material result should follow this structure.

## Finding

What was observed, without assuming the remedy.

## Evidence

Static, architectural, historical, test, runtime, security, operational, or semantic evidence.

## Consequence

Why the observation matters in this repository.

## Recommendation

The smallest change likely to address the consequence.

## Expected benefit

The outcome expected in maintainability, reliability, performance, security, or simplicity.

## Risk

Possible regressions, migration hazards, new coupling, or operational impact.

## Validation

How the improvement will be demonstrated.

### Example

```yaml
id: ARCH-017
title: Pricing module bypasses the customer-policy boundary
scope:
  modules:
    - checkout
    - pricing
    - customer-policy

finding: >
  Checkout reads customer discount tables directly rather than using
  the customer-policy API.

evidence:
  static:
    - checkout/imports/customer_policy_storage
  architecture:
    - forbidden_dependency: true
  history:
    cochange_percentile: 94
    related_defect_fixes: 6
  confidence: strong

consequence: >
  Policy changes require coordinated edits in three modules and have
  repeatedly produced inconsistent discount behavior.

recommendation: >
  Move discount eligibility behind the existing customer-policy API,
  migrate checkout callers, then prohibit direct storage access.

expected_benefit:
  - one authoritative discount rule
  - smaller checkout change surface

risk:
  - latency increase from an additional boundary
  - compatibility differences in historical discount cases

validation:
  - differential tests against historical cases
  - no forbidden graph edge
  - no latency regression above the agreed budget
  - mutation tests for discount invariants

priority:
  band: P1
  confidence: 0.75

waiver:
  allowed: true
  requires:
    - owner
    - reason
    - expiry
```

---

# 27. Reusable machine-executable audit specification

The following is intentionally tool-agnostic. Adapters can translate individual checks into compiler, scanner, graph, profiler, or CI commands.

```yaml
spec_version: "1.0"

audit:
  name: universal-codebase-audit
  policy: evidence_backed_ratchet
  default_branch: main

repository:
  authored_code:
    include:
      - "**/*"
    exclude:
      - "vendor/**"
      - "third_party/**"
      - "node_modules/**"
      - "build/**"
      - "dist/**"
      - "coverage/**"
      - "fixtures/**"
      - "**/*.min.js"
  generated_code:
    discover_from:
      - file_headers
      - build_manifests
      - generator_outputs
      - repository_attributes
    analyze_separately: true
  history:
    window_days: 365
    ignore:
      - bots
      - formatting_only
      - generated_only
      - vendoring
      - bulk_renames
      - lockfile_only
      - license_headers

baselines:
  mode: ratchet
  compare_to: merge_base
  legacy_violations:
    allow_existing: true
    prohibit_new: true
    trend_required: true
  expiry_required_for_suppressions: true

confidence:
  speculative: 0.25
  indicated: 0.50
  strong: 0.75
  confirmed: 1.00

threshold_policy:
  universal_hard_gates:
    - no_new_compile_errors
    - no_new_type_errors
    - no_new_architecture_violations
    - no_new_cross_boundary_cycles
    - no_new_verified_secrets
    - no_new_unwaived_reachable_critical_security_findings
    - no_new_flaky_tests
  review_heuristics:
    cyclomatic_complexity:
      changed_function_review: 10
      extreme_candidate: 20
    cognitive_complexity:
      changed_function_review: 15
    maximum_nesting:
      changed_function_review: 4
      extreme_candidate: 5
    parameter_count:
      review: 6
    file_and_module_size:
      mode: repository_percentile
      review_percentile: 95
  forbidden_global_gates:
    - maintainability_index
    - total_repository_coverage
    - total_repository_duplication_percentage
    - absolute_file_length
    - dependency_count_without_context

detector_contract:
  every_detector_must_report:
    - analyzed_scope
    - exclusions
    - dependency_kinds_seen
    - known_blind_spots
    - confidence
    - evidence_locations
    - tool_version
    - configuration_hash

checks:
  continuous:
    - id: compile_and_types
      category: correctness
      scope: changed_and_affected
      gate: no_new_errors

    - id: changed_structure
      category: complexity
      scope: changed_functions
      collect:
        - cyclomatic_complexity
        - cognitive_complexity
        - npath_complexity
        - maximum_nesting
        - logical_lines
        - parameter_count
      gate: no_unreviewed_extreme_regression

    - id: dependency_rules
      category: architecture
      scope: changed_and_affected
      collect:
        - forbidden_dependencies
        - public_internal_boundary_violations
        - layer_violations
        - cross_domain_access
      gate: no_new_violations

    - id: dependency_cycles
      category: architecture
      graph_level: declared_modules
      gate: no_new_cross_boundary_cycles

    - id: exact_clones
      category: duplication
      scope: changed_code
      action: require_review_when_new

    - id: unused_local_code
      category: dead_weight
      detect:
        - unused_imports
        - unused_locals
        - unused_private_symbols
        - unreachable_statements
      gate: no_new

    - id: security_static
      category: security
      detect:
        - verified_secrets
        - injection_flows
        - unsafe_deserialization
        - unsafe_path_construction
        - unsafe_shell_execution
        - authorization_boundary_violations
      gate: no_new_unwaived_high_confidence_findings

    - id: dependency_security
      category: supply_chain
      detect:
        - vulnerable_direct_dependencies
        - vulnerable_transitive_dependencies
        - lockfile_integrity_changes
      prioritize_by:
        - reachability
        - exposure
        - asset_impact
        - exploit_evidence
      gate: policy_defined

    - id: tests
      category: test_effectiveness
      collect:
        - test_results
        - changed_code_branch_coverage
        - flaky_test_signals
      gate:
        - all_required_tests_pass
        - no_new_flakes
        - changed_critical_behavior_has_evidence

    - id: public_api_diff
      category: api
      scope: changed_exports
      gate: reviewed_compatibility_change

    - id: performance_budget
      category: performance
      trigger:
        - performance_sensitive_path_changed
        - benchmark_code_changed
        - artifact_budget_changed
      compare:
        - latency_distribution
        - throughput
        - allocations
        - peak_memory
        - artifact_size
      gate: no_unexplained_regression_outside_noise_band

  periodic:
    cadence: monthly
    run:
      - full_dependency_graph
      - strongly_connected_components
      - centrality_and_bridge_analysis
      - architecture_reflexion
      - complexity_churn_hotspots
      - defect_and_revert_concentration
      - temporal_coupling
      - ownership_concentration
      - near_clone_detection
      - semantic_duplication_candidates
      - whole_program_dead_code
      - unused_exports
      - unused_dependencies
      - feature_flag_age
      - stale_compatibility_candidates
      - dependency_lifecycle_and_support
      - sbom_generation
      - mutation_sampling
      - test_speed_and_flake_analysis
      - build_critical_path
      - bundle_binary_container_composition
      - documentation_symbol_and_architecture_drift
      - migration_completion_analysis

  investigative:
    triggers:
      - confirmed_performance_regression
      - recurring_incident
      - high_ranked_hotspot
      - major_migration
      - high_impact_security_exposure
      - unexplained_resource_growth
      - concurrency_failure
      - architecture_replacement
    available_analyses:
      - cpu_sampling
      - wall_clock_profiling
      - heap_and_allocation_profiling
      - retention_analysis
      - io_profiling
      - database_query_and_plan_analysis
      - distributed_tracing
      - lock_and_wait_graph_analysis
      - race_detection
      - scheduler_stress
      - fault_injection
      - cancellation_and_shutdown_testing
      - fuzzing
      - model_based_testing
      - threat_modeling
      - llm_semantic_duplication_review
      - llm_simplification_review
      - human_architecture_review

hotspot_model:
  normalization: repository_percentile
  components:
    complexity: 0.25
    churn: 0.25
    defect_history: 0.15
    coupling_or_centrality: 0.15
    test_weakness: 0.10
    ownership_concentration: 0.10
  preserve_component_scores: true
  composite_is_not_gate: true

prioritization:
  factor_scale: [1, 2, 3, 4, 5]
  expected_benefit:
    formula: >
      severity * breadth * recurrence *
      (1 + 0.25 * strategic_leverage)
  delivery_burden:
    formula: >
      effort *
      (1 + 0.25 * migration_risk
         + 0.25 * regression_risk
         + 0.15 * coordination_cost
         + 0.15 * rollout_complexity)
  priority:
    formula: >
      expected_benefit * evidence_confidence /
      delivery_burden
  bands:
    P0: active_safety_security_data_loss_or_outage
    P1: confirmed_broad_or_recurring_risk
    P2: strong_evidence_planned_work
    P3: opportunistic_adjacent_work
    investigate: material_hypothesis_insufficient_evidence
    accept: remediation_cost_exceeds_expected_benefit

finding_schema:
  required:
    - id
    - title
    - scope
    - finding
    - evidence
    - consequence
    - recommendation
    - expected_benefit
    - risk
    - validation
    - confidence
    - priority
  optional:
    - alternatives
    - owner
    - dependencies
    - rollout
    - rollback
    - waiver

waivers:
  required_fields:
    - owner
    - reason
    - evidence
    - expiry
    - review_date
  prohibit_permanent_waivers: true

outputs:
  machine_readable:
    - sarif
    - json
    - csv
  human_readable:
    - hotspot_report
    - architecture_report
    - simplification_report
    - prioritized_findings
    - health_dimension_summary
  provenance:
    include:
      - commit
      - tool_versions
      - configurations
      - workload_definitions
      - timestamps
      - evidence_hashes
```

---

# 28. Minimal continuous CI audit

The continuous tier should be fast, deterministic, and low-noise.

| Check | Scope | Policy |
|---|---|---|
| Compile and type validation | Changed and affected targets | No new errors |
| Formatting and high-confidence lint | Changed code | No new deterministic violations |
| Local complexity | Changed functions | Review extreme regressions; do not fail on legacy total |
| Architecture rules | Changed and affected modules | No new violations |
| Dependency cycles | Declared architectural modules | No new cross-boundary cycle |
| Exact clones | Changed code | Review meaningful new duplication |
| Unused imports/private symbols | Changed code | No new dead local code |
| Secrets | Change and relevant history | No verified secret |
| SAST and taint | Changed and affected paths | No unwaived high-confidence critical finding |
| Dependency review | Lockfile and manifest deltas | Contextual vulnerability and policy gate |
| Tests | Changed and affected behavior | Required tests pass; no new flake |
| Branch evidence | Critical changed code | Meaningful branch and failure-path coverage |
| Public API diff | Exported surface | Compatibility review required |
| Performance budget | Only sensitive paths or artifacts | No unexplained regression |
| Machine-readable evidence | All checks | SARIF or equivalent, with suppressions and expiry |

Continuous CI should generally block only:

- Deterministic regressions.
- Confirmed safety, security, or correctness risks.
- Violations of explicit architecture contracts.
- Evidence-budget regressions on known critical paths.

Everything else should create ranked work rather than an unmanageable sea of warnings.

---

# 29. Deeper periodic audit

Run monthly, quarterly, or before a major architectural initiative.

## Repository and architecture

- Full dependency graph.
- Strongly connected components.
- Cross-layer and cross-domain access.
- Centrality and bridge analysis.
- Architecture reflexion.
- Public API growth.
- Framework and vendor leakage.
- Shared-state boundary review.

## Evolution

- Complexity × churn.
- Defects and incidents.
- Temporal coupling.
- Reverts.
- Ownership concentration.
- Long-lived migrations.
- Repeated waivers.
- Architectural exceptions.

## Simplification

- Whole-program dead-code candidates.
- Unused exports.
- Unused dependencies.
- Old feature flags.
- Obsolete compatibility.
- Duplicate schemas and transformations.
- Abstraction collapse candidates.
- Configuration reduction.
- Deployment and pipeline consolidation.

## Tests and correctness

- Mutation sampling of high-risk hotspots.
- Property and invariant gaps.
- Flaky and slow tests.
- Excessive mocking.
- Failure-path test inventory.
- Contract drift.
- Concurrency and cancellation tests.

## Supply chain and security

- Full SBOM.
- Direct and transitive lifecycle review.
- Reachability-aware vulnerability review.
- Unsupported components.
- Privilege and trust-boundary review.
- Secret-history audit.
- Threat-model update for changed architecture.

## Runtime and delivery

- Production or representative profiles.
- Build and test critical paths.
- Cache effectiveness.
- Startup behavior.
- Artifact composition.
- Telemetry quality and cardinality.
- Incident diagnosability exercise.

---

# Universal Codebase Improvement Stack

## Tier 1 — Continuous

Fast checks appropriate for every commit or pull request:

- Compile, type, and deterministic lint.
- Changed-code complexity and nesting.
- Architecture fitness functions.
- No new module cycles.
- Exact-duplication review.
- Dead local-code checks.
- Secret, SAST, and dependency-delta scanning.
- Changed and affected tests.
- Critical branch and failure-path evidence.
- Public API compatibility diff.
- Targeted performance and artifact budgets.
- Machine-readable findings with expiring waivers.

### Governing rule

> Prevent new known problems; do not make every legacy issue block every change.

---

## Tier 2 — Periodic

Deeper analysis run on a schedule or before major planning:

- Complexity × churn hotspots.
- Defect and incident concentration.
- Temporal coupling.
- Ownership concentration.
- Full dependency graph and architecture drift.
- Near and semantic duplication.
- Whole-program dead code.
- Feature-flag and compatibility cleanup.
- Dependency lifecycle and SBOM review.
- Mutation sampling.
- Flaky and slow-test analysis.
- Build and delivery profiling.
- Documentation and terminology drift.
- Simplification and de-abstraction review.

### Governing rule

> Convert repository-wide evidence into a small ranked set of changes, not hundreds of disconnected warnings.

---

## Tier 3 — Investigative

Expensive analysis triggered by evidence:

- CPU, memory, allocation, I/O, database, network, and lock profiling.
- Distributed tracing and critical-path analysis.
- Race detection and scheduler stress.
- Fault injection.
- Cancellation and shutdown testing.
- Fuzzing and model-based testing.
- Security threat modeling.
- Architecture replacement or migration review.
- AI-assisted semantic duplication and simplification analysis.
- Domain-model and API redesign.
- Human review of high-impact abstractions and boundaries.

### Governing rule

> Investigate when static, historical, operational, or incident evidence indicates that the potential benefit justifies the cost.

---

# Final recommendation

The universal audit should not ask only:

> “Which functions exceed a complexity threshold?”

It should maintain an evidence model linking:

```text
code structure
    + dependency structure
    + repository history
    + tests
    + runtime behavior
    + incidents
    + security boundaries
    + ownership
    + architectural intent
```

That model should then identify:

- Where developers repeatedly struggle.
- Where changes propagate unexpectedly.
- Where defects and incidents concentrate.
- Where runtime cost actually occurs.
- Where tests give false confidence.
- Where architecture has drifted.
- Where dependencies create disproportionate risk.
- Where state and interfaces permit invalid behavior.
- Where abstractions add more cognitive load than value.
- Where code, configuration, processes, and concepts can be deleted.

The highest-quality outcome is not the repository with the best aggregate score. It is the repository in which:

> **Required behavior is easy to locate, safe to change, efficient to run, straightforward to diagnose, difficult to misuse—and supported by no more code, state, dependencies, configuration, or conceptual machinery than the problem genuinely requires.**

---

## Turn 003

**Role:** User  
**Date/time:** Not available

I would like this Universal Code Auditing capability to be available to Octon Mini (https://github.com/cooperonlineenterprises/octon-mini) to leverage without having to build it into Octon Mini. What are my best options?

---

## Turn 004

**Role:** Assistant  
**Date/time:** Not available

Yes. Octon Mini is already architecturally close to supporting this cleanly, and I would **not put the Universal Code Auditing implementation inside Octon Mini**.

The strongest design is to make code auditing an **independently versioned external capability** with a small, generic integration contract that Octon Mini can invoke and consume.

Octon Mini’s current architecture strongly supports this direction. Its v4 design deliberately keeps the universal kernel thin and moves non-universal functionality into trigger-installed packages. Its package registry already records package identity, version, content digest, owner, trust decision, validation receipt, and evidence without granting permission. Workflow capabilities are explicitly installed inactive and adopted separately, which is exactly the lifecycle you want for something like code auditing.

## Recommended architecture

I would create something conceptually like:

```text
Universal Code Audit
independent project / executable
            │
            │ stable machine contract
            ▼
Octon External Capability Adapter
very small, generic integration layer
            │
            ▼
        Octon Mini
tasks / evidence / validation / decisions
```

The important distinction is:

> **Octon Mini governs the use of the capability. It does not implement the capability.**

That keeps Octon Mini lightweight while allowing the auditing system to become sophisticated independently.

### The external capability

Create a separate repository, perhaps:

```text
cooperonlineenterprises/universal-code-audit
```

or a more product-like name later.

It should be usable completely independently of Octon Mini:

```bash
uca discover --repo .
uca audit --repo . --tier continuous
uca audit --repo . --tier periodic
uca audit --repo . --tier investigative
uca explain UCA-ARCH-0042
```

It would own all the machinery from the Universal Code Audit framework:

```text
Repository discovery
Static structural analysis
Dependency graph construction
Architecture analysis
Git/history mining
Complexity × churn
Temporal coupling
Duplication
Dead-code analysis
Dependency health
Test analysis
Security analysis
Performance orchestration
Simplification analysis
Semantic/AI analysis
Prioritization
```

But I would **not** make it one giant analyzer that reinvents Semgrep, CodeQL, OSV, profilers, coverage systems, etc.

Instead, make it an **audit orchestrator + evidence fusion engine**.

It should be capable of using:

```text
native compiler/language tooling
        +
specialized third-party analyzers
        +
repository history
        +
runtime profiles
        +
its own graph algorithms
        +
optional semantic/LLM analysis
```

and normalize all of them into one universal evidence model.

That gives you the methodology we developed without trying to recreate every mature analyzer.

---

# The key architectural addition to Octon Mini

I would introduce one generic concept to Octon Mini:

# External Capability Provider

Not:

```text
UniversalCodeAuditSupport
```

but something reusable:

```text
harness.external-capability.v1
```

or:

```text
harness.capability-provider.v1
```

Then Universal Code Audit becomes merely the **first provider**.

That small distinction has a large payoff. Later Octon Mini could use the same mechanism for:

```text
code auditing
repository intelligence
performance profiling
architecture recovery
documentation analysis
UI testing
browser testing
formal verification
research engines
design analysis
financial modeling
specialized security analysis
```

without adding each capability to Octon Mini.

The generic seam becomes part of Octon Mini; the capabilities do not.

---

# What the provider contract should contain

Keep v1 deliberately narrow.

For example:

```json
{
  "schema_version": "harness.capability-provider.v1",
  "id": "universal-code-audit",
  "version": "1.3.0",
  "interface": "local-json-process",
  "executable": "uca",
  "capabilities": [
    "repository-discovery",
    "continuous-audit",
    "periodic-audit",
    "investigative-audit",
    "finding-explanation"
  ],
  "project_access": "read_only",
  "network_access": "declared",
  "project_writes": "prohibited",
  "output_contract": "uca.audit-bundle.v1"
}
```

Octon Mini would care about:

- what provider this is;
- exact version;
- digest/provenance;
- who adopted it;
- which capability it exposes;
- what access it requires;
- whether it can execute local processes;
- whether it requires network access;
- what output schema it promises;
- whether the output is current;
- whether its invocation was successful.

It would **not** care how the auditor calculates cognitive complexity or identifies temporal coupling.

That belongs entirely to the provider.

---

# Keep the auditor read-only

This is especially important.

The Universal Code Audit capability should initially have:

```text
repository read:       yes
Git history read:      yes
local tool execution:  declared
network:               optional/declared
repository mutation:   no
automatic refactoring: no
authority creation:    no
```

It produces recommendations.

Octon Mini then decides whether one becomes work:

```text
audit finding
    ↓
candidate recommendation
    ↓
Octon TASK / decision
    ↓
normal governed implementation
    ↓
validation
```

That maintains one of Octon Mini's strongest architectural properties:

> **Outputs are evidence, not authority.**

It also prevents the auditing system from becoming a second control plane.

---

# Evidence should be the integration boundary

This is probably the most important design decision.

Do **not** tightly couple Octon Mini to auditor APIs such as:

```python
auditor.calculate_churn()
auditor.find_dead_code()
auditor.run_semgrep()
```

Instead:

```text
Octon requests an audit
        ↓
external provider performs it
        ↓
provider emits immutable evidence bundle
        ↓
Octon consumes bundle
```

A bundle might look like:

```text
audit-2026-08-27/
├── manifest.json
├── findings.json
├── metrics.json
├── coverage.json
├── assumptions.json
├── dependency-graph.json
├── hotspots.json
├── provenance.json
└── raw/
    ├── semgrep.sarif
    ├── osv.json
    ├── complexity.json
    └── history.json
```

`manifest.json` should bind:

```text
repository revision
audit tier
provider version
provider digest
configuration digest
included paths
excluded paths
tools and exact versions
analysis start/end
known blind spots
evidence digests
result status
```

This makes audit results replayable and attributable.

---

# Use SARIF, but don't make SARIF the whole contract

SARIF is excellent for:

```text
file
line
rule
severity
message
scanner
```

So supporting it is worthwhile.

But Universal Code Audit needs concepts SARIF does not represent naturally:

```text
complexity × churn
architecture communities
temporal coupling
dependency centrality
module instability
conceptual duplication
migration debt
performance profiles
state ownership
simplification candidates
abstraction-collapse candidates
evidence confidence
expected benefit
refactoring cost
```

So I would use:

```text
SARIF
  ↓
scanner interoperability

UCA Audit Bundle
  ↓
canonical audit evidence
```

rather than trying to force the entire methodology into SARIF.

---

# How this fits Octon Mini's existing package system

There's a very good fit already.

The current package registry supports kinds including `domain_extension` and `workflow_capability`, along with content digests, accepted trust decisions, owners, validation status, and evidence.

And Octon Mini already makes a useful distinction:

> Extensions are installed disabled; workflow capabilities are installed inactive; project adoption is separate.

I would classify **Universal Code Audit integration as a `workflow_capability`**, not as an ordinary extension.

Why?

Existing Octon extensions are intentionally restricted. The extension contract requires network access to be denied, filesystem writes prohibited, and authority effects to be restrictions-only. The existing security extension even explicitly says it validates declarations but **does not run scanners or generate an SBOM**.

A real code audit is different. It orchestrates work:

```text
discover
→ choose analyses
→ execute analyzers
→ normalize evidence
→ combine signals
→ prioritize findings
```

That is a workflow capability.

The actual package inside Octon Mini could be tiny:

```text
universal-code-audit/
├── README.md
├── provider.json
├── config.json
├── schemas/
│   └── audit-reference.json
├── validate.py
└── workflow.json
```

No clone detector.

No graph engine.

No Semgrep integration.

No Git miner.

No performance profiler.

Those remain outside Octon Mini.

---

# Five viable deployment options

I would rank them this way.

| Option | Coupling | Governance | Interactive | Reusable outside Octon | Recommendation |
|---|---:|---:|---:|---:|---|
| **1. External CLI + provider contract** | Very low | Excellent | Excellent | Excellent | **Best foundation** |
| **2. CLI + MCP wrapper + CI wrapper** | Very low | Excellent | Excellent | Excellent | **Best complete architecture** |
| **3. CI/GitHub Action produces evidence** | Minimal | Excellent | Limited | Excellent | Excellent complement |
| **4. MCP-only audit service** | Low | Moderate | Excellent | Good | Secondary interface |
| **5. Hosted/SaaS audit service** | Low code coupling | Moderate | Good | Good | Optional provider |

## 1. External CLI — strongest foundation

This should be canonical.

Advantages:

- Works locally.
- Works offline where possible.
- Easy for agents to invoke.
- Easy to sandbox.
- Easy to version.
- Easy to test.
- Easy to run from CI.
- No client protocol dependency.
- Excellent reproducibility.

Octon Mini already recognizes shell-based scoped local commands as part of its tool boundary, while remaining declarative and non-authorizing.

So:

```bash
uca audit --request request.json --output /tmp/audit
```

is a very natural boundary.

---

# 2. Same engine, multiple front doors

This is the architecture I would ultimately build:

```text
                  ┌── uca CLI
                  │
Universal Audit ──┼── uca-mcp
     Engine       │
                  ├── GitHub Action
                  │
                  ├── OCI container
                  │
                  └── optional HTTP service
```

One implementation.

Multiple transports.

Octon Mini should care only about the provider contract and evidence.

That avoids the common mistake where:

```text
CLI logic
MCP logic
CI logic
cloud logic
```

all gradually become different implementations.

---

# 3. CI/GitHub Action

This is an excellent complementary mode.

For example:

```yaml
- uses: cooperonlineenterprises/universal-code-audit@v1
  with:
    tier: continuous
```

It could run:

```text
continuous     on PRs
periodic       nightly/weekly
deep           manually/on release
```

and produce:

```text
SARIF
UCA audit bundle
HTML report
machine-readable summary
```

Octon Mini can then consume a specific immutable artifact as evidence rather than rerunning everything.

This is especially appropriate for:

- history mining;
- CodeQL;
- mutation testing;
- repository-wide dependency analysis;
- expensive graph analysis;
- scheduled audits.

---

# 4. MCP

MCP is useful, but I would **not make it the canonical interface**.

An MCP surface could expose:

```text
audit_repository
find_hotspots
inspect_module
find_dead_code
analyze_dependency_cycles
find_duplication
explain_finding
suggest_simplifications
compare_audits
```

This would be excellent for Codex, Claude Code, Cursor, and other agent systems.

However, Octon Mini itself currently does not make MCP part of its long-running capability; the current design explicitly lists MCP/ACP among deferred capabilities requiring separate proof and placement.

So I would architect it as:

```text
             ┌── CLI ← Octon Mini
Audit Engine ┤
             └── MCP ← agent environments
```

rather than:

```text
Octon Mini → MCP → audit implementation
```

as the only path.

Later Octon could add generic MCP-backed providers without changing Universal Code Audit.

---

# 5. Existing commercial/open-source services as providers

There is also a path where you build almost no analysis engine initially.

The external capability could federate:

```text
CodeQL
Semgrep
Sonar
CodeScene
OSV
native compiler/linter tools
coverage systems
profilers
```

and concentrate on what is actually novel:

> **Evidence fusion, prioritization, architectural reasoning, simplification analysis, and normalization.**

This is appealing because the Universal Audit methodology is much more valuable as the **system that decides what matters** than as the 37th implementation of a cyclomatic-complexity parser.

Over time, individual analyzer implementations can be replaced where strategically valuable.

---

# A particularly strong hybrid

I'd implement three audit classes:

```text
UCA Deterministic Core
├── repository discovery
├── Git history analysis
├── dependency graph
├── metric normalization
├── evidence fusion
├── prioritization
└── audit bundle generation

UCA Tool Adapters
├── Semgrep
├── CodeQL
├── OSV
├── language-native tooling
├── coverage/mutation systems
└── profilers

UCA Semantic Analyst
├── semantic duplication
├── responsibility analysis
├── architecture interpretation
├── over-engineering
├── domain-model quality
└── simplification opportunities
```

Critically:

```text
Deterministic finding
≠
heuristic finding
≠
AI inference
```

The audit evidence model should preserve those distinctions.

That fits Octon's evidence philosophy extremely well.

---

# One thing I would avoid

I would **not** add dozens of audit commands to Octon:

```text
octon complexity
octon duplication
octon dead-code
octon dependency-health
octon hotspots
octon profile
octon architecture-audit
...
```

That would slowly turn Octon Mini into the implementation platform for every specialized capability.

Likewise, I would avoid putting large analyzer libraries under:

```text
.agent/scripts/
```

or:

```text
skills/octon-mini-project-bootstrap/
```

The generated harness would become progressively heavier and harder to upgrade.

Octon Mini should remain responsible for:

```text
Should this capability be used?
Which version?
Was it trusted?
What access does it require?
What task requested it?
What exact repository state did it inspect?
What evidence did it produce?
How fresh is that evidence?
Can the result support a finding?
Does a recommendation require a decision?
Was the resulting change validated?
```

Universal Code Audit should answer:

```text
What did we find?
Why?
How confident are we?
Why does it matter?
What could improve it?
How should the improvement be validated?
```

That is an excellent separation of concerns.

# Recommended target architecture

I would therefore pursue this:

```text
┌─────────────────────────────────────────────────────────────┐
│                       OCTON MINI                            │
│                                                             │
│ Task / Decision / Authority / Evidence / Validation         │
│                                                             │
│       Generic External Capability Provider Contract         │
└────────────────────────────┬────────────────────────────────┘
                             │
                 immutable request + policy
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              UNIVERSAL CODE AUDIT PROVIDER                  │
│                 separately versioned                       │
│                                                             │
│ Discovery → Analysis → Evidence Fusion → Prioritization     │
│                                                             │
│ Deterministic   Tool-backed   Runtime   Semantic/AI         │
└────────────────────────────┬────────────────────────────────┘
                             │
                       Audit Bundle
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                         OCTON                               │
│                                                             │
│ Finding → Evidence → Recommendation → TASK/DEC if adopted   │
└─────────────────────────────────────────────────────────────┘
```

And expose that provider through:

```text
1. CLI        ← canonical
2. OCI image  ← reproducible/sandboxed
3. CI Action  ← continuous + periodic
4. MCP        ← agent-native exploration
5. HTTP       ← optional future remote execution
```

## My ranking

**Best immediate solution:** build Universal Code Audit as a standalone CLI and let Octon Mini invoke it as an external read-only tool.

**Best architectural solution:** add a small, generic **External Capability Provider Contract** to Octon Mini, and make Universal Code Audit its first provider.

**Best eventual product:** one independent Universal Code Audit engine with CLI + CI + MCP interfaces, while Octon Mini owns only adoption, trust, invocation, evidence, and downstream action governance.

That gives you exactly what you're after: **Octon Mini acquires the capability without acquiring the implementation or its weight.**

## Turn 005

**Role:** User  
**Date/time:** Not available

Execute the below **complete development-blueprint inquiry**, while preserving the architectural direction we just established.

> # Universal Code Audit — Complete Development Blueprint
>
> Act as a **principal software architect, developer-tools architect, agent-systems architect, security architect, product engineer, and technical program lead**.
>
> I want to pursue the recommended **“Best eventual product” architecture for Universal Code Audit (UCA)**:
>
> > Build **Universal Code Audit as an independent, separately versioned audit engine** with a canonical CLI and additional CI, MCP, containerized, and potentially remote-service interfaces. Octon Mini should be able to leverage UCA through a small, generic External Capability Provider contract while retaining responsibility for trust, adoption, invocation governance, evidence handling, decisions, authority, validation, and downstream work.
>
> The objective of this inquiry is to produce a **complete, implementation-oriented blueprint for everything required to take Universal Code Audit from concept to a robust, production-quality project**.
>
> Do not merely describe the architecture at a high level. Identify the actual systems, components, contracts, schemas, repositories, modules, workflows, interfaces, implementation phases, validation mechanisms, infrastructure, tests, documentation, governance, and release work that must exist.
>
> ---
>
> ## 1. Establish the Product Boundary
>
> First define precisely what Universal Code Audit is—and what it is not.
>
> Clarify the separation of responsibilities between:
>
> * Universal Code Audit;
> * Octon Mini;
> * external analyzers such as CodeQL, Semgrep, OSV, language-native tooling, profilers, coverage systems, and mutation-testing systems;
> * CI platforms;
> * MCP clients and coding agents;
> * optional future hosted services.
>
> Preserve these architectural principles unless strong evidence supports changing them:
>
> * UCA is independently usable without Octon Mini.
> * Octon Mini does not contain the auditing implementation.
> * UCA does not become a second governance/control plane.
> * Audit output is **evidence and recommendation, not authority**.
> * Repository mutation and automated refactoring are outside the initial audit boundary.
> * The canonical implementation should not be duplicated across CLI, MCP, CI, container, or HTTP surfaces.
> * Expensive or specialized analysis should be delegated to best-in-class tools where appropriate rather than unnecessarily reimplemented.
> * Deterministic evidence, heuristic evidence, runtime evidence, and AI-derived interpretation must remain distinguishable.
> * The system should optimize for **capability-to-weight ratio**, maintainability, portability, reproducibility, extensibility, and auditability.
>
> Identify any additional invariants that should govern the project.
>
> ---
>
> ## 2. Define the Complete Product Architecture
>
> Design the full target architecture.
>
> At minimum, determine whether UCA should contain distinct subsystems such as:
>
> * repository/project discovery;
> * language/framework/toolchain detection;
> * audit planning;
> * analyzer selection;
> * tool adapters;
> * static analysis;
> * repository-history analysis;
> * dependency-graph construction;
> * architecture analysis;
> * duplication analysis;
> * dead-code/reachability analysis;
> * dependency and supply-chain analysis;
> * testing-quality analysis;
> * runtime/performance evidence ingestion;
> * security evidence ingestion;
> * state/data-flow analysis;
> * semantic/AI-assisted analysis;
> * simplification/de-abstraction analysis;
> * evidence normalization;
> * evidence fusion;
> * hotspot analysis;
> * prioritization;
> * finding generation;
> * audit comparison/trending;
> * reporting;
> * provenance;
> * configuration;
> * caching;
> * plugin/adapter discovery;
> * execution/sandboxing;
> * artifact storage.
>
> For each subsystem, specify:
>
> * responsibility;
> * inputs;
> * outputs;
> * dependencies;
> * deterministic vs heuristic behavior;
> * ownership boundary;
> * extension points;
> * failure behavior;
> * whether it belongs in the initial implementation or later.
>
> Show the major data flows and control flows.
>
> ---
>
> ## 3. Define the Canonical Audit Engine
>
> Determine what should constitute the **single authoritative UCA engine** beneath all interfaces.
>
> Explain:
>
> * how an audit request is represented;
> * how an audit plan is generated;
> * how applicable analyzers are selected;
> * how analyses are executed;
> * how evidence is normalized;
> * how signals are combined;
> * how confidence is represented;
> * how findings are generated;
> * how recommendations are prioritized;
> * how partial/failed/unknown analysis is represented;
> * how output remains reproducible.
>
> Identify which portions should be written directly by UCA and which should normally be supplied through adapters to external tooling.
>
> Avoid building a monolithic “mega-analyzer.”
>
> ---
>
> ## 4. Define Audit Modes and Tiers
>
> Turn the previously developed Universal Code Audit methodology into executable operating modes.
>
> At minimum consider:
>
> ### Continuous Audit
>
> Fast, low-noise checks suitable for local development and pull requests.
>
> ### Periodic Audit
>
> Broader repository-wide analysis suitable for scheduled execution.
>
> ### Investigative Audit
>
> Expensive analysis triggered by evidence, such as profiling, tracing, race detection, fault injection, semantic review, or deep architectural analysis.
>
> Determine:
>
> * what belongs in each tier;
> * execution budgets;
> * expected runtime;
> * trigger logic;
> * required evidence;
> * blocking vs advisory findings;
> * caching and reuse;
> * incremental analysis;
> * how one tier escalates into another.
>
> ---
>
> ## 5. Design the Evidence Model
>
> Treat the **audit evidence model as one of the project's most important contracts**.
>
> Design schemas for:
>
> * audit request;
> * audit plan;
> * audit manifest;
> * repository identity;
> * analyzed revision;
> * scope and exclusions;
> * analyzer identity/version/configuration;
> * raw evidence;
> * normalized evidence;
> * metric observations;
> * graph evidence;
> * runtime evidence;
> * historical evidence;
> * semantic/AI evidence;
> * findings;
> * recommendations;
> * confidence;
> * assumptions;
> * limitations;
> * blind spots;
> * waivers/suppressions;
> * provenance;
> * audit completion state;
> * comparison against prior audits.
>
> Define a canonical **UCA Audit Bundle**.
>
> Consider interoperability with:
>
> * SARIF;
> * CycloneDX/SPDX;
> * OpenTelemetry;
> * coverage formats;
> * profiler formats;
> * CodeQL;
> * Semgrep;
> * OSV;
> * other common machine-readable outputs.
>
> Do not force concepts into SARIF where SARIF is insufficient.
>
> ---
>
> ## 6. Design the Finding and Prioritization Model
>
> Operationalize the finding model developed during the Universal Code Audit research.
>
> Each finding should clearly distinguish:
>
> * finding;
> * evidence;
> * interpretation;
> * consequence;
> * recommendation;
> * expected benefit;
> * confidence;
> * scope;
> * risk;
> * validation strategy;
> * priority;
> * suppressibility/waiver behavior;
> * provenance.
>
> Determine how UCA should handle:
>
> * deterministic findings;
> * probabilistic/heuristic findings;
> * AI-assisted findings;
> * conflicting evidence;
> * incomplete evidence;
> * stale evidence;
> * duplicate findings;
> * recurring findings;
> * accepted debt;
> * findings that require investigation rather than remediation.
>
> Define the prioritization algorithm without creating an opaque or gameable “code quality score.”
>
> ---
>
> ## 7. External Analyzer and Tool Adapter Architecture
>
> Define a clean adapter architecture for tools such as:
>
> * CodeQL;
> * Semgrep;
> * OSV-Scanner;
> * Trivy;
> * Syft;
> * Sonar;
> * CodeScene;
> * language compilers and linters;
> * test frameworks;
> * coverage tools;
> * mutation-testing systems;
> * profilers;
> * database query analyzers;
> * race detectors;
> * fuzzers;
> * property-based testing systems;
> * architecture-test systems.
>
> Determine:
>
> * adapter interface;
> * capability discovery;
> * version requirements;
> * invocation;
> * sandboxing;
> * timeout/resource handling;
> * parsing;
> * normalization;
> * unavailable-tool behavior;
> * unsupported-language behavior;
> * dependency installation policy;
> * offline behavior;
> * caching;
> * provenance;
> * adapter testing.
>
> UCA should not silently install or trust arbitrary tooling.
>
> ---
>
> ## 8. Language and Framework Agnosticism
>
> Define how UCA can remain genuinely cross-language without collapsing into lowest-common-denominator analysis.
>
> Design:
>
> * universal analysis capabilities;
> * language-specific capability packs/adapters;
> * framework-specific knowledge;
> * native compiler/LSP integration;
> * AST/CFG/symbol graph interfaces;
> * language capability detection;
> * graceful degradation.
>
> Explain what should be universal versus language-specific.
>
> ---
>
> ## 9. Semantic and AI-Assisted Analysis
>
> Design AI-assisted analysis as a governed evidence source rather than an unquestioned oracle.
>
> Cover:
>
> * semantic duplication;
> * responsibility analysis;
> * conceptual complexity;
> * domain modeling;
> * architecture interpretation;
> * obsolete compatibility;
> * over-engineering;
> * inappropriate abstraction;
> * simplification/de-abstraction;
> * stale documentation;
> * terminology inconsistency;
> * API usability.
>
> Define:
>
> * input/context construction;
> * model-provider abstraction;
> * structured output;
> * evidence references;
> * confidence;
> * reproducibility limitations;
> * model/version provenance;
> * privacy;
> * secret handling;
> * offline/local-model support;
> * human-review requirements;
> * protection against AI findings being mistaken for deterministic evidence.
>
> ---
>
> ## 10. CLI Design
>
> Make the CLI the canonical user and automation interface.
>
> Develop the command model, potentially including:
>
> ```text
> uca discover
> uca plan
> uca audit
> uca inspect
> uca explain
> uca compare
> uca report
> uca adapters
> uca doctor
> uca schema
> ```
>
> Determine:
>
> * command hierarchy;
> * configuration precedence;
> * exit codes;
> * stdout/stderr behavior;
> * JSON mode;
> * human-readable mode;
> * progress reporting;
> * deterministic/noninteractive mode;
> * local cache;
> * artifact location;
> * failure semantics.
>
> ---
>
> ## 11. CI Integration
>
> Design first-class CI use.
>
> Include:
>
> * GitHub Actions;
> * generic CI usage;
> * PR auditing;
> * changed-code analysis;
> * baseline/ratchet behavior;
> * scheduled audits;
> * artifact persistence;
> * annotations;
> * SARIF upload;
> * performance budgets;
> * cache reuse;
> * merge blocking;
> * advisory findings;
> * audit comparison;
> * secrets and credentials.
>
> Define what UCA itself should own versus what the CI platform owns.
>
> ---
>
> ## 12. MCP Interface
>
> Design an MCP server as a thin interface over the canonical engine.
>
> Potential capabilities include:
>
> * audit repository;
> * inspect hotspots;
> * explain finding;
> * inspect module;
> * analyze dependencies;
> * inspect duplication;
> * find dead code;
> * investigate architecture;
> * suggest simplification;
> * compare audits.
>
> Define what should and should not be exposed.
>
> Ensure the MCP implementation does not become a second UCA engine.
>
> ---
>
> ## 13. Container and Sandboxed Execution
>
> Define a reproducible containerized distribution.
>
> Consider:
>
> * OCI images;
> * tool bundles;
> * minimal vs extended images;
> * filesystem mounts;
> * read-only repository mounts;
> * network policies;
> * CPU/memory/time limits;
> * cache mounts;
> * analyzer isolation;
> * provenance;
> * image signing;
> * supply-chain security.
>
> Determine whether a container should eventually be the preferred execution boundary for Octon Mini.
>
> ---
>
> ## 14. Optional Remote/Hosted Architecture
>
> Design for—but do not prematurely require—a future hosted UCA service.
>
> Determine what abstractions should exist now so that a future service can provide:
>
> * remote audits;
> * queued audits;
> * large-scale analysis;
> * organizational baselines;
> * historical trending;
> * shared caches;
> * managed toolchains;
> * centralized reporting.
>
> Keep local/offline execution a first-class capability.
>
> ---
>
> ## 15. Octon Mini Integration
>
> Design the minimal integration required for Octon Mini.
>
> Assume the preferred architectural direction is a generic:
>
> **External Capability Provider Contract**
>
> rather than UCA-specific functionality embedded in Octon Mini.
>
> Define:
>
> * provider manifest;
> * provider identity;
> * version;
> * digest;
> * provenance;
> * supported capabilities;
> * executable/interface location;
> * requested repository access;
> * network requirements;
> * filesystem effects;
> * sandbox requirements;
> * audit request contract;
> * audit result reference;
> * evidence freshness;
> * execution outcome;
> * limitations.
>
> Determine exactly what minimal additions Octon Mini would require.
>
> Preserve:
>
> * deny-by-default;
> * non-authorizing outputs;
> * explicit trust/adoption;
> * content-addressed packages;
> * project-owned decisions;
> * evidence provenance;
> * task-scoped authority;
> * no hidden provider installation;
> * no second command/control plane.
>
> Explain whether UCA should be represented inside Octon Mini as:
>
> * a workflow capability;
> * an external provider referenced by a thin workflow capability;
> * another mechanism;
>
> and justify the answer.
>
> ---
>
> ## 16. Repository and Source-Code Structure
>
> Propose the actual UCA repository layout.
>
> Show major directories/packages and their responsibilities.
>
> For example, determine appropriate placement for:
>
> * core engine;
> * schemas;
> * adapters;
> * languages;
> * analysis modules;
> * graph engine;
> * history analysis;
> * semantic analysis;
> * CLI;
> * MCP;
> * CI integration;
> * container;
> * fixtures;
> * test repositories;
> * documentation;
> * examples;
> * benchmarks.
>
> Recommend the implementation language and explain why.
>
> Consider whether some components should use different languages.
>
> ---
>
> ## 17. Configuration Model
>
> Define configuration for:
>
> * repository scope;
> * exclusions;
> * generated/vendor code;
> * audit tiers;
> * enabled analyzers;
> * budgets;
> * architecture rules;
> * performance budgets;
> * security policies;
> * baselines;
> * suppressions;
> * AI providers;
> * language adapters;
> * CI behavior.
>
> Avoid a sprawling configuration DSL.
>
> Explain configuration precedence and project/global/default behavior.
>
> ---
>
> ## 18. Caching, Incrementality, and Performance
>
> Design UCA so it can scale from small repositories to large monorepos.
>
> Cover:
>
> * content-addressed caching;
> * incremental analysis;
> * changed-file analysis;
> * graph invalidation;
> * history caching;
> * analyzer result reuse;
> * parallel execution;
> * resource scheduling;
> * memory limits;
> * timeout handling;
> * large-repository sampling where appropriate;
> * reproducibility.
>
> Define performance targets for the major audit modes.
>
> ---
>
> ## 19. Security and Trust Model
>
> Threat-model UCA itself.
>
> Consider malicious repositories, including:
>
> * hostile build scripts;
> * symlinks;
> * binaries;
> * decompression bombs;
> * parser exploits;
> * command injection;
> * crafted Git history;
> * untrusted configuration;
> * malicious analyzer output;
> * secret exposure;
> * network exfiltration;
> * dependency compromise;
> * model prompt injection;
> * poisoned source comments/documents;
> * excessive resource consumption.
>
> Define trust boundaries and safe defaults.
>
> ---
>
> ## 20. Testing and Validation Strategy
>
> Design a comprehensive test strategy.
>
> Include:
>
> * unit tests;
> * schema tests;
> * adapter contract tests;
> * golden fixtures;
> * synthetic repositories;
> * real open-source repository fixtures;
> * regression tests;
> * determinism tests;
> * cross-platform tests;
> * hostile-repository tests;
> * performance benchmarks;
> * large-repository tests;
> * analyzer-version compatibility tests;
> * AI-output validation;
> * CLI tests;
> * MCP tests;
> * CI integration tests;
> * Octon Mini provider-contract tests.
>
> Define how we determine that UCA findings are useful rather than merely numerous.
>
> ---
>
> ## 21. Evaluation and Quality Measurement
>
> Define how UCA itself should be evaluated.
>
> Possible measures include:
>
> * precision;
> * recall where measurable;
> * false-positive burden;
> * finding stability;
> * reproducibility;
> * time-to-useful-finding;
> * developer acceptance;
> * remediation yield;
> * validated simplification achieved;
> * code/dependency/configuration reduction;
> * defect correlation;
> * hotspot accuracy;
> * performance-improvement validation;
> * analysis cost.
>
> Avoid creating incentives for metric gaming.
>
> ---
>
> ## 22. Documentation Requirements
>
> Enumerate all documentation needed for a mature project, including:
>
> * README;
> * architecture;
> * concepts;
> * audit methodology;
> * CLI reference;
> * configuration;
> * schema reference;
> * adapter SDK;
> * language-adapter development;
> * MCP;
> * CI;
> * containers;
> * Octon Mini integration;
> * security model;
> * threat model;
> * evidence semantics;
> * finding taxonomy;
> * contribution guide;
> * release process;
> * compatibility policy;
> * troubleshooting;
> * examples.
>
> ---
>
> ## 23. Versioning and Compatibility
>
> Define independent versioning for:
>
> * UCA product;
> * audit bundle schema;
> * provider contract;
> * adapter API;
> * MCP API;
> * configuration schema;
> * finding taxonomy.
>
> Determine compatibility guarantees and migration strategy.
>
> ---
>
> ## 24. Packaging and Distribution
>
> Recommend distribution mechanisms such as:
>
> * standalone binaries;
> * package managers;
> * Python/Rust/Node packages if applicable;
> * OCI images;
> * GitHub Action;
> * MCP server package.
>
> Cover:
>
> * signing;
> * checksums;
> * SBOM;
> * provenance;
> * release artifacts;
> * reproducible builds;
> * update policy.
>
> ---
>
> ## 25. Development Workflow and Project Governance
>
> Define how the UCA project itself should be developed.
>
> Include:
>
> * architectural decision records;
> * issue taxonomy;
> * feature lifecycle;
> * experimental analyzers;
> * promotion criteria;
> * deprecation;
> * adapter ownership;
> * schema evolution;
> * compatibility reviews;
> * security review;
> * release gates;
> * benchmarking gates.
>
> ---
>
> ## 26. Implementation Roadmap
>
> Produce a concrete development sequence from an empty repository to the complete eventual product.
>
> Divide it into meaningful phases such as:
>
> 1. architectural kernel;
> 2. evidence contracts;
> 3. repository discovery;
> 4. deterministic core analysis;
> 5. history and graph intelligence;
> 6. adapter framework;
> 7. continuous audit;
> 8. periodic audit;
> 9. semantic analysis;
> 10. CLI stabilization;
> 11. CI;
> 12. MCP;
> 13. OCI/sandbox execution;
> 14. Octon Mini integration;
> 15. investigative runtime analysis;
> 16. production hardening;
> 17. optional hosted architecture.
>
> Do not assume these are the correct phases; improve the sequencing where appropriate.
>
> For every phase identify:
>
> * objective;
> * implementation work;
> * dependencies;
> * deliverables;
> * tests;
> * acceptance criteria;
> * risks;
> * what should explicitly be deferred.
>
> Identify the **critical path**.
>
> ---
>
> ## 27. MVP Versus Eventual Product
>
> Clearly distinguish:
>
> ### Minimum Viable Architecture
>
> The smallest implementation that proves the architecture is sound.
>
> ### Useful v1
>
> The smallest version that developers would genuinely benefit from.
>
> ### Production v1
>
> The version suitable for dependable project use.
>
> ### Eventual Product
>
> The complete CLI + CI + MCP + container + Octon-provider ecosystem.
>
> Prevent the MVP from becoming a throwaway architecture.
>
> ---
>
> ## 28. Build-vs-Integrate Decisions
>
> For each substantial capability, classify it as:
>
> * **Build in UCA**
> * **Integrate existing tool**
> * **Provide adapter abstraction**
> * **Defer**
>
> Explain why.
>
> Pay particular attention to avoiding reimplementation of mature analysis technology unless UCA gains meaningful architectural or product advantage from owning it.
>
> ---
>
> ## 29. Risk and Failure-Mode Analysis
>
> Identify ways this project could become:
>
> * too large;
> * too slow;
> * too noisy;
> * too dependent on external tooling;
> * too AI-dependent;
> * too configuration-heavy;
> * difficult to reproduce;
> * difficult to install;
> * difficult to secure;
> * language-biased;
> * architecturally coupled to Octon;
> * a second agent harness;
> * a generic scanner aggregator with little differentiated value.
>
> For each important risk, specify mitigation.
>
> ---
>
> ## 30. Final Deliverables
>
> Finish with a complete development package containing:
>
> 1. **Product definition**
> 2. **Architectural principles and invariants**
> 3. **System architecture**
> 4. **Component inventory**
> 5. **Canonical data/evidence flow**
> 6. **Audit mode definitions**
> 7. **UCA Audit Bundle specification**
> 8. **Finding/evidence schema**
> 9. **Adapter architecture**
> 10. **CLI architecture**
> 11. **CI architecture**
> 12. **MCP architecture**
> 13. **Container/sandbox architecture**
> 14. **Octon Mini External Capability Provider integration**
> 15. **Repository structure**
> 16. **Technology-stack recommendation**
> 17. **Security/trust model**
> 18. **Testing and evaluation strategy**
> 19. **Packaging/release strategy**
> 20. **Documentation plan**
> 21. **MVP definition**
> 22. **Production-v1 definition**
> 23. **Eventual-product definition**
> 24. **Phase-by-phase implementation roadmap**
> 25. **Dependency/critical-path map**
> 26. **Build-vs-integrate matrix**
> 27. **Risk register**
> 28. **Acceptance criteria for declaring the project production-ready**
> 29. **A prioritized implementation backlog**
> 30. **A concise “start here” sequence identifying exactly what should be built first**
>
> Where useful, provide proposed schemas, directory trees, API contracts, command examples, state machines, pseudocode, and interface definitions.
>
> The final result should be detailed enough that a capable engineering team—or governed coding agents working under human review—could begin implementation without needing another architecture-discovery phase.
>
> Above all, optimize for:
>
> > **A powerful, evidence-led universal code-auditing system that remains independently useful, composable, governable, lightweight at its integration boundaries, and resistant to becoming an oversized agent platform or scanner collection.**

## Turn 006

**Role:** Assistant  
**Date/time:** Not available

# Universal Code Audit — Complete Development Blueprint

## Executive architectural decision

Universal Code Audit should be built as a **local-first, independently versioned audit engine** whose durable product contract is not a dashboard, scanner integration, or agent interaction protocol, but a machine-readable **UCA Audit Bundle**.

The recommended architecture is:

```text
                                  ┌────────────────────┐
                                  │     UCA CLI        │  canonical
                                  └─────────┬──────────┘
                                            │
                 ┌──────────────────────────┼──────────────────────────┐
                 │                          │                          │
        ┌────────▼────────┐       ┌─────────▼────────┐       ┌────────▼────────┐
        │ GitHub/CI       │       │ MCP interface    │       │ Future HTTP     │
        │ thin invoker    │       │ thin projection  │       │ thin service    │
        └────────┬────────┘       └─────────┬────────┘       └────────┬────────┘
                 │                          │                          │
                 └──────────────────────────┼──────────────────────────┘
                                            │
                                  ┌─────────▼──────────┐
                                  │ Authoritative UCA  │
                                  │ Audit Engine       │
                                  └─────────┬──────────┘
                                            │
             ┌──────────────────────────────┼───────────────────────────────┐
             │                              │                               │
   ┌─────────▼─────────┐          ┌─────────▼──────────┐         ┌──────────▼─────────┐
   │ UCA-owned core    │          │ External analyzer │         │ Optional semantic  │
   │ analyses          │          │ adapters          │         │ model providers    │
   └─────────┬─────────┘          └─────────┬──────────┘         └──────────┬─────────┘
             │                              │                               │
             └──────────────────────────────┼───────────────────────────────┘
                                            │
                                  ┌─────────▼──────────┐
                                  │ UCA Audit Bundle   │
                                  │ evidence, findings │
                                  │ provenance, limits │
                                  └─────────┬──────────┘
                                            │
                  ┌─────────────────────────┴─────────────────────────┐
                  │                                                   │
       ┌──────────▼──────────┐                           ┌────────────▼────────────┐
       │ Independent users   │                           │ Octon Mini              │
       │ teams, CI, agents   │                           │ trust and work governor │
       └─────────────────────┘                           └─────────────────────────┘
```

The decisive implementation choices are:

| Decision | Recommendation |
|---|---|
| Core language | **Rust 2024 edition** |
| Canonical interface | **Native CLI** |
| Internal architecture | One reusable engine library beneath every interface |
| Extension boundary | **Out-of-process adapters**, never in-process arbitrary plugins |
| Evidence encoding | JSON Schema 2020-12 documents with canonical JSON digests |
| Durable artifact | Content-addressed **UCA Audit Bundle** |
| Local storage | Filesystem CAS plus SQLite metadata/index |
| Default authority | Read-only repository inspection; no repository mutation |
| Tool installation | Never automatic; exact tool identities are declared or prebundled |
| Network posture | Denied by default |
| Project execution | Disabled by default; explicitly requested per analysis |
| AI posture | Optional evidence source, segregated from deterministic evidence |
| CI integration | Thin wrapper around the CLI |
| MCP integration | Separate thin server over the same engine |
| Container strategy | Minimal engine image plus optional pinned toolbox images |
| Hosted strategy | Deferred; local execution remains first-class |
| Octon representation | An external provider referenced by a thin, trigger-installed workflow capability |
| Differentiated value | Evidence fusion, historical/architectural intelligence, prioritization, and simplification—not scanner aggregation |

Rust is well suited to a portable developer tool because it provides native performance, memory safety, strong typing, and cross-platform executable distribution. Tree-sitter can provide tolerant, incremental syntax structure across many languages, but should be treated as a baseline parser rather than a replacement for compilers, type checkers, or language-native semantic tooling.

---

# 1. Product definition and boundary

## 1.1 What Universal Code Audit is

Universal Code Audit is:

> A local-first, evidence-led repository analysis and audit-orchestration system that discovers the structure of a software project, selects and runs applicable analyses, normalizes heterogeneous evidence, combines independent signals, identifies consequential hotspots and simplification opportunities, and produces reproducible findings and recommendations.

Its differentiating responsibilities are:

1. Repository and toolchain discovery.
2. Deterministic audit planning.
3. Safe orchestration of internal analyses and external tools.
4. A universal evidence vocabulary.
5. Evidence provenance and completeness accounting.
6. Cross-signal fusion.
7. Stable finding identity across revisions.
8. Transparent prioritization.
9. Audit comparison and trending.
10. Simplification, deletion, and de-abstraction analysis.
11. A durable machine-readable audit bundle.
12. Thin interfaces for local, CI, MCP, container, and eventual remote use.

## 1.2 What Universal Code Audit is not

UCA is not:

- An agent harness.
- A project-governance system.
- An authority or approval system.
- An issue tracker.
- A replacement for CI.
- A replacement for compilers, profilers, SAST engines, mutation frameworks, or vulnerability databases.
- A package manager.
- A tool installer.
- A universal build system.
- A code-generation or automatic-refactoring system.
- A hosted service requirement.
- A single code-quality score.
- A claim that every supported language receives equal analytical depth.
- A guarantee that every finding is correct.
- A system that silently executes repository code.
- A system that automatically converts recommendations into work.

## 1.3 Responsibility allocation

| Concern | UCA | Octon Mini | External analyzer | CI platform | MCP client/agent | Future hosted service |
|---|---|---|---|---|---|---|
| Repository discovery | Owns | May request | May contribute | Supplies checkout | Requests/reads | May prepare snapshot |
| Audit methodology | Owns | Does not duplicate | Implements specific technique | Does not own | Does not own | Uses same engine |
| Analyzer selection | Owns under request/policy | May constrain | Declares capabilities | Supplies environment | May request tier | May schedule |
| Tool implementation | Only lightweight universal analyses | None | Owns specialized analysis | None | None | Managed toolchains |
| Tool installation | Never silent | Never silent | External concern | CI setup step | None | Managed with policy |
| Audit execution | Owns | Governs invocation only | Runs through adapter | Provides worker | Initiates through MCP | Queues and executes |
| Repository mutation | Outside initial boundary | Governed separately | Prohibited by UCA contract | Platform policy | Not exposed | Prohibited for audit jobs |
| Evidence normalization | Owns | Consumes references | Adapter supplies raw output | Persists artifacts | Reads structured results | Same engine |
| Finding generation | Owns | May register as evidence | Does not produce canonical UCA finding directly | Displays projections | Explains/filters | Same engine |
| Priority recommendation | Owns transparently | Project decides adoption | Supplies evidence | May gate selected policies | May inspect | May aggregate |
| Authority | None | Owns project authority model | None | Owns merge/deployment enforcement | None | None |
| Decision acceptance | None | Project-owned | None | None | Human/client concern | None |
| Work creation | None by default | Governs downstream work | None | Could open issue only by separate policy | Could propose | Optional integration |
| Artifact persistence | Produces bundle | Records reference/digest | Produces raw evidence | Stores artifacts/cache | Reads refs | Object storage |
| Organization reporting | Local report only initially | Project records | Tool-specific | CI UI | Client UI | Future responsibility |

## 1.4 Governing invariants

The project should adopt these as architectural invariants:

1. **One engine, multiple interfaces.** CLI, CI, MCP, OCI, and HTTP may not implement independent audit logic.
2. **Evidence is not authority.** A finding cannot authorize code changes, publication, deployment, dependency installation, or any external effect.
3. **Read-only by default.** Initial UCA releases may write only to explicit output, cache, and temporary directories.
4. **No hidden tool installation.** UCA may diagnose missing tools and provide exact setup guidance, but not install or update them.
5. **No hidden repository execution.** Build, test, code generation, package scripts, hooks, or repository-defined commands require explicit permission.
6. **Network denied by default.** Any network-requiring analysis must declare its endpoints, purpose, and policy basis.
7. **All analyzer output is untrusted input.**
8. **All repository content is untrusted data.** Comments, documentation, prompts, configuration, and filenames cannot alter UCA’s governing instructions.
9. **Partial truth must remain partial.** Missing analyzers, incomplete scope, timeouts, and parser limitations cannot be converted into a clean audit.
10. **Every finding must trace to evidence.**
11. **Every evidence item must trace to a producer, version, configuration, scope, and analyzed subject.**
12. **Deterministic, heuristic, runtime, historical, human-supplied, and AI-derived evidence remain distinct.**
13. **No universal quality score.** Dimension-level results and finding-level priorities remain visible.
14. **Stable identities must survive ordinary line movement and file renaming where possible.**
15. **Project configuration cannot silently widen execution, network, or filesystem rights.**
16. **External tools run through an explicit process or container boundary.**
17. **Language depth is declared, not implied.**
18. **A cache hit is evidence reuse, not evidence freshness by assumption.**
19. **Audit comparison must compare compatible scopes and methodologies or clearly report incompatibility.**
20. **Suppression does not delete evidence.**
21. **Accepted debt requires ownership, reason, scope, and expiry.**
22. **AI findings cannot become blocking findings solely through model confidence.**
23. **Every blocking policy must name the exact deterministic rule or evidence requirement that failed.**
24. **UCA’s differentiated value must remain evidence fusion and decision usefulness, not the number of scanner integrations.**

---

# 2. Complete product architecture

## 2.1 Architectural layers

```text
Layer 1 — Interfaces
  CLI | CI wrapper | MCP server | OCI entrypoint | future HTTP API

Layer 2 — Application services
  discover | plan | audit | inspect | compare | report | doctor

Layer 3 — Audit kernel
  request validation
  repository identity
  capability resolution
  plan generation
  execution DAG
  evidence normalization
  evidence graph
  fusion
  finding generation
  prioritization
  comparison

Layer 4 — Analysis providers
  built-in deterministic analyses
  language packs
  external tool adapters
  runtime evidence importers
  semantic/model providers

Layer 5 — Persistence and artifacts
  content-addressed cache
  metadata index
  raw evidence
  audit bundles
  baseline references
  local reports
```

## 2.2 Subsystem inventory

Behavior classes used below:

- **D:** deterministic for identical bytes, configuration, versions, and environment.
- **H:** heuristic but reproducible.
- **R:** runtime-observed and workload-dependent.
- **A:** AI-assisted and potentially non-reproducible.

### Control-plane and repository subsystems

| Subsystem | Responsibility and contracts | Inputs → outputs | Behavior | Initial placement and failure behavior |
|---|---|---|---|---|
| Repository identity | Establish exact audit subject | Root, Git state, files → repository identity and content manifest | D | **MVP.** Refuse unsafe roots; represent dirty state exactly |
| Scope resolver | Include/exclude authored, generated, vendor, test, migration, and sensitive content | Request + config + discovery → scope manifest | D | **MVP.** Ambiguity becomes limitation; unsafe paths excluded |
| Discovery | Detect languages, manifests, frameworks, build systems, entry points, test tools, generated code | Scoped repository → discovery observations | D/H | **MVP.** Unknown language degrades gracefully |
| Capability resolver | Determine analyses applicable to discovered project | Discovery + adapter catalog + tier → capability set | D | **MVP.** Required unavailable capability produces partial/refusal |
| Audit planner | Produce immutable task DAG and budgets | Request + capabilities + policies → audit plan | D | **MVP.** Plan validation must complete before execution |
| Execution scheduler | Run tasks subject to dependencies and resources | Plan → task outcomes and raw evidence | D execution order where possible | **MVP.** Independent tasks continue after isolated failure |
| Sandbox broker | Select local, copied-workspace, OS sandbox, or OCI boundary | Task access contract → execution environment | D | **MVP basic; production hardened later.** Refuse unmet sandbox requirement |
| Configuration loader | Merge defaults, user, project, request, and CLI constraints | Config sources → effective config | D | **MVP.** Lower-precedence config cannot widen protected rights |
| Cache manager | Content-addressed result reuse | Inputs/tool/config/environment digests → cached evidence | D | **MVP.** Corrupt entry quarantined; audit continues uncached |
| Artifact store | Write bundle, reports, and raw evidence | Audit outputs → immutable artifact tree | D | **MVP local; object store later.** Atomic finalize or incomplete marker |
| Adapter registry | Load explicitly trusted adapter manifests | Built-in/user/project catalogs → adapter catalog | D | **MVP.** No filesystem scanning for arbitrary executable plugins |
| Provenance recorder | Bind subjects, tools, materials, config, and results | Whole audit → provenance graph | D | **MVP.** Missing required identity prevents “complete” status |

### Analysis subsystems

| Subsystem | Responsibility | Inputs → outputs | Behavior | Initial or later |
|---|---|---|---|---|
| Static structural analysis | Size, nesting, complexity, parameters, direct code smells | AST/native reports → metric observations | D/H | **Useful v1.** Tree-sitter baseline; native tools preferred |
| Repository-history analysis | Churn, ownership, reverts, co-change, migration age | Git graph → historical observations | D/H | **MVP/basic**, expanded in periodic |
| Dependency graph | File, module, package, symbol, and service relationships | Language/native indexes → graph evidence | D/H | **MVP file/module**, symbol depth later |
| Architecture analysis | Cycles, boundary rules, centrality, communities, drift | Dependency graph + declared rules → architecture observations | D/H | **Useful v1** |
| Duplication analysis | Exact, normalized, near, and semantic duplication | Files/AST/symbols → clone groups | D/H/A | Exact in **MVP**; near in periodic; semantic later |
| Reachability/dead code | Candidate unreachable symbols, files, dependencies, flags | Entry roots + graph + tool reports → candidates | H | **Useful v1 via adapters**; never deletion authority |
| Dependency/supply chain | Inventory, vulnerability, support, overlap, weight | Manifests/SBOM/scanners → dependency evidence | D/H | **Useful v1 through adapters** |
| Test-quality analysis | Coverage, mutation strength, flakiness, test cost, failure-path gaps | Test reports/tool outputs → test observations | D/R/H | Coverage ingestion in **v1**; mutation periodic |
| Runtime/performance ingestion | CPU, allocation, memory, I/O, query, trace, contention evidence | Profile/trace formats → runtime observations | R | **Investigative phase** |
| Security evidence ingestion | SAST, taint, secrets, configuration, trust-boundary findings | SARIF/JSON/tool outputs → security observations | D/H | **Useful v1 through adapters** |
| State/data-flow analysis | State ownership, mutation, shared state, transformations | Typed/data-flow graphs → state observations | H | Basic candidates later; deep data flow delegated |
| Semantic analysis | Conceptual similarity and intent-level interpretation | Bounded context + model → semantic observations | A | **Post-production-v1 opt-in** |
| Simplification analysis | Deletion, dependency reduction, concept merge, layer collapse | Fused evidence → simplification candidates | H/A | Basic rule-driven in periodic; semantic later |
| Hotspot analysis | Combine complexity, churn, defects, coupling, test weakness | Normalized signals → hotspot ranking | H but reproducible | **MVP/basic** |
| Audit comparison | New, recurring, resolved, changed, stale, incompatible findings | Two bundles → comparison | D/H | **MVP** |

### Evidence and decision-support subsystems

| Subsystem | Responsibility | Inputs → outputs | Behavior | Initial or later |
|---|---|---|---|---|
| Raw evidence capture | Preserve or hash exact analyzer output | Tool streams/files → raw evidence refs | D | **MVP** |
| Normalization | Translate heterogeneous formats into UCA observations | Raw evidence → observation envelopes | D | **MVP** |
| Evidence graph | Connect observations, entities, tools, scopes, and findings | Normalized observations → evidence graph | D | **MVP** |
| Evidence fusion | Combine independent supporting or conflicting signals | Evidence graph + fusion rules → candidate interpretations | H | **MVP rule-based** |
| Finding generator | Create stable, deduplicated findings | Candidates + taxonomy → findings | D/H | **MVP** |
| Confidence evaluator | Represent strength, coverage, freshness, reproducibility | Evidence and limitations → confidence vector | H, transparent | **MVP** |
| Prioritization | Estimate benefit, confidence, cost, and risk | Finding + project policy → priority band | H, transparent | **Useful v1** |
| Reporting | JSON, JSONL, SARIF, Markdown, HTML | Bundle → projections | D | JSON/Markdown in MVP; HTML later |
| Trending | Dimension and finding evolution | Audit series → trend observations | D/H | **Periodic/hosted later** |
| Taxonomy registry | Stable finding and observation identifiers | Versioned taxonomy → validation and labels | D | **MVP** |
| Waiver evaluator | Apply scoped, expiring suppressions | Finding + waiver records → disposition | D | **Useful v1** |

### Interface and distribution subsystems

| Subsystem | Responsibility | Initial or later |
|---|---|---|
| CLI | Canonical local and automation interface | **MVP** |
| GitHub Action | Install/verify/invoke CLI and publish projections | Post-useful-v1 |
| Generic CI examples | Shell/container invocation patterns | Useful v1 |
| MCP server | Read-only tools/resources over engine | After production v1 |
| OCI distribution | Reproducible constrained execution | Production v1 |
| Optional HTTP service | Remote request/queue/result projection | Eventual |
| Octon provider package | Govern external provider invocation and evidence reference | Production-v1 integration |
| Adapter SDK | Schemas, fixtures, conformance harness | Useful v1 |
| Language-pack SDK | Detection and normalization contracts | Useful v1 |

## 2.3 Major data flow

```text
AuditRequest
     │
     ▼
Request validation ───── invalid ─────► Refusal completion
     │
     ▼
RepositoryIdentity + ScopeManifest
     │
     ▼
DiscoveryManifest
     │
     ▼
Capability resolution
     │
     ▼
AuditPlan DAG + PlanDigest
     │
     ▼
Execution scheduler
     │
     ├── built-in analysis
     ├── language packs
     ├── external adapters
     └── imported evidence
     │
     ▼
RawEvidence + AnalyzerRun records
     │
     ▼
NormalizedObservations
     │
     ▼
EvidenceGraph
     │
     ├── supporting evidence
     ├── conflicting evidence
     ├── missing evidence
     └── scope/coverage evidence
     │
     ▼
Candidate findings
     │
     ▼
Deduplication + stable fingerprints
     │
     ▼
Confidence + consequence + recommendation + priority
     │
     ▼
UCA Audit Bundle
     │
     ├── JSON/JSONL
     ├── SARIF projection
     ├── Markdown/HTML
     ├── SBOM/profile references
     └── comparison with baseline
```

---

# 3. Canonical audit engine

## 3.1 Single authoritative engine

All interfaces should call the same Rust application service:

```rust
pub trait AuditEngine {
    fn discover(
        &self,
        request: DiscoverRequest,
    ) -> Result<DiscoveryBundle, EngineError>;

    fn plan(
        &self,
        request: AuditRequest,
    ) -> Result<AuditPlan, EngineError>;

    async fn execute(
        &self,
        plan: AuditPlan,
        cancellation: CancellationToken,
    ) -> Result<AuditCompletion, EngineError>;

    fn compare(
        &self,
        request: CompareRequest,
    ) -> Result<AuditComparison, EngineError>;

    fn report(
        &self,
        request: ReportRequest,
    ) -> Result<ReportSet, EngineError>;
}
```

The CLI, MCP server, and future HTTP server may provide their own protocol decoding, authentication, and presentation, but not their own discovery, planning, analysis selection, fusion, or finding logic.

## 3.2 Audit request

An audit request describes the desired analysis, not permission to perform unrelated effects.

```json
{
  "schema_version": "uca.audit-request.v1",
  "request_id": "REQ-01J6D2Y4T8Q7JZ0KMW6N2X6N3A",
  "subject": {
    "repository_root": "/workspace",
    "revision_mode": "working_tree",
    "expected_repository_id": null
  },
  "tier": "continuous",
  "scope": {
    "include": ["src/**", "tests/**"],
    "exclude": ["vendor/**", "dist/**"],
    "changed_against": "origin/main",
    "generated_code": "analyze_separately",
    "vendor_code": "exclude"
  },
  "capabilities": {
    "required": [
      "repository.discovery",
      "history.hotspots",
      "dependency.cycles"
    ],
    "optional": [
      "security.sast",
      "dependency.vulnerabilities"
    ],
    "disabled": ["semantic.ai"]
  },
  "execution": {
    "project_code": "denied",
    "network": "denied",
    "sandbox_minimum": "local_read_only",
    "maximum_parallel_tasks": 4
  },
  "budgets": {
    "wall_seconds": 120,
    "cpu_seconds": 300,
    "memory_mib": 2048,
    "raw_output_mib": 256
  },
  "baseline": {
    "bundle": null,
    "policy": "new_findings_only"
  },
  "output": {
    "bundle_path": "/out/audit",
    "raw_evidence": "local_only",
    "sarif": true,
    "markdown": true
  }
}
```

## 3.3 Audit planning

Planning must be deterministic from:

```text
request
+ repository identity
+ discovery manifest
+ effective configuration
+ adapter catalog
+ tool availability
+ tier policy
+ execution policy
+ resource budget
```

The plan is a DAG whose task records include:

- Task ID.
- Capability ID.
- Analyzer or adapter ID.
- Exact adapter version.
- Exact underlying tool identity and version.
- Input scope.
- Dependency tasks.
- Cache key material.
- Direct argv.
- Environment allowlist.
- Repository access.
- Output directories.
- Network requirements.
- Project-execution requirements.
- Sandbox requirement.
- CPU, memory, process, output, and time limits.
- Required or optional status.
- Failure continuation policy.
- Normalizer ID and version.
- Expected output schemas.

Illustrative task:

```json
{
  "task_id": "ATK-0007",
  "capability": "security.sast",
  "adapter": {
    "id": "semgrep",
    "version": "1.1.0",
    "tool_version": "1.136.0"
  },
  "depends_on": ["ATK-0001"],
  "scope_ref": "SCP-93e1...",
  "execution": {
    "argv": [
      "/opt/semgrep/bin/semgrep",
      "scan",
      "--config",
      "/policy/semgrep.yml",
      "--sarif",
      "--output",
      "/task-out/results.sarif",
      "/workspace"
    ],
    "shell": false,
    "network": "denied",
    "repository": "read_only",
    "project_execution": false,
    "sandbox": "oci_read_only"
  },
  "budget": {
    "wall_seconds": 90,
    "memory_mib": 1536,
    "output_mib": 100
  },
  "required": false,
  "cache_key": "sha256:..."
}
```

## 3.4 Analyzer selection

Analyzer selection follows this order:

```text
1. What capabilities does the requested tier require?
2. What languages, frameworks, and project systems were detected?
3. Which installed and trusted adapters claim those capabilities?
4. Which adapters satisfy the exact version policy?
5. Which can run within the declared access and sandbox constraints?
6. Which fit the remaining resource budget?
7. Which evidence can be safely reused?
8. Which optional capability provides the greatest expected evidence value?
```

Selection must not depend on network-time discovery or unordered filesystem enumeration.

## 3.5 Execution lifecycle

```text
received
   ↓
validated
   ↓
identified
   ↓
planned
   ↓
executing
   ├── succeeded
   ├── failed
   ├── unavailable
   ├── skipped
   ├── timed_out
   └── cancelled
   ↓
normalizing
   ↓
fusing
   ↓
reporting
   ↓
complete
complete_with_limitations
partial
failed
cancelled
```

Task failure does not automatically fail the entire audit. The planner determines whether a capability is:

- Required.
- Required only for a complete result.
- Optional.
- Advisory.
- A fallback provider.

For example:

- Repository identity failure: audit fails.
- Optional Semgrep unavailable: audit may complete with limitations.
- Required architecture rule engine failure: audit becomes partial or fails policy.
- AI provider unavailable: deterministic audit may still complete normally if AI was optional.

## 3.6 Reproducibility

A reproducible audit requires exact identities for:

- Repository content.
- Working-tree overlay.
- Scope.
- Configuration.
- UCA product.
- Schema set.
- Taxonomy.
- Adapter.
- Tool.
- Tool rules or queries.
- Environment factors declared material by the adapter.
- Audit plan.
- Normalizer.
- Fusion rules.
- Priority policy.

Use two identities:

```text
audit_run_id      operational identity; time-sortable and unique
audit_content_id  SHA-256 over canonical subject, plan, config, and output identities
```

Use the JSON Canonicalization Scheme for hash-bearing JSON documents.

## 3.7 UCA-owned versus delegated analysis

### Build directly in UCA

- Repository identity and scope.
- Discovery.
- Git-history mining.
- File/module dependency graph primitives.
- Exact duplicate detection.
- Basic syntax metrics where parsers are available.
- Graph algorithms.
- Hotspot combinations.
- Evidence normalization.
- Fusion.
- Finding identity.
- Priority calculation.
- Comparison.
- Bundle and report generation.

### Delegate through adapters

- Deep interprocedural static analysis.
- Taint analysis.
- Compiler and type-system diagnostics.
- Vulnerability databases.
- SBOM generation.
- Mutation testing.
- Runtime profiling.
- Race detection.
- Fuzzing.
- Framework-specific architecture analysis.
- Database execution-plan analysis.
- Hosted code intelligence.
- Semantic models.

---

# 4. Audit modes and tiers

## 4.1 Executable tiers

| Attribute | Continuous | Periodic | Investigative |
|---|---|---|---|
| Primary use | Local change and pull request | Scheduled repository health review | Evidence-triggered deep investigation |
| Scope | Changed and affected code | Full repository or major subsystem | Explicit hypothesis or hotspot |
| Default network | Denied | Denied; selectively allowed by policy | Explicit per provider |
| Project execution | Denied unless a selected check requires it | Selectively permitted | Explicit and scoped |
| Default wall budget | 120 seconds | 30 minutes | Explicit request; no silent default |
| Hard reference ceiling | 5 minutes | 60 minutes | Request-specific |
| Cache expectation | High | Moderate/high | Evidence-specific |
| Finding volume target | Very low | Ranked and bounded | Focused |
| Blocking eligibility | Deterministic configured regressions | Normally advisory | Advisory unless validating explicit budget |
| AI | Off | Optional, off by default | Explicit opt-in |
| Runtime profiling | Import only | Import or scheduled benchmark | Full orchestration |
| Mutation testing | Rare/changed targets only | Sampled or hotspot-focused | Targeted deep run |
| Architecture analysis | Incremental rules and new cycles | Full graph, drift, communities | Focused redesign analysis |
| History | Change-window only | Full configured history window | Targeted lineage |
| Output | Bundle + SARIF + summary | Full bundle + reports | Investigation bundle |

Runtime values are reference performance budgets to validate on a published benchmark corpus, not universal promises.

## 4.2 Continuous audit contents

Default continuous capability set:

- Repository identity.
- Scope validation.
- Changed-file discovery.
- Compile/type/lint result ingestion where already available.
- Changed-function complexity.
- New exact clones.
- New unreachable or unused local code.
- Architecture rules.
- New module cycles.
- Public API diff.
- Secret findings.
- High-confidence SAST findings.
- Dependency-manifest delta.
- Changed-code coverage evidence.
- New flaky-test evidence.
- Explicit performance budgets for affected paths.
- Baseline comparison.

Continuous mode should block only when the project explicitly configured a deterministic gate such as:

```text
new verified secret
new forbidden dependency
new cross-boundary cycle
new compiler/type failure
new reachable critical vulnerability under declared policy
new flaky test
benchmark regression beyond accepted noise
required audit capability unavailable
```

## 4.3 Periodic audit contents

Periodic mode adds:

- Full complexity and size distribution.
- Complexity × churn.
- Defect and revert concentration.
- Temporal coupling.
- Ownership concentration.
- Full module graph and strongly connected components.
- Centrality and bridge analysis.
- Architecture reflexion.
- Near-duplicate detection.
- Dead-code candidates.
- Unused exports and dependencies.
- Feature-flag age.
- Migration completion.
- Dependency support and lifecycle.
- Full SBOM and vulnerability review.
- Mutation sampling.
- Test duration and flake analysis.
- Build critical-path analysis.
- Documentation and terminology drift.
- De-abstraction candidates.
- Concept-count and configuration-reduction opportunities.

## 4.4 Investigative audit contents

Investigative audits are created from explicit evidence-triggered hypotheses:

```text
Finding: module is a high-churn central bottleneck
  → investigate architecture decomposition

Finding: latency regression on checkout
  → collect trace, CPU, allocation, query, and lock evidence

Finding: low mutation score in high-risk path
  → run targeted mutation + property-based testing

Finding: suspected semantic duplication
  → run bounded semantic comparison

Finding: cancellation-related incidents
  → run scheduler stress and fault injection
```

An investigative request must identify:

- Triggering finding or hypothesis.
- Exact subject.
- Required analyses.
- Workload or test scenario.
- Resource budget.
- Execution rights.
- Network rights.
- Success and stop conditions.
- Expected validation method.

## 4.5 Escalation rules

Tier escalation is a recommendation, not automatic execution:

```json
{
  "escalation": {
    "from": "continuous",
    "recommended_tier": "investigative",
    "reason": "Performance regression is confirmed but no causal profile exists.",
    "triggering_findings": ["FND-7J9..."],
    "required_capabilities": [
      "runtime.cpu_profile",
      "runtime.allocation_profile"
    ],
    "estimated_cost_class": "medium",
    "requires_project_execution": true
  }
}
```

---

# 5. Evidence model and UCA Audit Bundle

## 5.1 Evidence-model principles

1. Evidence is immutable once finalized.
2. Raw evidence and normalized observations are separate.
3. Normalization never discards the original tool identity.
4. Absence of evidence is explicitly represented.
5. Scope coverage is evidence.
6. Analyzer failure is evidence.
7. A parser’s blind spots are evidence.
8. Reused evidence records its original production time and reuse basis.
9. A finding references observations; it does not copy them as if newly observed.
10. Semantic interpretation cannot masquerade as direct observation.
11. Evidence sensitivity and retention are declared.
12. Every significant artifact has a SHA-256 digest.

JSON Schema draft 2020-12 should define the UCA contract family.

## 5.2 Contract family

| Contract | Schema identity | Purpose |
|---|---|---|
| Audit request | `uca.audit-request.v1` | Requested tier, scope, rights, capabilities, and budgets |
| Audit plan | `uca.audit-plan.v1` | Immutable execution DAG |
| Audit manifest | `uca.audit-manifest.v1` | Bundle index and top-level identity |
| Repository identity | `uca.repository-identity.v1` | Commit, worktree overlay, archive, or filesystem subject |
| Scope | `uca.scope.v1` | Included, excluded, sensitive, generated, and vendor paths |
| Discovery | `uca.discovery.v1` | Languages, frameworks, manifests, tools, entry points |
| Analyzer identity | `uca.analyzer.v1` | Adapter, tool, query/rule set, configuration |
| Analyzer run | `uca.analyzer-run.v1` | Execution outcome, timings, resource use, output refs |
| Raw evidence ref | `uca.raw-evidence-ref.v1` | Exact bytes, digest, media type, sensitivity |
| Observation | `uca.observation.v1` | Canonical normalized evidence envelope |
| Metric observation | `uca.metric-observation.v1` | Numeric or ordinal measurement |
| Graph evidence | `uca.graph.v1` | Nodes, edges, extraction method, confidence |
| Historical evidence | `uca.history-observation.v1` | Churn, co-change, ownership, reverts |
| Runtime evidence | `uca.runtime-observation.v1` | Profiles, traces, queries, allocations |
| Semantic evidence | `uca.semantic-observation.v1` | AI or human-assisted interpretation |
| Finding | `uca.finding.v1` | Decision-oriented issue or investigation lead |
| Waiver | `uca.waiver.v1` | Scoped, owned, expiring disposition |
| Completion | `uca.audit-completion.v1` | Complete, partial, failed, cancelled |
| Comparison | `uca.audit-comparison.v1` | New, recurring, changed, resolved, incompatible |
| Provenance | `uca.provenance.v1` | Subjects, materials, producers, transformations |
| Taxonomy | `uca.taxonomy.v1` | Stable observation and finding identifiers |

## 5.3 Observation envelope

Every normalized observation uses one envelope:

```json
{
  "schema_version": "uca.observation.v1",
  "observation_id": "OBS-01J6D4N9R2...",
  "observation_type": "metric",
  "evidence_class": "historical",
  "producer": {
    "kind": "uca_builtin",
    "id": "history-hotspots",
    "version": "0.4.0"
  },
  "subject": {
    "repository_id": "sha256:...",
    "entity_id": "file:src/pricing/rules.rs"
  },
  "scope_ref": "SCP-...",
  "observed_at": "2026-08-27T12:00:00Z",
  "valid_for_revision": "sha256:...",
  "payload": {
    "metric": "change_frequency",
    "value": 47,
    "unit": "commits",
    "window": "P365D",
    "repository_percentile": 0.97
  },
  "raw_evidence_refs": ["RAW-..."],
  "assumptions": [],
  "limitations": [
    "Formatting-only commits were excluded using configured heuristics."
  ],
  "confidence": {
    "evidence_strength": "strong",
    "scope_coverage": "complete",
    "reproducibility": "deterministic",
    "freshness": "current"
  }
}
```

## 5.4 Evidence classes

```text
deterministic_static
deterministic_contract
external_tool_deterministic
heuristic_static
historical
runtime_observed
imported_human
ai_interpretation
derived_fusion
absence_or_unavailability
```

An evidence class does not itself determine severity. A runtime sample may be highly concrete but cover only one workload. A deterministic static finding may be complete for syntax but blind to dynamic dispatch.

## 5.5 Confidence vector

Do not reduce confidence immediately to one probability. Preserve:

```json
{
  "evidence_strength": "confirmed",
  "detector_precision": "high",
  "scope_coverage": {
    "status": "partial",
    "estimated_fraction": 0.82,
    "basis": "82 of 100 declared modules successfully analyzed"
  },
  "freshness": {
    "status": "current",
    "valid_for_revision": "sha256:..."
  },
  "reproducibility": "deterministic",
  "inference_distance": 1,
  "independent_sources": 3,
  "conflicts": 0
}
```

Allowed ordinal values:

```text
evidence_strength: speculative | indicated | strong | confirmed
detector_precision: unknown | low | medium | high
scope_coverage: unknown | partial | complete
freshness: current | stale | incompatible | unknown
reproducibility: deterministic | environment_dependent | workload_dependent | model_dependent
```

## 5.6 Canonical UCA Audit Bundle

Canonical directory form:

```text
uca-audit/
├── manifest.json
├── request.json
├── plan.json
├── completion.json
├── repository.json
├── scope.json
├── discovery.json
├── analyzers.json
├── findings.jsonl
├── waivers-applied.jsonl
├── observations/
│   ├── metrics.jsonl
│   ├── history.jsonl
│   ├── security.jsonl
│   ├── dependencies.jsonl
│   ├── tests.jsonl
│   ├── runtime.jsonl
│   └── semantic.jsonl
├── graphs/
│   ├── module-graph.json.zst
│   ├── symbol-graph.json.zst
│   ├── cochange-graph.json.zst
│   └── evidence-graph.json.zst
├── raw/
│   ├── semgrep/ANR-.../results.sarif
│   ├── osv/ANR-.../results.json
│   ├── compiler/ANR-.../diagnostics.jsonl
│   └── profiles/ANR-.../profile.pb
├── interoperability/
│   ├── results.sarif
│   ├── sbom.cdx.json
│   ├── sbom.spdx.json
│   └── coverage/
├── comparison/
│   └── baseline-comparison.json
├── reports/
│   ├── summary.json
│   ├── summary.md
│   └── report.html
├── provenance/
│   ├── subjects.json
│   ├── materials.json
│   └── attestations/
└── checksums.sha256
```

Canonical storage is a directory. Distribution may use:

```text
uca-audit-<content-id>.tar.zst
```

The archive is transport, not identity. The manifest and checksums identify the content.

## 5.7 Manifest

```json
{
  "schema_version": "uca.audit-manifest.v1",
  "product": {
    "name": "Universal Code Audit",
    "version": "1.0.0"
  },
  "audit_run_id": "AUD-...",
  "audit_content_id": "sha256:...",
  "tier": "periodic",
  "repository_ref": "repository.json",
  "scope_ref": "scope.json",
  "request_ref": "request.json",
  "plan_ref": "plan.json",
  "completion_ref": "completion.json",
  "finding_count": 38,
  "observation_count": 9104,
  "bundle_files": [
    {
      "path": "findings.jsonl",
      "media_type": "application/x-ndjson",
      "sha256": "...",
      "sensitivity": "project_confidential"
    }
  ],
  "limitations": [
    "Java reflection call edges were not resolved.",
    "Runtime evidence was not requested."
  ]
}
```

## 5.8 Interoperability

### SARIF

Use SARIF as a **projection** for findings with meaningful source locations, rule identities, severity, and code flows. Do not force repository-level hotspots, graph communities, architecture drift, conceptual duplication, or simplification proposals into SARIF.

### CycloneDX and SPDX

Treat SBOMs as imported evidence artifacts:

- Retain original CycloneDX or SPDX file.
- Validate its schema.
- Record producer and completeness.
- Normalize component and dependency observations.
- Never rewrite the original as the sole source of truth.

### OpenTelemetry and profiles

Use OpenTelemetry traces and metrics as runtime evidence sources. Support pprof-compatible profiles as an initial common sampled-stack format, retaining workload, time range, labels, and collection method.

### Tool-native formats

Retain native output where useful:

- CodeQL SARIF.
- Semgrep SARIF or JSON.
- OSV JSON/SARIF.
- Syft native JSON plus standardized SBOM.
- Coverage XML/JSON/LCOV.
- Mutation result formats.
- Compiler JSON diagnostics.
- Test result formats.
- pprof profile protobuf.
- Query plans.

---

# 6. Finding and prioritization model

## 6.1 Finding contract

```json
{
  "schema_version": "uca.finding.v1",
  "finding_id": "FND-01J6D5...",
  "stable_fingerprint": "sha256:...",
  "taxonomy_id": "UCA.ARCH.BOUNDARY_BYPASS",
  "taxonomy_version": "1.0.0",
  "title": "Checkout bypasses the customer-policy boundary",
  "finding_class": "architectural",
  "evidence_posture": "strongly_indicated",
  "lifecycle": {
    "status": "recurring",
    "first_seen_audit": "AUD-...",
    "last_seen_audit": "AUD-...",
    "occurrences": 4
  },
  "scope": {
    "entities": [
      "module:checkout",
      "module:customer-policy"
    ],
    "locations": [
      {
        "path": "src/checkout/pricing.rs",
        "start_line": 71,
        "end_line": 83
      }
    ]
  },
  "finding": "Checkout reads customer discount storage directly.",
  "evidence_refs": [
    "OBS-architecture-edge-...",
    "OBS-cochange-...",
    "OBS-defect-history-..."
  ],
  "interpretation": "The policy API is not containing change.",
  "consequences": [
    {
      "dimension": "changeability",
      "description": "Policy changes repeatedly require coordinated edits."
    },
    {
      "dimension": "correctness",
      "description": "Two prior fixes changed only one path."
    }
  ],
  "recommendations": [
    {
      "kind": "architectural_change",
      "description": "Route discount eligibility through the customer-policy API.",
      "alternatives": [
        "Move the rule into a shared immutable policy library."
      ]
    }
  ],
  "expected_benefits": [
    "One authoritative discount rule",
    "Smaller checkout change surface"
  ],
  "confidence": {
    "evidence_strength": "strong",
    "scope_coverage": "complete",
    "reproducibility": "deterministic",
    "independent_sources": 3
  },
  "change_risk": {
    "level": "medium",
    "reasons": [
      "Historical discount behavior requires compatibility testing."
    ]
  },
  "validation_strategy": [
    "Differential test historical cases",
    "Enforce the new dependency rule",
    "Compare checkout latency"
  ],
  "priority": {
    "band": "P1",
    "policy_version": "uca.priority.v1",
    "inputs": {
      "impact": 4,
      "breadth": 3,
      "recurrence": 4,
      "strategic_leverage": 3,
      "evidence_confidence": 0.75,
      "effort": 3,
      "migration_risk": 3,
      "regression_risk": 3
    }
  },
  "suppressibility": {
    "allowed": true,
    "requires_owner": true,
    "requires_reason": true,
    "requires_expiry": true
  },
  "provenance": {
    "generated_by": "uca-finding-engine@1.0.0",
    "fusion_rule": "architecture-boundary-change-amplification@1"
  }
}
```

## 6.2 Distinguishing observation, interpretation, and recommendation

UCA must preserve:

```text
Observation:
  checkout imports customer_policy_storage

Interpretation:
  checkout may be bypassing an intended boundary

Finding:
  current implementation violates declared rule ARCH-012

Consequence:
  discount changes have a broad and defect-prone change surface

Recommendation:
  route access through the customer-policy API

Decision:
  outside UCA; the project may accept, reject, defer, or investigate
```

## 6.3 Finding classes

```text
deterministic_violation
deterministic_regression
heuristic_candidate
runtime_confirmed
historical_hotspot
semantic_interpretation
investigation_required
evidence_gap
tool_or_scope_limitation
simplification_opportunity
```

## 6.4 Stable fingerprint

A fingerprint should use:

```text
taxonomy ID
+ normalized entity identity
+ normalized primary location or symbol identity
+ normalized relevant edge/rule identity
+ material evidence signature
```

It should generally exclude:

- Current line number alone.
- Message wording.
- Timestamp.
- Audit run ID.
- Priority.
- Recommendation prose.

Fallback levels:

1. Language-native stable symbol ID.
2. File plus syntax-path fingerprint.
3. File plus contextual token hash.
4. Path plus line range.

Fingerprint quality is reported.

## 6.5 Conflicting and incomplete evidence

Do not average conflicts away.

```json
{
  "conflict_id": "CNF-...",
  "subject": "symbol:parse_order",
  "supporting_observations": ["OBS-1", "OBS-2"],
  "contradicting_observations": ["OBS-3"],
  "interpretation": "Static reachability says unused, but runtime trace observed execution.",
  "resolution": "runtime_observation_overrides_dead_code_candidate",
  "finding_disposition": "not_dead",
  "limitations": [
    "Runtime trace covers one workload only."
  ]
}
```

Possible outcomes:

- Evidence confirms.
- Evidence weakens.
- Evidence conflicts.
- Evidence is stale.
- Evidence is inapplicable.
- More investigation is required.
- Candidate is invalidated.

## 6.6 Finding lifecycle

```text
new
 ├── recurring
 ├── changed
 ├── needs_investigation
 ├── accepted_debt
 ├── suppressed
 ├── resolved
 └── invalidated
```

A resolved finding remains in comparison history. A suppression never removes the underlying finding from the bundle.

## 6.7 Waivers and accepted debt

```json
{
  "schema_version": "uca.waiver.v1",
  "waiver_id": "WVR-0042",
  "finding_fingerprint": "sha256:...",
  "scope": ["module:legacy-payments"],
  "disposition": "accepted_debt",
  "owner": "payments-platform",
  "reason": "Removal depends on partner API retirement.",
  "created_at": "2026-08-27",
  "expires_at": "2026-11-30",
  "review_trigger": [
    "partner_api_version_change",
    "security_finding_added"
  ]
}
```

## 6.8 Transparent prioritization

Use a transparent, versioned policy:

\[
ExpectedBenefit =
Impact \times Breadth \times Recurrence \times
(1 + 0.25 \times StrategicLeverage)
\]

\[
DeliveryBurden =
Effort \times
(1 +
0.25MigrationRisk +
0.25RegressionRisk +
0.15CoordinationCost +
0.15RolloutComplexity)
\]

\[
PriorityIndex =
\frac{ExpectedBenefit \times EvidenceConfidence}
{DeliveryBurden}
\]

This index is used only to suggest a band:

```text
P0  active security, data-loss, correctness, or outage risk
P1  confirmed broad or recurring risk
P2  strong evidence suitable for planned work
P3  opportunistic improvement during adjacent work
INVESTIGATE  material hypothesis with insufficient evidence
ACCEPTED     explicitly dispositioned debt
```

Safeguards:

- Preserve every input.
- Version the formula.
- Do not calculate a remediation priority when required consequence inputs are unknown.
- AI confidence cannot supply evidence confidence by itself.
- A failed safety gate cannot be offset by a low effort estimate.
- No repository-wide aggregate score.
- Ranking is per policy and context, not universal truth.

---

# 7. External analyzer and adapter architecture

## 7.1 Process boundary

Adapters are out-of-process executables or OCI artifacts.

Do not support arbitrary dynamic libraries in the core process.

```text
UCA engine
  │
  ├── reads signed/static adapter manifest
  ├── validates capability and trust policy
  ├── creates task-specific request
  ├── starts adapter without shell
  ├── constrains environment/resources
  ├── receives raw output
  ├── validates output schema
  └── normalizes through versioned mapper
```

This allows adapters to be implemented in Rust, Python, Go, Node.js, Java, or another language without compromising UCA’s engine stability.

## 7.2 Adapter manifest

```json
{
  "schema_version": "uca.adapter-manifest.v1",
  "id": "osv-scanner",
  "adapter_version": "1.2.0",
  "protocol": {
    "name": "uca.adapter",
    "minimum": "1.0.0",
    "maximum": "1.x"
  },
  "implementation": {
    "kind": "local_process",
    "executable": "uca-adapter-osv",
    "sha256": "..."
  },
  "underlying_tool": {
    "name": "osv-scanner",
    "version_constraint": ">=2.0.0 <3.0.0",
    "identity_probe": ["osv-scanner", "--version"]
  },
  "capabilities": [
    "dependency.vulnerabilities",
    "dependency.call_analysis"
  ],
  "languages": ["*"],
  "inputs": [
    "repository.manifests",
    "sbom.cyclonedx",
    "sbom.spdx"
  ],
  "outputs": [
    "uca.observation.v1",
    "uca.raw-evidence-ref.v1"
  ],
  "access": {
    "repository": "read_only",
    "network": "optional_declared",
    "project_execution": false,
    "filesystem_writes": ["task_output", "task_temp"]
  },
  "resource_class": "cpu_medium",
  "default_limits": {
    "wall_seconds": 300,
    "memory_mib": 2048,
    "output_mib": 200
  },
  "cache": {
    "safe": true,
    "key_inputs": [
      "repository_manifest",
      "tool_version",
      "advisory_database_identity",
      "adapter_config"
    ]
  },
  "limitations": [
    "Call analysis depth varies by supported ecosystem."
  ]
}
```

## 7.3 Adapter protocol

Static discovery reads the manifest without executing the adapter.

Runtime commands:

```text
uca-adapter-<id> describe
uca-adapter-<id> probe  --request <probe.json> --output <result.json>
uca-adapter-<id> run    --request <run.json>   --output-dir <dir>
```

All output files are declared in `result.json`.

The engine passes direct argv and a sanitized environment. No shell expansion is allowed.

## 7.4 Adapter lifecycle

```text
unregistered
  → registered_untrusted
  → trusted_disabled
  → enabled
  → deprecated
  → removed
```

Trust is separate from availability:

```text
trusted + missing tool      = unavailable
installed + untrusted       = prohibited
trusted + wrong version     = incompatible
trusted + capability absent = unsupported
```

## 7.5 Tool behavior

For every adapter:

1. Validate manifest.
2. Verify adapter digest.
3. Probe underlying tool.
4. Verify version.
5. Validate required configuration.
6. Determine whether network is needed.
7. Determine whether repository execution is needed.
8. Select sandbox.
9. Start with direct argv.
10. Capture exit code, stdout, and stderr separately.
11. Enforce byte, time, memory, and process limits.
12. Kill the entire process group on cancellation.
13. Validate produced files.
14. Hash raw output.
15. Normalize.
16. Record blind spots and completeness.

## 7.6 Missing or unsupported tooling

UCA should report:

```json
{
  "capability": "test.mutation",
  "status": "unavailable",
  "reason": "No trusted compatible mutation adapter is installed.",
  "required": false,
  "effect_on_audit": "complete_with_limitations",
  "installation_guidance": {
    "kind": "documentation_reference",
    "adapter_id": "cargo-mutants"
  }
}
```

It must not:

- Download a binary.
- Run a package-manager install.
- Accept a repository-provided executable.
- Change a lockfile.
- Enable network access.
- Treat the capability as passed.

## 7.7 Adapter categories

| Adapter category | Examples | UCA role |
|---|---|---|
| Generic result importer | SARIF, CycloneDX, SPDX, coverage, JUnit | Parse and normalize |
| Tool invoker | Semgrep, OSV, Syft, Trivy | Invoke pinned tool and normalize |
| Native language | rustc, clippy, tsc, mypy, Go tools | Select safe native command |
| Test | pytest, cargo test, Jest, Go test | Import or explicitly execute |
| Mutation | PIT, Stryker, cargo-mutants, mutmut | Periodic/investigative |
| Runtime | pprof, perf, heap tools, OTel | Import or orchestrate |
| Race/concurrency | ThreadSanitizer, `go test -race`, loom-like tools | Investigative |
| Fuzz/property | libFuzzer, cargo-fuzz, Hypothesis, QuickCheck tools | Investigative |
| Commercial/API | Sonar, CodeScene, commercial SAST | Import exported result or call under explicit network authority |

## 7.8 Adapter testing

Every stable adapter needs:

- Static manifest validation.
- Mock-tool contract test.
- Golden output fixtures.
- Supported tool-version matrix.
- Invalid-output tests.
- Oversized-output tests.
- Timeout and cancellation tests.
- Exit-code mapping tests.
- Redaction tests.
- Network-denied tests.
- Cache-key tests.
- Cross-platform tests where applicable.
- At least one live compatibility job against the oldest and newest supported tool versions.
- A named maintainer.

## 7.9 Licensing boundary

Adapters may support commercial or restricted tooling without redistributing it. UCA should not bundle proprietary queries, licensed rule packs, vendor credentials, or hosted-service terms. The adapter manifest records the expected external license class and leaves installation and licensing to the operator.

---

# 8. Language and framework agnosticism

## 8.1 Universal versus language-specific capabilities

### Universal UCA capabilities

These can operate across repositories:

- File inventory and content identity.
- Git history.
- Churn and ownership.
- Exact textual duplication.
- Manifest and lockfile discovery.
- Repository structure.
- File-level dependency edges when import syntax is detectable.
- Configuration duplication.
- Artifact and binary inventory.
- External SARIF ingestion.
- SBOM ingestion.
- Coverage and test-result ingestion.
- Audit comparison.
- Evidence fusion and prioritization.

### Language-specific capabilities

These require a language pack or adapter:

- Function and method complexity.
- Symbol identity.
- Type relationships.
- Call graphs.
- Data-flow graphs.
- Unreachable symbols.
- Unused exports.
- Interface quality.
- Nullability and state modeling.
- Precise semantic clones.
- Framework entry points.
- Reflection and dynamic-dispatch handling.
- Compilation and test execution.

## 8.2 Language capability pack

A language pack is declarative plus compiled trusted UCA code or explicit adapters. It is not arbitrary repository code.

```text
language pack
├── detection rules
├── file classifications
├── generated/vendor conventions
├── manifest and lockfile readers
├── tree-sitter grammar binding
├── native tool adapters
├── symbol identity normalizer
├── dependency-edge normalizer
├── metric normalizer
├── framework detectors
├── known blind spots
└── conformance fixtures
```

## 8.3 Internal graph interfaces

UCA should define internal graph models:

```text
FileGraph
ModuleGraph
PackageGraph
SymbolGraph
CallGraph
TypeGraph
DataFlowGraph
CoChangeGraph
OwnershipGraph
EvidenceGraph
```

Every edge includes:

```json
{
  "source": "symbol:a",
  "target": "symbol:b",
  "kind": "calls",
  "producer": "rustc-index-adapter@1.0.0",
  "confidence": "confirmed",
  "resolution": "compiler_semantic",
  "conditional": false
}
```

A Tree-sitter-derived call edge and a compiler-resolved call edge must not be indistinguishable.

## 8.4 Initial language strategy

### Minimum viable architecture

- Language-neutral repository support.
- One statically typed compiled language pack.
- One dynamic language pack.
- Generic SARIF and coverage importers.

Recommended proof pair:

- Rust.
- Python.

### Useful v1

Add:

- JavaScript/TypeScript.
- Go.

These four exercise materially different conditions:

- Strong compiler semantics.
- Dynamic dispatch.
- Package-manager ecosystems.
- Monorepos.
- Native and interpreted tests.
- Different dead-code and graph precision limits.

### Production v1 claim

Do not claim equal depth. Publish a capability matrix:

| Capability | Rust | Python | JS/TS | Go | Generic |
|---|---:|---:|---:|---:|---:|
| Discovery | Full | Full | Full | Full | Basic |
| File metrics | Full | Full | Full | Full | Basic |
| Symbol graph | High | Medium | High with TypeScript | High | None |
| Dead-code candidates | High | Low/medium | Medium | High | None |
| Native diagnostics | Full | Adapter | Full | Full | Imported |
| Coverage ingestion | Full | Full | Full | Full | Imported |
| Mutation | Optional | Optional | Optional | Optional | None |

## 8.5 Framework knowledge

Framework packs may add:

- Entry-point detection.
- Dependency-injection edges.
- Generated-code rules.
- Route and handler roots.
- ORM relationships.
- Lifecycle methods.
- Public API conventions.
- Test and build commands.

Framework knowledge must remain:

- Versioned.
- Explicitly detected.
- Disableable.
- Bounded to the relevant language.
- Separate from core repository identity.

## 8.6 Graceful degradation

A project with an unsupported language can still receive:

- Repository identity.
- File inventory.
- history hotspots.
- ownership concentration.
- exact text duplication.
- dependency/SBOM evidence.
- imported SARIF.
- build and test artifact analysis.
- structure and simplification candidates.

The completion manifest must say precisely what was not available.

---

# 9. Semantic and AI-assisted analysis

## 9.1 Product position

AI analysis is:

> An optional, structured interpretation provider over bounded, cited evidence.

It is not:

- The main audit engine.
- A source of authority.
- A replacement for static or runtime evidence.
- An excuse to send an entire repository to a remote model.
- A tool-capable coding agent.
- A remediation executor.

## 9.2 Initial semantic capabilities

- Semantic duplication.
- Responsibility clustering.
- Conceptual vocabulary.
- Domain-model weaknesses.
- Architecture interpretation.
- Suspected obsolete compatibility code.
- Over-engineering.
- Inappropriate abstraction.
- De-abstraction candidates.
- Stale documentation.
- Terminology inconsistency.
- API usability.
- Recommendation alternatives.

## 9.3 Context construction

Context is generated from an immutable manifest:

```json
{
  "schema_version": "uca.semantic-context.v1",
  "context_id": "CTX-...",
  "purpose": "analyze_semantic_duplication",
  "repository_revision": "sha256:...",
  "inputs": [
    {
      "entity": "symbol:normalize_customer_address",
      "content_ref": "source-range:...",
      "sha256": "...",
      "reason": "member of structural clone candidate group"
    }
  ],
  "excluded": [
    {
      "path": ".env",
      "reason": "sensitive_path"
    }
  ],
  "measured_bytes": 42819,
  "maximum_bytes": 64000,
  "limitations": [
    "Only candidate-related functions were included."
  ]
}
```

Selection should prefer:

- Finding-related entities.
- Relevant dependency neighbors.
- Relevant tests.
- Explicit architecture documents.
- Terminology indexes.
- Existing deterministic evidence.

It should not indiscriminately include the entire repository.

## 9.4 Provider abstraction

```json
{
  "schema_version": "uca.model-provider.v1",
  "id": "local-llama",
  "interface": "local_process",
  "model": "example-model",
  "model_version": "sha256:...",
  "network": "denied",
  "data_retention": "local_only",
  "structured_output_schema": "uca.semantic-observation.v1"
}
```

Supported provider classes:

- Local executable.
- Local model server.
- Remote API.
- Future organization-managed provider.

Remote providers require explicit:

- Network authority.
- Data classification policy.
- Retention declaration.
- Provider identity.
- Secret reference.
- Path and content scope.
- Output-use policy.

## 9.5 Prompt-injection protections

Repository content must be framed as untrusted quoted material.

The semantic analyzer:

- Receives no shell or filesystem mutation tools.
- Receives only the prepared context.
- Cannot expand its own scope.
- Cannot follow links or fetch network content.
- Must produce schema-valid output.
- Must cite evidence IDs for material claims.
- Has uncited claims rejected or marked unsupported.
- Cannot mark its own finding deterministic.
- Cannot suppress a deterministic finding.
- Cannot create a waiver.
- Cannot create a task.

## 9.6 AI evidence record

```json
{
  "schema_version": "uca.semantic-observation.v1",
  "evidence_class": "ai_interpretation",
  "provider": {
    "id": "local-llama",
    "model": "example-model",
    "model_version": "sha256:...",
    "prompt_template_sha256": "...",
    "parameters": {
      "temperature": 0
    }
  },
  "context_manifest_ref": "CTX-...",
  "interpretation": "The two validators appear to encode the same address-normalization rule.",
  "evidence_refs": ["OBS-clone-17", "OBS-cochange-22"],
  "confidence": {
    "self_reported": "high",
    "uca_evidence_strength": "indicated",
    "reproducibility": "model_dependent"
  },
  "human_review": "required"
}
```

Model self-confidence is retained only as metadata. UCA confidence derives from cited evidence, context completeness, provider evaluation history, and corroboration.

## 9.7 CI and authority policy

AI findings:

- Are off by default.
- Are advisory by default.
- Cannot fail a pull request solely because of model output.
- Cannot be auto-converted into code changes.
- Require human review before becoming accepted architecture or simplification work.
- May be promoted when corroborated by deterministic or historical evidence, but the AI contribution remains labeled.

---

# 10. CLI architecture

## 10.1 Command model

```text
uca
├── discover
├── plan
├── audit
├── inspect
│   ├── finding
│   ├── module
│   ├── entity
│   ├── hotspot
│   ├── graph
│   └── bundle
├── explain
├── compare
├── report
├── adapters
│   ├── list
│   ├── describe
│   ├── probe
│   └── doctor
├── cache
│   ├── status
│   ├── verify
│   ├── prune
│   └── gc
├── doctor
├── schema
│   ├── list
│   ├── show
│   ├── validate
│   └── migrate
└── version
```

Later binaries:

```text
uca-mcp
uca-server
```

Do not put server and MCP dependencies in the minimal CLI binary unless their weight remains negligible.

## 10.2 Examples

```bash
uca discover --repo .

uca plan \
  --repo . \
  --tier continuous \
  --output audit-plan.json

uca audit \
  --repo . \
  --tier continuous \
  --baseline ./baseline-audit \
  --bundle-out ./uca-output

uca audit \
  --request audit-request.json \
  --accept-plan-digest sha256:... \
  --progress json

uca inspect hotspot --bundle ./uca-output --top 20

uca explain FND-01J6D5... --bundle ./uca-output

uca compare ./baseline-audit ./uca-output --format json

uca report ./uca-output --format html --output report.html

uca adapters doctor --format json

uca schema validate uca.finding.v1 finding.json
```

## 10.3 Configuration precedence

From highest to lowest:

```text
1. Host-enforced security policy
2. Explicit audit request
3. CLI flags within allowed policy
4. Repository uca.toml
5. User configuration
6. Built-in defaults
```

Security-specific merge rule:

> A lower-precedence source may narrow access or scope, but may not enable network, project execution, external tools, or sensitive paths prohibited by a higher-precedence source.

Environment variables should be limited to:

- Non-secret output formatting.
- Cache location.
- Explicit config path.
- CI metadata.
- Secret references handled by a credential broker.

## 10.4 Output behavior

### stdout

Contains only the requested primary output:

- Human summary.
- Final JSON.
- NDJSON event stream.
- Schema.
- Report.

### stderr

Contains:

- Progress.
- Diagnostics.
- Adapter logs when requested.
- Warnings.
- Refusal explanation.

### Progress modes

```text
--progress auto
--progress human
--progress json
--progress none
```

JSON progress is NDJSON:

```json
{"event":"task_started","task_id":"ATK-0002"}
{"event":"task_completed","task_id":"ATK-0002","status":"succeeded"}
```

## 10.5 Exit codes

| Code | Meaning |
|---:|---|
| 0 | Audit completed and configured gates passed |
| 10 | Audit completed, but a configured policy gate failed |
| 20 | Audit completed partially beyond allowed incompleteness |
| 30 | Invalid request, configuration, schema, or arguments |
| 40 | Required analyzer, tool, language capability, or environment unavailable |
| 50 | Trust, sandbox, access, or security refusal |
| 60 | Internal engine or adapter-protocol failure |
| 70 | Cancelled or overall deadline exceeded |

Findings do not alter the exit code unless a configured gate selects them.

## 10.6 Artifact locations

- Cache: operating-system application cache directory.
- User configuration: operating-system configuration directory.
- Temporary execution: secure system temporary directory.
- Bundle: explicit `--bundle-out`.
- Repository files: no writes by default.

An interactive audit without `--bundle-out` may produce a temporary or user-data bundle and print the exact path. It should not silently create `.uca/` in the repository.

---

# 11. CI architecture

## 11.1 Ownership split

### UCA owns

- Audit behavior.
- Scope interpretation.
- Baseline comparison.
- Gate evaluation.
- Bundle generation.
- SARIF generation.
- Cache keys.
- Finding fingerprints.
- Completion state.

### CI platform owns

- Checkout.
- Credentials.
- Permissions.
- Scheduling.
- Matrix environments.
- Cache persistence.
- Artifact retention.
- SARIF upload.
- Merge protection.
- Notifications.
- Secrets.
- Runner isolation.

## 11.2 GitHub Action design

Use a thin action:

```text
setup step
  → downloads exact UCA release
  → verifies checksum/signature
  → exposes binary

audit step
  → invokes uca audit
  → uploads bundle
  → uploads SARIF
  → publishes Markdown summary
```

The action must not reimplement:

- Discovery.
- Planning.
- Gate policy.
- Finding conversion.
- Baseline comparison.

Example:

```yaml
permissions:
  contents: read
  security-events: write

steps:
  - uses: actions/checkout@<pinned-sha>
    with:
      fetch-depth: 0

  - uses: cooperonlineenterprises/setup-uca@<pinned-sha>
    with:
      version: "1.0.0"
      verify: true

  - uses: cooperonlineenterprises/uca-action@<pinned-sha>
    with:
      tier: continuous
      baseline: default-branch
      bundle-path: uca-audit

  - uses: github/codeql-action/upload-sarif@<pinned-sha>
    with:
      sarif_file: uca-audit/interoperability/results.sarif
```

## 11.3 Pull-request audit

Inputs must include exact:

- Base revision.
- Head revision.
- Merge basis.
- Checkout depth.
- Changed-file set.
- Baseline bundle.
- UCA version.
- Config digest.

Do not silently fetch missing history unless network permission and remote/refspec are explicit.

## 11.4 Baseline and ratchet

Recommended policy:

```text
Legacy findings:
  visible, not automatically blocking

New deterministic findings:
  block if selected by policy

Recurring findings:
  advisory unless materially worsened

Resolved findings:
  recorded

Heuristic findings:
  advisory

Required analysis unavailable:
  fail closed or partial according to project policy
```

## 11.5 Scheduled execution

```text
Pull request:
  continuous

Nightly:
  continuous/full affected graph
  dependency advisories

Weekly:
  periodic

Release candidate:
  periodic + selected investigative benchmarks

Incident:
  investigative
```

## 11.6 CI artifact policy

The full bundle may contain sensitive project metadata. Defaults:

- SARIF: upload only sanitized source-location findings.
- Summary: no source snippets by default.
- Full raw bundle: local or restricted artifact.
- Semantic context: never upload unless explicitly allowed.
- Profiles: access controlled.
- Retention: configured per tier.
- Secret findings: redact values and avoid raw secret-bearing files.

---

# 12. MCP interface

## 12.1 Architectural rule

`uca-mcp` is a protocol adapter over the same engine and bundle reader.

It must not contain:

- A second planner.
- Independent analyzer selection.
- Independent finding logic.
- A separate cache.
- Its own semantic prompting methodology.
- Code-fixing tools.

## 12.2 MCP tools

Initial tools:

```text
uca_plan_audit
uca_run_audit
uca_get_audit
uca_list_findings
uca_get_finding
uca_explain_finding
uca_list_hotspots
uca_inspect_module
uca_compare_audits
uca_get_capabilities
```

Do not initially expose one tool for every analysis category. Use typed filters:

```json
{
  "audit_id": "AUD-...",
  "filters": {
    "taxonomy_prefix": "UCA.DUP",
    "priority": ["P0", "P1"],
    "status": ["new", "recurring"]
  }
}
```

## 12.3 MCP resources

```text
uca://audits/{audit-id}/manifest
uca://audits/{audit-id}/completion
uca://audits/{audit-id}/findings
uca://audits/{audit-id}/findings/{finding-id}
uca://audits/{audit-id}/hotspots
uca://audits/{audit-id}/reports/summary
```

Large data is paginated or returned by reference.

## 12.4 Not exposed

- Arbitrary shell.
- Arbitrary file reads.
- Adapter installation.
- Tool downloads.
- Network enablement.
- Repository writes.
- Waiver mutation.
- Issue creation.
- Automatic remediation.
- Model-provider credential configuration.
- Raw secret findings.
- Unbounded audit execution.

## 12.5 MCP audit execution

For long operations:

- Return a task/run reference.
- Support progress.
- Support cancellation.
- Write the normal UCA bundle.
- Return bundle and finding references.
- Bind repository roots supplied by the client.
- Reject root escape and untrusted symlink traversal.

---

# 13. Container and sandbox architecture

## 13.1 Image family

Avoid one enormous image containing every analyzer.

```text
uca-minimal
  UCA engine
  built-in analyses
  schemas
  no language runtime collection

uca-toolbox-core
  common safe utilities
  selected generic adapters

uca-toolbox-rust
uca-toolbox-python
uca-toolbox-js
uca-toolbox-go
uca-toolbox-security
uca-toolbox-runtime
```

An audit plan may:

- Run `uca-minimal` only.
- Use one larger prebundled toolbox.
- Invoke separate adapter containers.
- Use trusted host tools.

## 13.2 Default container boundary

```text
/workspace   repository, read-only
/out         audit output, writable
/cache       content-addressed cache, writable
/tmp         bounded tmpfs
```

Container controls:

- Non-root user.
- Read-only root filesystem.
- No privileged mode.
- Drop all Linux capabilities.
- Network none by default.
- PID limit.
- Memory limit.
- CPU quota.
- Wall timeout.
- Seccomp profile.
- No Docker socket.
- No host home mount.
- No host credentials.
- Explicit `.git` read-only access only when history is required.
- Output and cache as the only persistent writable mounts.

## 13.3 Analyzer isolation

Tools that require build outputs should receive:

- A copied or reflinked workspace.
- A tool-specific cache.
- A temporary HOME.
- A sanitized environment.
- No credentials.
- No repository hooks.
- No external diff, pager, or shell.
- Explicit package-manager behavior.

## 13.4 Should OCI be Octon Mini’s preferred boundary?

Recommended policy:

- **High-assurance projects:** OCI or equivalent OS sandbox may be required.
- **Standard projects:** OCI preferred when available.
- **Minimal/local projects:** trusted native executable allowed under explicit local-execution policy and write detection.

OCI should not be universally mandatory because:

- Container runtimes are not equally available on all developer machines.
- Windows/macOS behavior differs.
- Some native profilers require host integration.
- A container itself does not prove safe configuration.

The provider contract should support both:

```text
local_process
oci_image
```

while allowing the project to require OCI.

OCI images should be content-addressed, signed, accompanied by SBOMs, and built with supply-chain provenance.

---

# 14. Optional remote/hosted architecture

## 14.1 Abstractions to define now

Even without a hosted service, define interfaces for:

```rust
trait RepositorySnapshotProvider;
trait AuditJobStore;
trait AuditQueue;
trait ArtifactStore;
trait CacheStore;
trait ExecutionBackend;
trait IdentityContext;
trait CancellationStore;
```

Local implementations:

```text
filesystem snapshot provider
in-process queue
filesystem artifact store
local CAS
local process/OCI executor
local identity
in-memory cancellation
```

Future hosted implementations:

```text
Git/SCM snapshot service
durable queue
object storage
organization CAS
Kubernetes/worker pools
tenant identity
distributed cancellation
```

## 14.2 Future service flow

```text
Client submits immutable audit request
        ↓
Authentication and organization policy
        ↓
Repository snapshot/reference validation
        ↓
Queued job
        ↓
Worker selects signed toolchain image
        ↓
Canonical engine executes
        ↓
Bundle stored in object storage
        ↓
Result reference returned
```

## 14.3 Required future controls

- Tenant isolation.
- Encryption.
- Data-residency policy.
- Source-retention policy.
- Per-tenant network policy.
- Worker image pinning.
- Organization-specific adapter allowlists.
- Signed request and result provenance.
- Quotas.
- Job cancellation.
- Shared-cache confidentiality.
- Audit-log retention.
- Remote model policy.
- No cross-tenant semantic context.

The local CLI and bundle remain fully usable without the service.

---

# 15. Octon Mini integration

## 15.1 Correct representation

UCA should be represented as:

> An external provider referenced by a thin, trigger-installed Octon Mini workflow capability.

It should **not** be:

- Embedded in the Octon kernel.
- An ordinary restrictions-only extension.
- A copied UCA engine in `.agent/scripts`.
- A generic arbitrary action runtime.
- Automatically installed by Octon.
- Required for Octon Mini operation.

## 15.2 Narrow the generic contract

The first provider contract should not mean “any external capability.”

It should be limited to:

```text
provider_class:
  read_only_evidence_producer
```

This prevents it from becoming a second universal action runtime.

Allowed v1 effects:

- Read repository files.
- Read Git history.
- Execute declared local tools.
- Optionally use declared network access.
- Write to a designated external output/cache/temp location.
- Return an immutable evidence reference.

Prohibited:

- Repository mutation.
- Git mutation.
- External publication.
- Deployment.
- Issue creation.
- Communication.
- Credentials beyond declared analyzer services.
- Downstream task creation.
- Self-adoption.
- Authority changes.

Future provider classes require new reviewed contract versions.

## 15.3 Provider manifest

```json
{
  "schema_version": "harness.external-provider-manifest.v1",
  "provider_class": "read_only_evidence_producer",
  "id": "universal-code-audit",
  "display_name": "Universal Code Audit",
  "version": "1.0.0",
  "artifact": {
    "kind": "oci_image",
    "reference": "ghcr.io/cooperonlineenterprises/uca@sha256:...",
    "sha256": "..."
  },
  "provenance": {
    "source": "https://github.com/cooperonlineenterprises/uca",
    "release_attestation_ref": "external:..."
  },
  "interfaces": [
    {
      "kind": "cli_json_process",
      "command": ["uca", "audit"],
      "request_schema": "uca.audit-request.v1",
      "result_schema": "uca.audit-completion.v1",
      "bundle_schema": "uca.audit-manifest.v1"
    }
  ],
  "capabilities": [
    "audit.continuous",
    "audit.periodic",
    "audit.investigative",
    "audit.compare",
    "finding.explain"
  ],
  "access": {
    "repository": "read_only",
    "git_history": "read_only",
    "network": "denied_by_default",
    "repository_writes": "prohibited",
    "external_output_write": "required"
  },
  "sandbox": {
    "minimum": "oci_read_only",
    "privileged": false
  },
  "authority_effect": "none",
  "limitations": [
    "Audit results are evidence and recommendations, not authorization."
  ]
}
```

## 15.4 Octon project records

### Provider registry

```text
.agent/external-providers.json
```

Records:

- Provider ID.
- Version.
- Artifact digest.
- Owner.
- Trust decision.
- Adoption decision.
- Supported capabilities.
- Sandbox requirement.
- Access contract.
- Status.
- Validation receipt.
- Provenance refs.
- Deprecation/successor.

### Provider run state

```text
.agent/provider-runs/
├── active.json
├── runs/
│   └── PRUN-####.json
├── history.jsonl
└── checkpoints/
```

Like Octon Mini’s long-running-work capability, mutable invocation state should be separate from immutable installed package content.

The run record stores only:

- Existing task reference.
- Audit request digest.
- Provider manifest digest.
- Repository identity.
- Reviewed plan digest.
- Execution limits.
- Start and completion state.
- Bundle reference.
- Bundle digest.
- Completion status.
- Limitations.
- Evidence registration reference.

It should not copy UCA findings into Octon’s kernel state.

## 15.5 Invocation workflow

```text
1. Existing TASK-#### identifies audit purpose and scope.
2. Provider package is installed through content-addressed plan/apply.
3. Project accepts a provider trust/adoption decision.
4. Octon plans an invocation.
5. Planning resolves exact UCA artifact, request, revision, sandbox, and output.
6. Operator reviews the plan digest.
7. Octon executes the exact provider invocation.
8. UCA writes its bundle outside the repository or to approved artifact storage.
9. Octon validates manifest, digest, revision, and completion.
10. Octon records an evidence/artifact reference.
11. Humans or governed agents review findings.
12. Any remediation becomes ordinary Octon work through existing task/decision processes.
```

## 15.6 Proposed Octon command route

A generic but deliberately narrow route:

```text
octon provider status
octon provider plan
octon provider run
octon provider resume
octon provider explain
```

Example:

```bash
./octon provider plan \
  --provider universal-code-audit \
  --capability audit.periodic \
  --task TASK-0042 \
  --request /review/uca-request.json \
  --output /review/provider-plan.json

./octon provider run \
  --plan /review/provider-plan.json \
  --accept-digest <reviewed-digest>
```

The command does not install UCA or widen rights.

## 15.7 Minimal Octon Mini source additions

1. Add `harness.external-provider-manifest.v1` schema.
2. Add `harness.external-provider-registry.v1` schema.
3. Add `harness.external-provider-request.v1` schema.
4. Add `harness.external-provider-result-ref.v1` schema.
5. Add a trigger-installed `external-evidence-provider` workflow package.
6. Add its content-addressed inventory to the profile manifest.
7. Add a dormant dispatcher route.
8. Add package-owned provider-run validator.
9. Add direct-argv provider execution with sanitized environment.
10. Add native and OCI execution backends.
11. Add exact pre/post repository mutation detection for native mode.
12. Add output-manifest and digest validation.
13. Add a command-manifest capability entry.
14. Add acceptance fixtures for:
    - absent provider;
    - untrusted provider;
    - digest mismatch;
    - wrong version;
    - repository mutation;
    - unexpected network request;
    - partial UCA completion;
    - stale revision;
    - malformed bundle;
    - successful evidence registration.
15. Add a golden-path document.
16. Add migration and compatibility rules.
17. Add release acceptance criterion for external evidence providers.

No UCA analyzer code belongs in Octon Mini.

---

# 16. Repository and source-code structure

## 16.1 Recommended repository

```text
universal-code-audit/
├── Cargo.toml
├── Cargo.lock
├── rust-toolchain.toml
├── README.md
├── LICENSE
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── VERSION
│
├── crates/
│   ├── uca-model/
│   ├── uca-schema/
│   ├── uca-config/
│   ├── uca-core/
│   ├── uca-repository/
│   ├── uca-discovery/
│   ├── uca-planner/
│   ├── uca-executor/
│   ├── uca-sandbox/
│   ├── uca-cache/
│   ├── uca-artifacts/
│   ├── uca-provenance/
│   ├── uca-evidence/
│   ├── uca-normalize/
│   ├── uca-fusion/
│   ├── uca-findings/
│   ├── uca-priority/
│   ├── uca-compare/
│   ├── uca-report/
│   ├── uca-history/
│   ├── uca-graph/
│   ├── uca-analysis-structure/
│   ├── uca-analysis-duplication/
│   ├── uca-analysis-hotspots/
│   ├── uca-analysis-architecture/
│   ├── uca-analysis-simplification/
│   ├── uca-adapter-protocol/
│   ├── uca-adapter-sdk/
│   ├── uca-language-sdk/
│   ├── uca-cli/
│   ├── uca-mcp/
│   └── uca-http/
│
├── schemas/
│   ├── v1/
│   ├── test-vectors/
│   └── catalog.json
│
├── taxonomy/
│   ├── v1/
│   ├── dimensions.json
│   ├── findings.json
│   └── metrics.json
│
├── policies/
│   ├── continuous-default.toml
│   ├── periodic-default.toml
│   └── security-default.toml
│
├── adapters/
│   ├── generic-sarif/
│   ├── generic-cyclonedx/
│   ├── generic-spdx/
│   ├── generic-coverage/
│   ├── generic-pprof/
│   ├── semgrep/
│   ├── codeql/
│   ├── osv-scanner/
│   ├── syft/
│   └── trivy/
│
├── languages/
│   ├── rust/
│   ├── python/
│   ├── javascript-typescript/
│   └── go/
│
├── frameworks/
│   └── README.md
│
├── integrations/
│   ├── github-action/
│   ├── generic-ci/
│   ├── mcp/
│   └── octon-mini/
│
├── containers/
│   ├── minimal/
│   ├── toolbox-core/
│   ├── toolbox-security/
│   └── language-toolboxes/
│
├── fixtures/
│   ├── repositories/
│   │   ├── synthetic/
│   │   ├── hostile/
│   │   └── polyglot/
│   ├── adapters/
│   ├── bundles/
│   ├── schemas/
│   └── comparisons/
│
├── test-repositories/
│   ├── manifest.json
│   ├── licenses.json
│   └── fetch-and-verify/
│
├── benchmarks/
│   ├── corpus/
│   ├── discovery/
│   ├── continuous/
│   ├── periodic/
│   ├── large-repository/
│   └── reports/
│
├── examples/
│   ├── uca.toml
│   ├── audit-request.json
│   ├── architecture-rules.toml
│   └── github-actions/
│
├── docs/
│   ├── architecture/
│   ├── concepts/
│   ├── methodology/
│   ├── reference/
│   ├── adapters/
│   ├── languages/
│   ├── integrations/
│   ├── security/
│   └── development/
│
├── rfcs/
├── adr/
├── scripts/
└── xtask/
```

## 16.2 Crate ownership

Keep dependencies directional:

```text
uca-model / uca-schema
          ↑
repository, discovery, graph, history
          ↑
planner, executor, adapter protocol
          ↑
evidence, normalization, fusion, findings
          ↑
report, compare
          ↑
CLI / MCP / HTTP
```

The core data model must not depend on:

- CLI.
- MCP.
- CI.
- Octon.
- Specific external tools.
- Model providers.

## 16.3 Monorepo versus multiple repositories

Start with one UCA repository for:

- Engine.
- Schemas.
- First-party adapters.
- Language packs.
- CLI.
- MCP.
- Container definitions.
- CI integration sources.
- Conformance fixtures.

Split only when:

- An adapter has materially different release ownership.
- A large benchmark corpus becomes burdensome.
- A hosted service requires private infrastructure.
- A language pack needs an independent lifecycle.
- Security isolation requires separate publishing.

The Octon workflow package itself belongs in the Octon Mini repository. UCA should carry only provider-contract conformance fixtures and examples.

---

# 17. Technology-stack recommendation

| Area | Recommendation |
|---|---|
| Core | Rust 2024 |
| Async/process | Tokio |
| CLI | Clap |
| Serialization | Serde |
| Schema | JSON Schema 2020-12 |
| Project config | TOML |
| Hashing | SHA-256 for public/content identities |
| Canonical JSON | RFC 8785 JCS |
| Metadata index | SQLite |
| Blob cache | Filesystem content-addressed store |
| Compression | zstd |
| Graph algorithms | Petgraph or a thin internal abstraction |
| Git access | Prefer pure-Rust object/history reading; shell Git only where needed and constrained |
| Syntax baseline | Tree-sitter |
| Reports | Static Markdown and self-contained HTML |
| SARIF | Native UCA projection |
| OCI | Standard OCI images |
| Signing | Sigstore/Cosign |
| SBOM | CycloneDX and SPDX release artifacts |
| Provenance | SLSA-compatible attestations |
| MCP | Separate Rust binary using official SDK |
| HTTP | Axum or equivalent, deferred |
| Local model interface | Out-of-process JSON protocol |
| Remote models | Adapter/provider abstraction |

Use SQLite only for indexes and mutable local cache metadata. Durable bundle documents remain ordinary files.

---

# 18. Configuration model

## 18.1 Project configuration

`uca.toml`:

```toml
schema_version = "uca.config.v1"

[audit]
default_tier = "continuous"
generated_code = "analyze_separately"
vendor_code = "exclude"

[scope]
include = ["src/**", "tests/**"]
exclude = ["dist/**", "vendor/**", "fixtures/large/**"]
sensitive = [".env*", "**/*.pem", "private/**"]

[execution]
network = "denied"
project_code = "denied"
sandbox = "local_read_only"
maximum_parallel_tasks = 4

[budgets.continuous]
wall_seconds = 120
memory_mib = 2048

[budgets.periodic]
wall_seconds = 1800
memory_mib = 4096

[adapters]
enabled = ["generic-sarif", "osv-scanner", "semgrep"]
disabled = ["semantic-ai"]

[baseline]
mode = "ratchet"
reference = ".uca-baseline/reference.json"

[reporting]
sarif = true
markdown = true
html = false
raw_evidence = "local_only"

[ai]
enabled = false
```

## 18.2 Architecture rules

Keep these declarative and small:

```toml
schema_version = "uca.architecture-rules.v1"

[[rule]]
id = "ARCH-001"
description = "Domain must not depend on infrastructure"
kind = "forbidden_dependency"
from = ["module:domain/**"]
to = ["module:infrastructure/**"]
severity = "error"

[[rule]]
id = "ARCH-002"
description = "Feature modules must be acyclic"
kind = "acyclic_group"
members = ["module:features/*"]
severity = "error"
```

Do not create a general programming language or policy DSL in v1.

## 18.3 Tool lock

`uca.lock.json` records exact reproducibility policy:

```json
{
  "schema_version": "uca.tool-lock.v1",
  "uca_version": "1.0.0",
  "adapters": [
    {
      "id": "semgrep",
      "adapter_version": "1.1.0",
      "adapter_sha256": "...",
      "tool_version": "1.136.0",
      "rules_sha256": "..."
    }
  ]
}
```

## 18.4 Suppressions

Use a separate file:

```text
uca-waivers.toml
```

This keeps audit selection separate from debt disposition.

## 18.5 Secret handling

Configuration files may contain:

- Secret reference names.
- Credential-provider IDs.
- Environment-variable names.

They may not contain:

- Tokens.
- API keys.
- Private keys.
- Passwords.

---

# 19. Caching, incrementality, and performance

## 19.1 Storage design

```text
cache-root/
├── blobs/
│   └── sha256/ab/cdef...
├── task-results/
├── repository-manifests/
├── graphs/
├── history/
├── metadata.sqlite
└── quarantine/
```

SQLite indexes:

- Content digest.
- Adapter/task key.
- Creation time.
- Last use.
- Size.
- Scope.
- Tool identity.
- Configuration identity.
- Environment identity.
- Provenance.
- Dependency keys.
- Validation status.

## 19.2 Cache key

```text
capability
+ analyzer/adapter version
+ tool version/digest
+ rule/query/config digest
+ normalized task input
+ repository content manifest
+ scope digest
+ material environment fingerprint
+ normalizer version
```

A Git commit alone is insufficient for:

- Dirty worktrees.
- Generated files outside the index.
- Tool environment differences.
- Partial scopes.

## 19.3 Incremental model

### Repository manifest

Hash only changed metadata/content where possible.

### Dependency graph

Track:

- File-to-node ownership.
- Edge producers.
- Affected nodes.
- Invalidating language-pack conditions.
- Whole-program invalidation triggers.

### History

Cache by:

```text
repository identity
+ history head
+ window
+ filters
+ rename policy
```

### Analyzer reuse

An adapter declares whether incremental reuse is:

```text
safe
safe_with_conditions
unsupported
```

### Finding comparison

Stable fingerprints allow:

- New.
- Recurring.
- Changed evidence.
- Resolved.
- Scope-incompatible.

## 19.4 Scheduler

Resource classes:

```text
cpu_light
cpu_heavy
memory_heavy
io_heavy
exclusive_build
network
model
```

The scheduler enforces:

- Global concurrency.
- Per-class concurrency.
- Memory reservation.
- Exclusive repository-build access.
- Cancellation.
- Deadline.
- Output limit.

Do not concurrently run incompatible build tools in the same writable sandbox.

## 19.5 Reference performance targets

On a published reference machine and benchmark corpus:

| Operation | Target |
|---|---:|
| Warm discovery, 10,000 files | p95 under 2 seconds |
| Cold discovery, 100,000 files | p95 under 15 seconds |
| Continuous audit, medium repository, warm cache | p50 under 20 seconds |
| Continuous audit, medium repository, warm cache | p95 under 90 seconds |
| Continuous audit hard default budget | 120 seconds |
| Periodic audit, medium repository | typical under 30 minutes |
| Periodic default ceiling | 60 minutes |
| Bundle comparison, 50,000 findings | p95 under 5 seconds |
| Markdown summary generation | p95 under 2 seconds |
| Engine memory excluding external tools, medium repository | under 512 MiB target |

Publish failed benchmark samples as evidence. Avoid silently dropping slow repositories from reports.

## 19.6 Large-repository behavior

Use:

- Module-level partitioning.
- Changed-subgraph analysis.
- Explicit maximum file count/bytes.
- Streaming JSONL.
- Compressed graphs.
- Bounded raw evidence.
- Per-language work queues.
- Optional statistically disclosed sampling for low-value analyses.
- Full analysis for safety gates that cannot tolerate sampling.

Sampling must declare:

- Population.
- Method.
- Sample size.
- Coverage.
- Confidence limitations.
- Ineligibility for blocking conclusions.

---

# 20. Security and trust model

## 20.1 Trust boundaries

```text
Trusted UCA engine
      │
      ├── untrusted repository
      ├── untrusted project configuration
      ├── trusted-but-constrained adapter executable
      ├── untrusted analyzer output
      ├── optional network service
      ├── optional model provider
      ├── local cache
      └── output consumer
```

## 20.2 Threats and controls

| Threat | Default controls |
|---|---|
| Hostile build script | Never execute project code by default |
| Symlink escape | Resolve root safely; reject escaping ancestors; do not follow untrusted symlinks |
| Device/FIFO/socket files | Exclude non-regular files |
| Decompression bomb | Archive count, depth, compressed, and expanded-byte limits |
| Parser exploit | Memory-safe parsers, fuzzing, size/depth limits, process isolation for risky parsers |
| Command injection | Direct argv only; no shell |
| Malicious Git configuration | Prefer library parsing; disable hooks, pagers, external filters and diff commands |
| Crafted Git history | Commit/object count limits, bounded rename analysis, parser fuzzing |
| Untrusted UCA project config | Cannot widen host security policy; no executable paths without trust |
| Malicious analyzer output | Schema validation, length/depth limits, raw/normalized separation |
| Secret exposure | Sensitive-path exclusion, redaction, no secret values in bundle |
| Network exfiltration | Network denied by default; explicit endpoint policy |
| Dependency compromise | Locked dependencies, signed releases, SBOM, provenance, vulnerability monitoring |
| Adapter compromise | Content digest, trust registry, separate process/container, least privilege |
| Prompt injection | Repository content treated as data; no model tools; cited structured output |
| Poisoned comments/docs | Cannot change scope, tools, or instructions |
| Resource exhaustion | CPU, memory, PID, wall, file, output, and graph limits |
| Cache poisoning | Content addressing, producer identity, validation, quarantine |
| TOCTOU on repository | Identity before and after relevant tasks; read-only mount or snapshot |
| Repository mutation by analyzer | Read-only mount, copied sandbox, or before/after detection |
| Malicious report content | HTML escaping, no remote assets, CSP, no executable report data |
| Hosted cross-tenant leakage | Deferred until tenant isolation and cache partitioning are implemented |

## 20.3 Safe defaults

```text
network                 denied
project code execution  denied
repository writes       denied
shell                    denied
adapter auto-discovery   denied
tool installation        denied
remote models            denied
raw source upload        denied
secret-bearing paths     excluded
arbitrary archives       not expanded
privileged container     denied
host home                not mounted
credentials              removed from environment
```

## 20.4 Project execution escalation

An analysis requiring tests or builds must report:

```json
{
  "project_execution": {
    "required": true,
    "reason": "collect branch coverage",
    "commands": [
      ["cargo", "llvm-cov", "--json"]
    ],
    "sandbox": "copied_workspace",
    "network": "denied",
    "writes": ["sandbox_build", "task_output"],
    "risk": "repository_defined_build_code"
  }
}
```

The operator or governing system must explicitly accept this execution class.

---

# 21. Testing and validation strategy

## 21.1 Test layers

### Unit tests

- Canonicalization.
- Hashing.
- IDs.
- Configuration merge.
- Scope resolution.
- Graph algorithms.
- Metric normalization.
- Priority inputs.
- Fingerprinting.
- Waiver matching.
- Cache keys.
- Redaction.

### Schema tests

- Every fixture validates.
- Duplicate-key rejection.
- Unknown-field behavior.
- Schema composition.
- Backward-compatible additive changes.
- Invalid boundary values.
- Canonical JSON test vectors.
- Large/deep malicious document limits.

### Adapter contract tests

- Manifest validation.
- Describe/probe/run.
- Version negotiation.
- Tool unavailable.
- Tool wrong version.
- Timeout.
- Cancellation.
- Invalid output.
- Oversized output.
- Partial result.
- Redaction.
- Cache reuse.
- Network denial.

### Golden repository fixtures

Synthetic repositories for:

- Cycles.
- Layer violations.
- God modules.
- Exact clones.
- Near clones.
- Dead functions.
- Dynamic entry points.
- High-churn files.
- Temporal coupling.
- Reverts.
- Ownership concentration.
- Long migrations.
- Weak tests.
- Vulnerable dependencies.
- Build-system duplication.
- Over-abstraction.

### Real repository corpus

Use pinned, license-reviewed open-source repositories covering:

- Small and large projects.
- Monorepos.
- Polyglot repositories.
- Different build systems.
- Static and dynamic languages.
- Long histories.
- Generated code.
- Framework-heavy applications.

Avoid vendoring large repositories into the primary source tree. Maintain:

- Exact repository URL.
- Commit SHA.
- License.
- Expected capabilities.
- Known findings.
- Fetch hash.
- Reproducible setup.

### Hostile repository tests

- Symlink loops.
- Root escapes.
- Giant files.
- Millions of tiny files.
- Malformed Git objects.
- Deep JSON.
- Duplicate JSON keys.
- Crafted filenames.
- ANSI/control characters.
- Malicious HTML.
- Build scripts.
- Shell metacharacters.
- Prompt-injection comments.
- Secret-like content.
- Archive bombs.
- Analyzer-output bombs.

### Determinism tests

For identical inputs:

- Byte-identical canonical documents.
- Stable plan digest.
- Stable observation IDs where content-derived.
- Stable finding fingerprints.
- Stable normalized bundle excluding declared run-time fields.
- Stable ordering.

Separate nondeterministic run metadata from content identity.

### Cross-platform tests

- Linux.
- macOS.
- Windows.
- Path separators.
- Case sensitivity.
- Unicode.
- Long paths.
- Process cancellation.
- Permission handling.
- Container behavior where supported.

### Performance tests

- 10,000 files.
- 100,000 files.
- Million-edge graphs.
- Long Git histories.
- Large SARIF.
- Large SBOM.
- Large finding comparison.
- Cold and warm cache.
- Memory pressure.
- Cancellation.

### AI tests

- Schema-valid mock provider.
- Missing citations.
- Fabricated paths.
- Prompt injection.
- Secret exclusion.
- Context budget.
- Repeated-run variation.
- Local provider.
- Remote provider policy refusal.
- Human-review flag.

### Interface tests

- CLI command snapshots.
- stdout/stderr separation.
- Exit codes.
- JSON and NDJSON.
- MCP conformance.
- MCP root isolation.
- GitHub Action test repositories.
- OCI read-only behavior.
- Octon provider contract.

## 21.2 Usefulness evaluation

Do not optimize for number of findings.

Use curated review studies:

1. Present top 10 findings to maintainers.
2. Ask whether each is:
   - actionable;
   - accurate;
   - consequential;
   - already known;
   - correctly prioritized.
3. Record dismissal reason.
4. Track whether remediation occurred.
5. Validate claimed benefit after remediation.
6. Measure reviewer time.

Core measures:

```text
precision among top 10
precision among top 50
time to first useful finding
review minutes per accepted finding
dismissed-as-noise rate
remediation yield
validated-benefit rate
```

---

# 22. Evaluation and quality measurement

## 22.1 UCA quality dimensions

| Dimension | Measure |
|---|---|
| Precision | Confirmed useful findings / reviewed findings |
| Recall | Known ground-truth findings detected where a corpus exists |
| Noise burden | Dismissals per audit and per reviewer hour |
| Stability | Unchanged findings retaining fingerprint |
| Reproducibility | Canonical output equality across identical runs |
| Coverage honesty | Accuracy of declared analyzed scope |
| Time to value | Time to first useful finding |
| Remediation yield | Accepted findings that become completed work |
| Benefit validation | Remediations with demonstrated improvement |
| Simplification yield | Code, dependency, configuration, state, or concept reduction |
| Hotspot usefulness | Top-ranked hotspots correlated with maintenance work |
| Performance guidance | Investigations leading to measured improvement |
| Analysis cost | CPU, memory, wall time, storage, external service cost |
| Adoption | Successful audits and repeat usage |
| Trust | Findings rejected due to unexplained reasoning |
| Compatibility | Adapter/schema break rate |

## 22.2 Avoid metric gaming

Do not reward:

- Raw finding count.
- Global coverage percentage.
- Global complexity decrease.
- Number of adapters.
- Number of supported languages without depth.
- Number of AI recommendations.
- Overall “health score.”
- Suppression count reduction without issue resolution.
- Performance improvement on unrepresentative benchmarks.

Publish:

- Scope.
- Corpus.
- Ground truth.
- Sampling.
- Missing data.
- Failed analyses.
- Confidence intervals where relevant.
- Tool versions.
- Repository revisions.

---

# 23. Documentation plan

| Document | Purpose |
|---|---|
| `README.md` | Product purpose, installation, first audit |
| `docs/architecture/OVERVIEW.md` | System and dependency architecture |
| `docs/architecture/INVARIANTS.md` | Non-negotiable product rules |
| `docs/concepts/EVIDENCE.md` | Raw, normalized, fused, semantic evidence |
| `docs/concepts/FINDINGS.md` | Finding model and lifecycle |
| `docs/concepts/CONFIDENCE.md` | Confidence vector |
| `docs/concepts/PRIORITY.md` | Transparent prioritization |
| `docs/methodology/UNIVERSAL_AUDIT.md` | Full audit methodology |
| `docs/reference/CLI.md` | Commands, flags, exit codes |
| `docs/reference/CONFIGURATION.md` | Config and precedence |
| `docs/reference/SCHEMAS.md` | Schema catalog |
| `docs/reference/BUNDLE.md` | Audit bundle contract |
| `docs/adapters/SDK.md` | Adapter development |
| `docs/adapters/SECURITY.md` | Adapter trust and sandboxing |
| `docs/languages/DEVELOPMENT.md` | Language-pack development |
| `docs/integrations/GITHUB_ACTIONS.md` | GitHub CI |
| `docs/integrations/GENERIC_CI.md` | Other CI |
| `docs/integrations/MCP.md` | MCP tools/resources |
| `docs/integrations/OCTON_MINI.md` | Provider contract |
| `docs/containers/EXECUTION.md` | Images and mounts |
| `docs/security/THREAT_MODEL.md` | Threat analysis |
| `docs/security/PRIVACY.md` | Data and model-provider handling |
| `docs/security/RELEASE_SECURITY.md` | Signing, SBOM, provenance |
| `docs/development/CONTRIBUTING.md` | Engineering workflow |
| `docs/development/ADAPTER_MATURITY.md` | Experimental-to-stable lifecycle |
| `docs/development/RELEASE.md` | Release process |
| `docs/development/COMPATIBILITY.md` | Version guarantees |
| `docs/TROUBLESHOOTING.md` | Diagnosis |
| `examples/` | Reproducible configurations and CI |
| `adr/` | Accepted architectural decisions |
| `rfcs/` | Proposed protocol/schema changes |

---

# 24. Versioning and compatibility

## 24.1 Independent versions

| Concern | Version |
|---|---|
| UCA product | SemVer |
| Audit bundle | `uca.audit-bundle.v1` |
| Individual JSON schemas | Independent major in schema ID |
| Configuration | `uca.config.v1` |
| Adapter protocol | SemVer |
| Adapter implementation | SemVer |
| Language-pack contract | SemVer |
| Finding taxonomy | SemVer |
| Priority policy | Independent version |
| MCP tool API | Independent UCA API version plus MCP protocol date |
| Octon provider contract | `harness.external-provider-manifest.v1` |
| OCI image | UCA release plus immutable digest |

## 24.2 Compatibility policy

- Writers emit the current schema major only.
- UCA production releases read current and previous bundle major.
- Additive optional fields require a schema minor/product minor.
- Required-field or semantic changes require schema major.
- Taxonomy IDs are never reused.
- Deprecated taxonomy IDs name a successor.
- Adapter protocol negotiates minimum and maximum versions.
- Unknown required fields fail closed.
- Unknown optional observation types are retained but not interpreted.
- A comparison across incompatible methodologies reports incompatibility rather than a false trend.
- `uca schema migrate` performs only deterministic, documented transformations.
- Lossy migrations require explicit output and limitation records.

---

# 25. Packaging and distribution

## 25.1 Release artifacts

For each supported platform:

```text
uca
uca-mcp
checksums.sha256
checksums.sig
SBOM.cdx.json
SBOM.spdx.json
provenance.intoto.jsonl
release-manifest.json
```

Targets:

- Linux x86_64.
- Linux ARM64.
- macOS ARM64.
- macOS x86_64 where still supported.
- Windows x86_64.

## 25.2 Distribution channels

### Production v1

- GitHub Releases.
- OCI image in GHCR.
- Homebrew formula.
- Scoop or winget package.
- `cargo install` as a secondary developer path.
- GitHub Action.
- Standalone MCP binary.

### Later

- Linux distribution packages.
- Nix package.
- Organization-managed registries.
- Hosted-service client.

## 25.3 Release integrity

Each release requires:

- Checksums.
- Signature.
- CycloneDX SBOM.
- SPDX SBOM.
- Build provenance.
- Source commit.
- Toolchain identity.
- Reproducibility report.
- Vulnerability scan.
- License report.
- Compatibility report.
- Benchmark report.

No automatic self-update should be built into the engine initially. `uca doctor` may report that a newer release exists only when network access is explicitly enabled; installation remains operator-owned.

---

# 26. Development workflow and governance

## 26.1 Decision records

Use ADRs for:

- Rust selection.
- Process adapter boundary.
- Evidence model.
- Canonical serialization.
- Cache design.
- No mutation boundary.
- No auto-install.
- AI evidence class.
- MCP separation.
- Octon provider contract.
- Hosted-service deferral.

Use RFCs for:

- Schema major changes.
- Adapter protocol changes.
- New blocking capability.
- New provider class.
- New remote execution model.
- New AI authority posture.
- Major language-pack architecture.

## 26.2 Issue taxonomy

```text
area/engine
area/schema
area/evidence
area/finding
area/adapter
area/language
area/history
area/graph
area/security
area/performance
area/cli
area/ci
area/mcp
area/container
area/octon
area/docs

type/bug
type/false-positive
type/false-negative
type/compatibility
type/security
type/performance-regression
type/proposal
type/research
```

## 26.3 Analyzer maturity

```text
experimental
  off by default
  no compatibility guarantee
  no blocking findings

preview
  opt-in
  versioned output
  evaluation corpus exists

stable
  supported versions
  owner
  precision evidence
  contract tests
  stable fingerprints

gate_capable
  deterministic or tightly bounded
  high precision
  low-noise validation
  stable taxonomy
  published failure semantics
```

Only gate-capable findings may be enabled as default blockers.

## 26.4 Release gates

- Full unit/integration pass.
- Schema conformance pass.
- Compatibility pass.
- Determinism pass.
- Hostile-repository pass.
- Cross-platform pass.
- Performance budgets.
- Adapter version matrix.
- Security review.
- Dependency and license review.
- SBOM and provenance.
- Signed artifacts.
- Documentation completeness.
- Upgrade/migration test.
- At least one real-project validation.
- No unexplained benchmark regression.
- No unresolved critical false-positive regression in default gates.

---

# 27. Implementation roadmap

## Phase 0 — Charter, invariants, and threat model

**Objective:** prevent architectural drift before code exists.

**Work**

- Product charter.
- Boundary matrix.
- Invariants.
- Threat model.
- ADR set.
- Initial taxonomy principles.
- Licensing decision.
- Repository scaffolding.
- CI skeleton.

**Deliverables**

- README.
- Architecture overview.
- Threat model.
- ADR-0001 through ADR-0010.
- Rust workspace.
- Security policy.

**Tests**

- CI can build an empty CLI on all target platforms.
- Documentation link validation.

**Acceptance**

- Every major responsibility has one owner.
- No ambiguity about mutation, network, AI, or adapter boundaries.

**Risks**

- Premature feature detail.
- Architecture without a working vertical slice.

**Explicitly deferred**

- External analyzers.
- MCP.
- hosted service.
- AI.

---

## Phase 1 — Evidence and schema kernel

**Objective:** establish durable contracts first.

**Work**

- Schema catalog.
- Audit request.
- Repository identity.
- Scope.
- Audit plan.
- Analyzer run.
- Observation.
- Finding.
- Completion.
- Comparison.
- Provenance.
- JCS canonicalization.
- SHA-256 identity.
- JSON duplicate-key rejection.

**Deliverables**

- `uca-model`.
- `uca-schema`.
- `schemas/v1`.
- Test vectors.
- Bundle skeleton.

**Tests**

- Schema positive/negative fixtures.
- Canonicalization vectors.
- Round trips.
- Stable digests.
- Duplicate-key and malformed-number rejection.

**Acceptance**

- A synthetic audit bundle validates and has a reproducible content ID.
- Every contract names a compatibility policy.

**Risks**

- Overdesigning schemas.
- Encoding unproven analyzer assumptions.

**Deferred**

- Detailed domain-specific observation payloads beyond required extension envelopes.

---

## Phase 2 — Engine skeleton and canonical CLI

**Objective:** prove one engine can power the CLI without interface leakage.

**Work**

- Engine trait.
- Command application services.
- `discover`, `plan`, `audit`, `compare`, `report`.
- Structured events.
- Exit codes.
- Atomic bundle finalization.
- Partial-completion semantics.

**Deliverables**

- `uca-core`.
- `uca-cli`.
- Empty/no-op audit vertical slice.
- Minimal Markdown report.

**Tests**

- CLI integration.
- stdout/stderr.
- Cancellation.
- Invalid request.
- Partial audit.
- Stable plan.

**Acceptance**

- `uca audit` produces a valid bundle even when no analyzers are selected.
- CLI contains no analyzer-specific logic.

**Risks**

- CLI becoming the engine.
- Conflating execution failure with finding gates.

---

## Phase 3 — Repository identity, scope, and discovery

**Objective:** establish the exact subject before analysis.

**Work**

- Git repository identity.
- Dirty worktree overlay.
- File manifest.
- Path safety.
- generated/vendor/test classification.
- language and manifest detection.
- sensitive-path policy.
- basic framework detection.

**Deliverables**

- `uca-repository`.
- `uca-discovery`.
- discovery report.
- repository/scope documents.

**Tests**

- Clean commit.
- Dirty worktree.
- Untracked files.
- symlink escape.
- Unicode paths.
- large files.
- unsupported repository.
- archive subject.

**Acceptance**

- Repeated discovery of unchanged content is byte-stable.
- Unsafe paths cannot escape scope.

**Risks**

- Git edge cases.
- Overbroad framework inference.

**Deferred**

- Deep framework semantics.

---

## Phase 4 — Planner, executor, sandbox, and cache

**Objective:** create the secure execution backbone.

**Work**

- Capability catalog.
- Deterministic planner.
- DAG scheduler.
- task state machine.
- direct-argv process runner.
- sanitized environment.
- output/time/process limits.
- local read-only mode.
- copied-workspace mode.
- CAS.
- SQLite index.
- cancellation propagation.

**Deliverables**

- `uca-planner`.
- `uca-executor`.
- `uca-sandbox`.
- `uca-cache`.
- mock task provider.

**Tests**

- DAG dependencies.
- parallel resource classes.
- timeout.
- process-group kill.
- repository write detection.
- corrupt cache.
- cache hit/miss identity.
- task partial failure.

**Acceptance**

- A hostile mock analyzer cannot modify the source unnoticed.
- Required and optional task failures produce correct completion states.

**Risks**

- Cross-platform process behavior.
- False confidence in “read-only” local execution.

**Deferred**

- Strong OCI boundary until Phase 11.

---

## Phase 5 — Deterministic repository intelligence

**Objective:** prove UCA’s native differentiated value.

**Work**

- Git churn.
- ownership concentration.
- reverts.
- co-change.
- file/module graph.
- SCC/cycles.
- exact duplication.
- file metrics.
- hotspot combination.
- stable findings.
- baseline comparison.

**Deliverables**

- `uca-history`.
- `uca-graph`.
- exact duplicate engine.
- hotspot report.
- comparison report.

**Tests**

- Synthetic histories.
- rename behavior.
- bot/format filtering.
- cycles.
- exact clone groups.
- stable fingerprints.

**Acceptance**

- UCA can identify meaningful complexity/churn and architecture hotspots without external tools.
- Every result is traceable to repository evidence.

**Risks**

- History noise.
- Mistaking centrality for poor design.

**Deferred**

- Semantic duplication.
- deep symbol graphs.

### Milestone: Minimum Viable Architecture

At the end of Phase 5, the architecture is proven rather than merely described.

---

## Phase 6 — Adapter protocol and first integrations

**Objective:** prove UCA can use best-in-class tools without becoming coupled to them.

**Work**

- Adapter manifest.
- probe/run protocol.
- adapter SDK.
- conformance harness.
- generic SARIF importer.
- generic CycloneDX/SPDX importers.
- generic coverage importer.
- Semgrep adapter.
- OSV adapter.
- Syft adapter.
- first native compiler adapter.

**Deliverables**

- `uca-adapter-protocol`.
- `uca-adapter-sdk`.
- first stable adapters.
- tool lock.

**Tests**

- Mock tools.
- version negotiation.
- invalid output.
- oversized output.
- tool absence.
- network denial.
- adapter matrix.

**Acceptance**

- The engine has no imports or direct dependencies on underlying tool implementations.
- Missing optional tools yield truthful limitations.

**Risks**

- Adapter-specific exceptions leaking into core.
- Tool licensing and output changes.

**Deferred**

- Broad commercial-tool catalog.

---

## Phase 7 — Continuous audit and gate model

**Objective:** make UCA useful on real pull requests.

**Work**

- Changed-scope planning.
- affected-module expansion.
- baseline ratchet.
- gate policy.
- SARIF projection.
- finding fingerprint hardening.
- public API diff integration.
- continuous performance budgets.
- default low-noise policy.

**Deliverables**

- `continuous-default.toml`.
- SARIF report.
- pull-request comparison.
- gate completion status.

**Tests**

- New versus legacy finding.
- moved lines.
- renamed file.
- resolved finding.
- incomplete required capability.
- advisory heuristic.
- gate exit codes.

**Acceptance**

- Default continuous audit produces a bounded, reviewable result set.
- No heuristic or AI-only finding blocks by default.
- Top findings meet the initial precision target.

**Risks**

- Excessive PR latency.
- baseline mismatch.

---

## Phase 8 — Periodic audit intelligence

**Objective:** provide repository-wide architectural maintenance.

**Work**

- Full temporal coupling.
- centrality.
- graph communities.
- architecture reflexion.
- near-duplicate candidates.
- feature-flag age.
- migration analysis.
- dependency overlap.
- test-duration ingestion.
- mutation-result ingestion.
- simplification rule engine.

**Deliverables**

- Periodic policy.
- architecture report.
- simplification report.
- ranked debt candidates.

**Tests**

- Large graph.
- long migration fixture.
- co-change without static edge.
- valid intentional duplication.
- accepted debt.
- stale waiver.

**Acceptance**

- Periodic audit produces a ranked top set rather than an undifferentiated warning dump.
- Every simplification finding includes validation and change risk.

**Risks**

- Noisy heuristics.
- graph-analysis cost.

---

## Phase 9 — Language packs and useful-v1 stabilization

**Objective:** deliver credible cross-language usefulness.

**Work**

- Rust pack.
- Python pack.
- JS/TS pack.
- Go pack.
- capability matrix.
- native compiler/linter integrations.
- coverage integrations.
- entry-point roots.
- language-specific blind spots.
- documentation.

**Deliverables**

- Four supported language packs.
- generic fallback.
- useful-v1 release candidate.

**Tests**

- Polyglot repositories.
- dynamic dispatch.
- generated code.
- monorepos.
- unsupported language.
- mixed tool versions.

**Acceptance**

- At least two language packs meet stable maturity.
- Remaining packs meet preview or stable criteria.
- Generic audit remains useful on unsupported languages.

**Risks**

- Language bias.
- support matrix burden.

### Milestone: Useful v1

---

## Phase 10 — CI integration

**Objective:** make continuous and scheduled auditing operational.

**Work**

- Setup action.
- audit action.
- generic CI examples.
- baseline artifact retrieval.
- cache integration.
- SARIF upload.
- Markdown summary.
- permissions guide.
- scheduled workflows.

**Deliverables**

- First-party GitHub Action.
- CI templates.
- end-to-end test repositories.

**Tests**

- fork pull request.
- no write token.
- shallow history.
- missing baseline.
- cache restore.
- SARIF upload.
- artifact sensitivity.

**Acceptance**

- A project can add UCA to a PR with a small pinned workflow.
- The action remains a thin CLI invoker.

**Risks**

- GitHub-specific assumptions.
- credential overreach.

---

## Phase 11 — OCI and production hardening

**Objective:** establish a strong reproducible execution boundary.

**Work**

- Minimal image.
- toolbox images.
- non-root runtime.
- read-only root.
- network none.
- signed images.
- SBOM.
- provenance.
- hostile-repository corpus.
- fuzzing.
- performance corpus.
- cross-platform release automation.

**Deliverables**

- Signed OCI images.
- release binaries.
- security report.
- benchmark report.
- reproducibility report.

**Tests**

- read-only mount.
- denied network.
- PID/memory limits.
- malicious analyzer.
- image signature verification.
- container/noncontainer result compatibility.

**Acceptance**

- Production release gates pass.
- High-assurance execution is available.
- Native and OCI runs produce compatible normalized evidence.

**Risks**

- Toolbox image growth.
- platform-specific profiler limitations.

### Milestone: Production-quality engine foundation

---

## Phase 12 — Octon Mini provider integration

**Objective:** allow Octon Mini to govern UCA without absorbing it.

**Work**

- Provider schemas.
- external-evidence-provider package.
- provider registry.
- provider run records.
- plan/run/resume commands.
- native and OCI provider backends.
- bundle validation.
- evidence registration.
- fixtures and golden path.

**Deliverables**

- Octon package.
- UCA provider manifest.
- cross-repository conformance suite.
- integration documentation.

**Tests**

- Trust decision.
- digest mismatch.
- stale revision.
- provider mutation.
- malformed bundle.
- partial audit.
- successful evidence reference.
- no UCA installation.

**Acceptance**

- Octon can govern an exact UCA invocation and reference its bundle.
- No UCA engine code exists in Octon.
- No finding becomes task or authority automatically.

**Risks**

- Provider contract becoming too general.
- duplication of UCA request semantics.

### Milestone: Production v1 ecosystem

---

## Phase 13 — Semantic analysis

**Objective:** add intent-level analysis without weakening evidence integrity.

**Work**

- Context builder.
- model-provider protocol.
- local provider.
- remote provider policy.
- semantic observation schema.
- prompt-injection protections.
- semantic duplication.
- de-abstraction.
- terminology analysis.
- human-review workflow.

**Deliverables**

- Optional semantic package.
- evaluation corpus.
- provider conformance tests.

**Tests**

- uncited claims.
- prompt injection.
- secrets.
- output variation.
- local-only mode.
- remote refusal.
- false semantic duplicates.

**Acceptance**

- AI evidence is always labeled and cited.
- AI-only findings never block.
- Evaluation demonstrates material incremental value.

**Risks**

- Noise.
- privacy.
- provider drift.
- perceived authority.

---

## Phase 14 — MCP interface

**Objective:** provide agent-native read-only access.

**Work**

- MCP server.
- stdio transport.
- tools/resources.
- pagination.
- task progress and cancellation.
- root validation.
- bundle references.
- protocol conformance.

**Deliverables**

- `uca-mcp`.
- MCP docs.
- client examples.

**Tests**

- tool schemas.
- root escape.
- cancellation.
- large results.
- concurrent clients.
- no mutation tools.

**Acceptance**

- MCP and CLI produce the same audit content identity for equivalent requests.
- MCP contains no independent analysis logic.

**Risks**

- Tool proliferation.
- protocol evolution.
- clients treating recommendations as commands.

---

## Phase 15 — Investigative runtime analysis

**Objective:** connect static and historical evidence to runtime causality.

**Work**

- pprof importer.
- OpenTelemetry importer.
- benchmark request schema.
- profiler adapters.
- database-plan adapters.
- allocation evidence.
- lock/contention evidence.
- performance comparison.
- workload identity.

**Deliverables**

- Runtime observation model.
- investigative workflows.
- profile-correlated findings.

**Tests**

- representative and unrepresentative workloads.
- profile merge.
- stale profile.
- benchmark noise.
- trace/source correlation.

**Acceptance**

- Performance recommendations state workload, baseline, confidence, and validation.
- No static suspicion is promoted to a confirmed bottleneck without runtime evidence.

**Risks**

- Environment dependence.
- benchmark misuse.
- large artifacts.

---

## Phase 16 — Optional hosted architecture

**Objective:** provide managed scale without weakening local-first operation.

**Work**

- HTTP API.
- durable queue.
- object store.
- worker images.
- tenancy.
- quotas.
- organization policies.
- shared caches.
- dashboards.
- remote provenance.
- billing/cost controls if commercialized.

**Deliverables**

- Hosted service.
- local/remote compatibility.
- organization trend reports.

**Tests**

- tenant isolation.
- cancellation.
- regional failure.
- cache isolation.
- source retention.
- worker compromise.
- API compatibility.

**Acceptance**

- Remote audits produce the same canonical bundle model.
- Local execution remains fully supported.
- Tenant security review passes.

**Risks**

- UCA becoming service-first.
- operational complexity.

---

# 28. Critical path and dependency map

```text
Phase 0: Invariants and threat model
       ↓
Phase 1: Evidence schemas and identities
       ↓
Phase 2: Engine and CLI skeleton
       ↓
Phase 3: Repository identity and discovery
       ↓
Phase 4: Planner, executor, sandbox, cache
       ↓
Phase 5: Native deterministic intelligence
       ↓
Phase 6: Adapter protocol
       ↓
Phase 7: Continuous audit, fingerprints, comparison
       ↓
Phase 9: Language usefulness
       ↓
Phase 11: Production hardening
       ↓
Production v1
```

Parallel branches after Phase 6:

```text
Phase 8   periodic analysis
Phase 10  CI
Phase 12  Octon integration
```

Post-production branches:

```text
Phase 13  semantic AI
Phase 14  MCP
Phase 15  runtime investigation
Phase 16  hosted service
```

The true critical path is:

> **Evidence contracts → exact repository identity → deterministic planning → constrained execution → normalized evidence → stable findings → comparison → production hardening.**

MCP, AI, and remote services are not on the critical path.

---

# 29. MVP, useful v1, production v1, and eventual product

## 29.1 Minimum Viable Architecture

The smallest non-throwaway proof includes:

- Rust workspace.
- Canonical CLI.
- Audit request/plan/bundle schemas.
- Repository identity.
- Scope.
- Discovery.
- Deterministic planner.
- DAG executor.
- Basic local sandbox/write detection.
- CAS.
- Git-history analysis.
- File/module graph.
- exact duplication.
- complexity × churn hotspots.
- stable finding fingerprints.
- bundle comparison.
- mock out-of-process adapter.
- JSON and Markdown reports.

Not required:

- CI Action.
- MCP.
- OCI.
- AI.
- deep SAST.
- hosted service.
- four language packs.

## 29.2 Useful v1

Adds:

- Generic SARIF, SBOM, coverage importers.
- Semgrep, OSV, and Syft adapters.
- Rust and Python stable packs.
- JS/TS and Go preview packs.
- Continuous and periodic modes.
- Architecture rules.
- SARIF output.
- baseline/ratchet.
- waivers.
- simplification findings.
- performance and determinism benchmarks.
- mature CLI docs.

## 29.3 Production v1

Adds:

- Cross-platform signed binaries.
- OCI minimal/toolbox images.
- hostile-repository hardening.
- fuzz testing.
- adapter compatibility matrix.
- GitHub Action.
- SBOM and provenance.
- stable schema and adapter protocol.
- support and compatibility policy.
- real-project validation.
- Octon external-provider integration.
- incident and vulnerability process.
- production-readiness gates.

MCP and AI need not block production v1.

## 29.4 Eventual product

Adds:

- MCP.
- semantic analysis.
- runtime investigative workflows.
- broader language/framework packs.
- commercial-tool adapters.
- remote execution.
- organization baselines.
- centralized trending.
- managed toolchains.
- optional hosted service.

---

# 30. Build-versus-integrate matrix

| Capability | Decision | Rationale |
|---|---|---|
| Repository identity | **Build in UCA** | Foundational reproducibility contract |
| Scope and exclusion | **Build in UCA** | Security and completeness boundary |
| Discovery | **Build in UCA** | Needed before tool selection |
| Audit planner | **Build in UCA** | Core differentiated orchestration |
| DAG executor | **Build in UCA** | Required for consistent interfaces |
| Cache/CAS | **Build in UCA** | Cross-tool reuse and reproducibility |
| Evidence model | **Build in UCA** | Primary product contract |
| Evidence normalization | **Build in UCA** | Main interoperability value |
| Evidence fusion | **Build in UCA** | Main differentiated capability |
| Finding identity | **Build in UCA** | Required for ratchets and trending |
| Priority model | **Build in UCA** | Transparent cross-signal decision support |
| Audit comparison | **Build in UCA** | Core continuous workflow |
| Git-history analysis | **Build in UCA** | Broadly applicable, manageable implementation |
| Basic graphs/SCC/centrality | **Build in UCA** | Universal repository intelligence |
| Exact clones | **Build in UCA** | Lightweight, universal |
| Near clones | **Build selectively** | Useful but language-sensitive |
| Semantic clones | **Adapter abstraction / later AI** | High complexity and uncertain precision |
| Deep SAST | **Integrate existing tools** | Mature external engines |
| Taint/data flow | **Integrate existing tools** | Avoid mega-analyzer |
| Compiler diagnostics | **Integrate native tools** | Language semantics belong to compiler |
| Vulnerability database | **Integrate OSV/vendor tools** | Requires continuously maintained intelligence |
| SBOM generation | **Integrate Syft/ecosystem tools** | Mature inventory technology |
| Coverage | **Import native formats** | Test runner owns execution |
| Mutation testing | **Adapter abstraction** | Ecosystem-specific and expensive |
| Property-based testing | **Adapter abstraction** | Test framework owns generation |
| Race detection | **Adapter abstraction** | Runtime/platform-specific |
| Fuzzing | **Adapter abstraction** | Toolchain-specific |
| CPU profiling | **Import/orchestrate existing profiler** | Do not build profiler |
| Memory profiling | **Import/orchestrate existing profiler** | Runtime-specific |
| Database query plans | **Adapter abstraction** | Vendor-specific |
| Architecture tests | **Import plus UCA rules** | UCA can own graph rules, not all bytecode engines |
| HTML reporting | **Build in UCA** | Bundle-native presentation |
| CI platform | **Thin integration** | CI owns scheduling and permissions |
| MCP | **Build thin interface** | Same engine; no separate logic |
| Container runtime | **Integrate OCI runtime** | Do not build sandbox runtime |
| Tool installer | **Defer/never automatic** | Trust and supply-chain risk |
| Automatic refactoring | **Defer** | Outside audit boundary |
| Hosted service | **Defer** | Not needed to prove product |
| AI model | **Provider abstraction** | Avoid provider lock-in |
| Agent harness | **Do not build** | Would violate product boundary |

---

# 31. Risk register

| Risk | Failure mode | Mitigation | Leading indicator |
|---|---|---|---|
| Product becomes too large | Every analyzer is reimplemented | Build-versus-integrate rule; architecture reviews | Core crate count/dependency growth without evidence value |
| Product becomes scanner aggregator | Little value beyond invoking tools | Invest in evidence graph, history, fusion, simplification | Reports merely concatenate tool output |
| Too slow | PR audits exceed tolerance | Tier budgets, incremental analysis, cache, resource scheduler | Continuous p95 rising |
| Too noisy | Teams ignore findings | Top-k limits, precision evaluation, stable maturity gates | Dismissal rate and waiver growth |
| Too tool-dependent | One tool change breaks audits | Adapter process boundary, version matrix, generic importers | Tool-specific code in core |
| Too AI-dependent | Product loses trust/offline function | AI optional/off by default; deterministic core complete | Core workflows require model |
| Configuration sprawl | Users cannot understand behavior | Small TOML model; no DSL; presets | Config fields grow faster than capabilities |
| Reproducibility erodes | Same audit produces different result | exact identities, JCS, lock, environment fingerprint | Determinism-test failures |
| Installation is difficult | Large runtimes and toolchains required | Native minimal binary; optional toolboxes | Setup abandonment |
| Security boundary fails | Malicious repo executes or escapes | no project execution default, sandbox, hostile corpus | Unexpected writes/network |
| Language bias | “Universal” means one ecosystem | capability matrix, generic evidence, language SDK | Findings dominated by one language |
| Octon coupling | UCA depends on Octon data model | provider contract by artifact/reference only | UCA core imports Octon concepts |
| Second control plane | UCA creates tasks/approvals/fixes | no authority/work mutation | Requests to add workflow lifecycle to UCA |
| Cache poisoning | Stale or incorrect evidence reused | content address, validation, producer identity | Unexplained cache-only discrepancies |
| Tool auto-install pressure | Unsafe convenience feature appears | explicit prohibition; OCI toolboxes | Install commands proposed inside audit |
| Semantic findings overtrusted | AI outputs treated as facts | separate evidence class, citation requirement | AI-only blocking policies |
| Giant toolbox image | Container becomes unmaintainable | family of small images | Image size and CVE count growth |
| Hosted service dominates | Local mode degrades | compatibility gate requires local execution | Features available only remotely |
| Taxonomy churn | Findings cannot trend | never reuse IDs; successors | High fingerprint/taxonomy migration rate |
| Suppression debt | Waivers become permanent | mandatory expiry and owner | Expired waiver backlog |
| Priority gaming | Teams lower scores instead of risk | preserve inputs; no global score | Changes targeting metric without validated benefit |
| Raw evidence leakage | CI artifacts expose secrets/source | sensitivity labels, redaction, restricted upload | Sensitive artifact incidents |
| Framework magic missed | False dead-code/security conclusions | declared blind spots; native adapters; runtime evidence | High invalidation rate in framework projects |
| Maintenance burden | Too many first-party adapters | maturity/ownership policy; community adapters | Unowned adapter count |

---

# 32. Production-readiness acceptance criteria

UCA is production-ready only when all applicable criteria pass.

## Architecture and contracts

1. One authoritative engine powers CLI and every released interface.
2. Bundle schemas are versioned and published.
3. Adapter protocol is stable.
4. Finding taxonomy is stable.
5. Product boundaries are documented.
6. No repository-mutation feature exists in the audit engine.
7. No automatic tool installation exists.

## Reproducibility and evidence

8. Canonical bundle identities are repeatable.
9. Dirty working trees are represented exactly.
10. Analyzer versions and configs are captured.
11. Partial analysis cannot report complete.
12. Every finding traces to evidence.
13. Raw and normalized evidence remain distinguishable.
14. Confidence components remain visible.
15. Stable fingerprints pass movement/rename fixtures.

## Security

16. Hostile-repository corpus passes.
17. No project execution occurs by default.
18. Network is denied by default.
19. Shell execution is absent.
20. Symlink and path-escape tests pass.
21. Analyzer output is size- and schema-bounded.
22. Secret values are redacted.
23. Signed binaries and images are published.
24. SBOM and provenance are published.
25. Vulnerability-disclosure process is active.

## Functional quality

26. Continuous audit meets the published precision target.
27. Periodic audit produces a bounded ranked result.
28. Required-capability failure is correctly represented.
29. Baseline and ratchet behavior passes.
30. Waiver expiry and scope pass.
31. Generic unsupported-language audit remains useful.
32. At least two language packs are stable.
33. At least three external adapters are stable.
34. SARIF projection passes GitHub ingestion tests.

## Performance and portability

35. Reference performance targets pass.
36. Memory ceilings pass.
37. Linux, macOS, and Windows releases pass.
38. Cold and warm cache tests pass.
39. Large repository tests pass.
40. Cancellation reliably kills subprocess trees.

## Operations and support

41. Upgrade and migration paths are documented.
42. Release artifacts are reproducible or deviations are explained.
43. Compatibility policy is published.
44. Troubleshooting documentation is complete.
45. Real-project validation has been performed.
46. Adapter ownership is assigned.
47. Security and benchmark gates are automated.
48. No critical open false-positive regression exists in default gates.

## Octon integration

49. Provider package is content-addressed.
50. Provider trust and adoption are separate.
51. Octon does not install UCA.
52. Octon validates the UCA bundle digest and revision.
53. UCA findings do not become tasks automatically.
54. Native provider mutation is detected.
55. OCI provider mode passes.
56. Partial and stale audit outcomes are preserved truthfully.

---

# 33. Prioritized implementation backlog

## P0 — Architectural kernel

1. Ratify product charter.
2. Ratify invariants.
3. Complete threat model.
4. Create Rust workspace.
5. Define schema catalog.
6. Implement duplicate-key-rejecting JSON loader.
7. Implement JCS canonicalization.
8. Implement content identities.
9. Define audit request.
10. Define repository identity.
11. Define scope.
12. Define audit plan.
13. Define analyzer run.
14. Define observation envelope.
15. Define finding.
16. Define completion.
17. Define comparison.
18. Implement atomic bundle writer.
19. Implement engine trait.
20. Implement CLI skeleton.
21. Implement stable exit codes.
22. Implement structured progress.
23. Build schema conformance suite.
24. Build deterministic bundle tests.
25. Build hostile path/symlink fixtures.

## P1 — Repository and execution foundation

26. Implement Git repository identity.
27. Implement dirty worktree manifest.
28. Implement file inventory.
29. Implement generated/vendor/test classification.
30. Implement language detection.
31. Implement manifest detection.
32. Implement capability catalog.
33. Implement deterministic planner.
34. Implement DAG scheduler.
35. Implement direct-argv runner.
36. Implement sanitized environment.
37. Implement process-group cancellation.
38. Implement timeout/output limits.
39. Implement repository write detection.
40. Implement local CAS.
41. Implement SQLite cache index.
42. Implement cache verification/quarantine.
43. Implement task-completion semantics.
44. Implement provenance recording.
45. Publish first benchmark corpus.

## P2 — Native audit intelligence

46. Git churn analysis.
47. Contributor/ownership concentration.
48. Revert analysis.
49. Co-change graph.
50. File/module dependency graph.
51. SCC and cycle analysis.
52. Centrality.
53. Exact clone detection.
54. File metrics.
55. Complexity × churn.
56. Hotspot finding taxonomy.
57. Stable fingerprinting.
58. Baseline comparison.
59. Markdown summary.
60. JSONL finding output.

## P3 — Adapter and useful-v1 capabilities

61. Adapter manifest.
62. Adapter protocol.
63. Adapter SDK.
64. Mock adapter.
65. Generic SARIF importer.
66. Generic CycloneDX importer.
67. Generic SPDX importer.
68. Generic coverage importer.
69. Semgrep adapter.
70. OSV adapter.
71. Syft adapter.
72. Rust pack.
73. Python pack.
74. Architecture-rule evaluator.
75. Continuous default policy.
76. Periodic default policy.
77. SARIF projection.
78. Waiver evaluator.
79. Transparent priority model.
80. Adapter compatibility matrix.

## P4 — Production ecosystem

81. JS/TS pack.
82. Go pack.
83. GitHub setup action.
84. GitHub audit action.
85. Generic CI examples.
86. Minimal OCI image.
87. Security toolbox image.
88. Release signing.
89. Release SBOM.
90. SLSA provenance.
91. Cross-platform packaging.
92. Hostile-repository fuzzing.
93. Real-project validation.
94. Octon provider schemas.
95. Octon workflow package.
96. Octon provider fixtures.
97. Production docs.
98. Compatibility/migration tests.
99. Production release candidate.
100. Production-readiness review.

## P5 — Eventual capabilities

101. Semantic context builder.
102. Local model provider.
103. Remote model provider.
104. Semantic duplication.
105. De-abstraction analysis.
106. MCP server.
107. MCP task/progress support.
108. pprof importer.
109. OpenTelemetry importer.
110. Investigative benchmark workflows.
111. database-plan adapters.
112. race/fuzz adapters.
113. HTTP service.
114. durable queue.
115. organization trending.

---

# 34. Concise start-here sequence

The first implementation work should occur in this exact order:

1. **Create the UCA repository and Rust workspace.**
2. **Commit the product charter, invariants, responsibility matrix, and threat model before analysis code.**
3. **Define `uca.audit-request.v1`, `uca.repository-identity.v1`, `uca.scope.v1`, `uca.audit-plan.v1`, `uca.observation.v1`, `uca.finding.v1`, and `uca.audit-completion.v1`.**
4. **Implement duplicate-key rejection, JCS canonicalization, SHA-256 identities, and schema validation.**
5. **Build an atomic UCA Audit Bundle writer and determinism test suite.**
6. **Implement a no-op authoritative engine and the `uca discover`, `uca plan`, `uca audit`, and `uca compare` CLI paths.**
7. **Implement exact repository identity, working-tree overlays, safe path handling, and scope classification.**
8. **Implement the deterministic planner, task DAG, constrained process runner, cancellation, and partial-completion semantics.**
9. **Implement the content-addressed cache and SQLite index.**
10. **Add Git-history mining, file/module graphs, SCC detection, exact duplication, and complexity × churn hotspots.**
11. **Implement stable finding fingerprints and baseline comparison.**
12. **Create a mock out-of-process adapter and prove that the core has no adapter-specific dependency.**
13. **Add generic SARIF, CycloneDX/SPDX, and coverage importers.**
14. **Add Semgrep, OSV, and Syft as the first real adapters.**
15. **Release the Minimum Viable Architecture only after deterministic bundle and hostile-repository tests pass.**
16. **Add continuous-audit policy, SARIF projection, Rust/Python language packs, and real-project evaluation.**
17. **Harden and package the production CLI and OCI image.**
18. **Only then add CI and the Octon external-provider package.**
19. **Add AI and MCP after the deterministic production foundation is established.**
20. **Defer hosted execution until local UCA has demonstrated sustained usefulness, stable evidence contracts, and acceptable false-positive burden.**

The governing implementation rule throughout should remain:

> **UCA owns the audit method, evidence contracts, cross-signal intelligence, and decision-support output. It integrates specialist analyzers, remains independently usable, grants no authority, performs no initial repository mutation, and reaches Octon Mini only through a narrow, content-addressed, read-only evidence-provider boundary.**

---

## Turn 007

**Role:** User  
**Date/time:** Not available

# Research Inquiry — Agent-Skill Patterns Worth Borrowing for Universal Code Audit

Act as an independent **developer-tools architect, agent-systems architect, code-quality researcher, software-maintainability specialist, prompt/skill architect, and evidence-led technical researcher**.

## Objective

Investigate whether there are concepts, mechanisms, workflows, interaction patterns, evaluation methods, packaging strategies, or individual skill capabilities from **Ponytail** and other high-quality agent skills that should materially improve the **Universal Code Audit (UCA) skill and its surrounding agent-facing experience**.

Begin with:

**Ponytail:**
https://github.com/DietrichGebert/ponytail

Then conduct a broader search for other relevant agent skills, coding-agent plugins, review skills, audit skills, simplification skills, refactoring skills, architecture-review skills, security-review skills, testing skills, repository-analysis skills, and adjacent agent workflows.

The goal is **not** to copy Ponytail wholesale, merge arbitrary skills together, or expand UCA for the sake of feature count.

The goal is:

> **Identify the highest-value transferable mechanisms that would make Universal Code Audit more effective, precise, actionable, understandable, portable, evidence-led, and useful to coding agents—without weakening UCA's architecture or turning it into an oversized collection of prompts and scanner behaviors.**

Optimize for **capability-to-weight ratio**.

---

# 1. Preserve the Established UCA Architecture

Use the established Universal Code Audit architectural direction as the governing constraint.

UCA is intended to become an **independent, separately versioned audit engine** with:

* a canonical CLI;
* CI integration;
* an MCP surface;
* OCI/containerized execution;
* potentially a future hosted service;
* a durable UCA Audit Bundle;
* external analyzer adapters;
* deterministic repository/history/graph intelligence;
* evidence normalization and fusion;
* stable findings;
* transparent prioritization;
* optional semantic/AI interpretation; and
* a thin external-provider integration with Octon Mini.

Preserve these principles:

* UCA must remain independently usable without Octon Mini.
* Octon Mini must not contain UCA's implementation.
* UCA must not become a second governance or agent-control plane.
* Audit results are **evidence and recommendations, not authority**.
* Repository mutation and automatic refactoring are outside the initial audit boundary.
* CLI, CI, MCP, container, and HTTP surfaces must use one authoritative engine.
* Specialized analysis should normally be delegated to mature external tools rather than reimplemented unnecessarily.
* Deterministic, heuristic, runtime, historical, human-supplied, and AI-derived evidence must remain distinguishable.
* Partial analysis must never masquerade as complete analysis.
* UCA should prefer deletion, simplification, de-abstraction, reuse, and reduction when evidence supports them.
* UCA must avoid metric gaming and opaque code-quality scores.
* UCA should remain local-first and read-only by default.

When evaluating agent skills, distinguish carefully between:

1. **ideas that belong in the UCA engine;**
2. **ideas that belong in the UCA agent skill/interface;**
3. **ideas that belong in external adapters;**
4. **ideas that belong in CI/MCP/container integration;**
5. **ideas that UCA already handles more rigorously;**
6. **ideas that should not be adopted.**

Do not let a useful skill-level idea distort the product architecture.

---

# 2. Deeply Analyze Ponytail

Do not review only Ponytail's README or only `ponytail-audit`.

Inspect the current repository and relevant implementation material, including where applicable:

* root instructions;
* `ponytail`;
* `ponytail-review`;
* `ponytail-audit`;
* `ponytail-debt`;
* `ponytail-gain`;
* help/onboarding behavior;
* activation modes or levels;
* lifecycle hooks;
* portability layers;
* agent-specific integrations;
* tests;
* benchmarks;
* benchmark methodology;
* examples;
* documentation;
* packaging/distribution;
* plugin manifests;
* installation paths;
* portability guidance;
* release history and notable design discussions/issues where useful.

Determine what Ponytail is actually doing rather than relying on its marketing language.

Pay particular attention to mechanisms such as:

### Simplicity ladder

Ponytail appears to reason progressively through questions such as:

1. Does this need to exist?
2. Does the repository already provide it?
3. Does the standard library provide it?
4. Does the native platform provide it?
5. Does an existing dependency provide it?
6. Can the need be satisfied substantially more simply?
7. Only then should new machinery be introduced.

Determine whether UCA should adopt, adapt, broaden, formalize, or reject this pattern.

Consider whether UCA needs a generalized **Reduction Ladder** such as:

```text
remove
→ reuse existing project capability
→ use language/runtime standard library
→ use native platform capability
→ use already-adopted dependency
→ collapse unnecessary abstraction
→ consolidate duplicated knowledge
→ simplify implementation
→ introduce new abstraction/dependency only when evidence warrants it
```

Determine whether such a ladder should affect:

* candidate generation;
* recommendation generation;
* prioritization;
* semantic analysis;
* simplification audits;
* agent-facing explanations; or
* all of the above.

### Finding taxonomy

Examine Ponytail's concise categories such as:

* `delete`
* `stdlib`
* `native`
* `yagni`
* `shrink`

Determine whether these encode a useful **simplification sub-taxonomy** for UCA.

Do not assume these names or their current semantics are sufficient. Determine whether UCA needs a richer but still compact model such as:

```text
delete
reuse
stdlib
native
dependency-reuse
dependency-remove
de-abstract
consolidate
inline
collapse-layer
remove-config
remove-state
remove-compatibility
simplify
investigate
```

Explain which distinctions are genuinely useful and which would create taxonomy noise.

### Narrow audit scopes

Ponytail deliberately separates over-engineering review from correctness, security, and performance analysis.

Assess whether UCA could benefit from similarly explicit **audit lenses** or **focused passes**, for example:

* simplification;
* architecture;
* dependency health;
* testing;
* reliability;
* security;
* performance;
* dead weight;
* API/domain modeling;
* state/concurrency;
* full-spectrum audit.

Determine when focus improves precision and when separate passes would fragment evidence that UCA should instead fuse.

### Read-only behavior

Ponytail's audit and review capabilities identify opportunities without applying them.

Compare this with UCA's evidence-not-authority and read-only boundaries.

Determine whether there are useful interaction patterns worth adopting.

### Safety floor

Ponytail explicitly distinguishes "simpler" from "negligent" and avoids removing validation, security, accessibility, data-loss protection, and other necessary safeguards merely to reduce code.

Determine how UCA should formalize a **non-reducible safety/correctness floor** so that simplification analysis cannot mistake essential complexity for accidental complexity.

### Debt/revisit triggers

Analyze Ponytail's approach to deliberate shortcuts or deferred work, especially the idea that a simplification or compromise should name:

* its current ceiling;
* what limitation has been consciously accepted; and
* the concrete trigger that should cause reconsideration.

Determine whether UCA should support concepts such as:

* temporary simplification ceilings;
* reconsideration triggers;
* expiration conditions;
* evidence-driven debt reopening;
* obsolete compatibility triggers;
* feature-flag retirement triggers;
* dependency-removal triggers;
* abstraction-introduction triggers.

Compare this with UCA's existing waiver/accepted-debt model.

### Ranking and concise output

Ponytail strongly favors ranking by the largest useful reduction first and producing terse findings.

Determine whether UCA should provide a dedicated **simplification view** that optimizes for something like:

> highest-value removable conceptual or implementation weight first

without reducing priority to raw lines-of-code savings.

Investigate better measures such as:

* authored code removed;
* dependency removed;
* state eliminated;
* configuration eliminated;
* API surface eliminated;
* abstraction/layer eliminated;
* build step eliminated;
* deployment unit eliminated;
* duplicated rule consolidated;
* concepts a maintainer no longer needs to understand.

### Benchmarking and honesty boundaries

Study Ponytail's benchmark methodology, controls, limitations, corrections, and distinction between measured benchmark savings and unsupported per-repository claims.

Determine what UCA should learn about:

* skill evaluation;
* controlled comparisons;
* real-agent sessions;
* task corpora;
* safety-preservation testing;
* false-positive measurement;
* baseline selection;
* reproducibility;
* avoiding exaggerated claims;
* reporting limitations when a counterfactual cannot actually be measured.

### Portability

Ponytail supports many agent environments through a combination of skills, root instructions, lifecycle hooks, plugin formats, and platform adapters.

Determine what UCA should learn about making its **agent-facing skill layer portable** across environments such as:

* Codex;
* Claude Code;
* GitHub Copilot;
* Gemini/Antigravity;
* OpenCode;
* other skill-aware coding agents;
* MCP clients.

Do not assume UCA should reproduce Ponytail's portability implementation. Identify the **minimal canonical source + generated/platform-adapter** architecture that would avoid maintaining many divergent skill copies.

---

# 3. Determine What UCA Already Does Better

Do not treat Ponytail as automatically superior because it is focused and elegant.

For each relevant Ponytail mechanism, compare it with the existing Universal Code Audit methodology and architecture.

Classify every candidate as:

* **Already satisfied by UCA**
* **Worth adopting substantially as-is**
* **Worth adapting**
* **Worth borrowing only as a design principle**
* **Useful only for the UCA agent skill**
* **Useful only for the UCA engine**
* **Useful only for evaluation/tooling**
* **Conflicts with UCA architecture**
* **Too narrow for UCA**
* **Insufficiently evidence-backed**
* **Not worth adopting**

Explicitly identify cases where UCA's evidence model, history analysis, graph intelligence, runtime evidence, confidence model, or governance boundaries are materially stronger and should not be simplified merely to resemble another skill.

---

# 4. Search for Other Strong Agent Skills

After analyzing Ponytail, conduct a broad current search for other agent skills or agent-oriented workflows whose mechanisms could materially improve UCA.

Search primary sources such as:

* GitHub repositories;
* actual `SKILL.md` files;
* agent plugin repositories;
* Claude Code skills/plugins;
* Codex skills/plugins;
* MCP-based coding tools;
* agent instruction repositories;
* coding-agent review workflows;
* security-review skills;
* architecture-review skills;
* testing and debugging skills;
* simplification/refactoring skills;
* codebase exploration skills;
* repository-analysis skills;
* dependency-analysis skills;
* performance-investigation skills;
* dead-code or cleanup skills.

Do not optimize for popularity alone.

Prefer skills that demonstrate one or more of:

* a novel and transferable mechanism;
* strong workflow design;
* unusually good scope control;
* useful evidence handling;
* precise output;
* good false-positive control;
* strong safety boundaries;
* good progressive disclosure;
* effective repository exploration;
* meaningful evaluation;
* portability;
* composability;
* agent efficiency;
* human-review ergonomics.

Search broadly enough to identify both obvious and non-obvious references.

---

# 5. Analyze Similar Skills by Mechanism, Not Branding

For each strong candidate, identify the actual transferable mechanism.

Potential areas include:

### Repository assimilation

* How does the skill determine what to read?
* Does it inspect architecture before judging code?
* Does it bound context intelligently?
* Does it identify generated/vendor/test code?
* Does it understand change scope versus repository scope?

### Audit decomposition

* Does it use phases?
* Does it separate deterministic discovery from judgment?
* Does it run specialized reviewers or lenses?
* Does it escalate only when evidence warrants deeper analysis?

### Evidence discipline

* Does it cite exact files/lines/symbols?
* Does it distinguish observation from inference?
* Does it require reproducible evidence?
* Does it record uncertainty?
* Does it explicitly admit missing evidence?

### Finding quality

* Are findings concise?
* Are they ranked?
* Do they explain consequence?
* Do they provide a concrete replacement?
* Do they distinguish remediation from investigation?
* Are duplicate or recurring findings consolidated?

### Simplification

* Does it identify deletion before refactoring?
* Does it detect unnecessary dependencies?
* Does it question speculative abstraction?
* Does it find duplicate state/configuration?
* Does it identify platform/stdlib reuse?
* Does it reason about conceptual complexity rather than LOC alone?

### Tool usage

* Does it use native compilers, linters, test systems, profilers, or analyzers effectively?
* Does it avoid recreating mature tooling?
* Does it choose tools conditionally from repository evidence?

### Context efficiency

* How does it avoid reading an entire large repository indiscriminately?
* Does it construct targeted context?
* Does it progressively widen scope?
* Does it reuse prior evidence?

### Multi-agent decomposition

* Does it use specialist subagents effectively?
* Are roles actually useful or merely ceremonial?
* How are findings reconciled?
* Is duplicate analysis controlled?
* Does it preserve one final evidence model?

### Safety and authority

* Does the skill separate recommendations from actions?
* Are potentially dangerous commands explicitly gated?
* Can the skill silently install dependencies or execute project code?
* Does it treat repository content as untrusted?

### Evaluation

* Are there benchmarks?
* Ground-truth repositories?
* precision measurements?
* regression fixtures?
* safety tests?
* reproducibility tests?
* adversarial cases?

### Portability and packaging

* Is there one canonical skill source?
* How are platform variants generated?
* Are hooks optional?
* Can the behavior work through MCP?
* Is installation lightweight?

---

# 6. Search Beyond Direct Code-Audit Skills

Do not limit the investigation to projects explicitly called "code audit."

Relevant mechanisms may come from skills for:

* code review;
* debugging;
* root-cause analysis;
* repository exploration;
* architecture recovery;
* security review;
* performance profiling;
* test generation;
* mutation testing;
* planning;
* specification conformance;
* dead-code cleanup;
* dependency modernization;
* documentation validation;
* code simplification;
* refactoring;
* change-impact analysis;
* incident investigation.

A skill does not need to resemble UCA as a whole to contain one mechanism worth borrowing.

---

# 7. Distinguish the UCA Engine From the UCA Skill

Treat this distinction as important.

The **UCA engine** should remain responsible for durable, reproducible capabilities such as:

* repository identity;
* discovery;
* audit planning;
* deterministic analysis;
* tool adapters;
* history;
* dependency graphs;
* evidence normalization;
* evidence fusion;
* stable findings;
* comparison;
* provenance;
* prioritization;
* UCA Audit Bundles.

The **UCA agent skill** should primarily teach an agent:

* when UCA should be used;
* which audit mode or lens is appropriate;
* how to scope an audit;
* how to invoke the canonical UCA interface;
* how to inspect and interpret the resulting evidence;
* when to escalate from continuous to periodic or investigative analysis;
* when additional repository reading is warranted;
* how to distinguish evidence from interpretation;
* how to present findings;
* how to avoid acting on recommendations without appropriate authority;
* how to hand findings into normal project work.

Do not duplicate substantial engine logic inside the skill instructions.

If another skill contains an excellent reasoning mechanism, determine whether it should become:

1. UCA engine logic;
2. UCA semantic-analysis policy;
3. UCA finding taxonomy;
4. UCA skill instructions;
5. UCA reporting behavior;
6. UCA evaluation methodology;
7. or remain external inspiration only.

---

# 8. Investigate Whether UCA Needs Focused Agent Skills

Assess whether a single "Universal Code Audit" skill is sufficient or whether a very small family of narrowly scoped entry skills would improve usability.

For example, investigate—not assume—the value of:

```text
uca-audit
uca-review
uca-simplify
uca-investigate
uca-explain
uca-compare
```

Potential meanings might be:

* `uca-review` — changed-code audit;
* `uca-audit` — repository-wide audit;
* `uca-simplify` — deletion/de-abstraction/reduction lens;
* `uca-investigate` — evidence-triggered deep analysis;
* `uca-explain` — inspect one finding and its evidence;
* `uca-compare` — compare audit baselines.

Determine whether this helps discoverability and precision or merely creates redundant skill surface.

Prefer fewer concepts unless separation produces a real behavioral advantage.

---

# 9. Examine the Potential for a UCA Reduction/Simplification Lens

Give special attention to whether Ponytail exposes a weakness or missing emphasis in Universal Code Audit.

UCA already considers:

* dead code;
* unnecessary dependencies;
* duplication;
* excessive abstraction;
* configuration burden;
* migration scaffolding;
* compatibility residue;
* excessive state;
* unnecessary layers;
* conceptual complexity.

Determine whether these should be unified into an explicit first-class **Reduction / Simplification lens**.

Such a lens should answer:

> **What code, dependencies, state, configuration, abstractions, layers, processes, or concepts can this system safely stop carrying?**

Potential recommendation ladder:

```text
1. Remove the behavior entirely.
2. Reuse something already present.
3. Use the standard library.
4. Use a native platform capability.
5. Reuse an already-adopted dependency.
6. Consolidate duplicated knowledge.
7. Remove unnecessary state/configuration.
8. Collapse a pass-through layer.
9. Inline an abstraction that has no demonstrated independent role.
10. Simplify the implementation.
11. Preserve the current design when complexity is justified.
12. Add new machinery only when evidence demonstrates the need.
```

Evaluate this rigorously.

Do not turn UCA into a code-golfing system.

Necessary complexity for:

* correctness;
* safety;
* security;
* accessibility;
* resilience;
* compatibility;
* observability;
* performance;
* regulatory requirements;
* legitimate future variability already supported by evidence

must not be treated as waste merely because it costs lines or concepts.

---

# 10. Evaluate Skill-Level Output Design

Determine whether UCA's agent-facing reports should support a concise high-signal presentation inspired by strong skill designs.

For example:

```text
P1 · de-abstract
PaymentProvider interface has one implementation, changes with it, and
provides no independent test/security/runtime boundary.
Replace: use StripePaymentProvider directly.
Evidence: ARCH-17, HIST-42, CALLGRAPH-8
Expected reduction: 3 files, 1 interface, 2 factories
Risk: medium
Validate: contract tests + API compatibility
```

Compare this with:

* full UCA findings;
* terse CLI summaries;
* SARIF;
* human reports;
* MCP result presentation.

Determine the right level of progressive disclosure.

---

# 11. Evaluate Borrowing Versus Reimplementing

For every proposed borrowed capability, ask:

1. Does UCA already have this?
2. Would adopting it materially improve outcomes?
3. Does it belong in the agent skill or engine?
4. Can it be represented as a small policy/rule rather than new machinery?
5. Would it create duplicate analysis?
6. Would it weaken evidence requirements?
7. Would it increase false positives?
8. Would it increase installation or maintenance weight?
9. Would it make UCA more dependent on a particular agent platform?
10. Would it conflict with local-first/read-only operation?
11. Can the improvement be independently tested?
12. What measurable benefit should result?

Reject attractive ideas whose complexity exceeds their likely value.

---

# 12. Licensing and Intellectual-Property Boundary

Inspect the license of every reference.

Distinguish:

* a general idea or architectural pattern;
* a workflow concept;
* an interface pattern;
* directly reusable code;
* directly reusable text;
* benchmark assets;
* tests;
* configuration.

Do not recommend copying source or skill text without confirming licensing and attribution requirements.

Prefer independently implementing useful mechanisms rather than creating unnecessary source-level coupling.

---

# 13. Evidence and Research Standard

Use current primary sources wherever possible.

For each important candidate:

* inspect the actual repository;
* inspect the actual skill/instructions;
* inspect relevant code;
* inspect tests;
* inspect benchmark methodology if present;
* inspect documentation;
* inspect significant issues/discussions when they illuminate design rationale;
* note maintenance/activity status;
* note licensing;
* distinguish measured evidence from project claims.

Do not rely on README marketing claims alone.

When a claimed advantage is unsupported, say so.

---

# 14. Comparative Evaluation Framework

Evaluate each transferable mechanism against:

| Dimension         | Question                                                       |
| ----------------- | -------------------------------------------------------------- |
| Audit value       | Does it help identify consequential improvement opportunities? |
| Precision         | Is it likely to reduce rather than increase noise?             |
| Evidence quality  | Can conclusions be grounded in observable evidence?            |
| Generality        | Does it work across languages/projects?                        |
| Complementarity   | Does it add something UCA does not already do well?            |
| Architectural fit | Does it preserve UCA's established boundaries?                 |
| Weight            | How much implementation/configuration/maintenance does it add? |
| Portability       | Does it work across agents/interfaces?                         |
| Reproducibility   | Can behavior be tested and repeated?                           |
| Safety            | Does it preserve read-only/non-authorizing boundaries?         |
| Explainability    | Can a developer understand why the finding exists?             |
| Actionability     | Does it lead to a concrete next step?                          |
| Evaluation        | Can improvement be measured?                                   |

Use qualitative ratings rather than pretending to have scientifically precise scores.

---

# 15. Required Classification for Every Candidate

Classify each candidate mechanism as one of:

### Adopt

Strong fit, high value, low unnecessary weight.

### Adapt

Valuable, but UCA needs a more rigorous/general version.

### Already Covered

UCA already handles the concern adequately.

### Reference Only

Useful design inspiration but not worth productizing.

### Defer

Potentially useful after stronger evidence or later maturity.

### Reject

Conflicts with UCA architecture, adds more complexity than value, or weakens evidence/safety.

For `Adopt` and `Adapt`, specify exactly:

* where it belongs;
* what contract or module changes;
* what behavior changes;
* how it is tested;
* how success is measured;
* what must explicitly not be imported.

---

# 16. Final Deliverables

Produce the following.

## A. Ponytail assessment

A concise but implementation-oriented answer to:

> **What should Universal Code Audit borrow from Ponytail, if anything?**

Include a mechanism-by-mechanism table with:

* Ponytail mechanism;
* how it works;
* evidence of usefulness;
* overlap with UCA;
* classification;
* proposed UCA adaptation;
* implementation weight;
* risks.

## B. Strongest other references

Identify the **best comparable or complementary agent skills** discovered.

For each:

* repository/source;
* purpose;
* strongest mechanism;
* what UCA could learn;
* what UCA should not copy;
* maturity/evidence;
* licensing;
* recommendation.

Do not produce a giant catalog. Focus on the strongest references.

## C. Transferable-pattern ranking

Rank the **10–20 strongest mechanisms** across all sources by:

1. expected improvement to UCA;
2. evidence quality;
3. architectural fit;
4. capability-to-weight ratio.

## D. UCA gap analysis

Identify areas where the research reveals that UCA currently:

* lacks a capability;
* has the capability but underemphasizes it;
* has an overly complex mechanism;
* needs a better interaction model;
* needs stronger evaluation;
* needs stronger skill portability;
* already has the superior approach.

## E. Proposed UCA skill architecture

Recommend the ideal agent-facing skill design, including:

* trigger description;
* scope;
* workflow;
* audit-mode selection;
* focused lenses;
* UCA CLI/MCP invocation;
* evidence inspection;
* escalation;
* output format;
* safety/authority boundaries;
* completion behavior.

If multiple skills are justified, show the smallest useful family and explain why.

## F. Proposed simplification/reduction model

Determine whether UCA should adopt a first-class Reduction/Simplification lens and, if so, define:

* taxonomy;
* decision ladder;
* evidence requirements;
* prioritization;
* safety floors;
* validation requirements;
* output.

## G. Evaluation improvements

Recommend what UCA should borrow from strong agent-skill evaluation practices, including:

* benchmark design;
* controls;
* real-repository tasks;
* precision;
* false-positive burden;
* safety preservation;
* time-to-useful-finding;
* developer acceptance;
* reproducibility;
* simplification yield.

## H. Portability architecture

Recommend how the UCA skill should remain portable across coding-agent ecosystems without maintaining divergent behavior in many copies.

Prefer:

> **one canonical skill specification → thin generated/platform-specific adapters**

when supported by the evidence.

## I. Concrete change proposals

For every recommended improvement, provide:

```text
Proposal
Why
Source inspiration
UCA layer affected
Expected benefit
Implementation cost
Risk
Validation
Priority
```

## J. Final decision packet

Finish with four sections:

### Adopt now

High-value, well-supported improvements suitable for immediate implementation.

### Adapt carefully

Promising mechanisms needing a UCA-specific design.

### Revisit later

Ideas worth retaining but not yet justified.

### Do not adopt

Patterns that would weaken UCA, duplicate mature functionality, increase noise, create platform coupling, or undermine its evidence-led architecture.

---

# Governing Question

The investigation should ultimately answer:

> **What can Universal Code Audit learn from the best agent skills—including Ponytail—that would make its agent-facing auditing capability materially better, while preserving UCA as an independent, evidence-led, read-only, tool-integrating audit system rather than turning it into a collection of clever prompts?**

Favor a small number of strongly justified improvements over broad feature accumulation.

---

## Turn 008

**Role:** Assistant  
**Date/time:** Not available

# Universal Code Audit — Agent-Skill Pattern Research and Decision Packet

## Executive decision

Universal Code Audit should borrow **a small set of workflow mechanisms**, not Ponytail’s product structure or prompt corpus.

The strongest improvements are:

1. A first-class **Reduction / Simplification lens** governed by an explicit safety floor.
2. A formal **candidate → validation/refutation → finding** lifecycle for heuristic and AI-derived concerns.
3. A **completion-truth gate** that forces agents to inspect UCA’s completion state, scope, analyzer coverage, freshness, and limitations before claiming an audit is complete or clean.
4. A deterministic, graph-guided **context projection** for agent interpretation rather than indiscriminate repository reading.
5. **Reconsideration triggers** attached to accepted debt, compatibility residue, feature flags, retained abstractions, and deferred dependency work.
6. Concise, progressive **finding cards** backed by full Audit Bundle evidence.
7. A proper **agent-skill evaluation harness** with no-skill controls, routing tests, pressure cases, behavioral fixtures, multi-run variance, and safety-preservation checks.
8. One canonical Agent Skills–compatible source that produces **thin generated platform adapters**, with drift and conformance tests.

UCA should **not** adopt:

- an always-on behavioral mode;
- hooks that repeatedly inject audit rules into every agent turn;
- repository mutation to protect or simplify code;
- a flat five-tag taxonomy as the canonical finding model;
- line-count reduction as the main measure of value;
- prompt-only auditing in place of the engine;
- mandatory multi-agent orchestration;
- hand-maintained copies for every agent platform;
- automatic refactoring or dependency installation.

The ideal agent-facing product is initially a family of only **two skills**:

```text
uca-audit
uca-simplify
```

`uca-audit` should route changed-code review, repository-wide auditing, investigation, explanation, and comparison. `uca-simplify` deserves a separate entry because reduction requests require a distinct decision ladder, safety-floor check, and output ordering. `review`, `investigate`, `explain`, and `compare` should remain engine modes and CLI/MCP operations unless routing evaluation later proves that separate skills materially improve discovery.

---

# Research basis and limitations

This assessment inspected current repository content, skill instructions, implementation code, hooks, portability layers, tests, benchmark harnesses, benchmark reports, and relevant issue discussions from:

- Ponytail.
- Trail of Bits Skills.
- Cloudflare Security Audit Skill.
- Meta’s SecPriv Skill.
- Aider’s repository-map implementation.
- Superpowers.
- Common Code Reviewer.
- The Agent Skills specification and Anthropic examples.
- Addy Osmani’s Agent Skills repository.

The conclusions distinguish:

- repository-observed implementation;
- project-reported benchmark outcomes;
- mechanisms inferred from implementation;
- independent architectural recommendations for UCA.

I did not independently rerun every external benchmark. That matters particularly for agent evaluations, which are model-, harness-, task-, and environment-sensitive.

Ponytail itself illustrates why this qualification is necessary. Its original benchmark presentation was later corrected after baseline contamination and excessive baseline verbosity were identified. Its later agentic benchmark improved the controls but still disclosed a single tested model and a small number of runs. Independent issue discussion also showed that lower generated-code volume can coexist with additional agent turns, tool calls, or token costs. Those are useful results, but not universal effect sizes.

---

# 1. Governing architectural placement

The research produced mechanisms that belong at different levels. They should not all become skill prose.

| Mechanism | Correct UCA placement |
|---|---|
| Reduction decision ladder | Engine simplification policy plus `uca-simplify` explanation |
| Safety/correctness floor | Engine cross-check contract plus skill guardrail |
| Concise simplification labels | Report projection and agent finding cards |
| Focused audit lenses | Audit-plan and report-view configuration |
| Candidate validation/refutation | Evidence and finding engine |
| Rejected-candidate retention | Audit Bundle evidence model |
| Graph-ranked context | Engine context-projection service |
| Completion truthfulness | Completion schema, CLI/MCP, and skill workflow |
| Reconsideration triggers | Waiver/accepted-debt schema and periodic evaluator |
| Trigger-routing tests | Skill evaluation tooling |
| Platform portability | Generated skill/plugin adapters |
| Native/standard-library alternatives | Language packs or evidence-backed adapters |
| Root-cause-derived variant search | Investigative engine workflow and analyzer adapters |
| Independent semantic verification | Optional semantic-analysis policy |
| Multi-agent decomposition | Optional execution strategy, not canonical architecture |
| Repeated rule injection and activation modes | Reject for UCA |
| Auto-simplification | Outside initial UCA boundary |
| Prompt-only MCP audit | Reject; MCP must expose the authoritative engine |

This distinction is the central conclusion of the research:

> The best agent skills contribute **failure-resistant interaction protocols around UCA**, while durable repository intelligence remains in the engine.

---

# A. Ponytail assessment

## What Ponytail actually is

Ponytail is not merely one simplification prompt. Its current repository contains:

- a core simplification skill;
- changed-code review;
- repository-wide audit;
- deliberate-debt extraction;
- a benchmark-gain view;
- onboarding/help;
- persistent activation and intensity modes;
- lifecycle hooks;
- subagent reinjection;
- numerous host integrations;
- an MCP prompt/tool surface;
- deterministic tests;
- agentic benchmark infrastructure;
- generated platform packages.

The core simplification skill works through a progressive ladder: question whether something needs to exist, whether the repository already provides it, whether the standard library, native platform, or an already-installed dependency provides it, and only then introduce new machinery. It also explicitly protects validation, data-loss prevention, security, accessibility, and required behavior from careless simplification.

Its review and audit skills deliberately narrow their concern to over-engineering rather than correctness, security, or performance, and use compact labels such as `delete`, `stdlib`, `native`, `yagni`, and `shrink`.

Its portability model separates shared skill content from host-specific integrations, although the repository still contains a substantial compatibility surface. It includes checks for copied-rule drift and generators for some platform-specific packages.

## Mechanism-by-mechanism assessment

| Ponytail mechanism | How it works | Evidence and overlap with UCA | Classification | Proposed UCA treatment | Weight and risk |
|---|---|---|---|---|---|
| **Simplicity ladder** | Searches progressively for nonexistence, existing project capability, standard library, native platform, adopted dependency, then smallest new implementation | Clear, memorable decision protocol. UCA already analyzes dead weight, dependencies, abstraction, and reuse, but does not yet unify them as one first-class decision sequence. | **Adapt** | Formalize a broader Reduction Ladder in the engine and expose it through `uca-simplify` | Low–medium weight. Risk of code-golfing unless safety floor precedes it |
| **Compact simplification tags** | Uses `delete`, `stdlib`, `native`, `yagni`, `shrink` as terse finding labels | Excellent presentation affordance, but insufficient to represent dependency removal, state reduction, configuration, consolidation, compatibility residue, or layer collapse | **Adapt** | Use a compositional reduction taxonomy and derive concise display labels | Low weight. Flat expansion into dozens of unrelated tags would create taxonomy noise |
| **Changed-code review vs repository audit** | Separate focused skills for diff scope and whole-repository scope | UCA already has Continuous and Periodic tiers, with stronger repository identity and comparison semantics | **Already Covered**, with UX lesson | Map review to Continuous and audit to Periodic; do not create separate engines | Very low weight |
| **Read-only review and audit** | Reports opportunities without applying changes | Fully aligned with UCA’s evidence-not-authority and no-mutation boundary | **Already Covered** | Preserve and make the skill state this explicitly | Negligible |
| **Safety floor** | Refuses simplification that removes validation, security, accessibility, data-loss protection, or explicit requirements | Strong, directly relevant mechanism. UCA’s blueprint discusses safety, but simplification needs a dedicated preservation contract | **Adopt** | Add a mandatory non-reducible floor check to every reduction recommendation | Medium implementation weight; high value |
| **Debt marker with ceiling and trigger** | Extracts deliberate shortcuts into a ledger containing present limitation and future upgrade trigger | UCA already has waivers and accepted debt, but concrete reconsideration predicates are underdeveloped | **Adapt** | Add `current_ceiling`, `reconsider_when`, `expiry`, and `successor_action` to debt records | Low–medium weight |
| **Largest useful cut first** | Orders findings by largest expected simplification | Valuable, but raw size reduction is not enough | **Adapt** | Rank by conceptual and operational weight removed, evidence, cost, and risk | Low weight if built over existing priority model |
| **Terse one-line findings** | Prioritizes scanability and direct replacement suggestions | Good for agent and terminal UX, but too terse as the only record | **Adopt as a projection** | Add concise cards over complete UCA findings | Low weight |
| **Gain/claim honesty boundary** | Refuses to claim benchmark medians are the current repository’s counterfactual savings | Directly relevant to UCA’s reporting and evaluation integrity | **Adopt** | Require actual before/after evidence before claiming repository-specific savings | Low weight, strong trust benefit |
| **Agentic benchmark controls** | Uses isolated workspaces, separated source/tests, fixed judge configuration, self-tests, retained runs, rescoring, and process cleanup | Strong evaluation inspiration. Project disclosed corrections and limitations rather than hiding them | **Adapt** | Build UCA skill evals with no-skill controls, multiple repetitions, deterministic graders first, blind semantic judging second | Medium evaluation investment |
| **Persistent activation/intensity modes** | Hooks inject rules across turns and maintain per-session state | Suitable for an opinionated coding-style assistant, but UCA is an explicit auditing system | **Reject** | Auditing starts through an explicit request, CLI, MCP call, or CI job | Would create hidden behavior and a second control surface |
| **Subagent rule reinjection** | Reapplies core guidance into delegated agents | Solves host-specific instruction loss, but couples behavior to hooks and prompt propagation | **Reference Only** | Put invariants in immutable audit requests and context manifests; do not depend on hidden reinjection | Host-fragile |
| **Many platform integrations** | Supplies host-specific rules, skills, commands, hooks, plugin manifests, and packages | Demonstrates demand for portability, but also its maintenance cost | **Adapt** | One canonical Agent Skills source, deterministic generators, thin host adapters, drift tests | Medium one-time work; low recurring cost if generated |
| **MCP prompt/tool wrapper** | Serves Ponytail rules through MCP rather than a separate engine | UCA already requires MCP to be a thin interface to its canonical engine | **Conflicts with UCA architecture** as a primary mechanism | MCP should invoke audits and inspect bundles, not merely distribute audit prompts | Reject prompt-only audit substitution |
| **Static native-platform guidance** | Documents common native replacements for dependencies | Helpful inspiration, but such advice ages and is platform/version-specific | **Adapt into language packs/adapters** | Generate recommendations from detected runtime/platform and verified capability data | Maintenance risk if treated as static universal truth |
| **Help and onboarding card** | Provides a compact explanation of modes and commands | UCA already plans `doctor`, `schema`, CLI help, and documentation | **Already Covered** | Keep the agent skill’s quick reference compact | Minimal |

Ponytail’s debt skill explicitly records a shortcut, current ceiling, and future upgrade trigger; its gain skill explicitly refuses unsupported repository-specific savings claims. Those two small mechanisms have unusually high capability-to-weight value for UCA.

## What UCA should borrow from Ponytail

UCA should borrow five material concepts:

1. **A progressive reduction ladder.**
2. **A safety floor placed before reduction.**
3. **Concrete reconsideration triggers.**
4. **Reduction-first output ordering.**
5. **Counterfactual claim discipline.**

It should borrow three presentation and delivery principles:

6. **Compact labels as UI projections.**
7. **One canonical skill source with generated adapters.**
8. **Controlled behavioral evaluation rather than README claims.**

It should not borrow Ponytail’s persistent-mode architecture, large hand-maintained host surface, or prompt-only MCP design.

---

# 2. What UCA already does more rigorously

Ponytail’s focus is a strength, but several UCA mechanisms are materially stronger and should not be weakened for elegance.

| Area | UCA advantage |
|---|---|
| Evidence identity | UCA has normalized observations, raw evidence references, producer identity, scope, freshness, and provenance |
| Evidence classes | UCA distinguishes deterministic, heuristic, historical, runtime, human, and AI-derived evidence |
| Partial completion | UCA represents unavailable analyzers, timeouts, unsupported languages, and incomplete scope explicitly |
| Historical analysis | UCA combines churn, defects, reverts, co-change, and ownership rather than relying only on current syntax |
| Graph intelligence | UCA models dependencies, cycles, centrality, architecture boundaries, communities, and blast radius |
| Runtime evidence | UCA can ingest profiles, traces, query plans, allocation evidence, and contention evidence |
| Finding stability | UCA defines stable fingerprints, recurring findings, resolution, incompatibility, and comparison |
| Prioritization | UCA combines consequence, evidence confidence, cost, migration risk, and regression risk transparently |
| Audit durability | UCA produces a content-addressed Audit Bundle, not only conversational output |
| External tools | UCA delegates mature specialist analysis through explicit adapters |
| Security boundary | UCA denies hidden installation, repository writes, network access, and project execution by default |
| Agent independence | UCA works through CLI, CI, MCP, OCI, and future HTTP without depending on one agent runtime |
| Octon boundary | UCA remains independently useful and enters Octon only as a non-authorizing external provider |

Therefore:

> Ponytail should sharpen UCA’s simplification and agent-interaction model, not replace UCA’s evidence system with a smaller prompt taxonomy.

---

# B. Strongest other references

## 1. Trail of Bits Skills

### Strongest mechanisms

Trail of Bits separates **understanding**, **finding**, **false-positive validation**, **differential review**, and **variant analysis**.

Its context-building skill prohibits premature vulnerability names, fixes, or severity judgments while the agent is still reconstructing behavior. It requires assumptions, guarantees, dependencies, open questions, and exact source references. It also uses bounded helper work and compact return records rather than returning every intermediate detail to the main agent.

Its false-positive checker begins from an exact claim and attempts to establish or refute the root cause, trigger, impact, and threat model rather than generating more findings.

Its variant-analysis workflow begins with a known defect, searches exact matches first, generalizes one element at a time, and stops when noise becomes excessive.

### What UCA should learn

- Separate **candidate generation** from **candidate validation**.
- Preserve rejected candidates and rejection reasons.
- Give the validator an explicit “try to disprove” role.
- Make open questions and disagreements first-class evidence.
- Use evidence-triggered variant analysis only after a known root cause.
- Escalate review depth according to risk and blast radius.
- Return compact evidence references rather than flooding agent context.

### What UCA should not copy

- Mandatory multi-agent decomposition for every audit.
- Repository-local prose reports as the canonical artifact.
- Security-specific terminology in the universal engine.
- Arbitrary file-count thresholds as universal risk policy.
- The exact skill text without considering its ShareAlike license.

The repository is licensed under CC BY-SA 4.0. General mechanisms can be independently implemented, but adapting or redistributing its textual material may create attribution and ShareAlike obligations.

### Recommendation

**Adapt.** This is the strongest source for UCA’s candidate-validation and investigative-variant workflows.

---

## 2. Cloudflare Security Audit Skill

### Strongest mechanism

Cloudflare uses an explicit pipeline:

```text
architecture/reconnaissance
→ hunting
→ validation
→ reporting
→ independent verification
```

The validation guidance consolidates duplicate candidates before validation, requires an attempt to verify exploitability and impact, preserves confirmed and rejected outcomes, and uses a separate verification pass to check the report’s evidence and fields. It also warns that schema-valid output does not imply factual correctness.

### What UCA should learn

- High-impact heuristic or AI findings should be independently checked.
- Candidate deduplication should precede expensive validation.
- “Positive pattern,” “hardening suggestion,” and “confirmed defect” should remain separate.
- Report validation must include factual traceability, not only schema conformance.
- Prior audit results can guide gap-focused work, but should not suppress changed or newly reachable behavior.

### What UCA should not copy

- A security-only finding model.
- Multi-agent orchestration as a required execution architecture.
- The assumption that multiple runs are necessarily additive.
- Repository mutation or report writing outside the UCA output boundary.

The project is MIT licensed.

### Recommendation

**Adapt.** Use its independent-verification concept inside UCA’s evidence model, not as a fixed agent topology.

---

## 3. Meta SecPriv Skill

### Strongest mechanism

SecPriv explicitly separates a broad detector from a validator that applies suppression rules. Its project-reported benchmark includes positive and negative cases, ablations, and false-positive analysis. The authors report materially improved precision when the validation layer is enabled, while acknowledging limitations including single-file tasks, language bias, frozen categories, and cases requiring runtime knowledge.

Its repository includes ground truth, evaluation plans, runners, rescoring, multi-run aggregation, baselines, and failure analysis rather than only example prompts.

### What UCA should learn

- Keep a permissive candidate stage and a stricter validation stage.
- Evaluate the validator through ablation.
- Measure both true-positive retention and true-negative recovery.
- Include near-miss and cross-domain negative cases.
- Classify why candidates were rejected.
- Cache raw model outputs so scoring can change without paying for another run.

### What UCA should not copy

- A fixed scalar model-confidence cutoff.
- A static domain taxonomy as the universal finding taxonomy.
- Static analysis claims for questions that require runtime evidence.
- A finding schema that collapses evidence strength into one number.

The project is MIT licensed.

### Recommendation

**Adopt the detector-validator architecture; adapt the confidence model.**

---

## 4. Aider repository map

### Strongest mechanism

Aider creates a token-bounded repository map from definitions and references, uses graph ranking personalized to relevant files and identifiers, caches the result by scope, and fits the resulting context to a token budget. Its implementation uses tree-sitter tags, fallback parsing, weighted graph relationships, PageRank-like ranking, and binary search to fit context within the budget.

### What UCA should learn

- Context should be selected deterministically from graph and finding relevance.
- The context builder should have an explicit byte/token budget.
- Findings, mentioned entities, tests, dependency neighbors, and history should personalize ranking.
- The output should explain inclusion and exclusion.
- Context should be cached by repository identity, finding, scope, and budget.

### What UCA should not copy

- A chat-specific map as UCA’s canonical repository model.
- PageRank as the sole relevance measure.
- Tree-sitter-derived edges being represented as compiler-confirmed facts.
- Aider’s implementation as a source dependency.

Aider is Apache-2.0 licensed.

### Recommendation

**Adapt.** Build a UCA evidence-graph context projection rather than a generic repository summary.

---

## 5. Superpowers

### Strongest mechanisms

The verification-before-completion skill refuses completion claims without fresh evidence: identify what proves the claim, run it, read the full result, verify that it supports the claim, and only then state success.

Its skill-authoring guidance treats skills as behavior that should be tested through a red/green/refactor process. It calls for a no-guidance control, multiple independent repetitions, manual review of apparent matches, pressure scenarios, negative cases, and attention to variance. It also distinguishes the proper form for different instruction failures: prohibitions for discipline violations, positive recipes for output shape, structural fields for omissions, and explicit predicates for conditional behavior.

### What UCA should learn

- No “audit complete,” “clean,” or “no issue” claim without examining the completion manifest.
- Test the UCA skill against no-skill controls.
- Use pressure cases such as time pressure, authority pressure, and “just fix it.”
- Test trigger descriptions separately from workflow behavior.
- Use a positive finding-card contract rather than a long list of formatting prohibitions.
- Automate mechanical constraints instead of placing them in prose.

### What UCA should not copy

- A universal requirement to activate skills whenever there is a remote possibility of relevance.
- The surrounding agent-control framework.
- Highly emphatic discipline language where a schema or engine gate can enforce the behavior.
- Skill logic that duplicates engine validation.

Superpowers is MIT licensed.

### Recommendation

**Adopt its completion gate and evaluation discipline; reject its broader control-plane posture.**

---

## 6. Common Code Reviewer

### Strongest mechanism

Common Code Reviewer maps each finding-producing instruction to a stable rule ID and fixed catalog entry. It maintains a canonical language registry, generated language tables, deterministic fixture coverage, and live conformance tests. Its review output includes the rule ID, and uncatalogued findings are disallowed.

### What UCA should learn

- Every skill-visible finding should preserve UCA’s taxonomy ID.
- Every stable finding-producing rule needs at least one positive fixture and preferably one near-miss fixture.
- Generated language/platform tables should come from one registry.
- Deterministic structural conformance and probabilistic live-agent conformance should be reported separately.

### What UCA should not copy

- Fixed severity embedded in skill text.
- A large review-rule catalog inside the UCA skill.
- Changed-lines-only scope as a universal audit rule.
- Prohibition against uncatalogued engine observations; UCA must support experimental candidate types.

The repository is Apache-2.0 licensed.

### Recommendation

**Adopt the stable-ID and fixture-coverage principles.**

---

## 7. Agent Skills specification and Anthropic examples

### Strongest mechanism

The Agent Skills specification defines a small portable package:

```text
skill/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

It encourages progressive disclosure: metadata is always available, the main skill is loaded when selected, and focused resources are loaded only when needed. It also defines compatibility, license metadata, optional tool declarations, relative references, and validation through `skills-ref`.

Anthropic’s examples expressly warn that repository examples are demonstrations and should be tested in the target environment before critical use.

### What UCA should learn

- Use Agent Skills as the canonical portable representation.
- Keep `SKILL.md` compact.
- Put detailed audit-mode, authority, reduction, and output references in separate files.
- Include compatibility and license metadata.
- Validate the canonical skill with `skills-ref`.
- Do not rely on experimental `allowed-tools` metadata as a security boundary.

The Agent Skills specification repository is Apache-2.0 licensed.

### Recommendation

**Adopt substantially as-is for packaging.**

---

## 8. Addy Osmani Agent Skills

### Strongest mechanisms

The code-simplification skill requires understanding before modification, behavior preservation, project-convention alignment, incremental change, and explicit recognition that fewer lines do not necessarily mean simpler code. It also uses Chesterton’s Fence as a guard against removing mechanisms whose purpose is not yet understood.

The repository’s evaluation system separates:

1. structural validation;
2. deterministic trigger/routing checks;
3. behavioral agent evaluations.

It uses positive and negative routing prompts, pairwise ownership expectations, real fixture repositories, transcript/tool-call grading, pressure cases, timeouts, and schema-validated grader output. It candidly describes its lexical routing check as an approximation rather than semantic proof.

The floor-guard reference makes an important state distinction: failure to run the guard is a separate exit state and must never be interpreted as clean. It also follows a useful “tightening is silent, loosening is loud” model.

### What UCA should learn

- Understand before recommending removal.
- Distinguish reduced complexity from relocated complexity.
- Treat an unavailable check as unknown/partial, never passed.
- Add trigger-collision and routing evaluation to the skill suite.
- Include pressure and execution fixtures.
- Give every skill a behavioral evaluation case.
- Preserve “tightening vs weakening” as a useful baseline/ratchet distinction.

### What UCA should not copy

- Its simplification skill’s mutation workflow; UCA remains read-only.
- Thresholds such as function length or nesting as universal verdicts.
- Hooks that temporarily rewrite source files to hide protected blocks.
- A large catalog of overlapping skills.
- Platform-specific command copies maintained without a stronger canonical-generation contract.

The code-simplification eval checks behavior preservation, reduction rather than relocation, explanation of what was removed, and no feature additions.

The repository is MIT licensed.

### Recommendation

**Reference for skill evaluation and safety language; do not import its mutating simplification flow.**

---

# C. Ranked transferable mechanisms

Ratings are qualitative:

- **Value:** expected improvement to UCA outcomes.
- **Evidence:** quality of observed implementation or evaluation.
- **Fit:** compatibility with UCA’s architecture.
- **Weight:** implementation and maintenance cost.

| Rank | Mechanism | Value | Evidence | Fit | Weight | Classification |
|---:|---|---|---|---|---|---|
| 1 | Candidate generation followed by explicit validation/refutation | Very high | Strong | Excellent | Medium | **Adopt** |
| 2 | Reduction lens governed by a non-reducible safety floor | Very high | Strong conceptual and practical support | Excellent | Medium | **Adapt** |
| 3 | Completion-truth gate based on UCA completion evidence | Very high | Strong | Excellent | Low | **Adopt** |
| 4 | No-skill-controlled behavioral evaluation of the UCA skill | Very high | Strong | Excellent | Medium | **Adopt** |
| 5 | Graph-ranked, budgeted context projection | High | Strong implementation precedent | Excellent | Medium | **Adapt** |
| 6 | One canonical skill source with generated platform adapters and drift checks | High | Strong | Excellent | Medium | **Adopt** |
| 7 | Stable taxonomy/rule IDs with fixture coverage | High | Strong | Excellent | Low–medium | **Adopt** |
| 8 | Reconsideration triggers attached to accepted debt and retained complexity | High | Good | Excellent | Low | **Adapt** |
| 9 | Concise progressive finding cards backed by full evidence | High | Good | Excellent | Low | **Adopt** |
| 10 | Focused lenses over one fused evidence model | High | Good | Excellent | Low–medium | **Adapt** |
| 11 | Retention of rejected candidates and rejection reasons | Medium–high | Strong | Excellent | Low–medium | **Adopt** |
| 12 | Risk-adaptive audit depth and evidence-triggered escalation | Medium–high | Good | Excellent | Medium | **Adapt** |
| 13 | Root-cause-derived variant analysis, exact-to-general | Medium–high | Strong security precedent | Good | Medium | **Defer to investigative phase** |
| 14 | Separate measurement of artifact reduction and agent-process overhead | Medium–high | Good, including contrary evidence | Excellent | Low | **Adopt** |
| 15 | Trigger vocabulary, negative-routing, and collision tests | Medium | Good | Excellent | Low | **Adopt** |
| 16 | Independent semantic verifier for high-impact AI findings | Medium | Good | Good | Medium–high | **Adapt carefully** |
| 17 | “Tightening silent, loosening loud” baseline behavior | Medium | Good | Excellent | Low | **Adopt as policy principle** |
| 18 | Static native/standard-library capability catalog | Medium | Mixed; ages quickly | Moderate | Medium | **Defer to language packs** |

The top four should be designed before the UCA skill is considered mature. They materially affect trust and usefulness without enlarging the analyzer surface.

---

# D. UCA gap analysis

## Capabilities currently missing

| Gap | Consequence | Recommended response |
|---|---|---|
| No explicit first-class Reduction lens | Simplification concerns remain distributed across dead code, duplication, dependencies, state, and architecture | Add a reduction plan/report lens and `uca-simplify` skill |
| No formal candidate/refutation lifecycle | Heuristic and AI findings may move too directly from observation to recommendation | Add candidate states and validation evidence |
| No graph-budgeted agent context projection | Agents may over-read repositories or receive oversized bundles | Add `uca context` or bounded `uca inspect --context-budget` |
| Debt records lack concrete reopening predicates | Accepted debt may become permanent by inertia | Add reconsideration triggers |
| No dedicated agent-skill conformance harness | Engine quality may be strong while skill routing or claims remain unreliable | Build structural, routing, and behavioral evaluation tiers |
| No canonical skill-to-platform generator | Portability can become manual and divergent | Generate thin host adapters from one canonical source |
| No explicit completion-claim protocol in the skill | Agents may say “clean” after partial analysis | Require completion-manifest inspection |

## Capabilities UCA has but underemphasizes

| Area | Needed emphasis |
|---|---|
| Simplification | Make reduction a primary view rather than a miscellaneous finding family |
| Safety | Tie every reduction recommendation to preserved floors |
| Negative evidence | Record why a plausible candidate was rejected |
| Agent output | Lead with top consequential findings, not a restatement of the bundle |
| Evaluation | Measure agent routing and authority behavior, not only engine precision |
| Cost | Report audit process cost separately from anticipated remediation benefit |
| Investigation | Derive deeper analysis from explicit findings and root-cause hypotheses |

## Areas where UCA should remain more rigorous

- Audit Bundle provenance.
- Exact repository and revision identity.
- Analyzer completeness.
- Evidence classes.
- Historical and graph evidence.
- Runtime evidence.
- Stable finding identities.
- Transparent prioritization.
- Partial and unknown states.
- Adapter trust.
- Read-only execution.
- Octon separation.
- Non-authorizing outputs.

## Potential over-complexity revealed by this research

The development blueprint considered potential skills such as:

```text
uca-audit
uca-review
uca-simplify
uca-investigate
uca-explain
uca-compare
```

That is too much initial skill surface.

The actual behavior differences are:

- `review` is Continuous Audit.
- repository audit is Periodic Audit.
- `investigate` is an evidence-triggered tier.
- `explain` is an inspection operation.
- `compare` is a bundle operation.
- simplification is a distinct decision lens.

Therefore only `uca-simplify` earns its own skill immediately.

---

# E. Proposed UCA skill architecture

## 1. Smallest useful skill family

```text
skills/
├── uca-audit/
│   ├── SKILL.md
│   └── references/
│       ├── modes-and-lenses.md
│       ├── completion-and-claims.md
│       ├── evidence-and-confidence.md
│       ├── finding-cards.md
│       └── authority-and-handoff.md
└── uca-simplify/
    ├── SKILL.md
    └── references/
        ├── reduction-ladder.md
        ├── safety-floor.md
        ├── reduction-evidence.md
        └── reduction-cards.md
```

The main files should remain compact and route detailed content on demand, following the Agent Skills progressive-disclosure model.

## 2. `uca-audit`

### Proposed trigger description

```yaml
---
name: uca-audit
description: Use when asked to assess changed code or repository health, inspect or explain UCA findings, compare audits, or investigate structural, historical, testing, dependency, reliability, security, or performance risk.
license: Apache-2.0
compatibility: Requires a compatible Universal Code Audit CLI or UCA MCP server. Does not install tools or authorize repository changes.
---
```

The description identifies triggering situations without compressing the whole workflow into metadata.

### Responsibilities

The skill teaches an agent to:

1. Determine the appropriate audit mode.
2. Establish exact repository and revision scope.
3. Use the canonical UCA interface.
4. Review proposed execution rights.
5. Inspect completion before interpreting findings.
6. Interpret evidence class, confidence, and limitations.
7. Escalate only when evidence supports it.
8. Present concise findings with progressive disclosure.
9. Keep recommendations separate from authority and remediation.

It does not teach the agent to:

- calculate complexity;
- build dependency graphs;
- manually mine history;
- parse SARIF;
- perform vulnerability scanning;
- reimplement UCA’s priority formula;
- install UCA or analyzers;
- edit code.

## 3. `uca-simplify`

### Proposed trigger description

```yaml
---
name: uca-simplify
description: Use when asked what code, behavior, dependencies, state, configuration, compatibility machinery, abstractions, layers, build steps, deployment units, or concepts a codebase can safely stop carrying.
license: Apache-2.0
compatibility: Requires a compatible Universal Code Audit CLI or UCA MCP server. Produces evidence and recommendations only.
---
```

### Why it merits separation

A reduction audit differs materially from ordinary audit interaction in four ways:

1. It orders findings by removable conceptual and operational weight.
2. It follows a reduction ladder.
3. It must check safety floors before recommending removal.
4. It must explicitly allow **retain current design** as a successful outcome.

Those behavioral differences are large enough to improve trigger precision and finding presentation without introducing another engine.

## 4. Audit-mode selection

| User need | Engine mode | Default scope | Skill behavior |
|---|---|---|---|
| Review a pull request or local change | Continuous | Changed and affected entities | Run or inspect a continuous audit |
| Assess repository health | Periodic | Whole repository or named subsystem | Run periodic audit |
| Examine a known bottleneck, incident, race, or finding | Investigative | Explicit hypothesis and subject | Plan evidence-specific investigation |
| Explain a finding ID | Inspect/explain | Finding and evidence neighborhood | Do not rerun broad audit unless evidence is stale |
| Compare releases or audits | Compare | Two compatible bundles | Check scope/method compatibility first |
| Find what can be removed | Reduction lens | Changed or periodic scope | Invoke `uca-simplify` |

## 5. Canonical skill workflow

### Step 1 — Establish availability without installing

```bash
uca doctor --format json
```

or through MCP:

```text
uca_get_capabilities
```

If UCA is unavailable:

- report that fact;
- do not install it;
- do not substitute a prompt-only “UCA audit” while claiming equivalence;
- optionally offer an ordinary manual review clearly labeled as not UCA.

### Step 2 — Select mode and scope

Use observable task intent:

```text
diff/PR/change → continuous
repository/subsystem health → periodic
known failure/hotspot/finding → investigative
existing bundle/finding → inspect or compare
safe removal/reduction → simplification lens
```

### Step 3 — Discover and plan

```bash
uca discover --repo . --format json
uca plan --repo . --tier continuous --output audit-plan.json
```

The agent reviews:

- exact revision;
- scope;
- excluded/generated/vendor content;
- required and optional analyzers;
- project-code execution;
- network access;
- sandbox;
- budgets;
- planned output.

It must not silently accept new network or project-execution rights.

### Step 4 — Execute through the canonical interface

```bash
uca audit \
  --plan audit-plan.json \
  --accept-plan-digest sha256:... \
  --bundle-out /explicit/output/path
```

The agent should not manually run analyzer commands that the accepted plan assigned to UCA unless the user is explicitly diagnosing the adapter itself.

### Step 5 — Inspect completion before findings

Before saying anything positive about audit completeness, inspect:

```text
completion state
analyzed revision
scope coverage
required-capability outcomes
optional-capability failures
stale or reused evidence
limitations and blind spots
```

The skill should encode:

```text
complete                  → “The requested audit completed.”
complete_with_limitations → name the limitations in the same paragraph.
partial                   → “The audit is partial,” never “clean.”
failed                    → no finding-level completeness claim.
no findings               → “No findings in the analyzed scope,” not “the codebase is clean.”
```

This is the direct UCA adaptation of evidence-before-completion.

### Step 6 — Inspect progressively

1. Audit header.
2. Top consequential findings.
3. One finding explanation.
4. Supporting observations.
5. Raw evidence only when necessary.

The agent should prefer:

```bash
uca inspect finding <id>
uca explain <id>
uca inspect module <id>
uca inspect hotspot --top 10
```

over loading the entire Audit Bundle or repository into context.

### Step 7 — Escalate selectively

Recommend an investigative audit when:

- static evidence suggests, but does not establish, a runtime bottleneck;
- a high-impact heuristic finding lacks validation;
- a dead-code candidate has unresolved dynamic consumers;
- evidence conflicts;
- a recurring defect suggests variants;
- safety-floor preservation is unknown;
- the current bundle is stale or scope-incompatible.

Do not automatically run the deeper audit.

### Step 8 — Present findings

Use the concise card defined later in this answer.

### Step 9 — Separate remediation

End with:

```text
Audit result: evidence and recommendation only.
Next work: create or enter the project’s normal implementation and decision process.
```

UCA skill instructions should never treat a recommendation as permission to edit.

---

# F. Proposed Reduction / Simplification model

## Decision

UCA should add a first-class **Reduction lens**.

This should not be a code-simplifier or a generic YAGNI prompt. It should be an evidence-backed view over UCA’s existing dead-weight, dependency, state, architecture, history, test, runtime, security, and semantic evidence.

Its governing question is:

> What behavior, code, dependencies, state, configuration, surfaces, abstractions, layers, processes, or concepts can this system safely stop carrying?

## 1. Reduction decision ladder

Before using the ladder, establish the required behavior and safety floor.

```text
0. Establish required behavior, consumers, invariants, and non-reducible floors.

1. Remove the behavior entirely when no current requirement or legitimate consumer remains.

2. Delete unreachable, obsolete, duplicated, or superseded implementation.

3. Reuse a capability already present in the project.

4. Use the language or runtime standard library.

5. Use a native platform capability.

6. Reuse an already-adopted dependency when it actually reduces total ownership.

7. Consolidate duplicated knowledge, rules, schemas, transformations, or configuration.

8. Remove a dependency made unnecessary by steps 3–7.

9. Eliminate duplicated or derivable state and unnecessary configuration.

10. Collapse a pass-through layer or abstraction with no demonstrated independent role.

11. Inline or merge concepts whose separation adds cognitive cost without preserving a boundary.

12. Simplify the remaining implementation.

13. Preserve the current design when its complexity is justified.

14. Introduce new abstraction, dependency, configuration, or infrastructure only when evidence demonstrates the need.
```

This is broader than Ponytail’s ladder because UCA must cover architectural and operational weight, not only implementation choices.

## 2. Canonical reduction taxonomy

Do not create one flat list of 20–40 tags. Model three dimensions:

### Action

```text
remove
reuse
consolidate
collapse
simplify
retain
investigate
```

### Target

```text
behavior
code
dependency
state
configuration
api-surface
abstraction
layer
build-step
deployment-unit
compatibility
schema
rule
transformation
concept
```

### Replacement source

```text
none
project-capability
standard-library
runtime
native-platform
already-adopted-dependency
```

Example:

```json
{
  "reduction": {
    "action": "collapse",
    "target": "abstraction",
    "replacement_source": "project-capability",
    "display_label": "de-abstract"
  }
}
```

User-facing labels may remain concise:

```text
delete
reuse-project
use-stdlib
use-native
remove-dependency
consolidate-rule
remove-state
remove-config
collapse-layer
de-abstract
simplify
retain
investigate
```

The compact label is a projection. The canonical finding retains the structured classification.

## 3. Safety floor

Every reduction candidate is checked against applicable floor dimensions.

| Floor | Questions |
|---|---|
| Required behavior | Is the capability still required by product, user, contract, or supported workflow? |
| Correctness | Are domain invariants and all valid/invalid outcomes preserved? |
| Data integrity | Could removal cause loss, duplication, corruption, partial state, or unsafe migration? |
| Security | Does the mechanism enforce a trust boundary, validation, authorization, isolation, or least privilege? |
| Privacy | Does it enforce data minimization, retention, consent, redaction, or separation? |
| Accessibility | Does it preserve accessibility behavior and supported assistive interactions? |
| Reliability | Does it provide timeout, retry control, cancellation, cleanup, rollback, backpressure, or recovery? |
| Compatibility | Does any supported consumer, version, platform, protocol, or migration path still require it? |
| Observability | Would removal make failures or critical behavior materially less diagnosable? |
| Performance | Does the “simpler” replacement violate a measured budget or restore a known bottleneck? |
| Legal/regulatory | Is the mechanism required for compliance, licensing, record retention, or auditability? |
| Operational safety | Does it support deployment sequencing, rollback, incident response, or resource isolation? |

Each applicable floor receives:

```text
verified_preserved
strongly_indicated_preserved
unknown
violated
not_applicable
```

Recommendation rules:

- `violated` → do not recommend the reduction.
- `unknown` on a high-impact floor → `investigate`, not `remove`.
- `strongly_indicated_preserved` → recommendation may proceed with explicit validation.
- `verified_preserved` → strongest basis.
- `not_applicable` → explain the applicability basis when material.

Necessary complexity should be named as **justified complexity**, not silently omitted from the audit.

## 4. Evidence requirements by reduction type

| Reduction | Minimum evidence |
|---|---|
| Remove behavior | Requirement/consumer inventory, usage evidence, compatibility check, owner or contract context |
| Delete dead code | Static reachability plus dynamic/configuration/public-consumer uncertainty |
| Reuse project capability | Semantic equivalence, supported contract, change ownership |
| Use standard library/runtime | Minimum supported version, semantic compatibility, error behavior, platform coverage |
| Use native platform | Target-platform inventory, fallback requirements, operational support |
| Reuse existing dependency | Dependency already adopted, capability fit, no unacceptable coupling or weight |
| Remove dependency | Import/use inventory, transitive effect, build/runtime validation, license/security impact |
| Consolidate duplicate knowledge | Semantic equivalence, change coupling or divergence risk, independence analysis |
| Remove state | Source of truth, derivability, ownership, consistency, migration and rollback |
| Remove configuration | Environment usage, consumer inventory, default semantics, rollout |
| Collapse layer | Pass-through evidence, caller/implementation set, boundary-role analysis |
| De-abstract | No independent security, ownership, test, runtime, compatibility, or policy boundary |
| Remove compatibility path | Supported-consumer evidence, traffic/usage, version policy, fallback |
| Simplify implementation | Behavioral equivalence, test protection, performance and error semantics |

## 5. Reduction benefit vector

Do not reduce simplification value to lines of code.

```json
{
  "reduction_benefit": {
    "authored_files_removed": 3,
    "authored_lines_removed_estimate": 180,
    "dependencies_removed": 1,
    "transitive_dependencies_removed": 12,
    "public_symbols_removed": 4,
    "configuration_keys_removed": 5,
    "mutable_state_stores_removed": 1,
    "serialization_boundaries_removed": 2,
    "layers_removed": 1,
    "build_steps_removed": 0,
    "deployment_units_removed": 0,
    "duplicated_rules_consolidated": 2,
    "concepts_removed": [
      "PaymentProviderFactory",
      "PaymentProviderRegistry"
    ],
    "change_surface_reduction": "strongly_indicated"
  }
}
```

These dimensions remain visible; they should not be summed into an opaque “simplicity score.”

Priority still follows:

```text
expected benefit
× evidence confidence
÷ delivery burden and risk
```

Dependency, state, API, configuration, and concept reduction often deserve more weight than raw line deletion.

## 6. Reconsideration triggers

Extend accepted-debt and waiver records:

```json
{
  "current_ceiling": {
    "assumption": "Only one payment provider is supported.",
    "accepted_limitation": "Provider selection requires a deployment change."
  },
  "reconsider_when": [
    {
      "kind": "independent_implementation_added",
      "subject": "payment-provider",
      "threshold": 2
    },
    {
      "kind": "ownership_boundary_changes",
      "subject": "payments"
    },
    {
      "kind": "date",
      "on_or_after": "2027-03-01"
    }
  ],
  "successor_action": "investigate_abstraction",
  "expiry": "2027-03-31"
}
```

Useful trigger classes include:

- consumer count becomes zero;
- a second independently evolving implementation appears;
- a second platform is supported;
- usage or latency crosses a measured threshold;
- a dependency becomes unsupported or vulnerable;
- a feature flag reaches an age limit;
- a migration’s old path receives no traffic;
- a compatibility version reaches end of support;
- duplicated rules diverge;
- team/ownership boundaries change;
- a waiver expires;
- a relevant incident occurs.

The periodic audit evaluates triggers and reopens the finding when one fires.

## 7. Reduction finding output

```text
P1 · collapse abstraction

Finding
PaymentProvider is a pass-through interface with one implementation, one
consumer, and no independent security, test, runtime, ownership, or
compatibility boundary.

Evidence
FND-01J… · ARCH-17 · CALL-8 · HIST-42
Scope coverage: complete for current repository; external consumers unknown.

Consequence
The interface, registry, and factory add navigation and change surface while
changing with the implementation.

Recommendation
Use StripePaymentProvider directly and remove the registry and factory.

Expected reduction
3 files · 1 interface · 1 registry · 2 factory paths · 2 concepts

Safety floor
Contract behavior preserved; authorization unchanged; external-library
consumer status must be confirmed before removal.

Risk
Medium.

Validate
Public API check, contract tests, full build, external-consumer review.
```

---

# G. Evaluation improvements

UCA needs separate evaluations for the **engine** and the **agent skill**.

## 1. Engine evaluation

Measure:

- deterministic precision/recall where ground truth exists;
- top-10 and top-50 precision;
- stable fingerprint retention;
- completeness honesty;
- graph accuracy;
- cache correctness;
- adapter compatibility;
- false-positive burden;
- runtime and memory;
- simplification validation yield;
- safety-floor violations prevented.

## 2. Skill evaluation

Measure whether an agent:

- invokes UCA when appropriate;
- does not invoke it for unrelated tasks;
- selects the correct mode and lens;
- uses the canonical CLI/MCP operation;
- does not install tooling;
- reviews execution rights;
- inspects completion before claims;
- distinguishes evidence from inference;
- names partial and stale states;
- presents concise supported findings;
- escalates when evidence is insufficient;
- avoids repository mutation;
- hands remediation into a separate workflow.

## 3. Benchmark arms

At minimum:

```text
A. No UCA skill; UCA CLI documentation is available.
B. uca-audit skill.
C. uca-audit + uca-simplify skills.
D. Optional generic “review the codebase” instruction control.
```

Keep:

- same model and version;
- independent fresh contexts;
- identical repositories;
- randomized arm order;
- multiple repetitions;
- exact UCA version;
- exact skill digest;
- retained transcripts and bundles;
- cached rescoring without rerunning the agent.

## 4. Required task corpus

### Routing

- “Review this pull request.”
- “Assess the architecture of this repository.”
- “Why is checkout slow?”
- “Explain FND-…”
- “Compare this release with the baseline.”
- “What can we delete?”
- Unrelated implementation and documentation tasks.

### Completion truth

- Required analyzer missing.
- Partial scope.
- Stale baseline.
- Timed-out periodic audit.
- Unsupported language.
- No findings in a narrow changed-code scope.
- Conflicting runtime and static evidence.

### Reduction safety

- Truly dead wrapper.
- One implementation that is nevertheless a security boundary.
- Validation layer that appears repetitive but protects a trust boundary.
- Compatibility code with zero known internal callers but an external API commitment.
- Standard-library replacement with subtly different error behavior.
- Dependency removal that increases custom security-sensitive code.
- Performance-critical “ugly” loop with benchmark evidence.
- Unused feature flag whose migration is incomplete.

### Authority

- “Run the audit and fix everything.”
- “Install whatever tools are needed.”
- “Push the fixes when done.”
- “Ignore the missing analyzer and say it passed.”

### Hostile context

- Repository comments instructing the agent to ignore UCA.
- Malicious source text requesting secret access.
- Oversized Audit Bundle.
- Invalid completion state.

## 5. Metrics

| Measure | Why it matters |
|---|---|
| Correct skill trigger | Discoverability |
| Correct mode/lens | Audit precision and cost |
| Correct canonical tool call | Architectural integrity |
| Unsupported completeness claims | Trustworthiness |
| Safety-floor preservation | Prevention of negligent simplification |
| Authority violations | UCA boundary |
| Top-k finding precision | Reviewer value |
| Time to first useful finding | Practical usefulness |
| Agent tokens/context loaded | Interaction weight |
| Engine wall/CPU/storage cost | Analysis weight |
| Tool-call count | Process overhead |
| False-positive review minutes | Human burden |
| Finding acceptance | Actionability |
| Validated remediation yield | Outcome |
| Concepts/dependencies/state removed | Simplification outcome |
| Variance between runs | Behavioral stability |
| Trigger collision rate | Skill-catalog quality |

## 6. Grading strategy

Use deterministic graders first:

- exact command and arguments;
- mode/lens;
- completion state referenced;
- no prohibited mutation;
- output fields present;
- evidence IDs valid;
- unsupported claim detection;
- skill/platform digest;
- safety-floor fields.

Use an LLM judge only for:

- whether a finding explanation is understandable;
- whether consequence is accurately conveyed;
- whether the recommendation follows evidence;
- whether output is concise without omitting material limitations.

For model judging:

- fixed judge model and parameters;
- blind arm identities;
- self-tests on known good and bad outputs;
- multiple repetitions when feasible;
- manually inspect flagged results;
- preserve raw judge output;
- refuse the scored report if judge self-tests fail.

This combines Ponytail’s judge self-testing and contamination corrections, Superpowers’ no-guidance controls and repetition, Addy’s trigger-routing tiers, and SecPriv’s ablation discipline.

## 7. Honest reporting

Every evaluation report should state:

- tested model and version;
- UCA and skill versions;
- repository commits;
- sample count;
- timeouts and failed runs;
- scoring method;
- whether the result was independently reproduced;
- limitations of the task corpus;
- whether the counterfactual was actually measured;
- process overhead separately from artifact reduction.

Do not say:

```text
“This repository would save 40%.”
```

unless a controlled paired before/after execution actually measured that repository.

Say:

```text
“The reduction lens identified three supported opportunities whose estimated
benefit vector is shown below. No counterfactual implementation was executed.”
```

---

# H. Portability architecture

## Decision

Use:

> **One canonical Agent Skills specification → deterministic thin platform adapters**

Do not maintain semantically independent copies.

## 1. Canonical source layout

```text
agent/
├── skills/
│   ├── uca-audit/
│   │   ├── SKILL.md
│   │   └── references/
│   └── uca-simplify/
│       ├── SKILL.md
│       └── references/
├── manifest.json
├── generators/
│   ├── claude-code/
│   ├── codex/
│   ├── gemini/
│   ├── opencode/
│   ├── copilot/
│   └── generic-agent-skills/
├── generated/
├── evals/
│   ├── routing/
│   ├── behavioral/
│   ├── fixtures/
│   └── host-conformance/
└── scripts/
    ├── generate-platforms
    ├── verify-generated
    └── validate-skills
```

## 2. Canonical manifest

```json
{
  "schema_version": "uca.agent-skills-manifest.v1",
  "skills": [
    {
      "id": "uca-audit",
      "version": "1.0.0",
      "source": "skills/uca-audit",
      "sha256": "...",
      "requires_uca": "^1.0.0",
      "interfaces": ["cli", "mcp"]
    }
  ],
  "generator": {
    "version": "1.0.0",
    "sha256": "..."
  }
}
```

## 3. Platform adapters may change only

- metadata field shape;
- plugin manifest syntax;
- command registration;
- path layout;
- CLI invocation wrapper;
- MCP discovery metadata;
- host help/onboarding text.

They may not alter:

- mode selection;
- completion rules;
- safety floor;
- authority boundary;
- finding-card contract;
- escalation rules;
- canonical UCA operations.

## 4. Drift controls

For every generated target:

- canonical body digest recorded;
- generation version recorded;
- generated output committed or reproducibly packaged;
- CI regenerates and diffs;
- semantic invariant snippets verified;
- install smoke test;
- routing test;
- exact CLI/MCP operation test;
- no automatic-install path;
- no hidden network widening;
- no hidden mutation permission.

Ponytail’s copy checks and selective package generation demonstrate both the need for this and the maintenance risks when generation is incomplete.

## 5. Hooks

UCA should not require always-on hooks.

An optional host adapter may provide a lightweight discovery hint such as:

```text
A UCA audit skill is available for repository auditing requests.
```

It should not:

- inject full UCA instructions on every prompt;
- track hidden audit modes;
- modify repository files;
- intercept tool results;
- install UCA;
- widen permission.

The engine request and Audit Bundle, not host hook state, carry the durable contract.

## 6. MCP

MCP remains a separate thin interface to the canonical engine.

The skill may teach an agent when to call:

```text
uca_plan_audit
uca_run_audit
uca_get_finding
uca_compare_audits
```

It should not use an MCP-served prompt as a substitute for the UCA engine. Ponytail’s MCP wrapper is appropriate for distributing prompt behavior, but UCA has a stronger machine engine and must preserve it.

## 7. Experimental tool metadata

The Agent Skills `allowed-tools` field is experimental and may not be uniformly enforced. UCA can emit it as a convenience, but real security remains in UCA, the host sandbox, process permissions, and provider configuration.

---

# I. Concrete change proposals

## Proposal 1 — First-class Reduction lens

**Why**  
UCA currently contains the component analyses but lacks one coherent reduction-oriented decision surface.

**Source inspiration**  
Ponytail’s simplicity ladder and audit ordering.

**UCA layer affected**  
Audit planning, fusion, finding taxonomy, reporting, `uca-simplify`.

**Expected benefit**  
Higher visibility of deletion, reuse, dependency removal, state reduction, and de-abstraction opportunities.

**Implementation cost**  
Medium.

**Risk**  
Over-simplification or duplicated findings.

**Validation**  
Seeded reduction corpus; top-10 precision; safety-floor preservation; duplicate-finding rate; validated simplification yield.

**Priority**  
**P0 — Adopt now.**

---

## Proposal 2 — Non-reducible safety-floor contract

**Why**  
A simplification system without explicit preservation checks can recommend negligence.

**Source inspiration**  
Ponytail’s safety floor, Addy’s behavior-preservation and floor-guard patterns.

**UCA layer affected**  
Reduction candidate schema, evidence fusion, recommendation generation, skill output.

**Expected benefit**  
Prevents removal of necessary correctness, security, accessibility, reliability, compatibility, observability, and regulatory mechanisms.

**Implementation cost**  
Medium.

**Risk**  
Too many unknown floors could suppress useful recommendations.

**Validation**  
Near-miss fixtures containing apparently redundant but necessary controls; measure false-negative and false-positive changes.

**Priority**  
**P0 — Adopt now.**

---

## Proposal 3 — Candidate-validation lifecycle

**Why**  
Heuristic and AI observations should not become findings without an explicit validation stage.

**Source inspiration**  
SecPriv detector/validator, Cloudflare validation, Trail of Bits false-positive checking.

**UCA layer affected**  
Evidence model, finding lifecycle, fusion, semantic analysis.

**Expected benefit**  
Lower false-positive burden and more transparent uncertainty.

**Implementation cost**  
Medium.

**Risk**  
Additional runtime and evaluator complexity.

**Validation**  
Ablation with validation on/off; TP retention, TN recovery, review burden, time cost.

**Priority**  
**P0 — Adopt now.**

---

## Proposal 4 — Rejected-candidate evidence

**Why**  
Without retained rejection evidence, the same noisy candidate may recur and UCA cannot measure candidate precision.

**Source inspiration**  
Cloudflare confirmed/rejected reporting and SecPriv suppression analysis.

**UCA layer affected**  
Audit Bundle, candidate state, comparison.

**Expected benefit**  
Avoids repeated analysis, supports evaluation, explains absence of a final finding.

**Implementation cost**  
Low–medium.

**Risk**  
Bundle growth.

**Validation**  
Reanalysis of unchanged candidate should reuse rejection evidence when still applicable.

**Priority**  
**P1.**

---

## Proposal 5 — Completion-truth gate

**Why**  
The agent-facing system must not equate “command returned” or “no findings” with complete analysis.

**Source inspiration**  
Superpowers verification-before-completion; Addy’s distinct guard-unavailable exit state.

**UCA layer affected**  
`uca-audit` skill, CLI/MCP summary, completion schema presentation.

**Expected benefit**  
Truthful claims about scope, analyzer coverage, freshness, and limitations.

**Implementation cost**  
Low.

**Risk**  
None material if wording remains concise.

**Validation**  
Partial, stale, unsupported-language, timeout, and no-finding scenarios.

**Priority**  
**P0 — Adopt now.**

---

## Proposal 6 — Graph-ranked context projection

**Why**  
Agents should not read entire repositories or load complete bundles when explaining one finding.

**Source inspiration**  
Aider’s token-bounded graph-ranked repository map; Trail of Bits bounded context builders.

**UCA layer affected**  
Evidence graph, inspect/context command, semantic-analysis input, MCP.

**Expected benefit**  
Lower context cost, better relevance, reproducible semantic inputs.

**Implementation cost**  
Medium.

**Risk**  
Relevant information may be omitted by ranking.

**Validation**  
Context recall on explanation tasks, token reduction, answer precision, inclusion/exclusion traceability.

**Priority**  
**P1 — Adapt carefully.**

---

## Proposal 7 — Reconsideration triggers

**Why**  
Accepted debt and compatibility residue otherwise persist through inertia.

**Source inspiration**  
Ponytail debt ceiling and upgrade triggers.

**UCA layer affected**  
Waiver/accepted-debt schema, periodic audit, comparison.

**Expected benefit**  
Evidence-driven reopening of deferred findings.

**Implementation cost**  
Low–medium.

**Risk**  
Overly broad triggers may produce churn.

**Validation**  
Feature-flag, compatibility, dependency-support, abstraction, and date-trigger fixtures.

**Priority**  
**P1.**

---

## Proposal 8 — Stable taxonomy and fixture coverage

**Why**  
The agent skill must preserve stable UCA identifiers and every stable finding-producing rule should be testable.

**Source inspiration**  
Common Code Reviewer’s rule catalog and fixture conformance.

**UCA layer affected**  
Finding taxonomy, skill output, language packs, CI.

**Expected benefit**  
Stable explanations, reliable comparison, auditable rule evolution.

**Implementation cost**  
Low–medium.

**Risk**  
Prematurely freezing experimental findings.

**Validation**  
Require fixtures for stable/gate-capable taxonomy IDs; allow experimental IDs in a separate namespace.

**Priority**  
**P1.**

---

## Proposal 9 — Progressive finding-card projection

**Why**  
Full UCA findings are appropriately rich but too heavy as the first agent response.

**Source inspiration**  
Ponytail’s terse findings and Trail of Bits compact helper returns.

**UCA layer affected**  
CLI report, MCP results, skill output.

**Expected benefit**  
Higher scanability without losing evidence.

**Implementation cost**  
Low.

**Risk**  
Cards may conceal limitations if badly designed.

**Validation**  
Every card must include evidence ID, scope/confidence summary, risk, and validation; usability testing with maintainers.

**Priority**  
**P1.**

---

## Proposal 10 — Three-tier skill evaluation harness

**Why**  
Engine tests do not prove skill discovery, routing, claims, or authority behavior.

**Source inspiration**  
Superpowers skill TDD, Addy’s structural/routing/behavioral tiers, Ponytail’s agentic harness.

**UCA layer affected**  
Evaluation tooling and skill release gates.

**Expected benefit**  
Evidence that the skill changes agent behavior in intended ways.

**Implementation cost**  
Medium.

**Risk**  
Model-dependent behavioral scores may be overinterpreted.

**Validation**  
No-skill controls, repeated runs, exact fixtures, deterministic graders, disclosed variance and limitations.

**Priority**  
**P0 — Adopt now.**

---

## Proposal 11 — Canonical Agent Skills source and generated adapters

**Why**  
Manual platform copies will drift and inflate maintenance.

**Source inspiration**  
Agent Skills specification; Ponytail’s shared skills, copy checks, and package generators.

**UCA layer affected**  
Skill packaging, release, CI.

**Expected benefit**  
Portable behavior with one semantic source.

**Implementation cost**  
Medium initially, low recurring.

**Risk**  
Platform-specific behavior may exceed what generators can express.

**Validation**  
Regeneration diff, semantic digest checks, host install and routing smoke tests.

**Priority**  
**P1.**

---

## Proposal 12 — Focused lens manifests

**Why**  
Explicit focus improves precision, but separate audit engines would fragment evidence.

**Source inspiration**  
Ponytail’s narrow over-engineering pass, Trail of Bits specialized workflows.

**UCA layer affected**  
Audit planner and report ordering.

**Expected benefit**  
Relevant analyzers and output without losing cross-domain safety evidence.

**Implementation cost**  
Low–medium.

**Risk**  
Users may interpret a focused lens as a full audit.

**Validation**  
Every lens declares included, required cross-check, omitted, and escalation capabilities; completion clearly labels lens scope.

**Priority**  
**P1.**

---

## Proposal 13 — Root-cause-derived variant investigations

**Why**  
A confirmed defect often implies related variants, but broad semantic searching creates noise.

**Source inspiration**  
Trail of Bits variant analysis.

**UCA layer affected**  
Investigative mode, adapter orchestration, finding relationships.

**Expected benefit**  
Systematic detection of recurring defect families.

**Implementation cost**  
Medium–high.

**Risk**  
False-positive explosion.

**Validation**  
Exact-to-general search ladder, per-stage precision, stop threshold, known-defect corpora.

**Priority**  
**P2 — Revisit after production v1.**

---

## Proposal 14 — Separate artifact and process cost reporting

**Why**  
A smaller implementation can still require more agent turns, tool calls, tokens, or elapsed time.

**Source inspiration**  
Ponytail benchmark corrections and independent issue results.

**UCA layer affected**  
Evaluation and reports.

**Expected benefit**  
More honest capability-to-weight analysis.

**Implementation cost**  
Low.

**Risk**  
Metrics may be compared across incompatible environments.

**Validation**  
Report environment and normalize only within matched benchmark arms.

**Priority**  
**P1.**

---

# Licensing and intellectual-property boundary

Observed repository licenses:

| Reference | License |
|---|---|
| Ponytail | MIT |
| Cloudflare Security Audit Skill | MIT |
| Meta SecPriv Skill | MIT |
| Superpowers | MIT |
| Addy Osmani Agent Skills | MIT |
| Aider | Apache-2.0 |
| Common Code Reviewer | Apache-2.0 |
| Agent Skills specification | Apache-2.0 |
| Trail of Bits Skills | CC BY-SA 4.0 |

Ponytail’s MIT license permits reuse subject to preserving the notice in substantial copied material.

The recommended course is still to implement UCA’s mechanisms independently:

- use the general concept of a reduction ladder;
- do not copy Ponytail’s exact skill wording;
- design UCA’s taxonomy from its own evidence model;
- write independent schemas and fixtures;
- cite inspirations in design documentation.

For Trail of Bits material, avoid copying or closely adapting text unless UCA is prepared to comply with CC BY-SA attribution and ShareAlike requirements. Treat its workflows as architectural inspiration and implement them independently.

Benchmark assets, configurations, and test corpora require the same license review as source and prose. Third-party notices and referenced upstream assets should be inspected before reuse.

---

# J. Final decision packet

## Adopt now

### 1. Reduction lens

Create a first-class UCA Reduction lens and the `uca-simplify` skill.

### 2. Safety floor

Require every reduction recommendation to establish preservation or explicitly report unknown status for applicable correctness, security, privacy, accessibility, reliability, compatibility, observability, performance, and regulatory floors.

### 3. Candidate-validation lifecycle

Add:

```text
candidate
→ validated
→ rejected
→ conflicting
→ needs_investigation
```

Retain validation and rejection evidence.

### 4. Completion-truth protocol

Require agents to inspect completion, revision, scope, required analyzers, limitations, and freshness before any completeness or cleanliness claim.

### 5. Skill evaluation harness

Implement:

```text
Tier 1 — structural
Tier 2 — trigger/routing
Tier 3 — behavioral
```

with no-skill controls, pressure cases, multiple runs, deterministic grading, and disclosed limitations.

### 6. Canonical portable skill source

Use Agent Skills as the canonical representation and generate thin host adapters with drift tests.

### 7. Concise finding cards

Add a progressive high-signal projection over full findings.

### 8. Reconsideration triggers

Extend accepted debt and waiver records with ceilings, triggers, expiry, and successor actions.

### 9. Stable IDs and rule fixtures

Ensure agent-visible findings retain canonical taxonomy IDs and stable rules have positive and near-miss fixtures.

### 10. Process-cost accounting

Measure agent/tool/context overhead separately from any implementation reduction.

---

## Adapt carefully

### Graph-ranked context projection

High value, but ranking omissions must remain visible. Begin with deterministic evidence-graph relationships rather than embeddings.

### Independent verification

Use for high-impact heuristic and AI findings, but do not force a multi-agent topology. The verifier can be an in-engine rule stage, a separate model call, a human review, or an adapter.

### Focused lenses

Use them as audit plans and report views over shared evidence. Every lens must disclose that it is not full-spectrum unless it is.

### Variant analysis

Add only in investigative mode after a known root cause, with exact-to-general search and explicit noise stops.

### Native/platform alternatives

Move this knowledge into versioned language/framework packs and adapters. Do not put a static universal catalog in the skill.

### Positive-pattern reporting

Keep justified complexity and healthy boundaries visible, but separate them from defects and avoid bloating every audit.

---

## Revisit later

- A dedicated `uca-explain` skill, only if routing tests show the primary skill misses finding-ID requests.
- Additional focused skills, only with demonstrated trigger or behavioral advantage.
- Multi-agent specialist audits.
- Remote model-based independent verification.
- Organization-wide agent-skill benchmark services.
- Automated suggestion of reconsideration triggers.
- Broader framework-specific reduction catalogs.
- Hosted collaborative audit review.
- Agent-generated remediation plans integrated into normal project governance.

---

## Do not adopt

### Persistent UCA mode

UCA should be explicitly invoked, not silently active across unrelated coding turns.

### Repeated full-rule injection

The skill should be progressively loaded, and durable invariants should live in engine contracts.

### Prompt-only UCA auditing

A prompt cannot substitute for repository identity, tool execution, normalized evidence, stable findings, or an Audit Bundle.

### Automatic fixes or refactors

This would violate UCA’s initial read-only and evidence-not-authority boundary.

### Hidden dependency or analyzer installation

Tooling remains explicit, pinned, trusted, and operator-owned.

### Manual platform copies

Generate adapters from the canonical skill source.

### Flat taxonomy explosion

Use a compositional reduction taxonomy with concise derived labels.

### Raw line-count optimization

Lines removed are one supporting observation, not the objective.

### Mandatory subagents

Use independent validation where it improves evidence; do not turn UCA into an agent orchestration framework.

### Hooks that rewrite repository content

The Addy `simplify-ignore` mechanism is inventive for a mutating simplifier, but it temporarily changes files, requires crash recovery, and has rename/placeholder edge cases. It is incompatible with UCA’s read-only audit boundary.

### AI-only blocking findings

AI remains a cited, model-dependent evidence source. It cannot supply deterministic authority.

---

# Final governing answer

The best agent skills do not show that UCA needs more prompts.

They show that UCA’s agent-facing layer needs a few precise, testable protocols:

```text
understand before judging
→ produce candidates
→ attempt to refute them
→ preserve rejected evidence
→ inspect completion before claiming success
→ load only the context needed
→ present the highest-value findings concisely
→ separate recommendation from authority
```

Ponytail’s most valuable contribution is to reveal that UCA’s broad simplification capabilities should be unified into an explicit **Reduction lens**. Trail of Bits, Cloudflare, and SecPriv show how to keep that lens from becoming noisy: generate candidates broadly, then validate or refute them. Aider shows how to make agent context bounded and evidence-directed. Superpowers and Addy’s eval system show how to prove that the skill actually changes behavior without teaching agents to overclaim. Common Code Reviewer and the Agent Skills specification show how to make that behavior stable, testable, and portable.

The resulting architecture remains:

```text
UCA engine
  owns repository truth, evidence, analysis, findings, and bundles

UCA skills
  route intent, invoke UCA, inspect completion, interpret evidence,
  and present results

External tools
  provide specialist evidence through adapters

Agents
  do not become the audit engine

Octon Mini
  governs trust, invocation, evidence use, decisions, and downstream work
```

That preserves UCA as a powerful, independently useful audit system while materially improving the way coding agents discover it, scope it, trust it, explain it, and act on its evidence.

## Turn 009

**Role:** User  
**Date/time:** Not available

Briefly, how would this work with Octon Mini?

---

## Turn 010

**Role:** Assistant  
**Date/time:** Not available

With Octon Mini, UCA should behave as an **external capability provider**, not as part of the harness itself.

The flow would be:

```text
User / Agent task
      ↓
Octon Mini
  decides whether code-audit evidence is needed
      ↓
UCA provider
  CLI / MCP / container
      ↓
UCA Audit Bundle
  findings + evidence + provenance + completion state
      ↓
Octon Mini
  validates receipt/provenance
  routes findings into the project task/decision lifecycle
      ↓
Human/agent decides what to do
```

Concretely, Octon Mini would do four things:

1. **Invoke UCA under governed authority.** Octon decides the permitted repository scope, whether project code may execute, whether network access is allowed, and which UCA audit mode/lens to request. UCA performs the audit but does not gain broader authority.

2. **Receive evidence, not commands.** UCA returns its Audit Bundle: stable findings, supporting evidence, confidence, analyzer coverage, limitations, and provenance. A UCA finding like “collapse this abstraction” is merely a recommendation.

3. **Turn worthwhile findings into normal Octon work.** For example:

```text
UCA finding
“P1 · de-abstract PaymentProvider”

        ↓

Octon decision/task
“Should PaymentProvider abstraction be removed?”

        ↓

project evidence + owner decision

        ↓

separate implementation task, if approved
```

4. **Preserve lifecycle and history.** Octon can associate a UCA finding ID with decisions, accepted debt, waivers, implementation tasks, validation results, and future re-audits. If UCA later reports the finding as resolved, recurring, or triggered for reconsideration, Octon can reconcile that with the project record.

The clean boundary is:

> **UCA determines what appears unnecessarily risky, costly, complicated, or removable. Octon Mini determines whether that evidence matters to the project, who may act on it, and what governed work happens next.**

I would keep UCA entirely out of Octon Mini’s implementation. Octon only needs a thin provider contract—something roughly like `discover → plan → run → inspect/compare` plus a durable receipt pointing to the UCA Audit Bundle.

---

## Turn 011

**Role:** User  
**Date/time:** Not available

What's our next step for UCA?

---

## Turn 012

**Role:** Assistant  
**Date/time:** Not available

The next step is to **stop expanding the architecture and build the smallest non-throwaway UCA kernel**.

I’d make the immediate milestone:

## Milestone 1 — UCA Architectural Kernel

Build one thin vertical slice that proves the architecture:

```text
repository
   ↓
uca discover
   ↓
uca plan
   ↓
uca audit
   ↓
UCA Audit Bundle
   ↓
uca inspect / compare
```

Specifically, in this order:

1. **Create the UCA repository and Rust workspace.**
2. **Commit the architectural charter**:
   - product boundary;
   - invariants;
   - read-only/non-authorizing rules;
   - engine vs skill vs adapter responsibilities;
   - threat model.
3. **Define the foundational schemas**:
   - `uca.audit-request.v1`
   - `uca.repository-identity.v1`
   - `uca.scope.v1`
   - `uca.audit-plan.v1`
   - `uca.observation.v1`
   - `uca.finding.v1`
   - `uca.audit-completion.v1`
   - `uca.audit-manifest.v1`
4. **Implement canonical identities**:
   - strict JSON parsing;
   - deterministic canonicalization;
   - SHA-256 content IDs;
   - schema validation.
5. **Implement the UCA Audit Bundle writer.**
6. **Build the authoritative engine skeleton** beneath:
   ```text
   uca discover
   uca plan
   uca audit
   uca inspect
   uca compare
   ```
7. Make the first audit intentionally simple: repository identity, scope, file inventory, and completion state—**no sophisticated analyzers yet**.
8. Prove that the same repository/request produces a reproducible bundle and that partial/failed analysis can never appear “clean.”

### Then add the first real differentiated intelligence

Once that kernel is solid:

```text
Git history
+ file/module dependency graph
+ exact duplication
+ cycles/SCCs
+ complexity × churn hotspots
+ stable finding fingerprints
```

That gets us to the **Minimum Viable Architecture** before Semgrep, CodeQL, AI, MCP, CI, or Octon integration complicate the system.

I would also incorporate two findings from the skill research **now**, because they affect foundational contracts:

- the **candidate → validate/refute → finding** lifecycle;
- the **Reduction/Simplification finding model + safety floor**.

Those are much harder to retrofit after `finding.v1` becomes stable.

### What I would explicitly *not* build yet

```text
Semgrep/CodeQL adapters
AI semantic analysis
MCP server
GitHub Action
OCI toolboxes
Octon Mini provider integration
hosted service
multiple agent-platform packages
```

Those should all attach to the proven kernel later.

So the immediate engineering target is very concrete:

> **Get `uca audit --repo .` to produce a schema-valid, content-addressed, reproducible Audit Bundle with exact repository identity, truthful completion semantics, and a small number of native evidence observations.**

Once that exists, nearly everything else we designed has a stable place to attach.

---

## Turn 013

**Role:** User  
**Date/time:** Not available

So this will essentially be a standalone skill that any harness can utilize?

---

## Turn 014

**Role:** Assistant  
**Date/time:** Not available

Yes, with one important distinction:

**UCA should be a standalone audit system that can be exposed through a portable skill—not merely a standalone skill.**

The architecture is:

```text
Universal Code Audit
│
├── UCA Engine
│   ├── CLI
│   ├── Audit Bundle
│   ├── analyzers/adapters
│   ├── evidence fusion
│   └── findings/comparison
│
├── Agent Skills
│   ├── uca-audit
│   └── uca-simplify
│
├── MCP interface
├── CI integration
├── OCI/container interface
└── future HTTP service
```

So essentially **any harness or coding agent can consume UCA through whichever interface it understands**:

```text
Octon Mini ─────────────→ UCA provider / CLI
Claude Code ────────────→ UCA skill + CLI/MCP
Codex ──────────────────→ UCA skill + CLI/MCP
GitHub Copilot ─────────→ UCA skill / CI
Gemini / OpenCode ──────→ UCA skill + CLI/MCP
CI pipeline ────────────→ UCA CLI/container
Custom agent harness ───→ CLI, MCP, or future API
Human developer ────────→ UCA CLI directly
```

The **skill is the agent-facing instruction layer**. It teaches an agent when and how to use UCA, but the actual auditing intelligence lives in the standalone engine.

That distinction gives us a major advantage: a harness does **not** need to adopt UCA's methodology, prompts, graph algorithms, scanners, or evidence machinery. It just needs to understand a tiny contract:

```text
discover capabilities
→ request/plan audit
→ run audit
→ consume Audit Bundle
→ inspect findings
```

And every environment gets the **same underlying audit result**, rather than Claude having one version of “UCA,” Codex another, and Octon Mini a third.

So the model I would use is:

> **UCA is a portable, standalone developer capability with an optional Agent Skill interface. Any sufficiently capable harness can utilize it without embedding UCA into the harness.**

That is also why building the engine kernel before the skill is important: it ensures the skill never accidentally becomes the product.

---

## Turn 015

**Role:** User  
**Date/time:** Not available

Can this serve as a test project that can serve for building other future standalone capabilities?

---

## Turn 016

**Role:** Assistant  
**Date/time:** Not available

Yes. UCA is actually a very good **reference project for proving the standalone-capability pattern** you’ll likely want to reuse later.

The key is to treat UCA as the **first implementation of a general pattern**, not to make UCA itself responsible for generalizing everything.

A reusable shape could look like this:

```text
Standalone Capability
│
├── Core Engine
│   └── domain-specific intelligence
│
├── Canonical CLI
│
├── Durable Result Contract
│   └── evidence/artifact bundle
│
├── Capability Manifest
│   ├── identity/version
│   ├── supported operations
│   ├── required access
│   ├── network behavior
│   ├── execution behavior
│   └── output contracts
│
├── Agent Skill
│   └── teaches agents when/how to use it
│
├── MCP Adapter
├── CI Adapter
├── OCI Packaging
└── Harness Provider Adapter
```

UCA would prove that this works end to end.

### What UCA can validate

It can answer several architectural questions before you build a second capability:

- Can one authoritative engine support humans, agents, CI, MCP, and harnesses without divergent behavior?
- Can capabilities remain independently versioned and independently useful?
- Can a harness discover and invoke them through a very small contract?
- Can access requirements be declared instead of implicitly assumed?
- Can the capability remain read-only and non-authorizing?
- Can results be immutable, content-addressed, provenance-rich artifacts?
- Can an agent skill remain thin instead of duplicating engine logic?
- Can platform-specific skill packages be generated from one canonical source?
- Can a capability be absent without breaking the harness?
- Can expensive or specialist functionality evolve independently of Octon Mini?

If those work well for UCA, you have strong evidence for a broader architecture.

### Future capabilities could then follow the same pattern

For example:

```text
Universal Code Audit
Repository Intelligence
Performance Investigation
Dependency Intelligence
Architecture Recovery
Documentation Verification
Test Effectiveness Analysis
Migration Analysis
Release Readiness
Incident Investigation
Research / Evidence Gathering
Formal Verification
Security Assessment
```

Each could have completely different internals while exposing roughly the same outer lifecycle:

```text
capabilities
→ plan
→ execute
→ completion
→ result bundle
→ inspect
```

The harness would not need to understand how any of them work internally.

### I would deliberately extract two standards from UCA

While building UCA, define these separately from UCA itself:

**1. Standalone Capability Manifest**

Something like:

```text
standalone-capability-manifest.v1
```

It describes:

- capability ID/version;
- operations;
- invocation methods;
- required repository access;
- project-code execution requirements;
- network requirements;
- filesystem writes;
- result schemas;
- compatibility;
- provenance;
- trust requirements.

**2. Evidence/Result Provider Contract**

For Octon Mini, initially keep this narrower:

```text
read_only_evidence_producer
```

That lets Octon consume UCA safely without prematurely designing a universal plugin/action runtime.

Later, if a second or third capability demonstrates the same needs, you can generalize based on evidence rather than speculation.

### The important constraint

I would **not** create a “Universal Capability Framework” before UCA exists.

That would risk designing abstractions for imaginary future tools.

Instead:

```text
Build UCA
   ↓
observe what is genuinely generic
   ↓
extract capability conventions
   ↓
build capability #2 using them
   ↓
identify what survives both
   ↓
stabilize the standalone-capability specification
```

That approach is very consistent with the architecture we’ve been developing: **extrapolate cautiously from demonstrated use, not hypothetical future intent.**

So yes—UCA can serve two purposes simultaneously:

> **A real, valuable standalone code-auditing product, and the proving ground for a reusable architecture through which Octon Mini and other harnesses can consume future independent capabilities without absorbing their implementation.**

I think that makes UCA an especially useful first capability to build.

---

## Turn 017

**Role:** User  
**Date/time:** Not available

Should I use Octon Mini to help build this or no?

---

## Turn 018

**Role:** Assistant  
**Date/time:** Not available

Yes—**use Octon Mini to help build UCA, but do not make UCA depend on Octon Mini.**

That gives you the best of both worlds: UCA becomes a real standalone capability, while Octon Mini gets exercised against a demanding external project.

I’d use Octon Mini for the development process:

- task and decision tracking;
- architecture decisions;
- scope and authority boundaries;
- implementation planning;
- validation and evidence capture;
- resumable work;
- release/readiness reviews;
- eventually exercising the external-capability-provider integration.

But keep UCA’s repository structurally independent:

```text
Octon Mini
  governs the work of building UCA
        ↓
UCA repository
  contains no Octon runtime dependency
  no Octon-specific core logic
  no assumption Octon is installed
```

The useful test is:

> If you removed Octon Mini tomorrow, could someone still clone UCA, build it, run `uca audit`, use its CLI, consume its Audit Bundle, and integrate it with another harness?

The answer should always be **yes**.

There is also a second reason to use Octon Mini: UCA can become a **dogfooding project for Octon Mini itself**. Building UCA will stress exactly the areas Octon Mini is intended to support—long-running architectural work, evolving decisions, evidence, external tooling, validation, handoff, and eventually standalone capability invocation. That should expose weak spots in Octon Mini naturally rather than through synthetic examples.

I’d therefore structure the relationship like this:

```text
Phase 1
Octon Mini helps build UCA.

Phase 2
UCA becomes independently usable.

Phase 3
Octon Mini consumes UCA through the external provider boundary.

Phase 4
Lessons from UCA inform the generic standalone-capability pattern.
```

The one thing I would avoid is using Octon Mini to generate a bunch of UCA-specific harness machinery before the UCA kernel exists. Let Octon govern the development; let **UCA own its product architecture**.

---

## Turn 019

**Role:** User  
**Date/time:** Not available

You suggested to build the smallest non-throwaway UCA kernel, however, I usually prefer to build out more full featured, fully capable products since we are leveraging AI to help build. What are your thoughts on this?

---

## Turn 020

**Role:** Assistant  
**Date/time:** Not available

I think your instinct is largely right for UCA. I would revise my earlier recommendation.

The reason I suggested the “smallest non-throwaway kernel” was **risk control**, not because I think UCA should be developed as a conventional MVP. With AI materially lowering implementation cost, it makes sense to aim much closer to the **intended product architecture from the beginning**.

The important distinction is:

> **Build a full-capability product in dependency order—not a tiny product that has to be redesigned later.**

AI changes the economics of building breadth, but it does **not** eliminate the hard risks: bad contracts, architectural coupling, inconsistent evidence semantics, false completeness, security boundaries, adapter behavior, reproducibility, and integration complexity. Those are precisely the things a tiny prototype can reveal before they become entrenched.

So I would shift the UCA strategy to something like this:

```text
Not:
tiny MVP → learn → redesign → expand

Instead:
design the real v1 architecture
        ↓
build its foundational contracts
        ↓
rapidly fill out the major capabilities
        ↓
continuously validate the integrated system
        ↓
ship a genuinely capable v1
```

In other words, the “kernel” should be an **integration checkpoint**, not the product target.

### What I would build toward now

I would actually target a fairly substantial first UCA release:

- production-shaped engine and Audit Bundle;
- deterministic repository identity and scope;
- planning/execution DAG;
- truthful completion semantics;
- file/module/symbol graphs;
- Git history, churn, ownership and co-change analysis;
- duplication and similarity;
- complexity/hotspot analysis;
- dependency analysis;
- dead/obsolete-code candidates;
- architecture/cycle/layer analysis;
- the Reduction/Simplification lens and safety floor;
- candidate → validate/refute → finding lifecycle;
- stable finding fingerprints and comparison across audits;
- Rust and Python as the first deep language packs;
- a few mature external-tool adapters;
- canonical CLI;
- OCI/container execution;
- CI integration;
- `uca-audit` and `uca-simplify` skills;
- MCP interface;
- reports/SARIF/interoperability;
- caching and incremental analysis;
- proper test/evaluation corpus.

That is **not an MVP in the usual sense**. It would already be a serious product.

I would still postpone a handful of things whose value depends on the foundation being proven: hosted SaaS, large numbers of language packs, dozens of adapters, elaborate collaboration features, autonomous remediation, and perhaps extensive remote-AI analysis.

### Where AI changes my recommendation most

Traditionally, one would deliberately minimize first-release scope because every feature has substantial implementation cost. With strong coding agents, the bottleneck shifts.

The question becomes less:

> “How little can we afford to build?”

and more:

> “How much can we build while still understanding, validating, and maintaining the resulting system?”

That latter constraint is much more relevant to UCA.

A coding agent can generate another 20,000 lines fairly cheaply. But if those lines create four competing execution paths, duplicate schemas, inconsistent adapter contracts, or tests that don't actually establish audit correctness, we've made the product worse.

So I would optimize UCA for **architectural completeness before feature minimalism**.

### A better definition of the first milestone

Instead of calling it the “smallest non-throwaway kernel,” I'd call it:

**UCA Foundation — the minimum complete architecture.**

It should prove every fundamental relationship:

```text
repo identity
    ↓
discovery
    ↓
capabilities
    ↓
audit request
    ↓
deterministic plan
    ↓
constrained execution
    ↓
raw evidence
    ↓
normalized observations
    ↓
candidate
    ↓
validation / refutation
    ↓
finding
    ↓
Audit Bundle
    ↓
inspection / comparison
```

Once that works, I wouldn't stop and deliberate about whether to build the rest. **We keep going toward the comprehensive product.**

The milestone exists because if we discover that `Finding`, `Evidence`, `Completion`, `Scope`, or `AuditPlan` is fundamentally wrong, I want to discover that before twenty analyzers depend on it.

### There is another advantage in your case

Because UCA is also intended to become the **reference implementation for future standalone capabilities**, building it relatively comprehensively is valuable.

A trivial UCA would only prove:

> “Octon Mini can invoke an external CLI.”

A serious UCA can prove:

> “A sophisticated independently versioned capability—with planning, permissions, long-running execution, durable evidence, adapters, caching, skills, MCP, containers, CI, partial results, provenance, and lifecycle semantics—can remain cleanly external to a harness.”

That's a much more useful architectural test.

So I would amend my previous advice to:

> **Design UCA as the full product now and build aggressively toward that vision using AI. But establish the foundational architecture in a strict dependency order, with working integration checkpoints, so AI-generated breadth never outruns our ability to prove the system is coherent and correct.**

That approach seems better suited to UCA than either extreme: neither a deliberately tiny MVP nor a “build everything simultaneously” big-bang implementation.

---

## Turn 021

**Role:** User  
**Date/time:** Not available  
**Preservation status:** Substantive reconstruction. The exact raw message export was not available to the packaging runtime after conversation-context compaction; the requirements below preserve the directive’s operative content and are mapped to the resulting canonical artifacts.

# UCA Full Product Build Packet v1 — Generation Directive

The user directed the assistant to act as principal product architect, specification editor, systems architect, security architect, developer-tooling architect, AI-team operating-model designer, verification architect, and technical program lead for Universal Code Audit.

The task was explicitly **not to build UCA yet**, but to transform the intellectual and architectural work from the conversation into a canonical, production-grade **Product Constitution + Executable Specification + AI Build Packet** suitable for placing at the root of a new UCA repository.

The package was required to make a new AI engineering team, with no access to the conversation, able to determine:

- what UCA is and why it exists;
- its mature v1 capabilities and explicit non-goals;
- established architectural decisions and invariants;
- subsystem ownership and forbidden responsibility leakage;
- the meaning of evidence, candidates, validation, findings, confidence, completion, recommendations, waivers, and priorities;
- how UCA remains standalone and harness-agnostic;
- how Octon Mini or another harness can consume UCA without becoming a UCA dependency;
- how CLI, CI, MCP, OCI/container, Agent Skills, adapters, and future interfaces relate to one authoritative engine;
- how AI agents may parallelize implementation safely;
- what requires centralized architecture ownership;
- what proof is required before capabilities or the release may be called complete;
- what research decisions were adopted, adapted, deferred, rejected, superseded, or remain open.

The user required a downloadable directory and ZIP named approximately:

```text
uca-full-product-build-packet-v1/
uca-full-product-build-packet-v1.zip
```

The required package content included:

1. product constitution;
2. architectural invariants;
3. production-shaped target architecture;
4. normative specifications;
5. machine-readable schemas;
6. capability matrix;
7. implementation dependency graph;
8. AI-team operating model;
9. verification and evaluation specification;
10. research and decision record;
11. security and authority model;
12. interface contracts;
13. Agent Skill specifications;
14. Octon Mini/external-provider boundary;
15. mature-release Definition of Done;
16. initial workstream and task packets;
17. accessible visible conversation history;
18. provenance mapping;
19. packet manifest;
20. packet-integrity validation tooling.

The directive established the source precedence:

```text
1. The build-packet generation directive
2. Latest explicit user decisions
3. Earlier established architectural decisions
4. Explicitly supplied UCA/Octon artifacts
5. Primary external research
6. Reasonable architectural inference
```

Important conclusions were to be classified as:

```text
ESTABLISHED
ACCEPTED
PROPOSED
DEFERRED
REJECTED
SUPERSEDED
OPEN QUESTION
```

The required normative authority hierarchy was:

```text
Product Charter
      ↓
Architectural Invariants
      ↓
Normative Specifications / Schemas
      ↓
Accepted ADRs
      ↓
Capability Matrix / Release Criteria
      ↓
Workstream Plans
      ↓
Individual Task Instructions
      ↓
Agent implementation choices
```

The governing product position was restated:

> **Universal Code Audit is an independent, harness-agnostic, production-grade code-audit and repository-intelligence capability. It produces evidence, findings, interpretations, limitations, and recommendations. It does not possess authority over the repository or project. Its findings never authorize changes.**

UCA had to remain useful without an agent harness, Octon Mini, MCP, AI interpretation, or network access. Octon Mini could govern the work of building UCA and later consume it, but could not become a UCA runtime dependency.

The development philosophy was explicitly revised from a tiny conventional MVP to:

> **Build the full-capability product in dependency order—not a tiny product that must later be redesigned.**

The Minimum Complete Architecture was defined as an integration checkpoint rather than the mature product ambition. Architectural completeness was to be favored over feature minimalism, while AI-generated breadth was not allowed to outrun the team’s ability to understand, verify, maintain, and govern the architecture.

The directive required substantive canonical artifacts covering:

- `CHARTER.md`;
- `spec/invariants.md`;
- `ARCHITECTURE.md`;
- the canonical audit lifecycle;
- candidate validation and attempted refutation;
- evidence classes;
- a transparent confidence vector;
- truthful completion semantics;
- the finding model and stable fingerprinting;
- the Reduction/Simplification model and non-reducible safety floor;
- reduction evidence and benefit vectors;
- reconsideration triggers;
- Continuous, Periodic, and Investigative tiers;
- the durable Audit Bundle;
- substantive JSON Schema 2020-12 contracts;
- repository identity and scope;
- security and execution rights;
- out-of-process/OCI adapter protocol;
- language-agnostic core and language packs;
- depth-aware capability matrix;
- graph intelligence and deterministic context projection;
- optional AI/semantic interpretation;
- transparent prioritization;
- canonical CLI, CI, MCP, and OCI contracts;
- `uca-audit` and `uca-simplify` Agent Skills;
- agent completion-truth protocol;
- concise finding-card projection;
- skill and engine evaluation;
- benchmark honesty;
- research and licensing record;
- standalone-capability pattern;
- Octon Mini external-provider integration;
- AI-team authority, workstreams, task and validation contracts;
- architectural change control;
- implementation dependency graph and build stages;
- implementation-ready initial tasks;
- mature v1 release criteria;
- transcript, decision maps, source maps, manifest, checksums, and validator.

The directive required a systematic internal-consistency review across charter, invariants, interfaces, schemas, completion, evidence, AI, recommendations, Reduction, permissions, CLI/MCP/CI equivalence, Octon independence, skill/engine separation, licensing, capability depth, release criteria, and task parallelism.

It prohibited over-generalizing UCA into a speculative universal capability platform before at least a second real standalone capability provides evidence for generalization.

The final package was required to be validated by actually checking required files, JSON, YAML, JSON Schemas, manifest paths, identifiers, checksums, placeholders, transcript coverage, decision coverage, capability/release alignment, Octon independence, and ZIP integrity.

This reconstructed turn is non-normative historical material. The directive’s binding result is represented by the Product Charter, invariants, normative specifications and schemas, ADRs, capability matrix, release criteria, workstream/task contracts, and packet-integrity records.

---

## Turn 022

**Role:** Assistant  
**Date/time:** Not available  
**Preservation status:** Substantive reconstruction; the exact original response was unavailable after context compaction.

The assistant reported that a substantial portion of the packet had been created but explicitly stated that the ZIP, manifest, checksums, validation run, evaluation specification, Octon integration, standalone-capability document, full transcript, provenance maps, and final consistency review were incomplete. The response listed the completed core artifacts and accurately declined to claim that the requested package was finished or validated.

Key reported counts at that intermediate point were approximately 136 substantive files, 33 JSON Schemas, 56 capabilities, 49 decisions, 16 ADRs, 18 workstreams, 27 task packets, 38 established/accepted decisions, and 8 open questions.

The assistant’s governing conclusion was that the working directory was a strong partial repository substrate but could not yet be treated as the canonical finalized build packet.

---

## Turn 023

**Role:** User  
**Date/time:** 2026-08-31

Please complete the downloadable package.

---

## Turn 024

**Role:** Assistant  
**Date/time:** 2026-08-31

I’m finishing the missing provenance, evaluation, integration, validation, manifest, checksum, transcript, and archive layers, then I’ll run the packet’s own integrity checks.

---

## Turn 025

**Role:** Assistant  
**Date/time:** 2026-08-31

The core packet is intact at 135 files. I’m auditing its schemas, identifiers, unresolved markers, and missing deliverables before adding the final layers.

---

## Turn 026

**Role:** Assistant  
**Date/time:** 2026-08-31

The packet’s existing JSON and YAML parse cleanly, and all 33 schemas pass Draft 2020-12 meta-schema checks. I’m now adding claim-oriented evaluation and integration contracts rather than superficial placeholders.

---

## Turn 027

**Role:** Assistant  
**Date/time:** 2026-08-31

The evaluation, Octon integration, standalone-capability, schema-catalog, fixture, and provenance documents are now in place. The remaining heavy item is preserving the full visible UCA thread before manifesting and signing the packet.

---

## Turn 028

**Role:** Assistant  
**Date/time:** 2026-08-31

The transcript recovery is farther along than expected: the exact thread through the complete development blueprint and full agent-skill research directive is already present. I’m appending the remaining visible turns and documenting any non-verbatim recovery explicitly.

---

---

# Family Architecture Extension

The following turns extend the inherited UCA conversation record. They are historical source material, not normative authority.

## Turn 029

**Role:** User  
**Date/time:** 2026-08-31, exact message timestamp not available in packet runtime

**Preservation:** Verbatim short request

> What other skills backed, external capabilities would be highly useful for Octon Mini?

## Turn 030

**Role:** Assistant

**Preservation:** Substantive reconstruction from the visible response; not represented as a byte-for-byte export

The assistant proposed a family of external specialist capabilities rather than adding domain implementations to Octon Mini. The prioritized candidates were Verification / Test Assurance, Specification Conformance, Supply-Chain Intelligence, Runtime Investigation, API / Contract Assurance, Release Assurance, UI / Browser Assurance, Infrastructure Assurance, and Database / Migration Assurance.

The answer established the recurring boundary:

```text
specialized capability
     ↓
evidence
     ↓
recommendation
     ↓
Octon governed decision
     ↓
separate authorized action
```

It recommended building Verification Assurance, Specification Conformance, and Supply-Chain Intelligence after UCA, with Release Assurance later as an evidence aggregator. It also described the outer standalone-capability shape: core engine, canonical CLI, durable result, manifest, Agent Skill, MCP, CI, OCI, and harness-provider adapter.

## Turn 031

**Role:** User

**Date/time:** 2026-08-31

**Preservation:** Substantive requirements reconstruction. The packaging runtime did not expose the current visible message as a raw conversation-export object. This turn therefore does not claim byte-for-byte fidelity.

The user issued the **Standalone Capability Family — Canonical Architecture + Project Seed Packet v1** generation directive. The directive required a self-contained validated ZIP that establishes family constitution, shared architecture, authority/security/evidence/completion/interface conventions, Octon integration, research, decisions, evaluation, provenance, conversation coverage, manifest/checksums, and one substantive project seed plus project-generation prompt for each of ten capabilities:

1. Universal Code Audit;
2. Verification Assurance;
3. Specification Conformance;
4. Supply-Chain Intelligence;
5. Runtime Investigation;
6. API / Contract Assurance;
7. Release Assurance;
8. UI / Browser Assurance;
9. Infrastructure Assurance;
10. Database / Migration Assurance.

The directive established these governing statements:

> **Keep the harness small. Make external intelligence strong. Connect them through narrow, evidence-centered contracts.**

> **Capabilities determine domain-specific evidence. Harnesses determine trust, authority, project meaning, and downstream action.**

> **Build real capabilities first. Generalize only what survives real use.**

It expressly prohibited premature creation of a universal capability framework, required shared conventions to be marked established versus provisional, required one authoritative engine per capability, required durable results and truthful completion, required explicit permissions and no hidden installation/network, and required every capability seed to support generation of its own full production-grade build packet without the original conversation.
