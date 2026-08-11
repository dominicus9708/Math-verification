# Periodic harmonic gap condition

Date: 2026-08-11

Status: **exact cycle identity plus elementary upper bound**. It is a necessary condition for a nontrivial positive cycle, not an exclusion theorem.

## 1. Odd-event cycle

Suppose a positive periodic orbit has `q` distinct odd states in one period. Rotate the orbit so that

\[
\boxed{n=x_0=\min\{x_0,\ldots,x_{q-1}\}.}
\]

Let

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}},
\qquad
v_i=v_2(3x_i+1),
\]

with indices modulo `q`, and let

\[
A:=\sum_{i=0}^{q-1}v_i.
\]

The odd-event multiplier is

\[
\lambda=\frac{2^A}{3^q}.
\]

## 2. Exact product identity over one period

Each event satisfies

\[
\frac{2^{v_i}x_{i+1}}{3x_i}
=1+\frac1{3x_i}.
\]

Multiplying over the period and using `x_q=x_0=n` gives

\[
\boxed{
\frac{2^A}{3^q}
=
\prod_{i=0}^{q-1}
\left(1+\frac1{3x_i}\right).
}
\]

Therefore

\[
\boxed{
\Delta_{A,q}
:=A\log2-q\log3
=
\sum_{i=0}^{q-1}
\log\left(1+\frac1{3x_i}\right)>0.
}
\]

In particular,

\[
\boxed{2^A>3^q}
\]

and hence

\[
\boxed{A/q>\log_2 3.}
\]

## 3. Harmonic upper bound using cycle distinctness

Every odd state in a cycle has an odd predecessor, so no odd cycle state is divisible by `3`. Thus all `x_i` lie in the residue classes `1,5 mod 6` and are distinct.

Using

\[
\log(1+t)\le t,
\]

we have

\[
\Delta_{A,q}
\le
\frac13\sum_{i=0}^{q-1}\frac1{x_i}.
\]

Among positive integers at least `n`, the set coprime to `6` has at most two representatives in each interval of length six. Consequently there is an absolute constant `C>0` such that the reciprocal sum of any `q` distinct admissible integers all at least `n` satisfies

\[
\sum_{i=0}^{q-1}\frac1{x_i}
\le
\frac13\log\left(1+\frac{3q}{n}\right)+\frac{C}{n}.
\]

Therefore

\[
\boxed{
0<
A\log2-q\log3
\le
\frac19\log\left(1+\frac{3q}{n}\right)
+\frac{C}{3n}.
}
\]

The precise harmless endpoint constant can be sharpened by enumerating the two admissible residue classes, but no finite enumeration is needed for the logarithmic form.

## 4. Interpretation

A positive cycle must therefore satisfy simultaneously:

1. the exact boundary lock `C=n` in the survival-ceiling formulation;
2. a positive powers-of-two/powers-of-three logarithmic gap;
3. an upper bound on that gap controlled by the number of distinct odd states and the cycle minimum.

This is the periodic analogue of the harmonic correction corridor. Unlike the nonperiodic theorem, the product is taken over one finite period and no density-one argument is involved.

The remaining cycle problem is to combine this upper bound with arithmetic lower bounds for `|A log 2-q log 3|` and with extremal restrictions on the parity word. No claim of full cycle exclusion is made here.
