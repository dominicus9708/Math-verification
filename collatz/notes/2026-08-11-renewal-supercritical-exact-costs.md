# Renewal supercritical exact costs

Date: 2026-08-11

Status: **exact necessary-condition theorems for aggregate-supercritical renewal-floor segments**. These strengthen the earlier asymptotic renewal-resonance bounds but do not by themselves exclude an infinite renewal chain.

## 1. Setup

Let `N<N'` be consecutive renewal floors of a nonperiodic odd-state/block orbit. Let the renewal segment contain `m` maximal debit blocks and `H` odd events in total. Let

\[
P=\frac{2^{H+D}}{3^H}=2^{D-\alpha H},
\qquad
\alpha=\log_2(3/2),
\]

be its aggregate coefficient multiplier. Assume the segment is aggregate-supercritical:

\[
\boxed{P>1.}
\]

Write the floor gap as

\[
\boxed{g:=N'-N\ge2.}
\]

Every interior block start and every interior odd-event state is strictly larger than `N'` by the renewal-floor definition.

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

In particular no aggregate-supercritical renewal segment can contain only one or two maximal blocks, because `g>=2`.

## 3. Exact odd-event cost

At odd-event resolution the exact product is

\[
P\frac{N'}N
=
\prod_{i=0}^{H-1}
\left(1+\frac1{3x_i}\right),
\]

with `x_0=N` and every interior `x_i>N'`.

Since `P>1`,

\[
\frac{N'}N
<
\left(1+\frac1{3N}\right)
\left(1+\frac1{3N'}\right)^{H-1}.
\]

Thus

\[
\frac{N'}{N+1/3}
<
\left(1+\frac1{3N'}\right)^{H-1}.
\]

The left side is

\[
1+\frac{g-1/3}{N+1/3}.
\]

Applying the same logarithmic inequalities gives

\[
\frac{g-1/3}{N'}
<
\frac{H-1}{3N'}.
\]

Therefore

\[
\boxed{H>3g.}
\]

Since `H` is an integer,

\[
\boxed{P>1\Longrightarrow H\ge3g+1.}
\]

This is strictly stronger than the block-count cost because `H>=m`.

## 4. Exact resonance upper bound

The mandatory endpoint gap also cancels the starting odd-event correction:

\[
\frac N{N'}
\left(1+\frac1{3N}\right)<1.
\]

Hence

\[
P
<
\prod_{i=1}^{H-1}
\left(1+\frac1{3x_i}\right)
<
\left(1+\frac1{3N'}\right)^{H-1}.
\]

Taking logarithms,

\[
0<\log P
<
\frac{H-1}{3N'}.
\]

Since

\[
\log P=(D-\alpha H)\ln2,
\]

we obtain the exact universal bound

\[
\boxed{
0<\Delta:=D-\alpha H
<
\frac{H-1}{3N'\ln2}.
}
\]

No asymptotic `O(1/N')` term is needed.

## 5. Continued-fraction / quadratic-overload dichotomy

Let the reduced form of `D/H` be `p/q`. If `p/q` is not a continued-fraction convergent of `alpha`, Legendre's theorem implies

\[
\left|\frac DH-\alpha\right|
\ge
\frac1{2H^2},
\]

hence

\[
\boxed{\Delta\ge\frac1{2H}.}
\]

Combining with the exact renewal upper bound gives

\[
\frac1{2H}
<
\frac{H-1}{3N'\ln2},
\]

so

\[
\boxed{
H(H-1)>
\frac{3\ln2}{2}\,N'.
}
\]

Therefore every aggregate-supercritical renewal segment satisfies the exact dichotomy

\[
\boxed{
\begin{array}{ll}
\text{Arithmetic resonance:}& (D/H)_{\rm red}\text{ is a convergent of }\alpha,\\[1mm]
\text{or}\
\text{Quadratic overload:}&H(H-1)>(3\ln2/2)N'.
\end{array}
}
\]

This sharpens the earlier `mH \gtrsim N'` overload alternative.

## 6. Structural role

These theorems do not exclude a divergent orbit. They show instead that every floor-increasing aggregate-supercritical renewal must pay three simultaneous costs:

1. block count exceeds the floor gap: `m>g`;
2. odd-event count exceeds three times the floor gap: `H>3g`;
3. the aggregate exponent ratio is either a continued-fraction optimal approximation of `log_2(3/2)` or the segment has odd-event depth at least on the order of `sqrt(N')`.

Thus the only inexpensive renewal transitions are aggregate-subcritical ones. The next global task is to combine these exact costs with formation-floor/mixed-place arithmetic into a well-founded renewal progress theorem.
