# Long-record loop lower bound and coarse Fourier closure

Date: 2026-08-21

Status: **analytic lower bound on critical Bernoulli record mass and consequent almost-every-scale Fourier contraction for long record excursions.** This closes the coarse-Fourier side of the record-strip program. Short records and the final selector/Hensel splice remain open. This is not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad b_k=\lceil\alpha k\rceil,
\]

and let \(\mathcal R_{s,r}(L)\) be a nonempty record first-passage language in the strip

\[
0\le y_j\le r\quad(j<L),
\qquad y_L=-1.
\]

The terminal step is necessarily a mechanical plateau followed by an odd parity bit.

Under the product Bernoulli measure \(P_\alpha\), parity bits are independent with

\[
P_\alpha(\varepsilon=1)=\alpha.
\]

Define

\[
K_\alpha(\mathcal R)
=-\ln P_\alpha(\mathcal R)
=-\ln\left(|\mathcal R|\alpha^Q(1-\alpha)^{L-Q}\right),
\]

where all record words have the same total odd count \(Q\).

## 1. Mechanical block displacement is centered

For a block of length \(n\) beginning at phase \(a\), put

\[
D_a(n)=b_{a+n}-b_a.
\]

The one-slack ceiling identity gives

\[
\boxed{|D_a(n)-\alpha n|<1.}
\]

If a block starts at strip state \(y\), and its number of odd parity bits is \(X\), then

\[
y_{\rm out}=y+D_a(n)-X.
\]

Hence the condition

\[
\boxed{X=D_a(n)}
\]

returns exactly to the same strip state.

## 2. A central loop block has probability at least c/sqrt(r)

Fix a central state

\[
c_r=\lfloor r/2\rfloor.
\]

Consider any block length

\[
r\le n\le2r.
\]

Let

\[
X_k=\varepsilon_1+\cdots+\varepsilon_k,
\qquad
S_k=X_k-\alpha k.
\]

For fixed \(\alpha\in(0,1)\), standard Stirling bounds for the binomial mass imply that there is a constant \(c_0(\alpha)>0\) such that, uniformly in \(n\) and every integer \(D\) with \(|D-\alpha n|<1\),

\[
\boxed{
P_\alpha(X_n=D)\ge\frac{c_0}{\sqrt n}
\ge\frac{c_0}{\sqrt{2r}}.
}
\]

The Bernoulli centered increments have range length one. The exponential-martingale proof of the maximal Hoeffding inequality gives

\[
P_\alpha\left(\max_{k\le n}|S_k|\ge A\right)
\le2\exp\left(-\frac{2A^2}{n}\right).
\]

Choose

\[
A_r=r/4-2.
\]

Since \(n\le2r\), the right side is \(O(e^{-c r})\). For all sufficiently large \(r\), it is less than half the preceding central point mass. Therefore the event

\[
X_n=D_a(n),
\qquad
\max_{k\le n}|S_k|<A_r
\]

has probability at least

\[
\boxed{
\frac{c_1(\alpha)}{\sqrt r}.
}
\]

During this event,

\[
|X_k-D_a(k)|
\le |S_k|+|D_a(k)-\alpha k|
<r/4-1,
\]

so a path beginning at \(c_r\) remains strictly inside \([0,r]\) and returns exactly to \(c_r\) at block end.

Thus it is a genuine strip loop.

## 3. Deterministic entrance and exit connectors cost only exp(-O(r))

Starting at \(y=0\), choose parity zero until the mechanical rise count reaches \(c_r\). Then

\[
y_j=D_s(j)
\]

increases monotonically from \(0\) to \(c_r\) without leaving the strip. Because

\[
D_s(j)=\alpha j+O(1),
\]

this entrance connector has length \(O_\alpha(r)\).

Conversely, ending immediately before the prescribed terminal record crossing, choose parity one over the shortest suffix containing exactly \(c_r\) mechanical plateau steps. Along this connector, \(y\) decreases monotonically from \(c_r\) to \(0\). Since the plateau density is \(1-\alpha\), its length is also \(O_\alpha(r)\).

The final plateau-odd step exits through \(y=-1\).

Let

\[
\rho_\alpha=\min(\alpha,1-\alpha)>0.
\]

All forced connector bits therefore have total Bernoulli probability at least

\[
\exp(-C_0(\alpha)r).
\]

## 4. Fill the middle by independent loop blocks

After removing the two connectors and final exit, partition the remaining middle interval into blocks whose lengths lie in \([r,2r]\), except for at most one remainder of length \(<r\). The remainder can be absorbed into the forced connector cost by following the mechanical bit \(\varepsilon=d\), which keeps \(y\) fixed.

Each full middle block independently has a strip-loop event of probability at least

\[
c_1/\sqrt r.
\]

The number of full blocks is at most

\[
\frac{L}{r}+1.
\]

Therefore there are constants \(r_0,C_1,C_2>0\), depending only on \(\alpha\), such that for every \(r\ge r_0\) and every nonempty record length \(L\ge C_1r\),

\[
\boxed{
P_\alpha(\mathcal R_{s,r}(L))
\ge
\exp(-C_2r)
\left(\frac{c_1}{\sqrt r}\right)^{L/r+1}.
}
\]

Taking minus logarithms gives

\[
\boxed{
K_\alpha(\mathcal R_{s,r}(L))
\le
C_3(\alpha)
\left[
r+\left(\frac{L}{r}+1\right)\log r
\right].
}
\]

The constants are phase-independent.

## 5. Long records have vanishing information cost per bit

If

\[
\boxed{L\ge r^2,}
\]

then

\[
\boxed{
\frac{K_\alpha(\mathcal R)}{L}
=O_\alpha\left(\frac{\log r}{r}\right).
}
\]

From the entropy–Haar dichotomy proved in the companion note, for every \(\eta>0\),

\[
\#\left\{j:
\sup_{v_2(t)=L-j-1}|\widehat\mu_{\mathcal R}(t)|
>\delta_\alpha+\eta
\right\}
\le
\frac{2K_\alpha(\mathcal R)}{\eta^2},
\]

where

\[
\delta_\alpha=|2\alpha-1|\approx0.2618595071.
\]

Hence for every fixed \(\eta>0\), a long record with \(L\ge r^2\) has

\[
\boxed{
1-O_\alpha\left(\frac{\log r}{\eta^2r}\right)
}
\]

of all dyadic valuation levels satisfying

\[
\boxed{
|\widehat\mu(t)|\le\delta_\alpha+\eta<1
}
\]

provided \(\eta<1-\delta_\alpha\).

For example, any fixed \(\eta<1/2-\delta_\alpha\) makes the good-level bound strictly below \(1/2\), while the bad-level fraction tends to zero.

This proves the required **coarse Fourier contraction for long record excursions** without a pointwise parabolic Harnack theorem.

## 6. New long/short record split

The deterministic tail now divides naturally into two exact regimes.

### Long record

\[
L_r\ge r^2.
\]

The theorem above gives near-\(\delta_\alpha\) Fourier contraction on all but an \(O(\log r/r)\) fraction of valuation levels.

### Short record

\[
L_r<r^2.
\]

The entire record occupies only \(O(r^2)\) dyadic levels. These are now the remaining fine/deterministic windows to splice with the selector Haar/Hensel machinery.

Thus the previous vague coarse/fine cutoff of order \((r+1)^2\) is no longer only heuristic: the long side has an analytic Fourier theorem, and the unresolved side is explicitly the short-record family plus the exceptional \(O(L\log r/r)\) levels inside long records.

## 7. Remaining theorem

The remaining Stage-4 bridge can now be stated as:

> **Exceptional-level selector/Hensel splice.** Control the selector overlap on (i) all levels belonging to short record excursions \(L_r<r^2\), and (ii) the \(O(L_r\log r/r)\) exceptional valuation levels of long record excursions. Long-record nonexceptional levels already have uniform record-side Fourier contraction.

Companion finite regression:

`collatz/src/long_record_loop_fourier_certificate.py`.
