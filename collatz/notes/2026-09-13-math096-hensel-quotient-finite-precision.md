# MATH-096 — normalized Hensel quotient and finite future precision

Date: 2026-09-13

Status: `EXACT STRUCTURAL REDUCTION / FINITE 2-ADIC PRECISION SUFFICIENT`

## 1. Hensel quotient identity

For every exact composed cylinder

\[
Y=A+2^Hs,
\qquad
Y'=B+3^Qs,
\]

there is an exact correction numerator `C` with

\[
2^HB=3^QA+C.
\]

Writing

\[
S=\frac{C}{3^Q}
\]

gives

\[
\boxed{
X:=3^{-Q}B=\frac{A+S}{2^H}.
}
\]

Thus the normalized MATH-092 address `X` is the quotient remaining after the low `H` dyadic Hensel condition

\[
A\equiv-S\pmod{2^H}
\]

has been consumed.  This identifies the recent one-paid address variable with the same quotient/carry architecture used in the earlier fixed-depth Hensel calculations.

The identity is algebraic and is also regressed on all 910 canonical one-paid cylinders.

## 2. Resolution-indexed precision

For an exact current source family of size `M`, let

\[
R=\lceil\log_2M\rceil.
\]

Every canonical one-paid edge has resolution

\[
h\le73.
\]

Define

\[
\boxed{P(R)=73+R.}
\]

This many 2-adic bits of

\[
G=3^{-Q},\qquad X=3^{-Q}B
\]

are sufficient for every future one-paid address decision.

Indeed, for a multi child, necessarily `h<=R`, and exact family arithmetic gives

\[
R'\le R-h.
\]

MATH-092 propagates `P` bits exactly to `P-h` bits.  Since

\[
73+R'\le73+R-h=P-h,
\]

the child still has all precision required for its entire future.

If an edge is terminal, no future address state is needed and its compatibility requires at most its own `h<=73` current bits, already contained in `P(R)`.

## 3. Compact proof-facing address state

Consequently the infinite 2-adic address can be replaced, without loss for the remaining one-paid problem, by the finite pair

\[
\boxed{
X\bmod2^{73+R},
\qquad
G\bmod2^{73+R}.
}
\]

Together with exact source multiplicity and phase information this is sufficient to reproduce every later canonical one-paid compatibility decision.

This does not claim that the resulting finite state space is already small enough for a symbolic proof; it establishes finite sufficiency and removes unnecessary high 2-adic bits.

## 4. Relation to MATH-090

At a terminal edge with overshoot

\[
z=h-R>0,
\]

MATH-090 rewrites the same compatibility decision as

\[
r_R<M,
\qquad
\nu_2(C_R)\ge z.
\]

Thus the finite word `(X,G)` and the carry-valuation description are equivalent views of the compatibility channel: one is convenient for forward transduction, the other for terminal pruning.

## 5. Claim boundary

MATH-096 does not by itself close any new macro depth.  Its role is to provide the exact compact state used by the subsequent danger-corridor calculations.

Reproducibility:

`collatz/src/2026_09_13_math096_hensel_quotient_precision_certificate.py`
