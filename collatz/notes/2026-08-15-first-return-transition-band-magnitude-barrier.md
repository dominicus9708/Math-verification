# First-return gate transition-band magnitude barrier

Date: 2026-08-15

Status: **exact enlarged-section exclusion for all bounded credits `1..397` in the four first-return gate fibres**.  It allows an arbitrary combinatorial rearrangement of a wide front/pair transition band and proves that the required Hensel-syndrome repair is still too large to be generated.  It is stronger than the original explicit-cube audit but remains a section theorem rather than a full-gate-fibre theorem.  It does not prove Collatz.

## 1. Enlarging the explicit cube

Start from a first-return cube

\[
1^F(01/10)^J0.
\]

For an integer `h>=1`, replace the last `h` forced ones together with the first `h` pair coordinates by an arbitrary word `B` of length `3h` and odd count `2h`:

\[
\boxed{
1^{F-h}\,B\,(01/10)^{J-h}0,
\qquad |B|=3h,\quad |B|_1=2h.
}
\]

No survival constraint is imposed on `B` in the certificate.  Therefore this is an **over-family** of the admissible same-state transition band: proving nonexistence here is automatically safe for the actual admissible subset.

Put

\[
n:=J-h.
\]

After removing the common dyadic factor from the fixed front, the full correction-difference equation for incoming credit `delta` is

\[
3^n\Delta R_B+2^{3h}\Delta R_V
\equiv
-2^{2J+h+1}\delta
\pmod{3^{F+J}},
\]

where `V` is the remaining `n`-pair cube.

Dividing by the unit `2^{3h}` gives

\[
\boxed{
\Delta R_V
+3^n2^{-3h}\Delta R_B
\equiv
-2^{2n+1}\delta
\pmod{3^{F+J}}.
}
\]

Thus the remaining pair cube sees exactly the same normalized target form as a cube of dimension `n`.

## 2. Pair lifting and required boundary difference

Use the balanced-Hensel recurrence of the companion syndrome theorem for the low `n` pair coordinates.  After `n` lifts let the residual be `U_n`, now living modulo

\[
3^{F+h}.
\]

The identity

\[
T-\Delta R_V=3^nU_n/4
\]

shows that full repair by the boundary block requires

\[
\boxed{
\Delta R_B
\equiv
2^{3h-2}U_n
\pmod{3^{F+h}}.
}
\]

Let `T_h(delta)` be the least signed representative of the right side.

## 3. Exact maximum boundary correction range

Among all binary words of length `3h` with exactly `2h` odd symbols, moving an odd symbol one time step to the right by an adjacent `10->01` exchange strictly increases the affine correction.

Therefore the minimum and maximum corrections occur at

\[
1^{2h}0^h
\qquad\text{and}\qquad
0^h1^{2h},
\]

respectively.

The geometric correction sums are

\[
R_{\min}=3^{2h}-4^h,
\]

\[
R_{\max}=2^h(3^{2h}-4^h).
\]

Hence every possible boundary difference satisfies the **exact** bound

\[
\boxed{
|\Delta R_B|
\le
M_h:=(2^h-1)(3^{2h}-4^h).
}
\]

Consequently

\[
\boxed{|T_h(\delta)|>M_h}
\]

is a complete nonexistence certificate for that `(h,delta)`, even after all `binom(3h,h)` boundary arrangements are over-allowed.

## 4. Exact first-return results

Audit every

\[
1\le\delta\le397.
\]

The exact magnitude barrier gives

\[
\boxed{\begin{array}{c|c|c}
\text{gate/fibre}&\text{repair impossible for every }h\le&
\text{first }h\text{ where magnitude alone no longer excludes}\\\hline
G_{81}\text{ neutral}&149&150\\
G_{81}\text{ one-slack}&149&150\\
G_{82}\text{ neutral}&150&151\\
G_{82}\text{ one-slack}&151&152
\end{array}}
\]

The statement in the last column is **not** an existence claim.  It only means that the scalar magnitude test ceases to be sufficient at that width.

For comparison, direct exhaustive boundary enumeration had already verified zero lifts for every `h<=7` in all four fibres, including all

\[
\binom{21}{7}=116,280
\]

possible `h=7` boundary words.  The magnitude theorem extends the exclusion from seven transition coordinates to roughly one hundred and fifty without enumerating the enormous boundary family.

## 5. Relation to early-defect / late-repair forcing

The current isolated R1 branch has its first Christoffel defect by odd rank twelve.  The systematic cube theorem had already shown that this very early contribution cannot alter the first failed high-syndrome trit.

The present theorem is stronger in a different direction: even if the transition between the front-loaded syndrome sector and the systematic pair sector is allowed to rearrange arbitrarily over a width approaching `150`, no bounded credit in `1..397` can be fully lifted in the four first-return enlarged sections.

Thus the missing full-fibre repair, if it exists, cannot be a tiny local modification of the explicit cube boundary.  It must use a substantially more global reorganization of the gate orientation.

## 6. Strategic consequence

The unresolved gate freedom has now been pushed away from two easy explanations:

1. it cannot be supplied by the certified early first defect itself;
2. it cannot be supplied by any arbitrary front/pair boundary rearrangement of width up to roughly `150`.

The next full-fibre kernel theorem should therefore work at a genuinely renormalized scale.  A natural object is the minimal transition width

\[
h_*(\delta)
:=
\min\{h:\text{a same-state full-fibre repair of credit }\delta\text{ is possible}\},
\]

or a lower bound on it derived from the Euclidean gate state rather than from the explicit cube section.

The current theorem supplies the first exact nontrivial lower bound on this width for the over-family above.

## Reproducibility

Exact certificate:

`collatz/src/gate_transition_band_magnitude_certificate.py`
