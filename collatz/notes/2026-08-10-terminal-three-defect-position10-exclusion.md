# Exact exclusion of the position-10 three-terminal-defect geometry

Date: 2026-08-10

Status: **FINITE EXACT EXCLUSION / BRANCH-SPECIFIC**

This note continues the isolated first-crossing analysis at

\[
(q,\sigma)=(137,528,045,312,\;217,976,794,617)
\]

inside the `m=46`, high-four-trit `1000` recursive-sufficiency branch.

It concerns Family A of the exactly-three-terminal-defect analysis: the first two terminal coordinates belong to one inherited positive-defect run, and the third/local isolated defect occurs at terminal position `10` in the project's last-20 indexing.

The result below eliminates this entire geometry.  It does not eliminate the whole `1000` branch or prove Collatz globally.

## 1. Exact lower-18 split

For the position-10 local defect the exact endpoint residue is

\[
y\bmod3^{18}=224,474,041.
\]

The near-return window

\[
0\le d=y-x\le29,785,654
\]

splits the lower-18 ternary Cantor choices into exactly two carry classes.

### Carry 0

\[
\boxed{8,192\text{ lower choices}},
\qquad
\boxed{d_{\min}=23,589,342}.
\]

The safe Denjoy--Koksma/Ostrowski correction budget gives

\[
\boxed{z_0\le14,837,573}.
\]

The exact `3^30` terminal congruence uses

\[
B=120,123,938,613,220,
\qquad
K_0=94,991,663,650,112.
\]

### Carry 1

\[
\boxed{20,480\text{ lower choices}},
\qquad
\boxed{d_{\min}=9,240,435}.
\]

The safe amplitude ceiling is

\[
\boxed{z_0\le49,747,722}.
\]

The terminal constant is

\[
K_1=94,991,663,650,113.
\]

## 2. State-dependent correction-budget transfer

The inherited adjacent amplitudes are reduced with the same exact bounded-discrete-log transfer used in the two-defect analysis.

For every compatible upper 22-trit Cantor state `S_22`, the transfer retains a safe maximum near-return difference `d_cap(S_22)` obtained from

\[
\Delta S
\le U_S-\Lambda_-x-d
\]

and the certified inherited-amplitude lower cost.  The lower-18 choices are restored only when their exact `d` obeys this state-dependent cap.

### Carry 0 reduction

The transfer leaves

\[
\boxed{215,180}
\]

distinct high states and the safe ordinary-start superset

\[
\boxed{980,644,423}.
\]

Only the following upper-four ternary states survive:

| upper four trits | high states | safe ordinary starts |
|---|---:|---:|
| `0000` | 70,103 | 366,937,708 |
| `0001` | 61,828 | 300,786,849 |
| `0010` | 43,776 | 178,533,419 |
| `0011` | 35,094 | 127,922,908 |
| `0100` | 3,427 | 5,431,391 |
| `0101` | 952 | 1,032,148 |

Every `011*` and `1***` state is already removed by the safe correction budget.

### Carry 1 reduction

The parallel exact discrete-log/state generator gives

- `18,899,030` raw amplitude/target pairs;
- `12,577,756` pairs passing the safe correction-budget filter;
- `1,241,089` distinct high states with at least one permitted lower choice;
- the safe ordinary-start superset
  \[
  \boxed{15,742,256,601}.
  \]

The upper-four distribution is:

| upper four trits | high states | safe ordinary starts |
|---|---:|---:|
| `0000` | 131,054 | 2,105,911,112 |
| `0001` | 131,043 | 2,086,970,699 |
| `0010` | 131,016 | 2,044,438,045 |
| `0011` | 130,969 | 2,017,810,997 |
| `0100` | 130,308 | 1,793,611,317 |
| `0101` | 129,998 | 1,732,218,499 |
| `0110` | 128,903 | 1,578,361,991 |
| `0111` | 128,155 | 1,498,864,271 |
| `1000` | 67,156 | 341,761,640 |
| `1001` | 57,949 | 272,330,637 |
| `1010` | 40,238 | 156,965,106 |
| `1011` | 31,640 | 109,496,317 |
| `1100` | 2,290 | 3,220,574 |
| `1101` | 370 | 295,396 |

No `1110` or `1111` state survives.

## 3. Exact 16-step affine evaluator

To scan the large ordinary-start supersets exactly, the implementation precomputes for every residue

\[
r\pmod{2^{16}}
\]

its 16-bit parity mask, odd count `q(r)`, and affine correction `R(r)`.  Hence for every ordinary integer in that residue class,

\[
\boxed{
T^{16}(x)=\frac{3^{q(r)}x+R(r)}{2^{16}}.
}

Within-block coefficient crossing is checked from prefix popcounts of the stored parity mask against the exact barrier

\[
a_k=\lceil k\log_3 2\rceil.
\]

The barrier table is generated with exact arbitrary-precision integer comparisons, not floating logarithms.  Thus the block evaluator is an exact batching of 16 ordinary accelerated-Collatz steps, not an approximation.

## 4. Carry-0 exact scan

All

\[
\boxed{980,644,423}
\]

safe starts were checked.  The branch maxima are:

| upper four trits | starts checked | max `tau_c` |
|---|---:|---:|
| `0000` | 366,937,708 | 427 |
| `0001` | 300,786,849 | 417 |
| `0010` | 178,533,419 | 373 |
| `0011` | 127,922,908 | 414 |
| `0100` | 5,431,391 | 317 |
| `0101` | 1,032,148 | 281 |

The carry-0 maximum is

\[
\boxed{\max\tau_c=427}.
\]

No start survives through depth `1000` and no 128-bit overflow occurs.

## 5. Carry-1 exact scan

All

\[
\boxed{15,742,256,601}
\]

safe starts were checked.  The branch maxima are:

| upper four trits | starts checked | max `tau_c` |
|---|---:|---:|
| `0000` | 2,105,911,112 | 433 |
| `0001` | 2,086,970,699 | 493 |
| `0010` | 2,044,438,045 | 452 |
| `0011` | 2,017,810,997 | 451 |
| `0100` | 1,793,611,317 | **501** |
| `0101` | 1,732,218,499 | 430 |
| `0110` | 1,578,361,991 | 443 |
| `0111` | 1,498,864,271 | 436 |
| `1000` | 341,761,640 | 389 |
| `1001` | 272,330,637 | 421 |
| `1010` | 156,965,106 | 447 |
| `1011` | 109,496,317 | 362 |
| `1100` | 3,220,574 | 272 |
| `1101` | 295,396 | 216 |

The carry-1 maximum is

\[
\boxed{\max\tau_c=501}
\]

at

\[
\boxed{x=36,770,206,083,312,529,643,055}.
\]

Again no start survives through depth `1000` and no 128-bit overflow occurs.

## 6. Independent Wolfram cross-check

The maximizing start from every nonempty subbranch was re-evaluated with Wolfram arbitrary-precision integers using direct comparisons

\[
3^{q_k}<2^k.
\]

The returned stopping times were, in the recorded carry-0 then carry-1 order,

\[
\boxed{
281,317,414,373,417,427,
216,272,362,447,421,389,436,443,430,501,451,452,493,433
}
\]

and agree exactly with the C++ block scans.

## 7. Result

The two safe supersets contain in total

\[
980,644,423+15,742,256,601
=
\boxed{16,722,901,024}
\]

ordinary starts.

Every one has coefficient stopping time at most

\[
\boxed{501},
\]

astronomically below the isolated target

\[
\sigma=217,976,794,617.
\]

Therefore Family A with the local third defect at terminal position `10` is impossible.

The remaining Family-A local positions are now

\[
\boxed{3,5,7,9,12,14,19}.
\]

The inherited-length-three Family B remains open.

## 8. Scope

This is a finite exact, branch-specific exclusion.  It is not a proof of Collatz and does not eliminate the entire `1000` branch.
