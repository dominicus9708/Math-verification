# Phase-height zero-tail box calibration

Date: 2026-08-20

Status: **exact finite calibration of the eventual-zero-lift obstruction in normalized phase-height boxes.** This is not an asymptotic theorem and not a proof of the Collatz conjecture.

## 1. Zero-tail box cap

For a phase-height state \((s,h)\), the actual affine exponent is

\[
a=b_s+h.
\]

Every normalized sparse-tail base satisfies

\[
1\le\rho<3^a.
\]

Define the exact zero-tail box cap

\[
\boxed{
Z(s,h)
:=
\max_{1\le\rho<3^{b_s+h}}
\tau_{s,h}(\rho),
}
\]

where \(\tau_{s,h}(\rho)\) is the largest \(J\) such that \(\rho\) remains above the shifted coefficient barrier through the first \(J\) future ordinary steps.

Equivalently, with the generalized minimal survivor

\[
\mu_{s,h}(J)
=\min\mathcal S_{s,h}(J),
\]

we have

\[
\boxed{
Z(s,h)
=
\max\left\{
J:\mu_{s,h}(J)<3^{b_s+h}
\right\}.
}
\]

Thus

\[
\mu_{s,h}(Z(s,h)+1)\ge3^{b_s+h}.
\]

If \(Z(s,h)<\infty\), no normalized base in that entire phase-height box can support an infinite zero-lift tail.

## 2. Reachable five-step phase-height layers

Starting from the four ordinary coefficient-surviving depth-five branches,

\[
(s,h)=(5,0),(5,1),
\]

the exact five-step transition gives the reachable height sets

\[
\boxed{
 s=10:\quad h\in\{0,1,2,3\},
}
\]

and after one further macro layer

\[
\boxed{
 s=15:\quad h\in\{0,1,2,3,4,5\}.
}
\]

No intermediate height in these ranges is missing.

## 3. Exact box caps through s=15

Exhaustive scans of every integer

\[
1\le\rho<3^{b_s+h}
\]

give:

\[
\begin{array}{c|c|c|r|r|r}
s&h&a=b_s+h&3^a&Z(s,h)&\rho_{\max}\\\hline
5&0&4&81&64&27\\
5&1&5&243&71&129\\
10&0&7&2187&85&1249\\
10&1&8&6561&110&2919\\
10&2&9&19683&118&9225\\
10&3&10&59049&170&37503\\
15&0&10&59049&137&35655\\
15&1&11&177147&178&142587\\
15&2&12&531441&192&142587\\
15&3&13&1594323&259&1394431\\
15&4&14&4782969&281&3064033\\
15&5&15&14348907&374&10507503
\end{array}
\]

Here \(\rho_{\max}\) is the first base attaining the maximum survival length.

All displayed caps are exact ordinary-integer scans with exact coefficient barriers.

## 4. Five-step interpretation

For the current macro size \(B=5\), a cap \(Z\) allows at most

\[
\left\lfloor\frac Z5\right\rfloor
\]

complete consecutive zero-lift macro blocks.

Thus the checked normalized boxes have complete-zero-block caps

\[
\begin{array}{c|c|c}
s&h&\lfloor Z/5\rfloor\\\hline
5&0&12\\
5&1&14\\
10&0&17\\
10&1&22\\
10&2&23\\
10&3&34\\
15&0&27\\
15&1&35\\
15&2&38\\
15&3&51\\
15&4&56\\
15&5&74
\end{array}
\]

A coefficient-surviving extension that remains inside one of these boxes must therefore introduce a new nonzero macro lift before the following macro block.

## 5. Interpretation

The finite data show two things.

First, the eventual-zero obstruction is not confined to the four initial branch bases. Entire normalized phase-height boxes can be closed exactly.

Second, the cap grows with phase/height and is not bounded by a small universal constant in the checked range. Therefore the correct asymptotic target should not be a fixed maximum zero-run length.

The normalized linear-corridor theorem gives a sharper route: after a fixed state, a zero-lift tail occupies only

\[
\frac{2^s\rho}{3^{b_s+h}}
=O(n)
\]

rather than the whole box. A global theorem should exploit this reachable corridor instead of attempting exhaustive control of every point below \(3^{b_s+h}\).

## 6. Remaining target

The natural deterministic target is now a comparison between

\[
\widehat\mu_{s,h}(L)
=\frac{2^s}{3^{b_s+h}}\mu_{s,h}(L)
\]

and the linear reachable corridor.

A proof that the normalized minimal survivor eventually outruns every such corridor would force infinitely many nonzero macro lift digits, hence exclude ordinary-integer infinite coefficient survivors within the corrected Stage-4 model.

Exact scanner:

`collatz/src/phase_height_zero_tail_box_cap.cpp`.
