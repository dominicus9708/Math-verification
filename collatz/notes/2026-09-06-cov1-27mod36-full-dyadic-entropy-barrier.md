# COV-1: the `27 mod 36` progression has full dyadic suffix entropy

Date: 2026-09-06

Status: **SAFE EXACT BARRIER.**  The first unresolved recursive-sufficiency progression left by the Ansari induction audit,

\[
36\mathbb N_0+27,
\]

is not thin in the dyadic parity coordinate.  After its forced first two shortcut parity bits, it realizes every finite parity suffix.  Consequently no proof that relies only on a fixed finite shortcut-parity prefix and forward first descent can certify the entire progression.  This does not prove that the progression is non-recursive; it identifies the proof mechanism that cannot suffice.

---

## 1. Reduced coordinate

Write

\[
N=36k+27=4Y+3,
\qquad
Y=9k+6.
\]

For every `r>=1`, multiplication by `9` is invertible modulo `2^r`. Therefore

\[
\boxed{
k\pmod{2^r}
\longmapsto
Y=9k+6\pmod{2^r}
}
\]

is a bijection.

Equivalently, as `k` runs through one complete set modulo `2^r`, the integers `36k+27` run through every residue class modulo `2^(r+2)` that is congruent to `3 mod 4`.

Status: **SAFE ALGEBRA.**

---

## 2. Parity interpretation

Under the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

an integer `N=4Y+3` has first two parity bits `11`.

The classical parity-vector bijection identifies the remaining residue `Y mod 2^r` with the next `r` parity bits.  Since Section 1 shows that `Y` runs over every residue modulo `2^r`, the progression `36k+27` realizes every length-`r` suffix after the fixed head `11`.

Thus

\[
\boxed{
\{\text{parity prefixes of }36k+27\text{ of length }r+2\}
=
\{11w:w\in\{0,1\}^r\}.
}
\]

Status: **SAFE FULL-SUFFIX THEOREM.**

---

## 3. Explicit all-ones obstruction at every finite depth

For every `L>=2`, solve

\[
9k\equiv-7\pmod{2^{L-2}}.
\]

There is a unique solution modulo `2^(L-2)` because `9` is odd.

For such `k`,

\[
36k+27
=4(9k+7)-1
\equiv-1\pmod{2^L}.
\]

Hence the first `L` shortcut parity bits are all `1`.

Along an all-odd prefix,

\[
T(x)=\frac{3x+1}{2}
\]

iterates exactly to

\[
\boxed{
T^j(N)
=
\frac{3^j(N+1)-2^j}{2^j}
=
\left(\frac32\right)^j(N+1)-1.
}
\]

For every positive `N` and `j>=1`,

\[
T^j(N)>N.
\]

Therefore, for every proposed finite depth `L`, there is an infinite residue subclass of `36N_0+27` having no forward descent during the first `L` shortcut steps.

Thus

\[
\boxed{
\text{no fixed finite shortcut-parity depth can prove all }36k+27\text{ recursive by first descent.}
}
\]

Status: **SAFE BARRIER.**

---

## 4. Relation to the failed `F_1 -> F_2` coverage step

The 2026-09-06 recursive-sufficiency audit reduced the first missing ternary-core obligation to

\[
36\mathbb N_0+27\text{ recursive?}
\]

because the companion class `36N_0+31` has the exact smaller merge

\[
32k+27
\to48k+41
\to72k+62
\to36k+31.
\]

The present theorem explains why the remaining `27` class does not collapse under the same kind of bounded parity-prefix search: its free parameter supplies full dyadic suffix entropy.

This is consistent with the broader DSD picture.  The missing theorem is genuinely **cross-base/global**, not a finite binary-prefix omission.

---

## 5. What the barrier does not say

The theorem does **not** show any of the following:

1. that some `36k+27` fails the Collatz conjecture;
2. that the progression is not recursive;
3. that no finite undirected merge certificate exists using additional arithmetic structure;
4. that no growing-depth proof can work;
5. that the original ternary core cannot be recursively sufficient by another argument.

It only rejects the route

\[
\boxed{
\text{fixed finite dyadic prefix}
+\text{forward first-descent test}
\Longrightarrow
\text{full }27\bmod36\text{ recursion}.
}
\]

---

## 6. DSD audit

### SAFE

- `k -> 9k+6 mod 2^r` is bijective for every `r`.
- Every parity suffix occurs after the forced `11` head.
- An all-ones prefix of arbitrary finite length occurs in the progression.
- Such a prefix has no descent during that finite window.

### OPEN

- universal recursion of `36N_0+27`;
- a cross-base or undirected-merge proof of that recursion;
- repaired recursive-sufficiency of all original ternary `F_n`.

### REJECTED ROUTE

- closing COV-1 by merely increasing one fixed binary-prefix depth.

---

## 7. Regression certificate

`collatz/src/cov1_27mod36_dyadic_bijection_certificate.py`

checks finite representatives of the bijection and explicit all-ones cylinder construction.  The finite loops are regression evidence; Sections 1--3 are the algebraic proof.

---

## 8. Next target

The next COV-1 calculation must exploit information that the free dyadic suffix does not erase.  Natural surviving coordinates are:

1. the fixed `3^2 | N` condition of the progression;
2. exact undirected merge/backtrace arithmetic;
3. growing-depth root-globalized conditions;
4. a direct corrected analysis of the general ternary removed layer `F_n\F_(n+1)`.

A pure fixed-depth parity automaton is now pruned from the proof tree.
