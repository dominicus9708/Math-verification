# R1 gap44 + depth28 mixed-fibre refinement

Date: 2026-08-14

Status: **exact finite refinement** of the gap44/prefix-Hensel mixed fibre theorem. It repeats the same uniform cyclic-correlation calculation one binary level deeper. The result improves the fixed final-44 suffix bound from `134,265` at depth 27 to `125,165` at depth 28. It also shows that the correlation remains very close to its group mean, so one extra fixed binary level gives a modest rather than dramatic gain. This does not globalize over suffix fibres and does not prove Collatz.

## 1. Exact depth-28 retained set

The depth-28 Hensel retained residue set is built independently by final odd-count slices `q=18,...,28` using

`collatz/src/depth28_hensel_retained_residue_qslice.cpp`.

The exact slice counts are

\[
\boxed{
\begin{array}{c|r|r}
q&\text{coefficient survivors}&\text{Hensel retained}\\\hline
18&663,535&197,622\\
19&1,236,935&681,580\\
20&898,798&572,783\\
21&464,889&324,805\\
22&185,684&139,645\\
23&57,923&46,245\\
24&13,953&11,738\\
25&2,520&2,228\\
26&322&299\\
27&26&26\\
28&1&1
\end{array}
}
\]

Summing gives

\[
\boxed{
3,524,586\text{ coefficient survivors},
\qquad
1,976,972\text{ retained}.
}
\]

All retained residues are `3 mod 4`, so after the affine reduction

\[
x=(N-3)/4
\]

the binary group is

\[
\boxed{\mathbb Z/2^{26}\mathbb Z}.
\]

## 2. Low-21 selector correlation

Let `L_21(x)` be the multiplicity of

\[
\sum_{i=0}^{20}a_i3^i\pmod{2^{26}},
\qquad a_i\in\{0,1\},
\]

and let `A_28(x)` be the indicator of the reduced depth-28 retained set.

For every cyclic shift `h`, define

\[
\boxed{
C_{28}(h)
=
\sum_xL_{21}(x)A_{28}(x+h).
}
\]

The exact NTT certificate

`collatz/src/r1_gap44_depth28_cyclic_correlation_certificate.cpp`

uses the same prime

\[
2013265921=15\cdot2^{27}+1
\]

and a length-`2^26` transform. Since the true count is at most `2^21`, one NTT modulus is exact.

The complete shift range is

\[
\boxed{
60,645
\le
C_{28}(h)
\le
62,985
\qquad
\forall h\pmod{2^{26}}.
}
\]

The exact maximum is

\[
\boxed{62,985}
\]

at shift

\[
\boxed{23,528,858}.
\]

The exact group mean is

\[
\frac{2^{21}\cdot1,976,972}{2^{26}}
=
\frac{1,976,972}{32}
=
\boxed{61,780.375}.
\]

Thus the maximum is less than two percent above the mean.

## 3. Adjacent two-copy gap44 bound

A final-44 gap interval of length `<3^21` can meet at most two low-21 Cantor copies. If two are met, their high-prefix starts differ by exactly `3^21`, whose reduced dyadic shift is

\[
\boxed{
3^{21}\bmod2^{26}
=58,479,283.
}
\]

Therefore the complete-copy overestimate is

\[
C_{28}(h)+C_{28}(h+58,479,283).
\]

The exact all-shift maximum is

\[
\boxed{125,165}
\]

at

\[
\boxed{h=34,750,766}.
\]

Hence every fixed final-44 odd-event suffix address satisfies

\[
\boxed{
\#\{\text{m44 selectors compatible with gap44 + depth28 Hensel}\}
\le125,165.
}
\]

This improves the depth-27 theorem

\[
134,265
\longrightarrow
125,165.
\]

The relative reduction from adding this one binary level is about `6.78%`.

## 4. Strategic interpretation

The important diagnostic is not only that the bound decreases. The one-copy correlations remain very tightly concentrated around the group mean at both depths 27 and 28.

Thus the current fixed-depth Hensel hard-core behaves nearly uniformly across the low-21 ternary Cantor shifts relevant to the gap44 fibre. Increasing the fixed depth by one gives a stable additional contraction, but does not reveal a new exceptional cross-base anti-alignment.

This supports the existing strategic conclusion:

\[
\boxed{
\text{fixed-depth refinement is useful computationally, but the terminal R1 theorem must be growing-scale and nonlocal.}
}
\]

The missing ingredient remains a global constraint coupling the final suffix fibre to the earlier part of the same ordinary integer orbit—most naturally the strengthened dyadic renewal address or a growing skew/defect state.
