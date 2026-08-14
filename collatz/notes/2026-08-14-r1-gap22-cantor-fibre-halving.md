# R1 gap-22 localization and uniform Cantor-fibre halving

Date: 2026-08-14

Status: **exact current-resonance gap bound + exact suffix/ternary cross-base fibre theorem**. It is the first current-R1 result in this project where the renewal gap turns a fixed odd-event suffix address into a uniform factor-two restriction on the low ternary selector fibre. It does not by itself halve the entire m=44 block, because the suffix address may vary with the candidate.

Use the unique current R1 coefficient pair

\[
(A,H)
=(217,976,794,617,
137,528,045,312).
\]

Let

\[
N'=N+g
\]

be the next renewal floor, with

\[
\boxed{g\in4\mathbb Z_{>0}.}
\]

Write the first-crossing correction as

\[
c=c_{\rm chr}-\eta,
\]

where `eta` is the Christoffel displacement defect.

## 1. Gap bound below 3^22

The exact endpoint identity is

\[
\boxed{c=(P-1)N+Pg,\qquad P>1.}
\]

Hence

\[
Pg<c,
\qquad
\boxed{g<c.}
\]

The Denjoy--Koksma mechanical bound gives

\[
\boxed{
c_{\rm chr}
\le\frac{H}{6\ln2}+\frac13.}
\]

The phase-adaptive two-place theorem gives the exact current-resonance defect-count floor

\[
\boxed{r_*\ge26,909,266,900.}
\]

The run-average defect inequality gives

\[
\boxed{
\eta\ge\frac5{48}r_*.
}
\]

Therefore

\[
\begin{aligned}
g
&<c_{\rm chr}-\eta\\
&\le
\frac{H}{6\ln2}+\frac13
-\frac5{48}(26,909,266,900).
\end{aligned}
\]

Using a rigorous rational lower bound for `ln 2` from its positive atanh series gives the exact comparison

\[
\boxed{
g<30,265,456,191<3^{22}.}
\]

Since

\[
3^{22}=31,381,059,609,
\]

the whole renewal gap is represented without wrap by its residue modulo `3^22`.

Because `g` is a positive multiple of four, write

\[
\boxed{g=4k.}
\]

Then

\[
\boxed{1\le k<3^{21}.}
\]

## 2. The last 22 odd events determine the endpoint modulo 3^22

Let

\[
a_i
\]

be the accumulated binary time immediately before the `i`-th odd event, so the full affine correction numerator is

\[
R=
\sum_{i=0}^{H-1}
3^{H-1-i}2^{a_i}.
\]

For `j=1,...,22`, put

\[
S_j:=A-a_{H-j},
\]

the total binary time contained in the final `j` odd-event suffix.

Modulo `3^22`, only the final 22 odd-event terms of `R` survive. Since

\[
N'
=\frac{3^HN+R}{2^A},
\]

and `H>22`,

\[
\boxed{
N+g
\equiv
\sum_{j=1}^{22}
3^{j-1}2^{-S_j}
\pmod{3^{22}}.
}
\]

Thus a fixed final-22 valuation suffix determines one endpoint residue

\[
\boxed{Y\equiv N+g\pmod{3^{22}}.}
\]

No earlier parity information enters this residue.

## 3. Low-22 ternary coordinate of the m=44 core

For a candidate in Ansari's m=44 recursively-sufficient block,

\[
N=
4\left(
3^{44}+
\sum_{i=0}^{43}a_i3^i
\right)+3,
\qquad a_i\in\{0,1\}.
\]

Modulo `3^22`, all terms above digit 21 disappear:

\[
\boxed{
N\equiv4S+3\pmod{3^{22}},
}
\]

where

\[
\boxed{
S=\sum_{i=0}^{21}a_i3^i
\in C_{22},
}
\]

and

\[
C_{22}:=
\left\{
\sum_{i=0}^{21}a_i3^i:a_i\in\{0,1\}
\right\}.
\]

The set has

\[
\boxed{|C_{22}|=2^{22}.}
\]

## 4. Gap equation in normalized ternary coordinates

Let `4^{-1}` denote the inverse of four modulo `3^22` and define

\[
\boxed{
Z_Y:=4^{-1}(Y-3)\pmod{3^{22}}.
}
\]

Since `Y=N+g`, `N=4S+3`, and `g=4k`,

\[
\boxed{
Z_Y\equiv S+k\pmod{3^{22}}.
}
\]

The gap bound gives

\[
1\le k<3^{21}.
\]

Therefore, for one fixed suffix residue `Y`, compatible low-22 Cantor coordinates `S` must lie in one cyclic interval of length strictly less than

\[
\boxed{3^{21}.}
\]

## 5. Cantor interval lemma

Put

\[
C_{21}:=
\left\{
\sum_{i=0}^{20}a_i3^i:a_i\in\{0,1\}
\right\}.
\]

Then

\[
\boxed{
C_{22}=C_{21}\ \dot\cup\ (3^{21}+C_{21}).
}
\]

Also

\[
C_{21}\subset
\left[0,\frac{3^{21}-1}{2}\right].
\]

### Lemma
Every ordinary interval of length `<3^21` contains at most `2^21` points of `C_22`.

If the interval meets only one of the two displayed copies of `C_21`, the claim is immediate.

If it meets both, write it as `[x,x+K]` with `K<3^21`, where the first intersection is a tail of `C_21` and the second becomes, after translation by `-3^21`, an initial segment of the same `C_21`.

The translated upper endpoint is

\[
y=x+K-3^{21}<x.
\]

Hence the two subsets correspond to

\[
C_{21}\cap[x,\infty)
\]

and

\[
C_{21}\cap(-\infty,y],
\]

which are disjoint subsets of one `C_21`. Their combined cardinality is therefore at most

\[
|C_{21}|=2^{21}.
\]

A cyclic interval modulo `3^22` of length `<3^21` cannot exploit the outer wrap to do better, because the empty arc from the maximum point of `C_22` back to zero has length greater than `3^21`.

Thus

\[
\boxed{
\max_{I:\ |I|<3^{21}}
|C_{22}\cap I|
\le2^{21}.
}
\]

The bound is sharp: an interval containing the complete first copy `C_21` attains `2^21`.

## 6. Uniform fibre-halving theorem

For every fixed final-22 odd-event suffix address `Y`, the admissible low ternary coordinates `S` lie in a cyclic interval of length `<3^21`.

By the Cantor interval lemma,

\[
\boxed{
\#\{S\in C_{22}:S\text{ compatible with }Y\}
\le2^{21}.
}
\]

Since `|C_22|=2^22`,

\[
\boxed{
\text{every fixed final-22 suffix fibre removes at least one half of the low-22 ternary selectors.}
}
\]

The upper 22 ternary selectors `a_22,...,a_43` do not enter this modulus, so the same statement lifts fibrewise to the full m=44 core: for each fixed suffix address, at most `2^43` of the `2^44` selector assignments can satisfy the renewal-gap condition.

## 7. Why this differs from the earlier shallow cross-mass filters

Earlier low-depth 2-adic and 3-adic filters were nearly statistically independent when intersected on the m=44 selector core. Their percentages therefore mostly multiplied without producing strong anti-alignment.

The present theorem is different. The common variable is the **same exact renewal gap**:

\[
\boxed{
\text{final parity suffix}
\to Y=N+g\pmod{3^{22}}
\to g=4k
\to\text{low ternary interval constraint}.
}
\]

Thus the factor-two loss is deterministic inside each fixed suffix fibre; no mixing or independence assumption is used.

## 8. Limitation and next target

This theorem does **not** imply that the whole m=44 block is globally halved, because different candidate parity words may realize different final-22 suffix residues `Y`. The union of their allowed half-Cantor fibres may cover much more than one half of the block.

The next hard target is therefore finite and precise:

> compress the set of final-22 odd-event suffix residues realizable by the current R1 critical language, and bound the union of their Cantor intervals.

If the realizable suffix-address family can be represented by a small Euclidean/Hensel state set rather than by arbitrary residues modulo `3^22`, the fibrewise `1/2` contraction can be promoted to a genuine global m=44 reduction.
