# Open gates

This register contains unresolved obligations only. Closed lemmas belong in the proof map / theorem index rather than being mixed into this list.

## G1 — Predicate-driven source/Bellman execution

**Module:** C4

The forward exact state `source/control × interval payload × P_min` remains valid for the directed physical gate.

Use it only where a checkpoint-conditioned source fiber remains too large for direct exact handling.

Status: **ACTIVE, predicate-driven**.

## G2 — Actual 28-gate right-H synchronized acceptance

**Module:** C4/C5

Closed subgates now include:

- lazy terminal-ternary observation;
- critical-cut right localization for `L=24,28,47`;
- max-slack quotient at fixed projective carry;
- one-dimensional projective interval payload;
- prescribed-cylinder singleton threshold `m>=18` for the current right H block;
- exact affine synchronization `z_H = 2^s Z-C(H_s^*) mod 3^28`;
- synchronized CRT checkpoint singleton exposure;
- terminal precision absorption: zero checkpoint ternary digits cross the critical cut;
- terminal ranked-one window theorem: modulo `3^L`, only the final `L` ranked one-events are observable;
- packed-prefix target-dominance completion of every locally legal terminal suffix.

Therefore the current pure target-dominance checkpoint acceptance problem is exactly a **28-gate** ordered-slack/projective problem, not a `397,573,380`-gate problem.

The omitted `397,573,352` earlier one-events need not be enumerated for this residue-existence predicate.

Remaining obligation:

execute the exact 28-gate quotient on the actual last-28 target capacities and obtain either:

1. a compact accepted set of prescribed `z_H mod 3^28` observations, with exact gate-by-gate state counts; or
2. a certified obstruction showing what additional quotient coordinate is required.

For the first 11 gates (`m=28..18`), each prescribed projective cylinder is empty or singleton. Lower precisions remain potentially multi-valued and must use exact quotienting rather than raw slack enumeration.

If the full H/L join asks for an additional boundary/grammar label beyond target dominance, attach that finite control to the quotient key and intersect it separately. Do not re-expand the unobservable earlier ranked ones merely to recover it.

Status: **ACTIVE — principal current executable gate, finite 28-gate form**.

## G3 — Hybrid synchronized 14-root join

**Module:** C4/C5

The checkpoint exposure seam, precision-absorption seam, terminal rank-window seam, and checkpoint-conditioned source-fiber seam are CLOSED.

For each G2-accepted synchronized observation:

1. expose zero or one ordinary `Z` in the SAFE corridor;
2. intersect each relevant source root with the exact debit-compatible parameter interval;
3. enumerate deep fibers when small;
4. continue compressed source/Bellman refinement for shallow fibers;
5. join only surviving boundary/control coordinates;
6. preserve every coordinate required for the full pre-bridge membership test.

Per exposed `Z`, exact cumulative deep-root caps remain:

- `f>=24`: 3,668;
- `f>=27`: 510;
- `f>=29`: 115;
- `f>=32`: 16;
- `f>=35`: 3;
- `f=37`: 1.

Status: **OPEN immediately after G2 accepted-observation execution**.

## G4 — Full pre-bridge correction-language membership

**Module:** C5

For every remaining joined `(source fiber, Z, right-H boundary/control state)`, prove membership or nonmembership in the exact long pre-bridge formation/correction language.

Status: **OPEN after G3**.

## G5 — Ordinary checkpoint/debit coherence after exposure

**Module:** C5

Verify actual joined `X`, `Z`, debit `L_-=3X-Z`, and any later renewal condition without circularity.

Status: **OPEN after G3; exposure/fiber subgates CLOSED**.

## G6 — Tail first-passage / post-checkpoint compatibility

**Module:** C5

Close the exact tail language and physical first-passage obligations for every pre-bridge survivor.

Status: **OPEN**.

## G7 — C4F / renewal / global formation compatibility

**Module:** C5

Provide an explicit invariant/state theorem if these predicates are needed.

Status: **OPEN**.

## G8 — Route-A completion

**Module:** C6

Complete the independent Route-A lower-bound/closure obligation.

Status: **OPEN**.

## G9 — All-surplus `s>=2`

**Module:** C6

Generalize or separately close surplus sectors not covered by the current `s=1` factorization.

Status: **OPEN**.

## G10 — Global branch completeness

**Module:** C0/C6

Prove all counterexample classes are covered by the final branch partition and that closure of every module implies ordinary Collatz.

Status: **OPEN**.

---

# Priority order

`G2 28-gate execution -> G3, with G1 only on large conditioned fibers -> G4/G5/G6/G7 -> G8/G9 -> G10`.

Closed synchronized seams should not be recomputed unless an upstream hypothesis changes.
