# Current status — 2026-09-01

## Current branch

Research branch: `collatz-stage4-window-threshold`

Primary active object: `A0, s=1, Route-B` long-membership closure.

## Last fully reduced search family

Every current Route-B survivor belongs to the exact 14-root arithmetic forest

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Canonical certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

This is a search-family representation after SAFE upstream pruning, not a proof that any root realizes full membership.

## Exact structural state now available

The current live toolbox includes:

- exact source affine cylinders and bit refinement;
- finite interval payload compression;
- fixed-count ballot / target-dominance states;
- exact H/L grammar and target-only hierarchy alignment;
- correction front localization and critical-cut ternary shielding;
- ternary carry, displacement cylinders, and backward exponential carry chart;
- one-dimensional ternary projective interval payload `Pi3_k`;
- normalized defect semiring and ordering-aware fixed-cylinder minimum;
- integer defect numerator `N=3^q eta`;
- scalar physical danger score `P` with one `P_min` label per exact active key;
- lazy terminal ternary observation;
- synchronized checkpoint CRT singleton exposure.

## Physical Bellman front

For the directed physical gate

\[
P=m_{lo}N+\delta_{lo}3^qX_{lo}.
\]

Whole-family rejection occurs when

\[
P>(L_{max}QFP+c_{W,hi})3^q.
\]

Under one exact source/control + payload transition the score map is increasing, so one `P_min` label is exact for this predicate.

## Right-H localization and projective sharpening

At the critical cut the right H block has

\[
h_R=630{,}138{,}897,\qquad q_R=397{,}573{,}380.
\]

Hence the current 24-, 28-, and 47-trit terminal predicates are fully right-local.

For right-indexed target capacity,

\[
D_t\le h_R-q_R=232{,}565{,}517.
\]

Since

\[
\lambda_m=2\cdot3^{m-1},\qquad
\lambda_{18}=258{,}280{,}326>232{,}565{,}517,
\]

every **prescribed** right-H projective slack/exponent cylinder is empty or singleton for `m>=18`.

This gives high-precision prescribed-cylinder ranges of 7, 11, and 30 one-gates for `L=24,28,47` respectively. It does not imply a unique carry path.

## Newly closed synchronized checkpoint interface

Use only the independent pre-defect corridor inputs

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33},
\]

\[
75\,2^{33}<L_-<112\,2^{33},\qquad L_-=3X-Z.
\]

They imply the SAFE integer checkpoint corridor

\[
Z_{min}=7{,}083{,}549{,}723{,}342{,}395{,}146{,}241,
\]

\[
Z_{max}=9{,}444{,}732{,}965{,}107{,}363{,}299{,}196.
\]

For the right H factor,

\[
z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}},
\]

with

\[
2^s\equiv12{,}596{,}342{,}295{,}887,
\]

\[
C(H_s^*)\equiv2{,}677{,}095{,}985{,}033
\pmod{3^{28}}.
\]

Together with `Z mod 2^27`, ordinary coprime CRT gives one class modulo

\[
M=2^{27}3^{28}=3{,}070{,}471{,}107{,}232{,}407{,}748{,}608.
\]

The certified corridor span is

\[
2{,}361{,}183{,}241{,}764{,}968{,}152{,}955<M,
\]

so each synchronized dyadic/right-H observation pair admits at most one ordinary checkpoint `Z` in the corridor.

Canonical theorem/certificate:

- `../theorems/SYNCHRONIZED_CHECKPOINT_CRT_SINGLETON.md`;
- `../src/A0_s1_routeB_synchronized_checkpoint_CRT_singleton_certificate.py`.

No marginal-density multiplication or independence assumption is used, and no later defect-derived X bound is used retroactively.

## Current stopping point

The checkpoint exposure seam is closed. The live architecture is now:

### Forward front

`14-root source/control × interval payload × P_min`.

### Backward right front

right-H projective/carry state synchronized to the actual checkpoint observation.

### Next join

Apply the synchronized observation to the real 14-root export families and join it with the forward `P_min` state at the exact boundary.

The immediate unresolved questions are which root/state families admit a synchronized checkpoint at all, which close by the physical Bellman gate before/at the join, and which require the next membership/tail predicate.

## What remains OPEN

- actual 14-root forward `P_min` execution/export;
- compressed multi-gate right-H carry-family export where still needed;
- exact 14-root forward/backward synchronized join;
- remaining pre-bridge correction-language membership;
- remaining ordinary debit/tail/renewal compatibility after checkpoint exposure;
- Route-A;
- all `s>=2` sectors;
- global branch completeness;
- the Collatz conjecture.

## Forbidden shortcuts retained

- adic mismatch -> membership rejection;
- marginal dyadic/ternary density multiplication;
- singleton prescribed cylinder -> singleton carry path;
- local carry greedy -> global path optimum;
- later refined bound used retroactively;
- checkpoint singleton exposure -> automatic same-orbit/full membership.

## Resume instruction

Resume from `../frontier/A0_S1_ROUTEB.md`.

The next calculation is the **14-root synchronized join**, using the forward `P_min` export and the right-H/checkpoint observation without introducing an independence assumption.
