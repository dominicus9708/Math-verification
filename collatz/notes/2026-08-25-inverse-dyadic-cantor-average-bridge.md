# Inverse-dyadic Cantor average bridge for the Stage 4 spectral target

Date: 2026-08-25

Status: **proved inverse-orbit truncated-product lemma + external-theorem bridge audit; triangular boundary assembly remains open.**

This note records a new external input relevant to the remaining Stage 4 odd-shell correlation problem and extracts the part that can be transferred rigorously to the repository's 3-adic reciprocity coordinate. It does not claim a proof of the Collatz conjecture.

## 1. External averaged Fourier estimate

Prasuna Bandi, *Averaged Fourier Estimates and Dyadic Approximation on the Cantor set*, arXiv:2606.27034v2 (2026), proves the following estimate for the natural middle-third Cantor measure `mu`.

Put

\[
\gamma=\frac{\log2}{\log3},
\qquad
\beta=1-\gamma.
\]

For `H>=3`, choose `K` by

\[
3^K\le H<3^{K+1}.
\]

Then for every nonzero integer `q`, uniformly in `M>=0`,

\[
\sum_{M<n\le M+H}|\widehat\mu(q2^n)|
\ll
H^\gamma 3^{\beta\min(\nu_3(q),K)}.
\]

The proof uses the exact order

\[
\operatorname{ord}_{3^r}(2)=2\cdot3^{r-1}
\]

and the truncated product

\[
P_K(q)=\prod_{r=1}^K
\left|\cos\frac{2\pi q}{3^r}\right|.
\]

Reference: arXiv:2606.27034v2, Lemma 7.

## 2. Why inverse powers are equally accessible

The repository boundary reciprocity identity contains inverse powers of two modulo powers of three. This is not an obstruction to Bandi's finite residue argument.

Because `2` is a primitive root modulo every `3^r`, its inverse is also a generator of the same finite cyclic unit group. Therefore

\[
\{2^{-n}\bmod3^r:n=0,\ldots,\varphi(3^r)-1\}
=(\mathbb Z/3^r\mathbb Z)^\times.
\]

The forward and inverse orbits have exactly the same period and residue multiplicities. Hence Bandi's residue-counting proof has an inverse-orbit analogue for the truncated product.

## 3. Explicit inverse-orbit truncated-product lemma

### Lemma

Let `H>=3` and choose `K` by

\[
3^K\le H<3^{K+1}.
\]

For nonzero integer `q`, put

\[
a=\min(\nu_3(q),K).
\]

For an inverse exponent `n`, let `q2^{-n} mod 3^K` denote multiplication by the inverse of `2^n` in the appropriate unit quotient after the common factor `3^a` is removed. Then for every interval of `H` consecutive exponents,

\[
\boxed{
\sum_{M<n\le M+H}
P_K(q2^{-n})
\le
\frac{11}{2}
H^\gamma3^{\beta a}.
}
\]

Here `P_K` is periodic modulo `3^K`, so only the residue class is relevant.

### Proof

If `a=K`, use `P_K<=1`. Then

\[
\sum P_K\le H.
\]

Since `H<3^{K+1}` and `3^K<=H`,

\[
\frac{H}{H^\gamma3^{\beta K}}
=\left(\frac{H}{3^K}\right)^\beta
<3^\beta=\frac32,
\]

so the displayed `11/2` constant is more than sufficient.

Now assume `a<K` and write

\[
q=3^a q_0,
\qquad3\nmid q_0.
\]

The inverse orbit of `q_0` modulo `3^{K-a}` has period

\[
T=2\cdot3^{K-a-1}.
\]

Therefore any one unit residue is hit at most

\[
1+\frac HT
<1+\frac{3^{K+1}}{2\cdot3^{K-a-1}}
=1+\frac92\,3^a
\le\frac{11}{2}3^a
\]

times in an interval of length `H`.

Group the inverse exponents by their unit residue `y mod 3^{K-a}`. Bandi's finite cosine-tree lemma gives

\[
\sum_{0\le y<3^{K-a}}P_K(3^a y)
\le2^{K-a}.
\]

Consequently

\[
\sum_{M<n\le M+H}P_K(q2^{-n})
\le
\frac{11}{2}3^a2^{K-a}.
\]

Finally

\[
2^K=(3^K)^\gamma\le H^\gamma
\]

and

\[
\left(\frac32\right)^a=3^{\beta a},
\]

which proves the claim.

No statistical equidistribution assumption is used.

## 4. Low-valuation frequencies have sublinear inverse-orbit mass

Fix any

\[
0\le\theta<1.
\]

If

\[
\nu_3(q)\le\theta K,
\]

then the lemma gives

\[
\sum P_K(q2^{-n})
\ll
H^\gamma3^{\beta\theta K}.
\]

Since `3^K<=H<3^{K+1}`,

\[
3^{\beta\theta K}\ll H^{\beta\theta},
\]

and therefore

\[
\boxed{
\sum P_K(q2^{-n})
\ll
H^{\gamma+\beta\theta}
=H^{1-\beta(1-\theta)}
=o(H).
}
\]

Thus every fixed valuation fraction `theta<1` gives a power-saving average along the inverse dyadic orbit.

By Markov's inequality, for any fixed `epsilon>0`, the number of exponents in the interval with

\[
P_K(q2^{-n})\ge\epsilon
\]

is at most

\[
O_\epsilon\!\left(
H^{1-\beta(1-\theta)}
\right).
\]

So the bad inverse-orbit times have zero density in this low-valuation regime.

## 5. High 3-adic valuation is the natural exceptional frequency channel

The only way the previous power saving can degenerate is when

\[
\nu_3(q)\approx K.
\]

This is exactly the kind of arithmetic exceptional family required by the repository's spectral-exception splitting lemma.

Moreover high-valuation frequencies are sparse in any ordinary integer frequency interval: the fraction divisible by `3^a` is at most approximately `3^{-a}` (up to endpoint rounding). Hence one obtains the desired qualitative split:

1. **good frequencies:** `nu_3(q)<=theta K`, where inverse-dyadic Cantor products have a power-saving averaged bound;
2. **exceptional frequencies:** `nu_3(q)>theta K`, which are arithmetically sparse and can be routed to the Beatty-boundary / predecessor-residue channel.

This complements the exact support-size barrier showing that global selector `L^2` mixing cannot hold once dyadic resolution exceeds selector depth.

## 6. Exact connection to the repository boundary reciprocity coordinate

For a mixed plateau-pair boundary coordinate, the repository has proved

\[
\frac{[3^{-\ell}]_{2^m}}{2^m}
=
\frac{[-2^{-m}]_{3^\ell}}{3^\ell}
+
\frac1{3^\ell2^m}.
\]

Thus a boundary cosine factor is governed by a residue on the same inverse-dyadic orbit modulo `3^ell` that appears in the lemma above.

Furthermore, after using the absolute-cosine period and the inverse of `2 mod 3^ell`, the main rational phase can be represented by a top-level Cantor factor at a residue proportional to

\[
k2^{-(m+1)}\pmod{3^\ell}.
\]

As the dyadic remaining length `m` decreases, this residue moves forward by multiplication by `2` in the 3-adic unit group. Hence the orbit direction is fully compatible with the averaged Fourier method.

## 7. Audit limitation: the triangular assembly lemma is still missing

The external/inverse-orbit theorem does **not** yet close Stage 4.

Bandi's `P_K(q)` is a complete nested Cantor product over

\[
r=1,\ldots,K
\]

at one fixed truncation depth `K`.

A Beatty-boundary cube instead contributes selected factors

\[
\left|\cos\left(
\pi k\frac{[3^{-\ell_j}]_{2^{m_j}}}{2^{m_j}}
\right)\right|
\]

with both

\[
\ell_j
\quad\text{and}\quad
m_j
\]

changing along the boundary word. The one-ordinal `ell_j` also depends on the boundary path/fibre.

Therefore the following implication is **not yet proved**:

\[
\boxed{
\text{inverse-orbit average for fixed }P_K
\Longrightarrow
\text{uniform decay of every Beatty boundary cube product}.
}
\]

The missing statement is a triangular assembly/comparison lemma that groups a positive fraction of the varying boundary factors into complete or dominated Cantor-product blocks without reversing the inequality.

This direction is delicate because

\[
P_K(q)\le
\left|\cos\frac{2\pi q}{3^K}\right|,
\]

so smallness of the full product alone does not upper-bound a single top-level factor.

## 8. Refined next target

The current Stage 4 spectral route is now reduced to:

> **Triangular Cantor-boundary assembly target.** Use the deterministic plateau-pair cube structure and the relation between `(m_j,ell_j)` to prove that, outside a sparse high-`3`-adic-valuation frequency family, a positive-density subfamily of the boundary cosine factors has cumulative logarithmic loss. Equivalently, bound the boundary cube product by an object to which the inverse-orbit averaged Cantor estimate applies.

If this target yields any positive linear boundary spectral loss strong enough to make the odd-shell repair rate smaller than `7/50`, the current Stage 4 criterion closes. A sublinear cumulative repair estimate would be stronger than necessary.

## 9. References and related repository results

External:

- Prasuna Bandi, *Averaged Fourier Estimates and Dyadic Approximation on the Cantor set*, arXiv:2606.27034v2, 2026, especially Lemmas 4, 6, and 7.

Repository:

- `2026-08-13-spectral-exception-splitting-lemma.md`;
- `2026-08-13-selector-energy-support-barrier.md`;
- `2026-08-13-deterministic-plateau-pair-cube-decomposition.md`;
- `2026-08-13-boundary-riesz-dyadic-ternary-reciprocity.md`;
- `2026-08-25-stage4-second-window-and-odd-shell-reduction.md`.
