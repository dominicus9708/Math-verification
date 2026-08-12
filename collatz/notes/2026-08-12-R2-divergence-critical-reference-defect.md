# R2 divergence-to-infinity and critical-reference defect

Date: 2026-08-12

Status: exact consequences of the R2 coefficient-survival / Beatty-skew formulation. These sharpen the terminal description but do not exclude R2.

## 1. Setup

Put

\[
\gamma:=\log_2 3,
\qquad
A_i^*:=\lfloor i\gamma\rfloor,
\qquad
A_i=A_i^*-s_i,
\]

with an admissible R2 skew path

\[
s_0=0,
\qquad
0\le s_{i+1}\le s_i+r_i-1,
\qquad
r_i=A_{i+1}^*-A_i^*\in\{1,2\}.
\]

Let

\[
\lambda_i:=\frac{2^{A_i}}{3^i}=2^{-\{i\gamma\}-s_i},
\qquad
c_q:=\frac13\sum_{i<q}\lambda_i.
\]

For a positive ordinary integer start `N` the odd-event state is

\[
\boxed{x_q=\frac{N+c_q}{\lambda_q}.}
\]

## 2. R2 forces actual divergence to +infinity

There are only two possibilities for the monotone correction `c_q`.

### Case A: `c_q -> infinity`

Since `lambda_q<1`,

\[
x_q>N+c_q\to\infty.
\]

### Case B: `c_q` converges to a finite limit

Then

\[
\sum_i\lambda_i<\infty,
\]

so necessarily

\[
\lambda_i\to0.
\]

Hence

\[
x_i=\frac{N+c_i}{\lambda_i}\to\infty.
\]

Therefore in all R2 cases

\[
\boxed{x_q\to\infty.}
\]

Every accelerated state between two successive odd-event states is at least the later odd endpoint. Hence the full Collatz trajectory also tends to `+infinity`.

Thus R2 is not merely a no-first-descent or coefficient-survival branch: it is a genuine positive divergent-to-infinity branch.

## 3. Critical reference correction

Define the critical Beatty reference correction

\[
\boxed{
c_q^*:=\frac13\sum_{i=0}^{q-1}2^{-\{i\gamma\}}.
}
\]

Because `gamma` is irrational, `{i gamma}` is equidistributed modulo one. Therefore

\[
\frac{c_q^*}{q}
\to
\frac13\int_0^1 2^{-x}\,dx
=
\boxed{\frac{1}{6\ln2}}.
\]

Hence

\[
\boxed{c_q^*=\frac{q}{6\ln2}+o(q).}
\]

For a hypothetical nonperiodic positive-integer survivor the previously proved harmonic estimate gives

\[
c_q=O_N(q^{1/9})=o(q).
\]

Define the real partial defect

\[
\boxed{\xi_q:=c_q^*-c_q.}
\]

Then

\[
\boxed{
\xi_q=\frac{q}{6\ln2}+o(q).
}
\]

Thus an R2 counterexample must cancel asymptotically almost all of the linear critical-reference correction.

## 4. Critical 2-adic reference

Define

\[
\boxed{
\Phi_*:=-\sum_{i=0}^{\infty}
\frac{2^{A_i^*}}{3^{i+1}}
\in\mathbb Z_2.
}
\]

For the actual path

\[
\Phi(s)
=-\sum_{i=0}^{\infty}
\frac{2^{A_i}}{3^{i+1}}.
\]

Their difference is the 2-adically convergent defect series

\[
\Phi(s)-\Phi_*
=
\sum_{i:s_i>0}
\frac{2^{A_i}(2^{s_i}-1)}{3^{i+1}}.
\]

Let

\[
i_*:=\min\{i:s_i>0\}.
\]

The exponents `A_i` are strictly increasing. Hence the `i_*` term is the unique defect term with the least power of two, and its factor `(2^{s_i}-1)/3^{i+1}` is odd in the 2-adic sense. Therefore

\[
\boxed{
v_2\bigl(\Phi(s)-\Phi_*\bigr)=A_{i_*}.
}
\]

If `Phi(s)=N` is an ordinary positive integer, then

\[
\boxed{
v_2(N-\Phi_*)=A_{i_*}.}
\]

Thus the first combinatorial departure from the critical Beatty path is exactly the first 2-adic bit at which the natural-number start differs from the critical reference.

## 5. Scope / redundancy audit

The previous renewal-floor theorem gives

\[
N\equiv3\pmod4.
\]

Directly from the first terms of the critical reference,

\[
\Phi_*\equiv3\pmod4,
\qquad
\Phi_*\not\equiv-1\pmod8,
\]

so `v_2(Phi_*+1)=2`.

Consequently the 2-adic distance to `Phi_*` is strongly correlated with the already transported floor depth `v_2(N+1)`. In particular this critical-reference valuation should not be treated as an independent Lyapunov quantity without further structure.

Its useful role is instead conceptual: it identifies the exact bit where an R2 natural integer leaves the universal critical Beatty reference.

## 6. Terminal interpretation

R2 can now be stated as the existence of an ordinary positive integer whose parity/exponent path

1. stays forever on the coefficient-survival side of the critical line;
2. diverges to `+infinity` in the ordinary real dynamics;
3. has harmonic correction `O(q^{1/9})`;
4. differs from the critical Beatty reference by a real defect of asymptotic size `q/(6 ln 2)`;
5. yet has a 2-adic defect series that converges exactly to `N-Phi_*`.

The remaining obstruction is therefore a genuinely mixed real/2-adic naturalness problem at the exact critical-density boundary.