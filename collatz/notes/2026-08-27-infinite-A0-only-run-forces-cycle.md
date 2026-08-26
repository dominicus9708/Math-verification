# Infinite A0-only return language forces periodicity

Date: 2026-08-27

Status: **SAFE STRUCTURAL LEMMA.** This is a branch classification, not an exclusion of all nontrivial Collatz cycles and not a proof of the Collatz conjecture.

## 1. Setup

Let

\[
(A_0,Q_0)=(114208327604,72057431991)
\]

be the repaired promoted lower resonance, and put

\[
C_A:=\frac{3^{Q_0}}{2^{A_0}}<1.
\]

Consider a future orbit of a hypothetical minimal counterexample `N` and a sequence of block endpoints

\[
X_0,X_1,X_2,\ldots,
\qquad X_n\ge N,
\]

such that for every `n`, the segment from `X_n` to `X_{n+1}` has its first coefficient crossing exactly at `A0/Q0`.

For the `n`-th block write its normalized affine correction as `S_n`.  Then

\[
\boxed{
X_{n+1}=C_A(X_n+S_n).
}
\]

## 2. Uniform correction ceiling

The first-crossing mechanical-envelope theorem is word-independent at fixed `(A0,Q0)`:

\[
0\le S_n\le S_A
\]

for every such block, where `S_A` is the normalized correction of the unique mechanical first-crossing word.

Hence

\[
\boxed{
X_{n+1}\le C_A X_n+C_A S_A.
}
\]

Define the finite affine fixed ceiling

\[
\boxed{
P_A:=\frac{C_A S_A}{1-C_A}.
}
\]

Then

\[
C_A P_A+C_A S_A=P_A.
\]

## 3. All A0 endpoints lie in one finite interval

Set

\[
M:=\max\{X_0,P_A\}.
\]

If `X_n<=M`, then

\[
X_{n+1}
\le C_A M+C_A S_A
=C_A M+(1-C_A)P_A
\le M.
\]

Therefore by induction

\[
\boxed{
N\le X_n\le M
\qquad\text{for all }n.
}
\]

The endpoints are ordinary integers, so the set

\[
[N,M]\cap\mathbb Z
\]

is finite.

## 4. Infinite A0-only repetition therefore forces a cycle

If the `A0`-only endpoint sequence were infinite, two endpoints would coincide:

\[
X_i=X_j
\qquad(i<j).
\]

But the deterministic Collatz map then gives

\[
T^{(j-i)A_0}(X_i)=X_i.
\]

Thus the orbit segment between them is periodic.

Since all current global candidates satisfy `N>2^71>2`, this cannot be the trivial `1,2` cycle.

Hence

\[
\boxed{
\text{an infinite consecutive A0-only return language forces a nontrivial positive Collatz cycle.}
}
\]

Equivalently,

\[
\boxed{
\text{a divergent counterexample cannot remain forever in the A0-only transition state.}
}
\]

## 5. What this closes

This removes one apparent escape mode from the finite-resonance branch.

A hypothetical **divergent** counterexample that has reached the promoted `A0` scale must eventually do at least one of the following:

1. use an activated lower resonance such as `mJ0`;
2. coefficient-survive through `A0` and enter a later/infinite-survivor scale;
3. leave the current two-resonance language in some other explicitly identified later crossing.

It cannot avoid all three merely by repeating first crossings at `A0` forever.

## 6. What remains open

This lemma does **not** eliminate the periodic alternative.

An infinite `A0`-only path is converted into a nontrivial-cycle problem, not into an immediate contradiction.  Existing external cycle lower bounds eliminate some short cycle structures but do not by themselves exclude an arbitrary period containing many `A0` blocks.

Therefore the proof program now has a clean separation:

\[
\boxed{
\text{A0-only infinite branch}
\Longrightarrow
\text{cycle branch},
}
\]

while

\[
\boxed{
\text{divergent branch}
\Longrightarrow
\text{eventual activated-resonance or later-survivor escape}.
}
\]

This distinction should be maintained in all subsequent audits.
