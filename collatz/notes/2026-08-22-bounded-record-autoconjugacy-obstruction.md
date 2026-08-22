# Bounded-record tail and the autoconjugacy obstruction

Date: 2026-08-22

Status: **literature-aligned structural reduction.** This note identifies a necessary 2-adic irrationality property of any hypothetical bounded-record divergent positive integer. It does not prove the remaining irrational case impossible and is not a proof of the Collatz conjecture.

Reference used here:

K. G. Monks and J. Yazinski, *The Autoconjugacy of the 3x+1 Function*, Discrete Mathematics 275 (2004), 219-236, DOI 10.1016/S0012-365X(03)00125-0.

Let

\[
\alpha=\frac{\ln2}{\ln3}=\log_3 2.
\]

For a 2-adic integer `x`, let

\[
\kappa_n(x)
\]

be the number of odd entries among the first `n` terms of its accelerated Collatz parity vector.

Monks--Yazinski prove two facts relevant here.

1. The autoconjugacy `Omega` complements the parity vector, so

\[
\kappa_n(x)+\kappa_n(\Omega(x))=n.
\]

2. If `x` is a rational 2-adic integer with divergent orbit, then

\[
\boxed{
\alpha
\le
\liminf_{n\to\infty}\frac{\kappa_n(x)}{n}.
}
\]

They also show that `Omega` commutes with the Collatz map and hence preserves divergence.

## 1. Apply the bounded-record density theorem

Assume a hypothetical positive integer `N` has divergent orbit and eventually bounded record gaps

\[
L_r\le M.
\]

The bounded-record linear-height theorem proved in this branch gives

\[
\boxed{
\liminf_{n\to\infty}
\frac{\kappa_n(N)}{n}
\ge
\alpha+\frac1M.
}
\]

Since `Omega` complements every parity bit,

\[
\frac{\kappa_n(\Omega(N))}{n}
=
1-rac{\kappa_n(N)}{n}.
\]

Therefore

\[
\boxed{
\limsup_{n\to\infty}
\frac{\kappa_n(\Omega(N))}{n}
\le
1-\alpha-\frac1M.
}
\]

But

\[
1-\alpha<\alpha
\]

because `alpha>1/2`. Hence

\[
\boxed{
1-\alpha-\frac1M<\alpha.
}
\]

## 2. The autoconjugate cannot be rational

Suppose for contradiction that

\[
\Omega(N)\in\mathbb Q_{\rm odd}.
\]

Because `Omega` is an autoconjugacy and `N` is assumed divergent, `Omega(N)` is also divergent. Monks--Yazinski then require

\[
\alpha
\le
\liminf
\frac{\kappa_n(\Omega(N))}{n}.
\]

This contradicts the stronger upper bound

\[
\limsup
\frac{\kappa_n(\Omega(N))}{n}
\le
1-\alpha-\frac1M
<\alpha.
\]

Therefore

\[
\boxed{
\Omega(N)\notin\mathbb Q_{\rm odd}.
}
\]

So every hypothetical bounded-record divergent positive integer would necessarily have an **irrational 2-adic autoconjugate**.

## 3. Interpretation

This result is not surprising from the global literature: Monks--Yazinski show that rationality of the autoconjugate on positive integers is already equivalent to excluding divergent positive-integer orbits.

The useful point here is localization. The current proof program has reduced the bounded-record post-atomic tail to precisely the branch on which the standard rational-autoconjugacy escape route is unavailable.

The remaining candidate must therefore be simultaneously

- a positive ordinary integer;
- divergent;
- eventually record-bounded by some finite `M>=4`;
- genuinely aperiodic;
- of parity lower density at least `alpha+1/M`;
- equipped with infinitely many non-singleton fresh Haar shells;
- and mapped by `Omega` to an irrational 2-adic integer whose complementary parity density lies strictly below `alpha`.

This identifies the remaining obstacle as a genuinely arithmetic rational/irrational cross-completion problem, not an omitted standard density theorem.
