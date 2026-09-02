# Open gates

This register contains unresolved obligations only. Closed lemmas belong in the proof map / theorem index rather than being mixed into this list.

## G1 — Predicate-driven source/Bellman execution

**Module:** C4

The forward exact state

`source/control × interval payload × P_min`

remains valid for the directed physical gate.

It is no longer necessary to force all 14 roots to ordinary-X singleton depth before checkpoint synchronization. The checkpoint-conditioned source-fiber theorem permits immediate source contraction after one ordinary `Z` is exposed.

Required output now:

- use forward `P_min` refinement where the active source fiber is still too large;
- preserve exact export coordinates queried by the synchronized join;
- report finite state counts as execution evidence only.

Status: **ACTIVE, predicate-driven rather than mandatory full expansion**.

## G2 — Compressed right-H acceptance over prescribed synchronized observations

**Module:** C4/C5

Closed subgates:

- lazy terminal-ternary observation;
- critical-cut right localization for `L=24,28,47`;
- one-dimensional projective interval payload;
- prescribed-cylinder singleton threshold `m>=18` for the current right H block;
- exact affine synchronization `z_H = 2^s Z-C(H_s^*) mod 3^28`;
- synchronized `2^27 × 3^28` CRT checkpoint singleton exposure;
- **critical-cut terminal precision absorption**: the right H block has `q_R=397,573,380`, so the active 24-, 28-, and 47-trit predicates export zero ternary digits across the cut.

Consequently, the checkpoint `z_H mod 3^28` is an input observation to be accepted or rejected inside the right H factor. Its projective residue coordinate is fully consumed before the cut and is not part of the left/source join key.

Remaining obligation:

construct a compact exact representation of which prescribed `z_H mod 3^28` observations are feasible in the right-H language, together with only the exact boundary/grammar control coordinates needed after the observation is discharged.

Required output:

- compact multi-gate right-H acceptance state;
- exact merge rule within identical boundary/control classes;
- accepted/rejected prescribed `z_H` observations or an equivalent symbolic cylinder representation;
- boundary/control export with **no residual checkpoint ternary carry coordinate**;
- exact finite state counts clearly separated from theorem claims.

Known restrictions:

- zero residual precision does not imply a unique right-H path;
- a prescribed cylinder may be empty/singleton without implying a unique carry path;
- different boundary/grammar controls remain distinct;
- physical defect/cost data may be forgotten only under a separate theorem;
- local carry greedy remains forbidden.

Canonical new theorem:

- `../theorems/CRITICAL_CUT_TERMINAL_PRECISION_ABSORPTION.md`.

Status: **ACTIVE — principal current structural gate, reduced state dimension**.

## G3 — Hybrid synchronized 14-root join

**Module:** C4/C5

The checkpoint exposure seam, terminal precision-absorption seam, and checkpoint-conditioned source-fiber cardinality seam are CLOSED.

For each right-H accepted synchronized observation and compatible dyadic observation:

1. expose zero or one ordinary `Z` in the SAFE corridor;
2. intersect each relevant source root with the exact debit-compatible parameter interval;
3. enumerate deep fibers when small;
4. continue compressed source/Bellman refinement for shallow fibers;
5. join only the surviving boundary/control coordinates — the consumed checkpoint ternary carry is not reintroduced;
6. preserve every coordinate required for the full pre-bridge membership test.

Per exposed `Z`, exact deep-root caps include:

- `f>=24`: at most 3,668 source parameters;
- `f>=27`: at most 510;
- `f>=29`: at most 115;
- `f>=32`: at most 16;
- `f>=35`: at most 3;
- `f=37`: at most 1.

Do not multiply marginal counts or infer membership from a small fiber.

Status: **OPEN after G2 accepted-observation representation; principal join immediately following G2**.

## G4 — Full pre-bridge correction-language membership

**Module:** C5

For every remaining joined `(source fiber, Z, right-H boundary/control state)`, prove membership or nonmembership in the exact long pre-bridge formation/correction language.

Checkpoint/source exposure alone is insufficient.

Status: **OPEN after G3**.

## G5 — Ordinary checkpoint/debit coherence after exposure

**Module:** C5

Closed pieces:

- synchronized checkpoint singleton exposure;
- exact source-fiber interval/cardinality after one exposed `Z`.

Remaining obligation:

verify the actual joined `X`, `Z`, debit `L_-=3X-Z`, and any later renewal condition without circularity.

Status: **OPEN after G3; exposure/fiber subgates CLOSED**.

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

`G2 accepted-observation compression -> G3, with G1 activated only where the checkpoint-conditioned source fiber remains too large -> G4/G5/G6/G7 -> G8/G9 -> G10`.

The synchronized checkpoint CRT seam, critical-cut precision-absorption seam, and source-fiber cardinality seam are closed and should not be recomputed unless an upstream hypothesis changes.
