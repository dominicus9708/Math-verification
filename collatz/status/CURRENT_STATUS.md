# Current status — 2026-09-03

## Current branch

Research branch: `collatz-stage4-window-threshold`.

Primary active object: `A0, s=1, Route-B` long-membership closure.

Canonical resume file:

- `../frontier/A0_S1_ROUTEB.md`.

## Exact retained family

Current first-defect roots:

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Each live source family is exact:

\[
X=r+2^h m,
\qquad T^h(X)=y+3^q m,
\]

with a finite integer parameter interval.

The persistent S10 source/control state remains

\[
\boxed{(r,y,m_{lo},m_{hi},h,S)},
\qquad S=q-Q(h).
\]

## Canonical jump-8 population

Pure-ballot jump-8 population:

\[
26{,}859{,}837{,}368{,}845{,}079{,}186.
\]

After first-75 tail-defect tightening:

\[
26{,}859{,}837{,}368{,}588{,}270{,}254.
\]

Cumulative bounded-displacement endpoint floors now reach

\[
\boxed{H_4=50}.
\]

Therefore horizon 51 forces

\[
\boxed{D_{51}\ge5}
\]

and hence

\[
\boxed{\eta_{future}>\frac5{12}}.
\]

Using the safe endpoint weakening `>=5/12`, the current population is

\[
\boxed{26{,}859{,}837{,}368{,}480{,}843{,}030}.
\]

The current source-cylinder count remains `14,224`; no whole interval is closed by this chain.

Downstream source export:

- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

## Exact bounded-displacement horizon table

\[
\boxed{
H_0=40,
\quad H_1=44,
\quad H_2=45,
\quad H_3=48,
\quad H_4=50.
}
\]

The `c=4` exceptional structure is exact:

- at horizon 49, only shard 3 and shard 24 have one live parent each;
- shard 3 is empty at horizon 50;
- shard 24 is still live at horizon 50 and empty at horizon 51.

Thus the finite global maximum is exactly 50.  No extrapolation is used.

Canonical files:

- `../theorems/FIVE_DISPLACEMENT_HORIZON_PRUNING.md`;
- `../src/A0_s1_8jump_c4_h49_shard_certificate.py`;
- `../src/A0_s1_8jump_c4_exception_horizon_certificate.py`;
- `../src/A0_s1_8jump_five_displacement_eta_pruning_certificate.py`;
- `../audits/S10_FIVE_DISPLACEMENT_HORIZON_PRUNING_AUDIT.md`.

## Sequential pruning audit

The future-defect floors are nested bounds on the same quantity and must not be added:

- `>=1/4` from `D_46>=3`;
- `>=1/3` from `D_49>=4`;
- `>=5/12` from `D_51>=5`.

The latest `5/12` floor supersedes the older two.

The exact incremental `1/3 -> 5/12` rejection is

\[
25{,}290{,}635.
\]

No marginal survival fractions are multiplied.

## Principal bottleneck

Bounded-displacement pruning remains valid but has so far shortened only upper tails of existing intervals.  It has not closed a source cylinder.

The more important unresolved mathematical interface is still

\[
\boxed{\text{source-controlled exact correction/checkpoint membership}}.
\]

The lower approximately `82.095%` `P_min`-unreachable sector especially requires a predicate independent of the directed `P_min` defect mechanism.

Late checkpoint observations remain:

\[
z_2=Z\bmod2^{27},
\qquad
z_H=Z\bmod3^{28}.
\]

A coherent CRT pair exposes at most one ordinary `Z` in the certified corridor, but residue compatibility alone is not source realization or same-orbit provenance.

## Immediate next work

1. Compute `H_5` from the new `>=5/12` canonical frontier using sparse source-preserving recursion.
2. Compare the additional pruning gain with its computational cost before continuing to much larger `c`.
3. In parallel, build the exact source/checkpoint join:
   \[
   \text{source family}\leftrightarrow(z_2,z_H)\leftrightarrow\text{checkpoint/right-H family}.
   \]
4. Require source/debit compatibility and same-orbit provenance after CRT exposure.
5. Keep checkpoint observations late-activated and keep source residue `r` until source-sensitive obligations are discharged.

## Still OPEN

- `H_5` and any higher bounded-displacement horizons;
- compact source-controlled full correction-language membership;
- exact 14-root source/checkpoint/correction joins;
- checkpoint/debit/tail realization;
- `A0,s=1,Route-B` closure;
- Route-A;
- all `s>=2` sectors;
- global branch completeness;
- Collatz.

## Forbidden shortcuts

- extrapolating `H_0..H_4` to an asymptotic law;
- adding `1/4`, `1/3`, and `5/12` floors;
- equal control state -> equal source payload;
- exact-pair uniqueness -> family uniqueness;
- CRT compatibility -> same orbit;
- terminal dominance acceptance -> membership;
- small source fiber -> membership;
- finite Route-B progress -> global Collatz.
