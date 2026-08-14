# Explicit Hensel cubes inside the common 57-bit gate suffix

Date: 2026-08-14

Status: **exact constructive difference-set theorem**. This strengthens the earlier finite residue certificate for the common `G_81/G_82` suffix by giving explicit neutral and one-slack orientation cubes whose correction differences fill whole 3-adic residue groups. It is a local arithmetic freedom result, not a Collatz proof.

## 1. Mechanical suffix

Use the common 57-bit suffix

\[
S=
0101101101011011011\,|
0101101101011011011\,|
0101101101011011010.
\]

It has length `57` and mechanical odd count `35`.

For an actual orientation `v`, relative to `S`, write

\[
\Sigma(v)=\#1(v)-35,
\]

and let `M(v)` be the minimum prefix relative-height displacement.

## 2. Neutral 21-cube

Define a family `C_21^(0)` as follows.

- positions `0,...,13` are fixed to `1`;
- positions `14,...,55` are divided into the 21 adjacent pairs
  \[
  (14,15),(16,17),\ldots,(54,55);
  \]
- in each pair independently choose either `10` or `01`;
- position `56` is fixed to `0`.

Every word in this family has exactly 35 ones.

The prefix-minimal vertex is obtained by taking `01` in every pair:

\[
11111111111111(01)^{21}0.
\]

Direct prefix comparison with `S` gives

\[
\Sigma=0,
\qquad
M=0.
\]

Replacing any selected `01` by `10` moves one odd symbol one step earlier and can only increase the relative prefix height before returning to the same height one step later. Hence every vertex satisfies

\[
\boxed{(\Sigma,M)=(0,0).}
\]

Thus `C_21^(0)` is a `2^21`-vertex cube wholly contained in the neutral survival fibre.

## 3. One-slack 22-cube

Define `C_22^(-1)` by

- positions `0,...,11` fixed to `1`;
- positions `12,...,55` divided into 22 adjacent pairs;
- choose `10` or `01` independently in every pair;
- position `56` fixed to `0`.

Every vertex has 34 ones. The all-`01` vertex is

\[
111111111111(01)^{22}0
\]

and direct prefix comparison gives

\[
\Sigma=-1,
\qquad
M=-1.
\]

Again every `01 -> 10` replacement only raises an intermediate prefix. Since the final displacement remains `-1`, every vertex has

\[
\boxed{(\Sigma,M)=(-1,-1).}
\]

Hence `C_22^(-1)` is a `2^22`-vertex cube wholly contained in the one-slack fibre.

## 4. Triangular correction coordinates

For a length-57 word with odd positions

\[
p_1<\cdots<p_q,
\]

the affine correction is

\[
R=\sum_{k=1}^{q}3^{q-k}2^{p_k}.
\]

Consider one adjacent pair whose unique odd symbol is the `k`-th odd event and whose left position is `p`. Switching

\[
01\longleftrightarrow10
\]

changes only that odd position and gives

\[
\boxed{
\Delta R=\pm 3^{q-k}2^p.
}
\]

Therefore its exact 3-adic valuation is

\[
\boxed{v_3(\Delta R)=q-k.}
\]

### Neutral cube

The 21 variable odd events have ranks `15,...,35`. Their valuations are therefore exactly

\[
20,19,\ldots,0.
\]

### One-slack cube

The 22 variable odd events have ranks `13,...,34`. Their valuations are exactly

\[
21,20,\ldots,0.
\]

In each coordinate the coefficient after removing the displayed power of three is a power of two and therefore a 3-adic unit.

## 5. Full difference-set theorem

Let a cube have coordinates with difference generators

\[
3^r u_r,
\qquad 0\le r<J,
\qquad 3\nmid u_r.
\]

The difference of two vertices uses an independent coefficient

\[
\epsilon_r\in\{-1,0,1\}
\]

on each coordinate. For an arbitrary target modulo `3^J`, choose `epsilon_0` to match the target modulo 3. After subtraction divide by 3 and choose `epsilon_1`; continue inductively. Because

\[
\{-u_r,0,u_r\}\pmod3
\]

is the full set of three residue classes, the induction always succeeds.

Hence

\[
\boxed{
\mathcal C_{21}^{(0)}-
\mathcal C_{21}^{(0)}
\equiv
\mathbb Z/3^{21}\mathbb Z
}
\]

at the correction-difference level, and

\[
\boxed{
\mathcal C_{22}^{(-1)}-
\mathcal C_{22}^{(-1)}
\equiv
\mathbb Z/3^{22}\mathbb Z.
}
\]

Equivalently, every Hensel carry target through 21 ternary digits in the neutral fibre, and through 22 ternary digits in the one-slack fibre, is realized by a pair of admissible orientations.

## 6. Inheritance by `G_81` and `G_82`

Keep the gate prefix preceding the common 57-bit suffix in its mechanical orientation. It contributes relative state `(0,0)`. Concatenation therefore preserves the neutral or one-slack state of the cube.

For any correction difference inside the suffix,

\[
D_{US}=2^{|U|}D_S
\]

because the prefix is identical in the two compared orientations. Since `2^{|U|}` is a unit modulo every power of 3, full difference-set coverage is inherited unchanged.

Thus both first-return gates have the constructive low-order freedom

\[
\boxed{
J=21\text{ in the neutral fibre},
\qquad
J=22\text{ in the one-slack fibre}.
}

This strictly strengthens the earlier computational `J<=12` difference-surjectivity certificate, although it does not claim that the *individual correction residue set* equals all units beyond 12; the proved statement here is the full **difference set**.

## 7. Proof-program consequence

For the current two-ended factorization, no contradiction can depend only on

- the early ordinary dyadic address, and
- at most the first 21 neutral / 22 one-slack 3-adic correction digits,

while allowing a mechanically transported middle.

The late gate boundary already contains an explicit local cube able to solve every such low-order Hensel carry target without changing its survival state.

Therefore the remaining boundary-compatibility obstruction must involve at least one genuinely cross-scale feature:

1. higher Hensel digits beyond this constructive cube;
2. correction ordering / positivity needed for a smaller predecessor;
3. the high dyadic zero-lift fibre of the same ordinary start;
4. the global headroom / renewal-gap condition;
5. the ternary recursively-sufficient start address.

The main structural point is that the first 21--22 ternary digits are not merely empirically flexible: their freedom is generated by an explicit triangular orientation cube.