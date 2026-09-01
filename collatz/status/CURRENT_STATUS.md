# Current status — 2026-09-01

## Current branch

Research branch: `collatz-stage4-window-threshold`

Primary active object: `A0, s=1, Route-B` long-membership closure.

## Last fully reduced search family

Every current Route-B survivor belongs to the exact 14-root arithmetic forest with first threshold disagreement

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Canonical certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

This forest is a search-family representation after SAFE upstream pruning. It is not a proof that any root realizes full membership.

## Current structural state

The following components are available as exact/local tools:

- source affine cylinder and exact bit refinement;
- finite interval payload compression;
- fixed-count ballot and target-dominance representation;
- exact dual H/L grammar;
- target-specific H/L–Stern-Brocot scale alignment;
- fixed-resolution correction/projective states;
- ternary suffix carry and displacement cylinders;
- normalized defect semiring;
- projective-cylinder exact defect floors;
- inverse physical defect budget;
- integer defect numerator `N=3^q eta`;
- exact scalar physical danger score `P` with one `P_min` Bellman label per exact active source/payload key;
- minimal lazy ternary observation `R_q=N_q mod 3^m(q)` for final `3^L` residue predicates;
- critical-cut ternary shielding;
- uniform projective-cylinder multiplicity bound with singleton threshold `m>=23`.

## Current physical Bellman reduction

For the directed real-envelope gate define

\[
P=m_{lo}N+\delta_{lo}3^qX_{lo}.
\]

The whole family closes under this gate when

\[
P>B3^q.
\]

Under a common exact source/control and interval-payload transition, `P` evolves by an increasing affine map `P -> P+c` or `P -> 3P+c`.

Therefore only the minimum `P` label is needed for this predicate.

The earlier `(source residue, defect)` Pareto frontier remains the general representation only when a later predicate queries those coordinates separately.

## Newly closed terminal-ternary interface

For a final defect/correction residue predicate

\[
N_J\pmod{3^L},
\]

the current exact observation precision is

\[
m(q)=\max(0,L-(J-q)).
\]

Thus the current residue coordinate

\[
R_q=N_q\bmod3^{m(q)}
\]

is completely dormant while at least `L` future one-events remain.

For the current

\[
J=j_0=65,868,186,701,
\]

a 28-trit terminal residue does not require any prefix ternary state through

\[
q\le65,868,186,673.
\]

Once active, the augmented exact key

`source/control × interval payload × R_q`

still carries only one `P_min` label.

## Critical-cut localization

At the existing exact critical cut, the right H-side factor has

\[
q_B=397,573,380
\]

one-events.

Hence every terminal residue predicate modulo `3^L` with

\[
L\le397,573,380
\]

is completely shielded from the left block.

In particular the current 24-, 28-, and 47-trit terminal resolutions are right-local.

Therefore the terminal ternary predicate should not be carried through the full left/forward 14-root scan.

## Projective-cylinder width

For every ranked one-position, the legal dominance interval has width at most

\[
t_0-j_0=38,530,419,209.
\]

At ternary precision `m`, a projective exponent cylinder has period

\[
\lambda_m=2\cdot3^{m-1}.
\]

Since

\[
\lambda_{23}=62,762,119,218>38,530,419,209,
\]

every specified projective exponent cylinder is empty or singleton for `m>=23`.

For a 28-trit backward filter, the first six one-gates (`m=28..23`) therefore have no within-cylinder exponent multiplicity.

This does not imply a unique carry/suffix branch.

## Current stopping point

The architecture is now a two-front exact join.

### Forward front

Carry

`source/control × interval payload × P_min`

on the 14-root forest, without terminal ternary state while it is unobservable.

### Backward right front

Start from the actual required terminal correction/defect residue and propagate it backward through the compressed right H/projective factor as an empty-or-singleton predecessor residue cylinder for each specified branch.

### Join

At an exact block boundary, join the backward admissible projective/control state to the forward source/physical Bellman families.

No independence assumption or marginal-ratio multiplication is allowed.

## Current mathematical bottleneck

The next unresolved object is

`compressed right-H backward projective residue filter -> exact cut-boundary export state`.

After that:

`forward 14-root Bellman state JOIN backward H/projective filter -> whole-family closure or next predicate activation`.

## What is already ruled out

Do not restart these rejected proof shortcuts:

- target adic mismatch as automatic membership rejection;
- interval inclusion as correction-language membership;
- endpoint exposure as same-orbit connectivity;
- product of marginal densities without independence;
- local carry greedy as a global defect minimizer before the cylinder sequence is fixed;
- terminal ternary saturation as an automatic contradiction with an early defect invisible at that ternary resolution;
- carrying a full terminal ternary residue coordinate from every root before the residue is observable.

## What has not been proved

- no global 14-root closure yet;
- no complete right-H backward residue filter yet;
- no exact forward/backward cut join yet;
- no complete Route-B membership/nonmembership theorem yet;
- no Route-A completion yet;
- no all-surplus `s>=2` completion yet;
- no global Collatz proof.

## Resume instruction

When computation resumes, start from `../frontier/A0_S1_ROUTEB.md` and the two new theorem objects:

- `../theorems/LAZY_TERNARY_OBSERVATION.md`;
- `../theorems/CRITICAL_CUT_TERNARY_SHIELDING.md`;
- `../theorems/TERMINAL_PROJECTIVE_CYLINDER_WIDTH.md`.
