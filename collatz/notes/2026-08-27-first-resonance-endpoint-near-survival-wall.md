# First-resonance endpoint near-survival coefficient wall

Date: 2026-08-27

Status: exact reduction plus exact Worley/continued-fraction certificate.  This strengthens the repaired first-resonance branch; it does not prove the Collatz conjecture.

## 1. Setup

Let a hypothetical minimal counterexample `N` enter the repaired first global resonance

\[
(A_0,Q_0)=(114208327604,72057431991)
\]

and let

\[
y=T^{A_0}(N)=N+g,
\qquad 0<g<2^{33}.
\]

We already have

\[
N>2^{71}
\]

and minimality implies every later orbit value is at least `N`.

The question is whether the endpoint `y`, which is not itself assumed minimal, could have a coefficient-subcritical prefix much earlier than `A_0` while its additive correction keeps the actual orbit above `N`.

## 2. Necessary inequality at the first subcritical prefix

Suppose `(j,q)` is the first prefix of the orbit from `y` satisfying

\[
3^q<2^j.
\]

All proper prefixes are coefficient-surviving.  Hence the standard whole-prefix correction bound applies:

\[
R\le q3^{q-1}.
\]

Writing

\[
C=\frac{3^q}{2^j}<1,
\]

we obtain

\[
T^j(y)=\frac{3^qy+R}{2^j}
\le C\left(y+\frac q3\right).
\]

But the orbit cannot fall below `N=y-g`, so necessarily

\[
C\left(y+\frac q3\right)\ge y-g.
\]

Therefore

\[
\boxed{
1-C
\le
\frac{g+Cq/3}{y}
<
\frac{2^{33}+q/3}{2^{71}}.
}
\]

This is the endpoint **near-survival coefficient wall**.

## 3. Diophantine reduction

Put

\[
\alpha=\log_3 2.
\]

For a subcritical pair define

\[
\delta=j\ln2-q\ln3>0.
\]

Then `C=e^{-delta}`.  If the necessary inequality above holds and

\[
H=\frac{2^{33}+q/3}{2^{71}},
\]

then

\[
1-e^{-\delta}\le H.
\]

Using

\[
-\ln(1-H)\le\frac{H}{1-H},
\]

and `q<=Q_0`, `j<A_0`, the companion exact-rational certificate obtains

\[
\boxed{
\left|\alpha-\frac qj\right|
<\frac{k}{j^2},
\qquad k<1.436.
}
\]

By the Worley--Dujella theorem, after reducing `q/j=a/b`, every candidate lies in an adjacent-convergent combination with

\[
rs<2k<2.872,
\]

so

\[
\boxed{rs\le2.}
\]

## 4. Complete finite candidate audit

The exact continued-fraction interval for `alpha` produces exactly `23` primitive `rs<=2` candidates below `alpha` with primitive denominator `<A_0` that survive the Worley approximation prefilter.

An actual pair can be a positive multiple

\[
(j,q)=m(b,a),
\qquad mb<A_0.
\]

For each primitive pair, the certificate checks the entire multiplicity interval without enumerating all `m`.

Let

\[
\delta_0=b\ln2-a\ln3>0.
\]

A rigorous lower interval `D_0` gives

\[
1-e^{-m\delta_0}
\ge
\frac{mD_0}{1+mD_0}.
\]

Subtracting the near-survival allowance

\[
\frac{2^{33}+ma/3}{2^{71}}
\]

gives a concave function of real `m`.  Positivity at the two endpoints `m=1` and `m=floor((A_0-1)/b)` therefore proves positivity throughout the whole integer multiplicity range.

All `23` primitive ranges fail the necessary near-survival inequality.

Thus

\[
\boxed{
\text{no coefficient-subcritical prefix of }y\text{ can occur for }1\le j<A_0.
}
\]

Equivalently,

\[
\boxed{
3^{q_j(y)}\ge2^j
\qquad(1\le j<A_0).
}
\]

Because the affine correction is positive, this also implies

\[
\boxed{
T^j(y)>y
\qquad(1\le j<A_0).
}
\]

So the near-return endpoint is itself strictly non-descending relative to its own start throughout the whole proper first-resonance horizon.

## 5. Sharpness at the first resonance

The same exact log intervals certify that the pair

\[
(A_0,Q_0)
\]

is *not* excluded by the near-survival inequality.  Therefore the endpoint wall is aligned with the same first Farey resonance already found from the start side:

\[
\boxed{
\text{start-side first possible crossing depth}
=
\text{endpoint-side first possible near-survival crossing depth}
=A_0.
}
\]

The theorem does not assert that `y` actually crosses at `A_0`; it may have `q_{A_0}(y)>=Q_0+1` and continue coefficient survival.

## 6. DSD logic-chain significance

The endpoint was previously described only by the ordinary near-return condition

\[
y=N+g,
\qquad g<2^{33}.
\]

The present theorem upgrades it to a second full coefficient-survivor boundary state:

\[
\boxed{
N\xrightarrow[A_0]{\text{first resonance}}y
\quad\Longrightarrow\quad
\begin{cases}
N\text{ coefficient-survives all proper prefixes},\\
y\text{ coefficient-survives all proper prefixes}.
\end{cases}}
\]

Thus the two ends are not merely close ordinary integers.  They belong to the same long-lived coefficient-survivor language for `A_0-1` steps.

This creates a new repaired-binary target:

> exclude two distinct coefficient-survivor integers in the first-resonance band whose ordinary separation is a positive multiple of four below `2^33` and whose first member closes the first resonance into the second.

Companion certificate:

`collatz/src/first_resonance_endpoint_near_survival_worley_certificate.py`.

External theorem already used elsewhere in the repository:
R. T. Worley (1981), with the Dujella--Ibrahimpasic adjacent-convergent formulation.
