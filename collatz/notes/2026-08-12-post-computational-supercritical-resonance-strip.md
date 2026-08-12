# Post-computational supercritical resonance strip

Date: 2026-08-12

Status: **exact consequence of the external paradoxical-start lower bound plus the Christoffel extremal bound, followed by a standard Legendre continued-fraction dichotomy**. This is a finite-to-asymptotic bridge, not a Collatz proof.

## 1. External start lower bound

Rozier–Terracol (arXiv:2502.00948; Discrete Mathematics 349 (2026), 115167), Theorem 1.3, show computationally that any paradoxical sequence not among their finite small list must start above

\[
\boxed{M_0:=2.8\times10^{19}.}
\]

Every aggregate-supercritical renewal segment is acyclic paradoxical, because its coefficient is below `1` while its endpoint renewal floor is strictly larger than its start.

Hence every currently unresolved aggregate-supercritical renewal satisfies

\[
\boxed{N>N_0:=M_0,\qquad N'>N.}
\]

## 2. Christoffel extremal floor bound

For any aggregate-supercritical renewal word with accelerated length `A` and odd count `H`, the Fernández–Ibáñez Christoffel extremal inequality gives the rational shadow bound

\[
N'<C\le\frac{1}{2^{A/H}-3}.
\]

Since `N'>M_0`,

\[
2^{A/H}-3<\frac1{M_0}.
\]

Writing

\[
\gamma:=\log_2 3,
\]

we obtain

\[
\boxed{
0<\frac AH-\gamma
<
\varepsilon_0
:=
\log_2\left(1+\frac1{3M_0}\right).
}
\]

Numerically,

\[
\boxed{
\varepsilon_0\approx1.7174940963\times10^{-20}.
}
\]

Thus every unresolved aggregate-supercritical renewal lies in an absolute critical strip of width about `1.72e-20` above `log_2 3`.

This conclusion does **not** assume that `A/H` is a continued-fraction convergent.

## 3. Legendre threshold

Suppose the reduced rational form of `A/H` is not a continued-fraction convergent of `gamma`.

Legendre's theorem implies

\[
\left|\frac AH-\gamma\right|\ge\frac1{2H^2}.
\]

Combining with the critical strip,

\[
\frac1{2H^2}<\varepsilon_0.
\]

Therefore every unresolved non-convergent aggregate-supercritical renewal must satisfy

\[
\boxed{
H>H_0:=(2\varepsilon_0)^{-1/2}.
}
\]

Numerically,

\[
\boxed{
H_0\approx5.395570552\times10^9.
}
\]

Hence below roughly `5.40 billion` odd events, every surviving supercritical renewal ratio would have to be a genuine continued-fraction convergent.

## 4. Combination with the internal upper-CF frontier

The continued-fraction bridge already excludes primitive upper-CF renewals through the upper convergent

\[
(A,H)=(630138897,397573379).
\]

The next upper convergent is

\[
(A,H)=(10439860591,6586818670).
\]

Its odd count already exceeds `H_0`.

Thus the finite computational frontier and the standard Legendre threshold meet in the same region:

\[
\boxed{
\text{every presently unresolved aggregate-supercritical renewal has }H>5.39\times10^9.
}
\]

The statement is intentionally conservative: the first unresolved upper-CF candidate has the stronger value `H=6,586,818,670`, while a non-convergent candidate is only forced above the Legendre threshold.

## 5. Structural meaning

The supercritical renewal hard core is no longer merely `near critical` in a qualitative sense. After importing the finite paradoxical-start theorem, every remaining segment must satisfy the fixed universal slope window

\[
\boxed{
0<A/H-\log_2 3<1.72\times10^{-20}.
}
\]

Therefore the remaining aperiodic proof may treat aggregate-supercritical renewals as an ultra-resonant exceptional language.

Any final global argument can split this language into:

1. exact/best continued-fraction approximants at enormous denominator;
2. non-convergent rational approximants with `H>5.39e9` and correspondingly enormous renewal words.

The subcritical renewal sector remains separate and is controlled by the persistent floor/discrepancy budget rather than this paradoxical-start bound.
