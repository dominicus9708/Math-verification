# Canonical lift-digit naturalness for the signed-skew Collatz code

Date: 2026-08-12

Status: **exact formation theorem**. This replaces the abstract condition `Phi(s) in N` by eventual vanishing of explicit mixed-radix/binary lift digits. It does not yet exclude the aperiodic branch.

## 1. Completed odd-event formation classes

Let

\[
x_{q+1}=\frac{3x_q+1}{2^{v_q}},\qquad v_q\ge1,
\]

be a finite odd-event exponent code. Put

\[
A_q:=\sum_{j<q}v_j.
\]

The completed first `q` odd events, including the condition that the `q`th endpoint is odd, determine one exact starting residue class modulo

\[
\boxed{2^{A_q+1}}.
\]

Let

\[
\boxed{\rho_q\in\{1,3,\ldots,2^{A_q+1}-1\}}
\]

be its least positive representative. At `q=0`,

\[
\boxed{\rho_0=1.}
\]

## 2. Unique lift digit

When the next valuation `v_q` is appended, the formation modulus grows from

\[
2^{A_q+1}
\]

to

\[
2^{A_{q+1}+1}=2^{A_q+v_q+1}.
\]

Hence there is a unique integer

\[
\boxed{t_q\in\{0,1,\ldots,2^{v_q}-1\}}
\]

such that

\[
\boxed{\rho_{q+1}=\rho_q+t_q2^{A_q+1}.}
\]

Iterating,

\[
\boxed{\rho_q=1+\sum_{j=0}^{q-1}t_j2^{A_j+1}.}
\]

Because

\[
A_{j+1}=A_j+v_j,
\]

the `v_j` binary digits of `t_j` occupy exactly the disjoint bit interval

\[
A_j+1,\ldots,A_{j+1}
\]

of `rho_q`.

Equivalently,

\[
\boxed{\frac{\rho_q-1}{2}=\sum_{j<q}t_j2^{A_j}.}
\]

Thus the lift digits are literally the binary expansion of `(rho_q-1)/2` cut into variable-length blocks of lengths `v_j`.

## 3. Canonical endpoint carry

Write the odd-event affine numerator as

\[
2^{A_q}x_q=3^qn+B_q,
\]

where

\[
B_q=\sum_{i=0}^{q-1}2^{A_i}3^{q-1-i}.
\]

For the canonical start `rho_q`, define the canonical endpoint carry

\[
\boxed{y_q:=\frac{3^q\rho_q+B_q}{2^{A_q}}.}
\]

By completed-event formation, `y_q` is a positive odd integer.

If the start is lifted by

\[
\rho_q\mapsto\rho_q+t2^{A_q+1},
\]

then the current endpoint becomes

\[
\boxed{y_q\mapsto y_q+2t3^q.}
\]

## 4. Exact digit congruence

To realize the next desired valuation `v_q`, we require

\[
v_2\bigl(3(y_q+2t_q3^q)+1\bigr)=v_q.
\]

Equivalently,

\[
3y_q+1+2t_q3^{q+1}\equiv2^{v_q}\pmod{2^{v_q+1}}.
\]

Dividing by two gives

\[
\frac{3y_q+1}{2}+t_q3^{q+1}
\equiv2^{v_q-1}\pmod{2^{v_q}}.
\]

Therefore the unique lift digit is

\[
\boxed{
t_q\equiv
3^{-(q+1)}
\left(
2^{v_q-1}-\frac{3y_q+1}{2}
\right)
\pmod{2^{v_q}},
}
\]

with the representative chosen in `[0,2^{v_q}-1]`.

In particular,

\[
\boxed{t_q=0\iff v_2(3y_q+1)=v_q.}
\]

The canonical carry recurrence can also be written as

\[
\boxed{
2^{v_q}y_{q+1}=3y_q+1+2t_q3^{q+1}.
}
\]

The extra term is exactly the formation injection required when the least current start residue does not itself realize the next valuation.

## 5. Naturalness equivalence

An infinite exponent/skew code determines nested completed-event residue classes and hence a 2-adic starting value.

The following are equivalent.

1. The 2-adic starting value is one finite positive odd integer `N`.
2. The formation floor `rho_q` is bounded.
3. The formation floor `rho_q` is eventually constant.
4. The lift digits satisfy

\[
\boxed{t_q=0\quad\text{for all sufficiently large }q.}
\]

Indeed, if `rho_q` is eventually constant, the recursion

\[
\rho_{q+1}-\rho_q=t_q2^{A_q+1}
\]

forces eventual `t_q=0`. Conversely, eventual zero lift digits freeze `rho_q` at a finite positive odd integer and the zero-injection carry recurrence then realizes every remaining valuation from that same integer.

Thus

\[
\boxed{
\Phi(s)\in\mathbb N_{>0}
\iff
(t_q)\text{ has finite support}.
}
\]

For the stabilized integer `N`,

\[
\boxed{
\frac{N-1}{2}=\sum_{q\ge0}t_q2^{A_q}
}
\]

is its ordinary finite binary expansion segmented by the valuation lengths.

## 6. Immediate progress consequence

If `t_q>0`, then

\[
\rho_{q+1}\ge\rho_q+2^{A_q+1}.
\]

Since `A_q>=q`, infinitely many nonzero lift digits force

\[
\boxed{\rho_q\to\infty.}
\]

Hence any infinite signed-skew path whose canonical transducer emits infinitely many nonzero digits is automatically excluded from positive-integer naturalness.

The only hard case is therefore an admissible harmonic signed-skew path whose deterministic lift-digit output becomes identically zero after some finite time.

## 7. Signed-skew transducer form

For the full aperiodic signed-skew coordinate put

\[
\gamma=\log_2 3,
\qquad
r_q=\lfloor(q+1)\gamma\rfloor-\lfloor q\gamma\rfloor\in\{1,2\},
\]

and

\[
A_q=\lfloor q\gamma\rfloor-s_q.
\]

Then

\[
\boxed{v_q=s_q+r_q-s_{q+1}.}
\]

The formation transducer is therefore completely explicit:

- input: the signed-skew path `s_q`;
- driver: the fixed Sturmian/Beatty word `r_q`;
- valuation block length: `v_q=s_q+r_q-s_{q+1}`;
- state: the canonical odd carry `y_q`;
- output: the lift digit `t_q` from the congruence in Section 4.

The aperiodic naturalness condition is exactly that this output sequence be eventually zero.

## 8. Refined aperiodic terminal target

The previous condition

\[
\Phi(s)\in\mathbb N_{>1}
\]

may now be replaced by the discrete statement below.

### Finite-Support Lift-Digit Exclusion

Prove that no infinite signed-skew path satisfying the full aperiodic necessary conditions

\[
s_{q+1}\le s_q+r_q-1,
\]

\[
\sum_{i<q}2^{-s_i}=O(q^{1/9}),
\]

\[
\liminf_{q\to\infty}\frac{s_q}{q}=0
\]

can have canonical lift output

\[
\boxed{t_q=0\quad\text{eventually}.}
\]

This statement is exactly equivalent to excluding positive-ordinary-integer naturalness for the signed-skew hard core.

It does **not** follow from any finite local filter, because every finite exponent/skew prefix has a valid residue class. The obstruction must be genuinely infinite: eventual zero output must be ruled out using the long-run harmonic/critical structure of the signed-skew input.
