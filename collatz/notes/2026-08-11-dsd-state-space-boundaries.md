# DSD-style state-space boundaries for the Collatz first-descent problem

Date: 2026-08-11

Status: **geometric reformulation + exact transition identities + theorem-target separation**.

## 1. Full state versus 3D projection

The proof state remains discrete and higher-dimensional. A sufficient cylinder state may contain

\[
\Xi_k=(r_k,y_k,Q_k,R_k,I_k,\ldots).
\]

For interpretation, project it to two structural coordinates plus the discrete time/order axis k.

For an individual initial integer n define

\[
\alpha_k:=\frac{3^{Q_k(n)}}{2^k},
\qquad
\omega_k:=\frac{T^k(n)}{n}.
\]

Equivalently use logarithmic coefficient slack

\[
s_k:=\log_2\alpha_k=Q_k\log_2 3-k.
\]

The projected state space is therefore

\[
\boxed{(s_k,\omega_k,k).}
\]

The coordinates are not physical spatial axes. They are a structural projection of coefficient state, actual orbit state relative to its start, and ordered update depth.

---

## 2. Exact branch dynamics in the projection

Let p_k be the parity of T^k(n).

For an even step p_k=0,

\[
\alpha_{k+1}=\frac{\alpha_k}{2},
\qquad
s_{k+1}=s_k-1,
\]

\[
\boxed{\omega_{k+1}=\frac{\omega_k}{2}.}
\]

For an odd step p_k=1,

\[
\alpha_{k+1}=\frac32\alpha_k,
\qquad
s_{k+1}=s_k+\log_2\frac32,
\]

\[
\boxed{
\omega_{k+1}=\frac32\omega_k+\frac{1}{2n}.
}
\]

The pair (s,omega) is a projection rather than a complete autonomous state because parity realizability still depends on the underlying integer/cylinder state.

---

## 3. Two boundary surfaces

The coefficient boundary is

\[
\boxed{s=0\quad(\alpha=1).}
\]

The actual first-descent boundary is

\[
\boxed{\omega=1.}
\]

Because the correction numerator is nonnegative,

\[
\omega_k
=\alpha_k+\frac{R_k}{2^k n}
\ge\alpha_k.
\]

Hence

\[
s_k>0\Longrightarrow\omega_k>1.
\]

Therefore actual descent cannot occur before coefficient crossing, reproducing

\[
\tau_c(n)\le\tau(n).
\]

The problematic region is

\[
\boxed{
\mathcal B_{\rm cross}
=\{s<0,\ \omega\ge1\},
}
\]

a coefficient-contracted state that has nevertheless not fallen below its own start.

In interval language this is exactly a nonempty bounded unresolved island.

---

## 4. First crossing is necessarily even

Suppose k is the first coefficient-crossing depth.

An odd step multiplies alpha by 3/2 and therefore cannot move alpha from >=1 to <1. Hence the first crossing must be an even step.

If q=Q_{k-1}=Q_k, then

\[
\boxed{
2^{k-1}<3^q<2^k.
}
\]

Equivalently,

\[
0<s_{k-1}<1,
\qquad
s_k=s_{k-1}-1<0.
\]

Since the crossing step is even,

\[
\omega_k=\frac{\omega_{k-1}}{2}.
\]

Thus first-crossing descent is equivalent to the single predecessor-band statement

\[
\boxed{
\omega_{k-1}<2.
}
\]

In integer form,

\[
\boxed{
n\le T^{k-1}(n)<2n.
}
\]

The left inequality follows automatically from coefficient survival. The right inequality is the unresolved part.

---

## 5. Correction occupancy coordinate

At the crossing predecessor write

\[
v=2^{k-1},\qquad u=3^q,
\]

so

\[
v<u<2v.
\]

Let R be the correction numerator for the common prefix. Then

\[
\omega_{k-1}
=\frac{u}{v}+\frac{R}{vn}.
\]

Define the correction occupancy of the remaining multiplicative gap to 2 by

\[
\boxed{
\vartheta
:=
\frac{R}{n(2v-u)}.
}
\]

Then

\[
\boxed{
\omega_{k-1}<2
\Longleftrightarrow
\vartheta<1.
}
\]

Therefore Proposition A (first-crossing descent) is exactly a uniform bound on this occupancy coordinate over realizable unresolved crossing states.

A stronger bound such as vartheta<=1/2 would be sufficient but is not presently proved.

---

## 6. Finite crossing-band audit

The exact implementation is

`collatz/src/first_crossing_band_audit.py`.

The reference output is

`collatz/results/first_crossing_band_depth26.csv`.

For n>1, 190,067 exact canonical first-crossing candidates were generated through child depth 26.

No candidate entered the dangerous region:

\[
\boxed{\vartheta<1\quad\text{in all 190,067 cases}.}
\]

The closest observed case is the depth-8 crossing with canonical start

\[
n=39,
\]

for which

\[
\boxed{
\vartheta=\frac{251}{507}<\frac12,
}
\]

and the predecessor descent margin is

\[
2n-T^7(n)=2.
\]

This is finite evidence only. Its purpose is to identify the correct boundary quantity for Proposition A.

---

## 7. The second projection: residue growth versus coefficient slack

The binary lift recursion is

\[
r_{k+1}=r_k+c_k2^k,
\qquad c_k\in\{0,1\}.
\]

Hence

\[
\boxed{
r_k=\sum_{i=0}^{k-1}c_i2^i.}
\]

The c_i are exactly the binary digits of the initial natural number in the canonical residue refinement.

A finite positive integer is therefore characterized by

\[
\boxed{
c_i=0\text{ for all sufficiently large }i.}
\]

The coefficient-surviving region is s_j>0 at every prior slice.

Define its lower residue frontier

\[
\mu(k)=\min\{r_k>1:s_j>0\text{ for every }j\le k\},
\]

with the inherited lower-bound convention needed at the first slices.

Then Proposition B is geometrically

\[
\boxed{\mu(k)\to\infty.}
\]

That is, the coefficient-surviving region may continue to exist at arbitrary depth, but its lower frontier must recede without bound along the residue coordinate. Equivalently, no infinite coefficient-surviving path may have an eventually-zero lift sequence.

---

## 8. Global DSD-style proof split

The global first-descent problem is therefore separated into two bad-set exclusions.

### Boundary exclusion A

Exclude entry into

\[
\mathcal B_{\rm cross}=\{s<0,\omega\ge1\}
\]

at the first coefficient crossing.

Equivalent forms are

\[
\tau=\tau_c,
\]

\[
T^{k-1}(n)<2n
\]

at the crossing predecessor, or

\[
\vartheta<1.
\]

### Frontier exclusion B

Exclude a finite-residue trajectory that remains forever in

\[
s>0.
\]

Equivalent forms are

\[
\mu(k)\to\infty,
\]

or the absence of an eventually-zero infinite coefficient-surviving lift path.

If A and B hold, every n>1 has a finite actual descent time. The well-ordering of the positive integers then closes the Collatz conjecture by strong induction.

This is the current global proposition architecture. Local merge, carry, wrap, and Pareto calculations are auxiliary structures for proving A or B, not replacements for these two global targets.
