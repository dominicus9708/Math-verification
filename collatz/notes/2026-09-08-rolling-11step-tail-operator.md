# MATH-025 — rolling 11-step tail operator

## Status

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`
- result: `CONFIRMED / EXACT LOCAL OPERATOR / COMPUTATIONAL ACCELERATION`

## Construction

Let the current shortcut depth be `K`, current odd-count be `q`, and current endpoint be `n`.
Write

\[
u=n\bmod 2^{11}.
\]

The next 11 shortcut parity bits depend only on `u`.  Let

\[
s_j(u)
\]

be the number of odd steps among the first `j` of those 11 steps, and let

\[
s(u)=s_{11}(u).
\]

For any threshold sequence `Q(k)`, define

\[
\boxed{H_K(u)=\max_{1\le j\le11}\bigl(Q(K+j)-s_j(u)\bigr)}.
\]

Then the next 11 coefficient gates are all satisfied exactly iff

\[
\boxed{q\ge H_K(u)}.
\]

For the exact endpoint transition, define `c(u)` by

\[
2^{11}T^{11}(u)=3^{s(u)}u+c(u).
\]

Because every integer congruent to `u mod 2^11` has the same 11-step parity word,

\[
\boxed{
T^{11}(n)=\frac{3^{s(u)}n+c(u)}{2^{11}}
}
\]

and

\[
\boxed{q'=q+s(u)}.
\]

Thus a full 11-step scalar continuation can be replaced by

1. one residue lookup `u=n mod 2048`;
2. one threshold lookup `q>=H_K(u)`;
3. if it survives, one exact affine update.

## Exact regression

The certificate exhausts all

\[
u=0,\dots,2047
\]

and all base depths

\[
K=0,\dots,1024.
\]

At every `(K,u)` it checks the threshold boundary cases around `H_K(u)`, giving

\[
\boxed{6,297,600}
\]

exact survival comparisons.

For every residue, six distinct lifts

\[
n=u+2^{11}t
\]

including a very large integer lift are directly iterated for 11 scalar steps and compared with the affine formula.  Every comparison passes.

The frozen floor

\[
(3+2^{-71})^q>2^k
\]

and the simpler threshold

\[
3^q\ge2^k
\]

are also checked to agree throughout the audited depth range.

## Relation to MATH-011

MATH-011 introduced `H(r)` specifically for the fixed `61+11` tail.

MATH-025 shows that the same object is a rolling operator at arbitrary base depth `K`:

\[
H(r)\longrightarrow H_K(u).
\]

This is a genuine computational reuse of the complete descriptor, not merely metadata.

## Scope warning

The operator is complete for **one 11-step continuation window** once `(K,q,n mod 2^11)` is known.

It is not a complete Collatz state, and it does not permit unrelated states to be merged across windows without preserving the exact endpoint needed by the next lookup.

## Reproduction

`collatz/src/2026_09_08_rolling_11step_tail_operator_certificate.cpp`
