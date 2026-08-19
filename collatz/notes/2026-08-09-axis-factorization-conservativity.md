# Conservativity of the realized-axis factorization for the E/O Collatz aggregate

Date: 2026-08-09

Status: **DERIVED INTERFACE PROPOSITION / NO NEW ARITHMETIC ASSUMPTION**

This note answers whether inserting the finalized realized-axis property layer between Formation and Static Aggregation changes the arithmetic content of the present Collatz calculation.

For the minimal E/O application used in this repository, it does not. The axis layer supplies a typed factorization and a compression-safe distinction between channel multiplicity and realized-line rank, but it adds no new numerical law.

## 1. Setup

Let

\[
F_h=\{c_0,\ldots,c_{h-1}\}\subseteq\mathfrak C_L
\]

be the distinct admitted occurrence channels representing one finite parity trace.

Let

\[
\beta:F_h\to\{0,1\}
\]

be the E/O label, with `0=E`, `1=O`.

Choose the realized-axis carrier

\[
E_{ax}^{EO}=\mathbb R^2
\]

and two lines

\[
\ell_E=\operatorname{span}(e_E^{ax}),
\qquad
\ell_O=\operatorname{span}(e_O^{ax}).
\]

Define

\[
\operatorname{AxLine}(c)=
\begin{cases}
\ell_E,&\beta(c)=0,\\
\ell_O,&\beta(c)=1.
\end{cases}
\]

Let the separate static term space be

\[
W_{agg}^{EO}=\mathbb R^2
\]

with basis `e_E^{agg},e_O^{agg}`, and define

\[
\psi(\ell_E)=e_E^{agg},
\qquad
\psi(\ell_O)=e_O^{agg}.
\]

## 2. Factorization proposition

The minimal static E/O term map factors as

\[
\boxed{
\tau_{EO}
=\psi\circ\operatorname{AxLine}.
}
\]

Indeed,

\[
\tau_{EO}(c)
=
\begin{cases}
e_E^{agg},&\beta(c)=0,\\e_O^{agg},&\beta(c)=1,
\end{cases}
\]

which is exactly the value obtained by first realizing the corresponding line and then applying `psi`.

Therefore

\[
\boxed{
\Comp_L^{\mathfrak R}(F_h)
=\sum_{c\in F_h}\psi(\operatorname{AxLine}(c))
=\begin{pmatrix}e_h\\q_h\end{pmatrix}.
}
\]

The same count vector would be obtained by the direct map `tau_EO` without explicitly displaying the axis factorization.

## 3. Conservativity statement

For every fixed finite occurrence support and E/O labeling, inserting the above realized-axis factorization leaves unchanged:

- the static count vector `(e_h,q_h)`;
- the log drift `Lambda_h`;
- the coefficient `3^q/2^h`;
- the downstream order correction `R(w)`;
- the affine iterate `T^h(n)`;
- every exact min-plus/canonical-residue calculation built from the parity trace.

Hence the axis layer is **conservative for the current Collatz arithmetic**.

It should not be cited as an extra number-theoretic premise or as a reason that a Collatz inequality is stronger than its direct parity-vector form.

## 4. What the axis layer does contribute

Although arithmetically conservative, the layer supplies several structural disciplines that are useful in this project.

### 4.1 Channel multiplicity versus line rank

A trace may contain `h` distinct occurrence channels while all of them realize only one or two lines.

Thus

\[
|F_h|=h
\]

but

\[
\operatorname{arank}(p)=
\begin{cases}
0,&h=0,\\
1,&h>0\text{ and only one parity occurs},\\
2,&\text{both E and O occur}.
\end{cases}
\]

This prevents the number of steps from being confused with realized-axis rank.

### 4.2 Ambient dimension versus realized rank

The supplied ambient bookkeeping carrier may remain `R^2` even when only one of the two lines occurs in a particular finite trace. The realized-axis rank is then one, while the downstream term space still has two available count coordinates and the count vector may be `(h,0)` or `(0,h)`.

Thus

\[
\dim E_{ax}^{EO}=2
\]

does not imply

\[
\operatorname{arank}(p)=2.
\]

### 4.3 Representation versus dynamics

The lines `ell_E,ell_O` are bookkeeping realizations. They are not the affine generators `M_E,M_O`, and no dynamical transition law follows from the existence of the lines.

### 4.4 Optional tag-sensitive refinements

The finalized axis system permits two channels on the same line to carry different tag-sensitive property values. The minimal Collatz factorization does not use such properties.

If a future Collatz application introduces a tag-sensitive property that affects the analytic term map, then the factorization through the bare line alone would no longer be valid. Such an extension must state the additional typed property and downstream encoding explicitly.

## 5. Practical rule

Use the realized-axis layer in the Collatz project for:

1. typed E/O bookkeeping;
2. separating repeated channel occurrences from two line classes;
3. making explicit which compression discards tag information;
4. providing an optional interface to later typed property records.

Do not use it as:

1. a substitute for the parity word;
2. an extra spatial dimension claim;
3. an affine-dynamics matrix;
4. an independent number-theoretic assumption.

The exact Collatz proof burden remains in the downstream arithmetic constraints on ordered traces, canonical residues, coefficient survival, and late-lift forcing.
