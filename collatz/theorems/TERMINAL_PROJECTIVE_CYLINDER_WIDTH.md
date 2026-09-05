# Terminal projective cylinder width theorem

Status: **EXACT / CLOSED**

Executable regression guard:

- `../src/A0_s1_routeB_terminal_projective_cylinder_multiplicity_certificate.py`

## Uniform formation width

Let the current full target have length

\[
t_0=104,398,605,910
\]

and total one-count

\[
j_0=65,868,186,701.
\]

For target ranked-one positions

\[
a_1<a_2<\cdots<a_{j_0}\le t_0-1,
\]

the `r`-th position must leave at least `j0-r` later locations for the remaining target ones. Therefore

\[
a_r\le t_0-1-(j_0-r).
\]

A target-dominance candidate satisfies

\[
r-1\le b_r\le a_r.
\]

Hence every ranked position has the uniform interval-width bound

\[
\boxed{
a_r-(r-1)\le t_0-j_0
=38,530,419,209.
}
\]

No Christoffel approximation or floating-point logarithm is needed for this bound.

## Projective cylinder multiplicity

At remaining ternary precision `m`, the exact projective exponent period is

\[
\lambda_m=2\cdot3^{m-1}.
\]

A prescribed projective cylinder has the form

\[
b\equiv\beta\pmod{\lambda_m}.
\]

An arithmetic progression of spacing `lambda_m` meets an interval of width at most `D` in at most

\[
\left\lfloor\frac{D}{\lambda_m}\right\rfloor+1
\]

points.

Therefore every current dominance interval satisfies

\[
\boxed{
M_m
\le
\left\lfloor
\frac{38,530,419,209}{2\cdot3^{m-1}}
\right\rfloor+1.
}
\]

## Singleton threshold

The two decisive periods are

\[
\lambda_{23}=62,762,119,218,
\]

\[
\lambda_{22}=20,920,706,406.
\]

Thus

\[
\lambda_{23}>38,530,419,209
\]

but

\[
\lambda_{22}<38,530,419,209.
\]

Hence the exact threshold supplied by the uniform formation-width argument is

\[
\boxed{m_*=23.}
\]

For every

\[
m\ge23,
\]

a specified projective exponent cylinder is **empty or singleton** inside the complete legal target-dominance position interval.

## Current terminal resolutions

For `L=28`, the backward precisions are `28,27,...,1`.

The first six one-gates

\[
28,27,26,25,24,23
\]

are therefore singleton-or-empty at the exponent-cylinder level.

For `L=24`, the first two one-gates (`24,23`) have this property.

For `L=47`, the first twenty-five one-gates (`47` down through `23`) have this property.

The first lower-precision multiplicity bounds are:

| m | lambda_m | maximum points in one cylinder |
|---:|---:|---:|
| 28 | 15,251,194,969,974 | 1 |
| 27 | 5,083,731,656,658 | 1 |
| 26 | 1,694,577,218,886 | 1 |
| 25 | 564,859,072,962 | 1 |
| 24 | 188,286,357,654 | 1 |
| 23 | 62,762,119,218 | 1 |
| 22 | 20,920,706,406 | 2 |
| 21 | 6,973,568,802 | 6 |
| 20 | 2,324,522,934 | 17 |
| 19 | 774,840,978 | 50 |
| 18 | 258,280,326 | 150 |
| 17 | 86,093,442 | 448 |
| 16 | 28,697,814 | 1,343 |
| 15 | 9,565,938 | 4,028 |

These are worst-case legal-interval bounds, not empirical average branch counts.

## DSD interpretation

This separates two distinct multiplicities:

1. **carry / projective-state branching** — different predecessor/successor carry states can select different exponent residue cylinders;
2. **within-cylinder formation multiplicity** — how many legal exponent positions lie in one already-selected residue cylinder.

The theorem closes only the second question.

For `m>=23`, within-cylinder formation multiplicity is gone completely.

This does **not** revive the rejected local carry greedy rule. The carry/cylinder sequence still cannot be chosen myopically.

## Strategic consequence

The backward right-H filter has a strongly constrained high-precision head:

- terminal residue fixes the successor projective state;
- for a specified predecessor/cylinder state, the first six exponent gates at `L=28` have at most one legal position each;
- any branching there is entirely attributable to distinct projective predecessor states / grammar branches, not multiple positions inside one cylinder.

This gives the next implementation target a cleaner separation of branching sources and provides a direct audit metric for the right-H backward DP.

## Audit classification

### EXACT / CLOSED

- uniform dominance interval width `<=t0-j0`;
- projective cylinder multiplicity formula;
- singleton threshold `m=23`;
- current `L=24,28,47` singleton-gate counts.

### REGRESSION ONLY

The certificate exhaustively checks the elementary interval/progression counting implementation on small finite intervals and asserts the current integer constants.

### OPEN

- actual number of projective predecessor states surviving each terminal gate;
- compressed state count in the right H grammar;
- exact boundary state exported to the critical cut;
- forward/backward join against the 14-root Bellman scan.

### NOT CLAIMED

No root is closed by the width theorem alone.
