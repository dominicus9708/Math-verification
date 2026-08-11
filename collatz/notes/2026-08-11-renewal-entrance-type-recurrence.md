# Renewal entrance-type recurrence cost theorem

Date: 2026-08-11

Status: **exact formation-class theorem for renewal-floor first blocks + persistent-window consequence**.

## 1. Renewal entrance type

Every renewal floor begins with a subcritical maximal block. Write its exact first-block type as

\[
\boxed{e(N):=(h,d),}
\]

where

\[
N=2^hK-1,
\qquad K\text{ odd},
\]

and

\[
\boxed{d=v_2(3^hK-1)\ge1.}
\]

The renewal-floor theorem gives

\[
\boxed{d<\alpha h,\qquad\alpha=\log_2(3/2).}
\]

## 2. Exact residue class of one entrance type

The exact valuation condition `v_2(3^hK-1)=d` is equivalent to

\[
3^hK-1\equiv2^d\pmod{2^{d+1}},
\]

hence

\[
\boxed{
K\equiv3^{-h}(1+2^d)
\pmod{2^{d+1}}.
}
\]

Substituting `N=2^hK-1` shows that every renewal floor with entrance type `(h,d)` lies in one exact residue class modulo

\[
\boxed{2^{h+d+1}.}
\]

Explicitly, if

\[
k_{h,d}:=3^{-h}(1+2^d)\bmod2^{d+1},
\]

then

\[
\boxed{
N\equiv2^h k_{h,d}-1
\pmod{2^{h+d+1}}.
}
\]

## 3. Recurrence of the same entrance type forces a large floor jump

Let two renewal floors `N<N'` have the same first-block type `(h,d)`. Their difference is a positive multiple of the common formation modulus:

\[
\boxed{
2^{h+d+1}\mid(N'-N).
}
\]

Therefore

\[
\boxed{
N'-N\ge2^{h+d+1}.
}
\]

This strictly strengthens the depth-only recovery cost `2^h`.

### Examples

For the base depth `h=2`, subcriticality forces `d=1`. The exact class is

\[
\boxed{N\equiv11\pmod{16}.}
\]

Thus any two depth-2 renewal floors differ by at least `16`.

For `h=3`, subcriticality again forces `d=1`, yielding

\[
\boxed{N\equiv7\pmod{32}.}
\]

## 4. Persistent discrepancy/time cost of entrance-type recurrence

Consider a renewal window beginning at a floor `N` of type `(h,d)` and ending at a later floor `N'` of the same type. Let `Q` be the odd-event count and `S` the cumulative coefficient discrepancy across the whole window.

The persistent product identity gives

\[
2^S\frac{N'}N
\le
\left(1+\frac1{3N}\right)^Q.
\]

Using

\[
\frac{N'}N
\ge
1+\frac{2^{h+d+1}}N,
\]

we obtain

\[
\boxed{
S
\le
Q\log_2\left(1+\frac1{3N}\right)
-
\log_2\left(1+\frac{2^{h+d+1}}N\right).
}
\]

Hence if `S>=0`,

\[
\boxed{
Q
\ge
\frac{
\log(1+2^{h+d+1}/N)
}{
\log(1+1/(3N))
}.
}
\]

For a large odd core `K=(N+1)/2^h`, this threshold is asymptotic to

\[
\boxed{Q\sim3\cdot2^hK\,\log\left(1+\frac{2^{d+1}}K\right),}
\]

and in the regime `K >> 2^{d+1}` it is asymptotic to

\[
\boxed{3\cdot2^{h+d+1}.}
\]

Thus recurrence of a high-resolution entrance type is exponentially expensive in event time unless the window pays negative cumulative discrepancy.

## 5. Structural dichotomy

An infinite aperiodic renewal chain therefore has two ways to avoid repeatedly paying the same large dyadic entrance modulus:

1. keep changing its exact entrance types `(h,d)` indefinitely; or
2. revisit entrance types, paying either a large floor jump/event-time budget or negative persistent coefficient discrepancy.

Since `d<alpha h`, bounded `h` implies only finitely many possible entrance types. In that regime at least one type must recur infinitely often, making the recurrence-cost theorem unavoidable.

The unbounded-`h` regime instead forces increasingly fine entrance formation moduli.
