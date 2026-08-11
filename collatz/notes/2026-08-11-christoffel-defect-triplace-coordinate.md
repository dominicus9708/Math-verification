# Christoffel defect as a tri-place coordinate

Date: 2026-08-11

Status: **exact mixed-place identity for the primitive upper-CF renewal branch**. The same normalized Christoffel correction defect controls the Archimedean rational shadow, the 2-adic formation residue, and the modular renewal-gap residue.

## 1. Setup

Fix primitive upper-CF aggregate data `(A,H)` and put

\[
P:=\frac{2^A}{3^H}>1,
\qquad
Z:=2^A-3^H=3^H(P-1).
\]

Let the ceiling Christoffel word at `(A,H)` have correction numerator

\[
R_{\rm chr},
\]

formation residue including endpoint oddness

\[
\rho_{\rm chr}\pmod{2^{A+1}},
\]

and gap residue

\[
 g_{\rm chr}:=R_{\rm chr}(2^A)^{-1}\pmod Z.
\]

Let a residual primitive-CF renewal word be parameterized by its exact left-displacement staircase `s`, with correction defect

\[
\mathcal E(s):=R_{\rm chr}-R(s)>0.
\]

Define the normalized defect coordinate

\[
\boxed{
\eta(s):=\frac{\mathcal E(s)}{3^H}.
}
\]

Its denominator is odd, so the same rational number is a well-defined real number and a 2-adic integer/rational unit combination.

## 2. Exact displacement formula

For Christoffel positions `i_k^{chr}` and displacement coordinates `s_k`, the actual one positions are

\[
i_k=i_k^{\rm chr}-s_k.
\]

The exact defect identity gives

\[
\mathcal E(s)
=
\sum_{k:s_k>0}
3^{H-k}2^{i_k^{\rm chr}-1}(1-2^{-s_k}).
\]

Therefore

\[
\boxed{
\eta(s)
=
\sum_{k:s_k>0}
2^{i_k^{\rm chr}-1}3^{-k}(1-2^{-s_k}).
}
\]

This is the basic mixed-place coordinate.

## 3. Archimedean action: shadow lowering

The Christoffel and actual rational fixed-point shadows are

\[
C_{\rm chr}=\frac{R_{\rm chr}}Z,
\qquad
C_s=\frac{R_{\rm chr}-\mathcal E(s)}Z.
\]

Since

\[
Z=3^H(P-1),
\]

we obtain

\[
\boxed{
C_s
=C_{\rm chr}
-
\frac{\eta(s)}{P-1}.
}
\]

Thus positive displacement defect lowers the available real renewal shadow by exactly `eta/(P-1)`.

## 4. 2-adic action: formation-address shift

For a length-`A` word with `H` ones and endpoint oddness included, the exact starting residue may be written in 2-adic form as

\[
\rho(w)
\equiv
-
\sum_{k=1}^{H}2^{i_k-1}3^{-k}
-
2^A3^{-(H+1)}
\pmod{2^{A+1}}.
\]

The endpoint term is the same for the Christoffel and displaced words. Subtracting the two residue formulas gives

\[
\begin{aligned}
\rho_s-\rho_{\rm chr}
&\equiv
\sum_{k=1}^{H}
(2^{i_k^{\rm chr}-1}-2^{i_k-1})3^{-k}\\
&=
\eta(s)
\pmod{2^{A+1}}.
\end{aligned}
\]

Hence

\[
\boxed{
\rho_s
\equiv
\rho_{\rm chr}+\eta(s)
\pmod{2^{A+1}}.
}
\]

The same real defect coordinate is therefore exactly the 2-adic formation-address displacement.

## 5. Modular gap action: opposite shift

The gap-channel residue is

\[
g_s
\equiv
R(s)(2^A)^{-1}
\pmod Z.
\]

Since

\[
R(s)=R_{\rm chr}-\mathcal E(s),
\]

we have

\[
g_s
\equiv
g_{\rm chr}-\mathcal E(s)(2^A)^{-1}
\pmod Z.
\]

But

\[
2^A\equiv3^H\pmod Z,
\]

so their inverses agree modulo the odd modulus `Z`. Thus

\[
\boxed{
 g_s
\equiv
 g_{\rm chr}-\eta(s)
\pmod Z.
}
\]

Therefore the formation address and gap address move in opposite directions under the same normalized defect.

## 6. Earliest-defect valuation

Let `k_*` be the first displaced one in actual position order:

\[
k_*:=\min\{k:s_k>0\}.
\]

In the integer defect sum

\[
\mathcal E(s)
=
\sum_{k:s_k>0}
3^{H-k}2^{i_k-1}(2^{s_k}-1),
\]

the term with `k_*` has the unique smallest power of two because actual one positions are strictly increasing. Its odd factor `2^{s_k}-1` cannot cancel.

Hence

\[
\boxed{
v_2(\mathcal E(s))=i_{k_*}-1.}
\]

Since `3^H` is odd,

\[
\boxed{
v_2(\eta(s))=i_{k_*}-1.}
\]

Consequently the Christoffel and actual formation residues agree through exactly the bits before the earliest displaced one and differ at the next bit:

\[
\rho_s\equiv\rho_{\rm chr}\pmod{2^{i_{k_*}-1}},
\]

but not modulo `2^{i_{k_*}}`.

This is the precise 2-adic meaning of the first combinatorial defect.

## 7. Tri-place residual conditions

A sufficiently large primitive-CF renewal candidate with nonzero `s` must use one rational coordinate `eta(s)` to satisfy all three requirements simultaneously:

### Real

\[
0<\eta(s)
<
(P-1)\left(C_{\rm chr}-N-\frac{P}{P-1}g\right).
\]

### 2-adic formation

\[
\boxed{
\rho_s
\equiv\rho_{\rm chr}+\eta(s)
\pmod{2^{A+1}}.
}
\]

### Renewal gap

\[
\boxed{
 g_s
\equiv g_{\rm chr}-\eta(s)
\pmod Z,
\qquad
 g_s\in4\mathbb Z\cap(0,H/3).
}
\]

Thus the remaining primitive-CF branch is no longer three unrelated filters. It is one **tri-place defect compatibility problem**.

## 8. Next target

A complete primitive-CF exclusion theorem may now be phrased as:

> prove that no nonzero admissible displacement coordinate `eta(s)` can simultaneously lower the real Christoffel shadow enough to admit a positive integer renewal start, shift the 2-adic formation residue to that start, and shift the `Z`-gap residue into `4Z intersect (0,H/3)` for all sufficiently large upper convergents.

The zero coordinate is the exact Christoffel branch, already reduced to a finite initial audit.

This tri-place formulation is the most compact exact form currently available for the residual primitive-CF supercritical renewal sector.
