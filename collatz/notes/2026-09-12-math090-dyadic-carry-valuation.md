# MATH-090 — dyadic carry-valuation form of one-paid compatibility

Date: 2026-09-12

Status: `EXACT LOCAL LEMMA / HENSEL-CARRY FORM OF ADDRESS COMPATIBILITY`

## 1. Setup

For an exact parent family

\[
Y'=B+3^Q s,
\qquad 0\le s<M,
\]

and a next macro source cylinder requiring

\[
Y'\equiv A_e\pmod{2^h},
\]

the source parameter satisfies

\[
3^Q s\equiv D\pmod{2^h},
\qquad D=A_e-B.
\]

Let

\[
R=\lceil\log_2M\rceil.
\]

## 2. Low-resolution solution

First solve only modulo `2^R`:

\[
\boxed{
r_R\equiv D(3^Q)^{-1}\pmod{2^R},
\qquad0\le r_R<2^R.
}
\]

If

\[
r_R\ge M,
\]

there is no source member in the parent family and the edge is excluded immediately.

## 3. Carry

Assume `r_R<M` and define

\[
\boxed{
C_R=rac{D-3^Qr_R}{2^R}\in\mathbb Z.
}
\]

When lifting the congruence one bit, write

\[
r_{j+1}=r_j+\varepsilon_j2^j.
\]

Because `3^Q` is odd,

\[
\boxed{\varepsilon_j\equiv C_j\pmod2.}
\]

If the lift bit is required to remain zero, then `C_j` must be even and

\[
C_{j+1}=C_j/2.
\]

Therefore preserving the same low-R source parameter through

\[
z=h-R
\]

additional zero lift bits is equivalent to

\[
\boxed{\nu_2(C_R)\ge z.}
\]

Hence for `h>R` exact compatibility is

\[
\boxed{
r_R<M
\quad\text{and}\quad
\nu_2(C_R)\ge h-R.
}
\]

## 4. Connection with MATH-089

MATH-089 identified

\[
z=h-R
\]

as both the terminal Bellman overshoot and the number of required zero-extension address bits.
MATH-090 rewrites the latter as one valuation condition:

\[
\boxed{z\le\nu_2(C_R).}
\]

Thus an actual locally dangerous one-paid terminal must satisfy

\[
\boxed{
r_R<M,
\qquad
z\le\nu_2(C_R),
\qquad
c\Omega_{out}<\lambda z.
}
\]

This is the current compact phase-address danger criterion.

## 5. Relation to the depth-41 bounded-carry calculation

The depth-41 fixed-`d` Hensel calculation also compresses candidate comparison into an integer carry whose divisibility/lift behavior determines whether a Hensel translation survives.

MATH-090 does **not** claim the two carry variables are numerically identical.  Their roles differ:

- depth-41 carry: dominance/translation witness;
- MATH-090 carry: same-integer macro compatibility.

But both are now instances of the same structural operation:

\[
\boxed{\text{finite 2-adic lifting controlled by carry divisibility}.}
\]

This is the strongest current bridge between `A_compat` and `A_dom`.

## 6. Computational consequence

Future danger searches need not compute a full `h`-bit residue first.
They may proceed in the exact order:

1. compute `R=ceil(log2 M)`;
2. solve the low-R residue `r_R`;
3. reject if `r_R>=M`;
4. compute the carry `C_R` only to the `z=h-R` bits needed;
5. reject if `nu_2(C_R)<z`;
6. only then evaluate any remaining terminal Bellman condition.

This is exact progressive Hensel lifting, not a probabilistic shortcut.

Reproducibility:

`collatz/src/2026_09_12_math090_dyadic_carry_valuation_certificate.py`
