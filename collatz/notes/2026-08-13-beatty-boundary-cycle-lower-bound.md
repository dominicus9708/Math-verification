# Cycle-lemma lower bound for the Beatty coefficient-survival boundary

Date: 2026-08-13

Status: **general combinatorial lower bound** for the boundary layer of the coefficient-survival language. The bound is weak compared with finite data but holds at arbitrary depth and has a divergent harmonic-scale cumulative effect. It is a symbolic-language statement, not a Collatz proof.

## 1. Coefficient-survival language

Put

\[
\alpha:=\log_3 2>\frac12,
\qquad
b_j:=\lceil \alpha j\rceil.
\]

For a binary parity word of length `L`, let `q_j` be the number of `1` symbols among its first `j` positions.

The coefficient-survival condition is

\[
\boxed{q_j\ge b_j\quad(1\le j\le L).}
\]

Let `C_L^{class}` be the number of length-`L` words satisfying every prefix condition.

At a Beatty barrier-rise step

\[
b_{L+1}=b_L+1,
\]

define the boundary count

\[
\boxed{
D_L^{class}:=
\#\{w:q_j(w)\ge b_j\ (j\le L),\ q_L(w)=b_L\}.
}
\]

A boundary parent has exactly one coefficient-surviving binary child at the next step.

## 2. One good cyclic rotation

Write

\[
b:=b_L=\lceil \alpha L\rceil.
\]

Take any binary word of length `L` with exactly `b` ones and define real increments

\[
x_i:=w_i-\alpha.
\]

Their total sum is

\[
\sum_{i=1}^L x_i=b-\alpha L>0,
\]

because `alpha` is irrational.

Let `S_j=sum_{i<=j} x_i`, with `S_0=0`, and choose an index `m` at which the cyclic prefix sequence attains a minimum. Rotate the word so that the position after `m` comes first.

For every prefix of the rotated word, the corresponding increment sum is nonnegative: before wrap this follows from minimality of `S_m`; after wrap it follows from the same minimality plus the positive total sum.

Hence the rotated word satisfies

\[
q_j-\alpha j\ge0
\]

for every prefix. Since `alpha*j` is nonintegral,

\[
q_j\ge\lceil\alpha j\rceil=b_j.
\]

Thus **every** length-`L`, weight-`b` word has at least one cyclic rotation in the coefficient-survival boundary language.

Each surviving boundary word can be the cyclic image of at most `L` source words. Therefore

\[
\boxed{
D_L^{class}
\ge
\frac1L\binom{L}{b}.
}
\]

The automatic first two `1` symbols required by the `N=3 mod 4` core need not be imposed separately: the Beatty conditions at `j=1,2` already force them.

## 3. Upper bound for the full survivor language

Forget all prefix conditions except the final one. Then

\[
C_L^{class}
\le
\sum_{q=b}^L\binom Lq.
\]

For `q>=b`,

\[
\frac{\binom L{q+1}}{\binom Lq}
=\frac{L-q}{q+1}
\le
\frac{L-b}{b+1}
=:\rho<1.
\]

Hence the binomial tail is bounded geometrically:

\[
\sum_{q=b}^L\binom Lq
\le
\binom Lb\frac1{1-\rho}
=
\binom Lb\frac{b+1}{2b+1-L}.
\]

Combining with Section 2 gives

\[
\boxed{
\frac{D_L^{class}}{C_L^{class}}
\ge
\frac{2b+1-L}{L(b+1)}.
}
\]

## 4. Asymptotic form

Since

\[
\frac bL\to\alpha,
\]

the lower bound has asymptotic scale

\[
\boxed{
\frac{D_L^{class}}{C_L^{class}}
\ge
\frac{2\alpha-1}{\alpha}\frac1L
+O(L^{-2}).
}
\]

Numerically,

\[
\boxed{
\frac{2\log_3 2-1}{\log_3 2}
\approx0.41505.
}
\]

Thus the theorem guarantees a boundary fraction of harmonic order `1/L` at every Beatty-rise depth.

Finite exact ballot DP gives much larger fractions (roughly `0.075`--`0.30` through depth 2000), but those finite observations are not used in the proof.

## 5. Cumulative significance

The Beatty barrier rises with positive density `alpha`. Therefore the sum of the proven boundary lower-bound scales over rise depths diverges:

\[
\sum_{\substack{L:\ b_{L+1}=b_L+1}}
\frac{2b_L+1-L}{L(b_L+1)}
=\infty.
\]

Consequently, in an ideally balanced binary-child transport where the correlation error vanished, repeated boundary pruning would force the coefficient-survivor mass downward indefinitely.

The actual cross-base problem is now isolated cleanly: prove that the ternary--dyadic correlation error is small enough compared with this boundary mass on a growing sequence of resolutions.

## 6. Relation to the mass-transport identity

The companion transport theorem gives

\[
C_{L+1}
=C_L-\frac{D_L}{2}+\frac{K_L}{2}.
\]

The present theorem controls the **class** analogue of `D_L`; Fourier discrepancy is needed to transfer it to ternary-weighted mass and to control `K_L`.

This yields a natural two-channel program:

\[
\boxed{
\text{cycle/ballot boundary lower bound}
\quad+\quad
\text{Fourier correlation upper bound}.
}
\]

If the weighted analogue satisfies a comparable harmonic lower bound while `|K_L|=o(D_L)`, the transport products contract without any start-by-start enumeration.
