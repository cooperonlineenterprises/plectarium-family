# Infrastructure Assurance Capability Model

## Governing operation

The product transforms an exact declared subject into attributable evidence, a bounded domain conclusion, truthful completion, and a durable result.

## Subject model

- Terraform/OpenTofu plan
- Kubernetes manifests
- Helm chart
- IAM policy
- container/deployment configuration
- cloud policy
- infrastructure diff

Subject identity must be stable enough to answer exactly what state the result describes. The generated project must define revision/version/environment/workload or artifact identity appropriate to the domain.

## Primary operations

- `discover`: identity, operations, depth, providers, tools, environments, and likely permissions;
- `plan`: exact subject, scope, providers, tools, effects, resources, expected evidence, and limitations;
- `execute` or domain equivalent: perform only the accepted plan;
- `inspect`: explain completion, evidence, and conclusions without reanalysis when unnecessary;
- `compare`: compare compatible results and expose incompatibility;
- `report`: produce human and standard projections;
- `doctor`: diagnose availability and environment without hidden installation.

## Domain conclusion model seed

Potential states:

- `coherent`
- `coherent_with_conditions`
- `policy_violation`
- `destructive_change`
- `privilege_expansion`
- `exposure_change`
- `high_risk`
- `incomplete`

The project-generation phase must define exact semantics, transition/lifecycle, scope qualification, and whether a state is evidence, conclusion, candidate, or limitation. It must avoid exaggerated language—for example, ordinary tests do not establish mathematical proof, static compatibility does not establish behavioral compatibility, and a no-op infrastructure plan does not establish production safety outside declared assumptions.

## Capability classes

- `read_only_evidence_producer` (`PROVISIONAL`)
- `controlled_environment_evidence_producer` (`PROVISIONAL`)

Classes are descriptive only. Exact permissions remain plan-specific.
