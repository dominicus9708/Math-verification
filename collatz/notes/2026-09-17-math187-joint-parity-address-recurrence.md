# MATH-187 — joint one-step recurrence for depth, paid count, phase, affine correction, and exact address

Date: 2026-09-17

Status: `EXACT STRUCTURAL RECURRENCE / r=1..21 AND k=2..41 COMMON TRANSITION / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-179 gives a common Beatty clock for paid counts `1<=r<=21` and global depths `2<=k<=41`, but its note still presents the phase, depth, and exact-address channels as parallel ingredients.

The present note writes one exact shortcut-step transition that updates all of the following at once:

- global depth and odd/even counts;
- coefficient slack and phase;
- normalized correction / fixed-d signature coordinates;
- paid penalty and paid-event counter;
- exact same-integer affine cylinder and source multiplicity.

The MATH-051 Hensel witness subset remains a separate product channel; no unsupported identification of the Hensel carry with the address carry is made.

No Collatz closure claim is made.

## 2. Common clock

Let

\[
\theta=\log_2(3/2),
\qquad
m(q)=\lfloor q\theta\rfloor,
\]

and define the Beatty increment

\[
\boxed{\delta_q:=m(q+1)-m(q)\in\{0,1\}.}
\]

For a global parity prefix let

\[
k=\text{depth},\qquad q=\text{odd count},\qquad d=k-q,
\]

\[
\boxed{u:=m(q)-d,}
\]

\[
\Omega_q:=\frac{2^{q+m(q)}}{3^q},
\qquad
\rho:=\frac{2^k}{3^q}=2^{-u}\Omega_q.
\]

Let the next actual shortcut parity bit be

\[
b\in\{0,1\},
\]

with `b=0` for an even shortcut step and `b=1` for an odd shortcut step.

## 3. Single clock recurrence

The exact count update is

\[
\boxed{k'=k+1,}
\]

\[
\boxed{q'=q+b,}
\]

\[
\boxed{d'=d+1-b.}
\]

Therefore the coefficient slack obeys the single formula

\[
\boxed{
 u'=u-1+b(1+\delta_q).
}
\]

Indeed:

- even: `u'=u-1`;
- odd: `u'=u+delta_q`.

The coefficient ratio obeys

\[
\boxed{
\rho'=\frac{2}{3^b}\rho.
}
\]

The Beatty phase clock obeys

\[
\boxed{
\Omega_{q'}
=\Omega_q
\left(\frac{2^{1+\delta_q}}3\right)^b.
}
\]

Thus the MATH-179 phase step and the MATH-072 depth/slack step are the same clock viewed at odd-count and global-depth resolutions.

## 4. Normalized correction recurrence

Write the affine shortcut prefix as

\[
T^k(N)=\frac{3^qN+C}{2^k}
=\frac{N+S}{\rho},
\qquad
S:=\frac{C}{3^q}.
\]

MATH-072 gives the exact one-step update

\[
\boxed{
S'=S+\frac{b\rho}{3}.
}
\]

Let

\[
\Sigma:=S+\rho-1.
\]

Then equivalently

\[
\boxed{
\Sigma'=\Sigma+(1-b)\rho.
}
\]

So the same bit `b` updates the two dual correction coordinates:

- odd steps increase `S` and leave `Sigma` fixed;
- even steps leave `S` fixed and increase `Sigma`.

## 5. Paid penalty recurrence

Inside the coefficient-valid region `u>=0`, MATH-072 gives the paid-odd penalty atom

\[
p=\frac{\Omega_q-\rho}{3}.
\]

At `u=0`, `rho=Omega_q`, so this increment is exactly zero. At `u>0`, it is strictly positive.

Hence one exact recurrence covers both mechanical zero-cost odd steps and positive-slack paid odd steps:

\[
\boxed{
\mathcal P'
=\mathcal P
+\frac{b}{3}(\Omega_q-\rho).
}
\]

Define the paid-event indicator

\[
\boxed{
\pi:=b\,\mathbf 1_{\{u>0\}}.
}
\]

If `c` is the paid-event count inside the current positive-slack excursion, then

\[
\boxed{c'=c+\pi.}
\]

When an even step returns to `u'=0`, the completed cluster is tagged by

\[
\boxed{r=c'}
\]

and the next excursion restarts with counter zero.

Therefore `r=1..21` does not require 21 unrelated transition laws. It is a terminal tag produced by repeated application of the same one-step recurrence.

## 6. Exact same-integer cylinder

Represent the current source and endpoint families by

\[
\boxed{
N=A+2^H s,
\qquad
Y=B+3^Q s,
\qquad
0\le s<M.
}
\]

This is the MATH-061 canonical affine-cylinder form.

The actual endpoint parity condition is

\[
B+3^Qs\equiv b\pmod2.
\]

Because `3^Q` is odd, modulo 2 this fixes one exact parameter parity

\[
\boxed{
\eta:=(b-B)\bmod2\in\{0,1\},
}
\]

so

\[
s=\eta+2t.
\]

The compatible child multiplicity is exactly

\[
\boxed{
M'=\left\lfloor\frac{M+1-\eta}{2}\right\rfloor.
}
\]

If `M'=0`, the branch is empty.

Otherwise the source cylinder becomes

\[
\boxed{
A'=A+2^H\eta,
\qquad
H'=H+1.
}
\]

The endpoint cylinder becomes

\[
\boxed{
Q'=Q+b,
}
\]

\[
\boxed{
B'
=\frac{3^b(B+3^Q\eta)+b}{2}.
}
\]

Therefore

\[
\boxed{
Y'=B'+3^{Q'}t.
}
\]

This is an exact same-integer update. No density or random-parity assumption is used.

## 7. Resolution update

Let

\[
R=\lceil\log_2M\rceil,
\qquad R(1)=0.
\]

Since one shortcut step selects one parity class of the parameter,

\[
\boxed{
R'\le\max(0,R-1).
}
\]

Iterating `ell` exact shortcut steps recovers MATH-074:

\[
\boxed{
R_{n+\ell}\le\max(0,R_n-\ell).
}
\]

Thus the one-step address recurrence is the microscopic version of the MATH-061 composition law and the MATH-074 resolution lemma.

## 8. Unified transition operator

Ignoring only the separate Hensel witness subset, define the observable state

\[
\mathscr S=
(k,q,d,u,\Omega,\rho,S,\Sigma;
 c,\mathcal P;
 A,H,B,Q,M).
\]

Then for actual parity `b` the common transition

\[
\boxed{
\mathscr S'=F_b(\mathscr S)
}
\]

is given simultaneously by

\[
\boxed{
\begin{aligned}
k'&=k+1,\\
q'&=q+b,\\
d'&=d+1-b,\\
u'&=u-1+b(1+\delta_q),\\
\rho'&=2\rho/3^b,\\
\Omega'&=\Omega\left(2^{1+\delta_q}/3\right)^b,\\
S'&=S+b\rho/3,\\
\Sigma'&=\Sigma+(1-b)\rho,\\
\mathcal P'&=\mathcal P+b(\Omega-\rho)/3,\\
c'&=c+b\mathbf1_{\{u>0\}},\\
\eta&=(b-B)\bmod2,\\
M'&=\left\lfloor(M+1-\eta)/2\right\rfloor,\\
A'&=A+2^H\eta,\\
H'&=H+1,\\
Q'&=Q+b,\\
B'&=\bigl(3^b(B+3^Q\eta)+b\bigr)/2.
\end{aligned}
}
\]

The branch exists only when `M'>0` and the proof-language side conditions remain valid.

This is the requested common recurrence core: `r` is accumulated by the paid-event counter and `k` is advanced by the same steps, so all `1<=r<=21` and `2<=k<=41` states can be generated by one transition system rather than separate formulas.

## 9. Redundant coordinates and minimal implementation core

Several displayed coordinates are algebraically redundant:

\[
d=k-q,
\]

\[
u=m(q)-(k-q),
\]

\[
\Omega=\frac{2^{q+m(q)}}{3^q},
\]

\[
\rho=\frac{2^k}{3^q},
\]

\[
S=1+\Sigma-\rho.
\]

Therefore an implementation need not physically store all of them.

A reduced analytic/address core may be taken as

\[
\boxed{
(k,q,\Sigma,c,\mathcal P;A,H,B,Q,M)
}
\]

with the remaining quantities derived exactly when needed.

However `Q` must not be identified with `q` merely because they coincide under one common origin. In the product construction, the depth/Hensel channel and a composed macro-address channel may use different origins. They should be kept distinct unless an explicit synchronization invariant is imposed.

## 10. Hensel product channel

MATH-051 uses the fixed-d signature together with a bounded-carry / viable-witness subset state. Denote that finite-state object by

\[
\mathcal H.
\]

The complete proof-facing product state is therefore

\[
\boxed{
\mathscr S_{\rm full}
=(k,q,\Sigma,\mathcal H;
 c,\mathcal P;
 A,H,B,Q,M).
}
\]

Its transition is

\[
\boxed{
F_b^{\rm full}
=F_b^{\rm clock/affine/address}
\times
\Phi_b^{\rm Hensel},
}
\]

where `Phi_b^Hensel` is the exact MATH-051 bounded-carry/witness-subset transition.

No claim is made that `mathcal H` equals the dyadic address carry.

## 11. Relation to MATH-186

For a block of repeated one-step transitions, the exact multiplicity recurrence gives the source-resolution decrease used by MATH-186.

The accumulated penalty recurrence gives the same `P_r` used by MATH-185.

Thus the boundary-transfer theorem is not an external rule layered on top of this recurrence; it is a block inequality derived from repeated applications of the same one-step map.

This is useful for the intended executor:

1. advance one exact state with `F_b`;
2. tag first returns to `u=0` by paid count `r`;
3. tag global depth `k` directly;
4. apply MATH-186/MATH-074 resolution safety on blocks;
5. invoke the MATH-051 Hensel product state without collapsing the carry channels.

## 12. Claim boundary

Established:

- one exact parity-step recurrence for global depth, odd/even counts, slack, phase, coefficient ratio, normalized correction, signature, paid penalty, paid count, exact source address, endpoint affine coefficient, and source multiplicity;
- `r` and `k` are outputs of one transition system, not separate recurrence families;
- repeated address steps recover the MATH-061/MATH-074 dyadic composition law;
- the recurrence preserves exact same-integer lineage.

Not established:

- a bounded-size arbitrary-depth Hensel witness state beyond the audited MATH-051 scope;
- a universal singleton terminal closure theorem;
- first-cell emptiness;
- the Collatz conjecture.
