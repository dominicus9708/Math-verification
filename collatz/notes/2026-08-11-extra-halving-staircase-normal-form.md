# Extra-halving staircase normal form

Date: 2026-08-11

Status: **exact reparameterization of the nonperiodic exponent hard core**. This note introduces no new assumption.

## 1. Remove the mandatory halving

At odd-event step `i`, let

\[
v_i:=v_2(3x_i+1)\ge1
\]

and

\[
A_i:=\sum_{j=0}^{i-1}v_j,
\qquad A_0=0.
\]

Define the cumulative extra-halving count

\[
\boxed{E_i:=A_i-i.}
\]

Then

\[
\boxed{
E_{i+1}-E_i=v_i-1\ge0,
}
\]

so `E_i` is a nondecreasing sequence of nonnegative integers.

## 2. Critical staircase discrepancy

Let

\[
\boxed{
\alpha:=\log_2(3/2)=\log_2 3-1.
}
\]

Since

\[
A_i=i+E_i,
\]

we have

\[
\boxed{
\lambda_i
:=\frac{2^{A_i}}{3^i}
=2^{E_i}\left(\frac23\right)^i
=2^{E_i-\alpha i}
}
\]

in ordinary real notation.

Thus the earlier critical discrepancy

\[
D_i=A_i-i\log_2 3
\]

is exactly

\[
\boxed{D_i=E_i-\alpha i.}
\]

The critical line is therefore the Beatty-type line `E=alpha i`, while the actual path is an integer-valued nondecreasing staircase.

## 3. Real harmonic condition

For a hypothetical nonperiodic first-descent survivor,

\[
\sum_{i=0}^{q-1}\lambda_i=O_n(q^{1/9}).
\]

Hence in staircase coordinates

\[
\boxed{
\sum_{i=0}^{q-1}
2^{E_i}\left(\frac23\right)^i
=O_n(q^{1/9}).
}
\]

The area-deficit theorem becomes

\[
\boxed{
\sum_{i=0}^{q-1}(E_i-\alpha i)
\le
-\frac89q\log_2q+O_n(q).
}
\]

## 4. 2-adic naturality using the same rational terms

The correction series is

\[
c_q
=\frac13\sum_{i=0}^{q-1}
2^{E_i}\left(\frac23\right)^i.
\]

The finite-natural condition for a fixed positive integer `n` is

\[
\boxed{
-\frac13
\sum_{i=0}^{\infty}
2^{E_i}\left(\frac23\right)^i
=n
\quad\text{in }\mathbb Z_2.
}
\]

The expression must be interpreted termwise as rational numbers `2^{E_i+i}/3^{i+1}` before evaluating in `Q_2`; the real shorthand `2^{E_i-alpha i}` is not a p-adic exponent expression.

Thus the same ordered positive rational terms have two simultaneous roles:

- their ordinary real partial sums grow at most like `q^{1/9}`;
- their 2-adic sum is the negative ordinary integer `-n` before the outer sign.

## 5. Why the staircase form matters

The raw exponents `A_i` are strictly increasing, while `E_i` makes the structural freedom more explicit:

- `v_i=1` means a flat staircase step `E_{i+1}=E_i`;
- `v_i>=2` means an upward jump;
- balanced critical behavior corresponds to following the line `alpha i`;
- the harmonic theorem forces the staircase to spend density one logarithmically below that line;
- returns toward the line require rare upward jumps.

The remaining nonperiodic proof target is therefore a rigidity theorem for a nondecreasing integer staircase whose associated rational series is simultaneously harmonic-small over `R` and an ordinary positive-integer formation series over `Z_2`.
