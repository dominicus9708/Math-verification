# Neutral correction difference-full composition theorem

Date: 2026-08-13

Status: **exact additive-combinatorial composition theorem + certified U6/U7 base cases**.  It proves totality of the neutral correction-credit transducer for every macroblock built by concatenating the certified base blocks.  It does not prove that an actual Collatz candidate must enter a positive-credit orientation and is not a proof of Collatz.

## 1. Neutral correction residue sets

Let `A` be a deterministic mechanical macroblock of time length `L_A` and mechanical odd count `Q_A`.  Let

\[
\mathcal N(A)
\]

be a family of actual orientations with relative state

\[
(\Sigma,M)=(0,0).
\]

Every member therefore has exactly `Q_A` actual odd symbols.

Define

\[
S_A
=\{R(a)\bmod3^{Q_A}:a\in\mathcal N(A)\}.
\]

Call `A` **difference-full** when

\[
\boxed{
S_A-S_A
=\mathbb Z/3^{Q_A}\mathbb Z.
}
\]

## 2. Concatenation theorem

Let `A` and `B` be difference-full neutral macroblocks.  Consider only the Cartesian neutral subfamily

\[
\mathcal N(A)\mathcal N(B)
\subseteq\mathcal N(AB).
\]

For two concatenated orientations,

\[
R(a_1b_1)-R(a_2b_2)
=3^{Q_B}\bigl(R(a_1)-R(a_2)\bigr)
+2^{L_A}\bigl(R(b_1)-R(b_2)\bigr).
\]

Take an arbitrary target residue

\[
y\pmod{3^{Q_A+Q_B}}.
\]

Because `B` is difference-full and `2^L_A` is a unit modulo powers of three, choose `b_1,b_2` such that

\[
2^{L_A}(R(b_1)-R(b_2))
\equiv y
\pmod{3^{Q_B}}.
\]

Then

\[
y-2^{L_A}(R(b_1)-R(b_2))
=3^{Q_B}c
\]

for a uniquely determined

\[
c\pmod{3^{Q_A}}.
\]

Since `A` is difference-full, choose `a_1,a_2` satisfying

\[
R(a_1)-R(a_2)
\equiv c
\pmod{3^{Q_A}}.
\]

Substitution yields the target residue `y` modulo \(3^{Q_A+Q_B}\).  Therefore

\[
\boxed{
S_{AB}-S_{AB}
=\mathbb Z/3^{Q_A+Q_B}\mathbb Z.
}
\]

Thus difference-fullness is closed under concatenation.

## 3. U6 base certificate

For

\[
U_6=1010110110101101101,
\qquad L=19,\ Q=12,
\]

the exact neutral fibre has

\[
\boxed{11,433}
\]

orientations and exactly the same number of distinct correction residues modulo

\[
3^{12}=531,441.
\]

Exact pairwise difference enumeration certifies

\[
\boxed{
S_6-S_6
=\mathbb Z/3^{12}\mathbb Z.
}
\]

The neutral correction extrema are

\[
527,345,\qquad2,960,239,
\]

with width

\[
\boxed{W_6=2,432,894.}
\]

This is verified by `collatz/src/u6_neutral_difference_full_certificate.cpp`.

## 4. U7 base certificate

For

\[
U_7=011011011010110110101101101,
\qquad L=27,\ Q=17,
\]

the exact neutral fibre contains

\[
1,741,350
\]

orientations and

\[
1,478,620
\]

distinct correction residues modulo \(3^{17}\).

A deterministic 90,000-element subset already has full cyclic difference set, so

\[
\boxed{
S_7-S_7
=\mathbb Z/3^{17}\mathbb Z.
}
\]

This stronger finite certificate is recorded separately in `2026-08-13-u7-neutral-difference-basis-uniform-credit-growth.md`.

## 5. Consequence for the Euclidean hierarchy

Every later deterministic macroblock formed by concatenating copies of `U6` and `U7` has a neutral Cartesian subfibre whose correction residue difference set is the full group modulo the appropriate power of three.

Hence, for every such macroblock `V` with length `L` and odd count `Q`, the neutral quotient transition

\[
\boxed{
D'
=\frac{R_h-R_l+2^L D}{3^Q}
}

has at least one valid neutral orientation pair for **every integer input \(D\)**.

Equivalently:

\[
\boxed{
\mathcal T_V(D)\ne\varnothing
\quad\text{for every }D\in\mathbb Z.
}
\]

Thus the correction-credit transducer cannot die merely because a required 3-adic residue class is absent.  Any obstruction must come from a stronger condition such as credit sign/size, actual-orientation coverage, headroom, or compatibility with the ordinary canonical address.

## 6. Width recursion

If `W_A,W_B` bound the exact correction widths of the chosen neutral subfamilies, then concatenation gives

\[
\boxed{
W_{AB}
\le3^{Q_B}W_A+2^{L_A}W_B.
}

Consequently every neutral successor satisfies

\[
\frac{2^{L}D-W_V}{3^Q}
\le D'
\le
\frac{2^{L}D+W_V}{3^Q}.
\]

When \(2^L>3^Q\), a uniform available-growth threshold is therefore

\[
D>\frac{W_V}{2^L-3^Q}.
\]

For `U7` the exact threshold is the sharp integer `191`, as certified separately.  For much larger near-resonant blocks the crude recursively propagated width makes this threshold large, so the useful role of the theorem is primarily **totality of the transducer**, while sharper local quotient choices are used for constructive credit growth.

## 7. Proof-program consequence

This theorem removes one possible failure mode from the R2 credit program.  The growing Euclidean recursion does not run out of neutral 3-adic correction matches: the required residue can always be supplied by the certified base-block difference sets.

The remaining hard statement is a coverage statement:

> show that every sufficiently long critical R2 orientation, not merely some alternate orientation in the same survival fibre, must accumulate a predecessor credit exceeding its available orbit headroom.

The present theorem provides the exact arithmetic transport needed for that future statement but does not establish the coverage condition itself.
