# Upstream compatibility audit: Formation / Realized-Axis / Static Aggregation / Collatz

Date: 2026-08-09

Status: **UPSTREAM INTERFACE AUDIT / NO CHANGE TO COLLATZ ARITHMETIC**

This note records version-interface differences discovered while aligning the Collatz application with the finalized realized-axis property system and the current Formation Axiom System.

The findings concern typing, notation, and dependency order. They do not invalidate the Bochner-integral realization theorems of the Channel-Indexed Static Aggregation manuscript, and they do not change any exact Collatz recurrence or numerical verification result.

## 1. Current upstream channel identity

The current Formation Axiom System uses operational channel identity

\[
\boxed{c=(p,a,\lambda,v,\rho).}
\]

Here `v` is the assigned value and is part of channel identity. Restriction/realization witnesses such as `H,h` are preserved through the formation structure/trace but are not coordinates of the operational channel tuple.

The finalized realized-axis property system inherits exactly this Stage-VI channel identity and explicitly treats the formation trace as derived/inherited provenance rather than as an extra coordinate of the tag.

## 2. Older Static Aggregation interface still uses a superseded tuple

The 2026-07-28 Channel-Indexed Static Aggregation manuscript currently states in its interface section that a candidate component channel has the form

\[
c=(H,h,p,a,\lambda,\rho).
\]

Its appendix likewise summarizes the channel with that older tuple.

This should be updated to the current operational channel type

\[
\boxed{c=(p,a,\lambda,v,\rho)}
\]

and the structural witnesses `H,h` should be referred to through the current formation-trace/interface data.

This is an interface correction. The analytic datum

\[
(X_c,\Sigma_c,\mu_c,\zeta_c,w_c)
\]

and the realized term

\[
T_L^{\mathfrak R}(c)=\int_{X_c}\zeta_c w_c\,d\mu_c
\]

are unchanged after replacing the channel's inherited tag type.

## 3. Finite channel families are sets without repetition

The current Formation core defines finite composition on finite subsets of the admitted channel set:

\[
\mathfrak D_L^{\mathrm{comp}}=\mathcal P_{\mathrm{fin}}(\mathfrak C_L),
\qquad
\Comp_L(F)=\sum_{c\in F}T_L(c).
\]

Thus a core channel family is unordered and contains no repeated occurrence of one identical channel.

The Static Aggregation manuscript is consistent with support-tagged finite records and summation over channel support, but a Collatz application must respect this set-valued support literally. Therefore a length-`h` parity trace cannot be represented by repeatedly inserting only two identical tags `c_E,c_O` into the same finite channel family.

For a literal DSD encoding one instead uses distinct occurrence-specific admitted channels

\[
F_h=\{c_0,\ldots,c_{h-1}\},
\]

with a downstream parity label `beta(c_j) in {E,O}`. The finalized realized-axis system then permits many of these distinct tags to realize the same bookkeeping line.

## 4. Realized-axis layer is between Stage VI and analytic aggregation

The finalized realized-axis property system factors through the Stage-VI formation record and is explicitly independent of the post-Stage-VI choices of term space, component-term map, finite-composition domain, and composition operator.

Therefore the dependency order for applications using all three DSD components is

\[
\boxed{
F_L^{\le6}
\longrightarrow
\text{realized-axis extension}
\longrightarrow
\text{analytic term realization / static aggregation}.
}
\]

A downstream application may explicitly map a realized line/property record into the analytic term space, but this bridge is extra application data. It is not generated automatically by the realized-axis axioms.

## 5. Static Aggregation strict-equivalence numbering is also version-sensitive

The 2026-07-28 manuscript contains a corollary phrased as follows in substance:

- structural comparison satisfies Formation conditions `(E1)-(E9)`;
- analytic realization then supplies `(E10)-(E11)` for terms and composition.

The current Formation manuscript has since been reorganized. In the current version:

- strict equivalence uses `(E1)-(E9)` with component-term compatibility already appearing at `(E9)`;
- preservation of finite compositions follows as an induced corollary from the channel bijection, term compatibility, and linearity.

Accordingly, a future revision of the Static Aggregation paper should avoid hard-coding the old `(E10)-(E11)` numbering. A version-robust statement is preferable:

> channelwise analytic transport realizes/preserves the current component-term map on admitted channels, and linearity then preserves every admitted finite composition; the countable absolute-summability extension is preserved under the stated bounded term-space isomorphism.

This preserves the analytic theorem while removing dependence on obsolete clause numbering.

## 6. Notation should be synchronized

Recommended replacements when the Static Aggregation manuscript is next revised:

- old `\mathcal C_L` -> current admitted-channel notation `\mathfrak C_L` (or explicitly state a local alias once);
- old channel tuple `(H,h,p,a,lambda,rho)` -> `(p,a,lambda,v,rho)`;
- retain `H,h` only through formation-trace/witness notation;
- align the finite composition domain with the current `\mathfrak D_L^{comp}` notation;
- update strict-equivalence references to theorem/definition names rather than old clause numbers where practical.

These are notation/interface changes only.

## 7. Analytic results that do not need to be rederived

The following core Static Aggregation results are unaffected by the upstream tag refactor, provided `c` ranges over the current admitted-channel set:

1. Bochner-integral existence of `T_L^R(c)` under strong measurability and integrability;
2. norm bounds for each realized term;
3. finite composition by addition;
4. countable composition under absolute summability;
5. perturbation/continuity estimates;
6. covariance under channelwise measure/field transport;
7. support-tagged distinction between absent and zero-valued channels;
8. the exact kernel criterion for aggregate injectivity on a specified record class;
9. the one-channel scalar specialization yielding the weighted structural descriptor.

Thus there is no reason to alter the Collatz coefficient/count formulas because of this manuscript-version mismatch.

## 8. Layer-safe Collatz specialization after synchronization

For a fixed finite parity trace choose distinct admitted occurrence channels

\[
F_h=\{c_0,\ldots,c_{h-1}\}.
\]

Map them in the realized-axis layer to two bookkeeping lines `ell_E,ell_O`, and then in the analytic layer use singleton channel realizations with terms

\[
T_L^{\mathfrak R}(c_j)=
\begin{cases}
e_E^{agg},&w_j=0,\\e_O^{agg},&w_j=1.
\end{cases}
\]

Then

\[
\Comp_L^{\mathfrak R}(F_h)
\cong
\begin{pmatrix}e_h\\q_h\end{pmatrix}.
\]

With

\[
\lambda_{EO}=
\begin{pmatrix}-\log2\\\log(3/2)\end{pmatrix},
\]

define

\[
\Lambda_h
=\lambda_{EO}^{T}\Comp_L^{\mathfrak R}(F_h).
\]

The exact Collatz identity is then

\[
\boxed{
T^h(n)
=
\exp\!\left(\lambda_{EO}^{T}\Comp_L^{\mathfrak R}(F_h)\right)n
+\frac{R(w)}{2^h}.
}
\]

The first term is the commutative static aggregate after scalarization; the second is the downstream order-sensitive affine cocycle.

## 9. Practical consequence

For the current Collatz repository:

- keep every exact arithmetic solver unchanged;
- use `dsd-layer-interface-spec.md` as the authoritative DSD application interface;
- treat the older Static Aggregation Formation-interface text as awaiting upstream synchronization;
- do not cite the superseded channel tuple or obsolete strict-equivalence clause numbering in new Collatz notes.

No global Collatz claim follows from this compatibility audit.
