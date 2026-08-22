# Singleton-run length and fresh-shell frequency

Date: 2026-08-22

Status: **exact asymptotic bound conditional on a hypothetical divergent bounded-record positive integer.** It shows that non-singleton fresh Haar shells cannot become arbitrarily sparse faster than logarithmically in record height. This is not a proof of the remaining post-atomic theorem and not a proof of Collatz.

Let `N` be a hypothetical positive integer with divergent accelerated Collatz orbit. Write

\[
m_k=\#\{0\le j<k:T^j(N)\text{ odd}\},
\qquad
b_k=\lceil k\log_3 2\rceil,
\qquad
h_k=m_k-b_k.
\]

From the reciprocal-summability/product argument already recorded in this branch,

\[
v_k:=\frac{2^kT^k(N)}{3^{m_k}}
\]

increases to a finite positive limit `v_infty`, and

\[
T^k(N)
=
v_k\frac{3^{b_k}}{2^k}3^{h_k}.
\]

Since

\[
1<\frac{3^{b_k}}{2^k}<3,
\]

we have the uniform upper bound

\[
\boxed{
T^k(N)<3v_\infty\,3^{h_k}.
}
\]

At a record time `tau_r`, where `h_{tau_r}=r`, this gives

\[
\boxed{
x_r:=T^{\tau_r}(N)<3v_\infty\,3^r.}
\]

## 1. All-odd runs are controlled by `v_2(x+1)`

Use the shifted coordinate

\[
z=x+1.
\]

An odd accelerated Collatz step is exactly

\[
\boxed{z\mapsto\frac{3z}{2}.}
\]

Therefore `ell` consecutive odd steps are possible only if

\[
\boxed{2^\ell\mid z_{\rm start}.}
\]

For a positive integer this implies

\[
2^\ell\le z_{\rm start}.
\]

If the run starts at, or a bounded number of steps after, record height `r`, the bounded-record assumption changes the value by only a fixed finite composition depending on `M`. Hence for a constant `C_{N,M}`,

\[
z_{\rm start}\le C_{N,M}3^r.
\]

Consequently

\[
\boxed{
\ell
\le
(\log_2 3)r+O_{N,M}(1).
}
\]

The same conclusion holds with an absolute additive adjustment for the first bit of a singleton stretch.

## 2. Consecutive singleton records cannot last longer than `O(r)` record levels

The singleton-record classification proved earlier shows that after at most the initial boundary adjustment, a consecutive stretch of singleton record macros is an all-odd parity stretch.

Every singleton record raises the record height by one and consumes at least one accelerated step. Therefore, if `K` consecutive singleton records begin near record height `r`, then the associated all-odd run has length at least

\[
K-O(1).
\]

Combining with the preceding valuation bound gives

\[
\boxed{
K
\le
(\log_2 3)r+O_{N,M}(1).
}
\]

Thus a bounded-record divergent candidate cannot hide all non-singleton records inside superlinear gaps in record height.

## 3. At least logarithmically many non-singleton records

Let

\[
r_1<r_2<r_3<\cdots
\]

be the record levels at which non-singleton record macros occur.

The previous theorem gives constants `A>0`, `B` such that

\[
r_{j+1}-r_j\le Ar_j+B.
\]

For all sufficiently large `j`, this implies

\[
r_{j+1}\le (1+A')r_j
\]

for some fixed `A'>0`. Iteration yields

\[
r_j\le C(1+A')^j.
\]

Therefore the number `J(R)` of non-singleton records up to record height `R` satisfies

\[
\boxed{
J(R)\ge c_{N,M}\log R-O_{N,M}(1).
}
\]

Every one of these non-singleton records carries the fresh terminal Haar shell from the bounded-record contraction theorem.

## 4. Interpretation

The post-atomic bounded-record obstruction is therefore not allowed to evade the fresh-shell mechanism by making non-singleton records finitely many or super-exponentially sparse in record height.

What remains possible is logarithmic-scale sparsity. The pure selector-Haar energy argument still cannot exclude this after atomicity, so the final theorem remains arithmetic rather than merely energetic.
