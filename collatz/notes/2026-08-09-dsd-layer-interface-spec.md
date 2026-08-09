# DSD layer interface for the Collatz verification program

Date: 2026-08-09

Status: **INTERFACE SPECIFICATION / SCOPE CORRECTION**

This note updates the Collatz application after the realized-axis property axiom system was finalized and after direct comparison with the channel-indexed static aggregation manuscript. It does not change the standard Collatz arithmetic, the parity-vector affine formula, the exact min-plus solvers, or any finite verification result. Its purpose is to separate the roles of the Formation Axiom System, the realized-axis property system, downstream static aggregation, and Collatz-specific dynamics.

## 1. Four distinct layers

The application is organized as

\[
\boxed{
F_L^{\le 6}
\longrightarrow
\mathcal A_{EO}
\longrightarrow
\mathfrak R_{EO}
\longrightarrow
\mathcal D_{\mathrm{Collatz}}
}
\]

where:

1. `F_L^{<=6}` is a fixed Stage-VI channel-complete formation record containing admitted operational channels;
2. `A_EO` is a realized-axis extension over that fixed Stage-VI record;
3. `R_EO` is a downstream channel-indexed analytic realization of component terms and their static composition;
4. `D_Collatz` is the Collatz-specific ordered affine/min-plus arithmetic layer.

The finalized realized-axis property system is non-dynamical and pre-aggregation. It is also independent of the post-Stage-VI term space, component-term map, composition domain, and composition operator. Therefore the ordered Collatz recurrence, affine matrices, correction cocycle, canonical residue, carry/lift variables, defect transfer, Bellman recurrence, and interval certificates belong to layer 4, not to the primitive axis-property layer.

## 2. A finite trace requires occurrence-specific admitted channels

The realized-axis system starts from inherited Stage-VI operational channels. It does not derive Collatz parity steps from arithmetic by itself.

Likewise, the static aggregation layer composes a family of admitted channels

\[
F\subseteq\mathcal C_L
\]

by

\[
\Comp_L^{\mathfrak R}(F)
=\sum_{c\in F}T_L^{\mathfrak R}(c).
\]

Because `F` is a channel family rather than a multiset of repeated uses of one channel, a literal DSD realization of a finite Collatz parity word should preserve each step occurrence as a distinct admitted channel.

For a fixed finite word

\[
w=(w_0,\ldots,w_{h-1})\in\{0,1\}^h,
\]

the Collatz application therefore supplies an injective occurrence interpretation

\[
\boxed{
\iota_w:\{0,\ldots,h-1\}\hookrightarrow C_L(p),
\qquad
j\mapsto c_j,
}
\]

for one chosen application configuration `p`, together with the parity label

\[
\boxed{
\beta(c_j)=
\begin{cases}
E,&w_j=0,\\
O,&w_j=1.
\end{cases}
}
\]

The channels `c_j` are distinct even when their parity labels coincide. This occurrence-channel construction is Collatz-application data. The Formation Axiom System does not automatically provide it from the integer recurrence, and the realized-axis axioms do not create new formation channels.

The DSD encoding is therefore conditional on choosing a Stage-VI application model containing the required finite channel family. The Collatz arithmetic itself remains meaningful independently of this encoding.

## 3. Minimal realized-axis extension

Use the finite representational carrier

\[
E_{ax}^{EO}=\mathbb R^2
\]

with two lines

\[
\ell_E=\operatorname{span}(e_E^{ax}),
\qquad
\ell_O=\operatorname{span}(e_O^{ax}).
\]

Select the occurrence channels

\[
C^{ax}_{A,p}=\{c_0,\ldots,c_{h-1}\}
\]

and set

\[
\boxed{
\operatorname{AxLine}(c_j)=
\begin{cases}
\ell_E,&\beta(c_j)=E,\\
\ell_O,&\beta(c_j)=O.
\end{cases}
}
\]

Thus many distinct tagged channels may realize the same line. The number of selected channels is `h`, while the realized-axis rank is at most two. This uses exactly the finalized distinction between channel multiplicity and realized-axis rank.

No bilinear, normal, closure, quaternion, stiffness, or other optional property structure is required for the Collatz application. Property declarations may remain empty unless a later application has a specific typed reason to add one.

Crucially, `E_ax^{EO}` is a configuration-relative representational carrier, not a claim of an additional physical two-dimensional space.

## 4. Static aggregation as a literal channel-indexed realization

Introduce a separate Banach term space

\[
W_{agg}^{EO}=\mathbb R^2
\]

with basis `e_E^{agg},e_O^{agg}`. It is not identified with `E_ax^{EO}` by the axis axioms.

If one wants the aggregate realization to factor through the realized-axis bookkeeping, supply the downstream interpretation

\[
\psi:\{\ell_E,\ell_O\}\to W_{agg}^{EO},
\qquad
\psi(\ell_E)=e_E^{agg},
\quad
\psi(\ell_O)=e_O^{agg}.
\]

For every occurrence channel `c_j`, choose the singleton realization

\[
X_{c_j}=\{*\},
\qquad
\mu_{c_j}(\{*\})=1,
\qquad
w_{c_j}(*)=1,
\]

and the constant local field

\[
\zeta_{c_j}(*)
=\psi(\operatorname{AxLine}(c_j)).
\]

Then the channel-indexed static term is literally

\[
\boxed{
T_L^{\mathfrak R}(c_j)
=\int_{X_{c_j}}\zeta_{c_j}w_{c_j}\,d\mu_{c_j}
=
\begin{cases}
e_E^{agg},&w_j=0,\\e_O^{agg},&w_j=1.
\end{cases}
}
\]

For

\[
F_h=\{c_0,\ldots,c_{h-1}\}
\]

the static composition is therefore

\[
\boxed{
\Comp_L^{\mathfrak R}(F_h)
=e_h e_E^{agg}+q_h e_O^{agg}
\cong
\binom{e_h}{q_h}.
}
\]

This is a reduced aggregate descriptor. It intentionally forgets the temporal ordering of the distinct occurrence channels.

## 5. Analytic scalarization of the static count vector

Define the downstream log-weight covector

\[
\lambda_{EO}
=
\begin{pmatrix}
-\log 2\\
\log(3/2)
\end{pmatrix}.
\]

Applied to the static aggregate,

\[
\boxed{
\Lambda_h
=\lambda_{EO}^{T}
\begin{pmatrix}e_h\\q_h\end{pmatrix}
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

may still be used as an analytic operator on `W_agg^{EO}`, but it is not to be identified with a primitive realized-axis property block. The covector form is the default because it introduces no artificial off-diagonal defined-zero relation.

## 6. Three different two-dimensional spaces

Three spaces may all be represented by `R^2`, but they have different types and must not be silently identified:

\[
\boxed{
E_{ax}^{EO}
\neq
W_{agg}^{EO}
\neq
H^{aff}.
}
\]

1. `E_ax^{EO}` is the realized-axis bookkeeping carrier containing `ell_E,ell_O`.
2. `W_agg^{EO}` is the Banach term space containing the static aggregate `(e_h,q_h)`.
3. `H^aff` is the affine homogeneous state space containing `(n,1)^T`.

The first bridge, when used, is the explicitly supplied downstream map `psi`. The second bridge is not a carrier identification at all; Collatz arithmetic uses the scalar aggregate `Lambda_h` together with an independent order-sensitive cocycle.

The affine generators on `H^aff` are

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

These are Collatz affine-dynamics operators. They are not the optional property blocks of the realized-axis axiom system and are not the static aggregation operator `G`.

## 7. Ordered correction remains downstream

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

- `exp(Lambda_h)n`: commutative E/O channel aggregate after scalarization;
- `R(w)/2^h`: order-sensitive affine cocycle.

The first term factors through the static aggregate. The second does not.

## 8. Compression discipline inherited from both DSD layers

The finalized realized-axis paper proves that equal realized-axis rank, equal matrix size, or a selected finite-coordinate scalar summary need not recover the full typed axis-property descriptor.

The static aggregation manuscript likewise treats an aggregate as a reduced representative unless an injectivity condition is proved; channel-resolved support records retain distinctions that an aggregate can lose.

The Collatz application has an exact arithmetic instance of the same warning:

words with the same `(e_h,q_h)` have the same `Lambda_h` but can have different `R(w)`.

For example, at length two the chronological words `EO` and `OE` have the same count vector `(1,1)` and the same multiplicative coefficient `3/4`, but

\[
R(EO)=2,
\qquad
R(OE)=1,
\]

so their affine offsets are `1/2` and `1/4` respectively.

Therefore the E/O static aggregate must never be treated as a complete classifier of a Collatz parity word. Order-sensitive calculations must retain `w`, `R`, or an exact equivalent such as `(r,y)` / defect state.

## 9. Consequence for existing exact solvers

No numerical recurrence changes are required.

The authoritative exact state remains

\[
(k,q;r,y),
\]

or the already proved finite-horizon quotients derived from it. Likewise, defect/carry, high-resolution cylinders, min-plus Bellman, endpoint arithmetic-progression certificates, and late-lift targets remain downstream arithmetic structures.

The required refactor is semantic and typological:

1. represent a fixed finite parity trace by distinct Stage-VI occurrence channels `c_j` if the channel-indexed static aggregation layer is used literally;
2. map those distinct tags to the two realized bookkeeping lines `ell_E,ell_O`;
3. keep `E_ax^{EO}`, `W_agg^{EO}`, and `H^aff` type-distinct;
4. realize the static terms only after the axis layer, through explicit analytic realization data;
5. reserve `M_E,M_O` and all ordered transfer states for the Collatz dynamics layer;
6. state explicitly whenever a reduced aggregate discards parity order.

## 10. Dependency diagram

For a fixed finite parity word:

\[
\boxed{
\begin{array}{c}
\text{occurrence }j\text{ with parity }w_j\\
\downarrow\;\iota_w\\
\text{distinct admitted channel }c_j\\
\downarrow\;\operatorname{AxLine}\\
\ell_E\text{ or }\ell_O\subset E_{ax}^{EO}\\
\downarrow\;\psi\;\text{and channel realization}\\
T_L^{\mathfrak R}(c_j)\in W_{agg}^{EO}\\
\downarrow\;\Comp_L^{\mathfrak R}\\
(e_h,q_h)^T\\
\downarrow\;\lambda_{EO}^{T}\\
\Lambda_h
\end{array}
}
\]

in parallel with the order-sensitive arithmetic path

\[
\boxed{
 w\longrightarrow R(w)\longrightarrow M_w\longrightarrow T^h(n).
}
\]

The two paths meet only in the exact identity

\[
\boxed{
T^h(n)=e^{\Lambda_h}n+R(w)/2^h.
}
\]

## 11. Claim status

This note is an interface correction prompted by the finalized realized-axis axiom system and the channel-indexed static aggregation manuscript. It is not a new Collatz theorem. The arithmetic identities used here are the existing exact parity-vector/affine identities already audited elsewhere in the repository.
