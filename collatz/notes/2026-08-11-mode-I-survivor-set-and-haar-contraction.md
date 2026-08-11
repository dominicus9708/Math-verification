# Mode I survivor set and Haar contraction

Date: 2026-08-11

Status: **exact set reformulation + measure-level contraction**. The measure contraction is not a proof of Mode I exclusion because a Haar-null set may still contain individual positive integers.

## 1. Maximal-block map

Let `B` denote the deterministic maximal debit-block map on positive odd integers:

\[
X=2^hK-1
\mapsto
B(X)=\frac{3^hK-1}{2^d},
\]

where

\[
h=v_2(X+1)\ge1,
\]

and `d>=1` is the trailing even-run length after the maximal odd run, so that the block multiplier is

\[
M(X)=\frac{2^{h+d}}{3^h}.
\]

By the macroblock sign theorem, on a nonperiodic orbit

\[
M(X)<1
\iff
B(X)>X.
\]

Set

\[
\alpha:=\log_2\frac32.
\]

Then the subcritical condition is

\[
\boxed{d<\alpha h.}
\]

## 2. Finite Mode I survivor sets

For `R>=1`, define

\[
\boxed{
\mathcal M_R
:=
\left\{
X\ge3\text{ odd}:
M(B^rX)<1
\text{ for every }0\le r<R
\right\}.
}
\]

Then

\[
\boxed{
\mathcal M_{R+1}\subseteq\mathcal M_R.
}
\]

Every `X in M_R` has a strictly increasing block-start orbit through its first `R` maximal blocks.

Define the Mode I formation frontier

\[
\boxed{
\mu_I(R):=\min\mathcal M_R
}
\]

when `M_R` is nonempty.

Because the sets are nested,

\[
\boxed{
\mu_I(R+1)\ge\mu_I(R).
}
\]

## 3. Exact Mode I criterion

An odd positive integer `X` generates an all-subcritical infinite block tail iff

\[
X\in\bigcap_{R\ge1}\mathcal M_R.
\]

Therefore

\[
\boxed{
\text{Mode I is absent from positive integers}
\iff
\bigcap_{R\ge1}\mathcal M_R=\varnothing.
}
\]

Since `mu_I(R)` is integer-valued and nondecreasing,

\[
\boxed{
\bigcap_{R\ge1}\mathcal M_R=\varnothing
\iff
\mu_I(R)\to+\infty.
}
\]

Thus Mode I exclusion has exactly the same frontier-escape form as the earlier unresolved-set reduction, but on the much smaller maximal-block state space.

## 4. Finite block words as exact parity cylinders

A finite maximal-block word

\[
\omega_R
=((h_0,d_0),\ldots,(h_{R-1},d_{R-1}))
\]

corresponds to the accelerated parity pattern

\[
1^{h_0}0^{d_0}
1^{h_1}0^{d_1}
\cdots
1^{h_{R-1}}0^{d_{R-1}},
\]

with an odd endpoint after the last zero run.

Let

\[
L_R:=\sum_{r<R}(h_r+d_r).
\]

Exact endpoint oddness upgrades the ordinary length-`L_R` parity congruence to one exact valuation class modulo `2^{L_R+1}`. Hence every finite block word has one exact positive-integer formation class, and its least positive representative is the formation floor of that word.

The Mode I set `M_R` is the union of the formation classes of all length-`R` block words satisfying

\[
d_r<\alpha h_r
\qquad(0\le r<R).
\]

## 5. Conditional Haar weight of one block

Condition on being at a block start, so the current accelerated parity bit is `1`.

For a fair binary parity cylinder, the probability that the maximal `1`-run has length exactly `h` and the following `0`-run has length exactly `d` is

\[
\boxed{2^{-(h+d)}.}
\]

Indeed, after conditioning on the initial `1`, one must observe `h-1` further ones followed by a zero, then `d-1` further zeros followed by the next one.

Define the one-block subcritical cylinder weight

\[
\boxed{
\kappa
:=
\sum_{h\ge1}
\sum_{\substack{d\ge1\\d<\alpha h}}
2^{-(h+d)}.
}
\]

Since no positive `d` is subcritical for `h=1`,

\[
\begin{aligned}
\kappa
&<
\sum_{h\ge2}2^{-h}
\sum_{d\ge1}2^{-d}\\
&=
\boxed{\frac12}.
\end{aligned}
\]

Thus

\[
\boxed{0<\kappa<\frac12.}
\]

## 6. Exponential Haar contraction of finite Mode I cylinders

Because the run decomposition renews at every next block-start `1`, concatenated block cylinders factor in the fair binary/Haar measure.

Therefore the total conditional Haar weight of all exact parity cylinders whose first `R` maximal blocks are subcritical is

\[
\boxed{
\kappa^R.
}
\]

In particular,

\[
\boxed{
\kappa^R<2^{-R}\to0.
}
\]

Hence the infinite all-subcritical block language is Haar-null in parity/2-adic cylinder space.

## 7. Why Haar contraction is not the missing proof

Haar measure zero does not imply absence of positive ordinary integers. A single fixed integer corresponds to one point in parity-path space and already has Haar measure zero.

Therefore

\[
\kappa^R\to0
\]

is only a measure-level elimination theorem.

The exact non-enumerative Mode I proof still requires the atomic/formation statement

\[
\boxed{
\mu_I(R)\to\infty.
}
\]

Equivalently, one must prove that the shrinking subcritical block cylinders cannot have a nested infinite branch whose exact formation floors stabilize at one finite positive integer.

## 8. Current Mode I proof target

The remaining Mode I task is now sharply separated into two parts:

1. **already closed at measure level:** the total subcritical block cylinder weight contracts exponentially;
2. **still open at atomic level:** exclude a bounded-formation-floor infinite branch inside this Haar-null language.

Combined with the near-critical necessity theorem, any surviving atomic branch would have to be an exceptionally thin sequence of very long near-critical subcritical blocks while its exact formation floor remains a fixed ordinary integer.
