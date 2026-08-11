# Renewal resonance and continued-fraction dichotomy

Date: 2026-08-11

Status: **exact/standard-number-theoretic consequence of the renewal-floor resonance bound**. It narrows aggregate-supercritical renewal segments to optimal Diophantine approximants or combinatorially large excursions.

## 1. Setup

For one renewal-floor segment let

\[
H:=\sum h_r,
\qquad
D:=\sum d_r,
\qquad
m:=\text{number of maximal blocks},
\]

and let `N'` be the next renewal floor. Put

\[
\alpha:=\log_2\frac32,
\qquad
\Delta:=D-\alpha H.
\]

The aggregate multiplier is

\[
P=2^\Delta.
\]

For a supercritical renewal segment,

\[
\boxed{\Delta>0.}
\]

The renewal-floor correction theorem gives

\[
\boxed{
\Delta
\le
\frac{1}{3\ln2}
\log\left(1+\frac{3(m-1)}{N'}\right)
+O\left(\frac1{N'}\right).
}
\]

## 2. Rational approximation form

Because `D,H` are positive integers,

\[
\boxed{
\frac{D}{H}-\alpha
=\frac{\Delta}{H}>0.
}
\]

Thus every aggregate-supercritical renewal segment gives a rational upper approximation `D/H` to `alpha`.

## 3. Legendre filter

Legendre's classical theorem states that if an irrational `alpha` and a reduced rational `p/q` satisfy

\[
\left|\alpha-\frac pq\right|<\frac1{2q^2},
\]

then `p/q` is a continued-fraction convergent of `alpha`.

Hence if

\[
\boxed{\Delta<\frac1{2H},}
\]

then the reduced form of

\[
\boxed{D/H}
\]

must be a convergent of

\[
\boxed{\alpha=\log_2(3/2).}
\]

Thus sufficiently short supercritical renewal segments are forced onto the sparse continued-fraction optimal-approximation layer.

## 4. Non-convergent excursions must be combinatorially large

If the reduced rational `D/H` is not a convergent of `alpha`, then

\[
\boxed{\Delta\ge\frac1{2H}.}
\]

For `m/N'` small, the renewal upper bound is

\[
\Delta
\le
\frac{m-1}{N'\ln2}
+O\left(\frac1{N'}\right).
\]

Therefore, after absorbing the lower-order term, there is an absolute positive constant `c` such that every sufficiently large non-convergent supercritical renewal segment satisfies

\[
\boxed{mH\ge cN'.}
\]

The precise value of `c` is not important for the structural use; the point is the forced linear-scale combinatorial cost.

## 5. Renewal exceptional-set dichotomy

Every sufficiently late aggregate-supercritical renewal segment therefore belongs to one of two exceptional classes:

\[
\boxed{
\begin{array}{ll}
\text{Arithmetic resonance:}& D/H\text{ is a continued-fraction convergent of }\alpha,\\[1mm]
\text{Combinatorial overload:}& mH\gtrsim N'.
\end{array}
}
\]

This is stronger than the raw statement `P>1` but still not a proof of exclusion.

## 6. Relation to linear forms in logarithms

The positive discrepancy corresponds to the nonzero linear form

\[
(D+H)\log2-H\log3=\Delta\log2.
\]

Baker/Matveev theory supplies effective lower bounds in terms of the coefficient height. Such bounds can further quantify the minimum length required by extremely close renewal resonances. However they do not currently close the problem without an independent upper control of `H` relative to `N'`.

## 7. Current role

The nonperiodic problem can now be viewed on the renewal-floor skeleton:

- aggregate-subcritical segments are ordinary floor-increasing steps;
- aggregate-supercritical segments must either use a continued-fraction optimal exponent ratio or pay a large `mH` cost relative to the next floor.

A future unified progress theorem may eliminate both exceptional mechanisms by combining exact formation addresses with the renewal-floor growth.