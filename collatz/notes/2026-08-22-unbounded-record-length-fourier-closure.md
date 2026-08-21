# Unbounded record-length Fourier closure

Date: 2026-08-22

Status: **analytic closure of the record-side coarse Fourier problem whenever record lengths tend to infinity.** Combined with the earlier long-record loop theorem, this removes the previously open short-record ballot regime without importing a moving-boundary ballot theorem. The remaining deterministic tail is the bounded-record regime. This is not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil\alpha k\rceil,
\]

and let \(\mathcal R_{s,r}(L)\) be a nonempty record first-passage language from record height \(r\), written in strip coordinate

\[
y_j=D_s(j)-q_j\in[0,r]
\qquad(j<L),
\]

with final exit \(y_L=-1\).

Under the Bernoulli product measure \(P_\alpha\), define

\[
K_\alpha(\mathcal R)
=-\ln P_\alpha(\mathcal R).
\]

The previous entropy--Haar theorem shows that \(K_\alpha/L=o(1)\) is sufficient to force near-\(|2\alpha-1|\) Fourier contraction on all but \(o(L)\) dyadic valuation levels.

The earlier long-record theorem handled \(L\gtrsim r^2\). This note handles the complementary regime by using only an interior corridor of width \(O(\sqrt L)\).

## 1. Exact mechanical centering on any middle block

For a block of length \(n\) beginning at mechanical phase \(a\), write

\[
D_a(n)=b_{a+n}-b_a.
\]

The one-slack identity gives

\[
\boxed{|D_a(n)-\alpha n|<1.}
\]

If the block starts at strip state \(y\) and contains \(X_n\) odd parity bits, then

\[
y_{\rm out}=y+D_a(n)-X_n.
\]

Therefore

\[
\boxed{X_n=D_a(n)}
\]

returns exactly to the same strip state for every phase and every block length.

## 2. Conditioned Bernoulli bridge maximal bound

Condition on

\[
X_n=D,
\qquad D=D_a(n).
\]

The parity positions are then a uniformly random size-\(D\) subset of \(\{1,\ldots,n\}\). Define

\[
S_k=X_k-\frac{kD}{n}.
\]

For \(k<n\),

\[
\boxed{
M_k:=\frac{S_k}{n-k}
}
\]

is a martingale under the conditioned law. Indeed

\[
E[X_{k+1}-X_k\mid X_k]
=\frac{D-X_k}{n-k},
\]

which gives

\[
E[S_{k+1}\mid S_k]
=S_k\frac{n-k-1}{n-k}.
\]

The hypergeometric variance satisfies

\[
\operatorname{Var}(S_k)
=\frac{k(n-k)}{n-1}\frac Dn\left(1-\frac Dn\right)
\le C_\alpha n
\]

uniformly because \(D/n=\alpha+O(1/n)\).

Apply Doob's \(L^2\) maximal inequality to \(M_k\) on the first half of the bridge and to the time-reversed bridge on the second half. There is a constant \(C_0(\alpha)\) such that

\[
\boxed{
P\left(
\max_{k\le n}|S_k|\ge A
\mid X_n=D
\right)
\le C_0\frac{n}{A^2}.
}
\]

Choose a fixed \(C_1\) large enough and put

\[
A=C_1\sqrt n.
\]

Then the conditional probability of

\[
\max_{k\le n}|S_k|<A
\]

is bounded below by an absolute positive constant.

## 3. Mechanical and bridge centering differ only by O(1)

For \(0\le k\le n\),

\[
\begin{aligned}
D_a(k)-\frac{kD_a(n)}n
&=
(D_a(k)-\alpha k)
-
\frac{k}{n}(D_a(n)-\alpha n).
\end{aligned}
\]

Hence

\[
\boxed{
\left|D_a(k)-\frac{kD_a(n)}n\right|<2.
}
\]

Thus on the conditioned bridge event,

\[
|X_k-D_a(k)|\le A+2.
\]

A bridge starting at a strip state whose distance from both walls is at least \(A+3\) therefore remains inside the record strip throughout the middle block.

## 4. Entrance and exit connectors of length O(sqrt L)

Fix

\[
y_*=C_2\sqrt L
\]

with \(C_2>C_1+4\), rounded to an integer.

### Entrance

Starting at \(y=0\), force parity zero. Then

\[
y_j=D_s(j)
\]

is monotone and increases only on mechanical rises.

Because the mechanical word contains no \(00\), every pair of mechanical steps contains at least one rise. Therefore the first time \(y=y_*\) is reached has length at most

\[
2y_*+1=O(\sqrt L).
\]

### Exit

Working backward from the prescribed final plateau-odd record exit, force parity one through the shortest suffix containing exactly \(y_*\) mechanical plateaus. Under parity one, the strip state decreases by one at every plateau and stays fixed at every rise.

Because the mechanical word contains no \(111\), every three consecutive mechanical steps contain a plateau. Hence this exit connector has length at most

\[
3y_*+O(1)=O(\sqrt L).
\]

The final plateau-odd step then exits from \(y=0\) to \(y=-1\).

All connector bits together have Bernoulli probability at least

\[
\boxed{
\exp(-C_3\sqrt L)
}
\]

for a constant depending only on \(\alpha\).

## 5. The middle bridge has probability c/sqrt L

After removing the two connectors and the final exit, the remaining middle length is

\[
n=L-O(\sqrt L).
\]

For all sufficiently large \(L\),

\[
n\asymp L.
\]

The exact return condition is

\[
X_n=D_a(n).
\]

Since \(|D_a(n)-\alpha n|<1\), uniform Stirling bounds give

\[
\boxed{
P_\alpha(X_n=D_a(n))\ge\frac{c_0}{\sqrt n}
\ge\frac{c_1}{\sqrt L}.
}
\]

By the bridge maximal estimate, a fixed positive fraction of this endpoint mass stays within \(A=O(\sqrt L)\) of its linear interpolation and therefore remains inside the interior corridor around \(y_*\).

Thus the safe middle loop has probability at least

\[
\boxed{
\frac{c_2}{\sqrt L}.
}
\]

## 6. Short-width record mass lower bound

The construction fits inside the strip whenever

\[
r\ge y_*+A+3.
\]

Since both \(y_*\) and \(A\) are fixed constants times \(\sqrt L\), there is a constant \(c_*>0\) such that the construction works whenever

\[
\boxed{L\le c_*r^2.}
\]

Multiplying entrance, bridge, exit, and final-step probabilities gives

\[
\boxed{
P_\alpha(\mathcal R_{s,r}(L))
\ge
c\,L^{-1/2}\exp(-C\sqrt L)
}
\]

uniformly in phase \(s\), record height \(r\), and every nonempty record length in this regime.

Therefore

\[
\boxed{
K_\alpha(\mathcal R)
\le
C\sqrt L+\frac12\log L+O(1).
}
\]

In particular,

\[
\boxed{
L\to\infty,\quad L\le c_*r^2
\quad\Longrightarrow\quad
\frac{K_\alpha}{L}\to0.
}
\]

## 7. Complementary long-width regime

For

\[
L>c_*r^2,
\]

use the earlier central \(r^2\)-loop construction. Choosing the loop-block constant small enough to satisfy the same bridge maximal inequality gives

\[
K_\alpha
\le
C\left[
r+\left(\frac{L}{r^2}+1\right)\log r\right].
\]

If \(r\to\infty\), then uniformly in this complementary regime,

\[
\frac{K_\alpha}{L}
=O\left(\frac1r+\frac{\log r}{r^2}\right)
\to0.
\]

## 8. Unified unbounded-record theorem

Along every infinite nonperiodic coefficient-surviving orbit we already proved

\[
r\to\infty.
\]

Combining the two regimes gives:

\[
\boxed{
L_r\to\infty
\quad\Longrightarrow\quad
\frac{K_\alpha(\mathcal R_{\tau_r,r}(L_r))}{L_r}\to0.
}
\]

The entropy--Haar dichotomy therefore implies that for every fixed \(\eta>0\), all but \(o(L_r)\) dyadic valuation levels of such a record satisfy

\[
\boxed{
|\widehat\mu(t)|
\le
|2\alpha-1|+\eta
<1
}
\]

for sufficiently small fixed \(\eta\).

Hence the record-side coarse Fourier problem is closed whenever record lengths are unbounded.

## 9. Remaining deterministic regime

The only remaining record-length alternative is:

\[
\boxed{
\sup_r L_r<\infty.
}
\]

The companion bounded-record notes now show that in this regime:

- singleton macros have length at most four and cannot form an infinite tail;
- non-singleton macros occur infinitely often;
- every non-singleton macro has an exact terminal Haar shell with contraction at most \(\kappa_M<1\) under a fixed bound \(M\).

Thus all record-length geometry has now been reduced to the bounded-record repeated fresh-shell selector/Hensel splice.

Companion finite regression:

`collatz/src/unbounded_record_corridor_bridge_certificate.py`.
