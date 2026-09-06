# COV-1: exact recursive 3-adic subcylinders inside `36k+27`

Date: 2026-09-06

Status: **FINITE SYMBOLIC PROGRESS / GLOBAL COV-1 OPEN.**  After the full-dyadic-entropy barrier ruled out closure by any fixed shortcut-parity depth, the missing progression was attacked from the `3`-adic side using exact undirected merge/backtrace words.  A positive family of infinite subprogressions is proved recursive, but they cover only a small part of the full `27 mod 36` progression.  This is not a proof of the Collatz conjecture.

---

## 1. Setup

Let

\[
x=36k+27.
\]

Its first shortcut iterate is

\[
y=T(x)=54k+41.
\]

Starting from `y`, use reverse shortcut edges

\[
E(z)=2z,
\]

and, whenever integral,

\[
O(z)=\frac{2z-1}{3}.
\]

Each reverse edge gives a genuine predecessor under the shortcut Collatz map:

\[
T(E(z))=z,
\qquad
T(O(z))=z.
\]

Thus if a reverse word sends `y` to some positive `m<x`, then

\[
m\leftrightarrow x
\]

and `x` is recursive.

---

## 2. Leading-coefficient contraction test

Suppose a reverse word has

- total length `K`;
- `q` occurrences of `O`.

Ignoring the affine constants, it multiplies `y` by

\[
\frac{2^K}{3^q}.
\]

Since

\[
y\sim\frac32x,
\]

the leading multiplier relative to `x` is

\[
\boxed{
\frac{2^{K-1}}{3^{q-1}}.
}
\]

Therefore an infinite affine subprogression can be universally sent below `x` only if

\[
\boxed{
2^{K-1}<3^{q-1}.
}
\]

For each fixed `q` there are only finitely many word lengths `K` satisfying this inequality.  Hence exhaustive enumeration through a fixed maximum `q` is finite and exact.

---

## 3. Exact 3-adic refinement rule

During a reverse word, write the current integer on a cylinder

\[
k=3^rt+a
\]

as

\[
z=At+B.
\]

The `E` edge gives

\[
(A,B)\mapsto(2A,2B).
\]

For an `O` edge we require

\[
At+B\equiv2\pmod3.
\]

If `3|A`, this is either valid on the whole cylinder or impossible on the whole cylinder according to `B mod 3`.

If `3\nmid A`, exactly one residue

\[
t\equiv c\pmod3
\]

works.  Refining

\[
t=3t'+c
\]

increases the `k`-cylinder depth from `r` to `r+1` and yields another exact affine state.

Thus every reverse word determines either no admissible `k`, or one exact `3`-adic cylinder.

Status: **SAFE SYMBOLIC CALCULUS.**

---

## 4. First explicit infinite recursive subprogression

The reverse word

\[
\boxed{EEOEOEOOOOOO}
\]

has

\[
K=12,
\qquad
q=8,
\]

and

\[
2^{11}=2048<2187=3^7.
\]

Its exact integrality conditions reduce to

\[
\boxed{k\equiv172\pmod{243}.}
\]

Write

\[
k=243t+172.
\]

Then

\[
x=36k+27
=8748t+6219.
\]

Following the reverse word from `T(x)` produces

\[
\boxed{m=8192t+5823.}
\]

The difference is

\[
x-m
=556t+396>0
\]

for every `t>=0`.

Therefore

\[
\boxed{
36(243t+172)+27
\text{ is recursive for every }t\ge0.
}
\]

This closes exactly `1/243` of the free `k` parameter by one universal affine merge certificate.

---

## 5. Exhaustive reverse-word scan through `q<=16`

The regression certificate enumerates **every** reverse word satisfying

\[
q\le16,
\qquad
2^{K-1}<3^{q-1},
\]

solves its exact `3`-adic integrality cylinder, and keeps it only if its final affine predecessor satisfies

\[
0<m<x
\]

for every free parameter value.

After removing cylinders contained in a coarser already-certified cylinder, the surviving prefix-free family is:

\[
\begin{array}{c|r}
\text{3-adic depth }r&\text{number of certified cylinders}\\\hline
5&1\\
7&5\\
9&25\\
10&131\\
12&580
\end{array}
\]

for a total of

\[
\boxed{742}
\]

pairwise disjoint `3`-adic cylinders.

Their exact natural density in the `k` parameter is

\[
\begin{aligned}
\delta_{16}
&=
\frac1{3^5}
+\frac5{3^7}
+\frac{25}{3^9}
+\frac{131}{3^{10}}
+\frac{580}{3^{12}}\\
&=
\boxed{\frac{5836}{531441}}\\
&\approx
\boxed{0.010981463605555462}.
\end{aligned}
\]

Hence at least about `1.098%` of the `k`-classes are now covered by explicit universal smaller-merge words within this bounded reverse-word search.

Status: **EXACT FINITE-SYMBOLIC CERTIFICATE.**

The percentage is not an asymptotic theorem in `q`; it must not be extrapolated.

---

## 6. Relation to the dyadic barrier

The previous note proved that `36k+27` has full dyadic suffix entropy after the fixed parity head `11`.  Therefore no fixed binary-prefix depth can cover the whole progression by forward descent.

The present calculation succeeds precisely because it uses the surviving `3`-adic coordinate:

\[
\boxed{
\text{full dyadic freedom}
\quad+\quad
\text{3-adic inverse integrality}
\quad\Longrightarrow\quad
\text{nontrivial exact merge cylinders}.
}
\]

This is a genuine cross-base mechanism rather than a deeper version of the rejected finite parity scan.

---

## 7. DSD audit

### SAFE

1. The reverse-edge calculus is exact.
2. The contraction condition `2^(K-1)<3^(q-1)` is an exact necessary leading-coefficient condition for a universal affine smaller merge.
3. The cylinder `k=172 mod 243` is fully recursive by the displayed affine certificate.
4. The 742 prefix-free cylinders and density `5836/531441` are exact for the exhaustive search domain `q<=16`.

### FINITE ONLY

- the number `742`;
- the density `5836/531441`;
- any trend in the number of newly discovered cylinders as `q` increases.

### OPEN

- whether the union of all such inverse-merge cylinders has density one;
- whether every `k` belongs to some finite reverse-word cylinder;
- universal recursion of `36N_0+27`;
- repaired recursive sufficiency of the original ternary `F_n` family.

### PROHIBITED UPGRADES

1. Do not infer full progression recursion from positive certified density.
2. Do not infer density-one coverage from the growth observed through `q=16`.
3. Do not identify a reverse-word search failure with a Collatz counterexample.
4. Do not restore universal ternary-core coverage until the remaining progression and higher-layer induction are proved.

---

## 8. Regression certificate

`collatz/src/cov1_27mod36_inverse_merge_cylinder_certificate.py`

reconstructs all contracting reverse words through `q=16`, performs the exact `3`-adic cylinder refinement, removes redundant cylinders, and asserts

\[
\boxed{
\#\mathcal C=742,
\qquad
\sum_{C\in\mathcal C}d(C)=\frac{5836}{531441}.
}
\]

---

## 9. Next target

The next useful question is no longer whether *some* `27 mod 36` subprogressions are recursive; that is now proved.

The target is to understand the infinite reverse-word language itself:

\[
\boxed{
\mathcal R
=
\{k:\text{some contracting admissible reverse word gives }m(k)<36k+27\}.
}
\]

The strongest possible COV-1 closure would be

\[
\boxed{\mathcal R=\mathbb N_0.}
\]

A weaker but still useful next theorem would give a recursive/automaton description of the complement in base `3`, allowing DSD to determine whether it is empty, a zero-density Cantor set, or a genuine surviving obstruction.
