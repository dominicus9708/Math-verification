# M=5 canonical-residue digit-factor hull obstruction

Date: 2026-08-22

Status: **finite exact negative diagnostic for a tempting Furstenberg-transversality route.** The M=5 parity language has low entropy, but after applying the triangular Collatz parity-to-start-residue map its ordinary binary digit-factor hull rapidly becomes essentially full. This does not prove that every possible invariant-hull construction fails, but it rules out the naive low-dimensional binary factor hull needed for a direct application of standard ×2/×3 intersection theorems.

## 1. Why the route looked promising

The exact M=5 parity-language entropy is

\[
h_5=(2-3\alpha)\log_2 6
\approx0.2771357407,
\qquad
\alpha=\log_3 2\approx0.6309297536.
\]

Thus

\[
\alpha+h_5<1.
\]

For genuinely ×2- and ×3-invariant sets, Furstenberg-type theorems of Wu, Han Yu, and the integer analogue of Glasscock–Moreira–Richter give strong intersection bounds when the dimension sum is below one.

The ternary selector side naturally has dimension \(\alpha\) when measured in dyadic bit scale. If the M=5 **canonical start residue** side admitted a ×2-invariant hull of dimension \(h_5\), these theorems would be extremely close to the desired Stage-4 transversality estimate.

## 2. Coordinate obstruction

The low-entropy object is the parity word \(v\). The same-integer overlap, however, is expressed in the canonical starting residue

\[
r(v)\pmod{2^H},
\]

where

\[
3^{q_H}r(v)+R_v\equiv0\pmod{2^H}.
\]

The parity-to-residue map is the finite form of the Collatz 2-adic conjugacy. It is triangular and an isometry in the 2-adic prefix metric, but it is **not** the ordinary binary shift.

Consequently, entropy with respect to parity prefixes does not automatically control the number of arbitrary contiguous binary digit factors occurring inside the canonical start residues.

## 3. Exact finite factor-hull test

The companion certificate uses 18 consecutive mechanical zero gaps. Scanning mechanical-zero start phases until all distinct gap factors are obtained gives exactly 19 distinct Sturmian gap types, with ordinary lengths 48 or 49.

For each gap type it enumerates every exact M=5 weighted-matching parity word, converts it to its unique canonical starting residue modulo \(2^H\), and collects every contiguous binary factor of length \(n\) in that residue.

Across the complete phase-factor sample the exact counts are:

\[
\begin{array}{c|r|r}
n&\#\text{ distinct residue factors}&2^n\\\hline
1&2&2\\
2&4&4\\
3&8&8\\
4&16&16\\
5&32&32\\
6&64&64\\
7&128&128\\
8&256&256\\
9&512&512\\
10&1024&1024\\
11&2048&2048\\
12&4096&4096\\
13&8192&8192\\
14&16384&16384\\
15&32768&32768\\
16&65525&65536\\
17&129694&131072\\
18&235309&262144
\end{array}
\]

Thus the binary digit-factor hull is already exactly full through length 15 and essentially full at length 16.

Even a **single** mechanical phase factor often fills every factor through length 12 or 13.

This is radically different from the parity-prefix entropy \(h_5\approx0.2771\).

## 4. Consequence

The naive construction

\[
\text{M5 parity language}
\xrightarrow{\Phi}
\text{canonical start residues}
\xrightarrow{\text{all binary digit factors}}
\text{×2-invariant hull}
\]

does not preserve the low dimension needed for a direct Furstenberg theorem.

Finite evidence is already consistent with topological entropy one for this digit-factor hull. We do **not** claim that full entropy has been proved asymptotically, but the route is unusable in its intended low-dimensional form even at modest scales.

This explains why standard ×2/×3 invariant-set transversality cannot simply be imported despite the attractive numerical inequality

\[
\alpha+h_5<1.
\]

The correct low-complexity structure lives in the **parity / T-conjugacy coordinate**, whereas the ternary selector is simple in the **ordinary integer digit coordinate**. The mismatch between these two coordinate systems is precisely the surviving cross-base obstruction.

## 5. What remains potentially useful from Furstenberg theory

The peer-reviewed integer transversality theorem of Glasscock–Moreira–Richter remains conceptually relevant, but applying it would require a new object that is simultaneously

1. structured enough in ordinary binary integer digits to satisfy their ×2-invariance hypotheses, and
2. small enough in dimension to preserve a margin below \(1-\alpha\).

The naive contiguous-factor hull fails requirement 2.

Therefore the active proof front returns to the non-shift-invariant tools already developed internally:

- dyadic Haar martingales on parity-prefix/canonical-cylinder levels;
- exact Hensel query shifts;
- record renewal and post-atomic integer arithmetic.

## References

- M. Wu, *A proof of Furstenberg's conjecture on the intersections of ×p and ×q-invariant sets*, Annals of Mathematics 189 (2019).
- H. Yu, *An improvement on Furstenberg's intersection problem*, accepted/published form associated with arXiv:1811.11073.
- D. Glasscock, J. Moreira, F. K. Richter, *Additive and geometric transversality of fractal sets in the integers*, J. London Math. Soc. 109 (2024), e12902, DOI 10.1112/jlms.12902.

Companion certificate:

`collatz/src/m5_canonical_residue_factor_hull_certificate.py`.
