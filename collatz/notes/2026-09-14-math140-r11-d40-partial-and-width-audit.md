# MATH-140 — r=11 D=40 partial exact q-gate audit and arithmetic-width boundary

Date: 2026-09-14

Status: `MAINLINE SUPPORT / PARTIAL EXACT SAFE SUBSET / IMPLEMENTATION-WIDTH AUDIT / NO r=11 CLOSURE CLAIM`

## Frozen source

The exact prepared r=11 source remains:

- prepared pieces: 605,977
- represented occurrence mass: 3,419,719,061,560
- frozen floor: 2^71

MATH-139 certifies through D=39:

- safe mass = 3,350,963,514,708
- tail = 68,755,546,852
- safe fraction = 97.9894387342%

## D=40 partial exact increment

The following odd-step classes have exact D=40 first-safe increments certified:

- s=22: 193,319,641
- s=23: 329,812,946
- s=24: 922,482,371
- s=25: 743,608,772
- s=26: 693,935,584
- s=33..53: exact direct/profile-address replay already completed

The pairwise-disjoint certified D=40 partial increment is

\[
\Delta_{40}^{\rm partial}=2,897,326,399.
\]

Therefore, without using any result from the still-pending classes s=27..32,

\[
\text{safe}\ge 3,353,860,841,107,
\]

\[
\text{tail}\le 65,858,220,453,
\]

and

\[
\text{safe fraction}\ge 98.07416284006216\%.
\]

This is an exact finite lower bound only. It is not an r=11 closure.

## Pending D=40 classes

The exact D=40 first-safe count remains pending for

\[
s=27,28,29,30,31,32.
\]

The leaf-support enumeration at D=40 grows to 3,498,117,988 newly crossing residues, making repeated class-by-class leaf traversal an implementation bottleneck. This is not a mathematical gate failure.

## Arithmetic-width audit

The q-envelope threshold contains a numerator of order

\[
2^{D+71}.
\]

An `unsigned __int128` implementation is therefore safe only while

\[
D+71\le127,
\]

namely

\[
\boxed{D\le56}.
\]

At D=57 and above the numerator can overflow 128 bits. A preliminary fixed-width profile probe that appeared to show zero new crossings at D=58..60 was therefore invalid. An independent arbitrary-precision replay restores nonzero crossings at those depths.

This width issue does **not** affect any certified result through D=40.

## Claim boundary

- D=40 partial exact subset: certified.
- D=40 whole-depth increment: not yet certified.
- r=11: OPEN.
- First universal Farey cell: OPEN.
- Collatz conjecture: OPEN.

The next exact steps are (i) finish s=27..32 with a non-leaf-explosive representation, and/or (ii) complete the independent MATH-141 continuation of the unchanged MATH-108 AP-union closure gate.
