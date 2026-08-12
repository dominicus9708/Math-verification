# Exact low-26 recursive floor bootstrap inside `m=44`

Date: 2026-08-12

Status: **finite exact recursive-sufficiency bootstrap certificate**. It verifies all `2^26` representatives obtained by freeing only the lowest 26 ternary selectors of the first unresolved `m=44` recursively sufficient block. Every representative falls below its own start within at most 354 accelerated time steps. Recursive sufficiency then advances the contiguous verified floor by `4*3^26 = 10,167,463,313,316` ordinary integers. This is not a proof of the full Collatz conjecture.

## 1. Representative family

Start from the recursively sufficient intersection

\[
F=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 m\ge0,\ a_i\in\{0,1\}
\right\}.
\]

The current first unresolved block begins at `m=44`. For `d<=44`, define

\[
A_d:=
\left\{
4\left(3^{44}+\sum_{i=0}^{d-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
\]

For `d=26`,

\[
\boxed{|A_{26}|=2^{26}=67,108,864.}
\]

Every `F`-member after the old verified floor and before the first selector with `a_26=1` belongs to `A_26`.

The next `F`-member after this block is

\[
\boxed{
N_{\rm next}=4(3^{44}+3^{26})+3.
}
\]

Hence

\[
F\cap(V_0,N_{\rm next})=A_{26},
\qquad
V_0=4\cdot3^{44}+2.
\]

## 2. Exact first-descent certificate

Use

\[
T(n)=
\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even}.
\end{cases}
\]

For every `N in A_26`, compute

\[
\tau_<(N):=\min\{k\ge1:T^k(N)<N\}.
\]

A parallel exact-integer enumeration of all `2^26` representatives gives

\[
\boxed{
\max_{N\in A_{26}}\tau_<(N)=354.
}
\]

No representative fails to descend within the verifier limit `2000`.

One maximizing representative has selector mask

\[
\boxed{22,916,555}
\]

and selector sum

\[
\boxed{S=318,906,298,102.}
\]

Its ordinary start is

\[
\boxed{
N_*=3,939,083,610,010,070,123,935.
}
\]

An independent Wolfram exact-integer audit gives

\[
T^{353}(N_*)\ge N_*,
\]

while

\[
\boxed{
T^{354}(N_*)
=2,684,210,287,892,228,253,695
<N_*.
}
\]

Thus the extremal witness agrees with the exhaustive representative verifier.

## 3. Recursive-sufficiency jump

Every member of `A_26` is recursive, because its first smaller iterate is a positive integer merging with it.

Therefore `A_26` may be removed from the recursively sufficient set `F`, and no remaining sieve member lies between the old floor and `N_next`.

The contiguous verified floor consequently advances to

\[
\boxed{
V_{26}
=4(3^{44}+3^{26})+2
=3,939,083,618,901,908,244,842.
}
\]

The exact increment is

\[
\boxed{
V_{26}-V_0
=4\cdot3^{26}
=10,167,463,313,316.
}
\]

Thus `67,108,864` recursively sufficient representatives certify more than `10.16` trillion additional ordinary starting values.

The ratio is

\[
\boxed{
\frac{4\cdot3^{26}}{2^{26}}
\approx151,507.
}
\]

So each representative check accounts for about `1.5*10^5` ordinary integers on average in this interval inference.

## 4. Growth table

The same exact finite verifier architecture gives the following representative-depth profile:

\[
\begin{array}{c|r|r}
d&|A_d|&\max\tau_<\\\hline
18&262,144&211\\
19&524,288&211\\
20&1,048,576&240\\
21&2,097,152&273\\
22&4,194,304&305\\
23&8,388,608&341\\
24&16,777,216&341\\
25&33,554,432&354\\
26&67,108,864&354
\end{array}
\]

This table is a finite computational certificate only; no asymptotic bound on the first-descent maximum is inferred from it.

## 5. Relation to the set/proposition strategy

The interval advance is not obtained by checking all ordinary integers from `V_0+1` to `V_26`.

Instead:

\[
\boxed{
10.16\text{ trillion ordinary integers}
\longrightarrow
67.1\text{ million recursively sufficient representatives}
\longrightarrow
\text{one set-level interval conclusion}.}
\]

This is already a large compression, but it is still a finite representative computation rather than the desired terminal structural theorem.

The separate cross-place cylinder theorem reduces the *full* `2^44` block by more than `92.17%` using class-level affine propositions. The next useful synthesis is to apply those class-level exclusions first and reserve explicit trajectory evaluation only for the small surviving representative fringe needed to advance the floor.

## 6. Reproducibility

Exact C++ verifier:

`collatz/src/m44_low26_recursive_bootstrap.cpp`

Compile, for example, with an OpenMP-capable compiler:

`g++ -O3 -march=native -fopenmp collatz/src/m44_low26_recursive_bootstrap.cpp -o low26`

All Collatz trajectory arithmetic uses unsigned 128-bit integers; the verifier's checked trajectories stay within that range. The result should not be extrapolated to larger selector depths without a separate overflow audit.

## 7. External input discipline

The interval inference uses Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471--480 (2025): Definition 1.3, Lemma 1.1, Theorem 2.1, Corollaries 2.1--2.2, and Lemmas 3.1--3.2.

Ansari's Lemma 3.1 guarantees existence of smaller merging integers for its recursive subsets but does **not** supply a general canonical reduction map. Accordingly this note uses only explicit first-descent witnesses and does not compose a hypothetical reverse ancestor larger than the target with an unspecified Ansari reduction.
