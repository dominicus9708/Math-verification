# Renewal-length unboundedness on a hypothetical aperiodic counterexample

Date: 2026-08-12

Status: **exact reduction conditional on the López--Stoll critical-density theorem for rational 2-adic divergent trajectories.** It proves that the sequence of renewal odd-event lengths cannot remain bounded. It does not exclude the aperiodic branch.

## 1. Setup

Let a hypothetical positive-integer nonperiodic first-descent counterexample have odd renewal floors

\[
N_0<N_1<N_2<\cdots
\]

and let the `j`th renewal segment contain `H_j` odd events and total halving count `A_j`.

Put

\[
\gamma:=\log_2 3,
\qquad
E_j:=H_j\gamma-A_j.
\]

The zero-output renewal classification gives:

1. no genuine renewal endpoint has positive signed layer `sigma>=1`;
2. the economical lower layer has `A_j=floor(H_j gamma)` and hence

\[
E_j=\{H_j\gamma\}>0;
\]

3. the upper layer and every deeper negative layer require positive additive correction to compensate a coefficient below one.

## 2. Fixed upper/deep-negative lengths have finite survival ceilings

Fix one odd-event length `H` and one endpoint layer with

\[
E:=H\gamma-A<0.
\]

The aggregate endpoint formula is

\[
\frac{N'}N=2^E\left(1+\frac{c_H}{N}\right)>1.
\]

Therefore

\[
c_H>(2^{-E}-1)N.
\]

For fixed `H` and a fixed renewal-compatible word/layer, the additive correction is bounded above by the corresponding finite Beatty-envelope reference correction `c_H^*`.

Hence

\[
\boxed{
N<\frac{c_H^*}{2^{-E}-1}.
}
\]

For a fixed bound `H<=H_0`, only finitely many lengths and relevant finite reference values occur. Consequently there is a finite threshold `M(H_0)` such that once

\[
N_j>M(H_0),
\]

no renewal segment of length `H_j<=H_0` can end on the upper or a deeper negative layer.

Thus every sufficiently late renewal segment of bounded length must be a lower-layer segment.

## 3. If all renewal lengths were bounded, the tail density would be strictly supercritical

Assume for contradiction that

\[
\boxed{H_j\le H_0}
\]

for every sufficiently large `j`.

By Section 2, all sufficiently late segments are lower-layer segments, so

\[
A_j=\lfloor H_j\gamma\rfloor
\]

and

\[
E_j=\{H_j\gamma\}>0.
\]

Because only finitely many lengths `1<=H<=H_0` occur and `gamma` is irrational, the finite set

\[
\{\{H\gamma\}:1\le H\le H_0\}
\]

has a strictly positive minimum

\[
\boxed{\delta(H_0)>0.}
\]

Hence for `J` sufficiently late renewal segments,

\[
\sum_{j<J}E_j\ge \delta(H_0)J.
\]

Meanwhile

\[
\sum_{j<J}H_j\le H_0J.
\]

Therefore the total halving count `A_tot` and total odd-event count `H_tot` satisfy

\[
H_{tot}\gamma-A_{tot}
\ge
\frac{\delta(H_0)}{H_0}H_{tot}.
\]

Thus

\[
\frac{A_{tot}}{H_{tot}}
\le
\gamma-\frac{\delta(H_0)}{H_0}.
\]

Equivalently, the proportion of odd accelerated steps on this tail satisfies a strict lower bound above the critical value

\[
\frac{H_{tot}}{A_{tot}}
\ge
\frac{1}{\gamma-\delta(H_0)/H_0}
>
\frac1\gamma
=
\frac{\ln2}{\ln3}.
\]

## 4. Contradiction with the rational-divergent critical-density theorem

López--Stoll prove that if a rational 2-adic integer has a noncyclic divergent `3x+1` trajectory, then the lower parity density must equal exactly

\[
\frac{\ln2}{\ln3}.
\]

A positive ordinary integer is a rational 2-adic integer. Therefore the strict density gap obtained in Section 3 is impossible for a positive-integer aperiodic counterexample.

Hence

\[
\boxed{
sup_j H_j=\infty.
}
\]

The odd-event lengths of renewal segments must be unbounded.

## 5. Interpretation

The remaining low-cost aperiodic hard core cannot be built from a bounded catalogue of short renewal excursions.

As the renewal floors increase, the trajectory must use renewal segments of arbitrarily large odd-event length. Combined with the Beatty-envelope slack theorem, the hard core therefore consists of increasingly long mechanical/Sturmian reference words carrying nonnegative slack excursions.

This is compatible with the known critical-density boundary: longer and longer segments allow their aggregate coefficient discrepancy per odd event to approach zero.

## 6. Scope

Unbounded renewal length is only a necessary condition. Rare extremely long segments can dominate the total odd-event count while allowing shorter lower-layer segments to occur in between.

Therefore the theorem does not imply `H_j->infinity` termwise and does not exclude an infinite aperiodic chain. It only rules out eventual boundedness of renewal lengths.