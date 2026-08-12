# Exact low-28 recursive floor bootstrap inside `m=44`

Date: 2026-08-12

Status: **finite exact recursive-sufficiency bootstrap certificate**. All `2^28` representatives obtained by freeing the lowest 28 ternary selectors of the first unresolved `m=44` core fall below their own start. Recursive sufficiency therefore advances the contiguous verified floor by `4*3^28 = 91,507,169,819,844` ordinary integers. This is a finite computation over representatives, not a global Collatz proof.

## 1. Representative family

Define

\[
A_{28}=
\left\{
4\left(3^{44}+\sum_{i=0}^{27}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
\]

Then

\[
\boxed{|A_{28}|=2^{28}=268,435,456.}
\]

Every member of the recursively sufficient Cantor core `F` after the old floor

\[
V_0=4\cdot3^{44}+2
\]

and before the first selector with `a_28=1` lies in `A_28`.

The next `F` member is

\[
N_{\rm next}=4(3^{44}+3^{28})+3.
\]

## 2. Exact trajectory certificate

Use the accelerated time-expanded map

\[
T(n)=
\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even}.
\end{cases}
\]

The exact parallel verifier computes

\[
\tau_<(N)=\min\{k\ge1:T^k(N)<N\}
\]

for every `N in A_28`.

It finds no failure and no 128-bit overflow. The exact maximum is

\[
\boxed{
\max_{N\in A_{28}}\tau_<(N)=425.
}
\]

One maximizing selector mask is

\[
\boxed{140,506,676,}
\]

with selector sum

\[
\boxed{S=7,662,208,534,542}
\]

and start

\[
\boxed{
N_*=3,939,083,639,383,279,069,695.
}
\]

An independent Wolfram exact-integer check gives

\[
T^{424}(N_*)\ge N_*,
\]

and

\[
\boxed{
T^{425}(N_*)
=3,358,484,204,253,692,110,597
<N_*.
}
\]

The C++ verifier additionally records the largest intermediate value seen over the entire representative scan as

\[
717,534,341,070,688,542,936,683,819,636,
\]

and explicitly checks before every odd step that `3n+1` fits in unsigned 128-bit arithmetic.

## 3. Verified-floor jump

Every member of `A_28` is recursive. Hence the recursively sufficient set may be refined by deleting `A_28`, and there is no retained core member before `N_next`.

Therefore the contiguous verified floor becomes

\[
\boxed{
V_{28}
=4(3^{44}+3^{28})+2
=3,939,083,700,241,614,751,370.
}
\]

The exact increase over `V_0` is

\[
\boxed{
V_{28}-V_0
=4\cdot3^{28}
=91,507,169,819,844.
}
\]

The interval-width / representative-count ratio is

\[
\boxed{
\frac{4\cdot3^{28}}{2^{28}}
\approx340,890.77.
}
\]

Thus one representative check corresponds to more than `340,000` ordinary integer starts on average in the interval inference.

## 4. Role in the proof program

This is a significant computational bootstrap but still not the desired terminal theorem: the representative count itself is `2^28`.

The next reduction therefore applies the cross-place cylinder/static-aggregation sieve **inside `A_28` before trajectory evaluation**. At small binary resolution, whole dyadic residue classes can be certified recursive by one affine inequality, so only their complement needs any deeper deterministic trajectory analysis.

This creates a two-stage proof architecture:

\[
\boxed{
\text{class-level proposition pruning}
\to
\text{small representative fringe}
\to
\text{recursive-sufficiency interval jump}.}
\]

## 5. Reproducibility

Exact verifier:

`collatz/src/m44_low28_recursive_bootstrap.cpp`

It uses OpenMP for parallelism and exact unsigned 128-bit arithmetic with an explicit overflow guard.

## External input

The interval implication uses Ansari's recursive-sufficiency framework: Definition 1.3, Lemma 1.1, Theorem 2.1, Corollaries 2.1--2.2, and Lemmas 3.1--3.2 in *Recursive sufficiency for the Collatz conjecture and computational verification* (2025).
