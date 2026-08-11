# Renewal supercritical exact block-count cost

Date: 2026-08-11

Status: **corrected exact theorem**. A stronger event-level version was briefly considered and then withdrawn after audit: renewal-floor minimality controls interior **block starts**, but not every odd-event state inside a maximal block. The surviving theorem below uses only block starts and is exact.

## 1. Setup

Let `N<N'` be consecutive renewal floors of a nonperiodic maximal-block orbit. Let the renewal segment contain `m` maximal debit blocks. Let

\[
P=\prod M_r
\]

be its aggregate block multiplier, and assume

\[
\boxed{P>1.}
\]

Write

\[
\boxed{g:=N'-N\ge2.}
\]

By the renewal-floor definition, every **interior block start** in the segment is strictly larger than `N'`.

## 2. Exact block-count cost

The block product identity gives

\[
P\frac{N'}{N}=Q,
\]

where each block correction factor is

\[
1+\frac{1-(2/3)^h}{X}<1+\frac1X.
\]

Since `P>1`,

\[
\frac{N'}N<Q.
\]

The first block factor is `<1+1/N`, and the remaining `m-1` factors have starts `X>N'`, so

\[
\frac{N'}{N+1}
<
\left(1+\frac1{N'}\right)^{m-1}.
\]

Now

\[
\frac{N'}{N+1}=1+\frac{g-1}{N+1}.
\]

Using

\[
\log(1+x)\ge\frac{x}{1+x},
\qquad
\log(1+x)<x,
\]

we obtain

\[
\frac{g-1}{N'}
<
\frac{m-1}{N'}.
\]

Hence

\[
\boxed{g<m.}
\]

Equivalently,

\[
\boxed{P>1\Longrightarrow m\ge g+1.}
\]

Since distinct renewal floors are odd, `g>=2`. Therefore an aggregate-supercritical renewal requires at least three maximal blocks:

\[
\boxed{P>1\Longrightarrow m\ge3.}
\]

## 3. Why the event-level strengthening is invalid

Inside a maximal block, the `v=1` credit odd states increase from the block start toward the block endpoint. Even if all interior **block starts** exceed the next renewal floor `N'`, early credit states inside the first block may lie between `N` and `N'`.

Therefore one cannot replace every interior odd-event denominator by `N'` in the odd-event correction product. In particular, the previously proposed claims

\[
H>3g
\]

and

\[
0<D-\alpha H<\frac{H-1}{3N'\ln2}
\]

are not established for a general renewal segment by this argument and must not be used.

The earlier block-level harmonic resonance estimate remains the valid aggregate estimate.

## 4. Structural role

The exact content retained from this line of attack is simple and useful:

\[
\boxed{
\text{aggregate-supercritical renewal}
\Longrightarrow
\text{block count exceeds floor increment.}
}
\]

This supplies a genuine combinatorial cost without assuming that all odd-event states are above the next renewal floor. Future renewal arguments should stay at maximal-block resolution unless an additional theorem explicitly controls the internal credit states.
