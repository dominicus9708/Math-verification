# Exact event-code formation bit and mixed-place unit bridge

Date: 2026-08-11

Status: **exact correction/refinement**. The coarser congruence modulo `2^{A_q}` remains valid, but a completed odd-to-odd exponent code requires one additional parity bit, equivalently exact 2-adic valuation `A_q`.

## 1. Completed odd-event code

Let

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}},
\qquad
v_i=v_2(3x_i+1)\ge1,
\]

and set

\[
A_0=0,
\qquad
A_q=\sum_{i=0}^{q-1}v_i.
\]

Repeated substitution gives

\[
\boxed{
2^{A_q}x_q
=3^q n+B_q,
}
\]

where

\[
\boxed{
B_q
=\sum_{i=0}^{q-1}3^{q-1-i}2^{A_i}.
}
\]

Define

\[
\boxed{c_q:=\frac{B_q}{3^q}}
=\sum_{i=0}^{q-1}\frac{2^{A_i}}{3^{i+1}}.
\]

Then

\[
\boxed{
n+c_q
=\frac{2^{A_q}x_q}{3^q}.}
\]

---

## 2. Coarse versus exact formation congruence

The coarse prefix divisibility condition is

\[
3^q n+B_q\equiv0\pmod{2^{A_q}},
\]

or equivalently

\[
\boxed{n+c_q\equiv0\pmod{2^{A_q}}.}
\]

This records the parity prefix through the divisions represented by `A_q`, but by itself does not certify that the completed endpoint `x_q` is odd.

Since a completed odd-event code requires `x_q` odd, the exact identity

\[
3^q n+B_q=2^{A_q}x_q
\]

implies

\[
3^q n+B_q
\equiv
2^{A_q}
\pmod{2^{A_q+1}}.
\]

Because `3^q` is odd, multiplication by its inverse modulo `2^{A_q+1}` preserves the unique high bit `2^{A_q}`, and therefore

\[
\boxed{
n+c_q
\equiv
2^{A_q}
\pmod{2^{A_q+1}}.}
\]

Equivalently,

\[
\boxed{v_2(n+c_q)=A_q.}
\]

Thus the exact starting residue of a completed exponent code is one residue class modulo `2^{A_q+1}`, not merely the coarser divisibility class modulo `2^{A_q}`.

In integer-correction notation this can be written

\[
\boxed{
n
\equiv
2^{A_q}-3^{-q}B_q
\pmod{2^{A_q+1}}.}
\]

---

## 3. Mixed-place unit identity

Divide the exact error by its complete power of two:

\[
\boxed{
E_q
:=
\frac{n+c_q}{2^{A_q}}
=
\frac{x_q}{3^q}.
}
\]

Because `x_q` and `3^q` are odd,

\[
\boxed{v_2(E_q)=0.}
\]

For `q>=1`, the next odd state is never divisible by three, since

\[
2^{v_{q-1}}x_q=3x_{q-1}+1\equiv1\pmod3.
\]

Hence

\[
\boxed{v_3(E_q)=-q\qquad(q>=1).}
\]

Thus the normalized error is simultaneously:

- the leading odd 2-adic unit after the exact approximation `-c_q -> n`;
- the real normalized endpoint `x_q/3^q`;
- a rational with exact 3-adic valuation `-q`.

This is an exact three-place bridge, not a probabilistic diagnostic.

---

## 4. Real window under no first descent

For a no-first-descent orbit,

\[
x_q\ge n.
\]

Also each event has `v_i>=1`, so

\[
x_{i+1}+1
\le
\frac32(x_i+1),
\]

and hence

\[
x_q+1\le(n+1)\left(\frac32\right)^q.
\]

Therefore

\[
\boxed{
\frac{n}{3^q}
\le
E_q
<
\frac{n+1}{2^q}.
}
\]

So a hypothetical positive-integer survivor requires a sequence of rational units `E_q` whose real size decays exponentially, whose 2-adic valuation stays exactly zero after factoring the complete formation precision, and whose 3-adic valuation is exactly `-q`.

This condition alone is not contradictory: the numerator `x_q` carries the remaining prime factors. It is recorded as an exact mixed-place attribute for subsequent filtering.

---

## 5. Relation to the earlier 2-adic limit

Since

\[
v_2(n+c_q)=A_q\to\infty,
\]

we recover

\[
\boxed{-c_q\to n\quad\text{in }\mathbb Z_2.}
\]

The new point is that the approximation order is exact, not merely at least `A_q`, and its normalized leading unit is precisely the normalized odd endpoint.
