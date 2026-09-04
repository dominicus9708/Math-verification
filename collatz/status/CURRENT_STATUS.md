# Current status — 2026-09-04

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

The exact `c=5`, horizon-51, 64-shard decision gives

\[
\boxed{\#\{D_{51}\le5\text{ paths}\}=0}.
\]

Therefore

\[
\boxed{H_5\le50},
\qquad
\boxed{D_{51}\ge6},
\qquad
\boxed{\eta_{future}>\frac12}.
\]

Using the safe endpoint weakening `>=1/2`, the current canonical population is

\[
\boxed{26{,}859{,}837{,}368{,}455{,}538{,}464}.
\]

The source-cylinder count remains `14,224`; no whole interval is closed by this chain.

Downstream source export:

- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

The `>=1/2` frontier validation workflow passed in GitHub Actions run `33864085911`.

## Exact bounded-displacement status

\[
\boxed{H_0=40,\ H_1=44,\ H_2=45,\ H_3=48,\ H_4=50.}
\]

For budget five only

\[
\boxed{H_5\le50}
\]

is claimed. `H_5=50` remains unproved without a horizon-50 witness.

Reachability evidence:

- GitHub Actions run `33756884264`;
- `../src/A0_s1_8jump_c5_h51_shard_probe.py`.

The latest `1/2` floor supersedes the older `1/4`, `1/3`, and `5/12` floors; the floors are not added.

## P_min role split

The directed `P_min` mechanism remains valid but cannot close the lower approximately `82.095%` of the first-75-tightened source population even under the maximal remaining target-correction budget.  Higher bounded-displacement budgets are therefore secondary rather than the principal closure route.

## Source/checkpoint same-orbit kernel — CLOSED

At the late activation seam let

\[
X=r+2^h k,
\qquad
T^h(X)=y+3^q k,
\qquad q=j_0-28,
\qquad k\in[k_{lo},k_{hi}].
\]

For a validated exact terminal suffix descriptor

\[
|B|=n,
\qquad q(B)=28,
\qquad C_B=C(B),
\]

and one ordinary checkpoint candidate `Z`, define

\[
Y_B(Z)=\frac{2^nZ-C_B}{3^{28}}.
\]

The source/checkpoint provenance test is exactly

\[
Y_B(Z)-y\equiv0\pmod{3^q},
\]

and

\[
k_*:=\frac{Y_B(Z)-y}{3^q}\in[k_{lo},k_{hi}].
\]

When it passes,

\[
X_*=r+2^hk_*
\]

satisfies

\[
\boxed{T^{h+n}(X_*)=Z}.
\]

Thus the local same-orbit arithmetic is no longer the principal OPEN item.

Canonical files:

- `../theorems/SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md`;
- `../src/A0_s1_source_activation_checkpoint_provenance_join_certificate.py`;
- `../audits/S10_SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN_AUDIT.md`.

Regression workflow run `33864578621` passed.

## Exposed checkpoint state minimization — CLOSED

Once an ordinary checkpoint `Z` is exposed **with provenance**,

\[
\boxed{z_2=Z\bmod2^{27}}
\]

and

\[
\boxed{z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}}}
\]

are derived coordinates, not independent persistent state.

For the current 28-gate terminal target-dominance predicate,

\[
\boxed{\text{completion exists}\iff3\nmid Z}.
\]

Before provenanced `Z` exposure, `z_2` and `z_H` remain directed observations and may not be Cartesian-paired.

Canonical files:

- `../theorems/EXPOSED_CHECKPOINT_OBSERVATION_STATE_MINIMIZATION.md`;
- `../src/A0_s1_exposed_checkpoint_observation_state_minimization_certificate.py`.

The combined source-checkpoint workflow including this certificate passed in run `33865446235`.

## Terminal locality correction — CLOSED

The condition

\[
q_{rem}=28
\]

means 28 future **one-events**.  It does not imply a universal short ordinary-bit shell.

The threshold one-position formula is

\[
\boxed{t_{r-1}=\lfloor(r-1)\log_2 3\rfloor}.
\]

At

\[
q=j_0-28=65{,}868{,}186{,}673,
\]

the exact threshold `q`-th one position is

\[
104{,}398{,}605{,}865.
\]

For the canonical activation seam immediately after the candidate `q`-th one,

\[
\boxed{44\le t_0-h_{act}\le38{,}530{,}419{,}237}.
\]

Hence the final 28 one-events should be compressed as valuation/event gaps, not by assuming a ~43-bit raw suffix.

Canonical files:

- `../theorems/TERMINAL_28_EVENT_LOCALITY_NOT_TIME_LOCALITY.md`;
- `../src/A0_s1_terminal_28_event_locality_not_time_locality_certificate.py`.

## Per-checkpoint source-fiber profile

For one already-exposed ordinary checkpoint `Z`, the independent SAFE debit corridor gives a per-cylinder source-parameter width

\[
\frac{37\cdot2^{33}}{3\cdot2^h}.
\]

On the current `>=1/2` jump-8 frontier, the total deterministic source-parameter cap for one `Z` is

\[
\boxed{3{,}256{,}612{,}398}.
\]

This is a reduction of at least

\[
\boxed{8{,}247{,}784{,}533}
\]

relative to the current population, once `Z` is exposed.

Further:

- `6,190` of `14,224` cylinders have per-`Z` cap `<=1`;
- `9,537` have cap `<=1000`.

This is localization only, not same-orbit membership.

Certificate:

- `../src/A0_s1_8jump_checkpoint_source_fiber_profile_certificate.py`.

## Principal bottleneck

The principal OPEN object is now more precise:

\[
\boxed{\text{source-preserving paired late-activation / ordinary-}Z\text{ exporter}}.
\]

What is already CLOSED:

1. terminal `Z mod 3^28` locality;
2. right-H affine transfer;
3. post-checkpoint `Z mod 2^27` locality;
4. CRT corridor uniqueness;
5. local exact source/checkpoint same-orbit join once a paired activation record is supplied;
6. state minimization after provenanced `Z` exposure.

What remains OPEN is construction of the actual paired late-activation relation from the current source families without expanding the raw ~`10^11`-bit middle word.

The terminal exporter must be event/valuation based.  The existing backward exponential carry chart is injective at precision `m>=18`; the important unresolved terminal export range is the low-precision `m<=17` carry family, together with source provenance.

## Immediate next work

1. Construct a source-preserving event/valuation exporter to the `q_rem=28` activation seam.
2. Keep source provenance while compressing the final 28 valuation gaps; do not enumerate raw bit-time.
3. Resolve/export the low-precision `m<=17` right-H carry family; high-precision layers are already one-step injective.
4. Expose ordinary checkpoint candidates `Z` with provenance rather than carrying independent post-exposure `(z_2,z_H)` labels.
5. Apply the CLOSED activation/checkpoint provenance kernel to each candidate.
6. Use the per-`Z` debit fiber only as a candidate cap, never as an orbit proof.
7. Keep higher bounded-displacement budgets secondary unless they supply a structural gain.

## Still OPEN

- exact `H_5` equality;
- compressed source-preserving paired late-activation / ordinary-`Z` exporter;
- low-precision terminal carry-family export with source provenance;
- exact 14-root source/checkpoint realization;
- remaining checkpoint/tail membership predicates beyond terminal target-dominance existence;
- `A0,s=1,Route-B` closure;
- Route-A;
- all `s>=2` sectors;
- global branch completeness;
- Collatz.

## Forbidden shortcuts

- extrapolating finite `H_c` values;
- `H_5<=50 -> H_5=50` without a witness;
- adding nested defect floors;
- equal control state -> equal source payload;
- CRT compatibility -> same orbit;
- debit-corridor localization -> same orbit;
- Cartesian pairing of independent `z_2`/`z_H` marginals;
- `q_rem=28 -> universal short raw bit shell`;
- exposed `Z` observations -> source realization without the activation-fiber test;
- finite Route-B progress -> global Collatz.
