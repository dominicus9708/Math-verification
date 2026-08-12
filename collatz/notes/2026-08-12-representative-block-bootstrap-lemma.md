# Representative-block bootstrap lemma for the recursively sufficient Cantor core

Date: 2026-08-12

Status: **exact set-theoretic bootstrap lemma**, conditional only on a finite representative family being recursive. It makes explicit the exponential compression between the number of ternary representatives that must be certified and the width of the ordinary integer interval inferred from recursive sufficiency. It does not supply an asymptotic proof that every representative family is recursive.

## 1. Recursively sufficient core

Use Ansari's recursively sufficient intersection

\[
F=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 m\ge0,\ a_i\in\{0,1\}
\right\}.
\]

Assume the ordinary Collatz conjecture has already been verified through

\[
\boxed{V_0=4\cdot3^{44}+2.}
\]

The first `F`-block above this floor is the `m=44` block.

## 2. Low-d representative family

For an integer

\[
0\le d<44,
\]

define

\[
\boxed{
A_d:=
\left\{
4\left(3^{44}+\sum_{i=0}^{d-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
}
\]

Its cardinality is exactly

\[
\boxed{|A_d|=2^d.}
\]

Any `F`-member in the `m=44` block that uses a selector of index at least `d` has selector sum at least `3^d`.

Therefore the first `F`-member after every element of `A_d` is

\[
\boxed{
N_{d,+}=4(3^{44}+3^d)+3.
}
\]

Equivalently,

\[
\boxed{
F\cap(V_0,N_{d,+})=A_d.
}
\]

## 3. Bootstrap lemma

### Lemma

If every member of `A_d` is recursive, then the Collatz conjecture is verified for every positive integer through

\[
\boxed{
V_d:=4(3^{44}+3^d)+2.
}
\]

### Proof

Since every member of `A_d` is recursive and `A_d subset F`, removing `A_d` from the recursively sufficient set `F` preserves recursive sufficiency.

But the resulting recursively sufficient set has no member in

\[
(V_0,V_d].
\]

Ansari's interval form of recursive sufficiency (Theorem 2.1 / Corollary 2.2) therefore extends the verified interval from `V_0` through `V_d`.

## 4. Compression factor

The ordinary interval increase is exactly

\[
\boxed{
V_d-V_0=4\cdot3^d.
}
\]

The number of representative starts whose recursiveness must be established is only

\[
2^d.
\]

Hence the interval-width / representative-count ratio is

\[
\boxed{
\mathcal C_d
:=
\frac{4\cdot3^d}{2^d}
=4\left(\frac32\right)^d.
}
\]

Thus

\[
\boxed{\mathcal C_d\to\infty}
\]

exponentially as `d` grows.

Equivalently, the fraction of ordinary integers represented explicitly is

\[
\boxed{
\mathcal C_d^{-1}
=\frac14\left(\frac23\right)^d
\to0.
}
\]

This is the exact quantitative form of the representative-set strategy: a vanishing fraction of specially structured starts can certify an entire contiguous interval, provided those representatives are proved recursive.

## 5. Relation to the intended set/proposition method

The logical form is

\[
\boxed{
A_d\text{ is recursive}
\Longrightarrow
F\setminus A_d\text{ remains recursively sufficient}
\Longrightarrow
(F\setminus A_d)\cap(V_0,V_d]=\varnothing
\Longrightarrow
[1,V_d]\text{ verified}.}
\]

No statement about the individual ordinary integers in the complement is needed.

This is a standard-mathematical realization of the intended formation/complement/static-aggregation viewpoint: describe the structurally relevant set, prove one property of that set, and infer the complement interval globally.

## 6. What remains difficult

The lemma makes the compression explicit but does not prove that `A_d` is recursive for arbitrary `d`.

Finite certificates currently establish this for substantial values of `d`; the global proof target is to replace those individual finite certificates by a uniform theorem controlling the representative family as `d` grows, or by a cross-place cylinder theorem that certifies whole subsets of `A_d` without trajectory enumeration.

## External input

The interval inference uses Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471--480 (2025), especially Definition 1.3, Lemma 1.1, Theorem 2.1, Corollaries 2.1--2.2, and Lemmas 3.1--3.2.
