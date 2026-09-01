# A0 s=1 Route-B — integer source/defect coordinate

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Purpose

The source/defect danger frontier was written as pairs

\[
(r,\eta).
\]

The normalized defect \(\eta\) is rational, with a denominator depending on
the current one-count.  That is mathematically harmless but unnecessarily
awkward for a large exact DP.

The affine source identity eliminates this rational coordinate.

Source:

`collatz/src/A0_s1_routeB_integer_defect_numerator_certificate.py`

---

## 2. Target correction at fixed rank

Let

\[
a_1<a_2<\cdots
\]

be the characteristic target one positions.

For the first \(q\) target ranks define

\[
\boxed{
C_q^*
=
\sum_{r=1}^q
3^{q-r}2^{a_r}.
}
\]

For a strict target-dominance candidate prefix \(W\) with the same current
one-count \(q\), its correction is \(C(W)\), and

\[
\eta
=
\frac{C_q^*-C(W)}{3^q}
\ge0.
\]

---

## 3. Affine source identity

For the candidate prefix channel

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

the correction identity is

\[
C(W)=2^h y-3^q r.
\]

Therefore

\[
3^q\eta
=
C_q^*-C(W)
=
C_q^*+3^q r-2^h y.
\]

Define

\[
\boxed{
N
:=
3^q\eta
=
C_q^*+3^q r-2^h y.
}
\]

Then

\[
\boxed{N\in\mathbf Z_{\ge0}.}
\]

The membership-defect coordinate is therefore an integer numerator.

---

## 4. Exact one-step update

### Next bit `0`

The one-count remains \(q\), and the affine channel update cancels exactly, so

\[
\boxed{N'=N.}
\]

### Next bit `1`

The new rank is \(q+1\).  Its target position is \(a_{q+1}\), and

\[
C_{q+1}^*=3C_q^*+2^{a_{q+1}}.
\]

The new integer numerator satisfies

\[
\boxed{
N'
=
3N+2^{a_{q+1}}-2^h.
}
\]

Strict target dominance gives

\[
h\le a_{q+1},
\]

so the added term is nonnegative.

Dividing by \(3^{q+1}\) recovers the earlier normalized increment formula.

---

## 5. Dyadic source coupling

Reducing the affine identity modulo \(2^h\) gives

\[
\boxed{
N
\equiv
C_q^*+3^q r
\pmod{2^h}.
}
\]

Equivalently,

\[
r
\equiv
-\,C_q^*3^{-q}
+N3^{-q}
\pmod{2^h}.
\]

Thus the source residue and membership defect are not independent axes.
They lie on one affine 2-adic relation.

This is a structural coupling only.  It does not imply that ordinary real
ordering of \(r\) determines ordinary ordering of \(N\); the dyadic projection
is not a monotone real map.

---

## 6. Danger frontier in integer form

At fixed layer, all histories in one exact control key have the same \(q\).
Hence

\[
\eta_1\le\eta_2
\iff
N_1\le N_2.
\]

The exact danger frontier can therefore be stored as

\[
\boxed{
\mathcal F_{r,N}
=
\operatorname{ParetoMin}\{(r,N)\}.
}
\]

rather than rational \((r,\eta)\).

The transition preserves the order:

- every common parameter step adds the same amount to \(r\);
- a `0` leaves \(N\) unchanged;
- a `1` maps \(N\mapsto3N+\text{same constant}\), which is strictly increasing.

Therefore coordinatewise danger dominance in \((r,N)\) is permanent under
common future refinements.

For the physical gate one reconstructs

\[
\eta=\frac{N}{3^q}.
\]

---

## 7. Computational consequence

The former state needed exact rational additions such as

\[
\frac{2^{a_r}-2^h}{3^r}.
\]

The integer form needs only

- integer multiplication by `3`;
- addition/subtraction of powers of `2`;
- comparison of nonnegative integers.

This is especially useful for a large Pareto-frontier implementation and for
exact hashing/caching.

It also aligns the defect coordinate directly with the ordinary correction
numerator used in the projective and residue calculations.

---

## 8. Regression

The certificate exhausts all strict target-dominance binary prefixes through

\[
h\le10.
\]

It checks:

- `153` affine numerator identities;
- `153` dyadic congruence identities;
- nonnegativity for every legal prefix;
- every legal one-step `0/1` numerator recurrence.

All arithmetic is integer exact.

---

## 9. DSD audit

### EXACT / CLOSED

- normalized prefix defect has an exact nonnegative integer numerator;
- the integer coordinate is reconstructed from source residue and endpoint;
- its bitwise recurrence is exact;
- source residue and defect obey one affine dyadic congruence;
- the source/defect danger frontier can use `(r,N)` with no rational state.

### NOT INFERRED

- real monotonicity from the dyadic congruence;
- bounded danger-frontier width;
- automatic closure of any 14-root family;
- Collatz.

---

## 10. Updated bottleneck

The exact adaptive state can now be implemented as

\[
\boxed{
(\text{active control},\text{interval payload},
\mathcal F_{r,N})
}
\]

with purely integer frontier arithmetic.

The unresolved quantitative problem is no longer coordinate correctness.  It
is the growth of the number of undominated frontier points and the effect of
adding the remaining checkpoint/projective predicates to the exact control
key.
