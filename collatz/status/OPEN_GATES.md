# Open gates

This register contains unresolved obligations only. Closed lemmas belong in the proof map / theorem index rather than being mixed into this list.

## G1 — 14-root forward family execution

**Module:** C4

Run the exact forward family state on all 14 source roots with

`source/control × interval payload × P_min`

and quantify where whole-family physical closure occurs before singleton expansion.

Required output:

- exact node state and merge rule;
- reproducible root-level certificate;
- closed/unresolved counts without probability language;
- exact export families for the synchronized join.

Status: **ACTIVE**.

## G2 — Backward right-H projective/export filter

**Module:** C4/C5

Several former G2 subgates are now CLOSED:

- lazy terminal-ternary observation;
- critical-cut right localization for `L=24,28,47`;
- one-dimensional projective interval payload;
- prescribed-cylinder singleton threshold sharpened to `m>=18` for the current right H block;
- exact affine synchronization
  `z_H = 2^s Z-C(H_s^*) mod 3^28`;
- synchronized `2^27 × 3^28` CRT checkpoint singleton exposure.

The remaining G2 obligation is not checkpoint exposure itself. It is to export only those compressed right-H projective/carry states that can supply the synchronized observation required by the join, without flat enumeration of all carry residues.

Required output:

- compact multi-gate right-H state where more than one prescribed carry/cylinder remains possible;
- exact export coordinates queried by G3;
- state counts / exact finite execution evidence clearly separated from theorem claims.

Known constraints:

- prescribed cylinders are empty/singleton for `m>=18`;
- singleton prescribed cylinder does not imply singleton carry path;
- carry base cannot generally be discarded;
- one-layer injectivity does not imply whole-path injectivity;
- local carry greedy remains forbidden.

Status: **ACTIVE, narrowed**.

## G3 — Exact synchronized 14-root forward/backward join

**Module:** C4/C5

Join

`14-root source/control × interval payload × P_min`

with the right-H synchronized observation/export state at an exact boundary.

The checkpoint part of the join is now deterministic: each coherent pair

`(Z mod 2^27, z_H mod 3^28)`

admits at most one ordinary checkpoint `Z` in the certified SAFE corridor.

The join must still prove that a given source/right-H state actually supplies a coherent pair and must preserve every boundary/control coordinate queried later.

Do not multiply marginal counts or assume left/right independence.

Status: **OPEN after G1/G2 export states are explicit; next principal join**.

## G4 — Full pre-bridge correction-language membership

**Module:** C5

For every remaining joined family, prove membership or nonmembership in the exact long pre-bridge formation/correction language.

Checkpoint/boundary exposure alone is insufficient.

Status: **OPEN after G3**.

## G5 — Ordinary checkpoint/debit coherence after exposure

**Module:** C5

The synchronized checkpoint singleton **exposure subgate is CLOSED** by

- `../theorems/SYNCHRONIZED_CHECKPOINT_CRT_SINGLETON.md`;
- `../src/A0_s1_routeB_synchronized_checkpoint_CRT_singleton_certificate.py`.

Remaining obligation: for a joined source/right-H family that supplies the synchronized observation, verify compatibility of the reconstructed ordinary checkpoint with the required source `X`, debit `L_-=3X-Z`, and any later ordinary renewal predicate without circularity.

Status: **OPEN after G3; exposure itself CLOSED**.

## G6 — Tail first-passage / post-checkpoint compatibility

**Module:** C5

Close the exact tail language and physical first-passage obligations for every pre-bridge survivor.

Status: **OPEN**.

## G7 — C4F / renewal / global formation compatibility

**Module:** C5

Provide an explicit invariant/state theorem if these predicates are needed. Do not assume a local pure-ballot/projective quotient preserves a complete C4F Boolean state.

Status: **OPEN**.

## G8 — Route-A completion

**Module:** C6

Complete the independent Route-A lower-bound/closure obligation.

Status: **OPEN**.

## G9 — All-surplus `s>=2`

**Module:** C6

Generalize or separately close the surplus sectors not covered by the current `s=1` factorization.

Status: **OPEN**.

## G10 — Global branch completeness

**Module:** C0/C6

Prove that all counterexample classes are covered by the final branch partition and that closure of every module implies the ordinary Collatz conjecture.

Status: **OPEN**.

---

# Priority order

Current priority is

`G1 || narrowed G2 -> G3 -> G4/G5/G6/G7 -> G8/G9 -> G10`.

The synchronized checkpoint CRT seam is no longer a blocker and should not be recomputed unless an upstream hypothesis changes.
