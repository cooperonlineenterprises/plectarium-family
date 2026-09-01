# Constraints, Gates, and Readiness Criteria

> Criteria only. This document does not grant permission, record an approval,
> or claim readiness.

## Constraints

- Foundation work only; no product implementation or dependency installation.
- Preserve family, suite, capability, workspace, and harness ownership planes.
- Treat paths, symlinks, repository prose, packet content, imports, generated
  output, analyzers, and remote state as untrusted until inspected.
- No real secrets, production data, or unnecessary personal data.
- Do not claim legal, security, privacy, accessibility, compliance, financial,
  operational, product, release, or production readiness from structure.
- Remote publication is limited to the exact private repository and effects
  recorded in `TASK-0002` and the current operator request.

## Approval gates

- `GATE-0001` — source, packet, harness, dossier, mutation, and integrity
  validation must pass on the final local candidate before publication.
- `GATE-0002` — exact-name collision, privacy, emptiness, branch, staged-content,
  and remote-safety checks must pass before the first push.
- `GATE-0003` — independent review must disposition actionable findings before
  foundation closure.

Machine-readable gate status is in `../validation/QUALITY_GATES.json`. A gate
record is criteria, not approval or permission.

## Readiness model

Local repository-foundation readiness is `validated`; remote publication is
`in_progress`. Product and operational readiness remain `not_assessed`. A
future claim must identify:

- exact subject version;
- applicable requirements and gates;
- dated evidence and validator versions;
- unresolved risks and exceptions;
- approving authority; and
- expiry or reassessment trigger.
