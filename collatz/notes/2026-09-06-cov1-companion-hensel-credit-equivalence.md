# COV-1: companion defects as exact Hensel correction credits

Date: 2026-09-06

Status: **SAFE EXACT EQUIVALENCE / GLOBAL COV-1 OPEN.**  The two universally useful companion defects `D=1` and `D=2` are not independent new congruence phenomena.  They reduce to exact correction-successor problems for the same standard affine constant `C(w)`.  In particular, `D=2` is exactly a same-length, same-weight, full-Hensel unit-credit competitor.  This merges the new companion calculus with the existing root-Hensel machinery.

---

## 1. Exact correction constant is injective at fixed weight

Let a length-`h`, weight-`s` binary word have odd positions

\[
0\le d_0<\cdots<d_{s-1}<h.
\]

Its affine correction is

\[
C(w)=\sum_{a=0}^{s-1}3^{s-1-a}2^{d_a}.
\]

The least odd position is recovered from

\[
\boxed{d_0=v_2(C(w)).}
\]

Indeed the `a=0` term has exact valuation `d_0`, while every later term has strictly larger `2`-adic valuation.  Subtracting

\[
3^{s-1}2^{d_0}
\]

and repeating recovers `d_1`, then `d_2`, and so on.

Therefore, for fixed `s`, the exact integer `C(w)` uniquely determines the word's odd positions and hence the word itself.

Status: **SAFE UNIQUENESS LEMMA.**

---

## 2. `D=1` companion has forced prefix `111`

Assume the forward word `w` begins with `1`, so

\[
C(w)\text{ is odd}.
\]

Let

\[
s=|w|_1.
\]

A `D=1` companion must have exact correction

\[
C(z)=8C(w)+3^{s+2}.
\]

Because `8C(w)` is divisible by `8` while `3^(s+2)` is odd,

\[
v_2(C(z))=0,
\]

so the first odd position of `z` is `0`.

Remove its contribution `3^(s+1)`.  The residual is

\[
8C(w)+2\cdot3^{s+1},
\]

which has `2`-adic valuation exactly `1`.  Thus the second odd position is `1`.

Remove `2\cdot3^s`.  The residual is

\[
8C(w)+4\cdot3^s,
\]

which has valuation exactly `2`.  Hence the third odd position is `2`.

Therefore every `D=1` companion is forced to begin

\[
\boxed{111.}
\]

Write

\[
z=111y,
\]

where `y` has length `h` and weight `s-1`.

The correction contributed by the initial `111` in a total word with `s+2` ones is

\[
3^{s+1}+2\cdot3^s+4\cdot3^{s-1}
=19\cdot3^{s-1},
\]

while shifting the suffix by three positions multiplies its correction by `8`.  Hence

\[
C(z)=19\cdot3^{s-1}+8C(y).
\]

Equating with the `D=1` target

\[
8C(w)+27\cdot3^{s-1}
\]

gives

\[
\boxed{
C(y)=C(w)+3^{s-1}.
}
\]

Thus

\[
\boxed{
D=1\text{ companion exists}
\iff
\exists y:\ |y|=h,\ |y|_1=s-1,
\ C(y)=C(w)+3^{s-1}.
}
\]

By Section 1 such `y`, when it exists, is unique.

---

## 3. `D=2` companion has forced prefix `011`

For `D=2`,

\[
C(z)=8C(w)+2\cdot3^{s+2}.
\]

The first valuation is

\[
v_2(C(z))=1,
\]

so position `0` is even and the first odd occurs at position `1`.

Subtracting `2\cdot3^(s+1)` leaves

\[
8C(w)+4\cdot3^{s+1},
\]

with valuation exactly `2`, so the second odd position is `2`.

Therefore every `D=2` companion begins

\[
\boxed{011.}
\]

Write

\[
z=011y,
\]

where `y` has length `h` and weight exactly `s`.

The two leading odd contributions are

\[
2\cdot3^{s+1}+4\cdot3^s
=10\cdot3^s.
\]

Thus

\[
C(z)=10\cdot3^s+8C(y).
\]

Equating with

\[
8C(w)+18\cdot3^s
\]

gives

\[
\boxed{
C(y)=C(w)+3^s.
}
\]

Therefore

\[
\boxed{
D=2\text{ companion exists}
\iff
\exists y:\ |y|=h,\ |y|_1=s,
\ C(y)=C(w)+3^s.
}
\]

Again `y` is unique whenever it exists.

---

## 4. Exact identification with a Hensel unit credit

The existing root-Hensel relation at length `h`, weight `s` groups words by

\[
C(y)\equiv C(w)\pmod{3^s}.
\]

For the `D=2` companion,

\[
C(y)-C(w)=3^s.
\]

Hence the Hensel credit is exactly

\[
\boxed{
\Delta
=\frac{C(y)-C(w)}{3^s}
=1.
}
\]

So

\[
\boxed{
D=2\text{ companion}
\iff
\text{same-length, same-weight full-Hensel competitor with unit credit }\Delta=1.
}
\]

This is an exact equivalence, not a heuristic analogy.

The `D=1` companion is a neighboring-weight analogue:

\[
|y|_1=s-1,
\qquad
C(y)-C(w)=3^{s-1}.
\]

Thus both useful companion defects are **unit correction-successor events**, one within the same Hensel weight and one one weight lower.

---

## 5. Consequence for existing root-max machinery

The root-Hensel class-max recursion already propagates, for every class `(s,r)`, the maximum exact correction

\[
M_h(s,r).
\]

Therefore `D=2` companion detection does not require a separate reverse-word enumeration.  For a given word `w`, it is enough to determine whether the exact correction value

\[
C(w)+3^s
\]

is realized by another length-`h`, weight-`s` word.

This is stronger than merely asking whether `w` is non-maximal:

- non-maximality means some credit `Delta>=1` exists;
- `D=2` requires the specific unit credit `Delta=1`.

Hence

\[
\boxed{
D=2\Longrightarrow\text{not root-Hensel maximal},
}
\]

but the converse is not asserted.

For minimal-counterexample applications in the root-safe depth range, any `D=2` companion is therefore already incompatible with root-Hensel maximality.  For the unconditional COV-1 progression problem, however, the companion theorem remains valuable because it gives an explicit smaller merge without assuming minimality.

---

## 6. Reinterpretation of the infinite `1^r00` seed family

For

\[
w_r=1^r00,
\qquad r\ge4,
\]

we have

\[
C(w_r)=3^r-2^r.
\]

### `D=2`

The suffix after the forced companion prefix `011` is

\[
y_r^{(2)}=0\,1^{r-1}01,
\]

and satisfies

\[
\boxed{
C(y_r^{(2)})=C(w_r)+3^r.
}
\]

Thus the infinite `D=2` seed family is an explicit family of unit full-Hensel credits.

### `D=1`

The suffix after the forced prefix `111` is

\[
y_r^{(1)}=00\,1^{r-2}01,
\]

with

\[
\boxed{
C(y_r^{(1)})=C(w_r)+3^{r-1}.
}
\]

This is the corresponding lower-weight unit successor.

---

## 7. Computational consequence

Because exact correction constants are injective at fixed weight, companion detection can be implemented without:

- enumerating reverse words;
- storing a `3^(s+2)` residue table;
- Fourier inversion over the whole ternary group.

For `D=1,2`, one computes one target exact integer and asks whether it is a valid length/weight correction constant.

A deterministic valuation decoder recovers the unique candidate odd positions, if they exist.

This does not solve the classification of all possible companion defects `D`; it sharply simplifies the two defects already known to imply universal positive descent.

---

## 8. DSD audit

### SAFE

1. Exact correction constant is injective at fixed weight.
2. `D=1` companion begins `111` and is equivalent to a lower-weight unit successor.
3. `D=2` companion begins `011` and is equivalent to a same-weight unit Hensel credit.
4. `D=2` implies failure of root-Hensel maximality.
5. No reverse-word enumeration is needed to test `D=1,2`.

### OPEN

1. Whether every useful companion certificate can be reduced to `D=1` or `D=2`.
2. Classification of higher positive/negative defects satisfying the branch descent interval.
3. Whether every non-eventually-one survivor path must eventually encounter a unit correction successor.
4. Full COV-1.

### PROHIBITED UPGRADES

1. Do not replace root-Hensel non-maximality by `D=2`; credits larger than one may exist without a unit successor.
2. Do not infer that every companion has `D=1` or `2` from finite experiments.
3. Do not use root-minimality arguments to prove unconditional recursive sufficiency unless the explicit smaller merge is also supplied.

---

## 9. Regression certificate

`collatz/src/cov1_companion_hensel_credit_equivalence_certificate.py`

checks the equivalences by exact finite enumeration for all binary words through length `9`.  The proofs in Sections 2--4 are algebraic and independent of that finite range.

---

## 10. Next target

The most useful next step is to combine the **unit-credit companion test** with the existing streaming Hensel class table.

Rather than constructing all companion words, propagate for each exact correction state whether the unit successors

\[
C+3^s
\]

and

\[
C+3^{s-1}
\]

are realizable at the same binary depth.

This produces a prefix-free unit-credit survivor language.  The terminal question becomes:

> Can an infinite parity path beginning with `11`, containing infinitely many zeroes, avoid both the same-weight and lower-weight unit-successor events forever?

If not, every remaining infinite path is eventually all odd and is excluded by the ghost terminal lemma.
