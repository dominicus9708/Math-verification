# Stopped-tree Carleson/Haar criterion for long open-positive excursions

Date: 2026-08-25

Status: **exact dyadic martingale identity + safe sufficient asymptotic criterion.**  No later-block L7 residue-maximality assumption is used.  The only global language-rate input in the criterion is the standard coefficient-survival entropy gap.  This is not a proof of the Collatz conjecture; the remaining theorem is an active-subtree selector-energy bound.

## 1. Why the tree is stopped

After the root-globalized first-defect/translation state is fixed, follow the exact mechanical-relative height

\[
h(k)=q_{\rm actual}(k)-q_{\rm mech}(k).
\]

Starting from height zero, stop a dyadic branch at the first of:

1. coefficient-boundary failure, `h<0`;
2. first nontrivial return to height zero after a positive excursion;
3. a chosen horizon `H` while the excursion is still open-positive.

The first-return leaves are prefix-free.  The horizon-active leaves are also pairwise disjoint dyadic cylinders.

The harmonic excursion theorem proved separately implies that every hypothetical nonperiodic no-first-descent hard orbit contains open-positive excursions of arbitrarily large length.  Therefore a terminal proof may concentrate on long active leaves rather than repeatedly multiplying finite-window densities.

## 2. Exact Haar telescoping identity

Let `mu` be any finite probability measure on the dyadic start coordinate, restricted/renormalized to a fixed parent cylinder.  For a dyadic parent `I` with children `I_0,I_1`, put

\[
a=\mu(I_0),\qquad b=\mu(I_1),\qquad |I_0|=|I_1|=|I|/2.
\]

Then exactly

\[
\boxed{
\frac{\mu(I_0)^2}{|I_0|}
+\frac{\mu(I_1)^2}{|I_1|}
-\frac{\mu(I)^2}{|I|}
=\frac{(a-b)^2}{|I|}.
}
\]

Hence for any finite complete stopped subtree `T` with leaf set `L(T)`,

\[
\boxed{
\sum_{J\in L(T)}\frac{\mu(J)^2}{|J|}
=
\frac{\mu(I_{\rm root})^2}{|I_{\rm root}|}
+
\sum_{I\in\operatorname{Int}(T)}
\frac{(\mu(I_0)-\mu(I_1))^2}{|I|}.
}
\]

The second term is the localized Haar/Carleson split energy.  It pays only at actually visited active ancestors; no global high-resolution selector energy is required.

## 3. Prefix-free first-order conversion

For any disjoint/prefix-free leaf family `F`, Cauchy--Schwarz gives

\[
\boxed{
\sum_{I\in F}\mu(I)
\le
\left(\sum_{I\in F}\frac{\mu(I)^2}{|I|}\right)^{1/2}
\left(\sum_{I\in F}|I|\right)^{1/2}.
}
\]

Thus the ambient fixed-depth factor `sqrt(2^H)` is replaced by the actual Kraft mass

\[
K(F):=\sum_{I\in F}|I|.
\]

This is the main advantage of the stopped-tree geometry.

## 4. Safe coefficient-only Kraft decay

Let

\[
\alpha:=\log_3 2.
\]

Every open-positive prefix is coefficient-surviving, so its parity prefix belongs to the classical upper-binomial/ballot language.  Consequently the number of length-`H` admissible prefixes is bounded by

\[
2^{H_2(\alpha)H+o(H)},
\]

where

\[
H_2(x)=-x\log_2x-(1-x)\log_2(1-x).
\]

Therefore the uniform dyadic Kraft mass of any length-`H` open-positive active family satisfies

\[
\boxed{
K_H\le 2^{-\delta_{\rm coeff}H+o(H)},
}
\]

with

\[
\boxed{
\delta_{\rm coeff}
:=1-H_2(\log_3 2)
\approx0.05004447.
}
\]

This statement uses no residue-maximality theorem and remains valid after the 2026-08-25 audit that withdrew arbitrary later-block L7 maximality as a global minimal-counterexample condition.

## 5. Stopped-tree energy sufficient criterion

Let `F_H` be the active open-positive cylinders at horizon `H`, measured from a fixed locked entry state, and define

\[
\boxed{
E_H:=\sum_{I\in F_H}\frac{\mu(I)^2}{|I|}.
}
\]

Suppose one proves, uniformly over the relevant locked entry states,

\[
\boxed{
E_H\le 2^{eH+o(H)}
}
\]

for some

\[
\boxed{e<\delta_{\rm coeff}.}
\]

Then

\[
\sum_{I\in F_H}\mu(I)
\le\sqrt{E_HK_H}
\le
\boxed{
2^{-\frac12(\delta_{\rm coeff}-e)H+o(H)}
}.
\]

Hence the selector mass of arbitrarily long open-positive excursions tends to zero exponentially.

Combined with the harmonic theorem forcing arbitrarily long open-positive excursions in every hypothetical hard orbit, such a uniform energy exponent theorem would eliminate the remaining nonperiodic hard branch.

## 6. Relation to the odd-frequency shell

At one binary refinement, let the selector child masses above parent `r` be `c_0(r),c_1(r)` and set

\[
u(r)=c_0(r)-c_1(r).
\]

The previous odd-frequency child-transport identity shows that `u` is carried only by the newly revealed odd Fourier shell.  Parseval identifies the depthwise sum of squared child imbalances with that odd shell.

Thus the stopped-tree split energy is not a new unrelated quantity.  It is the multiscale localization of the already isolated fresh odd-frequency selector energy, restricted to the dynamical active tree.

This localization is essential because the global selector measure has a hard support-size barrier once binary resolution exceeds the selector depth.

## 7. Current finite calibration

For the current `m=44` core `C_44 \ A_33`, the exact first-28-bit active-subtree certificate computes

\[
\boxed{
S_{28}
=
\sum_{I\in\operatorname{Int}(T_{28})}
\frac{(\mu(I_0)-\mu(I_1))^2}{|I|}
=
\frac{8856957423051132992}
{309182852153417706269310976}
}
\]

and hence

\[
\boxed{S_{28}\approx2.86463410288\times10^{-8}.}
\]

This is a finite calibration only.  It does **not** prove that `E_H` has sub-`delta_coeff` exponential growth.  In particular, an individual selector atom that remained active forever would eventually force large leaf energy, so the asymptotic energy theorem is genuinely nontrivial and cannot be replaced by the depth-28 number.

Portable exact certificate:

`collatz/src/m44_first_excursion_active_haar_energy_certificate.cpp`

## 8. Correct remaining theorem

The current proof-level target is therefore:

> **Locked-entry active-energy theorem.**  Uniformly over every globally admissible locked first-defect/root-translation entry state arising from the recursively sufficient selector core, the ternary selector measure restricted to the long open-positive coefficient-survival tree has leaf-energy exponent strictly less than `delta_coeff`.

Equivalently, it is enough to establish an appropriate Carleson bound on the localized odd-frequency shells along the active excursion tree.

This formulation deliberately avoids:

- multiplying finite-window survival densities;
- assuming statistical independence of ternary and dyadic channels;
- imposing invalid arbitrary later-block L7 maximality;
- or demanding impossible global high-resolution selector Fourier mixing.
