# Exact exclusion of the position-5 three-terminal-defect geometry

Date: 2026-08-10

Status: **FINITE EXACT EXCLUSION / BRANCH-SPECIFIC**

At the isolated first-crossing resonance

\[
(q,\sigma)=(137,528,045,312,217,976,794,617)
\]

inside the `m=46`, high-four-trit `1000` branch, this note eliminates Family A with the local third terminal defect at position `5`.

## 1. Transfer data

The exact lower-18 endpoint residue is

\[
\boxed{y\bmod3^{18}=370,128,241.}
\]

There is one near-return carry class:

\[
\boxed{16,384\text{ lower choices}},
\qquad
\boxed{d_{\min}=1,839,627},
\qquad
\boxed{z_0\le67,753,506}.
\]

The exact terminal constant is

\[
\boxed{K=14,061,641,112,655}.
\]

The bounded discrete-log transfer with the state-dependent correction budget leaves

\[
\boxed{3,796,529}
\]

distinct high states and the safe ordinary-start superset

\[
\boxed{48,739,016,799}.
\]

All 16 upper-four ternary states occur.

## 2. Exact coefficient-stopping evaluator

The ordinary-start scan uses an exact 16-step affine table indexed by `x mod 2^16`.  For each residue `r`, the table stores the 16-bit parity mask, the odd count `q(r)`, and the affine correction `R(r)`, so that

\[
T^{16}(x)=\frac{3^{q(r)}x+R(r)}{2^{16}}.
\]

The coefficient barrier

\[
a_k=\lceil k\log_3 2\rceil
\]

is generated with exact arbitrary-precision integer comparisons.

For the large remaining branches the evaluator was sharpened further.  If `p_j(r)` is the odd-count prefix within the 16-step block beginning at global depth `k`, then survival of the whole block is exactly equivalent to

\[
q_0\ge
\max_{1\le j\le16}
\left(a_{k+j}-p_j(r)\right).
\]

This threshold is precomputed for every block index and every `r mod 2^16`.  A surviving block therefore needs only one barrier comparison; the 16 individual parity bits are unfolded only in the unique block containing the first coefficient crossing.  This is an exact acceleration, not an approximation.

The fast evaluator was first run on previously completed subbranches and reproduced the same stopping times and maximizing starts before being used on the remaining large branches.

## 3. Complete scan

Every safe ordinary start was checked.  The upper-four branch results are:

| upper four trits | safe starts | max `tau_c` |
|---|---:|---:|
| `0000` | 4,294,349,925 | 482 |
| `0001` | 4,293,872,221 | 517 |
| `0010` | 4,292,565,479 | 463 |
| `0011` | 4,291,623,180 | 498 |
| `0100` | 4,271,797,794 | 459 |
| `0101` | 4,264,412,927 | **524** |
| `0110` | 4,237,526,471 | 505 |
| `0111` | 4,216,915,760 | 455 |
| `1000` | 2,946,042,538 | 436 |
| `1001` | 2,772,284,051 | 447 |
| `1010` | 2,400,017,550 | 452 |
| `1011` | 2,212,065,214 | 509 |
| `1100` | 1,355,494,336 | 421 |
| `1101` | 1,201,767,245 | 449 |
| `1110` | 913,492,609 | 425 |
| `1111` | 774,789,499 | 455 |

The sum is exactly

\[
\boxed{48,739,016,799}.
\]

No start survives coefficient contraction through depth `1000` and no 128-bit overflow occurs.

The global maximum is

\[
\boxed{\max\tau_c=524}
\]

at

\[
\boxed{x=36,771,052,192,510,326,003,879.}
\]

## 4. Independent check

The maximizing start was independently re-evaluated in Wolfram with arbitrary-precision integers by direct comparison of

\[
3^{q_k}<2^k.
\]

Wolfram returns exactly

\[
\boxed{\tau_c=524}.
\]

## 5. Result

Family A with the local third defect at terminal position `5` is impossible.

Together with the previously eliminated positions `3`, `10`, `15`, and `17`, the remaining Family-A local positions are now

\[
\boxed{7,9,12,14,19}.
\]

The inherited-length-three Family B remains open.

This is a finite exact, branch-specific result and does not prove the Collatz conjecture globally.
