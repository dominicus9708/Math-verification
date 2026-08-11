# Boundary lock versus strict-gap survivor branches

Date: 2026-08-11

Status: **exact periodic/aperiodic split in survival-ceiling coordinates**. It does not exclude nontrivial cycles; it isolates them as equality cases of the same boundary used for the nonperiodic hard core.

## 1. Contracting prefix ceiling

For an accelerated prefix write

\[
T^k(n)=a_k(n+c_k),
\]

and suppose

\[
0<a_k<1.
\]

The current endpoint survival ceiling is

\[
\boxed{
C_k:=\frac{a_kc_k}{1-a_k}.
}
\]

A start `n` survives this endpoint iff `n<=C_k`.

## 2. Exact ceiling-gap identity

From

\[
T^k(n)-n
=(a_k-1)n+a_kc_k,
\]

and

\[
a_kc_k=(1-a_k)C_k,
\]

we obtain

\[
\boxed{
T^k(n)-n
=(1-a_k)(C_k-n).
}
\]

Hence

\[
\boxed{
C_k-n
=\frac{T^k(n)-n}{1-a_k}.
}
\]

## 3. Integer quantization of the gap

Both `T^k(n)` and `n` are integers.

If the endpoint returns to the start,

\[
T^k(n)=n,
\]

then

\[
\boxed{C_k=n.}
\]

If the survivor has not returned,

\[
T^k(n)>n,
\]

then

\[
T^k(n)-n\ge1.
\]

Because

\[
0<1-a_k<1,
\]

we get

\[
\boxed{C_k-n>1.}
\]

Therefore a surviving contracting endpoint cannot have a ceiling in the open unit window just above the start:

\[
\boxed{
n<C_k\le n+1\quad\text{is impossible}.}
\]

More compactly,

\[
\boxed{
C_k=n
\quad\text{or}\quad
C_k>n+1.
}
\]

## 4. Boundary-lock interpretation of a cycle

If a positive nontrivial cycle has minimum element `n`, rotate the cycle so that the prefix begins at `n`. Every intermediate cycle state is at least `n`, and at the full period `K`,

\[
T^K(n)=n.
\]

The full-period affine coefficient must be contracting (`a_K<1`) because the positive affine correction compensates the multiplicative deficit. Hence

\[
\boxed{C_K=n.}
\]

Thus a periodic first-descent counterexample is an exact **boundary-lock state**: the survival ceiling meets the formation floor at equality and the state repeats.

## 5. Strict-gap interpretation of the nonperiodic hard core

For a nonperiodic first-descent survivor, no endpoint can equal the start. Hence every contracting checkpoint satisfies

\[
\boxed{C_k>n+1.}
\]

The earlier ceiling-stabilization argument strengthens this: along infinitely many contracting checkpoints of a nonperiodic survivor, the current ceilings must eventually leave every fixed finite interval.

Therefore the two counterexample modes are cleanly separated in the same boundary variable:

\[
\boxed{
\begin{array}{ll}
\text{periodic:}& C_K=n\text{ at some finite return prefix},\\
\text{aperiodic:}& C_k>n+1\text{ at every contracting prefix}.
\end{array}
}
\]

This split allows cycle-specific extremal word results to be used only on the equality branch, while harmonic-correction and sparse-return arguments remain confined to the nonperiodic branch.
