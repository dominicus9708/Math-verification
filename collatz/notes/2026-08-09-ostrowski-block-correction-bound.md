# Ostrowski-block correction bound for first-crossing resonances

Date: 2026-08-09

Status: **DERIVED COROLLARY OF DENJOY–KOKSMA + FINITE RESONANCE CHECKS**

This note extends the convergent-denominator Denjoy–Koksma refinement to integers that are short sums of continued-fraction denominator blocks. It is an external irrational-rotation estimate applied to the project’s mechanical correction channel; it is not a Collatz proof.

## 1. Rotation observable

As in `denjoy-koksma-resonance-refinement.md`, let

\[
\alpha=\log_2 3,
\qquad
f(x)=\frac13 2^{-x}\quad(0\le x<1),
\]

periodically extended to the circle. Then

\[
S^*(N)=\sum_{i=0}^{N-1}f(\{i\alpha\}),
\]

\[
\int f=\frac1{6\ln2},
\qquad
\operatorname{Var}(f)=\frac13.
\]

For every continued-fraction denominator `q_j` of `alpha`, Denjoy–Koksma holds from every starting phase `x`:

\[
\left|
\sum_{i=0}^{q_j-1}f(x+i\alpha)-q_j\int f
\right|
\le\frac13.
\]

## 2. Block decomposition lemma

Suppose an integer `N` is represented as

\[
N=\sum_j b_jq_j,
\qquad b_j\in\mathbb N_0.
\]

Split the orbit segment of length `N` consecutively into `b_j` blocks of length `q_j`. The starting phase of each block is arbitrary, but Denjoy–Koksma is uniform in that phase. Therefore triangle inequality gives

\[
\boxed{
\left|S^*(N)-\frac{N}{6\ln2}\right|
\le\frac13\sum_j b_j.
}
\]

In particular,

\[
\boxed{
S^*(N)
\le
\frac{N}{6\ln2}
+rac13\|b\|_1.
}
\]

Choosing the canonical Ostrowski expansion gives a natural small block-digit sum for computation, but the inequality itself only needs a valid nonnegative denominator-block decomposition.

## 3. First upper semiconvergent resonance

The relevant neighboring denominators of `log_2 3` include

\[
q_{n-1}=6,586,818,670,
\qquad
q_n=65,470,613,321.
\]

The previously studied upper resonance has

\[
\boxed{
72,057,431,991
=65,470,613,321+6,586,818,670.
}
\]

Thus `||b||_1=2` and

\[
\boxed{
S^*(72,057,431,991)
\le
\frac{72,057,431,991}{6\ln2}+\frac23.
}
\]

At

\[
\sigma=114,208,327,604,
\qquad
\delta=2^\sigma/3^q-1
\approx5.5108900957847576\times10^{-12},
\]

this gives

\[
\boxed{
x<3.1439839417872312\times10^{21}.}
\]

The earlier all-q pair bound gave about

\[
3.8136763085680545\times10^{21}.
\]

Both lie below the recursively sufficient verified lower interval already used to eliminate this resonance; the block-DK value simply strengthens the finite margin.

## 4. Next upper convergent resonance

For

\[
q=137,528,045,312,
\]

the Ostrowski digit sum is one because q itself is a convergent denominator. The block formula reduces to

\[
S^*(q)\le q/(6\ln2)+1/3,
\]

reproducing the bound

\[
x<3.6797780659000120\times10^{22}<2^{75}.
\]

## 5. Relation to observed resonance structure

Recent parity-vector work reports that known paradoxical `(j,q)` ratios cluster at continued-fraction convergents, semiconvergents, and nearby Stern–Brocot mediants of `log_3 2`. The present block estimate is structurally matched to exactly those Diophantine configurations: convergents have one denominator block, and simple semiconvergents/mediants have small block digit sums.

This does not prove that all future dangerous Collatz pairs have small Ostrowski digit sum. It only supplies a deterministic correction majorant once such a decomposition is known.

## 6. Proof-program role

The elementary pair bound remains the uniform all-q fallback. The hierarchy is now:

1. all q: `S^*(q) <= (7q+1)/24`;
2. convergent denominator q: `S^*(q) <= q/(6 ln 2)+1/3`;
3. short denominator-block decomposition: `S^*(q) <= q/(6 ln 2)+(1/3)||b||_1`.

The improvement affects constants and finite bit windows; by itself it does not improve the exponent coming from the linear-form lower bound on the resonance gap.