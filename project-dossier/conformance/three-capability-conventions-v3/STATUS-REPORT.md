# Three-Capability Conventions Checkpoint v3 Erratum

**Outcome:** `PASS_WITH_PROVISIONAL_DIVERGENCE`  
**Successor scope:** V2 lock correction and sequencing validity only  
**Authority effect:** None

## Correction

At clean family commit
`02d61dc63791d45885d48c280d3ff27ce76e56f7`, direct SHA-256 verification
proves:

- packet manifest:
  `54116db0e4f518ffe793df3d3ebd2b87064f00aab10b373bf1909f9126b24867`;
- packet checksum ledger:
  `e0134782dff26755d450f2aa2117d4a8d8afebbf53578e51c9dbbb809fabf4ee`.

V2 recorded a different checksum-ledger digest. V1 and v2 remain immutable.
Direct inspection shows v1 already contains the correct digest; v3 supersedes
v2 for lock identity and sequencing validity.

## Disposition

The corrected lock restores the profile-qualified v2 sequencing result:

- Verity remains `legacy_pre_family_1_2` with no family-schema conformance
  claim.
- Titra and Ortha remain packet-specific profiles.
- Cross-packet schema identity is repository+commit+packet+path+digest.
- Bare cross-packet `$id` registries are prohibited.
- Imports require verified bundle resolution and consumer-owned transformation.
- Compatibility remains unknown until implemented and tested.
- Completion refinements remain capability-specific.
- Shared contracts remain provisional/unresolved.
- Shared SDK/runtime remains deferred.
- Genea, Echo, Harmia, Iris, Janus, and Atlas may proceed.
- Sibyl remains last.

No capability or family packet was edited.

## Publication

V3 is local. Publishing the v1/v2/v3 checkpoint record set requires new
explicit authority for exactly one corrective family commit and one normal
push to `origin/main`, followed by equality and clean-worktree verification.
`TASK-0007` is blocked; repository files grant no authority.

