# Zero-output orbit potential and renewal trichotomy

Date: 2026-08-12

Status: **exact orbit-side identities plus a renewal endpoint cost theorem** for the post-formation (`t_q=0`) regime. This does not prove Collatz, but it removes formation variables from the long tail and compresses renewal transitions to three cost classes.

## 1. Orbit-side harmonic potential

Assume the canonical lift output has stabilized at zero, so the least formation representative is one fixed positive odd integer `N` and the odd Syracuse orbit is

\[
x_{q+1}=\frac{3x_q+1}{2^{v_q}},\qquad v_q=v_2(3x_q+1).\]

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
x_q=(N+c_q)2^{s_q+\theta_q}.
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

Thus `H_q` is a genuine monotone quantity transported by the actual Syracuse orbit after formation has ended.

## 2. Renewal-tail adiabatic corridor

Restart the coordinates at a renewal floor `N`, meaning every later odd-event state in the considered suffix is at least `N`.

Let `c_m^(N)` and `H_m^(N)` be the corresponding tail correction and potential. Then

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

Define the relative endpoint signed skew and irrational phase

\[
\boxed{
\sigma:=\lfloor H\gamma\rfloor-A\in\mathbb Z,
\qquad
\theta:=\{H\gamma\}\in(0,1).
}
\]

If `c_H` is the tail correction, then exactly

\[
\boxed{
\frac{N'}N
=2^{\sigma+\theta}\left(1+\frac{c_H}{N}\right).
}
\]

Equivalently,

\[
\boxed{
\log_2\frac{N'}N
=\sigma+\theta+
\left(\mathcal H_H^{(N)}-\log_2N\right).
}
\]

This decomposes every renewal growth step into:

1. an integer signed-skew contribution `sigma`;
2. the fixed irrational rotation phase `theta`;
3. a positive harmonic drift.

## 4. Renewal endpoint trichotomy

### 4.1 Positive skew: floor doubling

If

\[
\sigma\ge1,
\]

then every factor on the right is greater than one and

\[
\boxed{N'>2N.}
\]

Thus any positive endpoint skew pays an immediate floor-doubling cost.

### 4.2 Critical adjacent layers

The two adjacent endpoint layers

\[
\boxed{\sigma=0}
\]

and

\[
\boxed{\sigma=-1}
\]

are the only layers that can increase the renewal floor without either automatic doubling or a large harmonic compensation.

They are exactly the nearest lower and nearest upper dyadic layers around `H log_2 3`:

\[
A=\lfloor H\gamma\rfloor
\]

or

\[
A=\lceil H\gamma\rceil.
\]

### 4.3 Deep negative skew: exponential-duration overload

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

Combining the two inequalities yields the explicit lower bound

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

Thus each additional negative signed-skew layer multiplies the required odd-event duration by asymptotically a factor of `2^9=512`.

For example:

- `sigma=-2`: `H>(170.33...+o(1))N`;
- `sigma=-3`: `H>(87381+o(1))N`.

## 5. Hard-core consequence

Every post-formation renewal transition on a hypothetical nonperiodic counterexample is therefore in exactly one of three cost classes:

\[
\boxed{
\text{floor doubling}
\quad\lor\quad
\text{nearest lower/upper critical layer}
\quad\lor\quad
\text{exponential-duration overload}.
}
\]

Hence any low-cost infinite renewal chain must spend all sufficiently economical transitions on the two adjacent critical layers `sigma in {0,-1}`.

This recovers, in a formation-independent orbit language, the two-layer structure previously obtained through macroblock/Christoffel analysis.

## 6. Scope

The monotone orbit potential does not by itself prove a contradiction. Large valuation resets can occur when `x_q` is large, making the increment

\[
\log_2(1+1/(3x_q))
\]

very small. Therefore `H_q` is not a well-founded Lyapunov function.

Its value is structural:

- it survives after all formation digits have frozen;
- it exactly separates coefficient skew from additive correction;
- it gives an adiabatic corridor on renewal tails;
- and it yields a clean renewal endpoint trichotomy without any formation bookkeeping.

The remaining economical aperiodic hard core is an actual positive-integer orbit whose renewal endpoints repeatedly use the adjacent critical layers `sigma=0` or `sigma=-1`, while all other transitions pay either floor doubling or exponential duration.