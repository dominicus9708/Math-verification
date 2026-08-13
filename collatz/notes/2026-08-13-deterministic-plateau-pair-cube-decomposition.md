# Deterministic plateau-pair cube decomposition of the Beatty boundary

Date: 2026-08-13

Status: **exact combinatorial theorem + exponential-prevalence bound**. This note gives a deterministic hypercube decomposition inside the Beatty coefficient-survival boundary and an exact Fourier factorization on every cube. It is a reduction for the ternary--Beatty spectral-complementarity program, not a proof of Collatz.

## 1. Beatty boundary

Put

\[
\alpha:=\log_3 2\in(1/2,1),
\qquad
b_j:=\lceil \alpha j\rceil.
\]

For a binary word `w=(w_0,...,w_{L-1})`, let

\[
q_j(w):=\sum_{i=0}^{j-1}w_i
\qquad(0\le j\le L).
\]

The coefficient-survival boundary is

\[
\mathcal B_L
:=
\{w:q_j(w)\ge b_j\ (1\le j\le L),\ q_L(w)=b_L\}.
\]

The oriented-boundary spectrum at the next barrier rise can equivalently be studied through the surviving extension set

\[
\mathcal A_L:=\{w1:w\in\mathcal B_L\}.
\]

For odd child frequencies, its normalized Fourier transform is the normalized transform of the oriented boundary.

## 2. Deterministic plateau-pair coordinates

Define the plateau-start set

\[
\boxed{
P_L:=\{0\le j\le L-2:b_{j+1}=b_j\}.
}
\]

Because `alpha>1/2`, two consecutive Beatty increments cannot both vanish. Hence

\[
\boxed{
|j-j'|\ge2\quad(j\ne j',\ j,j'\in P_L),
}
\]

so the adjacent pairs `(j,j+1)`, `j in P_L`, are pairwise disjoint.

Their number is

\[
|P_L|=(L-1)-b_{L-1}
=(1-\alpha)L+O(1).
\]

## 3. Every mixed plateau pair is free

Fix `w in B_L` and `j in P_L`. Let

\[
Q=q_j(w)
\]

be the number of ones before the pair `(j,j+1)`.

Suppose

\[
w_j+w_{j+1}=1.
\]

The lower intermediate count among the two orientations `01` and `10` is exactly `Q`. Since `w` survives to time `j`,

\[
Q\ge b_j.
\]

But `j in P_L` means

\[
b_{j+1}=b_j.
\]

Therefore

\[
Q\ge b_{j+1},
\]

so both orientations satisfy the only prefix inequality that can differ. After the second position both orientations have total `Q+1`, so all later prefix counts agree.

Hence

\[
\boxed{
\cdots01\cdots\in\mathcal B_L
\iff
\cdots10\cdots\in\mathcal B_L
}
\]

for every mixed plateau pair.

Because the plateau pairs are disjoint and each mixed pair always contains one one, toggling one plateau pair does not change the prefix one-count entering any later plateau pair. Thus all mixed plateau pairs can be toggled **independently**.

## 4. Exact hypercube fibers

Fix all bits outside the plateau pairs and, for every plateau pair, fix only its pair-sum in `{0,1,2}`.

If exactly `m` plateau pairs have pair-sum one, then every choice of their orientations is admissible and remains in the same boundary class.

Thus the fiber has exactly

\[
\boxed{2^m}
\]

members.

No orbit enumeration is required inside this fiber: the `m` mixed plateau pairs are independent Boolean coordinates.

## 5. Canonical-residue adjacent-swap identity

For a parity word `u=(u_0,...,u_{n-1})`, let `r(u)` be its canonical start residue modulo `2^n`. If the one at position `j` is the `ell`-th one of the word, the standard parity-vector formula is

\[
\boxed{
r(u)\equiv
-\sum_{t:u_t=1}2^t3^{-q_{t+1}(u)}
\pmod{2^n}.}
\]

Consider a mixed plateau pair with one-ordinal

\[
\ell=Q+1.
\]

Moving that one one place to the right, `10 -> 01`, changes no other one-ordinal. Hence

\[
\boxed{
r(\cdots01\cdots)-r(\cdots10\cdots)
\equiv
-2^j3^{-\ell}
\pmod{2^n}.}
\]

The same identity applies to the surviving boundary extensions `w1`, with `n=L+1`.

This is the residue-space counterpart of the local `01/10` remainder ordering used in the Collatz parity-vector literature, but here it is used as an exact dyadic Fourier phase increment.

## 6. Exact Fourier factorization on one cube

Let

\[
\chi_k(r)=e^{-2\pi i kr/2^{L+1}}.
\]

For one hypercube fiber with mixed plateau-pair set `F`, choose one orientation as the base point. For `j in F`, let `ell_j` be the one-ordinal in that pair and set

\[
a_j=[3^{-\ell_j}]_{2^{L+1-j}}.
\]

Flipping coordinate `j` multiplies the character by

\[
z_j
=
\exp\!\left(
\frac{2\pi i k a_j}{2^{L+1-j}}
\right)
\]

(up to complex conjugation according to the chosen base orientation, which does not affect the magnitude).

Therefore the full `2^m`-point character sum factorizes exactly:

\[
\boxed{
\sum_{u\in\text{fiber}}\chi_k(r(u))
=
\chi_k(r_0)
\prod_{j\in F}(1+z_j).
}
\]

Consequently

\[
\boxed{
\frac1{2^m}
\left|
\sum_{u\in\text{fiber}}\chi_k(r(u))
\right|
=
\prod_{j\in F}
\left|
\cos\!\left(
\frac{\pi k a_j}{2^{L+1-j}}
\right)
\right|.
}
\]

This is an exact **boundary Riesz product** built from inverse powers of three.

The ternary selector channel has the forward-power Riesz product

\[
\prod_i
\left|\cos\frac{\pi k3^i}{2^r}\right|,
\]

whereas the Beatty boundary cube has the inverse-power factors above. This gives a concrete forward/inverse spectral-complementarity target.

## 7. Linear number of cube coordinates for almost every boundary word

The deterministic plateau pairs are disjoint. Under the Bernoulli-`alpha` product measure, the bits in different plateau pairs are independent, and a fixed plateau pair is mixed with probability

\[
\boxed{
p_{\rm mix}=2\alpha(1-\alpha).}
\]

Let `M_L(w)` be the number of mixed plateau pairs. Under that product measure,

\[
M_L\sim\operatorname{Bin}(|P_L|,p_{\rm mix}).
\]

All words in `B_L` have exactly `b_L` ones. Therefore their Bernoulli-`alpha` probability weight is constant, so a Chernoff bound for `M_L` transfers directly to a counting bound after division by that common weight.

Using the cycle-minimum lower bound

\[
|\mathcal B_L|\ge\frac1L\binom L{b_L}
\]

and Stirling, for every fixed

\[
0<c<(1-\alpha)p_{\rm mix}
=2\alpha(1-\alpha)^2,
\]

there is `gamma(c)>0` such that

\[
\boxed{
\frac{|
\{w\in\mathcal B_L:M_L(w)\le cL\}
|}{|\mathcal B_L|}
\le
\operatorname{poly}(L)e^{-\gamma(c)L}.
}
\]

For the concrete choice `c=0.10`,

\[
\frac{c}{1-\alpha}\approx0.270951,
\qquad
p_{\rm mix}\approx0.4657,
\]

and the binary-exponent form of the Chernoff rate is approximately

\[
\boxed{0.0425L.}
\]

Thus, apart from an exponentially small portion of the Beatty boundary, every boundary word carries at least `0.10 L` independent deterministic swap coordinates.

## 8. Consequence for the spectral target

The boundary Fourier problem no longer needs to be phrased as cancellation among an unstructured exponentially large set of parity words.

It reduces to two parts:

1. an exponentially small exceptional family of boundary words with too few mixed plateau pairs;
2. hypercube fibers with linearly many exact cosine factors

\[
\left|
\cos\!\left(
\frac{\pi k[3^{-\ell}]_{2^m}}{2^m}
\right)
\right|.
\]

Therefore a sufficient boundary spectral theorem is:

> outside a suitably sparse frequency family, a positive proportion of the deterministic plateau-pair factors stay uniformly away from one.

If this holds, the boundary transform has exponential Fourier decay on the selector-exception frequencies required by the spectral-splitting lemma.

## 9. Verification

`collatz/src/beatty_plateau_pair_cube_audit.py` checks the finite identities:

- plateau starts are disjoint;
- every mixed plateau pair can be swapped without leaving the boundary;
- multiple plateau swaps commute;
- the canonical-residue swap formula holds;
- direct boundary Fourier coefficients are bounded by the averaged cube-product bound.

The combinatorial proofs above are independent of the finite diagnostic.
