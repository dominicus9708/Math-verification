# Exact weighted zero-gap entropy for the eventual M=5 record language

Date: 2026-08-22

Status: **exact asymptotic counting reduction for the M=5 bounded-record language.** This strengthens the bounded-record entropy estimate but does not by itself prove the Collatz conjecture or the final selector/Hensel transversality theorem.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil \alpha k\rceil,
\qquad
d_k=b_k-b_{k-1}\in\{0,1\}.
\]

Late record times occur at mechanical zero positions \(d_k=0\). Let the distances between successive mechanical zeros be

\[
g_i\in\{2,3\}.
\]

The M=5 valuation-renewal note proved that a record beginning at one mechanical zero can either

1. take the immediately next zero (a singleton record), or
2. skip exactly one zero, which is possible only over a gap pair \((2,3)\) or \((3,2)\).

The exact non-singleton multiplicities are

\[
(2,3)\mapsto 2,
\qquad
(3,2)\mapsto 3.
\]

Thus the record language is a weighted monomer-dimer tiling of the mechanical-zero path.

## 1. Gap-2 events are isolated

The gap pair \((2,2)\) is impossible. If it occurred, four mechanical positions spanning the corresponding length-five factor would contain only two ones, whereas every length-five factor of the irrational Beatty word has either

\[
\lfloor5\alpha\rfloor=3
\]

or

\[
\lceil5\alpha\rceil=4
\]

ones.

More strongly, the gap pattern

\[
(2,3,2)
\]

is impossible. It would place four mechanical zeros in a span of eight positions, so the corresponding length-eight factor would have only four ones. But every length-eight Beatty factor has

\[
\lfloor8\alpha\rfloor=5
\]

or

\[
\lceil8\alpha\rceil=6
\]

ones.

Therefore any two gap-2 events are separated by at least two gap-3 events.

## 2. Each isolated gap-2 contributes an independent factor 6

Suppose \(g_j=2\). The preceding and following gaps are both 3.

There are exactly three mutually exclusive local possibilities:

- use neither adjacent skip: weight \(1\);
- skip across \((3,2)\): weight \(3\);
- skip across \((2,3)\): weight \(2\).

The two skip choices overlap and cannot both occur. Hence the total local partition factor is

\[
\boxed{1+3+2=6.}
\]

Because distinct gap-2 events are separated by at least one zero-weight dimer edge, these local choices do not interact. Consequently, on every interval whose endpoints are chosen away from the two boundary clusters, the weighted record count factors exactly as

\[
6^{N_2},
\]

where \(N_2\) is the number of interior gap-2 events. Arbitrary finite endpoints change the count only by a multiplicative constant independent of the interval length.

Thus

\[
\boxed{
\log_2 |\mathcal L_5(H)|
=N_2(H)\log_2 6+O(1).
}
\]

## 3. Exact asymptotic density of gap-2 events

Among the first \(H\) mechanical steps, the number of zeros is

\[
H-b_H=(1-\alpha)H+O(1).
\]

Let \(N_2(H)\) and \(N_3(H)\) count complete zero gaps of lengths 2 and 3. Then

\[
N_2+N_3=(1-\alpha)H+O(1)
\]

and the total span gives

\[
2N_2+3N_3=H+O(1).
\]

Eliminating \(N_3\) yields

\[
\boxed{
N_2(H)=(2-3\alpha)H+O(1).
}
\]

Since \(\alpha\approx0.6309297535714574\),

\[
2-3\alpha\approx0.1072107392856278>0.
\]

## 4. Exact M=5 entropy

Combining the preceding identities,

\[
\boxed{
|\mathcal L_5(H)|
=2^{h_5H+O(1)},
}
\]

with

\[
\boxed{
h_5=(2-3\alpha)\log_2 6.}
\]

Numerically,

\[
\boxed{h_5\approx0.2771357407279399.}
\]

This is much smaller than the crude endpoint-density entropy bound

\[
H_2(\alpha+1/5),
\]

because the actual M=5 language is not an arbitrary high-odd-density language: it is a weighted matching language locked to the Sturmian zero-gap geometry.

## 5. Dimension margin at the natural selector scale

The reduced ternary selector has \(2^m\) points at magnitude \(3^m\). At the natural dyadic bit scale

\[
H\sim m\log_2 3={m\over\alpha},
\]

the selector exponent relative to \(H\) is \(\alpha\).

The M=5 record language exponent is \(h_5\). Their entropy sum is

\[
\boxed{
\alpha+h_5
\approx0.9080654942993973<1.
}
\]

Hence there is a strict ambient entropy margin

\[
\boxed{
\delta_5:=1-\alpha-h_5
\approx0.0919345057006027.
}
\]

This does **not** by itself imply disjointness: the ternary selector and the Collatz parity-residue language are arithmetically correlated through the triangular parity-to-residue map. What it does mean is that the final M=5 cross-base theorem no longer needs a subexponential-overlap estimate as strong as the unrestricted coefficient-only Stage 4 target. Any rigorous same-integer overlap amplification rate strictly below \(\delta_5\) per dyadic bit would suffice at the natural bit scale.

## 6. Revised M=5 target

The first unresolved bounded branch can therefore be attacked with two simultaneous resources:

1. the exact valuation renewal from the M=5 macro classification;
2. the exact entropy margin
   \[
   \delta_5=1-\alpha-(2-3\alpha)\log_2 6>0.
   \]

The next useful theorem is:

> **M=5 selector/renewal transversality.** Bound the normalized overlap between the reduced ternary selector and the M=5 weighted matching parity-residue language by an exponential rate strictly smaller than \(\delta_5\), or derive a direct deterministic contradiction from the valuation-renewal arithmetic.

Companion finite regression:

`collatz/src/m5_weighted_zero_gap_entropy_certificate.py`.
