# H19 height-aware reopening of the G13 parent-credit channel

Date: 2026-08-15

Status: **exact finite diagnostic**.  This note connects the first surviving G13 transition lift to the primitive length-19 defect, then shows by exact enumeration that a dyadic shift blocked in the local neutral fibre reopens with only one unit of accumulated survival height.  The purpose is to identify the minimum state variables required by the next quotient calculation.  It is not a Collatz proof.

## 1. From the first G13 transition lift to the length-19 defect

The survival-conditioned G13 transition theorem leaves its first nonzero CRT layer at

\[
h=5233,
\qquad
F-h=12.
\]

The only positive lift at this first layer is

\[
k=1,
\]

so the exact parent credit is

\[
\boxed{\Delta_{\rm gate}=2^{12}=4096.}
\]

The corresponding local canonical-start displacement is

\[
\boxed{-3^{12}.}
\]

At the base Euclidean resolution `L=19`,

\[
\boxed{3^{12}-2^{19}=7153=23\cdot311.}
\]

Hence

\[
\boxed{-3^{12}\equiv-7153\pmod{2^{19}}.}
\]

Thus the low 19 dyadic bits of the first open G13 lift are governed exactly by the primitive integer defect of the base `(19,12)` resonance.

This is an exact renormalization bridge, not just a numerical similarity.

## 2. Why a scalar neutral-only quotient is insufficient

Consider the length-19 mechanical factor

\[
\boxed{1101101011011010110}
\]

with odd count `q=12`.

For every binary word of length 19 and weight 12, record

- its affine correction `R`;
- its minimum relative prefix height `M` against the mechanical factor;
- its unique correction residue modulo `2^19`.

There are exactly

\[
\binom{19}{12}=50388
\]

such words, and the fixed-`q` correction residues modulo `2^19` are all distinct.

Two particular left credits arising in the locally-neutral reconstruction are

\[
1585,\qquad1586.
\]

The reverse block relation is

\[
\boxed{
\delta_{\rm right}
=\frac{3^{12}\delta_{\rm left}-(R_u-R_w)}{2^{19}}.
}
\]

Therefore the required dyadic correction shift is

\[
R_u-R_w
\equiv3^{12}\delta_{\rm left}\pmod{2^{19}}.
\]

## 3. Exact neutral obstruction

If the incoming accumulated survival height is

\[
H=0,
\]

both words must satisfy

\[
M\ge0.
\]

Exact enumeration gives **zero** admissible pairs for both left credits:

\[
\boxed{
\delta_{\rm left}=1585:\quad0\text{ neutral pairs},
}
\]

\[
\boxed{
\delta_{\rm left}=1586:\quad0\text{ neutral pairs}.
}
\]

Thus the locally-neutral scalar-credit path really does stop at this factor.

## 4. One unit of height reopens both shifts

Now allow one unit of accumulated survival height:

\[
H=1.
\]

A local word is then admissible whenever

\[
M\ge-1.
\]

Exact enumeration finds witnesses immediately.  The minimal required height and resulting right credits are

\[
\boxed{1585\xrightarrow[H_{\min}=1]{}1604,}
\]

\[
\boxed{1586\xrightarrow[H_{\min}=1]{}1603.}
\]

In each witness one word has minimum relative height `0` and the other has minimum relative height `-1`.

Therefore the local-neutral obstruction is not stable under the smallest possible accumulated-height extension.

## 5. Consequence for the quotient state

This rules out the tempting reduction

\[
\text{phase}+\text{integer credit}
\]

as a sufficient state for the G13 parent-credit problem.

At minimum the quotient must retain accumulated survival height or an equivalent state variable:

\[
\boxed{
(\text{phase},H,\Sigma/M,\text{integer-relation state}).
}
\]

The result also explains why the previous scalar recurrent set with maximum credit `397` cannot simply be used to reject the G13 value `4096`: a locally unavailable correction relation can reappear after only one unit of structural headroom.

The next exact calculation should therefore propagate the finite length-19 relation system with height/state labels rather than collapse each block to its neutral fibre.

## Reproducibility

Exact certificate:

`collatz/src/h19_height_credit_reopening_certificate.py`
