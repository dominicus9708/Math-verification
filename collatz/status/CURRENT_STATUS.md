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

The exact `c=5`, horizon-51, 64-shard decision on the current `>=5/12` frontier gives

\[
\boxed{\#\{D_{51}\le5\text{ paths}\}=0}.
\]

Therefore

\[
\boxed{H_5\le50},
\qquad
\boxed{D_{51}\ge6},
\]

and hence

\[
\boxed{\eta_{future}>\frac12}.
\]

Using the safe endpoint weakening `>=1/2`, the current canonical population is

\[
\boxed{26{,}859{,}837{,}368{,}455{,}538{,}464}.
\]

The source-cylinder count remains `14,224`; no whole interval is closed by this chain.

Downstream source export:

- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

## Exact bounded-displacement status

Certified exact equalities through budget four:

\[
\boxed{
H_0=40,
\quad H_1=44,
\quad H_2=45,
\quad H_3=48,
\quad H_4=50.
}
\]

For budget five, the new exact result is only

\[
\boxed{H_5\le50}.
\]

`H_5=50` is not claimed because the horizon-51 emptiness test does not itself supply a horizon-50 `D<=5` witness.

Reachability evidence:

- GitHub Actions run `33756884264`;
- `../src/A0_s1_8jump_c5_h51_shard_probe.py`.

Canonical files:

- `../theorems/SIX_DISPLACEMENT_HORIZON_PRUNING.md`;
- `../src/A0_s1_8jump_six_displacement_eta_half_pruning_certificate.py`;
- `../audits/S10_SIX_DISPLACEMENT_HORIZON_PRUNING_AUDIT.md`.

## Sequential pruning audit

The future-defect floors are nested bounds on the same quantity and must not be added:

- `>=1/4` from `D_46>=3`;
- `>=1/3` from `D_49>=4`;
- `>=5/12` from `D_51>=5`;
- `>=1/2` from `D_51>=6` on the current `>=5/12` frontier.

The latest `1/2` floor supersedes the older floors.

The exact incremental `5/12 -> 1/2` rejection is

\[
\boxed{25{,}304{,}566}.
\]

The cumulative `>=1/2` removal from the first-75-tightened source set is

\[
132{,}731{,}790.
\]

No marginal survival fractions are multiplied.

## Principal bottleneck

Bounded-displacement pruning remains valid but has so far shortened only upper tails of existing intervals. It has not closed a source cylinder.

The more important unresolved mathematical interface is

\[
\boxed{\text{source-controlled exact correction/checkpoint membership}}.
\]

The lower approximately `82.095%` `P_min`-unreachable sector especially requires a predicate independent of the directed `P_min` defect mechanism.

Late checkpoint observations remain

\[
z_2=Z\bmod2^{27},
\qquad
z_H=Z\bmod3^{28}.
\]

A coherent CRT pair exposes at most one ordinary `Z` in the certified corridor, but residue compatibility alone is not source realization or same-orbit provenance.

## Immediate next work

1. Make the source/checkpoint join the principal path:
   \[
   \text{source family}\leftrightarrow(z_2,z_H)\leftrightarrow\text{checkpoint/right-H family}.
   \]
2. Locate and normalize the exact export schemas for the left source family, `z_H`, checkpoint/right-H family, and `z_2`.
3. Form a synchronized CRT candidate only after both residues activate.
4. Require source/debit compatibility and exact same-orbit provenance after CRT exposure.
5. Keep source residue `r` until all source-sensitive obligations are discharged.
6. Treat higher bounded-displacement budgets as secondary unless they yield a structural gain or favorable cost/benefit.

## Still OPEN

- exact `H_5` equality (only `H_5<=50` is known);
- compact source-controlled full correction-language membership;
- exact 14-root source/checkpoint/correction joins;
- checkpoint/debit/tail realization;
- `A0,s=1,Route-B` closure;
- Route-A;
- all `s>=2` sectors;
- global branch completeness;
- Collatz.

## Forbidden shortcuts

- extrapolating finite `H_c` values to an asymptotic law;
- `H_5<=50 -> H_5=50` without a horizon-50 witness;
- adding `1/4`, `1/3`, `5/12`, and `1/2` floors;
- equal control state -> equal source payload;
- exact-pair uniqueness -> family uniqueness;
- CRT compatibility -> same orbit;
- terminal dominance acceptance -> membership;
- small source fiber -> membership;
- finite Route-B progress -> global Collatz.
