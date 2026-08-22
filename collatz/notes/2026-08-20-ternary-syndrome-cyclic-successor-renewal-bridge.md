# Ternary-syndrome cyclic-successor renewal bridge

Date: 2026-08-20

Status: **exact identification of the sparse-tail ternary-syndrome min-plus problem with the existing cyclic-successor/Bellman geometry, plus an exact transfer of Hensel renewal translations into query translations.** This is not a proof of the Collatz conjecture.

## 1. Admissible canonical residue set

Fix a phase-height state \((s,h)\) and a finite horizon \(B\). Let

\[
\mathcal R_{s,h}(B)
\subset\{1,\ldots,2^B\}
\]

be the set of least positive canonical residues of all \(B\)-bit parity words whose every prefix satisfies the phase-shifted coefficient barrier.

For a current ternary progression

\[
x=\rho+3^a u,
\qquad u\ge0,
\qquad0<\rho<3^a,
\]

put

\[
M=3^a,
\qquad N=2^B.
\]

For each \(r\in\mathcal R_{s,h}(B)\), the least progression member in that parity cylinder is

\[
x_r=\rho+M J_r,
\]

where

\[
\boxed{
J_r=[M^{-1}(r-\rho)]_N.
}
\]

Therefore the exact finite-horizon syndrome minimum is

\[
\boxed{
\nu_{s,h}^{(a,\rho)}(B)
=
\rho+M\min_{r\in\mathcal R_{s,h}(B)}
[M^{-1}(r-\rho)]_N.
}
\]

## 2. Cyclic-successor form

Define the transformed canonical set

\[
\boxed{
\mathcal A_{s,h}^{(a)}(B)
:=
[M^{-1}\mathcal R_{s,h}(B)]_N
}
\]

and the transformed query

\[
\boxed{
\xi=[M^{-1}\rho]_N.
}
\]

For a subset \(A\subset\mathbb Z/N\mathbb Z\), define the cyclic successor distance

\[
\operatorname{succ}_N(\xi;A)
:=
\min_{z\in A}[z-\xi]_N.
\]

Then

\[
\boxed{
\nu_{s,h}^{(a,\rho)}(B)
=
\rho+3^a
\operatorname{succ}_{2^B}
\left(
\xi;
\mathcal A_{s,h}^{(a)}(B)
\right).
}
\]

Thus the ternary-syndrome sparse-tail solver is not a new optimization geometry. It is exactly the same cyclic-successor geometry already used in the earlier backward Bellman function \(J\).

The new contribution is the identification of the current ternary progression with the Bellman query coordinate.

## 3. Exact finite-horizon state compression

The min-plus increment

\[
J_{\min}
:=
\operatorname{succ}_{2^B}(\xi;\mathcal A)
\]

depends on the current syndrome only through

\[
\rho\pmod{2^B}
\]

and on the ternary exponent only through

\[
3^a\pmod{2^B}.
\]

Equivalently, for \(B\ge3\), the exact cost quotient is

\[
\boxed{
(s,h,\rho\bmod2^B,a\bmod2^{B-2}).
}
\]

This agrees with the macro-Hensel result but now places it directly inside the established cyclic-successor framework.

## 4. Translation conjugacy

Suppose two canonical residue sets satisfy an exact translated-set identity

\[
\boxed{
\mathcal R_1
=
\mathcal R_2+d
\pmod N.
}
\]

After multiplication by \(M^{-1}\), put

\[
\delta=[M^{-1}d]_N.
\]

Then

\[
\mathcal A_1
=
\mathcal A_2+\delta.
\]

Cyclic successor distance obeys the exact identity

\[
\boxed{
\operatorname{succ}_N(\xi;\mathcal A_2+\delta)
=
\operatorname{succ}_N(\xi-\delta;\mathcal A_2).
}
\]

Therefore every exact Hensel translated-set renewal becomes an exact **query-translation renewal** in the sparse-tail min-plus problem.

No wraparound correction is needed: the cyclic-successor formulation already handles it exactly.

## 5. Application to the existing depth-28 renewal certificates

The existing exact depth-28 first-return certificate establishes translated-set renewal identities for the retained hard language at first-defect positions

\[
p=2,5,10,
\]

with the previously derived swap translation

\[
\boxed{
d_p
=
2^p3^{-(q_{<p}+1)}
\pmod{2^{28}},}
\]

where \(q_{<p}\) is the mechanical odd count before the defect.

For a ternary exponent \(a\), the corresponding sparse-tail query translation is therefore

\[
\boxed{
\delta_p(a)
=
2^p3^{-(a+q_{<p}+1)}
\pmod{2^{28}}.
}
\]

Hence the exact finite renewal conjugacies already proved in canonical-residue space transfer directly into the ternary-syndrome min-plus query space.

The exceptional \(p=8\) transition remains exceptional: the old certificate explicitly found that its translated retained set is not the ordinary \(p=10\) hard set, so no false conjugacy is introduced here.

## 6. Triangular 2-adic structure of renewal translations

Because multiplication by any power of three is a 2-adic unit,

\[
\boxed{v_2(\delta_p)=p.}
\]

Thus a renewal beginning at defect position \(p\) preserves the first \(p\) dyadic bits of the query and modifies only higher bits.

For the exact renewal positions already certified,

\[
\begin{aligned}
p=2 &: \text{bits }0,1\text{ are preserved},\\
p=5 &: \text{bits }0,\ldots,4\text{ are preserved},\\
p=10&: \text{bits }0,\ldots,9\text{ are preserved}.
\end{aligned}
\]

This gives the renewal graph a triangular Hensel structure rather than an arbitrary permutation structure.

## 7. Relation to the previous backward Bellman function

Earlier in the project, the exact future-lift cost \(J\) was identified as a cyclic-successor distance to a transformed admissible suffix set.

The present identity shows that the sparse-tail ternary-progression minimum has the same form:

\[
\boxed{
\text{ternary progression}
\longleftrightarrow
\text{cyclic query},
}
\]

\[
\boxed{
\text{admissible parity cylinders}
\longleftrightarrow
\text{cyclic target set}.
}
\]

Therefore the phase-height-ternary solver and the earlier Bellman/cyclic-successor solver are two coordinate descriptions of the same finite-horizon min-plus mechanism.

This removes one apparent duplication in the proof program.

## 8. Revised sparse-tail bottleneck

The sparse-tail side is now reduced to the following precise issue.

- Exact finite-horizon cost is already a cyclic-successor problem.
- Exact Hensel renewal translates only the query.
- Low ternary digits contract/forget the remote past under accumulated odd steps.
- Some finite renewal channels are already exact, while the \(p=8\) channel is a known exception.

The missing asymptotic theorem is therefore a **renewal-controlled cyclic-query growth bound**: show that along the coefficient-surviving phase-height language, repeated query translations and exceptional transitions cannot keep the cyclic successor cost small often enough to support an infinite counterexample.

That statement is substantially narrower than a full arbitrary ternary-syndrome quotient.

## 9. Certificate

`collatz/src/ternary_macro_cyclic_successor_certificate.py` independently checks on a finite exact grid that

1. the cyclic-successor set formula equals the best-first parity-cylinder solver;
2. translated target sets are exactly conjugate to translated queries.

The project-specific depth-28 renewal identities themselves remain certified by the pre-existing

`collatz/src/m45_depth28_first_return_renewal_certificate.cpp`.
