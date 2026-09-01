# Release Assurance Evaluation Seed

## Claims the project must prove

- known ready/not-ready cases
- stale-result rejection
- scope incompatibility detection
- upstream provenance preservation
- exception handling
- no-publication authority tests

## Required corpus classes

- golden positive cases with known expected evidence/conclusions;
- near-miss negatives that look similar but should not produce the conclusion;
- contradictory evidence cases;
- provider/tool unavailable, denied, stale, timed-out, unsupported, and corrupt cases;
- malicious subject/input/tool-output cases;
- cross-interface equivalence cases;
- result identity, checksum, and comparison cases;
- authority-pressure cases specific to the product boundary;
- performance and large-subject cases.

## Evaluation honesty

The generated project must report scope, versions, environments, failures, sample count, variance, and process cost. More conclusions/findings are not automatically better. Ordinary software verification must not be called mathematical proof. External tool benchmark claims do not establish this product’s performance.

## Skill evaluation

Identity tests MUST verify exact use of Sibyl, descriptive-name and character-name routing, rejection of aliases, and evidence-centered language that does not imply authority.

Use no-skill controls and fresh contexts. Measure routing, operation selection, permission review, canonical invocation, completion inspection, truthful language, evidence/authority distinction, escalation, and downstream handoff.
