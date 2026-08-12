# Cumulative one-child mass lower bound from coefficient-survivor entropy

Date: 2026-08-12

Status: **exact asymptotic-combinatorial lower bound**. The coefficient-survivor entropy bound forces a linear cumulative amount of one-child boundary mass along the Sturmian rise times. Thus the growing-resolution transport program does not require a pointwise positive lower bound on every boundary fraction. This solves the purely dyadic cumulative-boundary part of the transport target, leaving the ternary formation/correlation transfer as the main unresolved bridge.

## 1. Excess cocycle recap

Put

\[
\beta:=\log_3 2,
\qquad
a_k:=\lceil k\beta\rceil.
\]

Let `S_k` be the number of length-`k` coefficient-surviving parity words, and let

\[
\eta_k:=\frac{g_{k,0}}{S_k}
\]

at a rise time

\[
a_{k+1}=a_k+1.
\]

The exact half-line transfer cocycle gives

\[
S_{k+1}=\begin{cases}
2S_k,&a_{k+1}=a_k,\\
(2-\eta_k)S_k,&a_{k+1}=a_k+1.
\end{cases}
\]

Equivalently, beginning from `S_0=1`,

\[
\boxed{
S_K
=2^K
\prod_{\substack{0\le k<K\\a_{k+1}=a_k+1}}
\left(1-\frac{\eta_k}{2}\right).
}
\]

## 2. Endpoint entropy upper bound

Every coefficient-surviving length-`K` word must in particular satisfy

\[
q_K\ge a_K.
\]

Ignoring all prefix restrictions can only enlarge the set. Therefore

\[
S_K\le\sum_{q=a_K}^{K}\binom Kq.
\]

Since

\[
\beta>1/2
\]

and the binary entropy

\[
H_2(x)=-x\log_2x-(1-x)\log_2(1-x)
\]

is decreasing on `[1/2,1]`, the standard binomial bound gives

\[
\boxed{
S_K\le(K+1)2^{H K},
\qquad
H:=H_2(\beta).
}
\]

Numerically,

\[
\boxed{H\approx0.9499555271883305.}
\]

## 3. Logarithmic pruning identity

Take base-two logarithms of the exact product formula:

\[
K-\log_2 S_K
=
\sum_{\text{rise }k<K}
-\log_2\left(1-\frac{\eta_k}{2}\right).
\]

The entropy upper bound implies

\[
K-\log_2 S_K
\ge
(1-H)K-\log_2(K+1).
\]

Thus

\[
\boxed{
\sum_{\text{rise }k<K}
-\log_2\left(1-\frac{\eta_k}{2}\right)
\ge
(1-H)K-\log_2(K+1).
}
\]

This identity already measures the exact cumulative dynamical pruning.

## 4. Linear cumulative one-child lower bound

For `0<=x<=1`, convexity and the endpoint values give

\[
\boxed{
-\log_2(1-x/2)\le x.
}
\]

Applying this termwise yields

\[
\boxed{
\sum_{\text{rise }k<K}\eta_k
\ge
(1-H)K-\log_2(K+1).
}
\]

Numerically,

\[
\boxed{
1-H
\approx0.05004447281166946.
}
\]

Therefore the total one-child boundary fraction accumulated over the first `K` resolutions is forced to grow linearly.

## 5. Average over rise times

The number of rise times through depth `K` is

\[
a_K=\beta K+O(1).
\]

Hence the asymptotic average one-child fraction **along rise times** obeys

\[
\boxed{
\liminf_{K\to\infty}
\frac{1}{a_K}
\sum_{\text{rise }k<K}\eta_k
\ge
\frac{1-H}{\beta}.
}
\]

Numerically,

\[
\boxed{
\frac{1-H}{\beta}
\approx0.07931861277485554.
}
\]

This does not say that every individual rise time has `eta_k>=0.0793`; finite values oscillate. It says that the dangerous tree cannot avoid a linear cumulative supply of one-child parents.

## 6. Importance for the child-transport theorem

The growing-resolution transport identity needs two ingredients:

1. enough mass must repeatedly lie on one-child dynamical parents;
2. the ternary formation measure must not align almost perfectly with the unique dangerous child.

The present theorem settles item 1 at the **uniform dyadic language-count level** in cumulative form.

The remaining bridge is to transfer this cumulative boundary abundance to the actual ternary representative mass. That requires controlling the discrepancy between the ternary subset-sum measure and the dyadic survivor/boundary sets, together with the child-imbalance term `U_j` or the sharper signed correlation `K_L`.

## 7. Why cumulative control is the right notion

A pointwise theorem

\[
\eta_k\ge\eta_*>0
\]

at every rise time would be stronger than necessary and may be false or difficult because the Sturmian timing produces oscillations.

For global contraction it is enough that

\[
\sum\eta_k
\]

grows linearly, because the survivor mass is multiplicative across resolutions.

Thus the coefficient-survivor entropy bound, which previously served only as a crude candidate-count estimate, now has a structural role: it certifies unavoidable cumulative branching loss in the resolution transport.

## 8. Next cross-base target

A terminal-style theorem can now focus on proving that the actual ternary representative boundary mass `M_D^(tern)(k)` tracks enough of the dyadic boundary abundance, for example in an aggregate form such as

\[
\sum_{k<K}\frac{M_D^{\rm tern}(k)}{C_k}
\ge cK-o(K),
\]

and that the formation imbalance/correlation consumes at most a fixed fraction of this mass.

The purely dyadic coefficient language no longer needs a new pointwise boundary theorem.