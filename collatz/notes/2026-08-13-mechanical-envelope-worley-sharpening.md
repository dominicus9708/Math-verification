# Mechanical-envelope sharpening of the Worley first-crossing isolation

Date: 2026-08-13

Status: **exact theorem application + exact rational certificate**. This note combines the first-crossing mechanical/Christoffel remainder envelope with the existing Worley--Dujella resonance isolation. It strengthens the Diophantine approximation constant and reduces the adjacent-convergent product budget from `rs<=4` to `rs<=3`. It does not prove Collatz or coefficient stopping globally.

## 1. First-crossing envelope

For the accelerated map, write a completed first coefficient crossing in odd-count form as

\[
A=\lceil q\log_2 3\rceil,
\qquad
P=\frac{2^A}{3^q}>1.
\]

For any parity word `w` that survives above its start through the first coefficient crossing, write

\[
T^A(N)=\frac{3^q}{2^A}(N+S_w).
\]

The first-crossing prefix constraint forces the maximal additive correction to be attained by the mechanical/Christoffel word. Hence

\[
S_w\le S_{\rm chr}.
\]

For the mechanical word,

\[
S_{\rm chr}
=\frac13\sum_{i=0}^{q-1}2^{-\{i\log_2(3/2)\}},
\]

and the Denjoy--Koksma bound gives

\[
\boxed{
S_w\le S_{\rm chr}
\le\frac{q}{6\ln2}+\frac13.
}
\]

This is strictly sharper than the earlier all-parity ceiling `(7q+1)/24` for the first-crossing branch.

## 2. Approximation consequence

If a first-crossing survivor starts at `N>=L`, then

\[
N(P-1)\le S_w.
\]

Also

\[
P-1\ge\ln P
=A\ln2-q\ln3
=q\ln2\left(\frac Aq-\log_2 3\right).
\]

Therefore

\[
0<\frac Aq-\log_2 3
<
\frac{1}{6L(\ln2)^2}
+
\frac{1}{3Lq\ln2}.
\]

Equivalently,

\[
\left|\log_2 3-\frac Aq\right|
<\frac{k(q)}{q^2},
\]

with

\[
\boxed{
k(q)=
\frac{q^2}{6L(\ln2)^2}
+
\frac{q}{3L\ln2}.}
\]

## 3. Current verified floor and target interval

Use the exact bootstrap floor

\[
\boxed{
L=V_{32}=4(3^{44}+3^{32})+2
=3,939,091,020,815,200,338,890.
}
\]

On

\[
72,057,431,991<q\le137,528,045,312,
\]

`k(q)` is increasing. Exact rational logarithm intervals certify

\[
\boxed{k(q)<1.666.}
\]

The previous all-parity certificate had only

\[
k(q)<2.021.
\]

Thus the first-crossing mechanical envelope cuts roughly 17.6% from the Diophantine approximation constant in this interval.

## 4. Worley--Dujella consequence

Use the classical Worley theorem in the Dujella--Ibrahimpasic form: if a reduced rational `a/b` satisfies

\[
\left|\alpha-\frac ab\right|<\frac{k}{b^2},
\]

then it is an adjacent-convergent combination

\[
(a,b)=
(rp_{m+1}\pm sp_m,
 rq_{m+1}\pm sq_m)
\]

with nonnegative integers `r,s` satisfying

\[
rs<2k.
\]

Here

\[
2k<3.332,
\]

so integrality gives

\[
\boxed{rs\le3.}
\]

The previous certificate required `rs<=4`.

Non-reduced actual pairs `(A,q)=g(a,b)` are still handled explicitly; no hidden coprimality assumption is introduced.

## 5. Exact finite certificate

`collatz/src/mechanical_envelope_worley_sharpened.py` uses exact `Fraction` arithmetic and rigorous rational intervals for `ln 2`, `ln 3`, and their quotient.

It certifies:

- `k_max < 1.666`;
- the complete `rs<=3` Worley primitive superset in the target denominator interval;
- exactly `29` primitive candidates before the direct first-crossing error filter;
- exactly one surviving primitive pair,

\[
\boxed{
(A,q)=
(217,976,794,617,
137,528,045,312);
}
\]

- multiplicity `g=1` only;
- the nearest rejected primitive is

\[
\frac{10,439,860,591}{6,586,818,670},
\]

whose certified approximation error is more than `25.17` times the direct mechanical-envelope allowance over the target interval.

Therefore the current resonance remains the unique possible first coefficient crossing throughout the whole interval, now with a substantially larger separation margin.

## 6. Conceptual consequence

The continued-fraction concentration is no longer merely a numerical observation in this finite interval.

The inference chain is

\[
\boxed{
\text{first-crossing prefix constraint}
\Rightarrow
\text{mechanical maximal remainder}
\Rightarrow
\text{very small rational-approximation error}
\Rightarrow
\text{finite adjacent-convergent family}
\Rightarrow
\text{one exact resonance}.
}
\]

This explains why convergents, semiconvergents, and nearby mediant-type combinations naturally appear: the Worley--Dujella theorem produces precisely small integer combinations of adjacent convergents once the Collatz first-crossing inequality forces an `O(q^{-2})` approximation.

It does **not** prove that every possible first-crossing resonance at arbitrary depth must itself be a convergent or semiconvergent. As the denominator grows with a fixed verification floor, `k(q)` grows quadratically and the finite combination budget grows as well. A terminal theorem must either raise the floor in tandem, obtain a stronger correction bound, or use the dyadic/ternary/3-adic compatibility conditions before applying the Diophantine reduction.

## External inputs

- R. T. Worley, *Estimating |alpha-p/q|*, Journal of the Australian Mathematical Society 31 (1981), 202--206.
- A. Dujella and B. Ibrahimpasic, *On Worley's theorem in Diophantine approximations*, Annales Mathematicae et Informaticae 35 (2008), 61--73.
- O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026), 115167 / arXiv:2502.00948. Their parity-vector order supplies the external remainder monotonicity background used by the mechanical-envelope argument.
