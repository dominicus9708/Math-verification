# R1 gap-44 full Cantor-fibre compression

Date: 2026-08-14

Status: **exact current-resonance fixed-suffix fibre theorem**. It strengthens the earlier mod-`3^22` half-fibre result by using the full `m=44` ternary selector coordinate modulo `3^44`. For one fixed final-44 odd-event suffix address, at most `2^21` of the `2^44` m44 selector assignments can satisfy the current renewal-gap bound. It does not globalize over all suffix addresses and does not prove Collatz.

Use the unique current R1 coefficient pair

\[
(A,H)
=(217,976,794,617,
137,528,045,312).
\]

For the next renewal floor write

\[
N'=N+g,
\qquad
\boxed{g\in4\mathbb Z_{>0}}.
\]

From the existing current-resonance gap theorem,

\[
\boxed{g<3^{22}}.
\]

Write

\[
\boxed{g=4k},
\]

so

\[
\boxed{1\le k<3^{21}}.
\]

## 1. Full m44 ternary coordinate

For the recursively-sufficient m44 core,

\[
N=
4\left(
3^{44}+
\sum_{i=0}^{43}a_i3^i
\right)+3,
\qquad a_i\in\{0,1\}.
\]

Put

\[
\boxed{
S:=\sum_{i=0}^{43}a_i3^i
\in C_{44},
}
\]

where

\[
C_m:=
\left\{
\sum_{i=0}^{m-1}a_i3^i:
a_i\in\{0,1\}
\right\}.
\]

Modulo `3^44`,

\[
\boxed{N\equiv4S+3\pmod{3^{44}}}.
\]

The full selector family has

\[
\boxed{|C_{44}|=2^{44}}.
\]

## 2. Final 44 odd events determine the endpoint modulo 3^44

Let `a_i^{time}` denote accumulated binary time immediately before the `i`-th odd event and, for `j=1,...,44`, put

\[
S_j^{time}:=A-a_{H-j}^{time}.
\]

Modulo `3^44`, only the last 44 terms of the affine correction numerator survive. Hence the final-44 valuation suffix determines one endpoint residue

\[
\boxed{
Y\equiv N+g
\equiv
\sum_{j=1}^{44}
3^{j-1}2^{-S_j^{time}}
\pmod{3^{44}}.
}
\]

No earlier parity information enters this residue.

## 3. Normalized gap equation

Let `4^{-1}` be the inverse of four modulo `3^44` and define

\[
\boxed{
Z_Y:=4^{-1}(Y-3)\pmod{3^{44}}.
}
\]

Since

\[
Y=N+g,
\qquad
N\equiv4S+3,
\qquad
g=4k,
\]

we obtain

\[
\boxed{
Z_Y\equiv S+k\pmod{3^{44}}.
}
\]

For one fixed final-44 suffix address `Y`, the compatible `S` therefore lie in one cyclic interval of length strictly less than

\[
\boxed{3^{21}}.
\]

## 4. General ternary Cantor interval lemma

### Lemma
For integers `m>r>=0`, every ordinary interval `I` of length `<3^r` satisfies

\[
\boxed{|C_m\cap I|\le2^r}.
\]

The same bound holds for cyclic intervals modulo `3^m`.

### Proof
Split the selector set into low and high ternary digits:

\[
C_m
=
\bigsqcup_{T\in C_{m-r}}
\left(3^rT+C_r\right).
\]

Each copy has convex-hull width

\[
\max C_r-\min C_r
=
\frac{3^r-1}{2}
<\frac{3^r}{2}.
\]

Distinct translates start at multiples of `3^r`, and the ordered start points differ by at least `3^r`. Hence an interval of length `<3^r` can meet at most two consecutive copies.

If it meets only one copy, the bound is immediate.

If it meets two consecutive copies, translate the first to `C_r`. The intersection with the first copy is a terminal subset

\[
C_r\cap[x,\infty),
\]

and after translating the second copy back by its start offset, its intersection is an initial subset

\[
C_r\cap(-\infty,y]
\]

with `y<x`, because the total interval length is strictly less than the separation of the two starts. These two subsets of one `C_r` are disjoint. Their total cardinality is therefore at most

\[
|C_r|=2^r.
\]

For the cyclic case modulo `3^m`, note that

\[
\max C_m=rac{3^m-1}{2},
\]

so the outer gap from `max C_m` back to zero has length greater than `3^{m-1}` and therefore greater than `3^r`. A cyclic interval of length `<3^r` cannot gain extra points from both sides of that outer gap beyond the ordinary-interval bound.

This proves the lemma.

## 5. Full-selector fixed-suffix theorem

Apply the lemma with

\[
\boxed{m=44,\qquad r=21}.
\]

For one fixed final-44 suffix residue `Y`, the compatible full ternary selector coordinate `S` lies in a cyclic interval of length `<3^21`. Therefore

\[
\boxed{
\#\{S\in C_{44}:S\text{ compatible with }Y\}
\le2^{21}.
}
\]

Since

\[
|C_{44}|=2^{44},
\]

the retained fraction inside one suffix fibre is at most

\[
\boxed{2^{-23}}.
\]

Equivalently,

\[
\boxed{
\text{every fixed final-44 odd-event suffix address removes at least }
1-2^{-23}
\text{ of the m44 selector assignments.}
}
\]

This is much stronger than the earlier mod-`3^22` statement, which retained at most `2^43` full assignments after lifting the low-22 half-fibre restriction. Here the full selector coordinate is used at once, so only `2^21` assignments remain in one fixed suffix fibre.

## 6. Why this still is not a global m44 reduction

The local suffix-address universality theorem remains decisive: the coefficient-record condition alone can realize every unit endpoint residue modulo `3^Q` for every finite `Q`, including `Q=44`.

Therefore one cannot multiply the `2^-23` fibre factor by a small record-only count of suffix residues. The missing global theorem must couple the suffix address to information not contained in the local record condition, for example

- the global skew/defect cost;
- the strengthened dyadic ordinary-start address;
- the same-integer canonical lift condition;
- or a phase-adaptive minimal-predecessor state carried across growing Euclidean scales.

The useful new reduction is nevertheless exact:

\[
\boxed{
\text{once a final-44 suffix fibre is fixed, the entire }2^{44}
\text{ selector family collapses to at most }2^{21}\text{ candidates.}
}
\]

Thus the next R1 target is no longer to improve a per-fibre ternary estimate. It is to control how many genuinely distinct final-44 suffix fibres can coexist with the same global dyadic/defect state.
