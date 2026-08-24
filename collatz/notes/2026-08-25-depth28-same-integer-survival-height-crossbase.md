# Exact depth-28 same-integer survival/height cross-base sieve

Date: 2026-08-25

Status: **exact finite cross-base certificate** for the first 28 time bits of the current R1 mechanical phase.  It is not a repeated-window theorem and does not prove Collatz.

## 1. Exact mechanical-relative survival language

The first 28 time bits of the current mechanical reference lie inside the exact initial H19 phase.  Enumerate every binary word `w` satisfying

\[
h_k=q_w(k)-q_{\rm mech}(k)\ge0
\]

at every prefix.  The total language has exactly

\[
\boxed{3,524,586}
\]

words.  By terminal relative height,

\[
\boxed{
(663535,1236935,898798,464889,185684,57923,13953,2520,322,26,1)
}
\]

for `h=0,...,10`.

Each such 28-bit parity word has a unique canonical start residue modulo `2^28`.  Because the first two mechanical bits are `11` and the relative height may not go negative, all surviving words begin with `11`; hence their starts are `3 mod 4` and may be represented by

\[
N=4Y+3,\qquad Y\pmod{2^{26}}.
\]

## 2. Exact ternary selector aggregation at the same address

The selector side is not sampled statistically.  Exact cyclic subset-sum multiplicities modulo `2^26` are computed for the ternary powers `3^i`, then matched to the canonical parity residues above.

For current `m=44`, after subtracting the already closed low-33 selector subblock, the total selector population is

\[
2^{44}-2^{33}=17,583,596,109,824.
\]

The exact number whose first 28 parity bits remain on the coefficient-survival side is

\[
\boxed{923,497,419,313,}
\]

or

\[
\boxed{0.0525203953471747\ldots}.
\]

Thus this one same-integer finite cylinder removes about `94.748%` of the current m44 selector mass.

For the two unresolved `m=45` affine 44-selector blocks, the total population is

\[
2^{45}=35,184,372,088,832,
\]

and the exact depth-28 survival count is

\[
\boxed{1,847,897,870,486,}
\]

or

\[
\boxed{0.0525204163320154\ldots}.
\]

The near equality of the two fractions is an exact negative control: at this finite resolution the recursively-sufficient ternary selector is extremely close to balanced relative to the raw survival language.  No independence claim is inferred.

## 3. Already-open first-defect channels

After applying the previously established first-defect channel closures, retain only

\[
P_{44}=\{2,5,8,10,13,16\},
\qquad
P_{45}=\{2,5,8,10\}.
\]

The exact depth-28 same-integer survivor counts are then

\[
\boxed{923,446,059,910}
\]

for current m44 and

\[
\boxed{1,845,541,690,295}
\]

for the two m45 blocks.

The late channels that were closed previously occupy only a small fraction of the raw depth-28 survival mass, so this channel restriction by itself is not the main contraction.

## 4. Neutral endpoint slice

At terminal relative height zero, the full parity language has exactly

\[
\boxed{663,535}
\]

words.

Requiring simultaneously an unresolved global first-defect channel and the ternary selector gives

\[
\boxed{173,842,387,012}
\]

current-m44 starts, and

\[
\boxed{347,336,064,583}
\]

m45 starts.

Relative to the full selector populations, these are about one percent.

This is the finite slice on which the root-translation ultrametric locking theorem can be attached immediately after the aligned depth-28 neutral endpoint.

## 5. Scope and role

This calculation is deliberately a **same-integer** sieve:

\[
\boxed{
\text{ternary selector address}
\cap
\text{exact dyadic parity address}
\cap
\text{coefficient-survival height}
\cap
\text{first-defect channel}.
}
\]

It does not multiply independent densities and it does not reapply the ternary selector condition to a later normalized state.

The result also shows why a pure sparsity argument is insufficient: the selector mass tracks the raw parity-language fraction very closely at depth 28.  The next global mechanism must therefore use transported same-integer information, such as the ultrametrically locked root translation, rather than a one-window density product.

## 6. Reproducibility

Exact source:

`collatz/src/depth28_selector_survival_height_crossbase_certificate.cpp`

The implementation constructs the full 28-bit survival language recursively, verifies parity-residue injectivity, performs exact cyclic ternary subset-sum aggregation modulo `2^26`, and asserts every count above.
