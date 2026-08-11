# Centered survivor-channel normal form and generating-function calculus

Date: 2026-08-11

Status: **exact reduction and exact set-generating representation**. This note does not claim a proof of the Collatz conjecture.

## 1. Centered exact survivor channel

Let a depth-k unresolved interval channel be re-centered at its least represented natural number. Write

\[
\boxed{n=\rho+2^k t,\qquad 0\le t\le N,}
\]

where \(N\in\mathbb Z_{\ge0}\cup\{+\infty\}\), and let

\[
\boxed{T^k(n)=\rho+h+u t.}
\]

Here

- \(\rho\) is the least unresolved natural represented by the channel;
- \(h=T^k(\rho)-\rho\ge0\) is the current headroom of the least representative;
- \(u=3^q\) is the exact affine lift multiplier;
- \(N\) is the centered channel width;
- \(k\) is the dyadic depth.

Thus the exact channel is represented by

\[
\boxed{s=(k,\rho,h,u,N).}
\]

This is equivalent to the earlier state \((k,r,d,u,[L,U])\) under

\[
\rho=r+2^kL,
\qquad
h=d+(u-2^k)L,
\qquad
N=U-L.
\]

The represented set is

\[
\boxed{\llbracket s\rrbracket=\{\rho+2^k t:0\le t\le N\}.}
\]

The current-depth no-descent difference is

\[
\boxed{T^k(n)-n=h+(u-2^k)t.}
\]

Hence the lower representative is always unresolved because \(h\ge0\), while the sign of \(u-2^k\) determines whether the current constraint can impose a finite upper width.

---

## 2. Exact child transition

Split the centered lift coordinate by

\[
t=c+2t',\qquad c\in\{0,1\}.
\]

If \(N<\infty\), the inherited child width is

\[
N_c=\left\lfloor\frac{N-c}{2}\right\rfloor
\]

whenever \(c\le N\); if \(N=+\infty\), then \(N_c=+\infty\).

The unshifted child lower start is

\[
\rho_c=\rho+c2^k.
\]

At depth k its endpoint is

\[
\rho+h+cu+2u t'.
\]

Because \(u\) is odd, the next parity is constant on the child and equals

\[
\boxed{p=(\rho+h+c)\bmod2.}
\]

Define

\[
\boxed{u'=3^p u}
\]

and the unshifted child endpoint at \(t'=0\),

\[
z_c'
=
\frac{3^p(\rho+h+cu)+p}{2}.
\]

Its new headroom intercept is

\[
\boxed{A_c=z_c'-\rho_c}
\]

and its new slope is

\[
\boxed{B_c=u'-2^{k+1}.}
\]

The new no-descent condition is exactly

\[
\boxed{A_c+B_c t'\ge0.}
\]

Intersect this half-line with \(0\le t'\le N_c\). If the resulting integer interval is empty, the child is removed. Otherwise write it as

\[
J_c\le t'\le K_c.
\]

Re-center with \(t'=J_c+t''\). Then

\[
\boxed{
\rho'=\rho_c+2^{k+1}J_c,
}
\]

\[
\boxed{
h'=A_c+B_cJ_c,}
\]

\[
\boxed{N'=K_c-J_c,}
\]

and

\[
\boxed{T^{k+1}(\rho'+2^{k+1}t'')=\rho'+h'+u't''.}
\]

Thus the centered state family

\[
\boxed{(k,\rho,h,u,N)}
\]

is exactly closed under unresolved refinement.

---

## 3. Unresolved-set generating function

For each depth k define

\[
\boxed{F_k(z):=\sum_{n\in U_k}z^n,\qquad 0<z<1.}
\]

Because the exact survivor channels partition \(U_k\),

\[
\boxed{F_k(z)=\sum_{s\in K_k}G_s(z),}
\]

where a centered channel has rational generating function

\[
\boxed{
G_s(z)=
 z^\rho\frac{1-z^{2^k(N+1)}}{1-z^{2^k}}
}
\]

for finite \(N\), and

\[
\boxed{
G_s(z)=\frac{z^\rho}{1-z^{2^k}}
}
\]

for \(N=+\infty\).

Hence an infinite arithmetic-progression survivor range is represented exactly by one rational function rather than by enumeration of its members.

---

## 4. Exact binary splitting in generating-function form

Before the new no-descent filter is applied, the two parity children form a disjoint partition of the parent range. Therefore

\[
\boxed{G_s(z)=G^{\rm inh}_{s,0}(z)+G^{\rm inh}_{s,1}(z).}
\]

After intersecting each child with its exact half-line \(A_c+B_ct'\ge0\), let \(G^{\rm surv}_{s,c}(z)\) be the surviving child generating function. Then

\[
0\le G^{\rm surv}_{s,c}(z)\le G^{\rm inh}_{s,c}(z)
\]

for \(0<z<1\), and the removed component is

\[
\boxed{R_{s,c}(z):=G^{\rm inh}_{s,c}(z)-G^{\rm surv}_{s,c}(z)\ge0.}
\]

Summing over all parent channels gives the exact dissipation identity

\[
\boxed{
F_{k+1}(z)=F_k(z)-R_{k+1}(z),
}
\]

where

\[
R_{k+1}(z)=\sum_{s\in K_k}\sum_{c=0}^1R_{s,c}(z).
\]

This identity is coefficientwise: each coefficient records whether a particular natural number remains unresolved.

---

## 5. Relation to the full-support generating mass

For any fixed \(z\in(0,1)\), define

\[
M_k(z)=\sum_{n\in U_k}(1-z)z^{n-2}.
\]

Then

\[
\boxed{M_k(z)=(1-z)z^{-2}F_k(z).}
\]

Thus the earlier full-support mass is simply a normalized evaluation of the unresolved-set generating function. No averaging assumption is introduced: the coefficients of \(F_k\) remain the exact 0/1 membership data of \(U_k\).

Since \(U_{k+1}\subseteq U_k\), monotone convergence gives

\[
\boxed{
\lim_{k\to\infty}F_k(z)
=
\sum_{n\in\cap_k U_k}z^n.
}
\]

Therefore, for any one fixed \(z\in(0,1)\),

\[
\boxed{
\text{Collatz}
\iff
F_k(z)\to0
\iff
M_k(z)\to0.
}
\]

Every positive integer carries a positive coefficient \(z^n\), so a finite or sparse counterexample set cannot disappear in the limit.

---

## 6. Proof-design consequence

The exact proof problem can now be expressed as a stability problem for a positive rational generating-function state.

The remaining task is not to evaluate larger finite ranges. It is to construct a fixed attribute map and either:

1. a universal generating-mass contraction certificate;
2. a frontier-escape theorem;
3. or a mixed certificate in which failure of contraction forces strict well-founded progress.

The centered exact state \((k,\rho,h,u,N)\) is the current minimal lossless state candidate from which such an attribute quotient should be built.
