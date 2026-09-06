# COV-1 external sufficiency prior-art audit

Date: 2026-09-06

Status: **PRIOR-ART BOUNDARY / COV-1 REMAINS OPEN.**

The unresolved repaired-coverage obligation is

\[
\boxed{36\mathbb N_0+27\text{ is recursive?}}
\]

where `recursive` means that every member `n>1` merges in the undirected Collatz graph with some positive integer `m<n`.

A literature check was performed to determine whether classical sufficient-set results already imply this statement.

---

## 1. Arithmetic progressions are sufficient, but this is weaker

K. M. Monks' work on arithmetic-progressession sufficiency proves that every nonconstant arithmetic progression is a sufficient set for the `3x+1` conjecture.  Later work by K. Monks, K. G. Monks, K. M. Monks and M. Monks develops strongly sufficient sets and arithmetic-sequence distribution in the `3x+1` graph.

Thus the progression

\[
36\mathbb N_0+27
\]

is certainly within a class of arithmetic sequences known to be **sufficient / merge-sufficient** in the standard sense.

However this says that arbitrary orbits can meet/merge with an orbit represented by the progression.  It does not provide the order condition

\[
\boxed{m<n}
\]

required for recursive sufficiency of each removed integer.

---

## 2. Ansari explicitly distinguishes the notions

Ansari (2025) defines a positive integer `n>1` to be recursive when there exists a positive `m<n` with

\[
m\leftrightarrow n.
\]

A set is recursively sufficient when every element outside it is recursive in that order-sensitive sense.

The same paper explicitly notes that the theorem for recursively sufficient sets cannot simply be replaced by the older merge-sufficiency theorem for arbitrary arithmetic progressions, because the latter supplies no order-friendly guarantee on the merging representative.

Therefore

\[
\boxed{
\text{arithmetic-progression sufficiency}
\not\Rightarrow
36\mathbb N_0+27\text{ recursive}.
}
\]

This distinction is exactly the one needed by the repaired ternary induction.

---

## 3. Independent 2026 audit reaches the same missing class

A separate public audit of Ansari's recursive-sufficiency construction independently identifies

\[
F_1\setminus F_2
=(36\mathbb N_0+27)\cup(36\mathbb N_0+31)
\]

and supplies the same type of explicit smaller merge for the `31 mod 36` class.

It leaves

\[
\boxed{36\mathbb N_0+27}
\]

as the unresolved first recursive-sufficiency obligation and reports no corrigendum on the inspected journal page at the date of that audit.

This agrees with the independent DSD residue audit in the present repository.

---

## 4. Consequence for the proof program

The following shortcut is rejected:

\[
36\mathbb N_0+27\text{ is an arithmetic progression}
\Longrightarrow
\text{it is recursive}.
\]

What the classical sufficient-set theorem can support is a **global hitting/sufficiency reformulation**, not the order-sensitive induction needed to recover the ternary `0/1` Cantor core.

Therefore COV-1 remains a genuine obligation unless one finds one of:

1. a universal smaller-merge construction for `36k+27`;
2. a different recursively sufficient spine avoiding this progression;
3. a direct minimal-counterexample coverage theorem not using the flawed ternary induction.

---

## 5. Relevant external references

- Kenneth M. Monks, *The sufficiency of arithmetic progressions for the 3x+1 Conjecture*, Proc. Amer. Math. Soc. 134 (2006), 2861--2872.
- Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, Maria Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, Discrete Mathematics 313 (2013), 468--489, DOI: 10.1016/j.disc.2012.11.019.
- Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3) (2025), 471--480, DOI: 10.7546/nntdm.2025.31.3.471-480.

The 2026 external audit located during this check is used only as corroborating prior-art audit evidence; the repository's own residue calculation remains the primary internal reason for reopening coverage.

---

## 6. DSD labels

### SAFE

- Standard arithmetic-progression sufficiency is not the same as recursive sufficiency.
- The order condition `m<n` is essential to the induction mechanism being repaired.

### OPEN

- universal recursion of `36N_0+27`;
- repaired ternary `F_n` recursive-sufficiency chain;
- an alternative order-sensitive sufficient spine.

### REJECTED

- treating Monks' arithmetic-progression sufficiency theorem as a proof of COV-1.
