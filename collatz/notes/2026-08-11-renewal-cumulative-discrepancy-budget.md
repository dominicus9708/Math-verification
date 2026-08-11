# Cumulative renewal discrepancy budget

Date: 2026-08-11

Status: **exact persistent renewal identity + harmonic upper bound**. Unlike one-segment rational-shadow denominators, this budget is transported across every renewal floor.

## 1. Renewal chain

Let

\[
N_0<N_1<N_2<\cdots
\]

be the renewal-floor chain of a hypothetical nonperiodic positive-integer first-descent survivor.

For segment `j`, let

\[
H_j=\text{odd-event count},
\qquad
D_j=\text{extra-halving count},
\]

and define

\[
\alpha:=\log_2(3/2),
\qquad
\Delta_j:=D_j-\alpha H_j.
\]

The segment multiplier is

\[
P_j=2^{\Delta_j}.
\]

Define cumulative quantities

\[
\boxed{S_J:=\sum_{j=0}^{J-1}\Delta_j,}
\]

and

\[
\boxed{Q_J:=\sum_{j=0}^{J-1}H_j.}
\]

Then the total coefficient multiplier from `N_0` to `N_J` is exactly

\[
\boxed{2^{S_J}.}
\]

## 2. Exact persistent product identity

At odd-event resolution,

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}}.
\]

Multiplying the exact ratios gives

\[
\boxed{
2^{S_J}\frac{N_J}{N_0}
=
\prod_{i=0}^{Q_J-1}
\left(1+\frac1{3x_i}\right).
}
\]

Thus the persistent correction budget

\[
\boxed{
B_J
:=S_J+\log_2\frac{N_J}{N_0}
}
\]

is exactly

\[
\boxed{
B_J
=
\sum_{i=0}^{Q_J-1}
\log_2\left(1+\frac1{3x_i}\right)>0.
}
\]

Unlike the rational fixed point of one renewal word, `B_J` and `S_J` genuinely propagate through the full chain.

## 3. Harmonic upper bound

All odd-event states in the tail beginning at `N_0` are distinct, are at least `N_0`, and after the initial state lie in the residue classes `1,5 mod 6`.

The standard harmonic counting estimate for such a set gives

\[
\sum_{i<Q}\frac1{x_i}
\le
\frac13\log\left(1+\frac{3Q}{N_0}\right)
+O(N_0^{-1}).
\]

Using `log(1+t)<=t`,

\[
B_J
\le
\frac19\log_2\left(1+\frac{3Q_J}{N_0}\right)
+O(N_0^{-1}).
\]

Therefore

\[
\boxed{
-\log_2\frac{N_J}{N_0}
<
S_J
\le
-\log_2\frac{N_J}{N_0}
+
\frac19\log_2\left(1+\frac{3Q_J}{N_0}\right)
+O(N_0^{-1}).
}
\]

Thus the cumulative coefficient discrepancy must track the negative logarithm of the renewal floor, with only a slowly growing harmonic correction.

## 4. Tail-rebased version

The same argument may be restarted at every renewal floor `N_j`, because by definition no later block/odd state falls below it.

For any `K>j`, let

\[
S_{j,K}:=\sum_{\ell=j}^{K-1}\Delta_\ell,
\qquad
Q_{j,K}:=\sum_{\ell=j}^{K-1}H_\ell.
\]

Then

\[
\boxed{
-\log_2\frac{N_K}{N_j}
<
S_{j,K}
\le
-\log_2\frac{N_K}{N_j}
+
\frac19\log_2\left(1+\frac{3Q_{j,K}}{N_j}\right)
+O(N_j^{-1}).
}
\]

This is a genuine renewal-to-renewal progress constraint.

## 5. Fixed-ratio consequence

Suppose a future renewal window has nonnegative net discrepancy,

\[
S_{j,K}\ge0,
\]

while increasing the floor by a fixed multiplicative factor

\[
\frac{N_K}{N_j}\ge R>1.
\]

Then the tail-rebased upper bound forces

\[
\frac19\log_2\left(1+\frac{3Q_{j,K}}{N_j}\right)
\gtrsim\log_2 R,
\]

hence asymptotically

\[
\boxed{
Q_{j,K}
\gtrsim
\frac{N_j}{3}(R^9-1).
}
\]

Thus a coefficient-nonnegative renewal excursion cannot raise a large floor by a fixed factor without paying odd-event time linear in the current floor, with a ninth-power dependence on the desired floor ratio.

## 6. Current role

This theorem does not exclude an infinite chain: arbitrarily long event windows are allowed.

Its importance is architectural. It identifies a persistent global budget, whereas one-segment shadow denominators and local congruence moduli are reset at each renewal floor.

A complete aperiodic proof should therefore combine this persistent discrepancy/floor budget with the exact sparse arithmetic of economical renewal layers (nearest layers, continued-fraction resonances, power-free words, and mixed formation addresses).
