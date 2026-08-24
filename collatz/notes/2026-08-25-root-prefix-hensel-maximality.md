# Root-safe whole-prefix Hensel maximality

Date: 2026-08-25

Status: **exact root-minimality theorem + exact universal root-credit bound + finite nested-language regression through depth 22.**  This is distinct from the withdrawn arbitrary later-block L7 maximality claim.  It does not prove Collatz; its current role is a strong finite sieve on the original minimal start.

## 1. Root-prefix setup

For a binary parity prefix `w` of length `k` with `q` odd symbols, write

\[
T^k(N)=\frac{3^qN+R(w)}{2^k}.
\]

Let `u` be another length-`k`, weight-`q` word in the same full-Hensel correction class:

\[
R(u)\equiv R(w)\pmod{3^q}.
\]

If

\[
R(u)>R(w),
\]

put

\[
\boxed{
\Delta:=\frac{R(u)-R(w)}{3^q}\in\mathbb Z_{>0}.
}
\]

Then exactly

\[
\boxed{
T_u^k(N-\Delta)=T_w^k(N).
}
\]

Indeed,

\[
3^q(N-\Delta)+R(u)=3^qN+R(w).
\]

The divisibility by `2^k` also shows that `N-Delta` lies in the canonical start class of `u`, so `u` is the actual parity prefix of that alternate start.

## 2. Why this is globally safe

Assume `N` is a hypothetical minimal positive counterexample and

\[
0<N-\Delta<N.
\]

By minimality, `N-Delta` eventually reaches `1`.  Its first `k` steps merge exactly with the original trajectory at `T^k(N)`.  Hence the original trajectory has the same future and also reaches `1`, contradiction.

Therefore, whenever every possible credit at depth `k` is smaller than `N`, the actual **root prefix from the original start `N`** must be a maximum-correction representative of its full-Hensel class.

This argument does not pull a later orbit state back through an earlier prefix.  It is therefore not affected by the 2026-08-25 counterexample to arbitrary later-block L7 maximality.

## 3. Universal maximum root credit

Let the odd positions of a length-`k`, weight-`q` word be

\[
0\le i_0<i_1<\cdots<i_{q-1}\le k-1.
\]

Then

\[
R(w)=\sum_{t=0}^{q-1}3^{q-1-t}2^{i_t},
\]

so

\[
\frac{R(w)}{3^q}
=\sum_{t=0}^{q-1}\frac{2^{i_t}}{3^{t+1}}.
\]

Since `q-1-t` odd positions must remain after `i_t`,

\[
i_t\le k-q+t.
\]

Hence

\[
\frac{R(w)}{3^q}
\le
\sum_{t=0}^{q-1}\frac{2^{k-q+t}}{3^{t+1}}
=2^{k-q}\left(1-\left(\frac23\right)^q\right).
\]

For every `q>=1`,

\[
2^{k-q}\left(1-\left(\frac23\right)^q\right)
\le\frac{2^{k-1}}3,
\]

with equality in the upper-envelope formula only at `q=1`.

For two words in one Hensel class,

\[
\Delta=\frac{R_{\max}-R_{\min}}{3^q}
<\frac{R_{\max}}{3^q}
\le\frac{2^{k-1}}3.
\]

Because `Delta` is an integer,

\[
\boxed{
\Delta\le\left\lfloor\frac{2^{k-1}}3\right\rfloor.
}
\]

This is sharp.  For `q=1`, choose the latest odd position `k-1` and the earliest position of the same parity:

\[
j=\begin{cases}
0,&k-1\text{ even},\\
1,&k-1\text{ odd}.
\end{cases}
\]

Then `2^(k-1)` and `2^j` are congruent modulo `3`, and

\[
\frac{2^{k-1}-2^j}{3}
=\left\lfloor\frac{2^{k-1}}3\right\rfloor.
\]

Therefore for every `k>=3`,

\[
\boxed{
\Delta_{\max}(k)
=\left\lfloor\frac{2^{k-1}}3\right\rfloor.
}
\]

## 4. Root-safe depth for a given start floor

If a candidate family has lower start bound `V`, then every root prefix depth satisfying

\[
\left\lfloor\frac{2^{k-1}}3\right\rfloor<V
\]

must be Hensel-maximal.

For the current `m=44` recursively sufficient core the verified lower floor is already far above `2^71`, while every remaining start is below `2^73`.  Thus the theorem makes a roughly 73--74-bit root-prefix sieve available on the original start.  The exact maximal safe integer depth should be evaluated from the exact current floor before a final finite certificate is stated.

## 5. Class-max recursion

The maximum correction in every full-Hensel class can be propagated without enumerating all `2^k` words.

Suppose at length `k` a class is represented by

\[
(q,r),\qquad r=R\bmod3^q,
\]

with known maximum correction `M_k(q,r)`.

Appending `0` gives

\[
(q,r),\qquad R'=R,
\]

while appending `1` gives

\[
q'=q+1,
\qquad
R'=3R+2^k,
\]

and its new residue is

\[
\boxed{
r'\equiv3r+2^k\pmod{3^{q+1}}.}
\]

Hence the candidate maximum for the `1` child is

\[
\boxed{3M_k(q,r)+2^k.}
\]

Merging coincident child classes by `max` produces the complete length-`k+1` class-max table.  Only the current class table is needed.

## 6. Nested root-max language

Define a root word to be admissible through depth `K` when, at every prefix `1<=k<=K`, it satisfies both:

1. coefficient survival `3^{q_k}>=2^k`;
2. its prefix correction equals the maximum correction of its full-Hensel class at that depth.

An exact regression through `K=22` gives the nested survivor counts

\[
\boxed{
\begin{array}{c|rrrrrrrrrrr}
k&1&2&3&4&5&6&7&8&9&10&11\\\hline
N_k&1&1&2&3&4&7&11&16&31&52&103
\end{array}}
\]

and

\[
\boxed{
\begin{array}{c|rrrrrrrrrrr}
k&12&13&14&15&16&17&18&19&20&21&22\\\hline
N_k&182&297&593&1049&1720&3439&6104&12194&22244&38019&75969.
\end{array}}
\]

At depth 22,

\[
\frac{\log_2N_{22}}{22}
=0.7369601459\ldots,
\]

corresponding to a finite raw exclusion exponent

\[
\boxed{1-\frac{\log_2N_{22}}{22}=0.2630398541\ldots.}
\]

These numbers are a finite regression, not an asymptotic entropy theorem.

## 7. Current proof-program role

The root-prefix theorem is promising for the present finite `m=44` bottleneck because:

- it is globally safe under minimality;
- it acts on every root prefix, not only sparse low-height later states;
- its credit bound remains far below the current start scale through approximately the whole ordinary binary address of the `m=44` core;
- and the finite nested language is substantially thinner than coefficient survival alone.

The correct next target is therefore a direct same-integer finite intersection:

\[
\boxed{
(\mathcal C_{44}\setminus A_{33})
\cap
\mathcal R_{K}^{\rm root-max}
}
\]

at the largest root-safe binary depth `K` (about 73--74), rather than an unsupported extrapolation of the depth-22 entropy rate.

A practical implementation should combine:

1. streaming full-Hensel class-max recursion;
2. nested root-max survivor propagation;
3. ternary-selector subset-sum/cylinder aggregation;
4. the exact `V_33` floor and `m=44` upper address bound.

If the intersection is empty, the current `m=44` block is closed without any arbitrary later-block L7 assumption.
