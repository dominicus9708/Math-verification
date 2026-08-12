# Critical skew first-passage unification of R1 and R2

Date: 2026-08-12

Status: **exact coding theorem for coefficient stopping from an odd renewal floor**. It unifies the finite first-crossing branch R1 and the infinite coefficient-survival branch R2 as first-passage versus eternal survival of the same Sturmian-driven integer skew walk.

## 1. Odd-event notation

Let

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}},
\qquad v_i\ge1,
\]

and put

\[
A_i:=\sum_{j<i}v_j,
\qquad
\gamma:=\log_2 3.
\]

Define the critical Beatty positions

\[
A_i^*:=\lfloor i\gamma\rfloor
\]

and the skew displacement

\[
\boxed{s_i:=A_i^*-A_i.}
\]

Also define the fixed Sturmian driver

\[
\boxed{
r_i:=A_{i+1}^*-A_i^*\in\{1,2\}.
}
\]

Then exactly

\[
\boxed{v_i=s_i+r_i-s_{i+1}.}
\]

## 2. Coefficient survival at event checkpoints

After `i` odd events the pure multiplicative coefficient of the stepwise accelerated map is

\[
\frac{3^i}{2^{A_i}}.
\]

This coefficient is greater than one exactly when

\[
A_i<i\gamma.
\]

Since `i gamma` is irrational for positive integer `i`, this is equivalent to

\[
A_i\le\lfloor i\gamma\rfloor=A_i^*.
\]

Thus

\[
\boxed{
\frac{3^i}{2^{A_i}}>1
\iff
s_i\ge0.
}
\]

Within one odd-to-odd block, the coefficient first jumps upward by `3/2` at the odd step and then decreases by successive factors `1/2`. Hence its smallest value in the block is at the block endpoint. Therefore checking the signs at all odd-event endpoints is equivalent to checking that the stepwise coefficient has never crossed below one.

## 3. R2 = eternal nonnegative skew survival

The R2 condition

\[
\tau_c(N)=\infty
\]

is therefore exactly

\[
\boxed{s_i\ge0\quad\forall i\ge0.}
\]

Together with `v_i>=1`, the local transition becomes

\[
\boxed{0\le s_{i+1}\le s_i+r_i-1.}
\]

This is the previously derived R2 critical Beatty skew-product formulation.

## 4. R1 = first passage below zero

Suppose instead the coefficient stopping time is finite.

Let `H` be the first odd-event index whose odd-to-odd block contains the first coefficient crossing. Then

\[
\boxed{
s_0,s_1,\ldots,s_{H-1}\ge0,
\qquad
s_H<0.
}
\]

Thus R1 is exactly the **first passage below zero** of the same skew walk.

The stepwise crossing itself always occurs at accelerated step

\[
\boxed{
A_+(H):=\lfloor H\gamma\rfloor+1
=\lceil H\gamma\rceil.
}
\]

## 5. Overshoot coordinate

Define the crossing overshoot

\[
\boxed{o:=-1-s_H\ge0.}
\]

Since

\[
A_H=\lfloor H\gamma\rfloor-s_H,
\]

we have

\[
\boxed{
A_H=A_+(H)+o.
}
\]

Therefore `o` is exactly the number of additional halvings after the first coefficient-crossing step before the next odd-event endpoint is reached.

### Odd crossing endpoint

If

\[
o=0
\]

then

\[
s_H=-1,
\]

and the coefficient crossing occurs exactly at the next odd endpoint.

### Even crossing endpoint

If

\[
o\ge1,
\]

then

\[
s_H\le-2,
\]

and the first coefficient crossing occurs strictly inside the final halving run, before the next odd endpoint.

Thus the earlier odd/even endpoint split is exactly the skew overshoot split

\[
\boxed{o=0\quad\text{vs}\quad o\ge1.}
\]

## 6. Exact coefficient at the next odd endpoint

Put

\[
P_H:=\frac{2^{A_+(H)}}{3^H}
\in(1,2).
\]

At the next odd endpoint the reciprocal pure coefficient is

\[
\lambda_H:=\frac{2^{A_H}}{3^H}
=2^oP_H.
\]

The exact odd-event identity is

\[
\boxed{
\lambda_H\frac{x_H}{N}
=1+\frac{c_H}{N}.
}
\]

For a renewal floor on an infinite first-descent survivor,

\[
x_H\ge N.
\]

Hence

\[
\boxed{
1+\frac{c_H}{N}
\ge2^oP_H>2^o.
}
\]

The overshoot therefore has a direct real harmonic cost.

## 7. General overshoot-overload theorem

For a renewal-floor tail, harmonic counting of the distinct odd-event states gives, for `H>=2`,

\[
\log\left(1+\frac{c_H}{N}\right)
\le
\frac1{3N}
+
\frac1{3(N+1)}
+
\frac19
\log\left(\frac{N+3H-5}{N+1}\right).
\]

Combining with

\[
1+c_H/N>2^o
\]

gives

\[
o\ln2
<
\frac1{3N}
+
\frac1{3(N+1)}
+
\frac19
\log\left(\frac{N+3H-5}{N+1}\right).
\]

Solving for `H`,

\[
\boxed{
H>
\frac{
2^{9o}(N+1)e^{-3/N-3/(N+1)}-N+5
}{3}.
}
\]

For large `N`,

\[
\boxed{
H>
\left(\frac{2^{9o}-1}{3}+o(1)\right)N.
}
\]

Thus every additional halving by which the coefficient crossing overshoots the next odd endpoint costs a factor `2^9=512` in the required odd-event depth.

For `o=1` this recovers the earlier even-endpoint bound

\[
H>(170.33\ldots+o(1))N.
\]

For `o=0` the inequality reduces to no linear overload, exactly matching the exceptional odd-endpoint first-crossing sector.

## 8. Unified terminal interpretation

The coefficient behavior of a hypothetical aperiodic renewal-floor counterexample is now one critical skew process:

\[
\boxed{
\begin{array}{ll}
\textbf{R1}:&\text{the skew walk first enters }\mathbb Z_{<0},\\[1mm]
\textbf{R2}:&\text{the skew walk remains in }\mathbb Z_{\ge0}\text{ forever}.
\end{array}
}
\]

The first-passage overshoot `o` further decomposes R1:

\[
\boxed{
\begin{array}{ll}
o=0:&\text{odd-endpoint first crossing; bounded formation/ceiling problem},\\[1mm]
o\ge1:&\text{interior-halving crossing; exponential }2^{9o}\text{ event overload}.
\end{array}
}
\]

This unification removes the need to treat coefficient stopping and coefficient survival as unrelated symbolic languages. The remaining arithmetic distinction is global naturalness: which infinite or finite first-passage skew paths can be generated by one fixed positive ordinary integer.