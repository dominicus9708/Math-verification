# Multi-resolution plateau occupancy halving and boundary moments

Date: 2026-08-26

Status: **exact finite-group counting theorem + boundary-cube moment consequence.** This note uses the previously proved deterministic plateau-pair cube factorization and reverse-carry conjugacy. It proves a uniform joint occupancy bound across the varying dyadic resolutions without identifying resolution-dependent carry digits. It is not a proof of the Collatz conjecture.

## 1. Setup

Fix a maximal dyadic modulus

\[
M_R=2^R
\]

and restrict to odd frequencies `u mod 2^R`.

For a plateau coordinate `j`, let its effective dyadic resolution be

\[
r_j=R-j
\]

and let `a_j` be the odd unit appearing in the exact boundary factor. In the Beatty application,

\[
a_j=[3^{-\ell_j}]_{2^{r_j}}.
\]

The corresponding cosine factor is

\[
Y_j(u)
:=
\left|\cos\left(\pi\frac{a_ju}{2^{r_j}}\right)\right|,
\]

with the argument interpreted modulo the effective dyadic group.

By the reverse balanced-carry conjugacy, for `s=1` the factor is dangerous/weakly attenuating exactly when

\[
Y_j(u)\ge\theta,
\qquad
\theta:=\cos(\pi/6)=\frac{\sqrt3}{2},
\]

or equivalently

\[
\left|\operatorname{cent}_{2^{r_j}}(a_ju)\right|
<\frac{2^{r_j-1}}3.
\]

Denote this dangerous event by `D_j`.

## 2. One-resolution counting fact

Let `r'>=2`, let `r>=r'+2`, and fix any odd residue class modulo `2^{r'}`.

Inside that class there are exactly

\[
2^{r-r'}
\]

lifts modulo `2^r`.

For any odd unit `a`, multiplication by `a` permutes residue classes modulo every dyadic quotient. The centered dangerous interval has total length

\[
\frac{2^r}{3}.
\]

Therefore one fixed residue class modulo `2^{r'}` contributes at most

\[
\left\lceil\frac{2^{r-r'}}3\right\rceil
\]

dangerous lifts. Since `r-r'>=2`,

\[
\boxed{
\left\lceil\frac{2^{r-r'}}3\right\rceil
\le2^{r-r'-1}.
}
\]

Thus imposing one new dangerous condition at a resolution at least two bits above the preceding conditioned resolution removes at least half of the remaining lifts.

At the lowest resolution, among the odd residues modulo `2^r` the dangerous set also has cardinality at most half the odd classes. For `r=2` it is empty; for every `r>=3` the same half bound follows by direct interval counting.

## 3. Multi-resolution occupancy-halving theorem

Let

\[
r_1<r_2<\cdots<r_k\le R
\]

with

\[
r_{i+1}-r_i\ge2.
\]

For each `i`, choose an arbitrary odd unit `a_i mod 2^{r_i}` and define

\[
D_i
:=
\left\{
 u\text{ odd mod }2^R:
 \left|\operatorname{cent}_{2^{r_i}}(a_i u)\right|
 <\frac{2^{r_i-1}}3
\right\}.
\]

Inducting from the lowest resolution upward with the preceding lift count gives

\[
\boxed{
\frac{
|D_1\cap\cdots\cap D_k|
}{2^{R-1}}
\le2^{-k}.
}
\]

Equivalently, for a uniformly chosen odd frequency,

\[
\boxed{
\Pr(D_1\cap\cdots\cap D_k)\le2^{-k}.
}
\]

No probabilistic independence assumption is used. The multipliers may be different at every resolution.

## 4. Why Beatty plateau cubes satisfy the hypothesis

For the deterministic plateau-start set

\[
P_L=\{j:b_{j+1}=b_j\},
\]

the already proved Beatty property `alpha=log_3 2>1/2` gives

\[
|j-j'|\ge2
\]

for distinct plateau starts.

Since the effective resolution is `r_j=R-j`, ordering the mixed plateau coordinates by increasing resolution preserves gaps at least two.

Therefore for **every** boundary hypercube with mixed coordinate set `F`, and every subset `J subseteq F`,

\[
\boxed{
\Pr_{u\,\mathrm{odd}}
\left(
Y_j(u)\ge\frac{\sqrt3}{2}
\ \forall j\in J
\right)
\le2^{-|J|}.
}
\]

This statement is uniform in the one-ordinals `ell_j` and therefore uniform over all boundary cubes.

## 5. Exponential tail for the number of dangerous factors

Let

\[
X_F(u):=\#\{j\in F:Y_j(u)\ge\sqrt3/2\}.
\]

The joint occupancy theorem and a union bound give, for every `0<lambda<=1`,

\[
\boxed{
\Pr(X_F\ge\lambda|F|)
\le
\sum_{h=\lceil\lambda|F|\rceil}^{|F|}
\binom{|F|}{h}2^{-h}.
}
\]

For example at `lambda=4/5`, the binary entropy estimate yields the exponent

\[
\boxed{
\frac45-H_2\!\left(\frac45\right)
\approx0.0780719051126.
}
\]

Outside this exceptional frequency family at least `|F|/5` factors are non-dangerous, hence

\[
\prod_{j\in F}Y_j(u)
\le
\left(\frac{\sqrt3}{2}\right)^{|F|/5}.
\]

## 6. Stronger moment theorem

The joint occupancy estimate has a cleaner moment consequence.

For every `q>0`,

\[
Y_j(u)^q
\le
\theta^q+(1-\theta^q)1_{D_j}(u),
\qquad
\theta=\frac{\sqrt3}{2}.
\]

Expanding the product over a cube and applying

\[
\Pr\!\left(\bigcap_{j\in J}D_j\right)\le2^{-|J|}
\]

to every subset `J subseteq F` gives

\[
\boxed{
\mathbb E_{u\,\mathrm{odd}}
\left[
\left(\prod_{j\in F}Y_j(u)\right)^q
\right]
\le
\left(
\frac{1+\theta^q}{2}
\right)^{|F|}.
}
\]

Two useful special cases are

\[
\boxed{
\mathbb E Y_F
\le
\left(\frac{2+\sqrt3}{4}\right)^{|F|}
=2^{-0.100031373047\ldots |F|},
}
\]

and

\[
\boxed{
\mathbb E Y_F^2\le\left(\frac78\right)^{|F|}.
}
\]

Thus the odd-frequency RMS cube factor obeys

\[
\boxed{
\|Y_F\|_2
\le
\left(\frac78\right)^{|F|/2}
=2^{-0.096322538971\ldots |F|}.
}
\]

## 7. Typical-cube averaged oriented-boundary consequence

The deterministic plateau-cube theorem already proves that, apart from an exponentially small fraction of boundary words, one has

\[
|F|\ge0.10L.
\]

On those cubes, the preceding moment theorem gives

\[
\|Y_F\|_2
\le
2^{-0.009632253897\ldots L}.
\]

Averaging the exact cube transforms and using Minkowski therefore gives an exponentially decaying normalized odd-frequency `L2` bound for the oriented Beatty-boundary transform, up to the already certified exponentially small low-mixed-coordinate boundary fraction.

This closes an **averaged boundary-spectrum subproblem** that had previously been phrased only as a target: outside the low-rank cube family, many varying-resolution factors cannot all remain close to one on a large set of odd frequencies.

## 8. DSD aggregation audit: why this is not yet same-address closure

The spectral transport identity uses an **unnormalized sum over frequencies**,

\[
\sum_k\widehat\mu(k)\overline{\rho(k)}.
\]

An exponentially decaying normalized `L2` average of the boundary transform does not by itself defeat the `2^L` frequency count. Applying Cauchy/Hölder without additional arithmetic structure reintroduces the ambient-frequency factor and is too weak at the current constants.

Therefore the valid logical chain is

\[
\boxed{
\text{nested dyadic resolutions}
\to
\text{joint occupancy}
\to
\text{boundary moments}
}
\]

but **not yet**

\[
\text{boundary moments}
\to
\text{same-address extinction}.
\]

The missing bridge must retain more structure of the selector frequencies or move back to a primal same-address formulation.

## 9. DSD interpretation

This theorem is useful precisely because it does not conflate resolution-dependent carry digits.

- underlying state: one odd dyadic frequency;
- resolution channel: quotient to `2^{r_j}`;
- observable: central-window occupancy / boundary-factor weakness;
- valid aggregation: nested lift counting across resolutions;
- forbidden aggregation: pretending the carry digits at different resolutions are one independent digit string.

Thus DSD serves here as an audit rule that permits the projection-level counting theorem while blocking a stronger but invalid independence claim.

## 10. Proof-program status

Newly established auxiliary result:

\[
\boxed{
\Pr(\text{any prescribed }k\text{ plateau factors are all dangerous})\le2^{-k}.
}
\]

and consequently

\[
\boxed{
\mathbb E Y_F^q
\le
\left(\frac{1+(\sqrt3/2)^q}{2}\right)^{|F|}.
}
\]

Still open:

1. a structured selector--boundary correlation estimate strong enough for the unnormalized Fourier transport sum, or an equivalent primal same-address theorem;
2. transfer through ordinary as well as oriented boundary terms in the full spectral genealogy at the strength needed for global contraction;
3. final extinction of the recursively sufficient selector family.

The Collatz conjecture remains open.

Certificate: `collatz/src/multiresolution_plateau_occupancy_halving_certificate.py`.
