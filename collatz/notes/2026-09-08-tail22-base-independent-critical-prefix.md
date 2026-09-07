# MATH-033 — base-independent critical prefix for exact 22-step coefficient survival

Date: 2026-09-08

Status:

`CONFIRMED / EXACT LOCAL DESCRIPTOR / COMPUTATIONAL ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Problem

MATH-031/032 used a 22-step descriptor anchored at base depth 61.  To reuse a 22-step block at arbitrary later base depth `K`, one would naively rebuild

\[
H_K(u)=\max_{1\le j\le22}
\left(q_{\rm pub}(K+j)-s_j(u)\right)
\]

for every residue `u mod 2^22` and every base `K`.

MATH-033 removes that base-dependent maximization.

## Frozen coefficient threshold

Let

\[
B=2^{71},\qquad A=3B+1,
\qquad c_0=A/B=3+2^{-71}.
\]

Define

\[
\beta=\frac{\log2}{\log c_0}.
\]

The published-floor threshold is

\[
q_{\rm pub}(k)=\min\{q:c_0^q>2^k\}.
\]

Because `A` is odd and greater than 1, equality

\[
c_0^q=2^k
\]

cannot occur for positive integers `q,k`. Hence

\[
\boxed{q_{\rm pub}(k)=\lceil\beta k\rceil}.
\]

## Critical-prefix descriptor

For one 22-step residue `u`, let `s_j(u)` be its cumulative added odd-count through local prefix `j`.

Choose the unique prefix

\[
\boxed{
j_*(u)=\arg\max_{1\le j\le22}
\bigl(\beta j-s_j(u)\bigr)
}
\]

and write

\[
s_*(u)=s_{j_*(u)}(u).
\]

Then for every base depth `K`,

\[
\boxed{
H_K(u)=q_{\rm pub}(K+j_*(u))-s_*(u)
}.
\]

### Proof

Since `j_*` maximizes the score, for every `j`,

\[
\beta(j_*-j)
\ge s_*-s_j=:m,
\qquad m\in\mathbb Z.
\]

Therefore

\[
\beta(K+j_*)
\ge\beta(K+j)+m.
\]

Taking ceilings and using integer translation of the ceiling function,

\[
\lceil\beta(K+j_*)\rceil
\ge
\lceil\beta(K+j)+m\rceil
=
\lceil\beta(K+j)\rceil+m.
\]

Thus

\[
q_{\rm pub}(K+j_*)-s_*
\ge
q_{\rm pub}(K+j)-s_j
\]

for every `j`, proving the formula.

## Exact critical-prefix comparison without floating point

To compare two scores

\[
\beta j_1-s_1
\quad\text{and}\quad
\beta j_2-s_2,
\]

let

\[
\Delta j=j_1-j_2,
\qquad
\Delta s=s_1-s_2.
\]

For positive `Delta j, Delta s`,

\[
\beta\Delta j>\Delta s
\]

is equivalent to

\[
2^{\Delta j}B^{\Delta s}>A^{\Delta s}.
\]

Thus `j_*` is computed by exact integer arithmetic; no floating-point logarithm is used in the certificate.

Equality for distinct prefixes would imply an odd positive power of `A` equals a power-of-two multiple of a power of `B`, which is impossible. Hence the critical prefix is unique.

## Exhaustive finite regression

The certificate constructs the critical prefix for every

\[
2^{22}=4,194,304
\]

residue and explicitly recomputes the full 22-prefix maximum at six separated base depths:

`K = 0, 61, 83, 127, 545, 1007`.

Total exact threshold equalities checked:

\[
\boxed{25,165,824}.
\]

All pass.

The critical-prefix histogram over all residues is also recorded by the certificate; the dominant critical prefix is `j=22` with `1,256,064` residues.

## DSD interpretation

The complete local descriptor for the threshold part of a 22-step block can now store only

\[
\boxed{(j_*,s_*)}
\]

instead of a separate `H_K` table for every base depth.

Together with the local total odd-count and exact affine-transition data, one residue descriptor can be reused at arbitrary base `K`.

This is a reduction of **calculation metadata**, not a global Collatz state quotient.

## Scope boundary

- The critical-prefix theorem is exact for the local coefficient-survival predicate.
- It does not say a `2^22` residue is a complete arbitrary-depth Collatz state.
- Endpoint propagation must remain exact.
- A fixed-width implementation may still overflow if a 22-step affine numerator is formed in one multiplication; later computation therefore uses two already-audited 11-step exact updates for endpoint arithmetic.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_tail22_base_independent_critical_prefix_certificate.cpp`

Certificate commit:

`1ab2f8c295895353de8012d609a55f77af6c68bc`
