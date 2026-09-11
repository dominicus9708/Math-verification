# MATH-075 — exact slack Bellman potential and localization of negative unit edges

Date: 2026-09-12

Status: `EXACT UNIT-EDGE POTENTIAL / POSITIVE-SLACK REGION BELLMAN-SAFE / FIRST-CELL OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-075 does not close the remaining first-cell boundary language.
- Its role is to remove every positive-slack unit transition from the negative Bellman core.

## 1. Setup

Use the MATH-060 slope

\[
\lambda=\frac{19}{503}.
\]

For the coefficient-boundary slack

\[
u=m(q)-d\ge0
\]

inside the first coefficient cell, MATH-053 gives

\[
E:u\mapsto u-1,
\qquad
O:u\mapsto u+\varepsilon_{q+1},
\]

where `epsilon` is `0` or `1`.

For an odd step taken at slack `u`, the penalty atom is

\[
\boxed{
p(q,u)=\frac{(1-2^{-u})\Omega_q}{3}.
}
\]

Define

\[
\boxed{H_u=-\lambda u.}
\]

For one unit shortcut edge, the reduced cost is

\[
g=p-\lambda+H_u'-H_u.
\]

## 2. Even edges are exactly neutral

Every coefficient-valid internal even edge has `u>=1` and

\[
u'=u-1.
\]

There is no odd-step penalty on this edge, so

\[
g=-\lambda+\lambda=\boxed0.
\]

Thus every internal even step is paid exactly by one unit of decreasing slack potential.

## 3. Every positive-slack odd edge is strictly safe

For an odd edge with `u>=1`,

\[
1-2^{-u}\ge\frac12.
\]

### epsilon = 0

The exact phase rule gives

\[
\Omega_q>\frac34.
\]

Therefore

\[
p>\frac18.
\]

Since `u'=u`,

\[
g=p-\lambda
>\frac18-\frac{19}{503}
=\boxed{\frac{351}{4024}}>0.
\]

### epsilon = 1

The exact phase rule gives

\[
\frac12<\Omega_q<\frac34.
\]

Hence

\[
p>\frac1{12}.
\]

Now `u'=u+1`, so

\[
g=p-2\lambda
>\frac1{12}-\frac{38}{503}
=\boxed{\frac{47}{6036}}>0.
\]

Thus

\[
\boxed{
u\ge1\text{ odd }\Longrightarrow g>0.}
\]

## 4. Exact residual negative edges

At `u=0`,

\[
p(q,0)=0.
\]

Therefore an odd edge has

\[
\boxed{
g=-\lambda\quad(\varepsilon=0),}
\]

or

\[
\boxed{
g=-2\lambda\quad(\varepsilon=1).}
\]

These are the only negative coefficient-valid unit edges under `H_u`.

Hence the complete unit-edge classification is

| edge | condition | reduced cost under `H_u` |
|---|---|---:|
| even | `u>=1` | `0` |
| odd | `u>=1, eps=0` | `>351/4024` |
| odd | `u>=1, eps=1` | `>47/6036` |
| odd | `u=0, eps=0` | `-lambda` |
| odd | `u=0, eps=1` | `-2 lambda` |

## 5. Consequence for paid clusters

A paid odd event is precisely an odd event at positive slack `u>=1`.

Therefore every paid odd event is strictly Bellman-safe under `H_u`, independent of the total paid count `r`.
All coefficient-valid even steps inside the same positive-slack excursion are neutral.

Consequently

\[
\boxed{
\text{every positive-slack excursion / paid cluster is internally Bellman-safe.}
}
\]

This statement is stronger, for the final Bellman accounting, than asking whether each paid-count layer is individually safe without a potential.

It does **not** mean that the same-integer descent certificates for `r=2,3,...` have been computed. It means that positive-slack paid count is no longer where negative reduced cost can originate once `H_u` is used.

## 6. Endpoint cost

The first coefficient-cell path starts at

\[
q=d=0,\qquad u=0.
\]

Immediately before the first coefficient-failure even transition, MATH-053 gives again

\[
u=0.
\]

Thus over the complete first-cell interior the slack potential has zero net endpoint contribution:

\[
\boxed{H_u(\text{end})-H_u(\text{start})=0.}
\]

Unlike the resolution potential `H_R`, `H_u` therefore consumes no additive first-cell endpoint allowance.

## 7. Meaning of the remaining problem

After MATH-075, all possible negative Bellman cost is localized to odd steps taken exactly on the coefficient boundary

\[
\boxed{u=0.}
\]

These are the zero-penalty, or free-odd, transitions.

When `epsilon=0`, one free odd contributes one slope unit of debt.
When `epsilon=1`, it raises slack from `0` to `1`; returning to the boundary later requires at least one even step, and the free odd carries two slope units of debt under the slack potential.

This identifies the remaining negative language as the coefficient-boundary mechanical skeleton plus the same-integer/Hensel address constraints.

## 8. Relation to the previous paid-count frontier

MATH-062 through MATH-071 analyzed paid-count layers without the present slack potential and eventually closed `r>=14` by exact finite certificates.

MATH-075 changes the proof strategy:

\[
\boxed{
\text{positive-slack paid region}
\Longrightarrow
\text{locally nonnegative Bellman region under }H_u.
}
\]

Therefore the final common-potential route need not automatically continue the expensive layer-by-layer descent calculation through `r=13,...,2`.
Those layers remain unclosed as standalone same-integer descent statements, but they are not the current source of negative unit Bellman weight.

## 9. DSD boundary

Established:

- exact neutralization of every internal even edge;
- strict positive reduced cost for every positive-slack odd edge;
- exact identification of `u=0` odd edges as the only residual negative unit edges;
- zero total endpoint overhead of `H_u` across the first coefficient cell.

Not established:

- that the remaining free-odd boundary language is empty;
- that Hensel dominance alone removes every free-odd history;
- that the combined `H_u+H_R` closes the first cell;
- first-cell emptiness;
- Collatz.

## 10. Next target

Combine

\[
H_u=-\lambda u
\]

with the MATH-073 resolution potential

\[
H_R=-\lambda R
\]

and MATH-074 carry/address envelope.
The purpose is to determine how many boundary free-odd transitions can survive before exact dyadic resolution or Hensel dominance forces a handoff.

## Reproducibility

`collatz/src/2026_09_12_math075_slack_bellman_potential.py`
