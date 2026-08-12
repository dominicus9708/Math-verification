# R2 critical Beatty skew-product formulation

Date: 2026-08-12

Status: **exact one-dimensional coding of the coefficient-survival terminal branch**. This removes the valuation variables from R2 and isolates the remaining global positive-integer naturalness problem.

## 1. Critical driver

Put

\[
\gamma:=\log_2 3.
\]

Define the critical Beatty event positions

\[
A_i^*:=\lfloor i\gamma\rfloor
\]

and the deterministic increment word

\[
\boxed{r_i:=A_{i+1}^*-A_i^*.}
\]

Because `1<gamma<2`,

\[
\boxed{r_i\in\{1,2\}.}
\]

The binary word `r_i-1` is the characteristic Sturmian/Beatty coding of the irrational rotation with slope `gamma-1`.

## 2. R2 displacement

For an R2 odd-event tail write

\[
A_i:=\sum_{j<i}v_j,
\qquad
s_i:=A_i^*-A_i.
\]

Coefficient survival at every odd-event checkpoint is equivalent to

\[
\boxed{s_i\ge0.}
\]

The exact transition is

\[
\begin{aligned}
s_{i+1}-s_i
&=(A_{i+1}^*-A_i^*)-(A_{i+1}-A_i)\\
&=r_i-v_i.
\end{aligned}
\]

Hence

\[
\boxed{v_i=s_i+r_i-s_{i+1}.}
\]

## 3. Eliminate the valuation variables

The only local condition on an odd-event valuation is

\[
v_i\ge1.
\]

Using the exact formula above,

\[
v_i\ge1
\iff
s_{i+1}\le s_i+r_i-1.
\]

Together with coefficient survival at the next checkpoint,

\[
s_{i+1}\ge0,
\]

we obtain the complete local R2 transition rule

\[
\boxed{
0\le s_{i+1}\le s_i+r_i-1.
}
\]

Explicitly:

### If `r_i=1`

\[
\boxed{0\le s_{i+1}\le s_i.}
\]

The displacement cannot increase.

### If `r_i=2`

\[
\boxed{0\le s_{i+1}\le s_i+1.}
\]

The displacement may increase by at most one.

Thus R2 is a one-dimensional nonnegative integer walk driven by a fixed Sturmian word.

## 4. Converse: every finite skew path is locally realizable

Conversely, suppose a finite integer sequence

\[
s_0=0,s_1,\ldots,s_q
\]

satisfies

\[
0\le s_{i+1}\le s_i+r_i-1
\]

for every `i<q`.

Define

\[
\boxed{v_i:=s_i+r_i-s_{i+1}.}
\]

Then every `v_i` is a positive integer. The cumulative event positions are

\[
A_i=A_i^*-s_i,
\]

and the resulting finite odd-event valuation code is an ordinary admissible Collatz/Syracuse code. By the standard 2-adic parity/valuation formation theorem it determines one exact residue class of positive starts modulo the corresponding power of two.

Therefore:

\[
\boxed{
\text{there is no additional finite local arithmetic obstruction in R2.}
}
\]

Any successful exclusion theorem must be genuinely infinite/global.

## 5. Harmonic cost in skew coordinates

The correction is

\[
\boxed{
c_q
=\frac13\sum_{i=0}^{q-1}
2^{-\{i\gamma\}}2^{-s_i}.}
\]

Hence a positive-integer nonperiodic first-descent survivor in R2 must satisfy

\[
\boxed{
\sum_{i<q}2^{-s_i}=O_N(q^{1/9}).
}
\]

Equivalently, its skew path must escape to large displacement in event density one.

Jensen gives the displacement-area requirement

\[
\boxed{
\sum_{i<q}s_i
\ge
\frac89q\log_2 q-O_N(q).
}
\]

## 6. Critical-density recurrence

The coefficient logarithm is

\[
q\gamma-A_q
=\{q\gamma\}+s_q.
\]

The known rational-2-adic critical-density necessity for a noncyclic trajectory is compatible with R2 only if

\[
\boxed{
\liminf_{q\to\infty}\frac{s_q}{q}=0.
}
\]

Thus the skew path must simultaneously:

- have large displacement for density-one indices;
- have superlinear accumulated area `Omega(q log q)`;
- yet return to sublinear height along an infinite subsequence.

These purely combinatorial conditions are consistent; they do not close R2.

## 7. Exact 2-adic naturalness map

For a skew path define

\[
A_i=\lfloor i\gamma\rfloor-s_i.
\]

Its Bernstein inverse/starting value is

\[
\boxed{
\Phi(s)
:=-\sum_{i=0}^{\infty}
\frac{2^{\lfloor i\gamma\rfloor-s_i}}{3^{i+1}}
\quad\in\mathbb Z_2.
}
\]

The series converges 2-adically because `A_i -> infinity` for any genuine infinite odd-event code.

A coefficient-survival counterexample in the positive ordinary integers would therefore be exactly an admissible skew path satisfying

\[
\boxed{
\Phi(s)=N\in\mathbb N,
}
\]

together with the harmonic/critical-density conditions above.

## 8. Exact R2 terminal theorem target

The whole R2 terminal branch is now equivalent to the following exclusion problem.

### Critical Beatty Skew Naturalness Exclusion

Prove that there is no infinite integer path `s=(s_i)` such that

\[
\boxed{s_0=0,}
\]

\[
\boxed{0\le s_{i+1}\le s_i+r_i-1,}
\]

\[
\boxed{
\sum_{i<q}2^{-s_i}=O(q^{1/9}),
}
\]

\[
\boxed{
\liminf s_i/i=0,
}
\]

and

\[
\boxed{
\Phi(s)\in\mathbb N_{>1}.
}
\]

Any theorem proving this statement eliminates R2 completely.

## 9. Architectural consequence

This formulation clarifies why finite congruence audits cannot settle R2:

- every finite skew prefix is locally realizable;
- local survival is already encoded by the one-dimensional inequality;
- the only missing condition is that the infinite 2-adic limit be one fixed positive ordinary integer.

Thus R2 is now an explicit **Sturmian-driven 2-adic naturalness problem**, rather than an open-ended Collatz trajectory search.