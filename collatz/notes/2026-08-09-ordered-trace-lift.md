# Ordered-trace lift over the DSD channel aggregate

Date: 2026-08-09

Status: **DERIVED EXACT INTERFACE LEMMA / NO NEW COLLATZ CLAIM**

This note completes the type-safe interface between a finite DSD channel family and the order-sensitive affine correction of a Collatz parity trace.

The core point is simple: the Formation and Static Aggregation layers use an unordered finite channel family, whereas the Collatz correction depends on chronological order. Therefore the order must be retained as additional application data rather than inserted into the non-dynamical realized-axis or static-aggregation layers.

## 1. Finite occurrence support

Fix a parity trace length `h` and a finite family of distinct admitted occurrence channels

\[
F_h=\{c_0,\ldots,c_{h-1}\}\subseteq\mathfrak C_L.
\]

The static DSD support `F_h` is an unordered set.

Supply a parity-label map

\[
\boxed{\beta:F_h\to\{0,1\}}
\]

with `0=E`, `1=O`.

To recover the Collatz time ordering, additionally supply a bijection

\[
\boxed{
\theta_h:\{0,\ldots,h-1\}\xrightarrow{\sim}F_h.
}
\]

The pair `(F_h,theta_h)` is an **ordered trace enrichment** of the static channel support. The map `theta_h` is downstream Collatz-application data; it is not a coordinate of the Formation Axiom System, the realized-axis property system, or the static composition operator.

The parity word represented by the enrichment is

\[
\boxed{w_j=\beta(\theta_h(j)).}
\]

## 2. Static aggregation forgets theta

Use the singleton E/O term realization from `dsd-layer-interface-spec.md`:

\[
T_L^{\mathfrak R}(c)=
\begin{cases}
e_E^{agg},&\beta(c)=0,\\e_O^{agg},&\beta(c)=1.
\end{cases}
\]

Then

\[
\Comp_L^{\mathfrak R}(F_h)
= e_h e_E^{agg}+q_h e_O^{agg},
\]

where

\[
e_h=\#\beta^{-1}(0),\qquad q_h=\#\beta^{-1}(1).
\]

This expression depends only on `(F_h,beta)` and is invariant under replacement of `theta_h` by any other ordering of the same channel support.

Thus static aggregation factors through the forgetful map

\[
(F_h,\beta,\theta_h)\longmapsto(F_h,\beta).
\]

## 3. Ordered affine correction as a functional of the trace enrichment

Put

\[
b_j:=\beta(\theta_h(j)).
\]

Let

\[
q_h=\sum_{j=0}^{h-1}b_j,
\qquad
q_{j+1}=\sum_{t=0}^{j}b_t.
\]

The number of odd steps strictly after position `j` is

\[
q_h-q_{j+1}.
\]

Therefore the exact order-sensitive correction is

\[
\boxed{
R(F_h,\beta,\theta_h)
=
\sum_{j=0}^{h-1}
 b_j\,2^j\,3^{q_h-q_{j+1}}.
}
\]

If the odd positions are `d_0<...<d_{q_h-1}`, this reduces to the standard form

\[
R=\sum_{i=0}^{q_h-1}2^{d_i}3^{q_h-1-i}.
\]

Hence the usual correction is exactly an ordered-trace functional on the DSD occurrence-channel support.

## 4. Complete layer-safe iterate formula

Let

\[
\lambda_{EO}=
\begin{pmatrix}-\log2\\\log(3/2)\end{pmatrix}
\]

and identify the static aggregate with the count vector

\[
\Comp_L^{\mathfrak R}(F_h)
\cong
\begin{pmatrix}e_h\\q_h\end{pmatrix}.
\]

Then

\[
\Lambda_h
=\lambda_{EO}^{T}\Comp_L^{\mathfrak R}(F_h)
\]

and the accelerated Collatz iterate is

\[
\boxed{
T^h(n)
=
\exp\!\left(
\lambda_{EO}^{T}\Comp_L^{\mathfrak R}(F_h)
\right)n
+
\frac{R(F_h,\beta,\theta_h)}{2^h}.
}
\]

Equivalently,

\[
T^h(n)=\frac{3^{q_h}n+R(F_h,\beta,\theta_h)}{2^h}.
\]

This is the final typed two-term decomposition presently recommended for the Collatz project.

## 5. Exact non-factorization through the static aggregate

There is no function of the static count aggregate alone that recovers `R` for all ordered traces.

Proof by the length-two support with one E-labelled and one O-labelled channel. Order them as `EO` and `OE`. Both orderings have

\[
\Comp_L^{\mathfrak R}(F_2)\cong(1,1)^T
\]

and the same multiplicative coefficient `3/4`, but

\[
R(EO)=2,
\qquad
R(OE)=1.
\]

Thus `R` does not factor through `Comp`.

This is the Collatz-specific analogue of the general DSD warning that an aggregate need not reconstruct the support-resolved structure that generated it.

## 6. Support-resolved record versus ordered trace record

The static analytic paper retains a support-tagged record

\[
\Rec_L^{\mathfrak R}(F_h)
=\left(F_h,(T_L^{\mathfrak R}(c))_{c\in F_h}\right).
\]

For Collatz use, the minimal order-enriched record is therefore

\[
\boxed{
\Rec_{L,\mathrm{ord}}^{\mathfrak R}(F_h,\theta_h)
=
\left(
F_h,
(T_L^{\mathfrak R}(c))_{c\in F_h},
\theta_h
\right).
}
\]

The first two coordinates are static and support-resolved. The final coordinate is application-level chronological structure.

No claim is made that this order-enriched record belongs to the core Static Aggregation manuscript. It is a Collatz-specific downstream enrichment.

## 7. A canonical finite application witness for any binary word

For bookkeeping purposes, a finite word may be represented by distinct items `a_0,...,a_{h-1}` in one application configuration, one parity quantity kind `lambda_par`, assigned values

\[
q_{L,\lambda_{par}}(a_j)=w_j\in\{0,1\},
\]

and a supplied role that admits the channels

\[
\boxed{
c_j=(p,a_j,\lambda_{par},w_j,\rho_{step}).}
\]

Provided the surrounding finite Formation data satisfy the current formation hypotheses, these channels are distinct because their material-item coordinate is distinct. The realized-axis extension may then send every `w_j=0` tag to `ell_E` and every `w_j=1` tag to `ell_O`.

This witness is an application realization, not an assertion that Collatz arithmetic intrinsically consists of DSD formation channels.

## 8. Consequence for the proof program

No exact solver state changes.

The ordered trace `theta_h` is already represented computationally by the parity word or equivalent state information. The purpose of this note is only to place that information at the correct layer:

\[
\boxed{
\text{Formation support}
\to
\text{Axis typing}
\to
\text{Static aggregate}
}
\]

in parallel with

\[
\boxed{
\text{ordered trace enrichment}
\to
R
\to
\text{affine/min-plus arithmetic}.
}
\]

The two branches combine in the exact iterate formula of Section 4.
