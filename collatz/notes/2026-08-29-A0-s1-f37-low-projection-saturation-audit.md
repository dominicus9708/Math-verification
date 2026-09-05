# A0 s=1 — f=37 low-projection saturation audit

## Purpose

The previously certified \(f=37\) ordinary-checkpoint sieve is strong only when enough information about the *same ordinary checkpoint* \(Z\) is retained.

This note audits what survives after projecting that sieve to the currently exposed low dyadic checkpoint moduli.

Companion certificate:

- `collatz/src/A0_s1_f37_low_projection_saturation_certificate.py`

## Input

For the \(f=37\) first-defect shell, the allowed checkpoint residue band modulo

\[
3\cdot2^{38}=824,633,720,832
\]

has inclusive length exactly equal to the certified debit-corridor size,

\[
B
=934,928,480,993-669,562,762,561+1
=\boxed{265,365,718,433}.
\]

The allowed band itself is

\[
41,593,248,016
\le
Z\bmod(3\cdot2^{38})
\le
306,958,966,448.
\]

## General interval-projection fact

Any interval of \(B\) consecutive integers projected modulo \(m\) hits every residue whenever

\[
B\ge m.
\]

More precisely, if

\[
B=qm+r,
\qquad0\le r<m,
\]

then every residue appears either \(q\) or \(q+1\) times.

Therefore the question is not whether the full \(f=37\) sieve is nontrivial; it is whether its information survives the projection to the exposed modulus.

## Current 27-bit checkpoint projection

For

\[
m=2^{27}=134,217,728,
\]

one has

\[
B=1977\,m+17,270,177.
\]

Thus

\[
\boxed{
\text{every residue modulo }2^{27}\text{ occurs in the }f=37\text{ allowed band.}
}
\]

Each residue occurs at least \(1977\) times within one band, and exactly \(17,270,177\) residue classes occur once more.

Hence the \(f=37\) arithmetic sieve alone removes **no** possible value of

\[
Z\bmod2^{27}.
\]

This conclusion is independent of the precise semantic interpretation of the currently counted \(8,478,475\) necessary tail-27 words.
Even if those words are later proved to encode checkpoint residues, the \(f=37\) sieve contributes no further rejection at the 27-bit projection level by itself.

## One extra ternary digit is still saturated

For

\[
m=3\cdot2^{27}=402,653,184,
\]

\[
B=659\,m+17,270,177.
\]

Therefore every residue modulo \(3\cdot2^{27}\) also occurs.

So merely adjoining one ternary digit to the 27-bit dyadic exposure does not make the \(f=37\) sieve visible.

## Dyadic visibility threshold

The relevant comparisons are

\[
2^{37}=137,438,953,472
< B
<2^{38}=274,877,906,944.
\]

At depth 37,

\[
B
=1\cdot2^{37}+127,926,764,961,
\]

so every residue modulo \(2^{37}\) still appears at least once.

At depth 38, however,

\[
B<2^{38},
\]

so missing dyadic residue classes become possible for the first time.

Thus

\[
\boxed{
38\text{ bits is the first pure-dyadic resolution at which the }f=37
\text{ checkpoint band can itself prune residues.}
}
\]

This threshold is consistent with the shell modulus \(2^{f+1}=2^{38}\).

## DSD audit classification

### EXACT

- the \(f=37\) allowed-band length is \(265,365,718,433\);
- projection modulo \(2^{27}\) is surjective;
- projection modulo \(3\cdot2^{27}\) is surjective;
- projection remains surjective modulo \(2^{37}\);
- \(2^{38}\) is the first pure dyadic depth at which the contiguous band may leave gaps.

### REJECTED shortcut

Do not intersect the \(f=37\) full-checkpoint sieve with a marginal \(27\)-bit tail address set and claim new rejection from the \(f=37\) arithmetic condition alone.
The projection of the \(f=37\) condition to \(Z\bmod2^{27}\) is the entire residue space.

Likewise, no statistical or density multiplication is licensed by the approximately 67.82% full-checkpoint rejection fraction.
That rejection exists only at sufficiently high coherent checkpoint resolution.

### OPEN

- whether the \(8,478,475\) necessary tail-27 words are, in the relevant certificate chain, already proved to map bijectively/injectively to the checkpoint dyadic address rather than merely satisfying a ballot-prefix requirement;
- coherent generation of
  \((Z\bmod2^{27},Z\bmod3^{28})\)
  by one admissible long correction/tail object;
- full correction-language membership;
- global Collatz coverage.

## Consequence for search design

The next useful operation is not to refine the \(f=37\) sieve at \(27\) dyadic bits.
Instead, either:

1. obtain enough additional *coherent* checkpoint information to reconstruct the ordinary \(Z\), especially the existing \(28\)-trit terminal-correction channel together with the dyadic channel; or
2. expose at least \(38\) coherent dyadic bits from the same long object.

The first option is presently preferable because the existing mixed-radix inequality

\[
2^{27}3^{28}>Z_{\max}-Z_{\min}
\]

already guarantees that a coherent residue pair selects at most one ordinary checkpoint in the certified corridor.
