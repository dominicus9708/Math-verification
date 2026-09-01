# Dependency ledger

This file records dependency order that must not be silently reversed.

## D1 — Radius-seven closure before refined X bound

Required order:

`old X bound`
→ `finite radius 0..7 closure`
→ `d75 >= 8`
→ `first-75 defect floor`
→ `Christoffel real-envelope conversion`
→ `refined X upper bound`.

Rule: the refined X bound is not used retroactively to justify radius-seven closure unless a separate certificate reruns that closure.

## D2 — Refined X bound before shell-conditioned pruning

Shell-specific physical restrictions that were derived from the refined interval remain downstream of that interval.

Rule: any later stronger shell bound must declare whether it is independent or downstream.

## D3 — 14-root forest after late-shell elimination

The 14-root forest is retained only after certified late-shell elimination.

Rule: do not present the 14 roots as an unconditional partition of every possible threshold deviation.

## D4 — H/L grammar before target specialization

Universal dual H/L grammar is established before target Christoffel/Stern-Brocot specialization.

Rule: arbitrary H/L candidates are not Christoffel words merely because the target is.

## D5 — Projective observation before membership use

Required interface:

`projective observation`
→ `formation/order restriction`
→ `ordinary displacement/defect`
→ `eta floor`
→ `physical pruning`.

Rejected shortcut: `adic mismatch -> membership rejection`.

## D6 — Local defect floors before global accumulation

Local floors are not automatically additive. Use ranked atoms, fixed-cylinder ordering minimum, or a certified semiring/block composition.

## D7 — Fixed-cylinder greedy only after cylinder sequence is fixed

Right-to-left maximal-position greedy is exact inside an already fixed cylinder sequence, not for selecting the carry/cylinder path.

## D8 — Bellman merge only inside exact future-control classes

One `P_min` label is legal only when histories share the exact future control/payload state required by the active theorem.

## D9 — Synchronized checkpoint reconstruction

The checkpoint dyadic and ternary observations are residues of the **same** ordinary checkpoint `Z`.

The exposure chain is CLOSED in this order:

`independent pre-defect X/L_- corridor`
→ `SAFE ordinary Z corridor`
→ `right-H affine z_H <-> Z mod 3^28`
→ `Z mod 2^27`
→ `coprime CRT class mod 2^27*3^28`
→ `corridor span < CRT modulus`
→ `at most one ordinary Z`.

Canonical theorem:

- `../theorems/SYNCHRONIZED_CHECKPOINT_CRT_SINGLETON.md`.

Rules:

- do not multiply marginal dyadic/ternary densities;
- do not assume independence;
- checkpoint singleton exposure does not itself prove orbit/membership compatibility.

## D10 — No retroactive defect bound in checkpoint CRT seam

The synchronized checkpoint singleton certificate intentionally uses only

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33}
\]

and

\[
75\,2^{33}<L_-<112\,2^{33}.
\]

Rule: the later defect-derived refined X upper bound is not a dependency of the checkpoint-exposure theorem.

## D11 — Checkpoint exposure before checkpoint-conditioned source fiber

Only after a coherent synchronized observation has exposed one ordinary checkpoint `Z` may the source fiber be conditioned on that `Z`.

Required chain:

`synchronized observation`
→ `zero/one ordinary Z in SAFE corridor`
→ `substitute X=r+2^h m into 75*2^33 < 3X-Z < 112*2^33`
→ `exact open m interval`
→ `source-fiber intersection/cardinality`.

The exact root-depth cap is

\[
K_h=\left\lceil\frac{37\,2^{33}}{3\,2^h}\right\rceil.
\]

Canonical theorem:

- `../theorems/SYNCHRONIZED_CHECKPOINT_SOURCE_FIBER_BOUND.md`.

Rules:

- the source-fiber theorem uses the independent debit corridor, not the later defect-derived refined X bound;
- small fiber cardinality is not membership;
- one candidate `(X,Z)` is not automatically same-orbit connectivity;
- do not multiply source-fiber counts by marginal dyadic/ternary ratios.

## D12 — Debit reconstruction without circularity

`L_-=3X-Z` couples X, Z, and debit.

The source-fiber theorem uses this identity only after `Z` is independently exposed and `X` remains in its independently defined source cylinder.

Rule: later ordinary debit/renewal compatibility must still be checked on the actual joined source/checkpoint state. Terminal debit data are not treated as an X-independent oracle.

## D13 — Hybrid join before singleton expansion

Full source singleton expansion is not a required dependency of checkpoint synchronization.

Allowed order:

`compressed right-H export`
→ `checkpoint exposure`
→ `checkpoint-conditioned source fiber`
→ `direct deep-fiber enumeration or shallow compressed Bellman refinement`.

Rule: choose direct enumeration only after the exact fiber is actually small. Shallow roots remain compressed when their checkpoint-conditioned fiber is still large.

This changes the computational order, not the mathematical membership obligation.

## D14 — Local Route-B closure before global claims

Even complete closure of all 14 A0 `s=1` Route-B roots would close only that module.

Required later dependencies:

`Route-B local closure`
→ `Route-A + s>=2 + remaining branches`
→ `global branch completeness`
→ `Collatz conclusion`.

## Change-control rule

Whenever a new theorem shortens the chain:

1. state exactly which prior obligation is discharged;
2. preserve old chronological evidence;
3. update `CANONICAL_PROOF_STACK.md`, `OPEN_GATES.md`, and the active frontier in the same maintenance cycle;
4. do not silently reinterpret old finite results under new assumptions.
