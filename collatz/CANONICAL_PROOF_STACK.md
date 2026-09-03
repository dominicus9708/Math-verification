# Canonical live proof stack

This file records the shortest current live implication chain.  A listed implication is exact or explicitly SAFE only in its stated domain.  Global Collatz closure remains OPEN.

## S0 — Physical A0 domain

Work in the certified `A0, s=1` Route-B formation with the fixed long target parameters

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701.
\]

Status: **DOMAIN / imported**.

## S1 — First-75 necessary defect

Certified finite arithmetic yields the SAFE necessary condition

\[
d_{75}\ge8.
\]

Status: **CERTIFIED arithmetic -> SAFE**.

## S2 — Exact 14-root source forest

Every current Route-B candidate lies in one retained first-defect root

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`

after the stated upstream SAFE cuts.

Each family is represented exactly as

\[
X=r+2^h m,
\qquad T^h(X)=y+3^q m.
\]

Status: **EXACT family representation after SAFE inputs**.

## S3 — Persistent source/control state

Let

\[
Q(h)=\min\{q:3^q>2^h\},
\qquad S=q-Q(h).
\]

Then `q=Q(h)+S`, and the justified persistent S10 core is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S)}.
\]

Source residue `r` may not be discarded before source-sensitive predicates are discharged.

Status: **EXACT / CLOSED state minimization for the active pre-checkpoint predicates**.

## S4 — Exact source-preserving transition

For a next-one valuation branch `a`,

\[
m\equiv(2^a-y)3^{-q}\pmod{2^{a+1}},
\]

and the resulting `m=rho_a+2^(a+1)k` refinement preserves exact affine source/current-state channels.

Exact residual inversion remains

\[
R=2^nZ-3^qY,
\qquad a=v_2(R).
\]

Certified multibit blocks compile finite valuation-jump trees without merging source payloads.

Status: **EXACT / CLOSED transition stack**.

## S5 — Jump-8 source frontier

Pure-ballot jump-8 frontier:

- `14,224` source cylinders;
- `26,859,837,368,845,079,186` source integers.

First-75 tail-defect tightening leaves

\[
26{,}859{,}837{,}368{,}588{,}270{,}254.
\]

Status: **EXACT finite frontier after SAFE inputs**.

## S6 — Bounded-displacement horizon chain

For future one-ranks write

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0,
\]

and let `D_r` count displaced ranks among the first `r` future one-events.

Let `H_c` be the longest exact source-preserving pure-ballot horizon achievable with `D_r<=c`.

Current certified table:

\[
\boxed{
H_0=40,
\ H_1=44,
\ H_2=45,
\ H_3=48,
\ H_4=50.
}
\]

For `c=4`, exactly two horizon-49 source parents remain: one in shard 3 and one in shard 24.  Shard 3 is empty at 50; shard 24 is live at 50 and empty at 51.  All other shards are empty already at 49.

Hence

\[
\boxed{D_{51}\ge5}.
\]

No source merging or horizon extrapolation is used.

Status: **EXACT / CLOSED through budget 4 on the current finite frontier**.

## S7 — Cumulative future-defect floor

Each displaced rank contributes normalized future defect

\[
\epsilon_r>\frac1{12}.
\]

Therefore S6 gives

\[
\boxed{\eta_{future}>\frac5{12}}.
\]

For monotone endpoint rejection this is safely weakened to

\[
\eta_{future}\ge\frac5{12}.
\]

The older `>=1/4` and `>=1/3` floors are superseded, not added.

Status: **SAFE consequence of exact finite horizon theorem**.

## S8 — Current canonical population

Applying the `>=5/12` endpoint floor to the first-75-tightened source intervals gives

\[
\boxed{26{,}859{,}837{,}368{,}480{,}843{,}030}
\]

source integers.

The incremental `>=1/3 -> >=5/12` rejection is

\[
\boxed{25{,}290{,}635}.
\]

All `14,224` source intervals remain nonempty.

Canonical export:

- `src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

Status: **EXACT endpoint arithmetic / zero whole-cylinder closures**.

## S9 — Directed physical predicate split

The exact directed `P_min` predicate remains valid, but a global future-reachability cutoff shows that roughly `82.095%` of the first-75-tightened source population can never be rejected by `P_min`, even with all remaining target-correction budget.

Therefore cumulative displacement is not a complete membership mechanism.  The lower sector requires an independent source-sensitive obstruction.

Status: **EXACT predicate localization; insufficient for closure**.

## S10 — Late checkpoint observations

Terminal ternary observation activates only at

\[
q_{rem}=28.
\]

The first 27 post-checkpoint parity bits determine

\[
Z\bmod2^{27}.
\]

The final 28 one-events determine the required ternary observation

\[
Z\bmod3^{28}.
\]

Only then may the synchronized CRT seam be used.  A coherent CRT pair exposes at most one ordinary checkpoint `Z` in the certified corridor.

Status: **EXACT observation/localization interface**.

## S11 — Source/checkpoint same-orbit realization

For an exposed or proposed checkpoint `Z`, the remaining obligation is not mere CRT compatibility but

\[
\boxed{
\text{CRT compatibility}
+
\text{source/debit compatibility}
+
\text{same-orbit provenance}.
}
\]

Exact residual correction inversion is available for a fully specified pair, but family-level source/checkpoint membership is not yet closed.

Status: **OPEN principal membership gate**.

## S12 — A0 `s=1` Route-B closure

Required conclusion: every family from all 14 roots is exactly rejected or discharged through the complete pre-checkpoint/checkpoint/tail obligations.

Status: **OPEN**.

## S13 — Global completion

Route-A, all `s>=2` sectors, remaining branches, and global branch completeness must be independently closed before any Collatz conclusion.

Status: **OPEN**.

---

# Immediate next work

1. Compute `H_5` from the current `>=5/12` canonical frontier using sparse source-preserving decision recursion.
2. Compare its incremental endpoint gain with execution cost before pushing to much larger `c`.
3. In parallel, construct the exact source/checkpoint join
   \[
   \text{source family}\leftrightarrow(z_2,z_H)\leftrightarrow\text{right-H/checkpoint family}.
   \]
4. Do not carry checkpoint observations before their activation boundary.

# Forbidden shortcuts

- extrapolating `H_0..H_4` to an asymptotic displacement law;
- adding the `1/4`, `1/3`, and `5/12` floors as independent quantities;
- exact-pair uniqueness -> family uniqueness;
- equal control/template state -> equal source payload;
- dropping source residue `r` early;
- correction/formation/displacement re-expression -> independent pruning;
- CRT compatibility -> same orbit;
- checkpoint exposure -> source realization;
- multiplying marginal survival fractions without independence;
- finite Route-B progress -> global Collatz.
