# A0 s=1: four shallow boundary windows determine a singleton candidate triple

Date: 2026-08-27

Status: **SAFE exact finite-address reduction.** This combines the renewal checkpoint, mixed-radix meet, and 40-bit debit/credit corridor. It does not prove the long pre/tail bridges exist and does not prove the Collatz conjecture.

## 1. Previously exposed checkpoint

The renewal checkpoint obeys

\[
2^{72}<Z<2^{73}.
\]

The companion mixed-radix theorem proves that

- first 28 tail parity bits determine `Z mod 2^28`;
- last 28 prefix odd ordinals determine `Z mod 3^28`;
- `2^28 3^28 > 2^72`.

Hence each such boundary-address pair yields at most one ordinary

\[
\boxed{Z\in(2^{72},2^{73}).}
\]

## 2. Once Z is fixed, X and Y lie in very narrow intervals

The renewal observables are

\[
L_-=3X-Z,
\qquad
L_+=3Y-Z.
\]

The exact corridor theorem gives, safely coarsened,

\[
75G<L_-<109G,
\]

\[
74G<L_+<108G.
\]

Therefore for a fixed `Z`,

\[
X=\frac{Z+L_-}{3}
\]

lies in an interval of width less than

\[
\frac{34G}{3},
\]

and similarly

\[
Y=\frac{Z+L_+}{3}
\]

lies in an interval of width less than the same amount.

Exact integer comparison gives

\[
\boxed{
\frac{34G}{3}<2^{37}<3^{24}.
}
\]

This turns the remaining start/end exposure into shallow local boundary problems.

## 3. Thirty-seven pre parity bits determine X

The first 37 parity steps of the pre block determine

\[
X\pmod{2^{37}}.
\]

Since the conditional `X` interval after fixing `Z` has width below `2^37`, this residue has at most one representative in that interval.

Thus

\[
\boxed{
Z+\text{first 37 pre parity bits}
\Longrightarrow
\text{at most one ordinary }X.
}
\]

The exact first-crossing ballot thresholds for those 37 steps leave

\[
\boxed{967,378,591}
\]

necessary parity prefixes. This is less than

\[
\boxed{2^{37}/128}.
\]

Again, these are necessary short prefixes; extension through the full pre bridge remains a separate condition.

## 4. Twenty-four tail endpoint trits determine Y

The final 24 odd ordinals of the tail affine correction determine

\[
Y\pmod{3^{24}}.
\]

Because the conditional `Y` interval after fixing `Z` has width below `2^37<3^24`, there is at most one ordinary representative in that interval.

Hence

\[
\boxed{
Z+\text{last 24 tail odd ordinals}
\Longrightarrow
\text{at most one ordinary }Y.
}

## 5. Four-window singleton structure

A physical `s=1` candidate can therefore be exposed from the four shallow boundary windows

\[
\boxed{
\begin{array}{c|c}
\text{boundary window}&\text{role}\\
\hline
\text{pre first 37 parity bits}&X\bmod2^{37}\\
\text{pre last 28 odd ordinals}&Z\bmod3^{28}\\
\text{tail first 28 parity bits}&Z\bmod2^{28}\\
\text{tail last 24 odd ordinals}&Y\bmod3^{24}
\end{array}}
\]

Together with the already-certified ordinary corridors, any tuple of these four short descriptors produces

\[
\boxed{
\text{zero or one ordinary triple }(X,Z,Y).
}
\]

The billion-step middle portions have not disappeared: they survive as **extension constraints** saying that the four short descriptors must be joined by a complete pre `0->0` ballot bridge and a complete tail `0->-1` first-passage bridge.

## 6. DSD audit

This reduction explicitly separates

\[
\text{candidate formation}
\quad\text{from}\quad
\text{long-bridge validation}.
\]

### SAFE

- each finite boundary window determines the stated residue;
- CRT/interval width turns residues into singleton ordinary candidates;
- no missing interior path is inferred from boundary compatibility.

### REJECTED

Do not infer

\[
\text{four shallow windows are mutually compatible}
\Longrightarrow
\text{the full pre/tail bridges exist}.
\]

That would be the same local-to-global error class already quarantined elsewhere.

## 7. New computational target

The direct `s=1` problem is no longer a `10^11`-step flat search. It is a four-boundary join followed by two extension checks:

\[
\boxed{
\text{37-bit pre start}
\leftrightarrow
\text{28-trit checkpoint-left}
\leftrightarrow
\text{28-bit checkpoint-right}
\leftrightarrow
\text{24-trit tail end}.
}
\]

The next proof-level task is to build an exact compact representation for the **pre last-28-odd endpoint language** and the **tail last-24-odd endpoint language**, then join them with the already small ballot-prefix automata before invoking any long-bridge extension theorem.

Companion certificate:

`collatz/src/A0_s1_four_window_singleton_exposure_certificate.py`.
