# MATH-018 — DSD 18-step tail complete descriptor

Date: 2026-09-08

Status: `CONFIRMED / EXACT FINITE DESCRIPTOR / COMPUTATIONAL ACCELERATION`

Collatz conjecture and the first universal Farey cell remain `OPEN`.

## 1. Motivation

After MATH-017, the next full internal-boundary calculation is depth 79.  The halo generator has already reduced the lower-61 search to finite universal-spine states, but naïvely advancing every state through another 18 shortcut steps for every boundary repeats the same tail computation.

The DSD target is therefore not another heuristic quotient.  It is a complete descriptor for the exact finite map from depth 61 to depth 79.

## 2. Exact descriptor

Let

\[
0\le r<2^{18}.
\]

For the first `j` shortcut steps of `r`, let

\[
s_j(r)
\]

be the number of odd steps, and write

\[
s_{18}(r)=s(r),\qquad t_{18}(r)=T^{18}(r).
\]

Define

\[
\boxed{
H_{18}(r)=
\max_{1\le j\le18}
\bigl(q_{\min}(61+j)-s_j(r)\bigr).
}
\]

The complete depth-61-to-79 descriptor is

\[
\boxed{
G_{18}(r)=
\bigl(H_{18}(r),s_{18}(r),T^{18}(r)\bigr).
}
\]

It simultaneously preserves:

1. the exact coefficient-survival threshold through all intermediate depths 62..79;
2. the final extra odd-count;
3. the exact final endpoint contribution.

## 3. Exact affine tail theorem

Write an arbitrary depth-61 endpoint as

\[
n=h2^{18}+r,
\qquad 0\le r<2^{18}.
\]

The first 18 shortcut parity bits depend only on `n mod 2^18`, hence only on `r`.

Therefore the parity word of `n` and `r` is identical for these 18 steps.  The standard affine shortcut formula then gives

\[
\boxed{
T^{18}(n)=T^{18}(r)+h3^{s_{18}(r)}.
}
\]

Consequently, if the lower-61 prefix has odd-count `q61`, then

\[
\boxed{
q_{79}=q_{61}+s_{18}(r)
}
\]

and

\[
\boxed{
T^{79}(N)=T^{18}(r)+h3^{s_{18}(r)}
}
\]

once the actual depth-61 endpoint has been decomposed as `h*2^18+r`.

Coefficient survival through depths 62..79 is exactly

\[
\boxed{
q_{61}\ge H_{18}(r).
}
\]

Thus one lookup of `G18(r)` replaces an 18-step repeated tail simulation without changing the mathematics.

## 4. Exact finite distribution

All `2^18=262,144` residues were enumerated.

| `H18` | residues |
|---:|---:|
|39|16,936|
|40|42,414|
|41|55,274|
|42|55,882|
|43|44,050|
|44|27,498|
|45|13,384|
|46|5,002|
|47|1,394|
|48|274|
|49|34|
|50|2|

The cumulative number surviving for a base `q61` is therefore:

| `q61` | residues surviving to depth79 |
|---:|---:|
|39|16,936|
|40|59,350|
|41|114,624|
|42|170,506|
|43|214,556|
|44|242,054|
|45|255,438|
|46|260,440|
|47|261,834|
|48|262,108|
|49|262,142|
|50+|262,144|

As expected,

\[
q_{\min}(79)=50.
\]

## 5. Exact regressions

The certificate performs:

- exhaustive construction of `G18` for all `262,144` residues;
- exact survival-gate comparison for every residue and every `q61=39..61`;
- endpoint-affine regression for every residue and deterministic high-part values
  `h = 0,1,2,17,339,1024,1363`;
- parity-word equality check under addition of `h*2^18`.

The finite regression is an implementation certificate.  The affine identity itself follows from the exact parity-residue dependence and shortcut affine formula.

## 6. DSD interpretation

- `D`: the tail state is split into low residue `r` and high affine coordinate `h`.
- `R`: exact resolution `2^18`; no lower-resolution quotient is substituted.
- `S`: `H18` is the complete survival threshold for this finite tail.
- `E`: states failing `q61 >= H18(r)` are rejected before endpoint propagation.
- `T`: endpoint transition is reconstructed exactly from `(s18,T18)`.
- `C`: exhaustive finite regression over all tail residues.
- `N`: `ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.
- `O`: computational acceleration only; no new universal Collatz exclusion by itself.

This is the same design principle as MATH-011, extended from 11 to 18 tail bits while preserving the final endpoint, not just survival.

## 7. Next calculation

Use `G18` inside the depth-79 internal-boundary scan.

The current m=29 halo generator has already produced:

- right local lower-61 states: `964,227`;
- left local lower-61 states: `963,422`.

The next bottleneck is no longer the 18-step tail itself.  After MATH-018 it is the repeated comparison across 339 boundary labels.  The next DSD question is whether the boundary-index dependence admits a safe exact quotient or batched affine evaluation before constructing 339 separate endpoint sets.

## Prohibited upgrades

- `G18` complete for this tail does not mean complete for the full Collatz state.
- finite depth-79 acceleration does not imply arbitrary-depth acceleration.
- tail survival does not imply first-cell survival.
- no collision result may be claimed for depth 79 until all 339 internal boundaries are exhaustively or equivalently covered.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_dsd_tail18_complete_descriptor.py`

Certificate commit:

`37ecd72ad037fc00d6c95c2ee5330cb8f7fa4c0f`
