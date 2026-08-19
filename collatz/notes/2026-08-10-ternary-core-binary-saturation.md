# Binary saturation of the 40-trit ternary core

Date: 2026-08-10

Status: **EXACT FINITE COMPUTATIONAL CERTIFICATE + NEGATIVE STRUCTURAL RESULT**

This note concerns the most restrictive `m=46`, high-four-trit `1000` branch at the isolated next first-crossing resonance.  It proves no global Collatz statement.  Its role is to determine how much low-2-adic information the remaining ternary digits can already realize.

## 1. Free ternary block

After fixing the certified high-four free trits to `1000`, write

\[
S=\sum_{i=0}^{39} a_i3^i,
\qquad a_i\in\{0,1\}.
\]

The ordinary start has the affine form

\[
\boxed{x=4(C+S)+3}
\]

for one fixed integer `C` determined by the leading ternary digits.

For an integer `B`, define the modular subset-sum support

\[
\mathcal S_B
=\left\{\sum_{i=0}^{39}a_i3^i\pmod{2^B}:a_i\in\{0,1\}\right\}.
\]

## 2. Exact packed-bit computation

A packed-bit dynamic program starts from the singleton residue `0` and, for every weight `3^i mod 2^B`, performs

\[
A\leftarrow A\cup(A+3^i).
\]

The full support was computed exactly for `B<=33`.  At `B=33` the final bitset has no missing bit:

\[
\boxed{\mathcal S_{33}=\mathbb Z/2^{33}\mathbb Z.}
\]

The same verifier therefore also certifies complete support for every smaller modulus `2^B`, `B<=33`.

For reference, independent lower-memory runs already showed full support for `B=30`, and the packed verifier reproduced full support successively for `B=31,32,33`.

This is an exhaustive finite computation, not an asymptotic theorem about powers of three.

## 3. Start-residue consequence

Multiplication by `4` maps residues modulo `2^33` bijectively onto the residue class `0 mod 4` modulo `2^35`.  Translation by the fixed number `4C+3` therefore gives

\[
\boxed{
\{x\pmod{2^{35}}:x\text{ in the `1000` branch}\}
=\{r\pmod{2^{35}}:r\equiv3\pmod4\}.
}
\]

Thus every `35`-bit residue compatible with the compulsory initial `OO` parity prefix is realized by at least one member of this ternary branch.

## 4. Parity-prefix consequence

For the accelerated Collatz map, length-`B` parity prefixes are in bijection with starting residues modulo `2^B`.

Every integer in the recursive-sufficiency branch is `3 mod 4`, so its first two accelerated parity symbols are `OO`.  The residue identity above therefore implies:

\[
\boxed{
\text{every length-35 parity word beginning with `OO` occurs in the `1000` branch.}
}
\]

Consequently no condition depending only on the first `35` parity bits can eliminate this branch.  This includes:

- the coefficient barrier through depth `35`;
- any fixed-depth dangerous-prefix test expressible from those parity bits;
- any start-side pruning based only on a modulus `2^B` with `B<=35`.

## 5. Proof-program consequence

This is a negative result for low-resolution pruning but a useful one.  It shows that the next bridge theorem must genuinely use at least one of:

1. start information above the 35-bit scale;
2. the terminal 3-adic endpoint core;
3. the near-return condition `y-x` being tiny;
4. high-resolution defect/lift coupling across the middle.

In particular, the current isolated resonance cannot be removed by refining only the previously identified small dangerous prefix near the root.  The `1000` ternary branch already realizes all such low binary/parity possibilities.

## 6. Verification scope

The high-memory `B=33` packed run uses about 2 GiB for two bitsets.  Lower `B` values can be checked with substantially less memory.  A repository verifier is supplied separately and accepts `B` and the number of free ternary digits as parameters.

No statement is made here about whether complete support continues modulo `2^34` or higher.