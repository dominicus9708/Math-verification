# DSD layer interface for the Collatz verification program

Date: 2026-08-09

Status: **INTERFACE SPECIFICATION / SCOPE CORRECTION**

This note updates the Collatz application after the realized-axis property axiom system was finalized. It does not change the standard Collatz arithmetic, the parity-vector affine formula, the exact min-plus solvers, or any finite verification result. Its purpose is to separate the roles of the Formation Axiom System, the realized-axis property system, downstream static aggregation, and Collatz-specific dynamics.

## 1. Four distinct layers

The application is organized as

\[
\boxed{
F_L^{\le 6}
\longrightarrow
\mathcal A_{EO}
\longrightarrow
\mathcal G_{EO}
\longrightarrow
\mathcal D_{\mathrm{Collatz}}
}
\]

where:

1. `F_L^{<=6}` is a fixed Stage-VI formation record containing admitted operational channels;
2. `A_EO` is an optional realized-axis extension that supplies bookkeeping axis carriers for selected inherited channels;
3. `G_EO` is a downstream analytic/static aggregation layer that realizes E/O occurrence terms and their aggregate coefficient descriptor;
4. `D_Collatz` is the Collatz-specific ordered affine/min-plus arithmetic layer.

The realized-axis property system is non-dynamical and pre-aggregation. Therefore the ordered Collatz recurrence, affine matrices, correction cocycle, canonical residue, carry/lift variables, defect transfer, Bellman recurrence, and interval certificates belong to layer 4, not to the primitive axis-property layer.

## 2. Application interpretation is additional data

The realized-axis system starts from inherited Stage-VI operational channels. It does not derive the Collatz parity branches `E` and `O` from arithmetic by itself.

A Collatz application therefore requires an explicit application interpretation. One conservative form is to select two inherited channels

\[
c_E,c_O\in C_L(p)
\]

for one chosen application configuration `p`, and provide a use map for a finite parity word

\[
\boxed{
u_w:\{0,\ldots,h-1\}\to\{c_E,c_O\}}
\]

with

\[
u_w(j)=c_E\iff w_j=0,
\qquad
u_w(j)=c_O\iff w_j=1.
\]

This use map is Collatz-application data. It is not derived by the Formation Axiom System or by the realized-axis property axioms.

The map is intentionally allowed to reuse the same inherited channel at many time indices. The temporal occurrence index `j` belongs to the downstream Collatz record; it is not identified with distinct realized-axis rank or with distinct formation-channel identity.

## 3. Minimal realized-axis extension

Use the finite representational carrier

\[
E^{EO}=\mathbb R^2
\]

with two lines

\[
\ell_E=\operatorname{span}(e_E),
\qquad
\ell_O=\operatorname{span}(e_O).
\]

Select

\[
C^{ax}_{A,p}=\{c_E,c_O\}
\]

and set

\[
\boxed{
\operatorname{AxLine}(c_E)=\ell_E,
\qquad
\operatorname{AxLine}(c_O)=\ell_O.
}
\]

This satisfies the intended bookkeeping realization when Primitive Axiom PI holds. No bilinear, normal, closure, quaternion, stiffness, or other property structure is required for the Collatz application. Property declarations may therefore remain empty unless a later application has a specific typed reason to add one.

Crucially, `E^{EO}` is a configuration-relative representational carrier, not a claim of an additional physical two-dimensional space.

## 4. Static occurrence aggregation

The static aggregation is performed on indexed occurrences, not by counting distinct axis channels.

Define the downstream component-term map

\[
\tau_{EO}(u_w(j))=
\begin{cases}
(1,0)^T,&u_w(j)=c_E,\\
(0,1)^T,&u_w(j)=c_O.
\end{cases}
\]

Then

\[
\boxed{
\mathbf c_h
=\sum_{j=0}^{h-1}\tau_{EO}(u_w(j))
=\binom{e_h}{q_h}.
}
\]

This is a reduced aggregate descriptor. It intentionally forgets the ordering of the occurrences.

Introduce the downstream analytic log-weight covector

\[
\lambda_{EO}
=
\begin{pmatrix}
-\log 2\\
\log(3/2)
\end{pmatrix}.
\]

The aggregate multiplicative drift is

\[
\boxed{
\Lambda_h
=\lambda_{EO}^{T}\mathbf c_h
=-e_h\log2+q_h\log(3/2).
}
\]

Hence

\[
\boxed{
\exp(\Lambda_h)=\frac{3^{q_h}}{2^h}.
}
\]

The previously used diagonal matrix

\[
G=\operatorname{diag}(-\log2,\log(3/2))
\]

may still be used as an analytic representation, but it is not to be identified with a primitive realized-axis property block. The covector form is the default because it introduces no artificial off-diagonal defined-zero relation.

## 5. Distinguish the two two-dimensional spaces

The E/O bookkeeping carrier and the affine homogeneous state space are different typed objects:

\[
\boxed{E^{EO}\neq H^{aff}.}
\]

`E^{EO}` realizes the bookkeeping axes `ell_E, ell_O`.

The affine state space `H^aff` carries homogeneous coordinates `(n,1)^T` and the arithmetic generators

\[
M_E=
\begin{pmatrix}
1/2&0\\0&1
\end{pmatrix},
\qquad
M_O=
\begin{pmatrix}
3/2&1/2\\0&1
\end{pmatrix}.
\]

These matrices are Collatz affine-dynamics operators. They are not the optional property blocks of the realized-axis axiom system.

## 6. Ordered correction remains downstream

For a parity word `w` with odd positions

\[
0\le d_0<\cdots<d_{q-1}<h,
\]

define

\[
R(w)=\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i}.
\]

Then

\[
M_w=
\begin{pmatrix}
3^q/2^h&R(w)/2^h\\
0&1
\end{pmatrix}
\]

and

\[
\boxed{
T^h(n)
=\exp(\Lambda_h)n+\frac{R(w)}{2^h}
=\frac{3^q n+R(w)}{2^h}.
}
\]

This is the canonical two-term decomposition for the current program:

- `exp(Lambda_h)n`: commutative E/O occurrence aggregate;
- `R(w)/2^h`: order-sensitive affine cocycle.

The first term factors through the static count descriptor. The second does not.

## 7. Compression discipline inherited from the finalized axis system

Equal realized-axis rank, equal matrix size, or equal reduced scalar aggregate does not recover a complete typed axis-property descriptor. The Collatz application has an analogous but purely arithmetic instance:

words with the same `(e_h,q_h)` have the same `Lambda_h` but can have different `R(w)`.

For example, at length two the words `EO` and `OE` have the same count vector `(1,1)` and the same multiplicative coefficient `3/4`, but distinct affine corrections.

Therefore the E/O static aggregate must never be treated as a complete classifier of a Collatz parity word. Order-sensitive calculations must retain `w`, `R`, or an exact equivalent such as `(r,y)` / defect state.

## 8. Consequence for existing exact solvers

No numerical recurrence changes are required.

The authoritative exact state remains

\[
(k,q;r,y),
\]

or the already proved finite-horizon quotients derived from it. Likewise, defect/carry, high-resolution cylinders, min-plus Bellman, endpoint arithmetic-progression certificates, and late-lift targets remain downstream arithmetic structures.

The only required refactor is semantic and typological:

1. add the Collatz application interpretation `u_w` (or an equivalent explicitly typed interface);
2. reserve realized-axis terminology for the `E^{EO}` bookkeeping carrier;
3. move numeric E/O weights to the downstream aggregation/analytic layer;
4. reserve `M_E,M_O` and all ordered transfer states for the Collatz dynamics layer;
5. state explicitly whenever a reduced aggregate discards parity order.

## 9. Dependency diagram

\[
\boxed{
\begin{array}{c}
\text{Collatz parity occurrence }(j,w_j)\\
\downarrow\;u_w\\
\text{selected inherited tag }c_E\text{ or }c_O\\
\downarrow\;\operatorname{AxLine}\\
\ell_E\text{ or }\ell_O\subset E^{EO}\\
\downarrow\;\tau_{EO}\;\text{(downstream)}\\
\mathbf c_h=(e_h,q_h)^T\\
\downarrow\;\lambda_{EO}^{T}\\
\Lambda_h\\
\end{array}
}\]

in parallel with

\[
\boxed{
 w\longrightarrow R(w)\longrightarrow M_w\longrightarrow T^h(n).
}
\]

The two paths meet only in the exact identity

\[
T^h(n)=e^{\Lambda_h}n+R(w)/2^h.
\]

## 10. Claim status

This note is an interface correction prompted by the finalized realized-axis axiom system. It is not a new Collatz theorem. The arithmetic identities used here are the existing exact parity-vector/affine identities already audited elsewhere in the repository.
