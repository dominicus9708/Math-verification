# Exact exclusion of two terminal defects in the `1000` branch

Date: 2026-08-10

Status: **FINITE EXACT EXCLUSION / BRANCH-SPECIFIC**

This note closes every configuration with exactly two positive mechanical-cap defects among the final 20 odd-position coordinates at the isolated first-crossing resonance

\[
(q,\sigma)=
(137,528,045,312,\;217,976,794,617)
\]

inside the `m=46`, high-four ternary prefix `1000` branch.

It does **not** eliminate the entire `1000` branch and does not prove Collatz or coefficient stopping globally.

## 1. Upstream reduction

The previous terminal analysis established:

1. the final 20 odd-position coordinates contain at least one defect;
2. every exactly-one-defect configuration is impossible;
3. if there are exactly two terminal defects, then either
   - both are born locally in the last-20 window;
   - the first is inherited and the second is separated/isolated;
   - or the only remaining geometry is an inherited adjacent pair at the first two terminal positions.

The first two cases had already been finitely eliminated:

- 65 locally born two-defect patterns fail the full `3^48` near-return test;
- inherited-first / separated-second patterns reduce to `1,113,680` ordinary starts, all with coefficient stopping time at most `292`.

Thus only the adjacent inherited pair remained.

## 2. Corrected long-run amplitude bound

For the adjacent pair write

\[
(z_0,z_1)=(z,w),
\qquad1\le w\le z.
\]

The Denjoy--Koksma/Ostrowski sharpening in
`2026-08-10-ostrowski-run-sharpening.md` gives the corrected amplitude ceiling

\[
\boxed{z\le21,128,727.}
\]

The exact terminal congruence is

\[
G(3\,2^{-z}+2\,2^{-w}-5)
\equiv4S_{22}+K\pmod{3^{30}},
\]

where

\[
G=120,123,938,613,220,
\qquad
K=197,151,077,055,918,
\]

and `S_22` is a 22-digit ternary `0/1` Cantor coordinate.

Writing `r=z-w` converts this to a bounded discrete-log interval problem in the cyclic unit group modulo `3^30`.

## 3. Exact discrete-log candidate set

The corrected scanner gives:

\[
\boxed{3,411,199}
\]

raw `(r,w,S_22)` pairs.

Applying only safe rational versions of the correction budget leaves

\[
\boxed{730,578}
\]

pairs.

Merging repeated terminal patterns with the same upper ternary coordinate leaves

\[
\boxed{443,009}
\]

distinct safe upper states.

Restoring every permitted lower-18 ternary start produces the safe ordinary-start superset

\[
\boxed{2,525,428,246}.
\]

The smallest surviving adjacent amplitude is

\[
\boxed{(z,w,r)=(3232,994,2238).}
\]

Hence even the smallest adjacent hit inherits a long positive-defect ancestry; under the certified gap-two growth bound its first terminal defect belongs to a positive-defect run of at least `5523` odd-position coordinates.

## 4. Secondary ternary prefix split

The `443,009` safe upper states occupy only upper-4 ternary values

\[
0000,0001,0010,0011,
0100,0101,0110,0111.
\]

No `1***` state survives the safe budget.  Thus the highest free `S_22` ternary digit is forced to zero in the exactly-two-defect case.

The corresponding safe ordinary-start counts are:

| upper 4-trit value | safe ordinary starts |
|:--|--:|
| `0000` | 720,072,547 |
| `0001` | 640,245,541 |
| `0010` | 495,217,343 |
| `0011` | 424,720,055 |
| `0100` | 121,076,522 |
| `0101` | 81,694,485 |
| `0110` | 28,732,927 |
| `0111` | 13,668,826 |

Their sum is exactly

\[
2,525,428,246.
\]

## 5. Exact coefficient-stopping scan

For every ordinary start in each row above, the accelerated Collatz map was iterated until the first coefficient contraction.

The barrier was not evaluated with floating logarithms.  Exact rational intervals for `ln 2` and `ln 3` certify the integer table

\[
a_k=\lceil k\log_3 2\rceil
\]

through `k=1000`, and the scan tests simply whether the accumulated odd count satisfies `q_k<a_k`.

All arithmetic on the actual starts was integer arithmetic; no 128-bit trajectory overflow occurred.

The exact branch maxima are:

| upper 4-trit value | starts checked | maximum `tau_c` | maximizing start |
|:--|--:|--:|--:|
| `0000` | 720,072,547 | 440 | 36,764,983,324,792,268,385,055 |
| `0001` | 640,245,541 | 409 | 36,765,457,444,052,973,768,319 |
| `0010` | 495,217,343 | 457 | 36,766,678,145,941,941,341,055 |
| `0011` | 424,720,055 | 440 | 36,767,412,870,927,666,367,087 |
| `0100` | 121,076,522 | 435 | 36,770,282,685,737,492,012,443 |
| `0101` | 81,694,485 | 378 | 36,771,059,512,570,930,489,551 |
| `0110` | 28,732,927 | 379 | 36,772,193,568,960,059,989,863 |
| `0111` | 13,668,826 | 311 | 36,772,654,757,601,689,981,767 |

Therefore over the full safe superset

\[
\boxed{
\max\tau_c=457
}
\]

at

\[
\boxed{
x=36,766,678,145,941,941,341,055.}
\]

This is astronomically below the isolated target crossing depth

\[
\sigma=217,976,794,617.
\]

The eight maximizing starts were independently checked with Wolfram exact integer arithmetic by directly comparing `3^q` and `2^k`; the returned stopping times were

\[
(440,409,457,440,435,378,379,311)
\]

in the table order above.

## 6. Result

Every configuration with exactly two defects among the final 20 odd positions is impossible in the `1000` branch.

Combined with the earlier zero- and one-defect exclusions:

\[
\boxed{
\#\{i\in[q-20,q-1]:z_i>0\}\ge3.
}
\]

for every hypothetical paradoxical candidate in this branch.

This is a finite, branch-specific necessary condition.  It is not yet a contradiction with the global run-aware defect budget.

## 7. Methodological consequence

The useful pattern is now clear:

\[
\text{terminal defect-count hypothesis}
\to
\text{exact }3\text{-adic congruence}
\to
\text{bounded discrete-log/Cantor states}
\to
\text{safe ordinary-start superset}
\to
\text{exact coefficient-stopping scan}.
\]

However, naively repeating this for defect count three will enlarge the terminal combinatorics.  The next step should first seek a transfer that handles several terminal defect positions simultaneously, rather than enumerate all three-defect geometries one by one.