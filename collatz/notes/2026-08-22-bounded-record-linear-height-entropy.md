# Bounded-record linear height and strengthened parity entropy

Date: 2026-08-22

Status: **exact asymptotic consequence of an eventual uniform record-length bound.** This strengthens the dyadic entropy budget in the bounded-record regime. It does not by itself prove cross-base transversality and is not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil\alpha k\rceil,
\qquad
h_k=m_k-b_k,
\]

where \(m_k\) is the number of odd accelerated Collatz steps among the first \(k\) iterates.

For sufficiently large record levels let

\[
\tau_r=\min\{k:h_k=r\},
\qquad
L_r=\tau_{r+1}-\tau_r.
\]

Assume that there is a fixed integer \(M\) and a record level \(r_0\) such that

\[
\boxed{L_r\le M\qquad(r\ge r_0).}
\]

## 1. Record height grows linearly in ordinary time

For \(r\ge r_0\),

\[
\tau_r
\le
\tau_{r_0}+M(r-r_0).
\]

Hence there is a constant \(C_0\) such that

\[
\boxed{r\ge \tau_r/M-C_0.}
\]

Now let

\[
\tau_r\le k<\tau_{r+1}.
\]

In one accelerated step the height increment is

\[
h_{j+1}-h_j
=(m_{j+1}-m_j)-(b_{j+1}-b_j)
\in\{-1,0,1\}.
\]

Since \(k-\tau_r<M\),

\[
h_k\ge r-M.
\]

Also

\[
\tau_r>k-M.
\]

Combining these inequalities gives

\[
\boxed{
h_k\ge\frac{k}{M}-C_M}
\]

for a constant \(C_M\) depending on the finite initial segment and on \(M\), but not on \(k\).

Thus an eventually bounded record length forces a positive linear height drift.

## 2. Strengthened odd-step density

Since

\[
m_k=b_k+h_k
\]

and \(b_k\ge\alpha k\),

\[
\boxed{
m_k
\ge
\left(\alpha+\frac1M\right)k-C_M.}
\]

Therefore

\[
\boxed{
\liminf_{k\to\infty}\frac{m_k}{k}
\ge
\alpha+\frac1M.
}
\]

This immediately excludes \(M\le2\), because then the right side exceeds one. The already proved singleton theorem is much stronger for the small-M cases, but the density inequality is a useful global quantitative statement.

For every admissible finite \(M\ge3\), define

\[
p_M:=\alpha+\frac1M\in(1/2,1).
\]

## 3. Endpoint entropy upper bound

Any sufficiently long parity prefix belonging to an eventual \(M\)-bounded record tail must satisfy

\[
q_H\ge p_MH-C_M.
\]

Because \(p_M>1/2\), the number of binary words obeying only this endpoint condition is at most

\[
\sum_{q\ge p_MH-C_M}\binom Hq.
\]

For fixed additive \(C_M\), the standard binomial entropy estimate gives

\[
\boxed{
\#\{\text{possible length-}H\text{ prefixes}\}
\le
2^{H H_2(p_M)+O_M(\log H)}.
}
\]

The actual record language is a subset, so the same upper bound applies to it.

Thus the bounded-record dyadic exclusion rate is at least

\[
\boxed{
\eta_M
:=1-H_2\left(\alpha+\frac1M\right).
}
\]

Since \(H_2(p)\) is strictly decreasing for \(p>1/2\),

\[
\boxed{
\eta_M>
1-H_2(\alpha)
=\eta_{\rm coeff}
}
\]

for every finite \(M\).

## 4. Numerical calibration

With

\[
\alpha\approx0.6309297535714574,
\qquad
\eta_{\rm coeff}\approx0.05004447,
\]

we obtain

\[
\begin{array}{c|c|c}
M&p_M&\eta_M\\\hline
3&0.9642630869&0.7776075894\\
4&0.8809297536&0.4733176008\\
5&0.8309297536&0.3444265295\\
6&0.7975964202&0.2732907139\\
8&0.7559297536&0.1982563103\\
10&0.7309297536&0.1598726676\\
20&0.6809297536&0.0966324818\\
50&0.6509297536&0.0667650355\\
100&0.6409297536&0.0580912834
\end{array}
\]

As \(M\to\infty\), \(\eta_M\downarrow\eta_{\rm coeff}\), as expected.

## 5. Consequence for the Stage-4 horizon slope

If a cross-base theorem gave subexponential normalized overlap for the bounded-record language, the crude entropy-only sufficient horizon slope would improve from

\[
1/\eta_{\rm coeff}\approx19.9823
\]

to

\[
\boxed{1/\eta_M.}
\]

For example:

\[
1/\eta_4\approx2.1127,
\qquad
1/\eta_{10}\approx6.2550,
\qquad
1/\eta_{50}\approx14.9779.
\]

This does not remove the cross-base theorem, but it shows that the bounded-record branch has substantially more entropy margin than the unrestricted coefficient-survival branch.

## 6. Relation to the terminal Haar theorem

The companion bounded-record terminal theorem supplies, at every non-singleton record, a fresh dyadic shell with

\[
|\widehat\mu(t)|\le\kappa_M<1.
\]

The present theorem supplies an independent global fact: an eventual length bound \(M\) also forces a positive linear excess odd density and hence a stronger bulk entropy deficit.

Thus the remaining bounded-record splice has two simultaneous resources:

1. a strengthened exponential language deficit \(\eta_M>\eta_{\rm coeff}\);
2. infinitely many fresh terminal Haar contractions, because singleton records cannot form an infinite tail.

The remaining obstruction is purely the repeated ternary-selector / ordinary-integer Hensel alignment across these dyadic constraints.
