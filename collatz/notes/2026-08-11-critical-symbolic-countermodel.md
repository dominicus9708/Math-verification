# Critical symbolic countermodel to purely Archimedean closure

Date: 2026-08-11

Status: **rigorous proof-strategy countermodel at the symbolic exponent-code level**. It does not construct a positive-integer Collatz counterexample. Its purpose is to show which information is insufficient for a proof.

## 1. Critical slope

Let

\[
\alpha:=\log_2(3/2).
\]

Choose a nondecreasing integer staircase `E_i` satisfying, for all sufficiently large `i`,

\[
\boxed{
E_i=\alpha i-\sqrt{i}+O(1).
}
\]

For example one may take a monotone integer rounding of the eventually increasing function `alpha i-sqrt(i)` and modify finitely many initial terms so that `E_0=0`.

Define

\[
A_i:=i+E_i.
\]

Then `A_{i+1}-A_i>=1`, so this is a valid abstract odd-event exponent code.

## 2. Critical density is satisfied

Since

\[
\frac{E_i}{i}\to\alpha,
\]

we have

\[
\boxed{
\frac{A_i}{i}	o1+\alpha=\log_2 3.
}
\]

Equivalently the odd-event/accelerated-step density tends to the critical value

\[
\boxed{
\frac{i}{A_i}	o\frac{\log2}{\log3}.
}
\]

Thus the standard critical-density necessary condition is satisfied.

## 3. Yet the real correction can be summable

The multiplicative term is

\[
\lambda_i
=2^{E_i}\left(\frac23\right)^i
=2^{E_i-\alpha i}.
\]

Hence

\[
\boxed{
\lambda_i=2^{-\sqrt{i}+O(1)}.
}
\]

Therefore

\[
\boxed{
\sum_{i=0}^{\infty}\lambda_i<\infty.
}
\]

The real correction series

\[
c_q=\frac13\sum_{i<q}\lambda_i
\]

is bounded, which is far stronger than the necessary harmonic bound `O(q^{1/9})`.

## 4. Finite formation remains valid

Every finite positive valuation word is realized by exactly one residue class modulo the corresponding power of two. Therefore every finite prefix of this exponent code is a legitimate finite Collatz parity/exponent class.

The infinite code also defines a 2-adic starting value through the standard conjugacy series

\[
\zeta
=-\frac13\sum_{i=0}^{\infty}
2^{E_i}\left(\frac23\right)^i
\quad\text{in }\mathbb Z_2.
\]

No claim is made that `zeta` is a positive ordinary integer. Establishing that such a harmonic-small critical code cannot have `zeta in N_{>=3}` is exactly the remaining mixed-place task.

## 5. Consequence for proof design

The following data are insufficient by themselves to prove Collatz:

1. finite exponent-code realizability;
2. critical asymptotic density `A_i/i -> log_2 3`;
3. even bounded real correction mass.

They coexist in an explicit abstract aperiodic exponent code.

Therefore a valid proof must use the **ordinary-integer nature of the 2-adic limit**, or an equivalent genuinely independent arithmetic invariant. Any argument that derives a contradiction only from critical density plus real drift is structurally incomplete.
