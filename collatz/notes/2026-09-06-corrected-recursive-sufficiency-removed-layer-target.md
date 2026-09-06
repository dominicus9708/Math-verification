# Corrected recursive-sufficiency removed-layer target

Date: 2026-09-06

Status: **SAFE SET IDENTITY + CONDITIONAL RECURSIVE-SUFFICIENCY INDUCTION TARGET.**  This note replaces the false printed auxiliary identity audited in Ansari (2025) by the exact set difference obtained directly from the definitions.  It does not prove that every removed layer is recursive and therefore does not restore universal ternary-Cantor coverage.

---

## 1. Reduced-coordinate definition

Write

\[
N=4Y+3.
\]

The ternary spine sets are

\[
F_n^Y
=
\left\{
3^n p+
\sum_{i=0}^{n-1}a_i3^i:
 p\in\mathbb N_0,
\ a_i\in\{0,1\}
\right\},
\]

and

\[
F_n=\{4Y+3:Y\in F_n^Y\}.
\]

For `p=3p'+d`, with

\[
d\in\{0,1,2\},
\]
we have

\[
Y
=
3^{n+1}p'
+d3^n
+\sum_{i=0}^{n-1}a_i3^i.
\]

The next set `F_(n+1)` consists exactly of the cases

\[
d\in\{0,1\}.
\]

Therefore the missing part is exactly the `d=2` branch.

---

## 2. Exact removed-layer theorem

Define

\[
A_n:=F_n\setminus F_{n+1}.
\]

Then directly from Section 1,

\[
\boxed{
A_n
=
\left\{
4\left(
3^{n+1}p
+2\cdot3^n
+\sum_{i=0}^{n-1}a_i3^i
\right)+3:
 p\in\mathbb N_0,
\ a_i\in\{0,1\}
\right\}.
}
\]

Modulo

\[
4\cdot3^{n+1},
\]
this is a disjoint union of exactly

\[
\boxed{2^n}
\]

arithmetic progressions, one for every lower ternary `0/1` word of length `n`.

Equivalently, in the reduced ternary expansion of `Y`, `A_n` consists exactly of numbers whose lowest ternary digit outside the already fixed lower `0/1` block is `2` at position `n`.

Status: **SAFE EXACT SET IDENTITY.**

---

## 3. Correct induction obligation

The intended recursive-sufficiency induction should not pass through the printed auxiliary equality.  Instead it should use the literal partition

\[
\boxed{F_n=F_{n+1}\ \dot\cup\ A_n.}
\]

Hence, under the standard recursive-sufficiency removal principle,

\[
\boxed{
F_n\text{ recursively sufficient}
\quad+\quad
A_n\text{ recursive}
\quad\Longrightarrow\quad
F_{n+1}\text{ recursively sufficient}.
}
\]

Conversely, if both `F_n` and `F_(n+1)` are recursively sufficient, that alone does not automatically prove every member of `A_n` recursive; the proof program therefore uses the displayed implication as the sufficient induction obligation rather than silently replacing it by a biconditional.

Status: **SAFE SUFFICIENT REDUCTION, subject to the standard definition/removal property of recursive sufficiency.**

This wording deliberately avoids overclaiming an unnecessary converse.

---

## 4. First layers

### `n=0`

There is one removed class:

\[
A_0=12\mathbb N_0+11.
\]

This is the classical first recursive removal used to pass from the odd core to the next spine layer.

### `n=1`

There are two classes:

\[
A_1
=(36\mathbb N_0+27)
\ \dot\cup\
(36\mathbb N_0+31).
\]

The second class is closed by the exact affine merge

\[
32k+27
\to48k+41
\to72k+62
\to36k+31,
\]

with

\[
32k+27<36k+31.
\]

The first class

\[
\boxed{36\mathbb N_0+27}
\]

remains the first unresolved coverage layer.

### `n=2`

There are four classes, corresponding to lower ternary sums

\[
s\in\{0,1,3,4\}.
\]

They are

\[
N
\equiv
4(18+s)+3
\pmod{108},
\]

namely

\[
\boxed{75,79,87,91\pmod{108}.}
\]

No universal recursion claim for these four classes is made here.

---

## 5. Global coverage theorem needed

The infinite ternary `0/1` core is

\[
F_\infty
:=
\bigcap_{n\ge0}F_n.
\]

To restore the previous minimal-counterexample coverage route by this spine, it is sufficient to prove

\[
\boxed{
A_n\text{ is recursive for every }n\ge0.
}
\]

Then recursive sufficiency propagates down the decreasing chain

\[
F_0\supset F_1\supset F_2\supset\cdots,
\]

and the intersection may again be used as a universal minimal-counterexample core, provided the passage to the intersection is justified by the recursive-sufficiency framework being used.

Thus the repaired coverage program is no longer an opaque auxiliary-set induction.  It is the explicit digit-`2` elimination problem:

\[
\boxed{
\text{eliminate the first ternary digit }2
\text{ at every position }n,
\text{ with arbitrary lower }0/1\text{ digits}.
}
\]

---

## 6. DSD decomposition

The coverage gate should now be written

\[
\boxed{
F_{\rm map}^{\rm cover}
=
\{\mathrm{COV}_n:n\ge0\},
}
\]

where

\[
\mathrm{COV}_n:\quad A_n\text{ is recursive}.
\]

Current status:

\[
\begin{array}{c|c}
n&\mathrm{COV}_n\\\hline
0&\textbf{CLOSED}\\
1&\textbf{PARTIAL: }31\bmod36\text{ closed, }27\bmod36\text{ open}\\
\ge2&\textbf{OPEN}
\end{array}
\]

For `COV_1`, the existing finite-symbolic inverse-merge certificate closes 742 exact `3`-adic subcylinders inside the `27 mod 36` branch, of total `k`-density

\[
\frac{5836}{531441},
\]

but this is finite-only progress and does not close the branch.

---

## 7. Structural implication for future methods

The lower `0/1` digits number `2^n`.  Therefore a proof that treats every lower word independently will reproduce an exponential layer width.

A scalable coverage proof should instead exploit a property uniform in

\[
s=\sum_{i<n}a_i3^i.
\]

The exact removed layer has affine form

\[
N
=4\cdot3^{n+1}p
+8\cdot3^n
+4s+3.
\]

Thus the natural compressed state is not the full lower word but a finite collection of residues/valuations of `s` needed by the merge mechanism.

This points toward a cross-base finite-state or `3`-adic backtrace theorem, not a separate trajectory proof for each of the `2^n` classes.

---

## 8. DSD audit labels

### SAFE

1. The exact formula for `A_n=F_n\\F_(n+1)`.
2. `A_n` has exactly `2^n` residue classes modulo `4*3^(n+1)`.
3. The `n=1` split is exactly `27,31 mod 36`.
4. The `31 mod 36` class has the displayed universal smaller merge.
5. Proving every `A_n` recursive is a sufficient repaired route to the ternary spine.

### OPEN

1. Full recursion of `A_1` because `36N_0+27` remains open.
2. `A_n` for every `n>=2`.
3. A uniform theorem in `n` and the lower ternary selector word.

### PROHIBITED UPGRADES

1. Do not replace the exact removed layer by Ansari's printed `F'_n\\A'_n` identity.
2. Do not infer higher-layer recursion from the successful `31 mod 36` affine pattern.
3. Do not call the infinite ternary core universal until the repaired coverage chain is actually established.
4. Do not convert finite inverse-word cylinder density into full `COV_1` closure.

---

## 9. Regression certificate

`collatz/src/corrected_recursive_sufficiency_removed_layer_certificate.py`

checks the exact residue identity for `0<=n<=8`.  Those loops are regression tests; Sections 1--2 are the general algebraic proof.

---

## 10. Next target

The next calculation should use the closed-form reverse-word congruence to compress the `COV_1` search, then ask whether the complement of the certified `3`-adic cylinders has a recursive automaton description.

In parallel, the same reverse-word calculus should be parameterized by

\[
(n,s),
\qquad
s=\sum_{i<n}a_i3^i,
\]

to determine which part of the mechanism is specific to `n=1,s=0` and which part generalizes to all removed layers.
