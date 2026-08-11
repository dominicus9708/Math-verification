# Exact supercritical renewal shadow-window theorem

Date: 2026-08-11

Status: **exact necessary-and-sufficient local characterization for a fixed aggregate-supercritical renewal-compatible segment word**. It combines the rational cycle shadow, the exact dyadic formation class, and all finite interior floor inequalities. It does **not** by itself certify that the endpoint is a suffix minimum of the infinite future orbit.

## 1. Fixed supercritical word

Let a finite maximal-block word `w` induce the affine map

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

We call the finite segment **renewal-compatible** if its integer endpoint `N'` is strictly above its start `N` while every interior block start is strictly above `N'`:

\[
\boxed{N<N',\qquad X_r>N'\text{ for every interior block boundary}.}
\]

Every genuine floor-to-floor renewal segment has this property. The converse becomes a genuine renewal step only when the infinite continuation from `N'` also stays at or above `N'`.

## 2. Shadow minimum and prefix-coefficient inequalities

For a word occurring as a genuine renewal segment, the rational periodic shadow has `C` as its strict minimum block-start state, so

\[
\boxed{C_r>C}
\]

at every interior block boundary.

Also the proper suffix from the `r`th block start back to the next copy of `C` decreases from `C_r` to `C`. An affine Collatz suffix has positive correction, so such a decrease is possible only if its multiplicative coefficient is less than `1`.

The suffix coefficient is `a/a_r`; hence

\[
\boxed{a_r>a.}
\]

For a fixed word already known to have these shadow inequalities, the finite renewal-compatible integer starts can be characterized exactly as below.

## 3. Translate the finite renewal inequalities below the shadow

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

The finite renewal-compatible condition is

\[
X_r>N'.
\]

Substituting the two shadow formulas gives

\[
C_r-C>(a_r-a)y.
\]

Because both coefficients are positive, this is equivalent to

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

Then, for a fixed word satisfying the shadow-minimum/prefix-coefficient conditions, all **finite** renewal-compatible inequalities are equivalent to

\[
\boxed{0<C-N<W(w).}
\]

If the word contains no interior block boundary (one maximal block), the macroblock sign theorem already rules out the supercritical floor-increasing case.

## 5. Exact formation class

A finite maximal-block word begins at an odd state and ends immediately before the next odd block start. Therefore exact formation, including endpoint oddness, fixes one residue class

\[
\boxed{N\equiv r_w\pmod{2^{A+1}}.}
\]

Consequently the positive integers that realize the fixed word as a **finite renewal-compatible segment** are exactly

\[
\boxed{
\left(r_w+2^{A+1}\mathbb Z\right)
\cap\mathbb N
\cap(C-W(w),C).
}
\]

A genuine renewal-floor transition is an element of this set whose endpoint `N'` also satisfies the global suffix-minimum condition for the infinite continuation.

## 6. Atomic consequences

The finite compatible candidate count for the word is finite. In particular, if

\[
W(w)<2^{A+1},
\]

there is at most one integer start realizing the finite renewal-compatible segment.

More generally the exact finite candidate count is the number of points of one arithmetic progression of spacing `2^{A+1}` inside the open shadow window.

Thus aggregate-supercritical finite renewal compatibility is reduced to a bounded **residue–window intersection** rather than an unbounded parity class.

## 7. Relation to the current proof architecture

The theorem does not exclude all supercritical renewal words and does not replace the global suffix-minimum condition. Its value is that three finite ingredients are now one object:

1. dyadic formation — `r_w mod 2^{A+1}`;
2. rational cycle shadow — `C`;
3. finite floor-to-floor inequalities — window width `W(w)`.

A complete supercritical-renewal exclusion may therefore seek a universal separation theorem of the form

\[
\boxed{
\operatorname{dist}\left(C,\ r_w+2^{A+1}\mathbb Z\right)
\ge W(w),
}
\]

for residual economical word classes, or a global theorem showing that the surviving residue-window intersections cannot concatenate into an infinite suffix-minimum chain.