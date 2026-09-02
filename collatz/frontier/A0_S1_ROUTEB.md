# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation.

## Input family

Exact retained roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary input certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

Each root is an exact source cylinder

\[
X=r+2^h m
\]

with a finite integer parameter interval and exact bit refinement.

## Closed synchronized seams

The following no longer need to be rediscovered:

1. synchronized `2^27 × 3^28` observations expose at most one ordinary checkpoint `Z` in the SAFE corridor;
2. one exposed `Z` contracts every root to an exact debit-compatible source fiber;
3. the checkpoint terminal ternary precision is fully consumed inside the right H block, so no checkpoint carry residue crosses the critical cut;
4. modulo `3^L`, only the final `L` ranked one-events affect the target-relative correction residue;
5. under equal-count target dominance, every locally legal final-rank suffix extends to a full dominant candidate by the packed prefix `b_r=r-1`.

Canonical new objects:

- `../theorems/CRITICAL_CUT_TERMINAL_PRECISION_ABSORPTION.md`;
- `../theorems/TERMINAL_RANK_WINDOW_DOMINANCE_COMPLETION.md`.

## Current right-H checkpoint reduction

For the current right H target

\[
q_H=397{,}573{,}380
\]

and synchronized ternary precision

\[
L=28,
\]

pure target-dominance acceptance of a prescribed `z_H mod 3^28` is exactly a finite **28-gate ordered-slack/projective problem**.

The earlier

\[
397{,}573{,}352
\]

one-events are invisible to this terminal residue and need not be enumerated for dominance existence.

The exact target position formula is

\[
a_r=\left\lceil\frac{(r-1)J_0}{R_0}\right\rceil-1
\]

for `r>=2`.

For the final 28 ranked ones, right-indexed capacities satisfy approximately

\[
232{,}565{,}502\le D_t\le232{,}565{,}517.
\]

At precision

\[
m=28,27,\ldots,18,
\]

the projective cylinder period `2*3^(m-1)` exceeds the relevant capacity, so each prescribed cylinder is empty or singleton for the first 11 gates.

This still does not imply a unique complete 28-gate path.

## Active G2 computation — actual 28-gate acceptance DP

Use the already certified max-slack quotient.

For a prescribed initial terminal carry/observation `z_0 mod 3^28`, at right-index `t` carry

`z_t -> S_max(z_t)`

where only the largest reachable ordering slack is retained for suffix-existence.

At gate `t`:

- `m=28-t`;
- target exponent `A_t=a_(q_H-t)`;
- base `q_H-t-1`;
- capacity `D_t=A_t-base`;
- legal slack interval `0 <= s_t <= min(D_t,S_previous)`;
- successor carry is

\[
z_{t+1}=
\frac{z_t+2^{A_t}-2^{B_t}}{3}
\pmod{3^{m-1}},
\qquad B_t=base+s_t.
\]

Histories reaching the same successor carry merge by maximum slack exactly for dominance existence.

After gate 28, ternary precision is zero. A nonempty quotient state means the prescribed terminal observation has a target-dominant completion; the packed-prefix theorem supplies the omitted earlier one-events.

## Boundary-control caveat

The 28-gate theorem closes target-dominance residue existence only.

If the full H/L grammar join requires a boundary/control label beyond dominance, attach that finite control to the quotient key:

`(projective carry, boundary/control) -> S_max`.

Do not expand the omitted 397,573,352 one-events merely to recover a control coordinate; derive the minimal boundary-control transition separately from the H/L grammar.

## Checkpoint-conditioned source join

For every right-H accepted synchronized observation:

1. combine `z_H` with the exact compatible dyadic checkpoint observation;
2. use the closed CRT seam to expose zero or one ordinary `Z`;
3. intersect each root with the exact source fiber

\[
\frac{Z+75\,2^{33}-3r}{3\,2^h}<m<
\frac{Z+112\,2^{33}-3r}{3\,2^h};
\]

4. enumerate deep fibers when small;
5. use `P_min` refinement on shallow large fibers;
6. preserve the full pre-bridge membership obligation.

Per exposed `Z` the cumulative deep caps remain:

- `f>=24`: 3,668;
- `f>=27`: 510;
- `f>=29`: 115;
- `f>=32`: 16;
- `f>=35`: 3;
- `f=37`: 1.

## Immediate executable milestone

Build a certificate implementing the exact 28-gate quotient on the **actual last-28 target capacities**, with one of two outcomes:

1. a compact symbolic/finite representation of the accepted `z_H mod 3^28` set and exact state counts by gate; or
2. a certified state-growth obstruction showing which additional quotient coordinate is still needed.

Then intersect any accepted synchronized observations immediately with the checkpoint/source seams above.

## DSD audit rules

Allowed:

- max-slack merge at identical carry + identical boundary/control for suffix existence;
- forgetting checkpoint ternary residue after its precision is consumed;
- packed-prefix completion for target dominance;
- exact finite 28-gate execution reported as execution evidence.

Forbidden:

- zero residual precision -> unique right-H history;
- packed-prefix dominance completion -> full H/L grammar membership without checking extra control;
- singleton prescribed cylinder -> singleton complete path;
- marginal density multiplication;
- small source fiber -> membership;
- one `(X,Z)` pair -> same orbit/full pre-bridge membership;
- finite state counts -> universal theorem.

## Global warning

Even complete closure of all current 14 Route-B roots would not prove Collatz. Route-A, `s>=2`, remaining formation sectors, and global branch completeness remain separate obligations.
