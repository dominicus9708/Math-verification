# Exact exclusion of the position-3 three-terminal-defect geometry

Date: 2026-08-10

Status: **FINITE EXACT EXCLUSION / BRANCH-SPECIFIC**

At the isolated resonance

\[
(q,\sigma)=(137,528,045,312,217,976,794,617)
\]

inside the `m=46`, high-four-trit `1000` branch, this note eliminates Family A with the local third terminal defect at position `3`.

The first two terminal defects form one inherited adjacent positive-defect run.  The position-3 local defect is isolated.

## 1. Exact lower-18 carry classes

The terminal residue is

\[
\boxed{y\bmod3^{18}=178,809,481.}
\]

The `1000` near-return window produces two carry classes.

### Carry 0

\[
\boxed{9,364\text{ lower choices}},
\qquad
\boxed{d_{\min}=18},
\qquad
\boxed{z_0\le72,229,180}.
\]

The exact terminal constant is

\[
K_0=96,252,740,569,301.
\]

### Carry 1

\[
\boxed{13,824\text{ lower choices}},
\qquad
\boxed{d_{\min}=20,971,503},
\qquad
\boxed{z_0\le21,206,640}.
\]

The terminal constant is

\[
K_1=96,252,740,569,302.
\]

## 2. Carry-1 reduction and scan

The exact bounded-discrete-log transfer with the state-dependent correction budget leaves

\[
\boxed{443,544}
\]

distinct high states and

\[
\boxed{2,528,361,015}
\]

safe ordinary starts.

Only the upper-four ternary states `0000` through `0111` survive; every `1***` state is removed by the safe budget.

All ordinary starts were checked with the exact 16-step affine coefficient-stopping evaluator.  The subbranch maxima are:

| upper 4 trits | starts | max `tau_c` |
|---|---:|---:|
| `0000` | 722,786,685 | 432 |
| `0001` | 642,117,295 | 422 |
| `0010` | 491,798,146 | 428 |
| `0011` | 423,410,848 | **441** |
| `0100` | 123,046,952 | 346 |
| `0101` | 81,881,297 | 351 |
| `0110` | 29,492,918 | 340 |
| `0111` | 13,826,874 | 308 |

Thus

\[
\boxed{\max\tau_c=441}
\]

for carry 1.

## 3. Carry-0 reduction and scan

The carry-0 transfer is much looser.  It leaves

\[
\boxed{1,994,749}
\]

distinct high states and

\[
\boxed{15,656,812,791}
\]

safe ordinary starts.  All 16 upper-four ternary states occur.

All starts were checked exactly.  The subbranch maxima are:

| upper 4 trits | starts | max `tau_c` |
|---|---:|---:|
| `0000` | 1,227,358,208 | **517** |
| `0001` | 1,227,345,920 | 454 |
| `0010` | 1,227,341,056 | 443 |
| `0011` | 1,227,306,648 | 422 |
| `0100` | 1,227,007,652 | 443 |
| `0101` | 1,226,796,825 | 443 |
| `0110` | 1,226,051,112 | 497 |
| `0111` | 1,225,230,410 | 438 |
| `1000` | 1,090,947,986 | 444 |
| `1001` | 1,054,666,619 | 428 |
| `1010` | 972,485,639 | 466 |
| `1011` | 919,881,328 | 452 |
| `1100` | 595,527,138 | 497 |
| `1101` | 520,888,133 | 501 |
| `1110` | 376,744,606 | 492 |
| `1111` | 311,233,511 | 425 |

Thus

\[
\boxed{\max\tau_c=517}
\]

for carry 0, attained at

\[
\boxed{x=36,764,783,225,585,092,412,863.}
\]

No start in either carry class survives coefficient contraction through depth `1000`; no 128-bit overflow occurs.

## 4. Independent check

The carry-0 global maximizing start and the carry-1 maximizing start were independently re-evaluated with Wolfram arbitrary-precision integer arithmetic by direct tests of

\[
3^{q_k}<2^k.
\]

The returned stopping times are exactly

\[
\boxed{517,441}.
\]

## 5. Result

The two safe supersets contain

\[
15,656,812,791+2,528,361,015
=
\boxed{18,185,173,806}
\]

ordinary starts.

Every one has coefficient stopping time at most `517`, so Family A with the local third defect at terminal position `3` is impossible.

After also removing positions `10`, `15`, and `17`, the remaining Family-A local positions are

\[
\boxed{5,7,9,12,14,19}.
\]

The inherited-length-three Family B remains open.
