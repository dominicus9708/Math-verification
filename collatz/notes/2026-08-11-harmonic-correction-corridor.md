# Harmonic correction corridor for a nonperiodic no-first-descent orbit

Date: 2026-08-11

Status: **exact necessary-condition theorem**. This note derives a global logarithmic-width corridor for the exponent sum of any nonperiodic positive-integer orbit that never descends below its start. It does not prove that such an orbit cannot exist.

## 1. Odd-event dynamics

Let `n>=3` be odd and suppose its odd-to-odd Syracuse orbit is

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}},
\qquad
v_i=v_2(3x_i+1)\ge1,
\]

with `x_0=n`.

Set

\[
A_q:=\sum_{i=0}^{q-1}v_i,
\qquad
\lambda_q:=\frac{2^{A_q}}{3^q}.
\]

The exact affine correction coordinate is

\[
c_q:=\sum_{i=0}^{q-1}\frac{2^{A_i}}{3^{i+1}},
\]

so

\[
\boxed{x_q=\frac{n+c_q}{\lambda_q}.}
\]

---

## 2. Exact product identity

From

\[
x_{i+1}
=
\frac{3x_i}{2^{v_i}}
\left(1+\frac1{3x_i}\right),
\]

multiplication over the first `q` odd events gives

\[
\boxed{
\frac{\lambda_q x_q}{n}
=
\prod_{i=0}^{q-1}
\left(1+\frac1{3x_i}\right).
}
\]

Using `lambda_q x_q=n+c_q`, this is equivalently

\[
\boxed{
1+\frac{c_q}{n}
=
\prod_{i=0}^{q-1}
\left(1+\frac1{3x_i}\right).
}
\]

Thus the affine correction budget is exactly the accumulated multiplicative `+1` correction along the odd orbit.

---

## 3. Arithmetic sparsity of nonperiodic odd-event states

Assume the orbit is nonperiodic. Then all `x_i` are distinct; otherwise deterministic iteration would enter a cycle.

For every `i>=1`,

\[
2^{v_{i-1}}x_i=3x_{i-1}+1,
\]

so `x_i` is odd and

\[
x_i\not\equiv0\pmod3.
\]

Hence, apart from the initial term, the orbit lies in the two residue classes

\[
\boxed{x_i\equiv1,5\pmod6.}
\]

Let `R_m` denote the first `m` positive integers coprime to `6`. Their reciprocal sum satisfies

\[
\sum_{r\in R_m}\frac1r
\le C_0+\frac13\log(m+1)
\]

for an absolute constant `C_0`; this follows by grouping the two admissible values `6j+1,6j+5` in each block of six.

Therefore any `q-1` distinct post-initial odd-event states satisfy

\[
\boxed{
\sum_{i=0}^{q-1}\frac1{x_i}
\le
C_n+\frac13\log(q+1),
}
\]

where `C_n` absorbs the initial term and the finite lower cutoff imposed by `x_i>=n` if no first descent occurs.

---

## 4. Polynomial correction bound

Using `log(1+t)<=t` for `t>=0`,

\[
\begin{aligned}
\log\left(1+\frac{c_q}{n}\right)
&=
\sum_{i<q}\log\left(1+\frac1{3x_i}\right)\\
&\le
\frac13\sum_{i<q}\frac1{x_i}\\
&\le
C_n'+\frac19\log(q+1).
\end{aligned}
\]

Hence

\[
\boxed{
1+\frac{c_q}{n}
\le K_n(q+1)^{1/9}
}
\]

for a constant `K_n>0` depending only on the fixed start `n`.

Equivalently,

\[
\boxed{c_q=O_n(q^{1/9}).}
\]

This is a global deterministic bound, not a probabilistic or finite-range estimate.

---

## 5. No-descent drift corridor

Assume additionally that the orbit never descends below its start:

\[
x_q\ge n\qquad\text{for every }q.
\]

Since

\[
\lambda_q x_q=n+c_q,
\]

we obtain

\[
\boxed{
\lambda_q
\le
1+\frac{c_q}{n}
\le
K_n(q+1)^{1/9}.
}
\]

Using

\[
\lambda_q=\frac{2^{A_q}}{3^q},
\]

we get the one-sided logarithmic corridor

\[
\boxed{
A_q-q\log_2 3
\le
\frac19\log_2(q+1)+C_n''.
}
\]

Thus a nonperiodic first-descent counterexample cannot wander arbitrarily far above the powers-of-two/powers-of-three balance line. Any positive excursion above the critical line is at most logarithmic in the number of odd events.

---

## 6. Record-time lower excursion

A nonperiodic orbit consists of distinct positive integers, so `x_q->infinity` and there are infinitely many record times `q` with

\[
x_q=\max_{0\le i\le q}x_i.
\]

Among `q` distinct positive integers coprime to `6`, the largest is at least `3q-2`. Hence at every sufficiently large record time,

\[
\boxed{x_q\ge3q-2.}
\]

At such a record time,

\[
\lambda_q
=
\frac{n}{x_q}
\left(1+\frac{c_q}{n}\right)
\le
\frac{nK_n(q+1)^{1/9}}{3q-2},
\]

and therefore

\[
\boxed{
\lambda_q=O_n(q^{-8/9})
}
\]

along infinitely many record times.

Equivalently,

\[
\boxed{
A_q-q\log_2 3
\le
-\frac89\log_2 q+O_n(1)
}
\]

along an infinite subsequence.

Thus a hypothetical divergent no-first-descent orbit must repeatedly make logarithmically deep excursions to the expanding-coefficient side, even though its positive excursions above the critical line are globally bounded by only `(1/9) log_2 q+O(1)`.

---

## 7. Role in the proof architecture

This theorem adds a universal attribute filter to the mixed-place hard core:

\[
\boxed{
D_q:=A_q-q\log_2 3
}
\]

must satisfy

\[
D_q\le\frac19\log_2 q+O_n(1)
\]

for every `q`, while

\[
D_q\le-\frac89\log_2 q+O_n(1)
\]

at infinitely many record times.

The remaining problem is to combine this forced real-drift oscillation with finite-natural 2-adic stabilization. No claim of contradiction is made here.
