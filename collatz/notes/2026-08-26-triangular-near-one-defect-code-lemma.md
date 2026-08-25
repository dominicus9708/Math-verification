# Triangular near-one defect code and direct Beatty-boundary assembly

Date: 2026-08-26

Status: **exact dyadic defect-code lemma + positive exponential frequency-average bound for the unconditioned Beatty boundary and any conditioning that preserves the late full plateau fibres.**  This removes the previously open triangular-product assembly obstacle at the pure Beatty-boundary level.  It does **not** by itself prove the uniform recurrent Stage-4 theorem, because an additional renewal/Hensel/dynamical conditioning may split the plateau fibres.  It is not a proof of the Collatz conjecture.

## 1. Setup on one deterministic plateau fibre

Let

\[
\alpha=\log_3 2,
\qquad
b_j=\lceil \alpha j\rceil,
\]

and let a Beatty-boundary plateau fibre have mixed-pair starts

\[
j_1<j_2<\cdots<j_n.
\]

For coordinate `i`, put

\[
m_i=L+1-j_i
\]

for the remaining dyadic resolution and let \(\ell_i\) be the one-ordinal in that mixed pair.  The exact cube factor is

\[
\left|
\cos\!\left(
\pi k\frac{[3^{-\ell_i}]_{2^{m_i}}}{2^{m_i}}
\right)
\right|.
\]

Only \(k\bmod 2^{m_i}\) matters at coordinate `i`.

For adjacent mixed coordinates define

\[
d_i:=j_{i+1}-j_i=m_i-m_{i+1},
\qquad
s_i:=\ell_{i+1}-\ell_i.
\]

Because \(s_i\) counts ones across an interval of length \(d_i\),

\[
\boxed{1\le s_i\le d_i.}
\]

## 2. Exact dyadic phase transport

Set

\[
a_i=[3^{-\ell_i}]_{2^{m_i}}
\]

and let

\[
r_i\equiv k a_i\pmod{2^{m_i}}.
\]

Choose the centered representative

\[
c_i\in(-2^{m_i-1},2^{m_i-1}]
\]

of \(r_i\).

Since

\[
a_i\equiv 3^{s_i}a_{i+1}\pmod{2^{m_{i+1}}},
\]

we have exactly

\[
r_i\equiv3^{s_i}r_{i+1}\pmod{2^{m_{i+1}}}.
\]

Therefore there is an integer defect \(z_i\) such that

\[
\boxed{
c_i=3^{s_i}c_{i+1}+z_i2^{m_{i+1}}.}
\]

This is the triangular boundary phase written as a mixed-radix defect code.

## 3. Two near-one endpoints force zero defect

Call coordinate `i` \(\delta\)-near if

\[
|c_i|\le\delta2^{m_i}.
\]

This implies that the corresponding cosine factor is at least \(\cos(\pi\delta)\).

If adjacent coordinates are both \(\delta\)-near, then the exact defect identity gives

\[
|z_i|
\le
\delta\left(2^{d_i}+3^{s_i}\right).
\]

Hence whenever

\[
\delta\left(2^{d_i}+3^{s_i}\right)<1,
\]

integrality forces

\[
\boxed{z_i=0}
\]

and therefore the congruence upgrades to the exact integer relation

\[
\boxed{c_i=3^{s_i}c_{i+1}.}
\]

For the explicit short-edge cutoff

\[
\boxed{d_i\le10}
\]

use

\[
\boxed{
\delta:=\frac1{60074}
<\frac1{2^{10}+3^{10}}
=\frac1{60073}.
}
\]

Since \(s_i\le d_i\), every short edge with two near endpoints has zero defect.

This is the direct dyadic counterpart of the earlier ternary near-one congruence picture.  No statistical independence and no external Cantor Fourier theorem is used.

## 4. Zero defect fixes the newly exposed Fourier bits

Fix the lower-resolution frequency

\[
k_{i+1}:=k\bmod2^{m_{i+1}}.
\]

There are exactly

\[
2^{d_i}
\]

lifts to \(k_i=k\bmod2^{m_i}\), obtained by choosing the newly exposed \(d_i\)-bit chunk.

Multiplication by the odd unit \(a_i\) is a bijection modulo \(2^{m_i}\).  The condition

\[
c_i=3^{s_i}c_{i+1}
\]

specifies at most one of the \(2^{d_i}\) possible lifted centered residues.  Therefore

\[
\boxed{
\text{a zero-defect edge fixes at most one new }d_i\text{-bit chunk.}
}
\]

Equivalently, compared with an unconstrained edge, it removes at least \(d_i\) bits of frequency freedom.

Every adjacent mixed plateau start has \(d_i\ge2\), so every short zero-defect edge saves at least two bits.

## 5. Linear supply of short edges in a typical fibre

The deterministic plateau-pair cube theorem already proves that, apart from an exponentially small fraction of Beatty-boundary words, a fibre has at least

\[
\boxed{n\ge L/10}
\]

mixed coordinates.

The adjacent gaps satisfy

\[
\sum_{i=1}^{n-1}d_i=j_n-j_1<L.
\]

Call an edge long if \(d_i\ge11\).  There can be at most \(L/11\) such edges.  Using \(L\le10n\), the number of short edges is therefore at least

\[
(n-1)-\frac{L}{11}
\ge
\boxed{\frac n{11}-1}.
\]

Thus no spatial equidistribution of the mixed coordinates is needed.  Linear cardinality alone forces a positive linear number of gaps of length at most ten.

## 6. Large Riesz product implies a sparse defect code

Let a mixed coordinate be `far` when it is not \(\delta\)-near.  Put

\[
\kappa:=\cos\frac{\pi}{60074}<1.
\]

If more than \(n/100\) mixed coordinates are far, then the normalized fibre product obeys immediately

\[
\boxed{
P_F(k)
\le
\kappa^{n/100}.
}
\]

Now suppose at most \(n/100\) coordinates are far.  A far vertex can spoil at most two short edges, so at least

\[
\frac n{11}-1-\frac{2n}{100}
=
\boxed{\frac{39}{550}n-1}
\]

short edges have two near endpoints and hence zero defect.

Each fixes at least two Fourier bits.  Therefore, after a particular far-vertex set is specified, the number of compatible frequencies is reduced by at least

\[
\boxed{\frac{39}{275}n-2}
\]

bits.

There are only

\[
\sum_{b\le n/100}\binom nb
=2^{H_2(0.01)n+o(n)}
\]

possible far sets, and

\[
H_2(0.01)
=0.0807931358\ldots<0.081.
\]

Consequently the fraction of frequencies having at most \(n/100\) far coordinates is at most

\[
\boxed{
2^{-\left(\frac{39}{275}-H_2(0.01)\right)n+o(n)}
}
\]

with

\[
\boxed{
\frac{39}{275}-H_2(0.01)
=0.0610250459\ldots>0.060.
}
\]

Thus the frequency set on which almost every triangular factor is near one is itself exponentially sparse.

## 7. Direct triangular-product average bound

Split frequencies into the two classes of Section 6.  Since every product is at most one,

\[
2^{-m_1}
\sum_{k\bmod2^{m_1}}P_F(k)
\le
\kappa^{n/100}
+
2^{-0.060n+o(n)}.
\]

Equivalently, with

\[
\eta_{\rm mix}
:=
-\frac1{100}\log_2\!\left(\cos\frac{\pi}{60074}\right)
>0,
\]

we obtain

\[
\boxed{
2^{-m_1}
\sum_kP_F(k)
\le
2^{-\eta_{\rm mix}n+o(n)}.
}
\]

Numerically,

\[
-\log_2\!\left(\cos\frac{\pi}{60074}\right)
\approx1.97274608\times10^{-9},
\]

so

\[
\eta_{\rm mix}
\approx1.97274608\times10^{-11}.
\]

The constant is intentionally crude; only strict positivity matters here.

Since a typical Beatty fibre has \(n\ge L/10\), its frequency-average product has the explicit rate

\[
\boxed{
\eta_{\rm tri}
:=
-\frac1{1000}\log_2\!\left(\cos\frac{\pi}{60074}\right)
\approx1.97274608\times10^{-12}
}
\]

per boundary step.

The earlier deterministic cube theorem gives an exponentially small exceptional boundary-word fraction for fibres with fewer than \(0.10L\) mixed coordinates (the recorded Chernoff binary rate is about \(0.0425L\)).  Averaging the fibre transforms and using the triangle inequality therefore yields a **positive exponential normalized L1 Fourier decay for the unconditioned Beatty boundary**.

Thus the previously open implication

\[
\text{triangular Beatty product}
\Longrightarrow
\text{positive average spectral decay}
\]

is closed at the pure Beatty-boundary level by a direct dyadic defect-code argument.  The complete inverse-Cantor-product theorem is no longer needed for this particular assembly step.

## 8. Compatibility with a fixed root-globalized low-bit lock

The exact adjacent-swap formula is

\[
r(\cdots01\cdots)-r(\cdots10\cdots)
\equiv-2^j3^{-\ell}\pmod{2^H}.
\]

Its dyadic valuation is exactly \(j\).  Hence any conditioning that depends only on the canonical start modulo \(2^P\) is unchanged by every plateau swap with

\[
\boxed{j\ge P.}
\]

Therefore a fixed finite root-globalized translation label does **not** destroy the late plateau cubes.  It can remove only finitely many early swap coordinates, which does not change the asymptotic positive-density or exponential-rate conclusion.

This is important for the ultrametric-locking route: the permanent low-bit root label is compatible with the present triangular assembly once the excursion is sufficiently far beyond the locked resolution.

## 9. What remains open

This note does not yet assert the full recurrent Stage-4 theorem.

The remaining scope question is now narrower:

> Does every globally admissible late renewal/height/Hensel boundary class preserve a positive linear subfamily of the full plateau-pair fibres to which the defect-code argument applies?

If the answer is yes, then for a normalized selector transform \(|\widehat C(k)|\le1\), the odd-shell correlation is bounded by the boundary L1 norm,

\[
\frac1M
\left|
\sum_{k\ \mathrm{odd}}
\widehat C(k)G_L(k)
\right|
\le
\frac1M
\sum_{k\ \mathrm{odd}}|G_L(k)|,
\]

and the present exponential boundary bound makes the fresh cross-base repair exponentially small.  This would be much stronger than the subcritical positive repair rate required by Stage 4.

However arbitrary later-block L7/Hensel maximality was withdrawn by the 2026-08-25 scope audit, so one may not simply assume that every old recurrent class is a union of these fibres.  The next audit must identify exactly which **root-safe** conditioning survives in the long open-positive excursion and verify fibre invariance for that conditioning.

Accordingly the terminal target has moved from an analytic triangular-product estimate to a much more concrete invariance statement:

\[
\boxed{
\text{root-safe recurrent conditioning}
\quad\Longrightarrow\quad
\text{positive-density late full plateau fibres}.
}
\]

## 10. Regression certificate

Portable verifier:

`collatz/src/triangular_near_one_defect_code_regression.py`

It checks exact phase transport on `454,608` finite states and zero-defect lift uniqueness on `63,216` finite lower states, in addition to the explicit threshold and counting constants.  The finite loops are implementation regressions; Sections 2--7 are algebraic/combinatorial proofs.
