# R2 rational critical-density reduction

Date: 2026-08-13

Status: **external-theorem application + exact branch reduction**.  It shows that an aperiodic ordinary-integer coefficient-surviving trajectory must lie exactly on the critical parity-density boundary.  It does not exclude that boundary and does not prove Collatz.

## 1. Coefficient-survival density floor

For the accelerated map, let `q_K` be the number of odd parity symbols in the first `K` steps and put

\[
\beta=\log_3 2.
\]

Infinite coefficient survival means

\[
3^{q_K}\ge2^K
\]

for every `K`, hence

\[
\boxed{
\frac{q_K}{K}\ge\beta
}
\]

up to the exact ceiling formulation

\[
q_K\ge\lceil\beta K\rceil.
\]

Therefore any R2 path satisfies

\[
\boxed{
\liminf_{K\to\infty}\frac{q_K}{K}\ge\beta.
}
\]

## 2. External rational-2-adic theorem

Lopez and Stoll, *The 3x+1 Periodicity Conjecture in R* (arXiv:2101.12747), prove the following necessary condition: if a rational 2-adic integer has a non-cyclic `3x+1` trajectory, then its parity sequence must satisfy

\[
\boxed{
\liminf_{K\to\infty}\frac{q_K}{K}
=\frac{\ln2}{\ln3}
=\beta.
}
\]

An ordinary nonnegative integer is, of course, a rational 2-adic integer.

## 3. Exact R2 reduction

Suppose an ordinary positive integer gives an infinite coefficient-surviving trajectory.

If the trajectory is non-cyclic, the external theorem and the coefficient lower bound combine to force

\[
\boxed{
\liminf_{K\to\infty}\frac{q_K}{K}=\beta.
}
\]

Thus an aperiodic R2 candidate cannot retain any positive asymptotic odd-count surplus above the Beatty barrier.

Equivalently, with

\[
s_K=q_K-\lceil\beta K\rceil\ge0,
\]

we necessarily have

\[
\boxed{
\liminf_{K\to\infty}\frac{s_K}{K}=0.
}
\]

There are arbitrarily large depths at which the accumulated surplus is sublinear in the horizon.

## 4. Rational defect predecessor interpretation

For a finite same-cell reference prefix, the defect identity gives the rational alternate predecessor

\[
N^\sharp=N-C/3^q.
\]

It follows the reference prefix and merges with the ordinary candidate at the same endpoint.  Hence after that finite prefix its parity tail is identical to the candidate tail.

When `N^sharp` is nonintegral it is still a rational 2-adic integer.  If the common tail is aperiodic, the same Lopez--Stoll critical-density condition applies to `N^sharp`, and finite-prefix changes do not alter the lower asymptotic density.

Thus the defect/rational-predecessor bridge is compatible with, but does not strengthen beyond, the exact critical-density obstruction: all rational same-tail representatives are forced onto the same boundary.

## 5. Proof-program consequence

The R2 branch may now be divided cleanly into

1. a cyclic/periodic branch, which belongs with the independent nontrivial-cycle problem;
2. an aperiodic branch satisfying the exact critical-density condition above.

Therefore the aperiodic R2 target should no longer be stated as merely

> prove that the odd density cannot stay above the coefficient threshold.

Positive density surplus is already excluded by the rational 2-adic theorem.

The remaining target is sharper:

> exclude an ordinary eventually-zero canonical lift sequence whose parity path stays above the Beatty boundary while returning to sublinear surplus infinitely often.

This is precisely the regime in which the late-lift, spectral-renewal, Christoffel/Beatty, and 3-adic predecessor channels must interact.

## External reference

Josefina Lopez and Peter Stoll, *The 3x+1 Periodicity Conjeture in R*, arXiv:2101.12747 (2021).
