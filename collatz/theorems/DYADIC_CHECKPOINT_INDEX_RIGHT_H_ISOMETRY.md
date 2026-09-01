# Dyadic checkpoint-index / right-H 3-adic isometry

Status: **EXACT / CLOSED for synchronized checkpoint residue pullback at fixed dyadic address**

## Setting

Use the already-closed synchronized checkpoint interface at terminal ternary precision 28.

Let

\[
z_2 = Z\bmod 2^{27},
\qquad 0\le z_2<2^{27},
\]

and parameterize every ordinary checkpoint in that dyadic address by

\[
Z=z_2+2^{27}n,
\qquad n\in\mathbb Z.
\]

For the fixed current right-H factor,

\[
z_H\equiv 2^s Z-C(H_s^*)\pmod{3^{28}},
\]

where

\[
s=630{,}138{,}897.
\]

Substitution gives

\[
z_H(n)\equiv A(z_2)+u n\pmod{3^{28}},
\]

with

\[
A(z_2)=2^s z_2-C(H_s^*)\pmod{3^{28}},
\]

\[
u=2^{s+27}\pmod{3^{28}}.
\]

For the current constants,

\[
u=15{,}139{,}992{,}122{,}704,
\]

and

\[
u^{-1}=13{,}299{,}776{,}895{,}097
\pmod{3^{28}}.
\]

Because `u` is a power of two, it is a unit modulo every `3^ell`.

## Theorem 1 — exact residue-cylinder isometry

For every

\[
1\le \ell\le28
\]

and all integers `n1,n2`,

\[
z_H(n_1)\equiv z_H(n_2)\pmod{3^\ell}
\]

if and only if

\[
n_1\equiv n_2\pmod{3^\ell}.
\]

### Proof

Subtract the affine formulas:

\[
z_H(n_1)-z_H(n_2)
\equiv u(n_1-n_2)\pmod{3^\ell}.
\]

Since `u` is invertible modulo `3^ell`, multiplication by `u` preserves and reflects divisibility by `3^ell`.

Hence the two congruences are equivalent.

Equivalently, multiplication by `u` is a 3-adic isometry on this checkpoint-index coordinate through precision 28.

## Theorem 2 — exact pullback of any right-H residue cylinder

Fix one target residue

\[
z_H\equiv c\pmod{3^\ell},
\qquad 1\le\ell\le28.
\]

Then, for fixed `z2`, this condition is exactly equivalent to one checkpoint-index residue class

\[
\boxed{
 n\equiv
 u^{-1}\bigl(c-A(z_2)\bigr)
 \pmod{3^\ell}.
}
\]

Thus a right-H residue-cylinder query does not require flat enumeration of checkpoint values inside one fixed dyadic address. It pulls back to one arithmetic progression in the ordinary integer checkpoint index `n`.

## Theorem 3 — SAFE corridor slice is a short ordinary interval

Use the already-certified SAFE ordinary checkpoint corridor

\[
Z_{min}\le Z\le Z_{max},
\]

where

\[
Z_{min}=7{,}083{,}549{,}723{,}342{,}395{,}146{,}241,
\]

\[
Z_{max}=9{,}444{,}732{,}965{,}107{,}363{,}299{,}196.
\]

For fixed `z2`, the compatible checkpoint-index values form the exact consecutive interval

\[
I_{z_2}=
\left[
\left\lceil\frac{Z_{min}-z_2}{2^{27}}\right\rceil,
\left\lfloor\frac{Z_{max}-z_2}{2^{27}}\right\rfloor
\right]\cap\mathbb Z.
\]

The largest possible cardinality of such a slice is

\[
\left\lfloor\frac{Z_{max}-Z_{min}}{2^{27}}\right\rfloor+1
=
17{,}592{,}186{,}046{,}876.
\]

Since

\[
3^{28}=22{,}876{,}792{,}454{,}961,
\]

we have

\[
|I_{z_2}|<3^{28}
\]

uniformly for every dyadic address `z2`.

Therefore the full 28-trit map

\[
n\mapsto z_H(n)\pmod{3^{28}}
\]

is injective on each SAFE dyadic checkpoint slice.

This is the indexed form of the synchronized CRT singleton theorem.

## Exact `Pi3` handoff

Because each right-H cylinder modulo `3^ell` pulls back to exactly one residue class of `n modulo 3^ell`, the existing one-dimensional ternary interval quotient applies directly to the checkpoint-index interval:

\[
\Pi^{(3)}_{28}(I_{z_2})
=
\bigl(|I_{z_2}|,\;n_{lo}\bmod3^{28}\bigr).
\]

After a query

\[
n\equiv\rho\pmod{3^\ell},
\]

the survivors are one consecutive child-index interval after writing

\[
n=\rho+3^\ell k.
\]

Thus, at fixed dyadic checkpoint address, synchronized right-H export can be handed to G3 through the already-certified exact `Pi3` interval machinery rather than through a flat list of right-H residues or ordinary checkpoints.

## Computational role

The preferred synchronized join coordinate is now

`fixed z2 × checkpoint-index interval Pi3 × right-H exported residue cylinder`.

The flow is:

1. fix/export the dyadic checkpoint address `z2`;
2. represent the corresponding SAFE ordinary checkpoint slice by its consecutive index interval `I_z2`;
3. pull every right-H residue cylinder back to one `n mod 3^ell` cylinder;
4. use `Pi3` to test/count/refine that intersection exactly;
5. at full precision 28, every surviving `n` is unique inside the slice;
6. reconstruct the ordinary checkpoint `Z=z2+2^27 n`;
7. immediately apply the checkpoint-conditioned source-fiber theorem.

## Scope restriction

This theorem compresses the **export/join coordinate after a right-H residue cylinder has been specified**.

It does **not** prove that the multi-gate right-H language has only one carry path.

It does **not** permit discarding the active carry base or formation/order state while constructing that residue cylinder.

It does **not** prove correction-language membership, same-orbit connectivity, or Collatz.

The following remain invalid:

- prescribed right-H cylinder -> unique carry/grammar path;
- `Pi3` checkpoint-index state -> complete right-H language state;
- one exposed checkpoint -> source membership;
- multiplying marginal dyadic and ternary counts.

## DSD classification

### EXACT / CLOSED

- affine checkpoint-index formula;
- unit/isometry congruence equivalence;
- unique residue pullback for every precision `ell<=28`;
- exact SAFE dyadic-slice interval;
- uniform cardinality `<3^28`;
- injectivity of full 28-trit right-H observation on each SAFE dyadic slice;
- exact compatibility with the existing `Pi3` interval quotient.

### SAFE dependency

The ordinary checkpoint corridor is inherited from the independently certified pre-defect corridor chain.

### OPEN

The multi-gate right-H procedure that generates the admissible exported residue cylinders remains the principal G2 structural gate.

## Certificate

- `../src/A0_s1_routeB_dyadic_checkpoint_index_rightH_isometry_certificate.py`
