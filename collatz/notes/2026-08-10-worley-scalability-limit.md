# Scalability limit of the current Worley resonance isolation

Date: 2026-08-10

Status: **DERIVED DIAGNOSTIC / NEGATIVE GLOBALIZATION RESULT**

The exact Worley--Dujella isolation in `2026-08-10-worley-resonance-isolation.md` is extremely effective on the present finite interval because the project-specific approximation constant is only slightly above `2`.  This note checks whether the same small-coefficient enumeration remains comparably strong at the next large continued-fraction scale.

## 1. Current interval

For the present verified floor

\[
L=4\cdot3^{44}+2,
\]

the necessary approximation constant is

\[
k(q)=\frac{q(7q+1)}{24L\ln2}.
\]

At the isolated current upper convergent denominator

\[
q_*=137,528,045,312,
\]

we have the exact certified inequality

\[
k(q_*)<2.021.
\]

Hence Worley--Dujella restricts the primitive approximation to adjacent-convergent combinations with integral product `rs<=4`.  This is why the current interval collapses to a tiny finite list.

## 2. Next upper-convergent scale

The next upper convergent of `log_2 3` after the intervening lower convergent has denominator

\[
q_{\rm next}=5,409,303,924,479
\]

and numerator

\[
8,573,543,875,303.
\]

Direct high-precision evaluation of the same project constant gives, with the present floor,

\[
\boxed{k(q_{\rm next})\approx3125.71.}
\]

Thus the basic Worley product allowance would become roughly

\[
rs<6251.5,
\]

rather than `rs<=4`.

## 3. Even after one recursive-sufficiency layer

If the current ternary layer were completely eliminated and the verified floor increased by approximately a factor of three, replacing `L` by `3L` in the same necessary inequality gives

\[
\boxed{k(q_{\rm next};3L)\approx1041.90.}
\]

Even a factor-nine floor improvement would still give

\[
k(q_{\rm next};9L)\approx347.30.
\]

Therefore the tiny-Worley-list phenomenon at the current resonance is not automatically stable under one or two recursive-sufficiency layer advances.

## 4. Proof-program consequence

The present Worley isolation should be treated as a rigorous **local finite-interval compression**, not as a complete global induction mechanism.

To make the resonance ladder globally repeatable one would need at least one of:

1. a substantially faster increase of the verified floor than one ternary factor per stage;
2. a stronger correction bound than the uniform `(7q+1)/24` estimate, valid on the relevant future resonances;
3. an independent cross-base bridge that removes whole ternary layers without enumerating all Worley forms;
4. a new Diophantine approximation bound that uses additional Collatz structure beyond the raw `k/q^2` inequality.

This reinforces the current priority: eliminate the isolated present resonance by coupling its small start representative, sparse mechanical defects, near-return endpoint, and zero-lift condition.  Extending the current Worley enumeration several resonances forward before obtaining such a bridge is unlikely to be the best use of computation.

The numerical values in this note are diagnostics; the current exact isolation theorem remains the rigorously certified result.