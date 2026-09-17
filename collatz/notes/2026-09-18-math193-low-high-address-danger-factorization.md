# MATH-193 — low/high factorization of singleton danger

Date: 2026-09-18

Status: `EXACT STRUCTURAL LEMMA / MODULAR DANGER FACTORIZATION / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-192 reduces singleton overshoot to one full `L`-bit residue

\[
r_L=((C-B)3^{-Q})\bmod 2^L.
\]

MATH-090 instead solves the same compatibility in two stages: first at the source-resolution scale `R`, then through `z=L-R` additional lift bits.

The two descriptions combine exactly and split the dangerous singleton condition into an independent low-address condition and a zero high-word condition.

No paid layer or first-cell closure is claimed.

## 2. Low-resolution residue and carry

Let

\[
D:=C-B,
\qquad
L=R+z,
\qquad z>0.
\]

Define

\[
\boxed{
r_R:=D3^{-Q}\bmod2^R,
\qquad0\le r_R<2^R,
}
\]

and the exact integer carry

\[
\boxed{
C_R:=\frac{D-3^Qr_R}{2^R}.
}
\]

Then

\[
D=3^Qr_R+2^RC_R.
\]

## 3. Exact low/high decomposition of the full residue

Write the full solution as

\[
r_L=r_R+2^Rt,
\qquad0\le t<2^z.
\]

The congruence

\[
D\equiv3^Qr_L\pmod{2^{R+z}}
\]

is equivalent to

\[
C_R\equiv3^Qt\pmod{2^z}.
\]

Hence

\[
\boxed{
t=(C_R3^{-Q})\bmod2^z}
\]

and therefore

\[
\boxed{
r_L
=r_R+2^R\bigl((C_R3^{-Q})\bmod2^z\bigr).
}
\]

This is an exact identity, not a bound.

## 4. Overshoot compatibility forces the high word to vanish

Because the parent source multiplicity satisfies

\[
M\le2^R,
\]

an overshoot-compatible source requires

\[
r_L<M\le2^R.
\]

But the decomposition above has `r_R<2^R` and `t>=0`. Thus

\[
r_L<M
\]

can occur only when

\[
\boxed{t=0.}
\]

Equivalently,

\[
\boxed{C_R3^{-Q}\equiv0\pmod{2^z}.}
\]

Since `3^{-Q}` is odd, this is equivalent to

\[
\boxed{\nu_2(C_R)\ge z.}
\]

In this compatible overshoot case,

\[
\boxed{r_L=r_R.}
\]

Thus MATH-090 and MATH-192 are exactly the same terminal compatibility test in two coordinate systems.

## 5. Exact danger factorization

MATH-192 says that a compatible singleton can be non-descending only if

\[
0\le r_L\le \min(M-1,r_{\rm bad}).
\]

Using `r_L=r_R` for every compatible overshoot, the full dangerous condition is exactly

\[
\boxed{
\begin{aligned}
&r_R<M,\\
&r_R\le r_{\rm bad},\\
&\nu_2(C_R)\ge z.
\end{aligned}
}
\]

Equivalently, with

\[
T:=\min(M-1,r_{\rm bad}),
\]

the danger corridor is

\[
\boxed{
(r_R,\; (C_R3^{-Q})\bmod2^z)
\in
[0,T]\times\{0\}.
}
\]

This is the desired DSD factorization:

- the low `R` bits decide whether the unique source lies inside the master-defect bad prefix;
- the high `z` bits decide whether the low-resolution source survives the overshoot at all.

The two roles must not be conflated or double-counted.

## 6. Relation to the transported carry

MATH-091 defines the exact macro-composition carry

\[
d=\frac{B+3^Qr_L-C}{2^L}.
\]

For a compatible overshoot, `r_L=r_R` and

\[
D-3^Qr_R=2^RC_R.
\]

Therefore

\[
\boxed{
d=-\frac{C_R}{2^z}.}
\]

So the `z` zero lift bits do not destroy the carry. They divide out exactly the forced power of two and transport the remaining signed integer carry into the next affine intercept.

This gives a natural split:

### Zero-carry resonance

\[
C_R=0
\iff d=0.
\]

Then

\[
D=3^Qr_R
\]

as an ordinary integer equality, not only a congruence.

### Nonzero transported carry

\[
C_R\ne0,
\qquad
\nu_2(C_R)\ge z
\]

implies

\[
\boxed{d\in\mathbb Z\setminus\{0\}.}
\]

The nonzero quotient carry is retained in the next MATH-091 child state.

## 7. Normalized 2-adic form

Let

\[
G=3^{-Q}\in\mathbb Z_2.
\]

Define the normalized carry

\[
\chi_R:=GC_R.
\]

Because `G` is odd,

\[
\nu_2(\chi_R)=\nu_2(C_R).
\]

The residue decomposition becomes

\[
\boxed{
r_L=r_R+2^R(\chi_R\bmod2^z).}
\]

Hence danger means

\[
\boxed{
r_R\in[0,T],\qquad \chi_R\equiv0\pmod{2^z}.}
\]

This is expressible entirely in the finite-precision address state of MATH-096.

## 8. Consequence for the non-enumerative proof program

The remaining singleton theorem no longer needs to range over ordinary source anchors.

It is enough to prove that every legal synchronized product state satisfies at least one of

\[
\boxed{r_R\ge M,}
\]

\[
\boxed{r_R>r_{\rm bad},}
\]

or

\[
\boxed{\nu_2(C_R)<z.}
\]

The last alternative is pure carry incompatibility; the first two are pure low-resolution address/master-defect conditions.

Thus the desired modular-avoidance theorem has been sharpened to exclusion of one rectangular corridor in finite address/carry coordinates.

## 9. Claim boundary

Established:

- exact decomposition of `r_L` into low residue plus high carry word;
- exact equivalence of MATH-090 carry lifting and MATH-192 singleton residue compatibility;
- exact danger criterion `r_R<M`, `r_R<=r_bad`, `nu_2(C_R)>=z`;
- exact transported-carry identity `d=-C_R/2^z`;
- zero-carry / nonzero-carry split.

Not established:

- exclusion of the danger corridor for every legal synchronized product state;
- closure of all nonzero transported-carry paths;
- closure of zero-carry aperiodic paths;
- any new paid-count layer closure;
- first-cell emptiness;
- the Collatz conjecture.
