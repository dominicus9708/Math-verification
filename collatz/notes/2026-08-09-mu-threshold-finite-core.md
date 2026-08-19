# Finite-core threshold decision for the minimal-survivor function

Date: 2026-08-09

Status: **DERIVED ALGORITHMIC COROLLARY**

This is a general threshold-decision version of the canonical core-reconstruction idea already used in the first-crossing branch. It is not an asymptotic lower bound for `mu(K)`.

## 1. Problem

For the accelerated Collatz map, define

\[
\mu(K)=\min\{n\ge1:\tau_c(n)>K\},
\]

where `tau_c(n)` is the first depth at which the multiplicative coefficient falls below one.

Fix a numerical threshold `U>=1`. We want to decide exactly whether

\[
\boxed{\mu(K)\le U}
\]

or equivalently certify

\[
\mu(K)>U.
\]

## 2. Bit cutoff

Let

\[
\boxed{B=\lfloor\log_2 U\rfloor+1,}
\]

so

\[
2^B>U.
\]

Every candidate `n<=U` satisfies

\[
0<n<2^B.
\]

The first `B` accelerated parity bits determine `n mod 2^B` uniquely by the classical parity-vector bijection. Since `n` already lies in `[0,2^B)`, that canonical residue is the integer `n` itself.

Therefore after depth `B`, there is no independent high-bit lift freedom for any candidate below `U`: its remaining orbit is determined by the reconstructed integer.

Equivalently, in the min-plus lift notation, every further nonzero lift would cost at least

\[
2^B>U
\]

and therefore cannot belong to a start below the threshold.

## 3. Exact decision algorithm

Assume first `B<=K`.

1. Generate all length-`B` parity prefixes surviving the coefficient barrier.
2. Reconstruct each canonical residue `r in [0,2^B)`.
3. Discard `r=0` and `r>U`.
4. For each remaining integer `r`, follow its actual deterministic orbit from depth `B` through depth `K`.
5. If any candidate survives through `K`, then `mu(K)<=U`; otherwise `mu(K)>U`.

If `B>K`, simply work at depth `K`; no extra reduction is needed.

This is an exact finite certificate procedure. It uses no probabilistic assumption.

## 4. Candidate-count bound

Let

\[
\alpha=\log_3 2>1/2,
\qquad
a_B=\lceil\alpha B\rceil.
\]

A coefficient-surviving length-`B` word must in particular have at least `a_B` odd bits at its endpoint. Ignoring the prefix barrier can only increase the count, hence

\[
|P_B|
\le
\sum_{q=a_B}^{B}\binom Bq.
\]

Since the binomial coefficients decrease for `q>B/2`,

\[
|P_B|
\le
(B+1)\binom B{a_B}.
\]

Let

\[
H:=H_2(\alpha)
=-\alpha\log_2\alpha-(1-\alpha)\log_2(1-\alpha)
\approx0.9499555271883306.
\]

Because `a_B/B>=alpha` and binary entropy decreases on `[1/2,1]`,

\[
\boxed{
|P_B|\le(B+1)2^{HB}.
}
\]

As `2^B<2U`, this gives the threshold-core envelope

\[
\boxed{
|P_B|=O\!\left((\log U)U^H\right).
}
\]

This is a count of nominal survivor cores before the canonical-residue cutoff `r<=U`, so the actual candidate count can only be smaller.

## 5. Polynomial thresholds in K

If the desired lower bound has polynomial scale

\[
U(K)=C K^p
\]

with fixed `C,p>0`, then

\[
B=p\log_2K+O(1),
\]

and the number of nominal coefficient-surviving cores is

\[
\boxed{
|P_B|=K^{pH+o(1)}.
}
\]

For the current sufficient growth target `p=8.616`,

\[
\boxed{pH\approx8.1848168223.}
\]

Thus each fixed-`K` threshold statement

\[
\mu(K)>C K^{8.616}
\]

has an exact deterministic finite-core verification whose nominal state count is polynomial in `K` (before accounting for the cost of following each deterministic tail).

This does **not** prove the statement uniformly for all `K`; it only shows that the target is not computationally equivalent to enumerating all `2^K` parity words.

## 6. Consistency check with the existing first-crossing core count

The earlier first-crossing reconstruction used the unconditional scale

\[
U(\sigma)=O(\sigma^{14.3}).
\]

The same entropy exponent gives

\[
14.3H
\approx13.5843640388,
\]

which reproduces the exponent already recorded in `core-reconstruction-theorem.md` for the crude parity-core count.

Thus the present threshold-decision theorem is the generic minimal-survivor version of the same finite-core principle rather than an unrelated counting argument.

## 7. Relation to prefix first-hit pruning

The bit cutoff is the extreme version of the prefix first-hit lower bound.

If an incumbent/threshold satisfies `U<2^k`, then at depth `k` any state requiring even one additional canonical lift has

\[
r_{\rm descendant}\ge r+2^k>U.
\]

Hence only states with zero future lift can remain under the threshold. Their tails are deterministic.

For `k<B`, the monotone prefix bounds `L_ell` can prune states earlier, before the full bit cutoff is reached.

## 8. Remaining proof issue

A polynomial-time-in-`K` family of finite checks is not a proof over infinitely many `K`. A global theorem still needs a uniform structural reason why every core below the proposed threshold eventually violates the coefficient barrier.

The current matrix/min-plus program therefore has two complementary roles:

1. reduce each fixed threshold problem to a small exact core;
2. search for a reusable dominance or arithmetic obstruction that certifies all sufficiently large `K` at once.