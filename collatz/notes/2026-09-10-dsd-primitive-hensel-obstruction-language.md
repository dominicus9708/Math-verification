# DSD structural checkpoint II — primitive Hensel obstruction language

Date: 2026-09-10
Status: `EXACT RIGHT-IDEAL STRUCTURE / d<=2 SYMBOLIC CLASSIFICATION / FINITE d=6..8 MOTIF EXTRACTION / GENERAL COMPLETENESS OPEN`

This note supplements `2026-09-10-dsd-depth-normalized-hensel-structure.md`.
MATH-050 remains the latest completed full-depth audit; this is not MATH-051.

## 1. Newly pruned states are primitive forbidden prefixes

Let a parity prefix `w` have q odd steps and correction C(w).  Suppose an unrestricted competitor `v` has the same exact Hensel class and larger correction,

\[
C(v)-C(w)=m3^q>0.
\]

Append the same suffix `u` to both words.  If `u` contains r odd steps, every odd suffix step multiplies the correction difference by 3 and every even suffix step leaves it unchanged.  Hence

\[
C(vu)-C(wu)=m3^{q+r}>0.
\]

So `wu` remains non-maximal in its exact Hensel class.

Therefore the Hensel-nonmaximal language is upward closed under right extension: it is a right ideal in the parity-word prefix tree.

The states counted by

\[
R_{k,d}=P_{k,d}-S_{k,d}
\]

are precisely first-failure states in the nested process.  They can be viewed as a prefix-free basis of **primitive Hensel obstruction motifs**.  Once a primitive motif is rejected, none of its descendants ever needs to be reconsidered as a nested survivor.

This is the language-theoretic meaning of the MATH-013 downstream-stable dominance rule.

## 2. d=0 and d=1

For d=0 there is only the all-odd word, so no same-(q,residue) competition exists.

For d=1, let the unique even position be `a`, with `0<=a<=k-1` and q=`k-1`.  Direct odd-block summation gives

\[
C_a=3^{k-1}-2^k+2^a3^{k-a-1}.
\]

For `a<b`,

\[
C_a-C_b
=2^a3^{k-b-1}\left(3^{b-a}-2^{b-a}\right).
\]

The factor in parentheses is nonzero modulo 3, so

\[
v_3(C_a-C_b)=k-b-1<k-1=q.
\]

Thus two distinct d=1 words can never have the same correction modulo `3^(k-1)`.

Hence the d=1 exact Hensel class map is injective and Hensel pruning is identically zero wherever the coefficient gate admits the word.

## 3. Complete d=2 collision classification

Let the two even positions be `a<b`; q=`k-2`.  Exact block summation gives

\[
C_{a,b}=3^{k-2}-2^k
+2^a3^{k-a-2}
+2^b3^{k-b-1}.
\]

A 3-adic valuation comparison shows that distinct same-class pairs can occur only between an adjacent pair and a non-adjacent pair with the matching valuation.  Comparing the remaining 3-adic unit then forces the non-adjacent first even position to be zero.

The complete collision family is therefore

\[
\boxed{\{0,j\}\quad\leftrightarrow\quad\{j,j+1\}},
\qquad 1\le j\le k-2.
\]

For every such pair,

\[
\boxed{C_{0,j}-C_{j,j+1}=3^{k-2}}.
\]

Thus `{j,j+1}` is the lower-correction representative and loses with translation credit 1.

In the nested prefix process, `{j,j+1}` first becomes a complete forbidden prefix at depth `j+2`.  Every later all-odd extension is already excluded by downstream stability.  Consequently the only newly appearing d=2 obstruction at depth k is

\[
\boxed{E=\{k-2,k-1\}},
\]

so, throughout the coefficient-admissible regime beginning at k>=6,

\[
\boxed{R_{k,2}=1}.
\]

This upgrades the previously finite d=2 pattern to an exact within-model statement.  It is not a Collatz proof.

## 4. d=3,4,5: no primitive defect observed

Direct fixed-d exact enumeration found no newly pruned states for d=3,4,5 throughout k=8..41.  Arbitrary Hensel class collisions do exist in these d-layers; the statement is only that no new first-failure motif survives the nested prefix filter in this audited interval.

This is finite evidence.  No arbitrary-k zero-defect theorem for d=3,4,5 is claimed here.

## 5. Right-edge odd-insertion operator

For an even-position set E of a length-k word, define `Phi_k(E)` by inserting an odd bit immediately before the final two positions.  In even-position coordinates,

\[
\Phi_k(E)=\{e\in E:e<k-2\}
\cup\{e+1:e\in E,\ e\ge k-2\}.
\]

This keeps d fixed and increases q by one.

Empirically, the primitive obstruction sets obey a particularly simple finite-depth recursion for small fixed d.

## 6. d=6: exact finite set recursion and regular motif families

For every transition k->k+1 with k=32..40,

\[
\boxed{\mathcal R_{k+1,6}=\Phi_k(\mathcal R_{k,6})\sqcup B^{(6)}_{k+1}},
\]

with exactly

\[
|B^{(6)}_{k+1}|=2.
\]

Moreover, exhaustive enumeration shows that for every k=32..41 the complete d=6 newly-pruned set is exactly the union of two parametric families

\[
A_{k,n}=\{n-2,n,n+1,n+2,n+3,k-2\},
\]

\[
B_{k,n}=\{n-3,n,n+1,n+2,n+3,k-2\},
\]

for

\[
10\le n\le k-6.
\]

Corresponding unrestricted competitors are

\[
A'_{k,n}=\{0,1,n-2,n,k-2,k-1\},
\]

\[
B'_{k,n}=\{0,1,n-3,n+1,k-2,k-1\}.
\]

Exact odd-block algebra gives

\[
C(A'_{k,n})-C(A_{k,n})
=C(B'_{k,n})-C(B_{k,n})
=3^{k-5}
=3\cdot3^{k-6}.
\]

Thus every displayed pair is an exact q=`k-6` Hensel collision with credit 3.

In parity-symbol form the candidate families are regular-pattern families

\[
O^{a}EOE^4O^{b}EO,\qquad a\ge8,\ b\ge0,
\]

and

\[
O^{a}EO^2E^4O^{b}EO,\qquad a\ge7,\ b\ge0.
\]

At fixed length k, each family contributes `k-15` words, so

\[
\boxed{R_{k,6}=2k-30}
\]

throughout the exact audited interval k=32..41.

The collision identity is symbolic; arbitrary-k **completeness** of these two families as the only primitive d=6 motifs is still open beyond the audited interval.

## 7. d=7: six boundary motifs per depth

For every transition k->k+1 with k=32..40, exhaustive set comparison gives

\[
\boxed{\mathcal R_{k+1,7}=\Phi_k(\mathcal R_{k,7})\sqcup B^{(7)}_{k+1}},
\]

with

\[
\boxed{|B^{(7)}_{k+1}|=6}.
\]

Therefore the finite exact counts satisfy

\[
R_{k,7}=6k-103
\]

for k=32..41, including the forward depth-41 check `R_{41,7}=143`.

Writing the new depth as K, the six newly born candidate motifs are

\[
E_1=\{2,K-9,K-6,K-5,K-4,K-3,K-2\},
\]
\[
E_2=\{2,K-8,K-6,K-5,K-4,K-3,K-2\},
\]
\[
E_3=\{K-12,K-9,K-6,K-5,K-4,K-3,K-2\},
\]
\[
E_4=\{K-11,K-8,K-7,K-6,K-4,K-3,K-2\},
\]
\[
E_5=\{K-11,K-8,K-6,K-5,K-4,K-3,K-2\},
\]
\[
E_6=\{K-10,K-8,K-7,K-6,K-4,K-3,K-2\}.
\]

Exact unrestricted competitors can be chosen as

\[
M_1=\{1,4,5,K-9,K-5,K-2,K-1\},
\]
\[
M_2=\{1,4,5,K-8,K-6,K-2,K-1\},
\]
\[
M_3=\{0,1,K-12,K-5,K-4,K-2,K-1\},
\]
\[
M_4=\{0,1,K-11,K-7,K-5,K-2,K-1\},
\]
\[
M_5=\{0,1,K-11,K-6,K-5,K-2,K-1\},
\]
\[
M_6=\{0,1,K-10,K-8,K-5,K-2,K-1\}.
\]

For q=`K-7`, block algebra gives

\[
C(M_i)-C(E_i)=2\cdot3^{K-7}\quad(i=1,2),
\]

and

\[
C(M_i)-C(E_i)=3\cdot3^{K-7}\quad(i=3,4,5,6).
\]

Hence the six birth motifs split into two credit-2 and four credit-3 exact Hensel collisions.

As with d=6, finite set recursion is established through K=41; arbitrary-depth completeness remains open.

## 8. d=8 and the onset of a hierarchy

At d=8 the exact count ledger gives

\[
R_{k,8}=23k-436
\]

for k=32..40.

Direct primitive-set comparison was additionally performed for 32->33 and 33->34.  In both transitions every old motif is carried by `Phi_k` with no loss and exactly 23 new motifs appear:

\[
\mathcal R_{k+1,8}=\Phi_k(\mathcal R_{k,8})\sqcup B^{(8)}_{k+1},
\qquad |B^{(8)}|=23
\]

for these two checked transitions.

This strongly suggests the same birth-and-propagation mechanism, but the full set recursion through depth 40 has not yet been independently regenerated in this checkpoint.

The d=9 ledger similarly has constant first difference 83 across k=32..40, while d=10 becomes quadratic after an activation irregularity at k=32.  A working hypothesis is that the degree of the defect count reflects the number of free placement parameters in primitive motif families.  This is a hypothesis, not a theorem.

## 9. Reverse exact residue recursion

Use the depth-normalized residue

\[
\rho\equiv2^{-k}C\pmod{3^q}.
\]

Forward maps are

\[
E:\rho\mapsto\rho/2\pmod{3^q},
\]

\[
O:\rho\mapsto(3\rho+1)/2\pmod{3^{q+1}}.
\]

For a target class `(q,d,rho)`, the even predecessor is unique:

\[
\boxed{\rho_E=2\rho\pmod{3^q}}.
\]

An odd predecessor exists iff

\[
\boxed{\rho\equiv2\pmod3},
\]

and then it is unique:

\[
\boxed{\rho_O=(2\rho-1)/3\pmod{3^{q-1}}}.
\]

Thus a target exact class has at most one parent from each parity channel.

In particular, **new odd/even class collisions can occur only in target classes with least ternary digit 2**.  Classes with `rho mod 3` equal to 0 or 1 have only the even-parent channel and therefore cannot acquire a new cross-channel competitor at that step once the parent class-max quotient is in force.

## 10. Demand-driven max recurrence

Let `A_{q,d}(rho)` be the maximum normalized score `x=C/2^(q+d)` among all unrestricted words in exact class rho.

Then, with absent predecessor terms omitted,

\[
\boxed{
A_{q,d}(\rho)=\max\left\{
\frac{A_{q,d-1}(2\rho)}2,
\frac{3A_{q-1,d}((2\rho-1)/3)+1}{2}
\right\}.
}
\]

The second term exists only for `rho=2 mod 3`.

A nested candidate-max channel can be propagated by the same recurrence, restricted to the static coefficient-admissible `(q,d)` region, and a target candidate class survives exactly when its candidate maximum equals `A_{q,d}(rho)`.

This is an exact demand-driven alternative to rescanning all unrestricted parity words.  Its practical memory/time advantage for the central boundary layers still has to be benchmarked; no speedup factor is claimed yet.

## 11. Computational consequence

The next-generation DSD-guided calculation should be hybrid:

1. **proved motif slices**: replace brute-force enumeration by exact primitive-obstruction formulas (d=0,1 and now d=2; d=6/7 only after arbitrary-k completeness is proved);
2. **candidate motif slices**: use motif filters as guaranteed early rejections but retain an exact fallback for unclassified states;
3. **reverse collision filter**: perform new-merge work only on normalized residue classes with least ternary digit 2;
4. **boundary zone**: preserve full exact ternary residue until a genuine quotient is proved;
5. **central computation**: benchmark demand-driven two-channel max recursion against the current tail-bucket unrestricted enumeration.

## 12. Audit limits

- finite motif recursion is not arbitrary-k completeness;
- an explicit competitor family gives a safe lower bound on pruning, not an exhaustive count unless completeness is separately proved;
- `rho mod 3 = 2` is a filter for possible **new cross-channel collisions**, not a replacement for the full `rho mod 3^q` class key;
- regularity of primitive motifs at small d does not imply a finite global obstruction basis;
- none of these results proves the Collatz conjecture.
