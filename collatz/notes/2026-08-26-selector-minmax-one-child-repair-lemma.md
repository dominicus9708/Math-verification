# Selector min/max mixing gives a direct one-child repair bound

Date: 2026-08-26

Status: **exact physical-space lemma + application to existing exact selector-DP extrema.**  This gives a simpler sufficient condition for controlling the one-child cross-base repair whenever the selector multiplicity is uniformly bounded above and below.  It does not by itself prove a positive-density supply of one-child events at all asymptotic scales, and it is not a proof of the Collatz conjecture.

## 1. Setup

At child modulus `2M`, let

\[
C(x)\ge0,
\qquad x\in\mathbb Z/(2M)\mathbb Z,
\]

be the exact selector multiplicity.

For a parent residue `r mod M`, define

\[
c(r)=C(r)+C(r+M),
\qquad
u(r)=C(r)-C(r+M).
\]

Let `D` be any one-child parent set and let

\[
v(r)\in\{-1,+1\}
\]

record the surviving child orientation.

The selector mass carried by `D` is

\[
S_D:=\sum_{r\in D}c(r),
\]

and the signed repair is

\[
K_D:=\sum_{r\in D}v(r)u(r).
\]

No assumption is made on the geometry or orientation pattern of `D`.

## 2. Min/max hypothesis

Assume globally on the child modulus that

\[
\boxed{
a\le C(x)\le b
}
\]

with `0<a<=b`.

Then for every parent residue,

\[
c(r)\ge2a
\]

and

\[
|u(r)|\le b-a.
\]

Therefore

\[
S_D\ge2a|D|
\]

while

\[
|K_D|
\le\sum_{r\in D}|u(r)|
\le(b-a)|D|.
\]

Hence

\[
\boxed{
\frac{|K_D|}{S_D}
\le
\frac{b-a}{2a}.
}
\]

This is a direct physical-space repair inequality.  It needs neither cancellation in `v` nor a Fourier estimate for the boundary.

## 3. One-child contraction

The exact child-transport identity says that the mass retained from one-child parents is

\[
\frac{S_D+K_D}{2}.
\]

Thus

\[
\frac{S_D+K_D}{2S_D}
\le
\frac12\left(1+\frac{b-a}{2a}\right).
\]

Put

\[
\rho:=\frac ab.
\]

The repair factor is

\[
\boxed{
\beta(\rho)
:=
\frac{b-a}{2a}
=
\frac{1-\rho}{2\rho}.
}
\]

A strict contraction exists exactly when

\[
\beta(\rho)<1,
\]

that is,

\[
\boxed{
\rho>\frac13.
}
\]

The guaranteed fraction of one-child mass lost is

\[
\boxed{
\delta(\rho)
=
\frac{1-\beta(\rho)}2
=
\frac{3\rho-1}{4\rho}>0.
}
\]

Equivalently,

\[
\boxed{
\text{retained one-child fraction}
\le
1-\delta(\rho)
=
\frac{1+\rho}{4\rho}.
}
\]

Thus the selector does **not** need to be asymptotically perfectly uniform.  A min/max ratio bounded uniformly above `1/3` is already enough to prevent the ternary child bias from repairing all dynamical one-child pruning.

## 4. Translated low-ternary cylinders

Fixing low ternary selector digits merely translates the high-selector subset-sum distribution on the dyadic group.

If the high-selector multiplicity is `h(x)` with

\[
h_{\min}\le h(x)\le h_{\max},
\]

then every fixed low-ternary cylinder has child-level count function

\[
C_\ell(x)=h(x-s_\ell)
\]

for some translation `s_ell`.

Therefore the same lemma holds uniformly over **every** low-ternary cylinder with

\[
\rho=\frac{h_{\min}}{h_{\max}}.
\]

This is useful because it turns a static selector-mixing estimate into a cylinder-uniform dynamic repair bound without enumerating boundary orientations.

## 5. Existing H24/H25 exact constants

The existing exact selector dynamic programs give the following multiplicity extrema.

### Full m=44 selector distribution

At H24 reduced dyadic resolution:

\[
a=4,188,525,
\qquad
b=4,199,983,
\]

so

\[
\rho=0.9972718937195698\ldots,
\]

\[
\frac{|K_D|}{S_D}
\le0.0013677846019780\ldots,
\]

and therefore

\[
\boxed{
\text{one-child retained mass}
\le0.500683892300989\ldots\,S_D.
}
\]

At H25:

\[
a=2,092,917,
\qquad
b=2,102,038,
\]

so

\[
\rho=0.9956608776815643\ldots,
\]

\[
\frac{|K_D|}{S_D}
\le0.00217901617694347\ldots,
\]

and

\[
\boxed{
\text{one-child retained mass}
\le0.501089508088472\ldots\,S_D.
}
\]

Thus at these finite scales the worst possible cross-base repair can recover only a tiny part of the ideal one-half pruning.

## 6. Fixed low-ternary cylinder constants

The same calculation using the high-selector multiplicity extrema gives:

\[
\begin{array}{c|c|c|c}
\text{case}&\rho&|K_D|/S_D\text{ bound}&\text{retained one-child fraction}\\\hline
H24,Q7&0.9557318855711004&0.0231592746340398&0.511579637317020\\
H24,Q8&0.9403365327645455&0.0317245290151849&0.515862264507592\\
H24,Q9&0.9116961789375583&0.0484283158701763&0.524214157935088\\
H25,Q7&0.9352951604325475&0.0345905989385898&0.517295299469295
\end{array}
\]

Every one of these is far above the threshold `rho>1/3`.

Hence for the already computed m=44 finite scales, **every low-ternary cylinder receives a uniform one-child contraction close to one half, regardless of the dynamical child orientation pattern.**

## 7. Relation to the convolution-transfer lemma

The earlier convolution-transfer theorem used min/max selector multiplicities to transfer a **global bounded-block loss** into every low-ternary cylinder.

The present lemma is the one-bit local analogue:

\[
\boxed{
\text{static selector min/max mixing}
\Longrightarrow
\text{uniform bound on cross-base child repair}.
}
\]

It explains why the direct cylinder-contraction constants and the convolution-derived constants were so close in the finite H24/H25 computations: the selector distribution is already nearly flat on those dyadic resolutions, so child orientation has little leverage.

## 8. Correct asymptotic target

For a scaling family `(m,L,Q)` it is enough, on the static side, to prove a coarse bound

\[
\boxed{
\inf_{\text{large scales}}
\frac{h_{\min}(m,Q,L)}{h_{\max}(m,Q,L)}
>\frac13.
}
\]

This is substantially weaker than proving asymptotic equidistribution or exponentially small Fourier coefficients.

If that static theorem is paired with a dynamical theorem that supplies enough one-child mass cumulatively, the child-transport identity yields contraction without needing the full spectral-overlap estimate.

If the min/max ratio degenerates at the desired scaling, then the correctly normalized spectral-complementarity norm from the 2026-08-26 normalization audit remains the fallback route.

## 9. Remaining dynamic question

This lemma controls **how much** one-child pruning can be repaired when a one-child boundary is encountered.  It does not prove that one-child boundaries carry a positive fraction of survivor mass at every step or over every large block.

The next calculation should therefore quantify cumulative one-child exposure in the pure coefficient-survival/neutral-return language, preferably in a block form that can be combined with a static ratio `rho>1/3`.

## 10. Reproducibility

Derived-constant certificate:

`collatz/src/selector_minmax_child_repair_bound.py`

The multiplicity extrema are imported from the independent exact selector-DP certificates already stored in the repository.  The new algebraic lemma itself is exact and independent of those finite numbers.
