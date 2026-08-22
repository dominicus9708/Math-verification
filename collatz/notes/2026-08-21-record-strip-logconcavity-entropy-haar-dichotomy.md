# Record-strip log-concavity and entropy–Haar dichotomy

Date: 2026-08-21

Status: **exact completion-kernel shape theorem and exact information-theoretic Fourier budget.** This replaces the overly strong pointwise-Harnack target by an averaged theorem that is true for every finite record language. It does not yet prove the final selector/record transversality theorem and is not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil \alpha k\rceil.
\]

For a record first-passage language \(\mathcal R_{s,r}(L)\), write

\[
g_j=q_j-(b_{s+j}-b_s),
\qquad
-r\le g_j\le0\quad(j<L),
\qquad g_L=1,
\]

and use the strip coordinate

\[
y_j=-g_j\in\{0,\ldots,r\}.
\]

The exact transition is

\[
y_j=y_{j-1}+d_j-\varepsilon_j,
\qquad
 d_j=b_{s+j}-b_{s+j-1}\in\{0,1\}.
\]

## 1. Completion vectors are log-concave

Let \(F_j(y)\) be the number of valid completions from strip state \(y\) after \(j\) steps to the prescribed record exit at time \(L\). Extend \(F_j\) by zero outside \([0,r]\).

Backward transfer uses only

\[
(M_0f)(y)=f(y)+f(y-1),
\]

or

\[
(M_1f)(y)=f(y)+f(y+1),
\]

followed by restriction to the strip.

The terminal vector is a point mass, hence log-concave. Convolution with the two-point sequence \((1,1)\) preserves log-concavity, and restriction to an interval preserves log-concavity because it only adds exterior zeros to a contiguous support. Therefore, for every phase, height, horizon and backward time,

\[
\boxed{
F_j(y)^2\ge F_j(y-1)F_j(y+1).
}
\]

On the positive support, the adjacent ratios

\[
R_j(y)=\frac{F_j(y+1)}{F_j(y)}
\]

are therefore nonincreasing in \(y\).

This establishes the qualitative Harnack shape exactly. It also shows why a pointwise uniform Harnack constant cannot be the correct final target: near a killed strip boundary one child completion can be zero, giving local imbalance one.

## 2. Critical Fourier gradient as conditional predictability

Let \(\mathcal R\subset\{0,1\}^L\) be any nonempty parity language for which parity words are identified with their canonical dyadic residues modulo \(2^L\). Give \(\mathcal R\) the uniform distribution.

Fix a depth \(j\in\{0,\ldots,L-1\}\). For a surviving prefix \(u\) of length \(j\), let

\[
C_0(u),\qquad C_1(u)
\]

be the numbers of full words extending the even and odd children. Put

\[
m(u)=C_0(u)+C_1(u),
\qquad
p(u)=\frac{C_1(u)}{m(u)},
\]

for prefixes with \(m(u)>0\), and define the child imbalance

\[
\delta(u)=|1-2p(u)|
=\frac{|C_0(u)-C_1(u)|}{C_0(u)+C_1(u)}.
\]

Under the uniform full-word distribution, the prefix \(u\) has probability \(m(u)/|\mathcal R|\). Define

\[
\Delta_j:=\mathbb E\,\delta(u).
\]

From the exact critical-child sign identity, every nonzero dyadic frequency satisfying

\[
v_2(t)=L-j-1
\]

obeys

\[
\boxed{
|\widehat\mu_{\mathcal R}(t)|\le\Delta_j.
}
\]

Thus one Fourier valuation shell is controlled by one binary conditional-predictability statistic.

## 3. Shannon entropy gives a global Haar budget

Let

\[
H_j:=H_2(B_{j+1}\mid B_1,\ldots,B_j)
=\mathbb E\,h_2(p(u)),
\]

where \(h_2\) is binary entropy in bits.

For a Bernoulli parameter \(p\),

\[
D_{\rm KL}(\operatorname{Bern}(p)\|\operatorname{Bern}(1/2))
=\ln2\,[1-h_2(p)].
\]

Pinsker's inequality gives

\[
D_{\rm KL}(\operatorname{Bern}(p)\|\operatorname{Bern}(1/2))
\ge\frac{(1-2p)^2}{2}.
\]

Therefore

\[
\mathbb E\,\delta(u)^2
\le
2\ln2\,(1-H_j),
\]

and by Cauchy–Schwarz,

\[
\boxed{
\Delta_j^2\le2\ln2\,(1-H_j).
}
\]

The chain rule gives

\[
\sum_{j=0}^{L-1}H_j=\log_2|\mathcal R|.
\]

Hence

\[
\boxed{
\sum_{j=0}^{L-1}
\sup_{\substack{0<t<2^L\\v_2(t)=L-j-1}}
|\widehat\mu_{\mathcal R}(t)|^2
\le
2\ln2\,
\bigl(L-\log_2|\mathcal R|\bigr).
}
\]

This is an exact all-language Fourier/Haar predictability budget. It does not require pointwise Harnack estimates.

## 4. Critical-slope Bernoulli recentering removes the baseline entropy cost

Record first-passage words of fixed \((s,r,L)\) all have the same total odd count

\[
Q=b_{s+L}-b_s+1.
\]

Let \(P_\alpha\) be the product Bernoulli measure with odd probability \(\alpha\). Every word in \(\mathcal R\) has the same \(P_\alpha\)-weight

\[
w_\alpha=\alpha^Q(1-\alpha)^{L-Q}.
\]

For the uniform distribution \(P_{\mathcal R}\) on \(\mathcal R\), define the tilted information cost

\[
\boxed{
K_\alpha(\mathcal R)
:=
D_{\rm KL}(P_{\mathcal R}\|P_\alpha)
=-\ln\bigl(|\mathcal R|w_\alpha\bigr).
}
\]

At depth \(j\), define

\[
\kappa_j
:=
\mathbb E\,
D_{\rm KL}(\operatorname{Bern}(p(u))\|\operatorname{Bern}(\alpha)).
\]

Relative-entropy chain rule gives

\[
\boxed{
K_\alpha(\mathcal R)=\sum_{j=0}^{L-1}\kappa_j.
}
\]

Pinsker now yields

\[
\mathbb E|p(u)-\alpha|
\le\sqrt{\frac{\kappa_j}{2}}.
\]

Since

\[
|1-2p|
\le
|1-2\alpha|+2|p-\alpha|,
\]

we obtain

\[
\boxed{
\Delta_j
\le
\delta_\alpha+\sqrt{2\kappa_j},
\qquad
\delta_\alpha:=|2\alpha-1|
\approx0.2618595071.
}
\]

Consequently, for every \(\eta>0\), the number of dyadic valuation levels at which

\[
\sup_{v_2(t)=L-j-1}|\widehat\mu_{\mathcal R}(t)|
>\delta_\alpha+\eta
\]

is at most

\[
\boxed{
\#\mathrm{Bad}_\eta
\le
\frac{2K_\alpha(\mathcal R)}{\eta^2}.
}
\]

This is the precise entropy–Fourier dichotomy:

- if \(K_\alpha(\mathcal R)\) is large, the record language is itself exponentially rare under the coefficient-critical Bernoulli measure;
- if \(K_\alpha(\mathcal R)=o(L)\), then all but \(o(L)\) dyadic valuation levels have record Fourier amplitude at most
  \[
  \delta_\alpha+o(1)<1.
  \]

So the hard regime cannot simultaneously have near-critical entropy and near-deterministic Fourier behavior at a positive fraction of scales.

## 5. Exact boundary commutator

On the finite strip \(\{0,\ldots,r\}\), let

\[
S_-f(y)=f(y-1),
\qquad
S_+f(y)=f(y+1),
\]

with zero extension outside the strip. Then

\[
M_0=I+S_-,
\qquad
M_1=I+S_+.
\]

A direct calculation gives

\[
S_-S_+=I-P_0,
\qquad
S_+S_-=I-P_r,
\]

where \(P_0,P_r\) are the endpoint coordinate projections. Therefore

\[
\boxed{
M_0M_1-M_1M_0=P_r-P_0.
}
\]

Thus the two Pascal transfers commute in the interior; all order dependence of the mechanical Beatty cocycle is carried by rank-one boundary insertions at the two strip walls.

This is the finite-width analogue of the earlier rank-one Beatty/Fourier cocycle. It explains why phase dependence should be treated as a boundary-renewal correction rather than as a bulk obstruction.

## 6. Revised splice target

The previous proposed theorem

> obtain a pointwise uniform Harnack bound at every interior state

is unnecessarily strong and false at killed boundaries.

The exact replacement is:

1. use the entropy–Fourier budget above to show that a near-maximal record language has critical-scale contraction near \(\delta_\alpha\) at almost every dyadic level;
2. charge the exceptional valuation levels to the tilted information cost \(K_\alpha\);
3. splice the remaining fine/exceptional levels to the existing selector Haar energy budget;
4. use the rank-two boundary commutator to isolate the phase-dependent errors at the two strip walls.

The remaining theorem is therefore an **exceptional-level selector/record splice**, not an unrestricted Harnack theorem.

Companion certificate:

`collatz/src/record_strip_logconcavity_entropy_haar_certificate.py`.
