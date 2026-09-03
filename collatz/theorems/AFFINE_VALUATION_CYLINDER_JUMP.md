# Affine valuation-cylinder jump transducer

Status: **EXACT / CLOSED as a source-family transition theorem**

## Setup

Let the current exact source/state family be

\[
Y(m)=y+A m,
\]

where `A` is odd and `m` ranges over a finite integer interval.
Assume the represented states are positive.

The next odd event in the accelerated Collatz parity sequence is preceded by

\[
a=v_2(Y(m))
\]

zero bits.  Thus its forced prefix is

\[
0^a1.
\]

## Exact valuation cylinder

Fix `a>=0` and set

\[
M_a=2^{a+1}.
\]

For a positive integer,

\[
v_2(Y)=a
\iff
Y\equiv2^a\pmod{2^{a+1}}.
\]

Because `A` is odd, it is invertible modulo `M_a`. Therefore

\[
y+A m\equiv2^a\pmod{M_a}
\]

has exactly one parameter residue

\[
\boxed{
 m\equiv\rho_a
 :=(2^a-y)A^{-1}\pmod{2^{a+1}}.
}
\]

Hence each possible next-one position is an exact dyadic parameter cylinder.
No memberwise orbit enumeration is required to identify the cylinder.

## Exact jump

Write a member of that child as

\[
m=\rho_a+2^{a+1}k.
\]

After `a` even steps and one odd step,

\[
Y'
=\frac{3Y+2^a}{2^{a+1}}.
\]

Substitution yields

\[
\begin{aligned}
Y'
&=
\frac{3(y+A\rho_a)+2^a}{2^{a+1}}
+3A k.
\end{aligned}
\]

Therefore, defining

\[
y'_a
:=
\frac{3(y+A\rho_a)+2^a}{2^{a+1}},
\]

we obtain the exact child family

\[
\boxed{
Y'(k)=y'_a+3A k.
}
\]

The new affine coefficient `3A` is again odd, so the same theorem applies recursively.

The exact transformed parameter interval is

\[
\left\lceil\frac{m_{lo}-\rho_a}{2^{a+1}}\right\rceil
\le k\le
\left\lfloor\frac{m_{hi}-\rho_a}{2^{a+1}}\right\rfloor.
\]

An empty interval means that valuation branch is absent from the family.

## Relation to residual correction decoding

For a remaining correction instance

\[
R=2^nZ-3^qY,
\]

if the next 1 occurs before the remaining endpoint depth, then the term `2^nZ` is invisible at the corresponding `2`-adic resolution and `3^q` is an odd unit. Therefore

\[
\boxed{v_2(R)=v_2(Y).}
\]

Thus the first jump of the residual valuation decoder can be executed entirely from the affine source cylinder. The checkpoint `Z` is not required to determine the next forced zero-run and odd event.

This is the family-resolution bridge missing from an exact-pair decoder.

## Compression consequence

A bitwise child refinement chooses one parity bit at a time.
The valuation-cylinder transition instead consumes the complete forced block

\[
0^a1
\]

in one transition and replaces the parent by an exact arithmetic child cylinder.

For a finite parameter interval, high-valuation branches rapidly become small because the modulus grows as `2^(a+1)`. This does not by itself prove that the full recursive tree is small, but it provides an exact block-jump representation on which further formation and physical predicates can act.

## DSD state interpretation

At this predicate the relevant state axes are:

- affine current-state base `y`;
- odd lift coefficient `A`;
- exact parameter interval;
- remaining length and one-count where required;
- future formation-control state.

The individual zero bits inside `0^a` are not independent future choices and may be forgotten after the jump. Their only required information is the certified valuation `a` and its effect on the future control state.

## Scope restrictions

This theorem does not establish:

- target-dominance / ballot validity after the jump;
- H/L or C4F preservation unless those controls are carried and updated;
- endpoint/checkpoint compatibility;
- tail or renewal closure;
- finiteness of the complete valuation-cylinder tree;
- A0 `s=1` Route-B closure;
- Collatz.

## Certificate

- `../src/A0_s1_affine_valuation_cylinder_jump_certificate.py`
