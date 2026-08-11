# State escape and small contracting returns

Date: 2026-08-11

Status: **exact consequence of the harmonic correction corridor** for a nonperiodic no-first-descent odd-event orbit. It sharpens the geometric picture of the remaining hard core but does not exclude it.

Let `n>=3` be fixed, let `x_i` be its nonperiodic odd-event orbit, and assume

\[
x_i\ge n\qquad\text{for every }i.
\]

Use

\[
\lambda_i=\frac{2^{A_i}}{3^i},
\qquad
c_i=\frac13\sum_{j<i}\lambda_j,
\qquad
\lambda_i x_i=n+c_i.
\]

The harmonic-correction theorem gives

\[
\boxed{
\sum_{i=0}^{q-1}\lambda_i=O_n(q^{1/9}),
\qquad
c_q=O_n(q^{1/9}).
}
\]

## 1. Counting visits below a state threshold

Since

\[
\lambda_i x_i=n+c_i\ge n,
\]

we have

\[
\boxed{\lambda_i\ge\frac{n}{x_i}.}
\]

Thus, if `x_i<=X`, then `lambda_i>=n/X`. Therefore

\[
\frac nX
\#\{0\le i<q:x_i\le X\}
\le
\sum_{i<q}\lambda_i,
\]

so

\[
\boxed{
\#\{0\le i<q:x_i\le X\}
=O_n(Xq^{1/9}).
}
\]

This holds uniformly for every threshold `X>=n`.

## 2. Density-one polynomial state escape

Fix any

\[
0<\theta<\frac89.
\]

Set `X=q^theta`. Then

\[
\#\{i<q:x_i\le q^\theta\}
=O_n(q^{\theta+1/9})
=o(q).
\]

Hence

\[
\boxed{
\frac1q
\#\{i<q:x_i>q^\theta\}
\longrightarrow1
\qquad(0<\theta<8/9).
}
\]

Thus a hypothetical nonperiodic no-first-descent orbit spends density one of its odd-event time above every polynomial scale `q^theta` with exponent below `8/9`.

## 3. Contracting checkpoints return to a small-state envelope

At a contracting checkpoint

\[
\lambda_i>1.
\]

Then

\[
x_i=\frac{n+c_i}{\lambda_i}<n+c_i.
\]

Therefore

\[
\boxed{
x_i=O_n(i^{1/9})}
\]

along every contracting checkpoint.

So the same hypothetical orbit has a strongly intermittent geometry:

- at density-one event times, the state exceeds `q^theta` for every `theta<8/9`;
- every return to the contracting side occurs inside an `O(q^{1/9})` state envelope.

This is compatible with the earlier bound that contracting checkpoints themselves number only `O(q^{1/9})` up to event time `q`.

## 4. Rank of contracting returns

Enumerate contracting checkpoint indices as

\[
q_1<q_2<\cdots.
\]

Their endpoint states `x_{q_j}` are distinct because the orbit is nonperiodic, and for positive event indices they are coprime to `6`. Therefore the `j`th distinct contracting state is at least of order `j` (indeed at least the `j`th positive integer coprime to `6`).

But

\[
x_{q_j}=O_n(q_j^{1/9}).
\]

Consequently

\[
\boxed{q_j=\Omega_n(j^9).}
\]

This is the indexed form of contracting-checkpoint sparsity.

## 5. Proof-role interpretation

The nonperiodic hard core is no longer an arbitrary near-critical orbit. It must exhibit an intermittent excursion pattern:

\[
\boxed{
\text{density-one large-state background}
\longleftrightarrow
\text{sparse small contracting returns}.
}
\]

The next useful filter must constrain the arithmetic mechanism that permits repeated transitions between these two scales. Merely extending the parity/exponent congruence is insufficient, as shown by the reset-pullback redundancy lemma.
