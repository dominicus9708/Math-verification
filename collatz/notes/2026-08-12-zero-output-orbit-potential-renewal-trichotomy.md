# Zero-output orbit potential and renewal endpoint classification

Date: 2026-08-12

Status: **exact orbit-side identities plus renewal endpoint record/cost theorems** for the post-formation (`t_q=0`) regime. This does not prove Collatz. It removes formation variables from the long tail and sharply restricts what a genuine next renewal floor can look like.

## 1. Orbit-side harmonic potential

Assume the canonical lift output has stabilized at zero, so the least formation representative is one fixed positive odd integer `N` and the odd Syracuse orbit is

\[
x_{q+1}=\frac{3x_q+1}{2^{v_q}},\qquad v_q=v_2(3x_q+1).
\]

Put

\[
A_q:=\sum_{i<q}v_i,\qquad \gamma:=\log_2 3,
\]

and the signed critical skew

\[
s_q:=\lfloor q\gamma\rfloor-A_q.
\]

Let

\[
\theta_q:=\{q\gamma\}.
\]

The standard odd-event affine correction is

\[
c_q:=\sum_{i=0}^{q-1}\frac{2^{A_i}}{3^{i+1}},
\]

and the exact state identity is

\[
\boxed{x_q=(N+c_q)2^{s_q+\theta_q}.}
\]

Define the orbit potential

\[
\boxed{\mathcal H_q:=\log_2x_q-s_q-\theta_q.}
\]

Then exactly

\[
\boxed{\mathcal H_q=\log_2(N+c_q).}
\]

Since

\[
N+c_{q+1}=(N+c_q)\left(1+\frac1{3x_q}\right),
\]

we get the formation-independent update

\[
\boxed{
\mathcal H_{q+1}-\mathcal H_q
=\log_2\left(1+\frac1{3x_q}\right)>0.
}
\]

Thus `mathcal H_q` is a genuine monotone quantity transported by the actual Syracuse orbit after formation has ended.

## 2. Renewal-tail adiabatic corridor

Restart the coordinates at a renewal floor `N`, meaning every later odd-event state in the considered suffix is at least `N`.

Let `c_m^(N)` and `mathcal H_m^(N)` be the corresponding tail correction and potential. Then

\[
\mathcal H_m^{(N)}-\log_2N
=\log_2\left(1+\frac{c_m^{(N)}}N\right).
\]

The previously proved uniform harmonic suffix bound gives

\[
1+\frac{c_m^{(N)}}N
\le
\exp(O(1/N))\left(1+\frac{3m}{N}\right)^{1/9}.
\]

Hence

\[
\boxed{
0<\mathcal H_m^{(N)}-\log_2N
\le
O(1/N)+\frac19\log_2\left(1+\frac{3m}{N}\right).
}
\]

In particular, for `m=o(N)`,

\[
\boxed{\mathcal H_m^{(N)}=\log_2N+o(1).}
\]

Short renewal excursions therefore have almost frozen additive-correction potential; their size change is governed almost entirely by the signed coefficient skew.

## 3. Exact renewal decomposition

Let a renewal segment start at odd floor `N` and end at the next odd renewal floor `N'>N`. Suppose it contains `H` odd events and total halving count `A`.

For each relative odd-event time `k`, put

\[
A_k:=\sum_{i<k}v_i,
\qquad
\boxed{e_k:=k\gamma-A_k.}
\]

Thus

\[
e_k=s_k+\{k\gamma\}.
\]

At the endpoint define

\[
\boxed{
\sigma:=\lfloor H\gamma\rfloor-A\in\mathbb Z,
\qquad
\theta:=\{H\gamma\}\in(0,1),
}
\]

so `e_H=sigma+theta`.

If `c_H` is the tail correction, then exactly

\[
\boxed{
\frac{N'}N
=2^{e_H}\left(1+\frac{c_H}{N}\right)
=2^{\sigma+\theta}\left(1+\frac{c_H}{N}\right).
}
\]

Equivalently,

\[
\boxed{
\log_2\frac{N'}N
=e_H+
\left(\mathcal H_H^{(N)}-\log_2N\right).
}
\]

## 4. Pure-coefficient renewal record theorem

Because `N'` is the next suffix minimum among odd-event states,

\[
x_k>N'=x_H
\qquad(0<k<H).
\]

Also `c_k<c_H`. Since

\[
x_k=(N+c_k)2^{e_k},
\qquad
x_H=(N+c_H)2^{e_H},
\]

we obtain the exact strict inequality

\[
\boxed{
e_k>e_H
\qquad(0<k<H).
}
\]

Thus every genuine renewal endpoint is a strict minimum of the **pure coefficient log** among all nonzero prefix times of that renewal segment. No formation variable and no harmonic error term remains in this statement.

### 4.1 First odd event

Since the first odd iterate must remain above the renewal floor `N>1`, one cannot have `v_0>=2`, because

\[
\frac{3N+1}{4}<N.
\]

Hence necessarily

\[
\boxed{v_0=1.}
\]

Therefore

\[
\boxed{e_1=\gamma-1=: \alpha=\log_2(3/2).}
\]

The record theorem gives

\[
\boxed{e_H<\alpha.}
\]

This immediately rules out every endpoint with

\[
\boxed{\sigma\ge1.}
\]

So the previously considered “positive-skew renewal doubling” case is not a genuine next-renewal-floor case at all.

### 4.2 Layer confinement

If

\[
\sigma=-m\qquad(m\ge0),
\]

then

\[
e_H\in(-m,-m+1).
\]

If some proper prefix had `s_k<=-m-1`, then

\[
e_k=s_k+\{k\gamma\}<-m<e_H,
\]

contradicting the renewal record theorem. Hence

\[
\boxed{s_k\ge-m\qquad(0<k<H).}
\]

In particular:

- if `sigma=0`, the entire segment satisfies `s_k>=0` and ends at `s_H=0`;
- if `sigma=-1`, the entire segment satisfies `s_k>=-1` and ends at `s_H=-1`.

Thus the two economical endpoint layers are also exact finite-strip constraints on the entire signed-skew excursion.

## 5. Correct renewal endpoint classes

Every genuine renewal endpoint satisfies

\[
\boxed{\sigma\le0.}
\]

### 5.1 Nearest lower layer

If

\[
\boxed{\sigma=0,}
\]

then

\[
A=\lfloor H\gamma\rfloor,
\]

and the record theorem further forces

\[
\boxed{\theta=\{H\gamma\}<\alpha=\log_2(3/2).}
\]

The whole segment remains on the coefficient-survival side `s_k>=0`.

### 5.2 Nearest upper layer

If

\[
\boxed{\sigma=-1,}
\]

then

\[
A=\lceil H\gamma\rceil,
\]

and the whole segment stays above the signed-skew floor `-1` before ending at `-1`.

These are the only two adjacent critical layers.

### 5.3 Deep negative layer: exponential-duration overload

Let

\[
\sigma=-m,\qquad m\ge2.
\]

Since `N'>N`, the exact ratio requires

\[
1+\frac{c_H}{N}>2^{m-\theta}>2^{m-1}.
\]

For a nonperiodic renewal segment all odd-event states are distinct and at least `N`. The previously established sparse reciprocal estimate gives

\[
\log\left(1+\frac{c_H}{N}\right)
\le
\frac1{3N}
+
\frac1{3(N+1)}
+
\frac19
\log\frac{N+3H-5}{N+1}.
\]

Combining gives

\[
\boxed{
H>
\frac{
2^{9(m-1)}(N+1)e^{-3/N-3/(N+1)}-N+5
}{3}.
}
\]

For large `N`,

\[
\boxed{
H>
\left(\frac{2^{9(m-1)}-1}{3}+o(1)\right)N.
}
\]

Thus each additional negative endpoint layer multiplies the required odd-event duration asymptotically by `512`.

Examples:

- `sigma=-2`: `H>(170.33...+o(1))N`;
- `sigma=-3`: `H>(87381+o(1))N`.

## 6. Large floor jumps also cost harmonic time

Because every genuine renewal endpoint satisfies

\[
e_H<\alpha=\log_2(3/2),
\]

we have

\[
2^{e_H}<\frac32.
\]

Hence

\[
\boxed{
\frac{N'}N
<\frac32\left(1+\frac{c_H}{N}\right).
}
\]

So the pure multiplicative coefficient of a genuine renewal segment can never by itself double the floor.

If

\[
N'\ge2N,
\]

then necessarily

\[
1+\frac{c_H}{N}>\frac43.
\]

The sparse harmonic estimate yields

\[
\boxed{
H>
\frac{
(4/3)^9(N+1)e^{-3/N-3/(N+1)}-N+5
}{3}.
}
\]

Thus for large `N`,

\[
\boxed{
H>(4.1060983\ldots+o(1))N.
}
\]

More generally, any renewal floor growth factor `R>3/2` must be paid for by harmonic correction rather than by pure coefficient growth.

## 7. Refined hard core

After formation has stabilized, a genuine nonperiodic renewal transition is therefore constrained as follows:

\[
\boxed{
\text{nearest lower layer }(\sigma=0)
\quad\lor\quad
\text{nearest upper layer }(\sigma=-1)
\quad\lor\quad
\text{deep-negative exponential-duration overload}.
}
\]

There is no positive-skew renewal endpoint branch.

Moreover, a floor doubling or any larger-than-`3/2` jump must itself pay a linear harmonic-time cost.

The remaining low-cost aperiodic hard core is therefore an actual positive-integer orbit whose renewal segments repeatedly use only the two adjacent critical layers `sigma in {0,-1}` and satisfy the strict pure-coefficient endpoint-record condition.

## 8. Scope

The monotone orbit potential is not by itself a well-founded Lyapunov function: large valuation resets tend to occur at large `x_q`, where its positive increment is tiny.

The new information is instead the combination of:

- a formation-independent monotone correction potential;
- exact decomposition of floor growth;
- strict pure-coefficient record structure at every renewal endpoint;
- elimination of positive endpoint skew;
- confinement of the entire signed-skew excursion above its endpoint layer;
- and explicit time overload for deep negative endpoints or large floor jumps.

A complete proof still needs an obstruction to infinite concatenation of the two adjacent critical-layer renewal excursions for one fixed positive integer orbit.