# Intermittent reset valuation filter

Date: 2026-08-11

Status: **exact necessary-condition theorem** for the nonperiodic no-first-descent hard core. It converts a return from the deep expanding side to a fixed critical strip into a logarithmically large valuation, a polynomial state-size lower bound, and a high-modulus residue constraint. It is not a proof of nonexistence.

## 1. Drift coordinate

For odd-event exponent positions

\[
A_q=\sum_{j=0}^{q-1}v_j,
\qquad v_j=v_2(3x_j+1),
\]

define

\[
\boxed{D_q:=A_q-q\alpha},
\qquad
\alpha:=\log_2 3.
\]

Then

\[
\boxed{D_{q+1}=D_q+v_q-\alpha.}
\]

The harmonic-correction/critical-strip theorem implies that for every fixed `theta` with

\[
0<\theta<\frac89,
\]

a density-one proportion of event indices in a large dyadic horizon lie below the depth

\[
-\theta\log_2 Q.
\]

We call such an index `Q`-deep.

---

## 2. Reset into a fixed critical strip

Fix `C>=0`. Suppose an event index `i` satisfies

\[
\boxed{D_i\le-\theta\log_2 Q}
\]

and its next event returns to the fixed critical strip

\[
\boxed{D_{i+1}\ge-C.}
\]

Then the drift recurrence gives

\[
-C
\le
D_i+v_i-\alpha,
\]

hence

\[
\boxed{
v_i
\ge
\theta\log_2 Q+\alpha-C.
}
\]

Because `v_i` is an integer, the exact lower bound may be written

\[
\boxed{
v_i
\ge
\left\lceil\theta\log_2 Q+\log_2 3-C\right\rceil.
}
\]

Thus a direct return from the density-one deep background to any fixed-width critical strip requires a valuation of logarithmic size.

---

## 3. State-size cost of a reset

The exact odd-event equation is

\[
3x_i+1=2^{v_i}x_{i+1}.
\]

If the orbit has no first descent from the fixed start `n`, then

\[
x_{i+1}\ge n.
\]

Therefore

\[
x_i
=\frac{2^{v_i}x_{i+1}-1}{3}
\ge
\frac{n2^{v_i}-1}{3}.
\]

Using the reset valuation lower bound,

\[
2^{v_i}
\ge
2^{\theta\log_2 Q+\alpha-C}
=
3\,2^{-C}Q^\theta,
\]

so

\[
\boxed{
x_i
\ge
n2^{-C}Q^\theta-\frac13.
}
\]

Hence a critical reset emerging directly from the deep background cannot occur at a small orbit state: its source value grows at least polynomially with the event horizon.

For return all the way to the contracting boundary `D_{i+1}>=0`, this simplifies to

\[
\boxed{
x_i\ge nQ^\theta-\frac13.}
\]

---

## 4. Exact high-modulus synchronization

The exact valuation condition

\[
v_i=t
\]

means

\[
3x_i+1=2^t u
\]

for an odd integer `u`. Therefore modulo `2^{t+1}`,

\[
3x_i+1\equiv2^t\pmod{2^{t+1}},
\]

and hence

\[
\boxed{
x_i
\equiv
3^{-1}(2^t-1)
\pmod{2^{t+1}}.}
\]

Thus a reset source with valuation `t=v_i` lies in one exact residue class modulo `2^{t+1}`.

Under the reset hypothesis,

\[
2^{v_i+1}
\ge
6\,2^{-C}Q^\theta.
\]

Consequently, a direct return to a fixed critical strip requires synchronization to a 2-adic residue whose modulus itself grows at least polynomially in the event horizon:

\[
\boxed{
\operatorname{modulus}\ge6\,2^{-C}Q^\theta.
}
\]

This is an exact formation/alignment cost, not a frequency estimate.

---

## 5. Sparsity of reset arrivals

A reset arrival to the fixed strip satisfies

\[
D_{i+1}\ge-C.
\]

The critical-strip sparsity theorem gives, among the first `Q` event endpoints,

\[
\boxed{
\#\{j<Q:D_j\ge-C\}
=O_{n,C}(Q^{1/9}).
}
\]

Therefore direct reset arrivals to a fixed strip are themselves at most `O_{n,C}(Q^{1/9})` in number.

The theorem should be read as an intermittency statement:

1. a density-one background lies deep on the expanding-coefficient side;
2. returns to a fixed critical strip are sparse;
3. whenever such a return occurs directly from the deep background, it requires a logarithmically large exact valuation;
4. that valuation forces both a polynomially large orbit state and a polynomially growing 2-adic synchronization modulus.

---

## 6. Relation to the remaining proof target

The reset theorem does not by itself contradict an infinite survivor. Large valuations are arithmetically possible, and sparse high-modulus synchronization can occur along a specially constrained orbit.

Its role is to add a new attribute layer to the mixed-place hard core. A hypothetical nonperiodic first-descent counterexample must support an intermittent structure consisting of:

\[
\boxed{
\text{deep expanding background}
\longrightarrow
\text{sparse high-valuation reset}
\longrightarrow
\text{critical strip}
}
\]

while simultaneously maintaining the finite-natural 2-adic formation condition for the original start.

The next proof task is to pull these reset congruences back to the fixed initial integer and determine whether infinitely many sparse high-valuation resets impose genuinely new independent residue information or merely restate the existing exponent code. Only the former can yield a new non-enumerative exclusion theorem.
