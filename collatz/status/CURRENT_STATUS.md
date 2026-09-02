# Current status — 2026-09-02

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

The live toolbox includes:

- exact source affine cylinders and bit refinement;
- finite interval payload compression;
- fixed-count ballot / target-dominance states;
- exact H/L grammar and target-only hierarchy alignment;
- correction front localization and critical-cut ternary shielding;
- ternary carry, displacement cylinders, and backward projective charts;
- one-dimensional ternary projective interval payload `Pi3_k`;
- backward max-slack feasibility quotient at fixed carry;
- normalized defect semiring and ordering-aware fixed-cylinder minimum;
- integer defect numerator `N=3^q eta`;
- scalar physical danger score `P` with one `P_min` label per exact active key;
- lazy terminal ternary observation;
- synchronized checkpoint CRT singleton exposure;
- synchronized checkpoint -> source-fiber cardinality bound;
- **critical-cut terminal precision absorption**.

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

A finite exact forward scan remains an execution tool, but it is no longer necessary to force every root to ordinary-X singleton depth before checkpoint information is used.

## Right-H localization and precision absorption

At the critical cut the right H block has

\[
h_R=630{,}138{,}897,\qquad q_R=397{,}573{,}380.
\]

The current 24-, 28-, and 47-trit terminal predicates are fully right-local.

For a terminal precision `L`, the projective block-carry theorem exports only

\[
L_{cut}=\max(0,L-q_R)
\]

ternary digits across this cut.

Therefore

\[
L_{cut}=0
\]

for `L=24,28,47`.

This is stronger than right-locality alone: after a prescribed terminal observation is accepted/rejected inside the right H block, **no checkpoint ternary carry residue remains in the cut join key**. Zero residual precision does not imply a unique right-H history; boundary/grammar controls and independent physical data remain distinct.

Canonical theorem/certificate:

- `../theorems/CRITICAL_CUT_TERMINAL_PRECISION_ABSORPTION.md`;
- `../src/A0_s1_routeB_critical_cut_terminal_precision_absorption_certificate.py`.

The generic arithmetic guard was independently checked locally on 2026-09-02: `L=24,28,47` all export precision `0`, with 4,225 small implementation checks. GitHub Actions execution is not claimed unless separately recorded.

## Closed synchronized checkpoint interface

Independent pre-defect inputs imply the SAFE integer checkpoint corridor

\[
Z_{min}=7{,}083{,}549{,}723{,}342{,}395{,}146{,}241,
\]

\[
Z_{max}=9{,}444{,}732{,}965{,}107{,}363{,}299{,}196.
\]

For the right H factor,

\[
z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}}.
\]

Together with `Z mod 2^27`, coprime CRT gives one class modulo

\[
M=2^{27}3^{28}=3{,}070{,}471{,}107{,}232{,}407{,}748{,}608.
\]

The certified `Z` corridor span is smaller than `M`, so every coherent synchronized observation pair admits at most one ordinary checkpoint `Z`.

## Closed checkpoint-conditioned source fiber

For one retained source root

\[
X=r+2^h m
\]

and one exposed checkpoint `Z`, the independent debit corridor

\[
75\,2^{33}<3X-Z<112\,2^{33}
\]

forces a source fiber of cardinality at most

\[
K_h=\left\lceil\frac{37\,2^{33}}{3\,2^h}\right\rceil.
\]

Current exact caps per root:

`f=2: 13,242,815,830`; `f=5: 1,655,351,979`; `f=8: 206,918,998`; `f=10: 51,729,750`; `f=13: 6,466,219`; `f=16: 808,278`; `f=18: 202,070`; `f=21: 25,259`; `f=24: 3,158`; `f=27: 395`; `f=29: 99`; `f=32: 13`; `f=35: 2`; `f=37: 1`.

Deep-root cumulative caps per exposed `Z`:

- `f>=24`: 3,668;
- `f>=27`: 510;
- `f>=29`: 115;
- `f>=32`: 16;
- `f>=35`: 3;
- `f>=37`: 1.

## Current live architecture — reduced hybrid synchronized join

### G2 right-H side

For a prescribed `z_H mod 3^28`, determine exact right-H acceptance and export only the surviving boundary/grammar control coordinates. The consumed checkpoint ternary residue is not exported across the cut.

The remaining structural problem is therefore the compact representation of the **accepted set of prescribed terminal observations**, not a residual carry state at the cut.

### Checkpoint/source join

For every accepted synchronized observation:

1. combine `z_H` with the compatible dyadic observation;
2. reconstruct zero or one corridor checkpoint `Z`;
3. intersect each relevant source root immediately with its exact debit-compatible `m` fiber;
4. enumerate deep fibers only when genuinely small;
5. use compressed `P_min` source refinement for shallow unresolved fibers;
6. preserve exact pre-bridge membership obligations.

## What remains OPEN

- compact right-H acceptance representation over prescribed `z_H mod 3^28`;
- actual accepted synchronized observations;
- hybrid synchronized join on the 14 roots;
- shallow-root compressed source refinement where checkpoint fibers remain large;
- exact pre-bridge correction-language membership for joined survivors;
- ordinary debit/tail/renewal compatibility after exposure;
- Route-A;
- all `s>=2` sectors;
- global branch completeness;
- the Collatz conjecture.

## Forbidden shortcuts retained

- adic mismatch -> membership rejection;
- marginal dyadic/ternary density multiplication;
- zero residual cut precision -> unique right-H history;
- singleton prescribed cylinder -> singleton carry path;
- small checkpoint-conditioned source fiber -> membership;
- one exposed `(X,Z)` pair -> automatic same orbit/full membership;
- local carry greedy -> global path optimum;
- later refined bound used retroactively;
- finite execution counts -> universal theorem.

## Resume instruction

Resume from `../frontier/A0_S1_ROUTEB.md`.

The next principal calculation is the **compact right-H acceptance set for prescribed synchronized `z_H` observations**. Once those observations are available, feed them immediately through the closed CRT and source-fiber seams; do not rebuild a cut-level ternary carry coordinate that has already been absorbed.
