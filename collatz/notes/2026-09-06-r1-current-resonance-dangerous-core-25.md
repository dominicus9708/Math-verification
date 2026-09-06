# R1 current resonance: exact 25-axis dangerous core

Date: 2026-09-06

Status: **SAFE FIXED-CELL ARITHMETIC / SELECTOR-COVERAGE CONDITIONAL GLOBAL USE.**  For the already isolated coefficient cell

\[
(A,q)=(217,976,794,617,137,528,045,312),
\]

the mixed-interaction theorem's dangerous-axis dimension is exactly `25`.  This arithmetic fact is independent of the ternary selector coverage.  What is conditional is the claim that every hypothetical minimal counterexample reaches this cell, because that reduction used the `V_33` floor whose global scope depends on the reopened recursive-sufficiency coverage theorem.

Nothing in this note proves the Collatz conjecture.

---

## 1. Dangerous-axis criterion

At a first coefficient crossing put

\[
M=2^A,
\qquad
P=3^q,
\qquad
D=M-P>0.
\]

The existing mixed-interaction reduction proves that an elementary odd-position coordinate `i` can reverse canonical-start order versus descent-margin order only if

\[
\boxed{3^{q-i}\ge D.}
\]

Divide by `3^q` and write

\[
\varepsilon:=\frac{2^A}{3^q}-1.
\]

Then coordinate `i` is dangerous only if

\[
\boxed{\varepsilon\le3^{-i}.}
\]

Thus it is enough to locate `epsilon` between two adjacent powers of `3`.

---

## 2. Rigorous logarithmic localization

Write

\[
E:=A\ln2-q\ln3.
\]

Then

\[
\varepsilon=e^E-1.
\]

The accompanying certificate uses only exact rational arithmetic and the positive atanh series

\[
\ln x
=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},
\qquad
z=\frac{x-1}{x+1},
\]

with an explicit geometric upper bound on the omitted positive tail.

It proves

\[
\boxed{
\ln(1+3^{-26})
<
A\ln2-q\ln3
<
\ln(1+3^{-25}).
}
\]

Exponentiating gives

\[
\boxed{
3^{-26}
<
\frac{2^A}{3^q}-1
<
3^{-25}.
}
\]

Therefore

\[
\varepsilon\le3^{-i}
\]

holds exactly for

\[
1\le i\le25.
\]

Hence

\[
\boxed{h(q)=25.}
\]

Status: **SAFE EXACT FIXED-CELL THEOREM.**

---

## 3. Interpretation

The nominal odd-event count is

\[
q=137,528,045,312.
\]

Nevertheless every elementary coordinate capable of a local `x`-versus-`z` order reversal lies among only the first

\[
\boxed{25}
\]

odd-position axes.

All later coordinates satisfy

\[
D>3^{q-i}
\]

and therefore have the proven safe elementary co-order property.

This is a dramatic geometric localization, but it is **not yet** a proof of the Dangerous-Core Extremal Reduction.  The existing theorem controls each elementary safe-tail edge; it does not automatically imply that the global minimizer of `x` over all safe-tail completions equals the global minimizer of `z`.

That global statement remains OPEN.

---

## 4. Dimension 25 is not `2^25` states

The odd-position coordinates are not independent bits.

For the first `h` odd events, admissibility requires

\[
0\le\alpha_1<\alpha_2<\cdots<\alpha_h,
\]

with

\[
\alpha_i\le\lfloor(i-1)\log_2 3\rfloor.
\]

An exact dynamic count gives, for `h=25`,

\[
\boxed{
\#\{\text{admissible first-25 odd-position prefixes}\}
=820,236,724.
}
\]

Thus the phrase “25-dimensional core” must not be misread as a brute-force `2^25` problem.

The correct conclusion is:

\[
\boxed{
\text{interaction support is localized to 25 axes,}
\quad
\text{but those axes still have a large constrained lattice.}
}
\]

A transfer/carry or extremal compression theorem is still required.

---

## 5. Small-q extremal diagnostic

As a DSD falsification check, all admissible first-crossing words were enumerated for `q<=20`.

For each `q`:

1. compute its exact dangerous dimension `h(q)`;
2. group words by their first `h(q)` odd-position coordinates;
3. within every group compare the safe-tail minimizers of the canonical start `x` and descent margin `z=x-y`.

No group with disjoint minimizer sets was found through `q=20`.

This is **FINITE DIAGNOSTIC ONLY**.

It does not prove the global Dangerous-Core Extremal Reduction.  In particular, the first record with `h(q)=3` occurs later at `q=29`, outside this exhaustive diagnostic range.

---

## 6. Dependency split

### SAFE without ternary coverage

For this fixed numerical pair `(A,q)`:

- the logarithmic localization;
- `h(q)=25`;
- the admissible first-25 prefix count;
- all existing one-coordinate and mixed-difference identities.

### CONDITIONAL on repaired `F_map^cover`

The implication

\[
\text{hypothetical minimal counterexample}
\Longrightarrow
(A,q)=(217976794617,137528045312)
\]

because the stronger start floor `V_33+1` is selector-coverage dependent.

### UNIVERSAL fallback

Without that coverage, the repository retains the weaker R1 branch based on the independent paradoxical-start frontier and mechanical envelope, giving the existing lower odd-event scale above approximately

\[
5.395570552\times10^9.
\]

No fixed 25-axis conclusion is claimed for that whole universal branch.

---

## 7. Next target

The correct next theorem remains a support-aware safe-tail contraction:

> After fixing the first 25 dangerous odd-position coordinates at the current fixed cell, integrate the remaining safe tail without enumerating all completions, while retaining a certified lower envelope for the descent margin.

The existing edgewise co-order theorem alone is insufficient to assert a common global minimizer.  A valid proof needs one additional ingredient, for example:

1. a unique-sink/monotonicity theorem on the constrained safe-tail lattice;
2. an interval/carry transfer that bounds `x` and `z` jointly;
3. or a direct contradiction showing that any safe-tail completion capable of lowering `z` must also lower `x` past the canonical-address floor.

Until such an ingredient is proved, the 25-axis localization is a strong reduction but not terminal closure.

---

## 8. Regression certificate

`collatz/src/r1_current_resonance_dangerous_core_certificate.py`

uses exact `Fraction` arithmetic for the logarithmic inequalities and an exact dynamic program for the `820,236,724` admissible-prefix count.
