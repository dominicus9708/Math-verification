# Dependency ledger

This file records dependency order that must not be silently reversed.

## D1 — Radius-seven closure before refined X bound

Required order:

`old X bound` -> `finite radius 0..7 closure` -> `d75 >= 8` -> `first-75 defect floor` -> `Christoffel real-envelope conversion` -> `refined X upper bound`.

Rule: the refined X bound is not used retroactively to justify radius-seven closure unless separately rerun.

## D2 — Refined X bound before shell-conditioned pruning

Shell-specific physical restrictions derived from the refined interval remain downstream of that interval.

## D3 — 14-root forest after late-shell elimination

The 14-root forest is retained only after certified late-shell elimination.

## D4 — H/L grammar before target specialization

Universal dual H/L grammar precedes target Christoffel/Stern-Brocot specialization.

## D5 — Projective observation before membership use

Required interface:

`projective observation` -> `formation/order restriction` -> `ordinary displacement/defect` -> `eta floor` -> `physical pruning`.

Rejected shortcut: `adic mismatch -> membership rejection`.

## D6 — Local defect floors before global accumulation

Local floors are not automatically additive. Use ranked atoms, fixed-cylinder ordering minimum, or a certified semiring/block composition.

## D7 — Fixed-cylinder greedy only after cylinder sequence is fixed

Right-to-left maximal-position greedy is exact inside an already fixed cylinder sequence, not for selecting the carry/cylinder path.

## D8 — Bellman merge only inside exact future-control classes

One `P_min` label is legal only when histories share the exact future control/payload state required by the active theorem.

## D9 — Synchronized checkpoint reconstruction

The checkpoint dyadic and ternary observations are residues of the same ordinary checkpoint `Z`.

Closed order:

`independent pre-defect X/L_- corridor` -> `SAFE Z corridor` -> `right-H affine z_H <-> Z mod 3^28` -> `Z mod 2^27` -> `coprime CRT` -> `corridor span < CRT modulus` -> `at most one ordinary Z`.

No marginal-density multiplication or independence assumption is permitted.

## D10 — No retroactive defect bound in checkpoint CRT seam

The checkpoint singleton theorem uses only the independent pre-defect `X` and debit corridors, not the later defect-derived refined X upper bound.

## D11 — Checkpoint exposure before checkpoint-conditioned source fiber

Only after one ordinary `Z` is independently exposed may the root cylinder `X=r+2^h m` be intersected with

\[
75\,2^{33}<3X-Z<112\,2^{33}.
\]

The exact root-depth cap is

\[
K_h=\left\lceil\frac{37\,2^{33}}{3\,2^h}\right\rceil.
\]

Small fiber cardinality is not membership.

## D12 — Debit reconstruction without circularity

`L_-=3X-Z` is used only after `Z` is independently exposed and `X` remains in its independently defined source cylinder.

## D13 — Hybrid join before singleton expansion

Full source singleton expansion is not a prerequisite of checkpoint synchronization.

Allowed order:

`compressed right-H acceptance` -> `checkpoint exposure` -> `checkpoint-conditioned source fiber` -> `deep direct enumeration or shallow Bellman refinement`.

## D14 — Terminal precision must be consumed before cut-state design

For a terminal `3^L` predicate crossing a processed right block with `q_B` one-events, the exact exported precision is

\[
L_{cut}=\max(0,L-q_B).
\]

At the current cut `q_B=397,573,380`, so `L=24,28,47` all export zero ternary digits.

Rule: once this predicate is discharged inside the right H block, do not carry its ternary residue across the cut as an active state coordinate merely because it existed at the terminal boundary.

Zero residual precision is not path uniqueness and does not authorize merging different boundary/grammar controls.

Canonical theorem:

- `../theorems/CRITICAL_CUT_TERMINAL_PRECISION_ABSORPTION.md`.

## D15 — Terminal ranked-one window before full right-H traversal

For equal-count target/candidate correction difference modulo `3^L`, all ranks earlier than the final `L` one-events vanish because their coefficients contain `3^L`.

Under target dominance, every locally legal final-rank suffix extends by the packed prefix `b_r=r-1`.

Therefore for the current checkpoint precision `L=28`, pure target-dominance residue existence is a 28-gate problem and does not depend on enumerating the preceding `397,573,352` right-H one-events.

Rule: do not rebuild a full 397M-one traversal to answer this terminal residue-existence predicate. If an additional H/L boundary/control label is required, derive and attach that control separately.

Canonical theorem:

- `../theorems/TERMINAL_RANK_WINDOW_DOMINANCE_COMPLETION.md`.

## D16 — Local Route-B closure before global claims

Even complete closure of all 14 A0 `s=1` Route-B roots would close only that module.

Required later dependencies:

`Route-B local closure` -> `Route-A + s>=2 + remaining branches` -> `global branch completeness` -> `Collatz conclusion`.

## Change-control rule

Whenever a new theorem shortens the chain:

1. state exactly which prior obligation is discharged;
2. preserve old chronological evidence;
3. update `CANONICAL_PROOF_STACK.md`, `OPEN_GATES.md`, and the active frontier in the same maintenance cycle;
4. do not silently reinterpret old finite results under new assumptions.
