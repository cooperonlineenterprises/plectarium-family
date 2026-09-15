# Plectarium Capability Family

This repository is the independent authority home for the Plectarium
capability family. It governs family-level identity, invariants, architecture,
narrow interoperability contracts, capability generation seeds, conformance
fixtures, and family release records. It contains no capability engine and no
Plectarium control-plane implementation.

Plectarium is the suite brand and is part of the Octon ecosystem. These remain
separate concerns:

| Concern | Authority home |
|---|---|
| Family constitution and shared contracts | This repository |
| Suite product experience and control plane | Independent `plectarium` repository |
| Capability semantics and releases | Each independent capability repository |
| Developer checkout/bootstrap coordination | Independent workspace repository |
| Harness-specific governance | The relevant harness repository |

## Repository map

- [`standalone-capability-family-packet-v1/`](standalone-capability-family-packet-v1/README.md)
  is the authoritative versioned family packet.
- [`imports/historical/`](imports/historical/) preserves accepted historical
  source bytes with explicit provenance and limitations.
- [`.agent/`](.agent/START_HERE.md) contains the live, non-authorizing project
  harness and work records.
- [`.agents/`](.agents/README.md) contains optional constrained agent
  capabilities.
- [`project-dossier/`](project-dossier/README.md) separates intended state,
  dated observations, conformance, plans, provenance, validation, and handoff.

## Validation

Run from this repository root. No dependency installation is authorized by
these commands.

```text
python3 -B .agent/scripts/validate.py --check
python3 -B -m unittest discover -s .agent/tests -p 'test_*.py'
"${PLECTARIUM_PACKET_PYTHON:-python3}" -B standalone-capability-family-packet-v1/scripts/validate-packet.py
```

For a high-assurance integrity refresh, run only the designated writers after
all source edits and packet change control are complete, then rerun the
read-only checks:

```text
"${PLECTARIUM_PACKET_PYTHON:-python3}" -B standalone-capability-family-packet-v1/scripts/validate-packet.py --refresh-projections --write-manifest --refresh-checksums
python3 -B .agent/scripts/refresh.py --refresh
python3 -B .agent/scripts/validate.py --check
```

The packet validator requires PyYAML and `jsonschema`. Select an interpreter
explicitly with `PLECTARIUM_PACKET_PYTHON`; `python3` is the fallback. The
family home may provide an untracked local binding, while tracked commands
remain host-neutral.

## Current readiness

The high-assurance repository foundation is adopted and validated under
`.agent/tasks/TASK-0001-family-repository-foundation.md`; exact private initial
publication is completed under `TASK-0002`. The closure commit's own equality
is verified as direct post-commit evidence. This setup does not establish
product, security, compliance, release, or production readiness.
