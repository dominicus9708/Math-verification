# Sparse first-displacement recursion for bounded-displacement reachability

Status: **EXACT structural theorem / full `c>=3` frontier execution OPEN**

## Purpose

The breadth-first bounded-displacement certificate is exact but becomes expensive when the allowed displacement budget grows.

The key observation is that before the **first** displaced future rank, the path is unique: it must follow the target-exact zero-defect child repeatedly.

Therefore a bounded-displacement path can be represented by sparse displacement events separated by deterministic zero-runs.

---

## 1. Zero chain

For an exact source state `s`, let

\[
z_0=s,
\]

and, while the target-exact child is nonempty,

\[
z_{k+1}=Z(z_k),
\]

where `Z` denotes the exact `d=0` source child.

Define

\[
\boxed{L_0(s)}
\]

as the maximum number of consecutive target-exact future one-events reachable from `s`.

Thus

\[
z_0,\ldots,z_{L_0(s)}
\]

are nonempty and the next zero child is empty.

---

## 2. First-displacement decomposition

Consider any nonempty future path using at most `c>=1` displaced ranks.

If the path uses no displacement, its length is at most `L_0(s)`.

Otherwise let the first displaced rank occur after exactly `k` zero-displacement events.  Necessarily

\[
0\le k\le L_0(s).
\]

The prefix before that event is uniquely

\[
s=z_0\to z_1\to\cdots\to z_k.
\]

At the next event choose an exact positive-displacement child

\[
u=\chi_d(z_k),
\qquad d>0,
\]

with nonempty source interval.

The remaining suffix then has displacement budget at most `c-1`.

This decomposition is unique because the first displaced rank is unique.

---

## 3. Maximum reachable horizon

Let

\[
H_c(s)
\]

be the maximum number of future one-events reachable from `s` with at most `c` displaced ranks.

Base case:

\[
\boxed{H_0(s)=L_0(s).}
\]

For `c>=1`, exact first-displacement decomposition gives

\[
\boxed{
H_c(s)
=
\max\left(
L_0(s),
\max_{\substack{0\le k\le L_0(s)\\d>0\\\chi_d(z_k)\ne\varnothing}}
\left[k+1+H_{c-1}(\chi_d(z_k))\right]
\right).
}
\]

No source-payload merge is used.

---

## 4. Equivalence with bounded-displacement reachability

Let `R_{r,c}(s)` be the exact source-preserving paths of horizon `r` with at most `c` displaced ranks.

Then

\[
\boxed{
\mathcal R_{r,c}(s)\ne\varnothing
\iff
r\le H_c(s).
}
\]

Therefore

\[
\boxed{
\mathcal R_{r,c}(s)=\varnothing
\iff
r>H_c(s).
}
\]

The recursion is exactly equivalent to the breadth-first definition; it only changes the execution order.

---

## 5. Why this is the correct next engine

The previous certified results are

\[
\max_s H_0(s)=40,
\qquad
\max_s H_1(s)=44,
\qquad
\max_s H_2(s)=45
\]

on the current jump-8 source family.

A raw breadth-first `c=3` expansion creates millions of intermediate states even though almost all intervening ranks are zero-displacement runs.

The sparse recursion skips those deterministic runs and branches only at positive-displacement events.

For fixed small `c`, this is the natural source-exact representation for continuing the cumulative displacement search.

No polynomial or asymptotic complexity bound is claimed here; only the exact decomposition and recursion are claimed.

---

## 6. DSD classification

### EXACT / CLOSED

- zero-chain definition;
- unique first-displacement decomposition;
- recurrence for `H_c`;
- equivalence with bounded-displacement reachability emptiness.

### OPEN

- full current-frontier execution for `c>=3`;
- whether `H_c` admits a useful analytic upper bound in `c`;
- whether the observed small values imply any positive asymptotic displacement density.

### Forbidden inference

The finite values `40,44,45` must not be extrapolated linearly without a separate proof.

## Dependencies

- `BOUNDED_DISPLACEMENT_SOURCE_REACHABILITY.md`
- `../src/A0_s1_8jump_bounded_displacement_reachability_certificate.py`
- `SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`
