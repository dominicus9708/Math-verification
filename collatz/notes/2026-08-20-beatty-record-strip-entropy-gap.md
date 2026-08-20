# Finite-width Beatty record-strip entropy gap

Date: 2026-08-20

Status: **analytic finite-width entropy bound for record first-passage words.** This is not the final Hensel transversality theorem and not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil \alpha k\rceil.
\]

At a record time \(s=\tau_r\), let a candidate next-record word of length \(L\) have local odd count \(q_j\) through its first \(j\) bits. Define

\[
D_s(j)=b_{s+j}-b_s,
\qquad
g_j=q_j-D_s(j).
\]

A genuine first passage from record height \(r\) to \(r+1\) satisfies

\[
\boxed{
-r\le g_j\le0\quad(0\le j<L),
\qquad g_L=1.
}
\]

Equivalently, the distance below the current record boundary

\[
y_j=-g_j
\]

stays in the finite strip

\[
\boxed{0\le y_j\le r}
\]

before exiting through \(y=-1\) on the last step.

## 1. Exact finite-state transition

Write

\[
d_j=b_{s+j}-b_{s+j-1}\in\{0,1\}
\]

for the mechanical Beatty bit and \(\varepsilon_j\in\{0,1\}\) for the actual parity bit. Then

\[
\boxed{
y_j=y_{j-1}+d_j-\varepsilon_j.}
\]

Thus there are only two bidiagonal strip transfer matrices:

- if \(d_j=0\), parity 0 keeps \(y\) fixed and parity 1 sends \(y\mapsto y-1\);
- if \(d_j=1\), parity 1 keeps \(y\) fixed and parity 0 sends \(y\mapsto y+1\).

The final first-passage step must have

\[
y_{L-1}=0,
\qquad d_L=0,
\qquad\varepsilon_L=1.
\]

This gives an exact \((r+1)\)-state automaton for the record language.

## 2. Bernoulli tilt at the coefficient-critical slope

Give each parity bit independent Bernoulli weight

\[
\Pr(\varepsilon_j=1)=\alpha,
\qquad
\Pr(\varepsilon_j=0)=1-\alpha.
\]

Over any block of \(n\) consecutive steps, conditional on the past, the number \(X\) of odd bits is

\[
X\sim\operatorname{Bin}(n,\alpha).
\]

Suppose the strip state at the block entrance is some \(g\in[-r,0]\). If the path remains in the strip through the block endpoint, then its block odd count must lie in an interval of at most \(r+1\) consecutive integers. Indeed

\[
g_{\rm out}=g+X-D
\in[-r,0],
\]

so

\[
D-r-g\le X\le D-g.
\]

This is the key point: the position of the interval may depend on phase and entrance state, but its cardinality is always at most \(r+1\).

## 3. Uniform binomial interval anti-concentration

For \(X\sim\operatorname{Bin}(n,p)\), Fourier inversion gives

\[
\Pr(X=k)
=\frac1{2\pi}\int_{-\pi}^{\pi}
(1-p+pe^{it})^n e^{-ikt}\,dt.
\]

Using

\[
|1-p+pe^{it}|^2
=1-4p(1-p)\sin^2(t/2),
\]

\[
1-u\le e^{-u},
\]

and

\[
\sin(|t|/2)\ge |t|/\pi
\qquad(|t|\le\pi),
\]

we obtain

\[
\boxed{
\max_k\Pr(X=k)
\le
\frac{\sqrt\pi}{2\sqrt{2np(1-p)}}.
}
\]

Therefore every interval \(I\subset\mathbb Z\) of at most \(r+1\) consecutive integers satisfies

\[
\Pr(X\in I)
\le
\frac{(r+1)\sqrt\pi}{2\sqrt{2np(1-p)}}.
\]

Take

\[
p=\alpha
\]

and

\[
\boxed{n=8(r+1)^2.}
\]

Since

\[
\frac{\sqrt\pi}{2\sqrt{16\alpha(1-\alpha)}}
\approx0.4592<\frac12,
\]

we have the uniform block estimate

\[
\boxed{
\Pr(\text{strip survives one }8(r+1)^2\text{-step block})<\frac12.
}
\]

This estimate is independent of the mechanical phase, entrance strip state, and the location of the admissible endpoint interval.

## 4. Repeated-block survival bound

Partition the first \(L-1\) steps of a record word into disjoint blocks of length

\[
M_r:=8(r+1)^2.
\]

Because the parity bits are independent under the tilted Bernoulli measure, the previous conditional estimate iterates. Thus

\[
\boxed{
\Pr_\alpha(\text{record strip survives to }L-1)
\le
2^{-\left\lfloor\frac{L-1}{8(r+1)^2}\right\rfloor}.
}
\]

The final record-crossing requirement can only reduce this probability further.

## 5. Conversion to a raw word-count entropy bound

All length-\(L\) first-passage record words from phase \(s\) have the same total odd count

\[
Q=D_s(L)+1.
\]

The mechanical one-slack identity gives

\[
D_s(L)-\alpha L\in(-1,1),
\]

hence

\[
Q-\alpha L\in(0,2).
\]

If \(\mathcal R_{s,r}(L)\) denotes the record-strip first-passage language, then every word in it has Bernoulli weight

\[
\alpha^Q(1-\alpha)^{L-Q}.
\]

Therefore

\[
|\mathcal R_{s,r}(L)|
\alpha^Q(1-\alpha)^{L-Q}
\le
2^{-\left\lfloor\frac{L-1}{8(r+1)^2}\right\rfloor}.
\]

Since \(Q=\alpha L+O(1)\),

\[
-\log_2\left(\alpha^Q(1-\alpha)^{L-Q}\right)
=
H_2(\alpha)L+O_\alpha(1).
\]

Thus

\[
\boxed{
|\mathcal R_{s,r}(L)|
\le
C_\alpha\,
2^{H_2(\alpha)L
-\left\lfloor\frac{L-1}{8(r+1)^2}\right\rfloor},
}
\]

where \(C_\alpha\) is an absolute constant depending only on \(\alpha\), not on \(s,r,L\).

This proves an explicit finite-width entropy deficit of order

\[
\boxed{\frac{1}{8(r+1)^2}}
\]

bits per step relative to the coefficient-critical entropy.

## 6. Exact finite calibration

The companion transfer certificate gives, at phase \(s=0\), exact record-strip counts. For \(L=120\):

\[
\begin{array}{c|r}
r&|\mathcal R_{0,r}(120)|\\\hline
1&52\,021\,196\,476\,823\,417\,565\,319\\
2&7\,874\,686\,249\,316\,026\,299\,051\,996\,699\\
3&544\,957\,853\,673\,420\,220\,948\,411\,316\,659\\
5&8\,163\,921\,856\,070\,439\,501\,923\,931\,001\,099
\end{array}
\]

while the same upper first-passage language without a lower strip wall has

\[
17\,254\,727\,620\,070\,642\,311\,953\,234\,924\,713
\]

words.

The minimum canonical residue also reacts sharply to the strip width. At phase zero:

\[
\begin{array}{c|rrrrrrr}
r\backslash L&3&6&9&11&14&17&19\\\hline
0&7&27&251&2043&15355&89083&154619\\
1&7&27&54&73&94&82&110\\
2&7&27&54&73&94&82&108
\end{array}
\]

These are finite diagnostics only; the analytic entropy theorem above is the all-length statement.

## 7. What this does and does not close

The theorem gives a rigorous finite-width spectral/entropy gap, but the width itself grows with record height. Therefore it does **not** supply a new uniform positive exponential exclusion rate over the entire tail.

What it does supply is the correct finite-dimensional setting for the last cross-base theorem:

> Add the ternary/Hensel Fourier phase to the \((r+1)\)-state Beatty-strip transfer and prove that the weighted operator has enough cancellation uniformly as \(r\) grows.

This is substantially more concrete than the previous unrestricted same-integer overlap problem. The remaining operator is a bidiagonal finite-width strip cocycle with a forced first-passage boundary and a ternary endpoint syndrome.

Certificate:

`collatz/src/beatty_record_strip_entropy_certificate.py`.
