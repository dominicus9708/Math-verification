# Sparse contracting checkpoints in a nonperiodic first-descent survivor

Date: 2026-08-11

Status: **exact consequence of the harmonic correction corridor**. This note does not prove nonexistence of the survivor.

Let `n>=3` be a fixed odd start whose odd-event Syracuse orbit is nonperiodic and satisfies `x_q>=n` for every event index. Use

\[
\lambda_q=\frac{2^{A_q}}{3^q},
\qquad
c_q=\sum_{i<q}\frac{2^{A_i}}{3^{i+1}}.
\]

The exact cumulative identity is

\[
\boxed{
c_q=\frac13\sum_{i=0}^{q-1}\lambda_i.
}
\]

The harmonic-correction theorem gives

\[
\boxed{c_q=O_n(q^{1/9}).}
\]

Hence

\[
\boxed{
\sum_{i=0}^{q-1}\lambda_i=O_n(q^{1/9}).
}
\]

For any threshold `t>0`, positivity gives the deterministic counting estimate

\[
\boxed{
\#\{0\le i<q:\lambda_i\ge t\}
\le
\frac{1}{t}\sum_{i<q}\lambda_i
=O_n\!\left(\frac{q^{1/9}}{t}\right).
}
\]

In particular, the contracting odd-event checkpoints

\[
\lambda_i>1
\]

satisfy

\[
\boxed{
\#\{i<q:\lambda_i>1\}=O_n(q^{1/9}).
}
\]

Therefore their natural density in event time is zero.

More generally, fix `0<a<8/9` and take `t=q^{-a}`. Then among the first `q` checkpoints, at most

\[
O_n(q^{1/9+a})=o(q)
\]

have `lambda_i>=q^{-a}`. Thus a density-one proportion satisfy

\[
\boxed{
\lambda_i<q^{-a}
}
\]

when viewed inside the first `q` events.

Since

\[
\log_2\lambda_i=A_i-i\log_2 3,
\]

this says that a hypothetical nonperiodic no-first-descent orbit spends a density-one proportion of odd-event checkpoints logarithmically below the multiplicative balance line, while the set of contracting or near-contracting checkpoints is sparse.

This should be combined with the bounded-formation / 2-adic naturality condition rather than treated as a standalone convergence proof.
