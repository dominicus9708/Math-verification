# Renewal-floor aggregate skeleton

Date: 2026-08-11

Status: **exact structural reduction for every nonperiodic positive-integer block orbit**. It recombines Mode I and Mode II on a common floor-to-floor skeleton.

## 1. Block-start orbit

Let `X_r` be the maximal debit-block starts of a nonperiodic positive-integer Collatz orbit. Because the map is deterministic, no state can repeat. Hence for every finite bound `B`, only finitely many `X_r` can satisfy `X_r<=B`; otherwise a value in the finite set `{1,...,B}` would repeat. Therefore

\[
\boxed{X_r\to\infty.}
\]

## 2. Renewal-floor times

For each suffix, let its minimum be attained. Extract the increasing sequence of indices

\[
\boxed{t_0<t_1<t_2<\cdots}
\]

for which

\[
\boxed{N_j:=X_{t_j}=\min_{r\ge t_j}X_r.}
\]

Nonperiodicity implies strict increase:

\[
\boxed{N_0<N_1<N_2<\cdots\to\infty.}
\]

Moreover, if `t_j<r<t_{j+1}`, then by the definition of the next suffix minimum,

\[
\boxed{X_r>N_{j+1}.}
\]

Thus every renewal segment has one lower endpoint `N_j`, one strictly higher endpoint `N_{j+1}`, and all interior block starts lie strictly above the higher endpoint.

Mode I is the special case in which renewal segments are eventually single subcritical blocks. Mode II produces renewal segments containing several increasing/decreasing blocks.

## 3. Exact aggregate transition

For one renewal segment `E_j=[t_j,t_{j+1})`, define

\[
H_j:=\sum_{r\in E_j}h_r,
\qquad
D_j:=\sum_{r\in E_j}d_r,
\]

\[
A_j:=H_j+D_j,
\qquad
P_j:=\prod_{r\in E_j}M_r
=\frac{2^{A_j}}{3^{H_j}}.
\]

The block-product identity gives

\[
\boxed{
P_j\frac{N_{j+1}}{N_j}
=
Q_j,
}
\]

where

\[
\boxed{
Q_j
:=
\prod_{r\in E_j}
\left(
1+\frac{1-(2/3)^{h_r}}{X_r}
\right)>1.
}
\]

Equivalently, the whole renewal segment is one exact affine map

\[
\boxed{
N_{j+1}
=
\frac{3^{H_j}N_j+B_j}{2^{A_j}}
}
\]

for a positive integer correction `B_j` determined by the exact block word.

## 4. Aggregate sign asymmetry

Because `Q_j>1`,

\[
\boxed{P_j<1\Longrightarrow N_{j+1}>N_j.}
\]

The converse need not hold: an aggregate segment may have `P_j>1` while its endpoint is still higher because of accumulated `+1` corrections. This is the only aggregate paradoxical sector.

Write

\[
\alpha:=\log_2\frac32.
\]

Then

\[
\boxed{
\log_2P_j=D_j-\alpha H_j.
}
\]

Thus a supercritical renewal segment has

\[
D_j-\alpha H_j>0.
\]

## 5. Cancellation of the starting-floor correction

Let `m_j:=t_{j+1}-t_j` be the number of maximal blocks in the renewal segment.

The starting correction factor satisfies

\[
1+\frac{1-(2/3)^{h_{t_j}}}{N_j}
<1+\frac1{N_j}.
\]

Since `N_j` and `N_{j+1}` are distinct odd integers,

\[
\boxed{
\frac{N_{j+1}}{N_j}
\ge1+\frac2{N_j}.
}
\]

Therefore, using `P_j=Q_j N_j/N_{j+1}`, the starting-floor correction is more than cancelled by the mandatory integer endpoint gap:

\[
\boxed{
P_j
<
\prod_{t_j<r<t_{j+1}}
\left(1+\frac1{X_r}\right).
}
\]

If `m_j=1`, the product on the right is empty and equals `1`; hence

\[
\boxed{m_j=1\Longrightarrow P_j<1.}
\]

This recovers the tail-minimum strict-expansion theorem as the one-block renewal case.

## 6. Harmonic resonance bound for supercritical renewal segments

All interior block starts are distinct odd integers not divisible by `3` and satisfy `X_r>N_{j+1}`. Their reciprocal sum obeys the standard spacing estimate

\[
\sum_{t_j<r<t_{j+1}}\frac1{X_r}
\le
\frac13\log\left(1+\frac{3(m_j-1)}{N_{j+1}}\right)
+O\left(\frac1{N_{j+1}}\right).
\]

Hence

\[
\boxed{
\log P_j
\le
\frac13\log\left(1+\frac{3(m_j-1)}{N_{j+1}}\right)
+O\left(\frac1{N_{j+1}}\right).
}
\]

Equivalently, if `P_j>1`, then

\[
\boxed{
0<
D_j-\alpha H_j
\le
\frac{1}{3\ln2}
\log\left(1+\frac{3(m_j-1)}{N_{j+1}}\right)
+O\left(\frac1{N_{j+1}}\right).
}
\]

Thus every supercritical floor-to-floor segment is forced into aggregate near-resonance. If `m_j=o(N_{j+1})`, its positive discrepancy tends to zero.

## 7. Relation to linear forms in logarithms

The discrepancy is the nonzero linear form

\[
(D_j+H_j)\log2-H_j\log3.
\]

General Baker/Matveev-type lower bounds therefore give an effective polynomial lower bound in the coefficient height. Combined with the renewal upper bound, this yields lower bounds on the required segment length for supercritical renewal segments. However such generic logarithmic-form bounds do not by themselves exclude the renewal hard core, because `H_j` is not yet controlled strongly enough relative to `N_{j+1}`.

## 8. Unified nonperiodic target

The Mode I/Mode II split can now be regarded as a local description rather than a mandatory final proof split.

Every nonperiodic positive-integer counterexample induces an infinite renewal-floor chain

\[
\boxed{
N_0<N_1<N_2<\cdots\to\infty
}
\]

with exact aggregate transitions above.

Each segment is either

1. aggregate subcritical, `P_j<1`; or
2. aggregate supercritical but forced into the renewal near-resonance window.

A unified nonperiodic exclusion theorem may therefore target the impossibility of an infinite finite-natural renewal chain satisfying the exact aggregate arithmetic together with these floor-to-floor resonance constraints.

This skeleton contains Mode I as the eventual one-block/subcritical case and Mode II as the multi-block excursion case.