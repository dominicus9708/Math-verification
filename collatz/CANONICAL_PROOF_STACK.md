# Canonical live proof stack

This file records the shortest current live implication chain. A listed implication is exact or explicitly SAFE only in its stated domain. Global Collatz closure remains OPEN.

## S0 — Physical A0 domain

Work in the certified `A0, s=1` Route-B formation with fixed target

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701.
\]

Status: **DOMAIN / imported**.

## S1 — First-75 necessary defect

Certified finite arithmetic gives the SAFE necessary condition

\[
d_{75}\ge8.
\]

Status: **CERTIFIED arithmetic -> SAFE**.

## S2 — Exact 14-root source forest

Every current Route-B candidate lies in one retained first-defect root

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`

after the stated upstream SAFE cuts.

Each source family is represented exactly by

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m.
\]

Status: **EXACT family representation after SAFE inputs**.

## S3 — Persistent source/control state

Let

\[
Q(h)=\min\{q:3^q>2^h\},
\qquad S=q-Q(h).
\]

Then `q=Q(h)+S`, and the justified persistent pre-checkpoint core is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S)}.
\]

Source residue `r` may not be dropped while source-sensitive obligations remain.

Status: **EXACT / CLOSED state minimization for active pre-checkpoint predicates**.

## S4 — Exact source-preserving transition

For a next-one valuation branch `a`,

\[
m\equiv(2^a-y)3^{-q}\pmod{2^{a+1}},
\]

and the exact affine source/current-state channel is preserved under the induced residue refinement.

Exact residual inversion remains

\[
R=2^nZ-3^qY,
\qquad a=v_2(R).
\]

Finite macroblocks compile the same tree without merging source payloads.

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

Let `D_r` count displaced future one-ranks among the first `r` future one-events, and let `H_c` be the longest exact source-preserving pure-ballot horizon reachable with `D_r<=c`.

Certified exact equalities through budget four are

\[
\boxed{H_0=40,\ H_1=44,\ H_2=45,\ H_3=48,\ H_4=50.}
\]

For budget five, the 64-shard exact horizon-51 decision gives

\[
\boxed{\#\{D_{51}\le5\text{ paths}\}=0},
\]

hence

\[
\boxed{H_5\le50},
\qquad
\boxed{D_{51}\ge6}.
\]

`H_5=50` is not inferred.

Status: **EXACT / CLOSED horizon-51 non-reachability; exact H5 equality OPEN**.

## S7 — Cumulative future-defect floor

Each displaced rank contributes normalized future defect

\[
\epsilon_r>\frac1{12}.
\]

Therefore

\[
\boxed{\eta_{future}>\frac12}.
\]

For monotone endpoint rejection use the SAFE weakening

\[
\eta_{future}\ge\frac12.
\]

Older `1/4`, `1/3`, and `5/12` floors are superseded, not added.

Status: **SAFE consequence of exact finite reachability**.

## S8 — Current canonical population

Applying the `>=1/2` endpoint floor gives

\[
\boxed{26{,}859{,}837{,}368{,}455{,}538{,}464}
\]

source integers.

The incremental `5/12 -> 1/2` rejection is

\[
\boxed{25{,}304{,}566}.
\]

All `14,224` source intervals remain nonempty.

Canonical export:

- `src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

Validation run: `33864085911`.

Status: **EXACT endpoint arithmetic / zero whole-cylinder closures**.

## S9 — Directed physical predicate split

The directed `P_min` predicate remains valid, but roughly `82.095%` of the first-75-tightened population can never be rejected by `P_min`, even under the maximal remaining target-correction budget.

Therefore bounded-displacement defect work is a secondary upper-tail mechanism, not a complete membership engine.

Status: **EXACT predicate localization; insufficient for closure**.

## S10 — Late observation activation is event-local, not time-local

Terminal ternary observation activates at

\[
q_{rem}=28,
\qquad q=j_0-28=65{,}868{,}186{,}673.
\]

The threshold one-position formula is

\[
\boxed{t_{r-1}=\lfloor(r-1)\log_2 3\rfloor}.
\]

Thus the threshold `q`-th one is at

\[
104{,}398{,}605{,}865.
\]

For the canonical activation seam immediately after the candidate `q`-th one,

\[
\boxed{44\le t_0-h_{act}\le38{,}530{,}419{,}237}.
\]

So the final observation is local in the last 28 one-events, not in a universally short raw bit-time shell.  The terminal exporter must use event/valuation-gap state.

Dependencies:

- `theorems/TERMINAL_28_EVENT_LOCALITY_NOT_TIME_LOCALITY.md`;
- `src/A0_s1_terminal_28_event_locality_not_time_locality_certificate.py`.

Status: **EXACT / CLOSED distinction**.

## S11 — Checkpoint observation arithmetic

The final 28 one-events determine the terminal ternary observation, the post-checkpoint 27-bit prefix determines

\[
Z\bmod2^{27},
\]

and the synchronized CRT seam exposes at most one ordinary `Z` in the certified corridor.

Terminal/right-H transfer is affine and bijective modulo `3^28`.

For the current 28-gate target-dominance terminal predicate,

\[
\boxed{\text{completion exists}\iff3\nmid Z}.
\]

Status: **EXACT / CLOSED observation and target-dominance interface**.

## S12 — Source/checkpoint same-orbit join kernel

At the late activation seam,

\[
X=r+2^hk,
\qquad
T^h(X)=y+3^qk,
\qquad q=j_0-28.
\]

For a validated 28-one terminal suffix with length `n` and correction `C_B`, define

\[
Y_B(Z)=\frac{2^nZ-C_B}{3^{28}}.
\]

The source provenance criterion is

\[
Y_B(Z)-y\equiv0\pmod{3^q},
\]

and

\[
k_*=(Y_B(Z)-y)/3^q\in[k_{lo},k_{hi}].
\]

When it passes,

\[
\boxed{T^{h+n}(r+2^hk_*)=Z}.
\]

For a fixed activation channel, terminal descriptor and `Z`, the source parameter is unique.

Dependencies:

- `theorems/SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md`;
- `src/A0_s1_source_activation_checkpoint_provenance_join_certificate.py`;
- `audits/S10_SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN_AUDIT.md`.

Regression run `33864578621` passed.

Status: **EXACT / CLOSED join kernel**.

## S13 — State minimization after provenanced checkpoint exposure

Once an ordinary checkpoint `Z` is exposed **with provenance**,

\[
\boxed{z_2=Z\bmod2^{27}}
\]

and

\[
\boxed{z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}}}
\]

are derived rather than persistent coordinates.  The actual post-checkpoint prefix is deterministic from `Z`.

Before exposure, the directed observations may not be Cartesian-paired.

Dependencies:

- `theorems/EXPOSED_CHECKPOINT_OBSERVATION_STATE_MINIMIZATION.md`;
- `src/A0_s1_exposed_checkpoint_observation_state_minimization_certificate.py`.

Combined validation run `33865446235` passed.

Status: **EXACT / CLOSED after provenanced Z exposure**.

## S14 — Per-checkpoint source localization

For one already-exposed ordinary checkpoint `Z`, the SAFE debit corridor restricts one current cylinder's source parameter to an interval of width

\[
\frac{37\cdot2^{33}}{3\cdot2^h}.
\]

On the current `>=1/2` frontier the total per-`Z` source-parameter cap is

\[
\boxed{3{,}256{,}612{,}398},
\]

at least an `8,247,784,533`-fold reduction relative to the current population.

`6,190` of `14,224` cylinders have cap `<=1`, and `9,537` have cap `<=1000`.

This is localization only; it is not same-orbit membership.

Dependency:

- `src/A0_s1_8jump_checkpoint_source_fiber_profile_certificate.py`.

Status: **EXACT deterministic per-Z cap / membership implication REJECTED**.

## S15 — Paired late-activation / ordinary-Z exporter

All local arithmetic needed after a correctly paired activation record is now closed.  The principal unresolved task is

\[
\boxed{\text{source-preserving paired late-activation / ordinary-}Z\text{ exporter}}.
\]

The exporter must:

1. carry current source provenance to `q=j0-28` without expanding the raw middle word;
2. encode the final 28 one-events as valuation/event gaps rather than raw bit-time;
3. resolve the low-precision right-H carry family (`m<=17`), after which the existing backward exponential carry chart is injective at higher precision;
4. expose ordinary checkpoint candidates `Z` with provenance;
5. apply the CLOSED S12 source/checkpoint membership kernel.

Status: **OPEN principal membership gate**.

## S16 — A0 `s=1` Route-B closure

Required conclusion: every family from all 14 roots is exactly rejected or discharged through the full pre-checkpoint/checkpoint/tail obligations.

Status: **OPEN**.

## S17 — Global completion

Route-A, all `s>=2` sectors, remaining branches, and global branch completeness must be independently closed before any Collatz conclusion.

Status: **OPEN**.

---

# Immediate next work

1. Build a source-preserving event/valuation exporter to `q_rem=28`.
2. Treat the final 28 one-events as integer valuation gaps; do not assume a short raw suffix.
3. Close/export the low-precision `m<=17` right-H carry family with source provenance; use existing high-precision injectivity afterward.
4. Prefer exposing a provenanced ordinary `Z` over maintaining independent post-exposure `(z_2,z_H)` state.
5. Run the CLOSED activation/checkpoint join kernel on each exported candidate.
6. Use debit source fibers only for candidate localization.
7. Keep further bounded-displacement budgets secondary unless structurally useful.

# Forbidden shortcuts

- extrapolating finite `H_c` data;
- `H_5<=50 -> H_5=50` without a witness;
- adding nested future-defect floors;
- exact-pair uniqueness -> family uniqueness;
- equal control/template state -> equal source payload;
- dropping source residue `r` early;
- correction/formation/displacement re-expression -> independent pruning;
- CRT compatibility -> same orbit;
- debit-corridor localization -> source realization;
- Cartesian pairing of independent boundary marginals;
- `q_rem=28 -> universal short raw bit shell`;
- dropping `z_2,z_H` before a unique provenanced `Z` is exposed;
- finite Route-B progress -> global Collatz.
