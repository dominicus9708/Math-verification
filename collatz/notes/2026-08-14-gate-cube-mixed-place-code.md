# Mixed-place anti-triangular code of a gate Hensel cube

Date: 2026-08-14

Status: **exact constructive cross-base coding theorem** for the explicit gate-wide orientation cubes.  It shows that the same pair coordinates which form a full low-order Hensel difference basis also form an injective dyadic difference code in the opposite order.  This is a structural boundary theorem, not a Collatz proof.

## 1. Cube coordinate geometry

Consider either explicit gate-wide cube from the preceding note.  Write it in the generic form

\[
1^F(01/10)^J0.
\]

Every vertex has

\[
q=F+J
\]

actual odd symbols.  Number the variable pairs in temporal order

\[
j=0,1,\ldots,J-1.
\]

The left time position of pair `j` is

\[
\boxed{p_j=F+2j,}
\]

and its unique odd event has rank

\[
\boxed{k_j=F+j+1.}
\]

Hence the correction exponent attached to that odd event is

\[
q-k_j=J-1-j.
\]

For two cube vertices define

\[
\epsilon_j\in\{-1,0,1\}
\]

according to whether the pair orientation moves from `01` to `10`, agrees, or moves in the opposite direction.  Up to the fixed global sign convention, their exact affine-correction difference is

\[
\boxed{
D(\epsilon)
=
\sum_{j=0}^{J-1}
\epsilon_j\,3^{J-1-j}2^{F+2j}.
}
\]

Thus one and the same coordinate has

\[
\boxed{
\begin{array}{c|c|c}
\text{pair }j&v_3&v_2\\\hline
j&J-1-j&F+2j.
\end{array}
}
\]

The 3-adic and 2-adic triangular orders are therefore reversed.

## 2. Hensel map is a bijection

Divide out the fixed dyadic factor `2^F`.  Modulo `3^J`,

\[
\boxed{
T(\epsilon)
:=2^{-F}D(\epsilon)
\equiv
\sum_{j=0}^{J-1}
\epsilon_j3^{J-1-j}4^j
\pmod{3^J}.
}
\]

There are exactly `3^J` coefficient vectors `epsilon` and exactly `3^J` target residues.

To prove injectivity, take two distinct vectors and let `j_*` be the **largest** temporal index where they differ.  At that coordinate their difference coefficient belongs to

\[
\{-2,-1,1,2\}
\]

and is therefore a 3-adic unit.  The corresponding term has 3-adic valuation

\[
J-1-j_*.
\]

Every term with smaller temporal index has strictly larger 3-adic valuation, so cancellation at that lowest valuation is impossible.  Hence the two vectors give different residues modulo `3^J`.

Therefore

\[
\boxed{
T:\{-1,0,1\}^J
\longrightarrow
\mathbb Z/3^J\mathbb Z
}
\]

is a bijection.

This is the explicit balanced-Hensel lifting already implicit in the full difference-set theorem, now with a unique coordinate vector attached to each target.

## 3. Dyadic canonical-start difference

For a fixed odd count `q`, the canonical 2-adic start coordinate of a parity block is

\[
\rho=-3^{-q}R.
\]

Hence the canonical-start difference associated with the same cube vector is

\[
\Delta\rho(\epsilon)
=-3^{-q}D(\epsilon).
\]

After removing the common low factor `2^F`, define

\[
\boxed{
Y(\epsilon)
:=2^{-F}\Delta\rho(\epsilon)
\equiv
-
\sum_{j=0}^{J-1}
\epsilon_j3^{-(F+j+1)}2^{2j}
\pmod{2^{2J}}.
}
\]

Every coefficient `3^{-(F+j+1)}` is an odd 2-adic unit.

## 4. Dyadic map is injective

Take two distinct vectors and let `j_0` be the **smallest** temporal index where they differ.  Their difference coefficient at `j_0` lies in

\[
\{-2,-1,1,2\}.
\]

If it is odd, the corresponding dyadic valuation is exactly

\[
2j_0.
\]

If it is `+/-2`, the valuation is exactly

\[
2j_0+1.
\]

Every later coordinate is divisible by

\[
2^{2j_0+2}.
\]

Therefore the lowest nonzero dyadic term cannot be cancelled by later coordinates.  Hence

\[
\boxed{
Y:\{-1,0,1\}^J
\hookrightarrow
\mathbb Z/2^{2J}\mathbb Z
}
\]

is injective.

The image contains exactly

\[
\boxed{3^J}
\]

of the

\[
4^J
\]

possible normalized `2J`-bit dyadic blocks.

## 5. Exact mixed-place graph

Since the Hensel map `T` is bijective, every ternary target

\[
t\in\mathbb Z/3^J\mathbb Z
\]

has a unique cube difference vector

\[
\epsilon(t).
\]

The same vector determines one dyadic block

\[
\Phi_J(t):=Y(\epsilon(t)).
\]

Thus the cube defines an exact graph

\[
\boxed{
\Gamma_J
=
\{(t,\Phi_J(t)):t\in\mathbb Z/3^J\mathbb Z\}
\subset
\mathbb Z/3^J\mathbb Z
\times
\mathbb Z/2^{2J}\mathbb Z.
}
\]

The cube therefore does **not** provide independent ternary and dyadic choices.  It provides a deterministic anti-triangular cross-base code: low Hensel digits are solved from the temporally late pair coordinates, whereas the low normalized dyadic bits are controlled by the temporally early coordinates.

## 6. Gate-scale dimensions

For the certified gate-wide cubes:

\[
\boxed{
\begin{array}{c|c|c}
\text{gate/fibre}&J&\text{dyadic code block length }2J\\\hline
G_{81}\text{ neutral}&567&1134\\
G_{81}\text{ one-slack}&568&1136\\
G_{82}\text{ neutral}&574&1148\\
G_{82}\text{ one-slack}&575&1150\\
G_{13}\text{ neutral}&7390&14780\\
G_{13}\text{ one-slack}&7391&14782\\
G_{14}\text{ neutral}&7958&15916\\
G_{14}\text{ one-slack}&7959&15918
\end{array}
}
\]

Within this explicit section of the fibre, the normalized dyadic image density is

\[
\boxed{\left(\frac34\right)^J.}
\]

For example, at `G_81` neutral scale this is approximately `10^-70.84`; at the second-return scales it is below `10^-923` and `10^-994`, respectively.

These densities are descriptive properties of the **explicit cube section only**.  They are not probabilities and do not bound the full same-state fibre, which may contain many additional orientations outside the cube.

## 7. Why this matters for the boundary problem

The previous gate-wide theorem said that low Hensel targets are highly flexible.  The present theorem adds the missing qualification:

> inside an explicit triangular cube, solving a Hensel target fixes a unique dyadic difference block rather than leaving the dyadic channel free.

This is precisely the mixed-place coupling needed by the two-ended proof architecture.

It suggests a deterministic boundary test of the form

\[
\boxed{
\text{required Hensel carry }t
\quad\Longrightarrow\quad
\Phi_J(t)
\stackrel{?}{=}
\text{required ordinary-start dyadic block}.
}
\]

A mismatch excludes **that cube section** immediately.

## 8. Limitation

The explicit cube is only a subset of the full neutral or one-slack orientation fibre.  Other admissible orientations with the same Hensel target can have different dyadic differences.

Therefore failure of the graph-membership test for `Gamma_J` does **not** yet exclude the whole gate fibre.

The next strengthening must analyze the kernel/fibre over a fixed Hensel target:

\[
\boxed{
\mathcal K_t
=
\{\text{admissible orientations with correction }\equiv t\pmod{3^J}\}
}
\]

and bound or characterize its dyadic image.

A terminal theorem would show that the dyadic image of the full Hensel fibre cannot contain the ordinary zero-lift target once the early first-defect channel and headroom constraints are imposed.

The current result provides an exact anti-triangular section and identifies the correct next object: **the dyadic diameter/image of a fixed Hensel fibre**, not the marginal Hensel residue set alone.