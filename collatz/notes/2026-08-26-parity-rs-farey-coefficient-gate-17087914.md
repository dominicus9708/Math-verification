# Farey extension of the global parity-RS coefficient gate to depth 17,087,914

Date: 2026-08-26

Status: exact finite theorem after taking Barina's published verification below \(2^{71}\) as an external finite input. This corrects the earlier artificial stopping point at depth 301,993. It is not a proof of the Collatz conjecture.

## 1. Starting parity-RS wall

The parity recursive-sufficiency theorem established in

`2026-08-26-parity-rs-global-coefficient-gate.md`

uses

\[
B=2^{71},\qquad p=190537,\qquad q=301994,
\]

with the exact adjusted-multiplier inequality

\[
(3B+1)^p<2^qB^p.
\]

Therefore every hypothetical minimal Collatz counterexample must satisfy, at **every** finite depth \(j\),

\[
\boxed{q\,Q_j>p\,j,}
\]

where \(Q_j\) denotes the number of odd shortcut steps among the first \(j\) steps.

The earlier depth 301,993 was only the range directly checked against the coefficient wall. It was not the range of validity of the RS wall itself.

## 2. Farey neighbours around the critical slope

Let

\[
\alpha:=\log_3 2.
\]

Exact integer-power comparisons give

\[
3^{190537}<2^{301994},
\]
so

\[
\frac{190537}{301994}<\alpha,
\]

and

\[
3^{10590737}>2^{16785921},
\]
so

\[
\alpha<\frac{10590737}{16785921}.
\]

Moreover

\[
10590737\cdot301994-190537\cdot16785921=1.
\]

Thus

\[
\boxed{
\frac{190537}{301994}
<\alpha<
\frac{10590737}{16785921}
}
\]

is trapped between two Farey neighbours.

A standard determinant argument then says that every rational number strictly between these two fractions has denominator at least the sum of their denominators:

\[
301994+16785921
=\boxed{17087915}.
\]

## 3. Exact Beatty-floor coincidence

Suppose for some positive integer \(j<17087915\) that

\[
\left\lfloor\frac{190537j}{301994}\right\rfloor
<
\lfloor\alpha j\rfloor.
\]

Then the integer

\[
n=\left\lfloor\frac{190537j}{301994}\right\rfloor+1
\]

would satisfy

\[
\frac{190537}{301994}<\frac nj<\alpha.
\]

But \(n/j\) would lie strictly between the Farey neighbours with denominator smaller than \(17087915\), impossible.

Hence

\[
\boxed{
\left\lfloor\frac{190537j}{301994}\right\rfloor
=\lfloor j\log_3 2\rfloor
\qquad
(1\le j\le17087914).
}
\]

## 4. Transfer to coefficient survival

The RS wall

\[
301994\,Q_j>190537\,j
\]

is equivalent to

\[
Q_j\ge
\left\lfloor\frac{190537j}{301994}\right\rfloor+1.
\]

By the floor identity above,

\[
Q_j\ge\lfloor\alpha j\rfloor+1
=\lceil\alpha j\rceil.
\]

Therefore

\[
3^{Q_j}\ge2^j.
\]

We obtain the corrected global finite gate:

\[
\boxed{
3^{Q_j}\ge2^j
\quad\text{for every }1\le j\le17,087,914
}
\]

for every hypothetical minimal counterexample, conditional only on the published finite verification below \(2^{71}\).

This is about \(56.58\) times deeper than the previous 301,993-step certificate.

## 5. Sharpness of this particular rational-wall transfer

The Farey mediant is

\[
\frac{190537+10590737}{301994+16785921}
=
\frac{10781274}{17087915}.
\]

Exact comparison gives

\[
3^{10781274}<2^{17087915},
\]
so the mediant is still below \(\alpha\).

Also

\[
10781274\cdot301994-190537\cdot17087915=1.
\]

Consequently at \(j=17087915\),

\[
\left\lfloor\frac{190537j}{301994}\right\rfloor
=10781273,
\]
while

\[
\lfloor\alpha j\rfloor=10781274.
\]

Thus depth \(17087915\) is the **first** depth where this specific RS rational wall alone no longer forces the exact coefficient-survival wall.

This is a sharp transfer threshold for \(190537/301994\), not a barrier of the parity-RS method itself. A closer valid lower rational slope can extend the gate again.

## 6. DSD logical-chain audit

The repaired chain now reads

\[
\text{published finite base }(2^{71})
\to
\text{global parity-RS wall valid at all finite depths}
\to
\text{Farey/Beatty coincidence}
\to
\text{exact coefficient survival through }17,087,914.
\]

Every arrow remains in the binary parity-prefix domain. No ternary selector, no local L7/L14 pullback, and no cross-base same-address hypothesis occurs.

## 7. Consequence for the next proof stage

The relevant global finite horizon is no longer 301,993 but

\[
\boxed{H_*=17,087,914.}
\]

Within this entire horizon, a minimal counterexample must remain in the coefficient-surviving parity language. Since the survivor-Hensel root-credit lemma gives

\[
0<d<\frac{Q_H}{3}\le\frac H3,
\]

and \(H_*\ll3\cdot2^{71}\), every same-\(Q_H\) coefficient-surviving Hensel sibling credit is automatically smaller than a hypothetical minimal root \(N>2^{71}\).

Thus survivor-level whole-prefix maximality is globally legitimate throughout the whole \(H_*\) horizon as well.

The next obstruction is therefore not root positivity. It is whether coefficient survival plus survivor-Hensel maximality/endpoint structure can force a merge or descent before \(H_*\), or whether a still-closer parity-RS rational wall must be constructed.

Certificate:

`collatz/src/parity_rs_farey_gate_17087914_certificate.py`.
