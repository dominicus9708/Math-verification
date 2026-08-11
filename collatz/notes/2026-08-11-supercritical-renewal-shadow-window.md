# Exact supercritical renewal shadow-window theorem

Date: 2026-08-11

Status: **exact necessary-and-sufficient local characterization for a fixed aggregate-supercritical renewal word**. It combines the rational cycle shadow with the exact dyadic formation class and all interior renewal inequalities.

## 1. Fixed supercritical word

Let a finite maximal-block renewal word `w` induce the affine map

\[
\boxed{F(x)=ax+b,}
\]

with

\[
0<a<1,
\qquad b>0.
\]

In Collatz aggregate notation,

\[
a=\frac{3^H}{2^A},
\qquad A=H+D,
\]

and aggregate-supercriticality means `2^A>3^H`, hence `a<1`.

The unique positive rational fixed point is

\[
\boxed{C=\frac{b}{1-a}.}
\]

For every interior maximal-block boundary `r`, let

\[
F_r(x)=a_r x+b_r
\]

be the corresponding prefix affine map, and define the rational shadow state

\[
\boxed{C_r:=F_r(C).}
\]

## 2. Shadow minimum and prefix-coefficient inequalities

For a renewal word, the rational periodic shadow has `C` as its strict minimum block-start state, so

\[
\boxed{C_r>C}
\]

at every interior block boundary.

Also the proper suffix from the `r`th block start back to the next copy of `C` decreases from `C_r` to `C`. An affine Collatz suffix has positive correction, so such a decrease is possible only if its multiplicative coefficient is less than `1`.

The suffix coefficient is `a/a_r`; hence

\[
\boxed{a_r>a.}
\]

## 3. Translate the renewal inequalities below the shadow

Let `N` be an integer in the exact formation class of the word, and write

\[
\boxed{y:=C-N.}
\]

If `N<C`, then the full endpoint is

\[
N'=F(N)
=C-a(C-N)
=C-ay.
\]

Thus `N'>N` automatically because `0<a<1` and `y>0`.

At an interior block boundary,

\[
X_r=F_r(N)
=C_r-a_r(C-N)
=C_r-a_r y.
\]

The renewal condition is

\[
X_r>N'.
\]

Substituting the two shadow formulas gives

\[
C_r-C>(a_r-a)y.
\]

Because both sides have positive coefficients, this is equivalent to

\[
\boxed{
y<\frac{C_r-C}{a_r-a}.}
\]

## 4. Exact shadow-window width

Define

\[
\boxed{
W(w):=
\min_{r\,\text{interior block boundary}}
\frac{C_r-C}{a_r-a}.
}
\]

Then all interior renewal inequalities are equivalent to the single bound

\[
\boxed{0<C-N<W(w).}
\]

If the renewal word contains no interior block boundary (one maximal block), the macroblock sign theorem already rules out the supercritical floor-increasing case, so the supercritical theorem is relevant only for multi-block words.

## 5. Exact formation class

A finite maximal-block word begins at an odd state and ends immediately before the next odd block start. Therefore exact formation, including endpoint oddness, fixes one residue class

\[
\boxed{N\equiv r_w\pmod{2^{A+1}}.}
\]

Consequently the positive integers that realize the fixed supercritical word as a floor-to-floor renewal segment are exactly

\[
\boxed{
\left(r_w+2^{A+1}\mathbb Z\right)
\cap\mathbb N
\cap(C-W(w),C).
}
\]

This is an exact bounded interval-channel representation.

## 6. Atomic consequences

The candidate count for the word is finite. In particular, if

\[
W(w)<2^{A+1},
\]

there is at most one integer renewal floor realizing the word.

More generally the exact candidate count is the number of points of one arithmetic progression of spacing `2^{A+1}` inside the open shadow window.

Thus aggregate-supercritical renewal formation is reduced to a finite **residue–window intersection** rather than an unbounded parity class.

## 7. Relation to the current proof architecture

This theorem does not exclude all supercritical renewal words. Its value is that the three previously separate ingredients are now one object:

1. dyadic formation — `r_w mod 2^{A+1}`;
2. rational cycle shadow — `C`;
3. renewal-floor inequalities — window width `W(w)`.

A complete supercritical-renewal exclusion may therefore seek a universal separation theorem of the form

\[
\boxed{
\operatorname{dist}\left(C,\ r_w+2^{A+1}\mathbb Z\right)
\ge W(w),
}
\]

for the residual economical word classes, or a global theorem showing that such residue-window intersections cannot concatenate indefinitely.