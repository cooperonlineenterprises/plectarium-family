# Handoff Start

> Navigation only. Reinspect the repository and current instructions before
> resuming work.

## Current position

- Project Blueprint 1.0.0 `high-assurance` snapshot generated on 2026-08-31
  and locally adopted.
- Active task: none; `TASK-0002` is complete.
- Accepted repository decision: `DEC-0001`.
- Fresh bounded evidence: `EVD-0001`, `EVD-0002`, `EVD-0003`.
- Current conformance: `FIND-0001` transitional; `FIND-0002` conformant for
  the exact identity-source byte comparison.
- External effects observed: exact private remote creation and bounded normal
  publication; closure equality is direct post-commit evidence.
- Product implementation: intentionally absent.
- Local repository foundation is validated; publication is incomplete and
  product, security, compliance, release, and production readiness are not
  established.

## Resume in this order

1. Read applicable instructions and `.agent/START_HERE.md`.
2. Inspect repository and source-control state; `family/` was not a Git
   repository when `EVD-0001` was recorded.
3. Read completed `TASK-0002`, `TASK-0001`, `DEC-0001`, `EVD-0003`, and
   `REV-0002`.
4. Read `project-dossier/AUTHORITY.md` and the machine-readable requirements,
   findings, plan, RAIDQ, sources, and quality gates.
5. Reconfirm final local/tracking/remote equality and clean worktree from
   direct evidence before relying on publication state.
6. Use the final published family commit, packet version, packet manifest
   digest, checksum digest, and used-path hashes as immutable downstream pins.

The packet validator uses an already-configured Python 3.14 runtime because
the unqualified local `python3` lacks its third-party dependencies. Do not
install anything under this task.
