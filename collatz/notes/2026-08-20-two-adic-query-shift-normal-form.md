# 2-adic query-shift normal form

Date: 2026-08-20

Status: **exact 2-adic normal form for the ternary-progression sparse-tail min-plus transition.** This is not a proof of the Collatz conjecture.

## 1. Normalized query

For the zero-carry ternary progression

\[
x=\rho+3^a u,
\qquad u\ge0,
\qquad0<\rho<3^a,
\]

define the 2-adic normalized query

\[
\boxed{\xi:=3^{-a}\rho\in\mathbb Z_2.}
\]

This coordinate combines the ternary exponent and syndrome into one 2-adic state.

## 2. Affine data of a parity macro word

Let \(W\) be a parity word of length \(B\), with

- \(Q_W\) odd steps,
- least positive canonical residue \(r_W\),
- canonical endpoint \(c_W\),
- affine correction \(R_W\).

Then

\[
\boxed{
T^B(x)
=\frac{3^{Q_W}x+R_W}{2^B},
}
\]

and in particular

\[
3^{Q_W}r_W+R_W=2^Bc_W.
\]

Define the phase-scaled correction

\[
\boxed{
\gamma_W(a)
:=
3^{-(a+Q_W)}R_W
\in\mathbb Z_2.
}
\]

## 3. The min-plus digit is the removed low dyadic block

The least compatible start in the current progression has the form

\[
x_W=\rho+3^aJ_W,
\qquad0\le J_W<2^B.
\]

The parity-cylinder condition is

\[
x_W\equiv r_W\pmod{2^B}.
\]

The earlier macro-Hensel formula gives

\[
J_W=[3^{-a}(r_W-\rho)]_{2^B}.
\]

Using

\[
R_W\equiv-3^{Q_W}r_W\pmod{2^B},
\]

we obtain

\[
\gamma_W(a)
\equiv
-3^{-a}r_W
\pmod{2^B}.
\]

Therefore

\[
\boxed{
J_W
=
[-\xi-\gamma_W(a)]_{2^B}.
}
\]

So the min-plus/Hensel cost is exactly the \(B\)-bit complement needed to cancel the low \(B\) dyadic bits of \(\xi+\gamma_W\).

## 4. Exact query shift

Let the endpoint of the least compatible start be \(\rho'\), with new ternary exponent

\[
a'=a+Q_W.
\]

Then

\[
\begin{aligned}
3^{-a'}\rho'
&=3^{-(a+Q_W)}
\frac{3^{Q_W}(\rho+3^aJ_W)+R_W}{2^B}\\
&=\frac{3^{-a}\rho+J_W+3^{-(a+Q_W)}R_W}{2^B}.
\end{aligned}
\]

Hence the new normalized query is

\[
\boxed{
\xi'
=
\frac{\xi+\gamma_W(a)+J_W}{2^B},
}
\]

where

\[
J_W=[-\xi-\gamma_W(a)]_{2^B}.
\]

Define the exact 2-adic block-shift operator

\[
\boxed{
\mathsf S_B(z)
:=
\frac{z+[-z]_{2^B}}{2^B}.
}
\]

Then the transition is simply

\[
\boxed{
\xi'
=
\mathsf S_B\bigl(\xi+\gamma_W(a)\bigr).
}
\]

This is an exact identity in \(\mathbb Z_2\).

## 5. Interpretation

Each macro step has three operations:

1. add the phase-scaled affine correction \(\gamma_W(a)\);
2. read/remove the lowest \(B\) dyadic bits;
3. shift the remaining 2-adic tail down by \(B\) bits.

The removed digit block is exactly

\[
\boxed{J_W.}
\]

Thus the sparse-tail min-plus cost and the future query state are the low and high parts of one 2-adic decomposition.

The previously growing ternary syndrome is therefore equivalent to a 2-adic digit stream under a correction-driven shift.

## 6. Finite precision requirement

To determine one \(B\)-step cost digit \(J_W\), only

\[
\xi+\gamma_W\pmod{2^B}
\]

is needed.

To determine the next query modulo \(2^B\) as well, one needs the input modulo

\[
2^{2B}.
\]

More generally, to follow \(n\) macro windows exactly at \(B\)-bit resolution requires only finite input precision of order

\[
2^{(n+1)B}.
\]

This explains why every finite-horizon problem admits an exact dyadic quotient while no fixed finite quotient automatically closes the infinite problem.

## 7. Same-Q correction differences

For two words \(u,w\) with the same odd count \(Q\),

\[
\boxed{
\gamma_u(a)-\gamma_w(a)
=
3^{-(a+Q)}(R_u-R_w).
}
\]

If they are in a full-Hensel correction class with

\[
R_u-R_w=3^Q\Delta,
\]

then

\[
\boxed{
\gamma_u(a)-\gamma_w(a)
=3^{-a}\Delta.
}
\]

Thus the old local credit \(\Delta\) is exactly a translated correction in the normalized 2-adic query coordinate.

This is only a coordinate identity. It does not restore the withdrawn claim that every later local credit gives a smaller original counterexample; the Stage-3C prefix-pullback qualification remains necessary.

## 8. Renewal interpretation

An exact Hensel translated-set renewal changes the admissible correction/query target by an additive 2-adic shift.

In the normal form, renewal is therefore a change in \(\gamma_W\) or, equivalently, in the low digit block read from

\[
\xi+\gamma_W.
\]

The depth-28 fixed renewal topology and its triangular translations can now be understood as a finite set of allowed correction-driven digit-shift rules acting on \(\xi\).

This provides a common coordinate system for

- the ternary-syndrome min-plus solver,
- the cyclic-successor Bellman function,
- the Hensel renewal graph,
- the correction/credit differences.

## 9. Revised core recurrence

The sparse-tail arithmetic can now be summarized by

\[
\boxed{
J_n=[-\xi_n-\gamma_{W_n}(a_n)]_{2^B},
}
\]

\[
\boxed{
\xi_{n+1}
=
\frac{\xi_n+\gamma_{W_n}(a_n)+J_n}{2^B},
}
\]

\[
\boxed{
a_{n+1}=a_n+Q_{W_n}.}
\]

The coefficient barrier restricts the allowed words \(W_n\). The global problem is to prove that no allowed infinite word sequence can keep producing sufficiently small Hensel/min-plus digits to support a counterexample indefinitely.

This is now a correction-driven 2-adic digit-shift problem over the already reduced phase/renewal language.

## 10. Certificate

`collatz/src/two_adic_query_shift_normal_form_certificate.py` checks the normal form against the direct CRT/canonical construction at finite 2-adic precision for all tested \(B=5\) and \(B=10\) words and syndrome states, and independently verifies the same-\(Q\) correction-difference identity.
