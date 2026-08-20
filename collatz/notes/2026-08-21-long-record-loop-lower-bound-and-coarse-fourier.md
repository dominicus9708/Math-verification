# Long-record bridge loops and coarse Fourier closure

Date: 2026-08-21

Status: **analytic lower bound on critical Bernoulli record mass and consequent almost-every-scale Fourier contraction for long record excursions.** The initial linear-block argument has been strengthened to an \(r^2\)-block bridge argument. This closes the coarse-Fourier side of the record-strip program. Short records and the final selector/Hensel splice remain open. This is not a proof of the Collatz conjecture.

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

## 1. Exact mechanical centering

For a block of length \(n\) beginning at phase \(a\), put

\[
D_a(n)=b_{a+n}-b_a.
\]

The one-slack ceiling identity gives

\[
\boxed{|D_a(n)-\alpha n|<1.}
\]

If a block begins at strip state \(y\) and has \(X\) odd parity bits, then

\[
y_{\rm out}=y+D_a(n)-X.
\]

Therefore

\[
\boxed{X=D_a(n)}
\]

returns exactly to the same strip state.

## 2. Condition on the exact endpoint: a discrete Bernoulli bridge

Fix a block length \(n\) and put

\[
D=D_a(n),
\qquad p_n=D/n.
\]

Condition on

\[
X_n=D.
\]

Under this conditioning, the \(D\) odd bits are uniformly distributed among the \(n\) positions. Equivalently, the centered variables

\[
Y_i=\varepsilon_i-p_n
\]

are a random permutation of a fixed finite population with total sum zero.

Let

\[
S_k=Y_1+\cdots+Y_k=X_k-kp_n.
\]

For \(k<n\), sampling without replacement gives

\[
\mathbb E(Y_{k+1}\mid\mathcal F_k)
=-\frac{S_k}{n-k}.
\]

Hence

\[
\boxed{
M_k:=\frac{S_k}{n-k}
}
\]

is an exact martingale for \(0\le k<n\).

The hypergeometric variance is

\[
\boxed{
\mathbb E S_k^2
=\frac{k(n-k)}{n-1}p_n(1-p_n).
}
\]

Take \(m=\lfloor n/2\rfloor\). Since \(p_n(1-p_n)\le1/4\),

\[
\mathbb E M_m^2
=\frac{m}{(n-1)(n-m)}p_n(1-p_n)
\le\frac{1}{4(n-1)}.
\]

If \(|S_k|\ge A\) for some \(k\le m\), then

\[
|M_k|\ge A/n.
\]

Doob's \(L^2\) maximal inequality therefore gives

\[
P\left(\max_{k\le m}|S_k|\ge A\mid X_n=D\right)
\le
\frac{n^2}{4(n-1)A^2}.
\]

Apply the same argument to the reversed bridge on the second half. For \(n\ge2\),

\[
\boxed{
P\left(\max_{k\le n}|S_k|\ge A\mid X_n=D\right)
\le
\frac{n}{A^2}.
}
\]

This is the bridge maximal inequality needed below; no external parabolic-Harnack theorem is required.

## 3. An r-squared central loop has probability at least c/r

Fix the central strip state

\[
c_r=\lfloor r/2\rfloor.
\]

Let

\[
A_r=r/4-2.
\]

Choose a small fixed \(c_*>0\), for example any value small enough that for all sufficiently large \(r\), every

\[
c_*r^2\le n\le2c_*r^2
\]

satisfies

\[
\frac{n}{A_r^2}\le\frac12.
\]

By the bridge maximal inequality,

\[
P\left(\max_{k\le n}|S_k|<A_r\mid X_n=D_a(n)\right)
\ge\frac12.
\]

Now compare the bridge centering \(kp_n\) with the mechanical count \(D_a(k)\). Since both \(D_a(n)-\alpha n\) and \(D_a(k)-\alpha k\) have absolute value below one,

\[
|kp_n-D_a(k)|<2.
\]

Therefore on the bridge event,

\[
|X_k-D_a(k)|
\le|S_k|+|kp_n-D_a(k)|
<r/4.
\]

A path starting at \(c_r\) stays strictly inside \([0,r]\) and, because \(X_n=D_a(n)\), returns exactly to \(c_r\) at block end.

For fixed \(\alpha\), Stirling bounds give a constant \(c_0(\alpha)>0\) such that whenever \(|D-\alpha n|<1\),

\[
P_\alpha(X_n=D)\ge\frac{c_0}{\sqrt n}.
\]

Since \(n\asymp r^2\),

\[
P_\alpha(X_n=D_a(n))\ge\frac{c_1}{r}.
\]

Combining with the conditional bridge probability gives the genuine strip-loop estimate

\[
\boxed{
P_\alpha(\text{central }r^2\text{-loop block})
\ge\frac{c_2(\alpha)}{r}.
}
\]

This improves the earlier \(O(r)\)-length loop of probability \(c/\sqrt r\).

## 4. Entrance and exit connectors cost only exp(-O(r))

Starting from \(y=0\), choose parity zero until the mechanical rise count reaches \(c_r\). Then \(y\) increases monotonically from \(0\) to \(c_r\). The entrance length is \(O_\alpha(r)\).

For the exit, choose parity one over the shortest suffix before the terminal record step containing exactly \(c_r\) mechanical plateaus. Then \(y\) decreases monotonically from \(c_r\) to \(0\). Its length is also \(O_\alpha(r)\).

The final plateau-odd bit exits through \(y=-1\).

With

\[
\rho_\alpha=\min(\alpha,1-\alpha)>0,
\]

the combined forced connectors have Bernoulli probability at least

\[
\exp(-C_0(\alpha)r).
\]

## 5. Fill a long record by independent bridge loops

After removing the entrance connector, exit connector and final exit, partition the middle into blocks with lengths in

\[
[c_*r^2,2c_*r^2],
\]

except for at most one shorter remainder. The remainder can be absorbed into the connector cost by choosing \(\varepsilon=d\), which keeps the strip state fixed.

Every full middle block independently contributes probability at least \(c_2/r\), and the number of such blocks is

\[
O\left(\frac{L}{r^2}+1\right).
\]

Therefore there exist phase-independent constants \(r_0,C_1,C_2>0\), depending only on \(\alpha\), such that for every \(r\ge r_0\) and every nonempty record length \(L\ge C_1r\),

\[
\boxed{
P_\alpha(\mathcal R_{s,r}(L))
\ge
\exp(-C_2r)
\left(\frac{c_2}{r}\right)^{C_2(L/r^2+1)}.
}
\]

Thus

\[
\boxed{
K_\alpha(\mathcal R_{s,r}(L))
\le
C_3(\alpha)
\left[
r+\left(\frac{L}{r^2}+1\right)\log r
\right].
}
\]

## 6. Long records: information cost per bit is O(1/r)

If

\[
\boxed{L\ge r^2,}
\]

then

\[
\boxed{
\frac{K_\alpha(\mathcal R)}{L}
=O_\alpha\left(\frac1r+\frac{\log r}{r^2}\right)
=O_\alpha(1/r).
}
\]

The entropy–Haar dichotomy gives, for every \(\eta>0\),

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

Consequently a long record has

\[
\boxed{
1-O_\alpha\left(\frac{1}{\eta^2r}\right)
}
\]

of all dyadic valuation levels satisfying

\[
\boxed{
|\widehat\mu(t)|\le\delta_\alpha+\eta.
}
\]

For any fixed

\[
0<\eta<\frac12-\delta_\alpha,
\]

the right side is strictly below \(1/2\), while the exceptional fraction tends to zero like \(O(1/r)\).

Thus the **long-record coarse-Fourier regime is analytically closed** up to a vanishing exceptional set of valuation levels.

## 7. Exact long/short split

The remaining deterministic tail divides into:

### Long records

\[
L_r\ge r^2.
\]

All but an \(O(1/r)\) fraction of dyadic levels have record-side Fourier contraction bounded by a fixed constant below \(1/2\).

### Short records

\[
L_r<r^2.
\]

The whole record occupies only \(O(r^2)\) levels and is assigned to the fine/deterministic selector-Haar/Hensel side.

The unresolved part of a long record is likewise only the \(O(L_r/r)\)-scale exceptional set supplied by the information budget.

## 8. Remaining theorem

The Stage-4 bridge is now reduced to:

> **Exceptional-level selector/Hensel splice.** Control selector concentration on (i) all levels of short record excursions \(L_r<r^2\), and (ii) the \(O(L_r/r)\) exceptional valuation levels inside long records. Every other level of every sufficiently large long record already has uniform record-side Fourier contraction below \(1/2\).

The finite certificate remains

`collatz/src/long_record_loop_fourier_certificate.py`.
