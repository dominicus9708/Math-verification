# Adelic parity-series bridge and record-height occupation bound

Date: 2026-08-20

Status: **exact common real/2-adic coordinate plus a literature-assisted necessary condition for any infinite nonperiodic Collatz orbit.** This is not a proof of the Collatz conjecture.

We use the accelerated map

\[
T(x)=\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

Let

\[
p_1<p_2<\cdots
\]

be the zero-indexed positions of odd steps, and let \(m_k\) be the number of odd steps among positions \(0,\ldots,k-1\).

Define

\[
\boxed{
S_n:=\sum_{i=1}^n\frac{2^{p_i}}{3^i}.
}
\]

## 1. Exact finite parity-series identity

The affine iterate has correction

\[
R_k=\sum_{i=1}^{m_k}3^{m_k-i}2^{p_i},
\]

so

\[
T^k(N)=\frac{3^{m_k}N+R_k}{2^k}.
\]

Dividing by \(3^{m_k}/2^k\) gives

\[
\boxed{
V_k:=\frac{2^kT^k(N)}{3^{m_k}}
=N+S_{m_k}.
}
\]

This is exactly the real correction coordinate previously denoted by \(v\).

At an even step \(V\) is unchanged. At an odd step,

\[
\boxed{
V_{k+1}=V_k\left(1+\frac1{3T^k(N)}\right).
}
\]

Therefore

\[
\boxed{
V_k
=N\prod_{\substack{0\le j<k\\T^j(N)\text{ odd}}}
\left(1+\frac1{3T^j(N)}\right).
}
\]

## 2. The same series is the 2-adic inverse-conjugacy series

Because

\[
N+S_{m_k}
=
\frac{2^kT^k(N)}{3^{m_k}},
\]

and \(3^{m_k}\) is odd, the 2-adic valuation of the right-hand side is at least \(k\). Hence

\[
\boxed{
N+S_{m_k}\longrightarrow0
\quad\text{in }\mathbb Z_2.
}
\]

For an infinite orbit there are infinitely many odd steps, so

\[
\boxed{
S_n\longrightarrow-N
\quad\text{in }\mathbb Z_2.
}
\]

This is the finite-orbit derivation of the Bernstein/Lagarias inverse parity-conjugacy formula

\[
N=-\sum_{i\ge1}\frac{2^{p_i}}{3^i}
\quad(2\text{-adically}).
\]

The important point for the present proof program is that the *same rational partial sums* \(S_n\) also have a real interpretation through \(V_k\).

## 3. Garcia--Tal/Heppner input and reciprocal summability

Garcia and Tal (1999), using Heppner's theorem, prove that a complete representative set \(P\) for the generalized Collatz orbit equivalence relation obeys, in the classical \(d=2,m=3\) case,

\[
\#(P\cap\{a,\ldots,a+K-1\})
\le
2(\lfloor\log_2K\rfloor+1)
\left(K^{1-\delta_1}+g(K)\right),
\]

where \(\delta_1,\delta_2\in(0,1)\) and

\[
g(K)=O(K^{\delta_2}).
\]

For an infinite nonperiodic orbit \(O(N)\), their Corollary 1 permits a representative set with

\[
O(N)\subset P.
\]

Put

\[
\beta:=\max(1-\delta_1,\delta_2)<1.
\]

Then, after absorbing constants,

\[
\boxed{
\#(O(N)\cap[a,a+K))
\ll (1+\log K)K^\beta.
}
\]

On the dyadic shell \([2^r,2^{r+1})\),

\[
\sum_{x\in O(N)\cap[2^r,2^{r+1})}\frac1x
\ll
(r+1)2^{-(1-\beta)r}.
\]

The shell series converges, hence

\[
\boxed{
\sum_{x\in O(N)}\frac1x<\infty.
}
\]

This reciprocal-summability statement is a short consequence of the quantitative Garcia--Tal bound; it is not quoted there as a separately named theorem.

## 4. Real convergence of the same parity series

Reciprocal summability makes the correction product converge:

\[
\boxed{
V_k\uparrow V_\infty<\infty.
}
\]

Hence

\[
\boxed{
S_n\longrightarrow V_\infty-N>0
\quad\text{in }\mathbb R.
}
\]

Thus the same formal positive rational series has two completion-dependent limits:

\[
\boxed{
S_n\to V_\infty-N\quad(\mathbb R),
\qquad
S_n\to-N\quad(\mathbb Q_2).
}
\]

This is the cleanest current bridge between the real correction coordinate and the 2-adic Hensel/parity coordinate.

## 5. Height escape

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil \alpha k\rceil,
\qquad
h_k=m_k-b_k.
\]

Write

\[
\delta_k=b_k-\alpha k\in[0,1).
\]

Since

\[
\frac{3^{b_k}}{2^k}=3^{\delta_k},
\]

the exact identity becomes

\[
\boxed{
T^k(N)=3^{h_k+\delta_k}V_k.
}
\]

Therefore

\[
N3^{h_k}
\le T^k(N)
<3V_\infty 3^{h_k}.
\]

If an infinite nonperiodic orbit had infinitely many indices with \(h_k\le H\), then infinitely many distinct orbit values would lie in the finite interval

\[
[1,3V_\infty3^H],
\]

which is impossible. Consequently

\[
\boxed{
h_k\longrightarrow+\infty.}
\]

This is stronger than mere unboundedness of the parity surplus.

## 6. Quantitative low-height occupation bound

The same orbit-count estimate gives a quantitative refinement. If \(h_k\le r\), then

\[
T^k(N)<3V_\infty3^r.
\]

Because the orbit is nonperiodic, its values are distinct. Therefore

\[
\boxed{
\#\{k:h_k\le r\}
\ll
(r+1)3^{\beta r}.
}
\]

This is the correct quantitative consequence.

A previous scratch interpretation that this directly implied a pointwise bound

\[
h_k\ge c\log k-O(\log\log k)
\]

for every large \(k\) was too strong. The occupation estimate instead implies such a logarithmic lower bound for the **record maximum** and bounds the duration of each record first-passage excursion.

If

\[
\tau_r:=\min\{k:h_k=r\},
\qquad
L_r:=\tau_{r+1}-\tau_r,
\]

then every index before \(\tau_{r+1}\) has height at most \(r\), so

\[
\boxed{
\tau_{r+1}\ll(r+1)3^{\beta r},
\qquad
L_r\ll(r+1)3^{\beta r}.
}
\]

## 7. Record first-passage structure

Between \(\tau_r\) and \(\tau_{r+1}\), define the relative discrepancy

\[
g_j
=
q_j-\left(b_{\tau_r+j}-b_{\tau_r}\right).
\]

Then

\[
-r\le g_j\le0
\qquad(0\le j<L_r),
\]

and

\[
\boxed{g_{L_r}=1.}
\]

The final step must therefore be an odd step on a Beatty plateau:

\[
\boxed{
T^{\tau_{r+1}-1}(N)\text{ odd},
\qquad
b_{\tau_{r+1}}=b_{\tau_{r+1}-1}.
}
\]

Hence every record endpoint satisfies

\[
\boxed{
T^{\tau_r}(N)\equiv2\pmod3
\qquad(r\ge1).
}
\]

The record macro is therefore a finite-width Beatty first-passage word carrying a forced ternary low digit.

## 8. Revised final cross-base object

The remaining divergent-tail object can now be stated simultaneously in three equivalent coordinates:

1. a parity discrepancy path in the strip \(-r\le g\le0\) ending at \(+1\);
2. a dyadic residue/Hensel word of length \(L_r\);
3. a partial sum of the adelic series
   \[
   S_n=\sum2^{p_i}/3^i
   \]
   which must converge to a positive real number but to \(-N\) 2-adically.

The next deterministic target is therefore a finite-width Beatty-strip Fourier/Hensel transversality theorem rather than an unrestricted coefficient-language theorem.

Certificate:

`collatz/src/adelic_parity_record_bridge_certificate.py`.

External inputs used here:

- M. V. P. Garcia and F. A. Tal, *A note on the generalized 3n+1 problem*, Acta Arith. 90 (1999), 245--250, especially Theorem 1, equation (6), and Corollary 1.
- The 2-adic inverse parity-series formula is classical Bernstein/Lagarias conjugacy; the finite identity above is derived directly and does not require the conjugacy theorem.
