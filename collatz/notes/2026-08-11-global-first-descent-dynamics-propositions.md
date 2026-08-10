# Global first-descent dynamics propositions for Collatz

Date: 2026-08-11

Status: **exact state-space reduction + proved interval aggregation lemma + revised global proposition chain**. This note does not claim a proof of the Collatz conjecture.

## 1. Why first descent is the correct global target

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

define the first actual descent time

\[
\tau(n)=\min\{k\ge1:T^k(n)<n\}.
\]

For positive integers, the Collatz conjecture is equivalent to

\[
\boxed{\tau(n)<\infty\quad\text{for every }n>1.}
\]

Indeed, if every n>1 eventually reaches a smaller positive integer, strong induction on n sends every orbit to 1. Conversely, an orbit that reaches 1 necessarily has a finite descent time.

This is the well-founded global rank appropriate to the discrete dynamics: the orbit itself need not decrease at every step, but it must eventually cross below its initial natural-number rank.

---

## 2. DSD-style layer separation

The Collatz application is organized in four formal layers.

### Formation layer

A raw tuple is retained only if it is an exact realizable Collatz prefix state. For a depth-k residue cylinder this means the canonical residue, endpoint, parity count, and correction satisfy the exact affine closure relation.

### Static aggregation layer

At fixed k, infinitely many integers sharing the same first k binary/residue data are grouped into one residue cylinder

\[
C_k(r)=\{r+2^k m:m\in\mathbb Z_{\ge0}\}.
\]

Within that cylinder, the unresolved values of m are aggregated into one integer interval.

### Axis-property layer

The channel carries exact attributes such as

\[
(r_k,y_k,Q_k,R_k),
\]

coefficient margin, parity, lift bit, and the unresolved interval bounds.

### Dynamics layer

The binary lift bit refines one time slice to the next. The state and its attributes are updated exactly, then the newly resolved complement is removed.

No physical wave, propagation-speed, Laplacian, or continuum-time assumption is used.

---

## 3. Exact prefix cylinder identity

Fix a depth-k canonical residue r and let q_j(r) be the number of odd accelerated Collatz steps in the first j steps of r.

For every j<=k and every m>=0,

\[
\boxed{
T^j(r+2^k m)
=
T^j(r)+3^{q_j(r)}2^{k-j}m.
}
\]

This is the prefix affine identity applied to a lift that is a multiple of 2^j.

Therefore

\[
T^j(r+2^k m)-(r+2^k m)
=
A_{j,k}(r)+B_{j,k}(r)m,
\]

where

\[
A_{j,k}(r)=T^j(r)-r,
\]

\[
B_{j,k}(r)=2^{k-j}\bigl(3^{q_j(r)}-2^j\bigr).
\]

---

## 4. Interval Aggregation Lemma

Define the unresolved m-set in the depth-k cylinder by

\[
I_k(r)
=
\left\{
m\in\mathbb Z_{\ge0}:
T^j(r+2^k m)\ge r+2^k m
\text{ for every }1\le j\le k
\right\}.
\]

Each condition is a one-variable affine inequality

\[
A_{j,k}(r)+B_{j,k}(r)m\ge0.
\]

Hence their finite intersection with m>=0 is an integer interval, possibly empty or unbounded:

\[
\boxed{
I_k(r)=[L_k(r),U_k(r)]\cap\mathbb Z
}
\]

with U_k(r) allowed to be +infinity.

This is an exact theorem, not an empirical observation.

If B_{j,k}>0, the j-th condition contributes a lower bound

\[
m\ge
\left\lceil-\frac{A_{j,k}}{B_{j,k}}\right\rceil.
\]

If B_{j,k}<0, it contributes an upper bound

\[
m\le
\left\lfloor\frac{A_{j,k}}{-B_{j,k}}\right\rfloor.
\]

Thus infinitely many unresolved integers can remain in a cylinder only if

\[
3^{q_j(r)}>2^j
\quad\text{for every }1\le j\le k.
\]

Because equality between a positive power of 2 and a positive power of 3 is impossible, this is exactly the coefficient-survival condition.

Therefore:

\[
\boxed{
I_k(r)\text{ nonempty and unbounded}
\Longrightarrow
3^{q_j(r)}>2^j\ \forall j\le k.
}
\]

Conversely, coefficient survival implies T^j(r)>=r because the correction numerator is nonnegative, so the canonical m=0 state is unresolved and every sufficiently large m is also unresolved. Hence

\[
\boxed{
I_k(r)\text{ is unbounded}
\Longleftrightarrow
3^{q_j(r)}>2^j\ \forall j\le k.
}
\]

This identifies coefficient survival as the exact condition for an **unbounded unresolved tail**, not as a formation condition for the entire Collatz state space.

---

## 5. Exact interval-channel transition

Write a depth-k unresolved channel as

\[
\mathfrak s_k=(r,y,q,[L,U]).
\]

Choose the next binary lift bit

\[
c\in\{0,1\}.
\]

Because

\[
m=c+2m',
\]

the inherited interval is

\[
L'_{\rm inh}
=
\max\left(0,\left\lceil\frac{L-c}{2}\right\rceil\right),
\]

\[
U'_{\rm inh}
=
\left\lfloor\frac{U-c}{2}\right\rfloor
\]

when U is finite, and remains unbounded when U=+infinity.

The canonical child state is

\[
r'=r+c2^k,
\]

\[
\widetilde y=y+c3^q,
\]

\[
p=\widetilde y\bmod2,
\]

\[
y'=\frac{3^p\widetilde y+p}{2},
\qquad
q'=q+p.
\]

The new no-descent condition is

\[
\boxed{
y'-r'+(3^{q'}-2^{k+1})m'\ge0.}
\]

Intersecting this half-line with the inherited interval gives the exact next unresolved channel. An empty intersection is removed.

This is the discrete DSD-style sequence

\[
\text{formed state}
\to
\text{static interval aggregate}
\to
\text{attribute update}
\to
\text{dynamic transition}
\to
\text{resolved-complement removal}.
\]

---

## 6. Finite exact audit

The implementation is

`collatz/src/first_descent_interval_channels.py`.

The reference output is

`collatz/results/first_descent_interval_channels_depth24.csv`.

Starting from all n>1, exact interval refinement through depth 24 gives channel counts

\[
1,1,1,2,3,4,8,13,19,38,64,128,226,367,734,1295,2114,4228,7495,14990,27328,46611,93222,168807,286581.
\]

These counts exactly match the independently computed coefficient-survivor counts through the same depth.

No bounded nonempty unresolved interval appears through depth 24. From depth 2 onward every retained interval is exactly

\[
[0,+\infty).
\]

This is finite evidence for the crossing proposition below, not a proof of it.

---

## 7. Coefficient stopping versus actual stopping

For an individual n, write

\[
T^k(n)=\frac{3^{Q_k(n)}n+R_k(n)}{2^k},
\qquad R_k(n)\ge0.
\]

Define the coefficient stopping time

\[
\tau_c(n)
=
\min\{k\ge1:3^{Q_k(n)}<2^k\}.
\]

If T^k(n)<n, then necessarily 3^{Q_k(n)}<2^k because R_k>=0. Therefore universally

\[
\boxed{\tau_c(n)\le\tau(n)}
\]

whenever tau(n) is finite.

Before the first coefficient crossing, 3^{Q_j}>=2^j implies T^j(n)>=n automatically.

Hence equality of the two stopping times reduces to one local statement.

### Proposition A — First-Crossing Descent

For every n>1 with finite tau_c(n),

\[
\boxed{
T^{\tau_c(n)}(n)<n.
}
\]

Equivalently,

\[
\boxed{\tau(n)=\tau_c(n).}
\]

In interval language: when an unresolved channel first acquires a negative coefficient slope, the unresolved interval becomes empty rather than becoming a nonempty bounded interval.

This is currently a theorem target, not a proved statement.

The earlier merge/carry/dominance calculations should now be interpreted as local tools for this proposition rather than as the global proposition itself.

---

## 8. Natural-number realization and the global survivor tree

At depth k, the lift bit c_k is exactly the k-th binary digit of the initial natural number.

Therefore every finite positive integer has an **eventually-zero lift sequence**:

\[
\exists K\quad c_k=0\quad\forall k\ge K.
\]

Infinite binary lift sequences with infinitely many 1s represent nonterminating 2-adic residue paths, not finite positive integers.

Thus the global Collatz problem does not require eliminating every infinite path in the abstract residue tree. It requires eliminating infinite unresolved paths that are realizable by finite positive integers, i.e. eventually-zero lift paths.

Let the coefficient-survivor tree contain the prefixes satisfying

\[
3^{Q_j}>2^j\quad\forall j\le k.
\]

Define

\[
\mu(k)=\min\{n>1:\tau_c(n)>k\}.
\]

Then the following are equivalent:

1. every positive integer has finite coefficient stopping time;
2. there is no eventually-zero infinite path in the coefficient-survivor tree;
3. \(\mu(k)\to\infty\) as \(k\to\infty\).

This gives the second global theorem target.

### Proposition B — No Finite-Integer Infinite Coefficient Survivor

\[
\boxed{\mu(k)\to\infty.}
\]

Equivalently, every infinite coefficient-surviving path has infinitely many nonzero binary lift bits and therefore does not represent a finite positive integer.

This is currently unproved globally. The existing exact lower bound

\[
\mu(547)\ge400,000,000,000
\]

is finite evidence only.

---

## 9. Revised proof architecture

The global proof program is now:

### Exact layer already established

- affine prefix/cylinder identity;
- exact state closure;
- interval aggregation of all unresolved integers in a cylinder;
- exact binary interval transition;
- endpoint quotient and local merge/carry diagnostics.

### Main theorem target A

Prove first-crossing descent:

\[
\tau=\tau_c.
\]

### Main theorem target B

Prove finite-integer coefficient survivors cannot persist forever:

\[
\mu(k)\to\infty.
\]

### Global conclusion

For every n>1, Proposition B gives finite tau_c(n). Proposition A then gives finite actual descent tau(n). Strong induction on n gives eventual arrival at 1.

Symbolically,

\[
\boxed{
\text{A}+\text{B}
\Longrightarrow
\forall n>1\ \exists k:T^k(n)<n
\Longrightarrow
\text{Collatz}.
}
\]

This replaces indefinite depth-by-depth calculation with two explicit infinite-range propositions.
