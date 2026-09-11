# MATH-057 — phase-address mechanical barrier and cumulative penalty lower bound

Date: 2026-09-11
Status: `EXACT PHASE-ADDRESS BARRIER / UNIVERSAL FINITE-SCOPE LINEAR PENALTY LOWER BOUND / FIRST-CELL CLOSURE OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This result is conditional on the current first-cell ordinary-start window and on remaining before the first coefficient crossing.
- It strengthens MATH-054/MATH-056 by replacing a finite first-72 penalty statement with a cumulative lower bound that grows with prefix length.

## 1. Correction penalty in odd-position form

Let the odd-step positions of a coefficient-valid parity prefix be

\[
k_0<k_1<\cdots<k_{q-1}.
\]

Define the mechanical boundary positions

\[
p_n=n+m(n),\qquad m(n)=\lfloor n\log_2(3/2)\rfloor.
\]

Coefficient admissibility implies

\[
k_n\le p_n.
\]

The normalized correction is

\[
S(w)=\sum_{n=0}^{q-1}\frac{2^{k_n}}{3^{n+1}},
\]

while the zero-slack mechanical envelope is

\[
S_*(q)=\sum_{n=0}^{q-1}\frac{2^{p_n}}{3^{n+1}}.
\]

Hence the cumulative slack penalty is exactly

\[
\boxed{
\mathcal P(w)=S_*(q)-S(w)
=\sum_{n=0}^{q-1}\frac{2^{p_n}-2^{k_n}}{3^{n+1}}.
}
\]

This is the cumulative version of the MATH-053 event penalty.

If `u_n=p_n-k_n>0`, the n-th odd event contributes

\[
\frac{(1-2^{-u_n})\Omega_n}{3}>rac1{12},
\qquad
\Omega_n=\frac{2^{n+m(n)}}{3^n}>\frac12.
\]

Thus every positive-slack odd event costs strictly more than `1/12`.

## 2. Boundary-anchor endpoint bound

At a state with

\[
u=m(q)-d=0,
\]

we have `k=q+m(q)` and therefore

\[
\frac{3^q}{2^k}=\frac1{\Omega_q}<2.
\]

Also MATH-053 gives

\[
0\le S(w)<\frac q3.
\]

Before the first universal crossing, `q<=q_0=72,057,431,991`, and the current ordinary-start window is

\[
2^{71}<N<1364\cdot2^{61}.
\]

Therefore every `u=0` anchor endpoint obeys

\[
T^k(N)=\frac{N+S(w)}{\Omega_q}
<2\left(1364\cdot2^{61}+\frac{q_0}{3}\right)
<2^{73}.
\]

The last inequality is exact integer/rational arithmetic and is checked in the certificate.

## 3. Complete phase partition for a zero-penalty tail

Let

\[
\theta=\log_2(3/2),
\qquad
x=\{q\theta\},
\qquad
\Omega=2^{-x}.
\]

Starting from `u=0`, a continuation with no positive-slack odd event is unique for a fixed phase. Its r-th future odd position relative to the anchor is

\[
\boxed{
r+m(r)+\mathbf 1[\Omega\le\tau_r],
}
\]

where

\[
\boxed{
\tau_r=\frac{3^r}{2^{r+m(r)+1}}.
}
\]

Thus all length-L zero-penalty factors are constant on the exact rational phase intervals obtained by cutting `(1/2,1)` at the finitely many thresholds `tau_r`.

For length L the certificate uses all thresholds `r<=L`; there are exactly `L+1` resulting intervals in the audited range. No floating-point phase approximation is used.

## 4. Same-phase ordinary-address compatibility

For one length-L mechanical factor let `R` be the unique start residue modulo `2^L` that realizes that parity factor.

For `L>=73`, the endpoint bound in Section 2 implies the actual endpoint is strictly below `2^73<=2^L`. Hence

\[
\boxed{T^k(N)=R}
\]

rather than merely being congruent to `R mod 2^L`.

At the same anchor,

\[
N=\Omega R-S,
\qquad
0\le S<q/3\le q_0/3.
\]

Therefore a necessary condition for one phase interval to be compatible with the first-cell ordinary-start window is that the interval contain an `Omega` satisfying

\[
\boxed{
2^{71}<\Omega R<1364\cdot2^{61}+\frac{q_0}{3}.
}
\]

This condition is checked by exact rational interval intersection for every phase interval.

## 5. Exact barrier

Canonical table:

`collatz/results/2026-09-11-phase-address-mechanical-barrier.tsv`.

The number of compatible phase/address intervals is

| L | compatible intervals |
|---:|---:|
| 73 | 15 |
| 74 | 7 |
| 75 | 5 |
| 76 | 4 |
| 77 | 2 |
| 78 | 2 |
| 79 | 0 |

The special initial phase `q=0`, `Omega=1` is checked separately and is also incompatible at L=79.

Therefore

\[
\boxed{
\text{every zero-penalty mechanical segment beginning at }u=0
\text{ has length at most }78.
}
\]

This is a same-integer phase/address obstruction. It does not use probability or empirical frequency.

## 6. Paid-cluster decomposition

Call an odd event with `u>0` a **paid odd event**. Let `P` be the number of paid odd events in a coefficient-valid prefix of length `K`.

Between returns to `u=0`, paid events occur in clusters.

A paid cluster begins after a zero-penalty odd event has raised the slack from `0` to `1`. If a cluster contains `r>=1` paid odd events, each paid odd can increase the slack by at most one, while every even step decreases it by exactly one. Returning to `u=0` therefore needs at most

\[
1+r
\]

even steps after the opening zero-cost odd event. After counting that opening event as the final step of the preceding mechanical segment, the remaining cluster length is at most

\[
2r+1.
\]

If there are `C` paid clusters, then `C<=P`. There are `C+1` zero-penalty mechanical segments, each of length at most 78. Hence

\[
K\le78(C+1)+(2P+C)
\le81P+78.
\]

Therefore

\[
\boxed{
P\ge\left\lceil\frac{K-78}{81}\right\rceil
}
\]

for `K>78`.

## 7. Cumulative penalty lower bound

Each paid odd event contributes strictly more than `1/12`. Combining Sections 5 and 6 gives

\[
\boxed{
\mathcal P_K>
\frac1{12}
\left\lceil\frac{K-78}{81}\right\rceil.
}
\]

This is the first current lower bound on the MATH-053 correction penalty that grows linearly with prefix length without enumerating depths or slack-event budgets.

At the last coefficient-valid prefix before the first universal crossing,

\[
K=A_0-1=114,208,327,603,
\]

so

\[
P\ge1,409,979,353
\]

and hence

\[
\boxed{
\mathcal P_{A_0-1}>
\frac{1,409,979,353}{12}
\approx117,498,279.4167.
}
\]

The final crossing step can only add nonnegative penalty, so the same lower bound applies to the terminal first-cell correction penalty.

## 8. Relation to MATH-056

MATH-056 defined

\[
V(K)=\min\{\text{first-72 penalty}:\text{same integer survives coefficient test through }K\}.
\]

That value is useful for finite optimization but its objective is frozen to the first 72 steps. Consequently a permanently positive additive law for `V(K)` is not the natural asymptotic target.

The proof-facing cumulative value should instead be

\[
\boxed{
W(K)=\min\{\mathcal P_K(N):N\text{ is a same-integer first-cell candidate coefficient-valid through }K\}.
}
\]

MATH-057 proves the unconditional finite-scope lower bound

\[
\boxed{
W(K)>
\frac1{12}
\left\lceil\frac{K-78}{81}\right\rceil.
}
\]

This supersedes the earlier suggestion that the first-72 value `V(K)` itself should exhibit a positive linear slope.

## 9. What remains open

The MATH-057 slope is not yet large enough by itself to close the first universal cell. The next task is to strengthen the per-block cost or shorten the allowed zero-penalty segments by adding non-redundant information, especially

1. exact transition compatibility between consecutive near-maximal mechanical segments;
2. nested Hensel cross-channel constraints;
3. same-integer endpoint/minimality information beyond the scalar first-cell address window.

The correct next object is therefore a weighted macro-transition graph between `u=0` anchors, not a deeper word enumeration.

## Reproducibility

- `collatz/src/2026_09_11_phase_address_mechanical_barrier_certificate.py`
- `collatz/results/2026-09-11-phase-address-mechanical-barrier.tsv`
