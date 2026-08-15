# Second-return gate transition-band magnitude barrier

Date: 2026-08-15

Status: **exact second-return extension of the transition-band magnitude certificate**.  The first-return enlarged-section theorem is extended to the `G13/G14` neutral and one-slack fibres for every bounded predecessor credit `1<=delta<=397`.  This is a section theorem for an over-family of transition blocks; it does not exclude the full gate fibre and does not prove Collatz.

## 1. Reused enlarged section

For a gate cube

\[
1^F(01/10)^J0,
\]

replace the final `h` forced ones and the first `h` pair coordinates by an arbitrary binary word `B` of length `3h` with exactly `2h` odd symbols:

\[
1^{F-h}B(01/10)^{J-h}0,
\qquad |B|=3h,\quad |B|_1=2h.
\]

No internal survival constraint is imposed on `B`, so this is an over-family of the admissible same-state transition band.

The exact maximum possible boundary correction difference is

\[
\boxed{M_h=(2^h-1)(3^{2h}-4^h).}
\]

After balanced-Hensel lifting the remaining `J-h` pair coordinates, let `T_h(delta)` be the least signed required boundary correction.  Then

\[
\boxed{|T_h(\delta)|>M_h}
\]

is a complete nonexistence certificate for that `(h,delta)` within the enlarged section.

## 2. Regression against the first return

The optimized exact recurrence used here was first run on the four existing first-return cases.  It reproduces the previously certified first widths at which magnitude alone ceases to exclude repair:

\[
150,\ 150,\ 151,\ 152
\]

for `G81-neutral`, `G81-one-slack`, `G82-neutral`, and `G82-one-slack`, respectively.

Thus the second-return calculation uses the same arithmetic criterion and agrees with the earlier certificate before extension.

## 3. Exact second-return results

For every

\[
1\le\delta\le397,
\]

the exact results are

\[
\boxed{\begin{array}{c|c|c|c}
\text{gate/fibre}&(F,J,q)&\text{repair impossible for every }h\le&
\text{first }h\text{ where magnitude alone no longer excludes}\\\hline
G_{13}\text{ neutral}&(5245,7390,12635)&1935&1936\\
G_{13}\text{ one-slack}&(5243,7391,12634)&1936&1937\\
G_{14}\text{ neutral}&(5648,7958,13606)&2084&2085\\
G_{14}\text{ one-slack}&(5646,7959,13605)&2084&2085
\end{array}}
\]

At the first non-excluded width, the minimizing bounded credit is

\[
\boxed{\delta=1}
\]

in all four cases.

The normalized first non-excluded widths are

\[
\boxed{\begin{array}{c|c|c}
\text{gate/fibre}&h_*/F&h_*/q\\\hline
G_{13}\text{ neutral}&0.3691134414&0.1532251682\\
G_{13}\text{ one-slack}&0.3694449743&0.1533164477\\
G_{14}\text{ neutral}&0.3691572238&0.1532412171\\
G_{14}\text{ one-slack}&0.3692879915&0.1532524807
\end{array}}
\]

The concentration of these ratios is a computational structural observation only; no asymptotic constant is claimed here.

## 4. Interpretation

The first-return magnitude theorem excluded arbitrary transition-band rearrangements only through widths around `150`.  At the second Euclidean return the same exact criterion excludes widths around `1935--2084`, tracking the much larger gate scale.

Therefore the low-syndrome failure of the explicit pair cube cannot be repaired, for any bounded credit `1..397`, by merely replacing a small or moderately wide front/pair boundary neighborhood.  Even an unconstrained binary transition band containing thousands of coordinates remains too small in correction magnitude throughout the certified ranges.

The first `h` in the final column is **not** an existence statement.  It means only that the scalar magnitude inequality stops being sufficient there.  A valid same-state repair must still satisfy the full affine word, survival, dyadic canonical-address, ternary Hensel, and ordinary renewal-gap constraints simultaneously.

## 5. Relation to the current R1 obstruction

The current finite mixed-filter audit shows that strong start-only and endpoint-only pruning still projects onto the full low-ternary Cantor coordinate when the two ends are chosen independently.  The missing information is same-word affine/canonical-address consistency.

The present second-return result narrows that bridge problem further.  Within the enlarged transition-section model, a successful same-word repair must use a genuinely large reorganization:

\[
\boxed{h\ge1936\text{ at }G_{13},\qquad h\ge2085\text{ at }G_{14}}
\]

before correction magnitude alone even permits a candidate.

Together with the mixed-place anti-triangular code, this supports treating the remaining object as a renormalized joint-image/kernel problem rather than as another marginal filtering problem.

## 6. Next exact object

The next proof object is the fixed-Hensel same-state joint image

\[
\mathcal G_{J,B}(s)
=\{(\Delta R\bmod3^J,\Delta\rho\bmod2^B):\text{same survival state }s\},
\]

with the transition width retained as part of the state.  The target is to bound the dyadic image of a fixed ternary Hensel fibre across the large transition band, rather than treating the two projections independently.

## Reproducibility

Exact certificate:

`collatz/src/gate_transition_band_magnitude_supergate_certificate.py`
