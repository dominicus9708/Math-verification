# R1 p=16 reverse-prefix tree through Q=17 and exact hard-mass cross audit

Date: 2026-08-15

Status: **exact finite extension + exact cross-mass diagnostic**. The targeted forward/reverse prefix tree in the unresolved `p=16` first-defect sector is extended from `Q=14` to `Q=17`, then intersected exactly with the full depth-27 Hensel/Cantor hard mass. The result shows continued cylinder birth but almost no special anti-alignment with the dyadic hard sector. It does not close the channel and does not prove Collatz.

## 1. Input hard sector

After the current first-defect and depth-27 Hensel reductions, the `p=16` sector has three low-19 dyadic hard residues

\[
89083,\quad220155,\quad351227
\]

and total current-core Cantor mass

\[
\boxed{116,337,853}.
\]

The three residues had identical low-ternary survivor sets through `Q=14`.

## 2. Exact Q=16 and Q=17 extension

Generate positive reverse exponent codes directly, index them by the required endpoint residue, and retain only the best correction at fixed `(q,z,K)`, exactly as in the `Q=14` certificate.

At `Q=16`, all three dyadic hard residues again have the same survivor set:

\[
\boxed{65,536\to61,324\text{ survivors},\quad4,212\text{ excluded}.}
\]

The excluded fraction is

\[
\boxed{0.0642700195\ldots}.
\]

There are exactly 91 prefix-minimal forbidden cylinders. Their length histogram is

\[
\boxed{6:1,\ 7:3,\ 9:5,\ 11:9,\ 12:36,\ 14:37.}
\]

At `Q=17`, the three hard residues remain synchronized:

\[
\boxed{131,072\to121,360\text{ survivors},\quad9,712\text{ excluded}.}
\]

The excluded fraction is

\[
\boxed{0.0740966796875.}
\]

The survivor growth ratio from `Q=16` is

\[
\boxed{121360/61324\approx1.9790,}
\]

still extremely close to the full binary branching factor two.

The `Q=16` exclusions alone would have produced `8424` excluded descendants at `Q=17`; hence `1288` excluded masks are genuinely new mass born at the next depth.

## 3. Exact cross-mass with the p=16 Cantor hard sector

The low-17 forbidden mask set was intersected with the actual `p=16` depth-27 hard sector without enumerating the full `2^44` selector family.

Use the split

\[
\text{low 17 selectors}\quad+\quad\text{high 27 selector subset-sum multiplicity mod }2^{25},
\]

and the independently certified depth-27 retained bitset. The aggregate first reproduces the known full p=16 hard mass exactly:

\[
\boxed{116,337,853}.
\]

Applying the `Q=17` forbidden low-prefix set removes

\[
\boxed{8,622,321}
\]

actual current-core representatives, leaving

\[
\boxed{107,715,532}.
\]

Thus the true cross-mass exclusion fraction is

\[
\boxed{
\frac{8,622,321}{116,337,853}
\approx0.07411449307.
}
\]

This is almost identical to the raw low-17 mask exclusion fraction.

## 4. Strategic consequence

The reverse-prefix tree is real and persistent: new prefix-minimal cylinders continue to appear at increasing reverse depth. But through `Q=17` its interaction with the p=16 dyadic hard sector is nearly multiplicative rather than strongly anti-aligned.

Therefore increasing this one reverse depth is retained as a useful finite pruning channel, but not as the primary terminal mechanism.

The R1 closure should instead preserve the same-integer mixed-place information: the early first-defect dyadic address, the gate Hensel syndrome/kernel, and the renewal-gap/Cantor address in one state.
