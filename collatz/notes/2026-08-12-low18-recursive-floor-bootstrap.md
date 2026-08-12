# Exact low-18 recursive floor bootstrap inside `m=44`

Date: 2026-08-12

Status: **finite exact recursive-sufficiency bootstrap certificate**. It verifies a complete 18-trit representative block of the `m=44` recursively sufficient core and thereby advances the contiguous verified interval by `4*3^18 = 1,549,681,956` integers. The certificate checks `2^18` recursive representatives rather than all integers in the interval. This is not a proof of the full Collatz conjecture.

## 1. Starting floor and recursively sufficient core

Use the current verified floor

\[
\boxed{V_0=4\cdot3^{44}+2.}
\]

Ansari's recursively sufficient intersection is

\[
F=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 m\ge0,\ a_i\in\{0,1\}
\right\}.
\]

The first members of `F` above `V_0` lie in the `m=44` block

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3.
\]

## 2. The low-18 representative block

Restrict to

\[
\boxed{
A_{18}:=
\left\{
4\left(3^{44}+\sum_{i=0}^{17}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
}
\]

Thus

\[
\boxed{|A_{18}|=2^{18}=262,144.}
\]

Every member of the `m=44` core below the first value with `a_18=1` belongs to `A_18`, because any selector with an index at least `18` contributes at least `3^18`.

The next `F`-member after this entire low-18 block is therefore

\[
\boxed{
N_{\rm next}=4(3^{44}+3^{18})+3.
}
\]

Consequently

\[
F\cap(V_0,N_{\rm next})=A_{18}.
\]

## 3. Exact recursive certificate for every representative

Use the time-expanded accelerated map

\[
T(n)=
\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even}.
\end{cases}
\]

For every

\[
N\in A_{18},
\]

the exact verifier computes the first depth

\[
\tau_<(N):=\min\{k\ge1:T^k(N)<N\}.
\]

The exhaustive calculation over the **representative set** `A_18`, using arbitrary-precision integer arithmetic only, gives

\[
\boxed{
\max_{N\in A_{18}}\tau_<(N)=211.
}
\]

In particular every member of `A_18` is recursive in Ansari's sense, since the smaller positive integer `T^{tau_<}(N)` merges with `N`.

One maximizing representative is obtained from selector sum

\[
\boxed{S=188,369,256,}
\]

and has start

\[
\boxed{
N_*=3,939,083,608,735,198,408,551.
}
\]

An independent Wolfram exact-integer check gives

\[
T^{210}(N_*)\ge N_*,
\qquad
T^{211}(N_*)
=3,429,201,394,071,635,023,778
<N_*.
\]

The exhaustive maximum is certified by the repository verifier; the Wolfram calculation is an independent audit of the extremal witness, not a replacement for the exhaustive representative check.

## 4. Contiguous verified-floor advancement

Because `A_18` is recursive, it may be removed from the recursively sufficient set `F` while preserving recursive sufficiency.

There is no remaining member of the refined sieve in

\[
(V_0,N_{\rm next}).
\]

Therefore Ansari's recursive-sufficiency interval theorem / Corollary 2.2 advances the verified interval to

\[
\boxed{
V_{18}:=N_{\rm next}-1
=4(3^{44}+3^{18})+2.
}
\]

Numerically,

\[
\boxed{
V_{18}=3,939,083,608,735,994,613,482.
}
\]

The increase over the previous floor is

\[
\boxed{
V_{18}-V_0
=4\cdot3^{18}
=1,549,681,956.
}
\]

Thus `262,144` representative checks certify a contiguous interval containing roughly `1.55` billion newly covered integers.

## 5. Set/proposition interpretation

The proof step is not

\[
\text{check all integers in a 1.55-billion-wide interval}.
\]

It is

\[
\boxed{
\text{identify one recursively sufficient representative set}
\to
\text{prove every member of that set recursive}
\to
\text{remove the set}
\to
\text{infer the whole interval}.}
\]

This is the finite bootstrap form of the intended proposition/set/static-aggregation strategy.

## 6. Relation to the cross-place sieve

The separate `m=44` cross-place cylinder theorem removes more than `92.17%` of the full `2^44` block at small `(3-adic,2-adic)` resolution without per-start trajectories.

The present low-18 certificate has a different role: it produces an **actual contiguous verification-floor increase**.

A useful next synthesis is therefore:

1. use cross-place class propositions to delete large families;
2. use exact finite trajectory checks only on the small representative residue left near the current floor;
3. advance the floor;
4. re-run the class propositions with the improved floor;
5. repeat.

This gives a mathematically safe bootstrap loop while keeping the large-scale work set-based rather than start-by-start.

## 7. Reproducibility

Verifier:

`collatz/src/m44_low18_recursive_bootstrap.py`

It traverses the `2^18` selector words in Gray-code order and uses exact integer arithmetic throughout.

## External input

The interval inference uses Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471--480 (2025), especially Definition 1.3, Lemma 1.1, Theorem 2.1, Corollaries 2.1--2.2, Lemmas 3.1--3.2.
