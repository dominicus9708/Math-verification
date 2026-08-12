# R2 dyadic paradoxical lifts in Beatty-skew coordinates

Date: 2026-08-12

Status: **exact bridge theorem combining the R2 skew formulation with Rozier--Terracol Theorem 3.2 (Discrete Mathematics 349 (2026), arXiv:2502.00948v5)**. It does not reduce R2 to the R1 renewal branch, because the lifted paradoxical starts are even and descend immediately through their initial dyadic prefix.

## 1. External input

Rozier--Terracol prove that if an integer `N>=2` has infinite stopping time, then infinitely many paradoxical sequences start from integers of the form

\[
2^kN.
\]

Their proof considers pairs `(a,b)` satisfying

\[
1-\frac1{4N}<\frac{3^a}{2^b}<1,
\]

lets `j` be the least step count for which the first `j` parity entries contain `a` odd terms, and splits into `j>=b` and `j<b`.

## 2. The R2 branch forces the dyadic-lift case

Assume now that `N` is an R2 start:

\[
\tau_c(N)=\infty.
\]

Then for every finite step count `j`,

\[
\frac{3^{q_j(N)}}{2^j}>1.
\]

Hence the Rozier--Terracol case `j>=b` is impossible: if `q_j(N)=a` and `j>=b`, then

\[
\frac{3^a}{2^j}\le\frac{3^a}{2^b}<1,
\]

contradicting `tau_c(N)=infinity`.

Therefore every pair used in their construction must satisfy

\[
\boxed{j<b.}
\]

The paradoxical start is

\[
\boxed{m=2^kN,\qquad k=b-j>0.}
\]

## 3. The pair lies on the nearest upper layer

Put

\[
\gamma:=\log_2 3.
\]

For `N>=2`,

\[
\frac{3^a}{2^b}>1-\frac1{4N}\ge\frac78>\frac12.
\]

Since `3^a/2^b<1`,

\[
0<b-a\gamma<1.
\]

Thus

\[
\boxed{b=\lceil a\gamma\rceil.}
\]

Write

\[
\delta_a:=b-a\gamma=1-\{a\gamma\}.
\]

Then the external pair condition is

\[
\boxed{
0<\delta_a< -\log_2\left(1-\frac1{4N}\right).
}
\]

## 4. Exact lift exponent in R2 skew coordinates

Let

\[
A_i=\sum_{r<i}v_r,
\qquad
s_i=\lfloor i\gamma\rfloor-A_i,
\]

and

\[
r_i=\lfloor(i+1)\gamma\rfloor-\lfloor i\gamma\rfloor\in\{1,2\}.
\]

The least step count whose parity prefix contains `a` odd entries is

\[
\boxed{j=A_{a-1}+1.}
\]

Since the pair gap `delta_a` above is less than

\[
-\log_2(7/8)<2-\gamma,
\]

one has

\[
\{(a-1)\gamma\}=2-\gamma-\delta_a
\]

and consequently

\[
\boxed{r_{a-1}=1.}
\]

Therefore

\[
\begin{aligned}
k
&=b-j\\
&=\lceil a\gamma\rceil-A_{a-1}-1\\
&=\lfloor a\gamma\rfloor-A_{a-1}\\
&=s_{a-1}+r_{a-1}\\
&=\boxed{s_{a-1}+1}.
\end{aligned}
\]

Thus every Rozier--Terracol paradoxical lift generated from an R2 start has the exact form

\[
\boxed{
m_a=2^{s_{a-1}+1}N.}
\]

This gives the R2 skew displacement a direct dynamical meaning: at the near-upper-layer rotation hits used in Theorem 3.2, `s_{a-1}+1` is exactly the number of initial halvings that must be prepended to turn the divergent R2 prefix into a paradoxical sequence.

## 5. Exact paradoxical inequality in odd-event variables

Put

\[
\theta_a:=\frac{3^a}{2^b}=2^{-\delta_a}.
\]

At step

\[
j=A_{a-1}+1
\]

the orbit has just applied the odd branch to the `(a-1)`st odd-event state. Using

\[
x_{a-1}=\frac{N+c_{a-1}}{\lambda_{a-1}},
\]

we obtain

\[
T^j(N)
=2^k\theta_a(N+c_{a-1})+\frac12.
\]

Since the lifted paradoxical endpoint equals `T^j(N)` and the lifted start is `2^kN`, paradoxicality is exactly

\[
\boxed{
(1-\theta_a)N
\le
\theta_a c_{a-1}+2^{-k-1}.
}
\]

Using `k=s_{a-1}+1`,

\[
\boxed{
(1-\theta_a)N
\le
\theta_a c_{a-1}+2^{-s_{a-1}-2}.
}
\]

This is an exact real bridge between the Diophantine near-resonance gap, the R2 harmonic correction, and the skew height.

## 6. Why this does not collapse R2 into R1

The lifted start

\[
m=2^kN
\]

is even. Its first iterate is `m/2<m`, so it has ordinary stopping time one and coefficient below one immediately.

Hence these lifted paradoxical sequences are not renewal-floor first coefficient crossings of the R1 type. They are finite sequences that first descend through a dyadic prefix to `N` and later rise back above the larger start `m`.

Therefore

\[
\boxed{\text{R2 does not reduce to R1 through Theorem 3.2}.}
\]

The theorem instead supplies an exact external interpretation of the R2 skew heights and an infinite family of dyadic paradoxical lifts.

## 7. Harmonic consequence

The R2 harmonic theorem gives

\[
c_{a-1}=O_N(a^{1/9}).
\]

Thus along the Rozier--Terracol near-resonance indices,

\[
(1-\theta_a)N
\le
O_N(a^{1/9})+2^{-s_{a-1}-2}.
\]

The external construction permits `theta_a` to approach one arbitrarily closely, so this inequality is compatible with R2 and does not itself yield a contradiction.

Likewise, Rozier--Terracol's harmonic-mean necessary condition forces these lifted coefficients increasingly close to one as the R2 odd states diverge, but their continued-fraction construction already supplies arbitrarily close upper-layer approximants.

## 8. Role

This bridge closes a possible false route: R2 cannot simply be renamed as R1 by invoking the divergent-to-paradoxical theorem.

What it does establish is the exact dictionary

\[
\boxed{
\text{R2 skew height at a near-critical rotation hit}
\longleftrightarrow
\text{dyadic exponent of a paradoxical lift}.
}
\]

Any future global contradiction involving the abundance, starting sizes, or arithmetic structure of paradoxical sequences can therefore be translated directly into constraints on the R2 skew path.