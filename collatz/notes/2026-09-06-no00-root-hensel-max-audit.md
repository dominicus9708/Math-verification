# Root-`11`, no-`00` Hensel audit

Date: 2026-09-06

Status: **singleton conjecture REJECTED; class-max property FINITE ONLY through length 26.**

This note audits the symbolic hard core suggested by the finite observation that parity words beginning with `11` and containing no `00` appeared to be maximum-correction representatives of their full-Hensel classes.

Nothing here proves the Collatz conjecture.

---

## 1. Setup

For a length-`L` parity word `w` with `q` odd bits at positions

\[
0\le d_0<\cdots<d_{q-1}<L,
\]

write the standard correction

\[
\boxed{
C(w)=\sum_{j=0}^{q-1}3^{q-1-j}2^{d_j}.
}
\]

Two words of the same length and same weight are in one **full-Hensel correction class** when

\[
\boxed{C(u)\equiv C(w)\pmod{3^q}.}
\]

A word is class-maximal if no same-class word has larger correction.

For the unresolved `36k+27` root, every actual parity prefix begins with `11`.  We therefore audit the language

\[
\mathcal N_L
:=
\{w\in\{0,1\}^L:w_0w_1=11,\;00\text{ never occurs}\}.
\]

---

## 2. Singleton behavior through length 23

Exact exhaustive comparison against **all** length-`L` words of matching weight gives:

\[
\boxed{
2\le L\le23:
\quad
\text{every }w\in\mathcal N_L
\text{ occupies a singleton full-Hensel class.}
}
\]

This is a finite theorem only.

The number of audited target words is Fibonacci-sized; for example

\[
|\mathcal N_{20}|=6765,
\qquad
|\mathcal N_{23}|=28657.
\]

---

## 3. Singleton property fails first at length 24

At

\[
L=24,
\]

the word, in time order,

\[
\boxed{
w=110110110101010110110101
}
\]

has

\[
q=15,
\qquad
C(w)=74,913,815.
\]

The distinct word

\[
\boxed{
u=111111111101011000100100
}
\]

has the same length and weight and

\[
C(u)=17,518,187.
\]

Their exact difference is

\[
\boxed{
C(w)-C(u)
=57,395,628
=4\cdot3^{15}.
}
\]

Hence

\[
C(w)\equiv C(u)\pmod{3^{15}}.
\]

Therefore

\[
\boxed{
\text{root-`11` + no-`00` does NOT imply Hensel-class singleton.}
}
\]

Status: **SAFE COUNTEREXAMPLE to the singleton conjecture.**

---

## 4. The more relevant class-max property survives the collision

The length-24 collision is one-sided:

\[
C(u)<C(w).
\]

Thus `w` remains the maximum correction representative of its class.

A complete exact class-max audit was then run for all root-`11`, no-`00` targets through

\[
\boxed{L=26.}
\]

No target with a larger same-class competitor was found.

Hence the current finite status is

\[
\boxed{
L\le26:
\quad
w\in\mathcal N_L
\Longrightarrow
w\text{ is full-Hensel class-maximal}
}
\]

**FINITE ONLY.**  There is currently no general proof, and the length-24 singleton failure is a warning against promoting the finite pattern.

---

## 5. DSD interpretation

The audit separates three logically different properties:

1. **singleton:** no other same-class word exists;
2. **unit-credit-free:** no larger word differs by exactly `3^q`;
3. **class-max:** no larger same-class correction exists at any positive integer credit.

The first property is now false.

The third property is the one relevant to full root-Hensel predecessor elimination.  It remains an open theorem candidate despite the finite verification through length 26.

Therefore future work must not use

\[
\text{no-`00`}\Rightarrow\text{singleton}
\]

but may retain the finite diagnostic

\[
\text{no-`00`}\Rightarrow\text{class-max through }L=26.
\]

---

## 6. Relation to the periodic ghost `110`

The periodic symbolic ray

\[
(110)^\infty
\]

lies inside the root-`11`, no-`00` language and is coefficient-surviving, since each period has multiplier

\[
\frac{3^2}{2^3}=rac98>1.
\]

Its corresponding periodic `2`-adic start is

\[
\frac{9N+5}{8}=N
\quad\Longrightarrow\quad
N=-5.
\]

Thus even a hypothetical general class-max theorem for the no-`00` language would not by itself close the positive-integer problem: the symbolic language contains genuine nonpositive `2`-adic ghosts.

The terminal problem must still use ordinary-integer stabilization or an equivalent same-integer condition.

---

## 7. Regression certificate

`collatz/src/no00_root_hensel_max_audit.cpp`

checks:

- singleton status through `L=23`;
- the exact length-24 collision above;
- class-max status through `L=25` by default;
- class-max status through `L=26` with `--full26`.

The `L=26` run is intentionally optional because the full class table uses substantial memory.

---

## 8. Current target

The correct next question is now narrower:

\[
\boxed{
\text{Does root-`11` + no-`00` imply full-Hensel class maximality for all }L?
}
\]

Two outcomes are both useful:

- a proof would identify a large exact Hensel-hard symbolic core;
- a counterexample would further prune the proposed hard core.

Until one occurs, the property remains **OPEN with finite evidence only**.
