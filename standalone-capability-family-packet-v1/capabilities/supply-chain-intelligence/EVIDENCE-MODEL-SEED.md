# Supply-Chain Intelligence Evidence Model Seed

## Primary evidence

- component inventory
- dependency paths
- advisories
- reachability/exposure context when supportable
- license declarations
- maintainer/lifecycle signals
- signatures and attestations
- registry/package origin

## Evidence requirements

Every material evidence item should identify producer, version/configuration, exact subject, scope, time/freshness, class, raw/source reference, assumptions, limitations, and reproducibility posture.

The generated project must define which family evidence classes apply and which domain refinements are needed. It must not collapse runtime observation, static inference, imported human assertion, AI interpretation, and unavailability into one undifferentiated confidence value.

## Contradiction and absence

Supporting, contradicting, unavailable, stale, and inapplicable evidence must remain visible. A missing provider or denied permission is evidence of incomplete verification/analysis, not evidence that the subject passed.

## Imported sibling results

Potential inputs include:

- universal-code-audit

Imported evidence preserves source capability/version/result identity, completion, subject/scope, evidence class, freshness, provenance, and limitations. Derived conclusions cite the imported result.

## Durable payload

The project must define the capability-specific payload of the Supply-Chain Intelligence Bundle rather than forcing it into UCA’s finding schema. The provisional shared envelope should be evaluated, not assumed stable.
