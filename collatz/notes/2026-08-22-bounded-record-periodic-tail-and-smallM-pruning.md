# Bounded-record periodic-tail and small-M pruning

Date: 2026-08-22

Status: **exact pruning results inside the bounded-record branch.** These results remove eventually periodic high-density tails and close the cases with eventual record bound `M<=3`. They do not close the general bounded-record branch and are not a proof of the Collatz conjecture.

Let the accelerated Collatz parity sequence of a positive integer `N` have odd-step positions

\[
0\le p_1<p_2<\cdots,
\]

where `p_i` is the zero-based position of the `i`-th odd accelerated step. The exact parity-series identity is

\[
\boxed{
\sum_{i\ge1}\frac{2^{p_i}}{3^i}=-N
\qquad\text{in }\mathbb Z_2.
}
\]

For coefficient-surviving divergent candidates the same series also converges in the real norm whenever the odd density is strictly larger than

\[
\alpha=\log_3 2.
\]

## 1. Eventually periodic odd-gap tails are impossible above the critical density

Assume that from some index `i0` onward the odd positions have an eventually periodic gap pattern. Equivalently, there are integers

\[
A\ge1,\qquad B\ge1
\]

such that

\[
\boxed{p_{i+B}=p_i+A}
\]

for all sufficiently large `i`.

The tail of the parity series then breaks into `B` geometric subsequences with common ratio

\[
\boxed{\rho=\frac{2^A}{3^B}.}
\]

If

\[
\boxed{2^A<3^B,}
\]

then `|rho|<1` in the real norm. Since `A>0`, also

\[
|\rho|_2=2^{-A}<1.
\]

Therefore each geometric subsequence converges in both `R` and `Q_2` to the **same rational number**

\[
\frac{u}{1-2^A/3^B}\in\mathbb Q.
\]

Adding the finite prefix, the entire parity series is a rational number `S in Q` whose real value is strictly positive, because every summand is positive:

\[
\boxed{S>0\quad\text{in }\mathbb R.}
\]

But the exact 2-adic parity identity says that the same rational element satisfies

\[
\boxed{S=-N\quad\text{in }\mathbb Q_2.}
\]

The embeddings of `Q` into `R` and `Q_2` preserve the underlying rational equality. Hence `S=-N` as rational numbers, contradicting `S>0` and `N>0`.

Thus:

\[
\boxed{
\text{No positive-integer Collatz orbit can have an eventually periodic odd-gap tail with }2^A<3^B.
}
\]

Equivalently, any eventually periodic parity tail with asymptotic odd density

\[
\frac BA>\alpha
\]

is impossible for a positive integer.

This is an exact adelic obstruction: the same geometric series would have to represent one positive rational in the real completion and the negative integer `-N` in the 2-adic completion.

## 2. Consequence for eventual bounded record length

Suppose the record-height gaps satisfy

\[
L_r\le M
\]

eventually. The bounded-record linear-height theorem gives

\[
\liminf_{k\to\infty}\frac{m_k}{k}
\ge
\alpha+\frac1M
>
\alpha.
\]

Therefore, if such a bounded-record tail were eventually periodic in its parity bits or in its odd-gap pattern, its period would have

\[
\frac BA\ge\alpha+\frac1M>\alpha,
\]

hence

\[
2^A<3^B.
\]

The theorem above excludes it.

So any hypothetical bounded-record counterexample must have a **genuinely aperiodic** tail. In particular, a finite Hensel/record quotient is not allowed to close the problem merely by leaving an eventually periodic cycle: every such high-density cycle is already arithmetically impossible for a positive integer.

## 3. Exact closure for `M<=3`

A record first-passage macro has final mechanical Beatty bit zero. For lengths at most three, the only possible mechanical factors ending in zero are

\[
0,
\qquad
10,
\qquad
010,
\qquad
110.
\]

The corresponding record first-passage parity words are uniquely

\[
\begin{array}{c|c}
\text{mechanical factor}&\text{record parity word}\\\hline
0&1\\
10&11\\
010&011\\
110&111.
\end{array}
\]

Hence **every record macro of length at most three is singleton**.

The previously proved singleton theorem states that an infinite tail consisting only of singleton record macros becomes all-odd after at most the initial boundary adjustment. An all-odd accelerated parity tail would require

\[
2^k\mid x+1
\]

for arbitrarily large `k`, impossible for a fixed positive integer `x`.

Therefore

\[
\boxed{
L_r\le3\text{ eventually is impossible.}
}
\]

So any hypothetical eventually bounded record tail must satisfy

\[
\boxed{M\ge4}
\]

and contain infinitely many non-singleton records.

## 4. What remains

The bounded-record branch is now pruned to tails that are simultaneously

1. genuinely aperiodic;
2. bounded by some fixed `M>=4`;
3. of odd density at least `alpha+1/M`;
4. forced to contain infinitely many non-singleton records;
5. supplied with a fresh terminal Haar contraction at every non-singleton record.

The remaining issue is not a finite periodic cycle. It is an aperiodic 2-adic/3-adic alignment problem.

Companion finite regression:

`collatz/src/bounded_record_periodic_smallM_certificate.py`.
