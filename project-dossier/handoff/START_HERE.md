# Handoff Start

> Navigation only. Reinspect the repository and current instructions before
> resuming work.

## Current position

- Project Blueprint 1.0.0 `high-assurance` snapshot generated on 2026-08-31
  and locally adopted.
- Active task: none. Project-family relocation `TASK-0008` is complete.
- Accepted repository decisions: `DEC-0001` through `DEC-0004`.
- Fresh bounded migration evidence: `EVD-0012` and `EVD-0013`; independent
  review: `REV-0008`.
- Current conformance: checkpoint v2 preserves its false family checksum lock
  as history; v3 corrects it and preserves provisional-divergence sequencing.
- Historical external effects: exact private remote creation and bounded
  normal foundation, closure, and checkpoint publication. Current direct
  evidence confirms the historical v3 publication; no current external effect
  or authority exists.
- Product implementation: intentionally absent.
- Local repository foundation and checkpoint publication are validated; and
  product, security, compliance, release, and production readiness are not
  established.

## Resume in this order

1. Read applicable instructions and `.agent/START_HERE.md`.
2. Inspect repository and source-control state at the canonical
   `repos/plectarium-family` checkout.
3. Read completed `TASK-0008`, `EVD-0012`, `EVD-0013`, and `REV-0008`.
4. Read `project-dossier/AUTHORITY.md` and the machine-readable requirements,
   findings, plan, RAIDQ, sources, and quality gates.
5. Treat `SRC-0008` and all earlier publication authority as consumed history;
   do not push without a new exact operator authorization.
6. Keep shared contracts provisional or unresolved and the shared runtime
   deferred until its accepted family trigger is satisfied.

The packet validator uses the explicit local `PLECTARIUM_PACKET_PYTHON` binding
with a `python3` fallback. Do not install dependencies implicitly.
