# A0 s=1 Route-B — displaced-rank defect budget audit

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Definition

Let the strict-high/threshold target one positions be

\[
a_1<a_2<\cdots<a_q,
\]

and let a prefix-dominance candidate have

\[
b_r\le a_r.
\]

Write

\[
\delta_r=a_r-b_r
\]

and let

\[
M=\#\{r:\delta_r>0\}
\]

be the number of ranked ones that are genuinely displaced from the target.

The normalized defect is

\[
\eta
=
\sum_{r=1}^q
\frac{2^{a_r}-2^{b_r}}{3^r}
=
\sum_{r=1}^q
w_r\left(1-2^{-\delta_r}\right),
\]

where

\[
w_r=\frac{2^{a_r}}{3^r}.
\]

For the characteristic target,

\[
\frac16\le w_r<\frac12.
\]

---

## 2. Phase-weighted and count-only bounds

For every moved rank,

\[
\delta_r\ge1
\]

and therefore

\[
\frac12\le1-2^{-\delta_r}<1.
\]

Hence the exact target phases give

\[
\boxed{
\frac12
\sum_{r:\delta_r>0}w_r
\le
\eta
<
\sum_{r:\delta_r>0}w_r.
}
\]

Using only the universal weight interval gives the coarser but horizon-free
count bound

\[
\boxed{
\frac{M}{12}
\le
\eta
<
\frac{M}{2}.
}
\]

Thus a family theorem forcing \(M\) displaced ranks immediately yields a safe
membership-defect floor

\[
\underline\eta\ge\frac{M}{12}.
\]

Conversely an observed value \(\eta\) can only be produced if

\[
M>2\eta.
\]

The latter is a structural diagnostic, not by itself a physical rejection
criterion.

---

## 3. Root-scale consequence

The preceding adaptive defect-budget inversion shows that, at the lower
endpoints of the current 14 root intervals, whole-root rejection through the
real-envelope route needs a defect floor of approximately

\[
4.91418\times10^9.
\]

If one uses only the coarse count inequality

\[
\eta\ge M/12,
\]

then a sufficient displaced-rank count would be approximately

\[
M
\gtrsim
12(4.91418\times10^9)
\approx
5.8970\times10^{10}.
\]

For the full pre bridge

\[
j_0=65,868,186,701,
\]

so this is roughly

\[
89.5\%
\]

of all ranked odd events.

This percentage is a **strategy diagnostic**, not a theorem that 89.5% must be
moved by every physical candidate.  It says that a root-wide proof based only
on the weakest universal `1/12 per moved rank` floor would need an extremely
strong family-wide displacement theorem.

Therefore the more promising exact architecture is:

1. use source refinement to raise \(X_{lo}\), decreasing
   \(\eta_{close}(X_{lo})\);
2. retain the actual phase weights \(w_r\) rather than replacing them all by
   \(1/6\);
3. use projective cylinders to force nonzero displacements at selected ranks;
4. compose the resulting weighted floors through the H/L grammar.

---

## 4. Regression

Source:

`collatz/src/A0_s1_routeB_displaced_rank_defect_count_certificate.py`

An independent exact small-horizon execution checked:

- characteristic target weights: `64`;
- dominance candidates: `360`;
- nontrivial count-bound cases: `347`;
- phase-weighted cases: `347`.

All comparisons were exact rational arithmetic.

These are implementation regressions only; the inequalities above are direct
algebraic consequences of the target weight bounds.

---

## 5. DSD analysis

The new summary coordinate \(M\) is deliberately weaker than the projective
state.

It forgets:

- which ranks moved;
- the target phase weight at each moved rank;
- the displacement size beyond nonzero;
- the adic successor class.

That information loss is safe only in the direction

\[
M\text{ forced}
\Longrightarrow
\eta\ge M/12.
\]

It is not safe to reconstruct projective or formation information from \(M\).

Thus \(M\) is a one-way lower-bound quotient, not a complete language state.

---

## 6. DSD audit

### EXACT / CLOSED

- each displaced ranked one contributes at least `1/12` and less than `1/2`
  to the normalized characteristic-target defect;
- the phase-weighted lower bound is stronger and exact in its stated form;
- forced displaced-rank counts can be converted to safe defect floors.

### REGRESSION ONLY

- the finite exact counts listed above audit indexing and normalization.

### NOT INFERRED

- no current 14-root family is proved to force the root-scale displaced-rank
  count;
- the approximate 89.5% figure is not a property of all physical candidates;
- moved-rank count alone is not a complete H/L or projective state;
- Route-B membership and the Collatz conjecture remain open.

---

## 7. Updated target

The next useful accumulator should keep at least the pair

\[
\boxed{
(\text{projective cylinder},\ \underline\eta_{phase})
}
\]

rather than only a collision flag or a moved-rank count.

At each exact H/L product, the defect floor should compose by

\[
\underline\eta(UV)
=
\underline\eta(U)
+
\frac{2^{|U|}}{3^{q(U)}}
\underline\eta(V),
\]

while source refinement independently lowers the required physical closure
budget.  This is the current audited path toward family closure without
singleton enumeration.
