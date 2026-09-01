# Handoff Start

> Navigation only. Reinspect the repository and current instructions before
> resuming work.

## Current position

- Project Blueprint 1.0.0 `high-assurance` snapshot generated on 2026-08-31
  and locally adopted.
- Active task: `TASK-0007` (`review`); `TASK-0006` is complete.
- Accepted repository decisions: `DEC-0001` through `DEC-0004`.
- Fresh bounded evidence: `EVD-0001` through `EVD-0011`.
- Current conformance: checkpoint v2 preserves its false family checksum lock
  as history; v3 corrects it and preserves provisional-divergence sequencing.
- External effects observed: exact private remote creation and bounded normal
  foundation, closure, and v1/v2 checkpoint publication. The v3 corrective
  commit and push remain pending at this recorded boundary.
- Product implementation: intentionally absent.
- Local repository foundation and checkpoint publication are validated; and
  product, security, compliance, release, and production readiness are not
  established.

## Resume in this order

1. Read applicable instructions and `.agent/START_HERE.md`.
2. Inspect repository and source-control state; `family/` was not a Git
   repository when `EVD-0001` was recorded.
3. Read completed `TASK-0006`, in-review `TASK-0007`, `DEC-0004`,
   `EVD-0009` through `EVD-0011`, `REV-0007`, and `CHK-0007`.
4. Read `project-dossier/AUTHORITY.md` and the machine-readable requirements,
   findings, plan, RAIDQ, sources, and quality gates.
5. Reconfirm final local/tracking/remote equality and clean worktree from
   direct evidence before relying on publication state; the corrective commit
   cannot attest its own subsequent push.
6. Create exactly one corrective commit, push it once normally to the exact
   family `origin/main`, and verify local/tracking/live-remote equality plus a
   clean worktree; report completion directly without a second evidence commit.
7. After that direct verification, use v3 profiles for Genea through Atlas;
   keep shared contracts provisional/unresolved and Sibyl last. Treat
   `SRC-0008` as consumed and do not perform a later family push.

The packet validator uses an already-configured Python 3.14 runtime because
the unqualified local `python3` lacks its third-party dependencies. Do not
install anything under this task.
