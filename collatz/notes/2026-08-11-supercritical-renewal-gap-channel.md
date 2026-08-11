# Supercritical renewal gap-channel normal form

Date: 2026-08-11

Status: **exact local arithmetic reformulation for a fixed aggregate-supercritical renewal-compatible word**. This replaces the shadow-distance variable by the actual integer floor gap.

## 1. Fixed word and affine data

Let a finite parity word `w` have accelerated length `A`, odd count `H`, correction numerator

\[
R=C(w),
\]

and assume it is aggregate-supercritical:

\[
\boxed{Z:=2^A-3^H>0.}
\]

Its affine map is

\[
F(x)=\frac{3^H x+R}{2^A}.
\]

The positive rational fixed point is

\[
\boxed{C=\frac{R}{Z}.}
\]

Let an integer start `N` realize the exact word, including endpoint oddness, and let

\[
N':=F(N),\qquad g:=N'-N.
\]

For a floor-increasing segment, `g>0`.

## 2. Exact gap formulas

From

\[
2^A N'=3^H N+R
\]

and `N'=N+g`, one obtains

\[
\boxed{R-ZN=2^A g.}
\]

Hence

\[
\boxed{N=\frac{R-2^A g}{Z}.}
\]

Using `2^A=3^H+Z`, equivalently

\[
\boxed{N'=\frac{R-3^H g}{Z}.}
\]

The rational-shadow distance is therefore

\[
\boxed{C-N=\frac{2^A}{Z}g,}
\]

and

\[
\boxed{C-N'=\frac{3^H}{Z}g.}
\]

Thus the earlier shadow-distance quantization is exactly the ordinary integer renewal gap in another normalization.

## 3. Exact gap residue class

The condition that `N` in the first boxed formula be an integer is

\[
R-2^A g\equiv0\pmod Z.
\]

Because

\[
\gcd(2^A,Z)=1,
\]

there is one exact residue class

\[
\boxed{g\equiv g_w:=R(2^A)^{-1}\pmod Z.}
\]

Thus the integer formation problem for the fixed word may be transferred from the start variable `N` to the gap variable `g`.

## 4. Translate the shadow window

For the fixed word, let `W(w)` be the finite renewal-compatible shadow-window width from the earlier theorem:

\[
0<C-N<W(w).
\]

Since

\[
g=(1-a)(C-N),
\qquad a=\frac{3^H}{2^A},
\]

define

\[
\boxed{G(w):=(1-a)W(w)=\frac{Z}{2^A}W(w).}
\]

Then the finite renewal-compatible condition is exactly

\[
\boxed{0<g<G(w).}
\]

Consequently the integer gap candidates for the fixed word are exactly

\[
\boxed{
\bigl(g_w+Z\mathbb Z\bigr)\cap(0,G(w))\cap\mathbb Z.
}
\]

This is the gap-channel normal form.

## 5. Relation to endpoint-odd quantization

Because both renewal endpoints are odd,

\[
\boxed{g\in2\mathbb Z.}
\]

Equivalently, writing `g=2t`,

\[
R-ZN=2^{A+1}t,
\]

so

\[
C-N=\frac{2^{A+1}}{Z}t.
\]

Thus the earlier positive shadow-distance ladder is precisely the even-gap lattice.

For genuine renewal floors, the first block is subcritical, so `N≡3 mod 4`; the same holds at the next renewal floor. Hence in the genuine renewal skeleton one further has

\[
\boxed{g\equiv0\pmod4.}
\]

## 6. Structural use

For residual economical supercritical words, `Z` is exponentially large in the exponent counts while `G(w)` is a finite dynamical width. If

\[
G(w)<Z,
\]

there is at most one positive representative of the gap residue class inside the renewal window. Therefore local integer renewal compatibility becomes the single separation test

\[
\boxed{g_w\ge G(w)}
\]

when `g_w` is chosen as the least positive residue.

This gap form is equivalent to the earlier residue-shadow-window formulation but is more directly compatible with:

- the exact floor gap `g=N'-N`;
- the block-count cost `g<m` for supercritical renewals;
- the renewal depth-transfer law via `v_2(g)`;
- the rational-cycle condition `Z|g`.

It is therefore the preferred local arithmetic coordinate for the remaining supercritical renewal analysis.
