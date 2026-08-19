# Worley--Dujella isolation of the next first-crossing resonance

Date: 2026-08-10

Status: **DERIVED EXTERNAL-THEOREM APPLICATION + EXACT RATIONAL CERTIFICATE**

This note rigorously discretizes the finite first-coefficient-crossing branch between the previously eliminated resonance and the next unresolved convergent.  It uses the classical Worley--Dujella continued-fraction theorem as an external input and exact rational interval arithmetic for all project-specific inequalities.  It is not a proof of Collatz or of coefficient stopping globally.

## 1. Setup

Let

\[
\alpha=\log_2 3.
\]

For a first coefficient crossing with `q` odd steps,

\[
\sigma=\lceil q\alpha\rceil,
\qquad
D=2^\sigma-3^q>0.
\]

Let

\[
L=4\cdot3^{44}+2
\]

be the current recursively-sufficient verification floor used by the project.

The interval considered here is

\[
\boxed{
72,057,431,991<q\le137,528,045,312.
}
\]

The left endpoint is the previously treated upper semiconvergent resonance.  The right endpoint is the next unresolved upper convergent denominator.

## 2. Necessary rational-approximation bound

At a paradoxical first crossing, with normalized correction `S=R/3^q`,

\[
x\le\frac{S}{\delta},
\qquad
\delta=\frac{2^\sigma}{3^q}-1.
\]

The elementary all-`q` pair bound gives

\[
S\le\frac{7q+1}{24}.
\]

Also

\[
\delta=e^{\sigma\ln2-q\ln3}-1
\ge \sigma\ln2-q\ln3
= q\ln2\left(\frac\sigma q-\alpha\right).
\]

If a paradoxical start is above the verified floor `x>=L`, then

\[
Lq\ln2\left(\frac\sigma q-\alpha\right)
<\frac{7q+1}{24},
\]

hence

\[
\boxed{
0<\frac\sigma q-\alpha
<
\frac{7q+1}{24Lq\ln2}.
}
\]

Equivalently,

\[
\left|\alpha-\frac\sigma q\right|
<\frac{k(q)}{q^2},
\qquad
\boxed{
k(q)=\frac{q(7q+1)}{24L\ln2}.}
\]

On the target interval `k(q)` is increasing, and exact rational logarithm bounds certify

\[
\boxed{k(q)<2.021.}
\]

## 3. External theorem: Worley--Dujella

The theorem used is the standard result of Worley, in the improved form quoted by Dujella and Ibrahimpasic:

if `a/b` is in reduced form and

\[
\left|\alpha-\frac ab\right|<\frac{k}{b^2},
\]

then for adjacent continued-fraction convergents `p_m/q_m`, `p_{m+1}/q_{m+1}` of `alpha`,

\[
\boxed{
(a,b)=
(rp_{m+1}\pm sp_m,
 rq_{m+1}\pm sq_m)
}
\]

for nonnegative integers `r,s` satisfying

\[
\boxed{rs<2k.}
\]

For the present interval, `k<2.021`, so the integral product obeys

\[
\boxed{rs\le4.}
\]

Thus only finitely many small adjacent-convergent combinations need to be checked.

Important: the actual pair `(sigma,q)` need not be reduced.  Write

\[
(\sigma,q)=g(a,b),
\qquad \gcd(a,b)=1.
\]

Then the approximation is still `a/b`, while the actual denominator is `q=gb`.  The verifier therefore enumerates every allowed reduced Worley form and every possible multiplicity interval that can place `gb` inside the target `q` interval.  No coprimality assumption on `(sigma,q)` is silently introduced.

## 4. Exact rational certification of the continued fraction

The verifier does not obtain the relevant continued fraction from floating point.

For `0<x<1`,

\[
\log\frac{1+x}{1-x}
=2\sum_{j\ge0}\frac{x^{2j+1}}{2j+1}.
\]

Using 61 retained terms and the positive geometric tail bound gives exact rational intervals for

\[
\ln2\quad(x=1/3),
\qquad
\ln3\quad(x=1/2).
\]

Their quotient yields an exact rational interval for `alpha=ln3/ln2`.  Interval continued-fraction inversion certifies the first 26 partial quotients, including

\[
\ldots,15,1,9,2,5,7.
\]

The relevant neighboring convergents include

\[
\frac{103,768,467,013}{65,470,613,321}
<\alpha
<
\frac{217,976,794,617}{137,528,045,312}.
\]

## 5. Finite Worley superset and direct project filter

After:

1. enumerating every adjacent-convergent `+/-` combination with `rs<=4`;
2. reducing it to `a/b`;
3. retaining only fractions for which some multiple `gb` lies in the target `q` interval;
4. applying the necessary Worley superset bound;

there are exactly

\[
\boxed{30}
\]

distinct reduced primitive approximants left.

The project-specific paradoxical lower-bound condition from Section 2 is then applied using exact rational upper/lower bounds for `alpha` and `ln2`.

Exactly one primitive approximation survives:

\[
\boxed{
\frac{\sigma}{q}
=
\frac{217,976,794,617}{137,528,045,312}.
}
\]

Its only multiplicity in the target interval is `g=1`.

Therefore:

\[
\boxed{
72,057,431,991<q\le137,528,045,312
}
\]

and

\[
\boxed{x\ge4\cdot3^{44}+2}
\]

imply that any paradoxical first coefficient crossing in this entire interval must occur at

\[
\boxed{
(q,\sigma)
=(137,528,045,312,
  217,976,794,617).
}
\]

Thus there is no unexamined first-crossing resonance between the previously eliminated semiconvergent and the current unresolved convergent, subject only to the stated external Worley--Dujella theorem and the already-derived project inequalities.

## 6. Separation margin

The nearest rejected primitive approximation in the Worley superset is

\[
\frac{124,648,188,195}{78,644,250,661}.
\]

Its certified approximation error is more than

\[
\boxed{2.68}
\]

times the largest direct error permitted by the project inequality over the target interval.

Hence the isolation is not a rounding-edge phenomenon.

## 7. Verification

`collatz/src/worley_resonance_isolation.py` uses only Python integer arithmetic and `fractions.Fraction`.

It certifies:

- exact logarithm intervals;
- the required continued-fraction prefix;
- `k_max<2.021`;
- the complete `rs<=4` Worley primitive superset;
- non-reduced multiplicity handling;
- exactly 30 primitive candidates before the direct project filter;
- exactly one surviving pair afterward;
- the `>2.68` margin for the nearest rejected primitive.

## 8. Proof-program consequence

The finite first-crossing branch no longer needs to treat every odd count in this very large interval separately.

The current unresolved task in this interval is genuinely concentrated at one Diophantine resonance:

\[
(q,\sigma)
=(137,528,045,312,
  217,976,794,617).
\]

Therefore all ternary-core, defect-run, rational Denjoy--Koksma, and zero-lift work aimed at that pair is not merely selecting a numerically interesting example: it exhausts the whole presently unverified `q` interval above the previous eliminated resonance.

The next global task after eliminating this pair would be to repeat the same exact Worley isolation on the following interval, with the approximation constant updated from the same verified floor or from any improved floor obtained in the meantime.

## 9. External reference discipline

The continued-fraction representation theorem is external mathematics and should be cited rather than presented as project-derived.  Suitable sources are:

- R. T. Worley, *Estimating |alpha-p/q|*, Journal of the Australian Mathematical Society 31 (1981), 202--206.
- A. Dujella and B. Ibrahimpasic, *On Worley's theorem in Diophantine approximations*, Annales Mathematicae et Informaticae 35 (2008), 61--73.

The Collatz-specific approximation bound, finite resonance interval, exact rational certificate, and coupling to the current recursive-sufficiency floor are project-derived applications.
