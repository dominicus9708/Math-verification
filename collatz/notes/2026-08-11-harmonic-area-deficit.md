# Harmonic area-deficit theorem

Date: 2026-08-11

Status: **exact consequence of the harmonic corridor for a hypothetical nonperiodic first-descent survivor**. This is a necessary-condition theorem, not a proof of Collatz.

## 1. Setup

Let an odd-event exponent path be

\[
0=A_0<A_1<\cdots,
\]

and define

\[
\lambda_i:=\frac{2^{A_i}}{3^i}.
\]

For a hypothetical fixed positive integer `n>=3` whose odd-event orbit is nonperiodic and never descends below `n`, the harmonic-correction theorem gives

\[
\boxed{
\sum_{i=0}^{q-1}\lambda_i\le C_n q^{1/9}
}
\]

for all sufficiently large `q`, for some constant `C_n>0`.

## 2. AM-GM compression

By the arithmetic-geometric mean inequality,

\[
\left(\prod_{i=0}^{q-1}\lambda_i\right)^{1/q}
\le
\frac1q\sum_{i=0}^{q-1}\lambda_i
\le
C_n q^{-8/9}.
\]

Taking base-2 logarithms,

\[
\frac1q\sum_{i=0}^{q-1}\log_2\lambda_i
\le
\log_2 C_n-\frac89\log_2 q.
\]

Since

\[
\log_2\lambda_i=A_i-i\log_2 3,
\]

we obtain

\[
\boxed{
\sum_{i=0}^{q-1}A_i
\le
\frac{\log_2 3}{2}q(q-1)
-\frac89 q\log_2 q
+O_n(q).
}
\]

Equivalently, if

\[
D_i:=A_i-i\log_2 3,
\]

then

\[
\boxed{
\sum_{i=0}^{q-1}D_i
\le
-\frac89 q\log_2 q+O_n(q).
}
\]

Thus the exponent path must accumulate a logarithmically growing negative area below the critical line.

## 3. Moving critical-strip sparsity

For any fixed `0<delta<8/9`, if

\[
D_i\ge-\delta\log_2 q,
\]

then

\[
\lambda_i=2^{D_i}\ge q^{-\delta}.
\]

Therefore

\[
q^{-\delta}
\#\{i<q:D_i\ge-\delta\log_2q\}
\le
\sum_{i<q}\lambda_i
\le C_nq^{1/9}.
\]

Hence

\[
\boxed{
\#\{i<q:D_i\ge-\delta\log_2q\}
=O_n\!\left(q^{1/9+\delta}\right).
}
\]

Because `1/9+delta<1`, the proportion tends to zero.

Thus for every `delta<8/9`, a density-one subset of event times satisfies

\[
\boxed{
D_i<-\delta\log_2q.
}
\]

This strengthens the earlier fixed-width critical-strip sparsity.

## 4. Valuation-budget form

Writing

\[
A_i=\sum_{j=0}^{i-1}v_j,
\qquad v_j\ge1,
\]

one has

\[
\sum_{i=0}^{q-1}A_i
=
\sum_{j=0}^{q-2}(q-1-j)v_j.
\]

Therefore the area deficit is equivalent to the weighted valuation constraint

\[
\boxed{
\sum_{j=0}^{q-2}(q-1-j)
\left(v_j-\log_2 3\right)
\le
-\frac89 q\log_2q+O_n(q).
}
\]

Any return to the critical line must therefore be supplied by late positive valuation jumps against a cumulative negative-area background.

## 5. Scope

This theorem is universal over a hypothetical nonperiodic first-descent survivor and uses no numerical cutoff. It does not itself contradict the 2-adic naturality condition. Its role is to strengthen the Archimedean side of the harmonic mixed-place exclusion target.
