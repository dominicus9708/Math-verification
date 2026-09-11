# MATH-073 — exact dyadic-resolution Bellman lemma

Date: 2026-09-12

Status: `EXACT RESOLUTION LEMMA / PARTIAL BELLMAN POTENTIAL / FIRST-CELL OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-073 does not close `2<=r<=13`.
- It formalizes the exact trade between missing penalty and consumed dyadic source resolution.

## 1. Exact source-count coordinate

Let one exact source cylinder be represented inside a finite ordinary-source interval by

\[
t\equiv a\pmod{2^h}.
\]

Let

\[
M=M(a,h)
\]

be the number of ordinary source anchors in that interval satisfying the congruence.

Refining by one more exact parity bit replaces the modulus `2^h` by `2^{h+1}` and chooses one of the two child residues

\[
a\pmod{2^{h+1}},
\qquad
 a+2^h\pmod{2^{h+1}}.
\]

The parent lifts alternate between the two children. Therefore their counts are exactly a floor/ceiling split:

\[
M_0+M_1=M,
\]

\[
\boxed{
M_i\le\left\lceil\frac M2\right\rceil.
}
\]

No parity randomness assumption is present; this follows from the exact dyadic congruence refinement.

## 2. Resolution height

Define

\[
\boxed{
R(M)=\lceil\log_2 M\rceil
}
\]

for `M>=1`.

If `M>=2`, then for every nonempty child

\[
M'\le\left\lceil\frac M2\right\rceil.
\]

Let `R=ceil(log2 M)`. Since `M<=2^R`,

\[
M'\le2^{R-1}.
\]

Hence

\[
\boxed{
R(M')\le R(M)-1.
}
\]

Thus every exact parity refinement consumes at least one unit of resolution height until the source class is singleton.

For `ell` consecutive exact refinements before singleton handoff,

\[
M_{j+\ell}\le\left\lceil\frac{M_j}{2^\ell}\right\rceil,
\]

and consequently the resolution height drops by at least `ell` whenever the entire segment remains resolution-active.

## 3. Bellman potential

Use the first-cell slope target

\[
\lambda=\frac{19}{503}.
\]

Define

\[
\boxed{
H_R(s)=-\lambda R(M(s)).
}
\]

Consider one exact resolution-active unit transition `s -> s'` with penalty increment `p>=0`.

The Bellman reduced cost is

\[
p-\lambda+H_R(s')-H_R(s).
\]

Using `R-R'>=1`,

\[
\begin{aligned}
p-\lambda+H_R(s')-H_R(s)
&=p-\lambda+\lambda(R-R')\\
&\ge p\\
&\ge0.
\end{aligned}
\]

Therefore

\[
\boxed{
\text{every resolution-active exact parity edge is Bellman-safe under }H_R.
}
\]

This statement is independent of how small the actual paid penalty increment is.

## 4. Interpretation

MATH-072 identified the analytic penalty atom as

\[
p=\frac{\Omega-\rho}{3}.
\]

MATH-073 supplies the complementary address-side resource.

If `p` is too small to pay the target slope locally, exact dyadic refinement still consumes source uncertainty.
The potential term

\[
\lambda(R-R')
\]

pays at least one slope unit for every such refinement until singleton resolution.

Thus the repeated empirical pattern

\[
\text{small penalty}
\longrightarrow
\text{higher address resolution}
\longrightarrow
\text{singleton handoff}
\]

has an exact Bellman formulation.

## 5. Relation to the 73-bit source ceiling

MATH-061 established the coarse first-cell source-resolution fact that at 73 dyadic bits there is at most one ordinary source anchor in the relevant source window.

Equivalently, the initial resolution height needed by the current finite first-cell source calculation satisfies the conservative bound

\[
\boxed{R\le73.}
\]

Therefore the resolution potential has bounded range

\[
\boxed{
-73\lambda\le H_R\le0.
}
\]

This gives a maximum resolution-potential endpoint overhead of 73 slope units.

## 6. Comparison with the existing 89-step additive allowance

MATH-060 keeps the conservative additive overhead

\[
C=89
\]

in the target

\[
\mathcal P_K\ge\lambda(K-89).
\]

MATH-073 does **not** claim that the historical constant 89 was derived from source resolution.
It only observes that the certified resolution-potential range fits strictly inside that available allowance:

\[
\boxed{73<89}.
\]

Numerically in step units the difference is

\[
\boxed{89-73=16.}
\]

Thus, if the remaining non-resolution transitions can be covered with at most the residual 16-step overhead (or by an independent terminal argument), the existing first-cell allowance is large enough to absorb the entire resolution potential.

That final implication is an OPEN target, not a result of MATH-073.

## 7. Important state distinction

`M` in this lemma is the count of exact same-integer **source anchors** in one dyadic cylinder.

It must not be silently replaced by a post-merge AP-union multiplicity.
MATH-070 and MATH-071 may merge target AP representations for computational efficiency; such merging can obscure source ancestry.

The Bellman lemma is therefore attached to the source-lineage coordinate, not to an arbitrary merged target representation.

This distinction is required by the DSD audit.

## 8. Consequence for r=14--17 comparison

The different closure methods now separate into two coordinates:

### Analytic coordinate

From MATH-072,

\[
S=1+\Sigma-\rho,
\qquad
\rho=2^{-u}\Omega,
\qquad
p=(\Omega-\rho)/3.
\]

### Address coordinate

From MATH-073,

\[
R=\lceil\log_2 M\rceil,
\qquad
R'\le R-1
\]

until singleton resolution.

A natural current state skeleton is therefore

\[
\boxed{
(S,\rho,\Omega,R,\text{exact dyadic address class}).
}
\]

The first four coordinates have explicit update or monotonicity laws.
The remaining open problem is to quotient the exact address class strongly enough that post-resolution/singleton behavior can be certified without enumerating every ordinary integer.

## 9. What remains open

MATH-073 does not prove:

- that `H_R` alone satisfies the complete first-cell Bellman system;
- that the remaining 16-step allowance is sufficient;
- that singleton states can all be closed symbolically;
- that the depth-41 carry state remains bounded at arbitrary depth;
- closure of `2<=r<=13`;
- first-cell emptiness;
- the Collatz conjecture.

The next target is to combine the MATH-051 bounded-carry/Hensel dominance state with `H_R`, so that singleton or near-singleton address classes can be compared symbolically rather than enumerated.

## 10. Regression

The companion script verifies for every

\[
2\le M\le1,000,000
\]

that both floor/ceiling child counts satisfy

\[
R(M')\le R(M)-1.
\]

The universal result is the algebraic argument above; the finite regression is an implementation check.

## Reproducibility

`collatz/src/2026_09_12_math073_resolution_bellman_lemma.py`
