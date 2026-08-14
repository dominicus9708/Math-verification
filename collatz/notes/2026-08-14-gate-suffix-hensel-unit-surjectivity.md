# Gate-suffix Hensel unit surjectivity through 12 ternary digits

Date: 2026-08-14

Status: **exact finite residue certificate + exact lifting consequence**.  This concerns the two first-return gate types `G_81` and `G_82` in the length-19 induced rotation.  It is a local arithmetic freedom statement, not a Collatz proof.

## 1. Common right suffix of the first-return gates

In the temporal orientation used for the predecessor-to-current type-0 return block, both `G_81` and `G_82` end with the same three length-19 mechanical factors:

\[
\boxed{
0101101101011011011
\;|\;
0101101101011011011
\;|\;
0101101101011011010.
}
\]

Their mechanical odd counts are

\[
12,\quad12,\quad11,
\]

so the 57-bit suffix contains

\[
\boxed{35}
\]

mechanical odd symbols.

Let `v` be an actual orientation of this suffix and compare it to the mechanical suffix by the relative-height state `(Sigma,M)`.

We consider two fibres:

\[
\boxed{(\Sigma,M)=(0,0)}
\]

and

\[
\boxed{(\Sigma,M)=(-1,-1)}.
\]

The first has 35 actual odd symbols; the second has 34.

## 2. Exact correction residue computation

For an actual binary word of length 57, write its affine correction as `R`, so

\[
T^{57}(x)=\frac{3^q x+R}{2^{57}}.
\]

An exact dynamic program was run with state

\[
(\text{position},\text{relative height},R\bmod3^{12})
\]

and the corresponding floor constraint:

- neutral fibre: relative height never below `0`, final height `0`;
- one-slack fibre: relative height never below `-1`, final height `-1`.

No floating-point arithmetic is used in the residue transition.

For each fibre, the set of final corrections modulo

\[
3^{12}=531,441
\]

has exactly

\[
\boxed{
2\cdot3^{11}=354,294
}
\]

elements.

A correction of any positive-odd-count word is never divisible by 3, because modulo 3 only the contribution of the last odd symbol survives.  Therefore `2*3^11` is the absolute maximum possible number of residues modulo `3^12`.

Hence both fibres attain the maximum:

\[
\boxed{
\mathcal R_{\rm neutral}(12)
=
\mathcal R_{\rm one\text{-}slack}(12)
=
(\mathbb Z/3^{12}\mathbb Z)^\times_{\text{mod }3},
}
\]

where the right side denotes all residue classes not divisible by 3.

Equivalently, every residue

\[
r\pmod{3^{12}},\qquad3\nmid r,
\]

is realized by at least one admissible orientation in each fibre.

## 3. Inheritance by the full `G_81` / `G_82` gate

Keep the entire prefix preceding this 57-bit suffix in the mechanical orientation.  Its relative state is `(0,0)` and therefore does not disturb the suffix fibre state.

Under concatenation,

\[
R_{UV}=3^{q_V}R_U+2^{L_U}R_V.
\]

The suffix has at least 34 actual odd symbols in the two fibres under consideration.  Hence for every

\[
J\le12,
\]

the prefix term is divisible by `3^J`:

\[
3^{q_V}R_U\equiv0\pmod{3^J}.
\]

Multiplication by the unit `2^{L_U}` merely permutes the nonzero-mod-3 residue classes.

Therefore both full first-return gates inherit the same unit surjectivity through 12 ternary digits.

## 4. Full low-digit difference set

Let

\[
U_J:=\{r\pmod{3^J}:3\nmid r\}.
\]

For every target

\[
t\pmod{3^J}
\]

there exist `a,b in U_J` with

\[
a-b\equiv t\pmod{3^J}.
\]

Indeed:

- if `t=0 mod 3`, choose `b=1`;
- if `t=1 mod 3`, choose `b=1`;
- if `t=2 mod 3`, choose `b=2`;

and in each case `b+t` is also nonzero modulo 3.

Thus

\[
\boxed{
U_J-U_J=\mathbb Z/3^J\mathbb Z.
}
\]

Since each member of `U_J` is realized inside the same neutral (or one-slack) fibre, the correction-difference set of that fibre is the full group for every

\[
\boxed{1\le J\le12.}
\]

## 5. Interpretation

The first-return gate therefore has no low-order 3-adic obstruction through twelve ternary digits inside either the neutral or one-slack survival fibre.

Any prescribed low-order carry target can be matched by a same-state orientation pair at the residue level.

This is a **negative/structural result** for proof design: a contradiction cannot come merely from the first twelve Hensel digits of a `G_81` or `G_82` gate.  The obstruction must involve at least one of

1. higher 3-adic digits;
2. positivity / correction ordering needed for an actual smaller predecessor;
3. the dyadic canonical-address channel;
4. the Archimedean headroom channel.

The result also explains why large Euclidean gates can retain substantial alternate-predecessor flexibility despite the severe coefficient/phase constraints: a very small 57-bit suffix already supplies a complete low-order Hensel difference basis.
