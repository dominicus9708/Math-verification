# COV-1: single-anchor inverse route has a strict <8% 3-adic coverage ceiling

Date: 2026-09-06

Status: **SAFE GLOBAL BARRIER FOR ONE PROOF MECHANISM.**  Let

\[
x=36k+27,
\qquad
T(x)=54k+41.
\]

Consider the proof mechanism that fixes the forward anchor `T(x)` and searches its reverse shortcut tree for a smaller positive predecessor `m<x` using

\[
E(z)=2z,
\qquad
O(z)=\frac{2z-1}{3}.
\]

Even if this reverse language is continued to arbitrary depth, the set of `3`-adic parameters `k` that it can possibly certify has Haar measure strictly below `0.08`.  Therefore its complement has measure above `0.92`.  The route remains useful as a finite symbolic eliminator but cannot by itself prove the whole progression recursive.

This is a statement about one anchored merge language, not about Collatz convergence and not about all possible recursive-merge mechanisms.

---

## 1. Immediate obstruction: `k=0`

At

\[
k=0,
\qquad
x=27,
\qquad
T(x)=41.
\]

A reverse certificate anchored at `41` would require some

\[
1\le m<27
\]

whose forward shortcut orbit reaches `41`.

Direct exact finite trajectory checking for the integers `1,...,26` shows that none reaches `41`.  Thus

\[
\boxed{k=0\notin\mathcal R_1,}
\]

where `R_1` denotes the single-anchor inverse-merge coverage set.

This already disproves the previously proposed target

\[
\mathcal R_1=\mathbb N_0.
\]

The stronger measure theorem below shows that this is not an isolated exceptional integer.

Status: **SAFE FINITE OBSTRUCTION.**

---

## 2. Canonical contracting words

For a reverse word with `q` letters `O`, let their positions be

\[
0\le p_0<\cdots<p_{q-1}\le P_q,
\]

where

\[
P_q=\lfloor(q-1)\log_2 3\rfloor.
\]

As proved in the preceding closed-form note:

1. trailing `E` letters are unnecessary;
2. every minimal coverage word ends in `O`;
3. the contraction condition is exactly `p_(q-1)<=P_q`;
4. final integrality is equivalent to stepwise `O` admissibility.

For `q>=3`, the necessary and sufficient cylinder solvability condition begins with

\[
2^{-p_0-1}
+3\,2^{-p_1-1}
+9\,2^{-p_2-1}
\equiv41\pmod{27}.
\]

Every contracting position set passing this condition determines at most one cylinder

\[
k\pmod{3^{q-3}}.
\]

The word may still fail positivity or `m<x`; retaining it nevertheless gives a valid **upper bound** on possible coverage.

---

## 3. Word-count measure bound

Let `N_q` be the number of contracting `q`-position sets satisfying the first-three mod-27 condition.

A cylinder modulo `3^(q-3)` has normalized Haar measure

\[
3^{-(q-3)}.
\]

Therefore, without needing disjointness,

\[
\boxed{
\mu_3(\mathcal R_1)
\le
\sum_{q\ge3}
\frac{N_q}{3^{q-3}}.
}
\]

Duplicates across words and across levels only make this upper bound looser.

Status: **SAFE UNION BOUND.**

---

## 4. Exact counting of the mod-27 filter

Modulo `27`, the sequence

\[
2^{-p-1}
\]

has period `18`, because `2` is a generator of the unit group modulo `27`.

For fixed

\[
p_1<p_2,
\]

the congruence uniquely determines `p_0 mod 18`.  Hence the number of allowed `p_0<p_1` can be counted exactly by residue arithmetic, without enumerating the later positions.

If `A(p_2)` is the exact number of admissible pairs `p_0<p_1<p_2`, then

\[
\boxed{
N_q
=
\sum_{p_2=0}^{P_q}
A(p_2)
\binom{P_q-p_2}{q-3}.
}
\]

This formula computes the full filtered word count in polynomial time at each `q`; it does not enumerate every reverse word.

---

## 5. Exact partial sum through `q<500`

Using Section 4 with integer arithmetic, define

\[
S_{<500}
:=
\sum_{q=3}^{499}
\frac{N_q}{3^{q-3}}.
\]

The regression certificate evaluates this as one exact rational number and verifies numerically only for readability that

\[
\boxed{
S_{<500}
\approx0.07950622802173427.
}
\]

The decimal is not the proof object; the exact `Fraction` value is retained and used in the final comparison.

---

## 6. Rigorous infinite tail bound

For the tail we may discard the mod-27 filter completely.  The number of contracting `q`-position sets is at most

\[
\binom{P_q+1}{q}.
\]

Since

\[
3^5=243<256=2^8,
\]
we have

\[
\log_2 3<\frac85.
\]

Therefore

\[
P_q+1
<\frac85q.
\]

For any `z>0`, the binomial theorem gives

\[
\binom nq z^q\le(1+z)^n.
\]

Take

\[
z=\frac53.
\]

Then

\[
\binom{P_q+1}{q}
\le
\left[
\frac{(8/3)^{8/5}}{5/3}
\right]^q.
\]

Dividing by `3^(q-3)` gives

\[
\frac{\binom{P_q+1}{q}}{3^{q-3}}
\le
27r^q,
\]

where

\[
\boxed{
r=\frac{(8/3)^{8/5}}5.}
\]

The inequality

\[
r<\frac{193}{200}
\]

is checked without floating point by raising to the fifth power:

\[
\frac{(8/3)^8}{5^5}
<
\left(\frac{193}{200}\right)^5.
\]

Hence

\[
\boxed{
S_{\ge500}
\le
27
\frac{(193/200)^{500}}
{1-193/200}.
}
\]

The exact rational tail is approximately

\[
1.41564\times10^{-5}.
\]

Status: **SAFE RIGOROUS TAIL.**

---

## 7. Global ceiling

Adding the exact finite rational sum and the rigorous rational tail yields

\[
\boxed{
\mu_3(\mathcal R_1)
<0.079520385
<\frac{2}{25}.
}
\]

Therefore

\[
\boxed{
\mu_3(\mathbb Z_3\setminus\mathcal R_1)
>\frac{23}{25}
=0.92.
}
\]

This is a theorem about the **entire infinite single-anchor reverse language**, not merely the finite `q<=23` certificate.

The earlier exact prefix-free coverage

\[
\frac{561769}{43046721}
\approx0.01305
\]

through `q<=23` is compatible with this ceiling but is logically independent: that value is an exact lower bound on actually certified cylinders through a finite depth, whereas the present result is an upper bound on everything this mechanism can ever certify.

---

## 8. Consequence for the proposed complement automaton

The previous note suggested building a `3`-adic automaton and attempting to prove that it has no infinite path.

That target is now **REJECTED**.

Not only does the explicit ordinary integer `k=0` survive, but the complement has positive Haar measure greater than `0.92`.  Hence any faithful automaton for this one-anchor language must possess a very large infinite survivor set.

The correct use of such an automaton is therefore descriptive:

- characterize the small covered sublanguage;
- identify which other merge anchors/mechanisms are needed on the complement;
- avoid mistaking failure of one inverse-tree anchor for a Collatz obstruction.

---

## 9. DSD audit

### SAFE

1. `k=0` is not covered by an inverse tree anchored at `T(27)=41` with `m<27`.
2. Every filtered contracting `q`-word contributes at most one `3^(q-3)` cylinder.
3. The union bound by `sum N_q/3^(q-3)` is valid.
4. The exact filtered count formula for `N_q` is valid.
5. The `q<500` contribution is computed exactly.
6. The infinite tail has the displayed rational geometric bound.
7. The whole single-anchor language has Haar measure `<2/25`.

### REJECTED

\[
\mathcal R_1=\mathbb N_0
\]

and the stronger proposed strategy “prove the complement automaton has no infinite path.”

### OPEN

1. Full recursion of `36N_0+27` by other mechanisms.
2. Whether a finite or structured family of **shifted forward anchors** can cover the complement.
3. Whether the corrected removed-layer hierarchy admits a uniform recursive-sufficiency proof independent of single-anchor inverse trees.

### PROHIBITED UPGRADES

1. Do not interpret the `>92%` complement as potential counterexamples; it is merely uncovered by this proof mechanism.
2. Do not infer an upper bound on all recursive integers in the progression.
3. Do not combine the finite `1.305%` lower coverage and infinite `<8%` upper ceiling as if they determined the true limiting coverage.
4. Do not continue trying to close COV-1 solely by deeper search from `T(x)`.

---

## 10. Regression certificate

`collatz/src/cov1_single_anchor_3adic_measure_upper_bound_certificate.py`

computes the exact filtered partial sum, proves the rational tail comparison, and asserts

\[
\boxed{
\mu_3(\mathcal R_1)<\frac{2}{25}.
}
\]

---

## 11. Revised next target

The proof tree should branch away from the single anchor.

The two highest-value routes are now:

### COV-1A — shifted-anchor hierarchy

For

\[
z_h=T^h(x),
\]
construct reverse merge languages anchored at later forward states, with the forward parity cylinder made explicit.  Determine whether a **bounded or recursively structured family of anchors** gives cumulative coverage that is qualitatively larger than the `<8%` one-anchor ceiling.

### COV-1B — direct removed-layer recursion

Use the exact form

\[
F_n\setminus F_{n+1}
\]

and seek a merge identity uniform in the lower ternary `0/1` word, rather than proving recursion by following a particular forward anchor.

Either route must be audited independently before restoring universal ternary-core coverage.
