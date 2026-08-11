# Depth-recovery discrepancy budget

Date: 2026-08-11

Status: **exact mixed progress theorem for renewal-floor windows**. It combines the transported floor depth with the persistent cumulative coefficient discrepancy.

## 1. Setup

Let `N=N_j` be a renewal floor and define

\[
\boxed{h:=v_2(N+1).}
\]

Consider a later renewal floor `N'=N_K`, `K>j`, whose floor depth has recovered to at least the initial level:

\[
\boxed{v_2(N'+1)\ge h.}
\]

Let

\[
Q:=\sum_{\ell=j}^{K-1}H_\ell
\]

be the total odd-event count in the window, and

\[
S:=\sum_{\ell=j}^{K-1}(D_\ell-\alpha H_\ell),
\qquad
\alpha=\log_2(3/2),
\]

its cumulative coefficient discrepancy.

## 2. Exact floor-gap cost of depth recovery

Because both floor endpoints satisfy

\[
N\equiv-1\pmod{2^h},
\qquad
N'\equiv-1\pmod{2^h},
\]

the positive gap is a positive multiple of `2^h`:

\[
\boxed{N'-N\ge2^h.}
\]

Equivalently,

\[
\boxed{\frac{N'}N\ge1+\frac{2^h}{N}.}
\]

## 3. Exact correction-product upper bound

The persistent odd-event product identity over the window is

\[
\boxed{
2^S\frac{N'}N
=
\prod_{i=0}^{Q-1}
\left(1+\frac1{3x_i}\right).
}
\]

Because `N` is a renewal floor, every later odd-event state in this window is at least `N`. Hence

\[
1+\frac1{3x_i}
\le
1+\frac1{3N}.
\]

Therefore

\[
2^S\frac{N'}N
\le
\left(1+\frac1{3N}\right)^Q.
\]

Using the depth-recovery floor gap gives

\[
\boxed{
S
\le
Q\log_2\left(1+\frac1{3N}\right)
-
\log_2\left(1+\frac{2^h}{N}\right).
}
\]

This is the exact depth-recovery discrepancy budget.

## 4. Nonnegative-discrepancy recovery requires exponentially many events

If the recovery window has

\[
S\ge0,
\]

then necessarily

\[
\boxed{
Q
\ge
\frac{
\log(1+2^h/N)
}{
\log(1+1/(3N))
}.
}
\]

Using

\[
\log(1+x)\ge\frac{x}{1+x},
\qquad
\log(1+y)\le y,
\]

we obtain

\[
Q
\ge
\frac{3N2^h}{N+2^h}.
\]

Since `N+1` is divisible by `2^h`, one has `N>=2^h-1`, so

\[
\boxed{
Q>\frac32(2^h-1).
}
\]

Thus any depth recovery with nonnegative net coefficient discrepancy pays odd-event time exponential in the recovered depth.

## 5. Quantitative mixed alternative

More generally fix `0<gamma<1`. If

\[
Q
\le
(1-\gamma)
\frac{
\log(1+2^h/N)
}{
\log(1+1/(3N))
},
\]

then the exact budget gives

\[
\boxed{
S
\le
-\gamma\log_2\left(1+\frac{2^h}{N}\right)<0.
}
\]

Hence every recovery to depth at least `h` must choose between two resources:

1. **event-time payment:** `Q` is at least the recovery threshold (in particular `Omega(2^h)` for nonnegative `S`); or
2. **coefficient payment:** the cumulative discrepancy becomes quantitatively negative.

This is a genuine mixed progress alternative; both quantities propagate through the renewal quotient.

## 6. Relation to the odd core

Writing

\[
N+1=2^hK,
\qquad K\text{ odd},
\]

the relative floor increment required for recovery is approximately `1/K`, while the nonnegative-discrepancy event cost remains of order `2^h`:

\[
\frac{
\log(1+2^h/N)
}{
\log(1+1/(3N))
}
\sim
3N\log\left(1+\frac1K\right)
\sim3\cdot2^h
\]

for large odd core `K`.

Thus a large odd core does not make repeated high-depth recovery free in event time.

## 7. Role

The theorem does not yet forbid infinitely many depth recoveries: an orbit may in principle pay ever larger event time. Its importance is that depth, time, floor growth, and persistent coefficient discrepancy are now coupled in one exact inequality.

The next global task is to determine whether an infinite non-eventually-periodic renewal chain can repeatedly recharge depth while respecting both this mixed budget and the sparse economical-renewal arithmetic.