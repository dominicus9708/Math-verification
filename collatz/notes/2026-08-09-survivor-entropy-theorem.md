# Exact entropy of the coefficient-survival parity language

Date: 2026-08-09

Let

\[
\alpha=\frac{\log2}{\log3},\qquad a_k=\lceil\alpha k\rceil.
\]

Let \(P_k\) be the set of binary words \(w=b_0\cdots b_{k-1}\) whose prefix
odd-counts \(q_j\) satisfy

\[
q_j\ge\lceil\alpha j\rceil\qquad(1\le j\le k).
\]

Equivalently, the multiplicative Collatz coefficient has not contracted through
any of the first \(k\) accelerated steps.

## Theorem

Put

\[
\rho=\frac{1-\alpha}{\alpha}=\log_2 3-1<1.
\]

Then

\[
\boxed{
\frac1k\binom{k}{a_k}
\le |P_k|
\le
\frac{1}{1-\rho}\binom{k}{a_k}
=\frac{1}{2-\log_2 3}\binom{k}{a_k}.
}
\]

Consequently

\[
\boxed{
\lim_{k\to\infty}\frac{1}{k}\log_2|P_k|
=H_2(\alpha),
}
\]

where

\[
H_2(\alpha)
=-\alpha\log_2\alpha-(1-\alpha)\log_2(1-\alpha)
\approx0.9499555271883306.
\]

### Lower bound

Among all \(\binom{k}{a_k}\) words with exactly \(a_k\) ones, define partial
sums

\[
S_j=q_j-\alpha j.
\]

Because \(\alpha\) is irrational, \(S_0,\ldots,S_{k-1}\) are pairwise distinct.
Since \(S_k=a_k-\alpha k>0\), rotating a word immediately after the unique
minimum of its cyclic partial sums produces a rotation satisfying
\(S_j>0\) for every nonempty prefix.  Thus every cyclic orbit contains at least
one member of \(P_k\).  An orbit has at most \(k\) members, so

\[
|P_k|\ge\frac1k\binom{k}{a_k}.
\]

### Upper bound

A surviving word must end with at least \(a_k\) ones, hence

\[
|P_k|\le\sum_{e\ge0}\binom{k}{a_k+e}.
\]

For each \(e\ge0\),

\[
\frac{\binom{k}{a_k+e}}{\binom{k}{a_k}}
=\prod_{h=1}^{e}\frac{k-a_k-h+1}{a_k+h}
\le\rho^e.
\]

Summing the geometric series gives the stated upper bound.

Finally \(a_k/k\to\alpha\), and Stirling's formula gives

\[
\frac1k\log_2\binom{k}{a_k}\to H_2(\alpha).
\]
The polynomial factor \(k\) and the constant \((1-\rho)^{-1}\) vanish after
division by \(k\), proving the entropy formula.

## Interpretation

The survivor language is exponentially sparse inside all \(2^k\) parity words,
but it still has positive entropy:

\[
|P_k|=2^{H_2(\alpha)k+O(\log k)}.
\]

Thus sparsity alone cannot establish emptiness of the exceptional language.  A
proof must use arithmetic realization / small-residue information in addition to
combinatorial entropy.
