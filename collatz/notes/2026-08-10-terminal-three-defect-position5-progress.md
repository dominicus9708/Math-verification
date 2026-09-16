# Position-5 three-terminal-defect scan progress

Date: 2026-08-10

Status: **PARTIAL FINITE EXACT EXCLUSION / CONTINUATION CHECKPOINT**

This note records the current exact scan state for Family A with the local third defect at terminal position `5` in the isolated `m=46`, `1000` branch.

It is a checkpoint only: position `5` is **not yet fully excluded**.

## 1. Transfer data

The exact lower-18 terminal residue is

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

The bounded discrete-log / state-dependent correction-budget transfer leaves

\[
\boxed{3,796,529}
\]

distinct high states and the safe ordinary-start superset

\[
\boxed{48,739,016,799}.
\]

All 16 upper-four ternary states occur.

## 2. Completed upper-four branches

The following branches have been completely exact-scanned:

| upper four trits | starts checked | max `tau_c` |
|---|---:|---:|
| `1111` | 774,789,499 | 455 |
| `1110` | 913,492,609 | 425 |
| `1101` | 1,201,767,245 | 449 |
| `1100` | 1,355,494,336 | 421 |
| `1011` | 2,212,065,214 | **509** |
| `1010` | 2,400,017,550 | 452 |
| `1001` | 2,772,284,051 | 447 |
| `1000` | 2,946,042,538 | 436 |
| `0111` | 4,216,915,760 | 455 |

The `0111` branch exceeded one tool-execution batch at four-trit resolution, so it was partitioned into its four upper-six-trit children.  The children contain

\[
1,055,042,470,
1,054,652,952,
1,053,796,628,
1,053,423,710
\]

starts respectively; every child was checked and their sum is exactly the original `0111` count.

The completed branches contain in total

\[
\boxed{18,792,868,802}
\]

safe ordinary starts.

None survives coefficient contraction through depth `1000`; no 128-bit overflow occurs.  The largest stopping time observed so far is

\[
\boxed{509}.
\]

## 3. Remaining position-5 branches

The following upper-four states remain unscanned at this checkpoint:

\[
\boxed{0110,0101,0100,0011,0010,0001,0000}.
\]

Their safe-start counts are:

| upper four trits | remaining starts |
|---|---:|
| `0110` | 4,237,526,471 |
| `0101` | 4,264,412,927 |
| `0100` | 4,271,797,794 |
| `0011` | 4,291,623,180 |
| `0010` | 4,292,565,479 |
| `0001` | 4,293,872,221 |
| `0000` | 4,294,349,925 |

For execution only, not as a mathematical relaxation, a large four-trit branch may be split into its next two ternary digits.  This partitions the exact same candidate set into four disjoint six-trit branches and keeps each scan within the runtime batch limit.

## 4. Scope

No conclusion about position `5` as a whole is yet made.  The next action is to scan the seven remaining upper-four branches, splitting each into six-trit children when required, with the same exact 16-step affine evaluator and exact coefficient-barrier table.
