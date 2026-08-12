# `A_31` shifted-block bootstrap at growing dyadic resolution

Date: 2026-08-12

Status: **finite exact recursive-sufficiency bootstrap through selector depth 31** using reuse of the already certified `A_30` block plus a new shifted copy. This is not a proof of the full Collatz conjecture.

## 1. Recursive block decomposition

For

\[
A_d=\left\{4\left(3^{44}+\sum_{i=0}^{d-1}a_i3^i\right)+3:a_i\in\{0,1\}\right\},
\]

one has the exact disjoint decomposition

\[
\boxed{A_{d+1}=A_d\;\dot\cup\;(A_d+4\cdot3^d).}
\]

Therefore, once `A_d` is certified recursive, advancing from depth `d` to `d+1` requires certifying only the shifted copy

\[
\boxed{A_d^+:=A_d+4\cdot3^d,}
\]

rather than rechecking all `2^(d+1)` representatives.

For `d=30`, the new half-block has exactly

\[
\boxed{|A_{30}^+|=2^{30}=1,073,741,824}
\]

members.

## 2. Growing dyadic class sieve

Use binary resolution

\[
\boxed{B_{\max}=24}
\]

instead of the earlier fixed `B_max=18`.

For one dyadic class `N mod 2^25`, every parity prefix through depth 24 is fixed, and

\[
T^B(N)=\frac{3^{q_B}N+R_B}{2^B}.
\]

A class is removed whenever for some `B<=24` the affine inequality

\[
\boxed{(3^{q_B}-2^B)N+R_B<0}
\]

holds uniformly across the full shifted-block interval.

The ternary selector multiplicities are aggregated modulo `2^25` by the cyclic subset-sum group algebra; the `2^30` representatives are not individually followed at this stage.

Exact result:

\[
\boxed{1,000,375,609}
\]

representatives are eliminated by a class-level forward-descent proposition.

The remaining fringe is

\[
\boxed{73,366,215}
\]

or

\[
\boxed{0.0683276122435927\ldots}
\]

of the new half-block.

Thus `93.1672%` of the new representatives are disposed of without deterministic continuation.

## 3. Exact fringe continuation

Only the `73,366,215` surviving representatives are then continued under the time-expanded accelerated map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

Every one reaches a value strictly below its own start.

There are

\[
\boxed{0}
\]

failures in the finite certificate.

The maximum first-descent depth in this shifted half-block is

\[
\boxed{\max\tau_<=525.}
\]

Hence the entire shifted family `A_30^+` is recursive.

Since `A_30` was already certified, the disjoint-union identity gives

\[
\boxed{A_{31}\text{ is recursive}.}
\]

## 4. New contiguous verified floor

By the representative-block bootstrap lemma, recursiveness of `A_31` advances the contiguous verified floor to

\[
\boxed{V_{31}=4(3^{44}+3^{31})+2}
\]

with exact value

\[
\boxed{V_{31}=3,939,086,079,428,030,067,314.}
\]

Relative to the original recursively extended floor

\[
V_0=4\cdot3^{44}+2,
\]

the cumulative interval increase is

\[
\boxed{V_{31}-V_0=4\cdot3^{31}=2,470,693,585,135,788.}
\]

Relative to the already certified `V_30`, the new incremental jump is

\[
\boxed{V_{31}-V_{30}=2\cdot4\cdot3^{30}=1,647,129,056,757,192.}
\]

## 5. Methodological significance

The step `30 -> 31` does not repeat the previous computation.

The logical structure is

\[
\boxed{
A_{30}\text{ certified}
\;\Longrightarrow\;
\text{reuse it unchanged}
\;\Longrightarrow\;
\text{certify only }A_{30}^+
\;\Longrightarrow\;
A_{31}\text{ certified}.
}
\]

Inside the new half-block, a growing-resolution class sieve first removes `93.1672%`, and only the remaining `6.8328%` are explicitly continued.

This is a genuine set/proposition bootstrap rather than a re-enumeration of the entire enlarged representative family.

## 6. Next structural target

The finite result does not establish a uniform theorem for all `d`.

The next target is to control the shifted-half survivor function

\[
S_d^+(B)=\#\{N\in A_d+4\cdot3^d:\tau_<(N)>B\}
\]

with a resolution `B=B(d)` that grows with `d`.

A terminal theorem would bound this family without individually continuing the residual representatives, ideally by combining:

1. the dyadic survivor-cylinder hierarchy;
2. the `3`-adic backtrace potential;
3. the ternary selector address;
4. the reuse identity `A_{d+1}=A_d dotcup A_d^+`.
