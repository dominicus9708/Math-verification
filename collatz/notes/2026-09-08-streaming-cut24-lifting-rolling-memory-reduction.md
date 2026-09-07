# MATH-029 — streaming cut-24 lifting + rolling memory reduction

Date: 2026-09-08

Status:

`CONFIRMED / EXACT REORDERING / COMPUTATIONAL MEMORY REDUCTION / FINITE ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Purpose

MATH-028 combined bounded residue lifting through depth 61 with the MATH-025 11-step rolling continuation on the finite domain

\[
0\le r\le10^9.
\]

Its exact prefix tree reached a breadth-first peak of `11,894,128` live prefix states at depth 30.  MATH-029 changes only the enumeration order so that the same finite computation can be reproduced with much smaller simultaneous state storage.

## Exact streaming decomposition

Choose cut depth

\[
\boxed{K_{\rm cut}=24}.
\]

Phase A constructs the exact surviving bounded-lift frontier only through depth 24.

The exact frontier size is

\[
\boxed{286,581}.
\]

The number of bounded-lift branch attempts before the cut is

\[
\boxed{735,398}.
\]

Phase B takes each cut-frontier state independently and performs a local DFS through depth 61.  Every depth-61 survivor is consumed immediately by the exact address lift

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}}
\]

and then by the MATH-025 rolling 11-step continuation.

No state equivalence, quotient, or heuristic merge is introduced.

## Exact regression against MATH-028

The DFS phase performs

\[
\boxed{186,328,593}
\]

branch attempts. Therefore the total is

\[
735,398+186,328,593
=\boxed{187,063,991},
\]

exactly the same number of lift-branch attempts as MATH-028.

The complete finite output also agrees:

\[
\boxed{1,796,718}
\]

depth-61 leaves,

\[
r_{\min}=703,
\qquad
r_{\max}=999,999,207,
\]

and the same deepest failing rolling-window base

\[
\boxed{545}
\]

with first witness

\[
\boxed{r=378,620,799,\qquad b=1183}.
\]

Thus the finite endpoint-coupling exclusion remains the MATH-028 result

\[
61\le k\le3,000,000,003.
\]

## Memory-state reduction

The audited maximum local DFS stack is

\[
\boxed{7}.
\]

For 16 workers the algorithmic live-prefix storage is therefore

\[
286,581+16\cdot7
=\boxed{286,693}
\]

prefix states, compared with the MATH-028 breadth-first peak

\[
11,894,128.
\]

Hence the audited live-prefix state-count reduction is

\[
\frac{11,894,128}{286,693}\approx\boxed{41.49}.
\]

This is an algorithmic storage reduction, not a mathematical pruning result.  The same exact prefix tree is traversed in a different order.

An observed resident-memory reduction may depend on compiler, allocator, worker count, and platform, so the theorem-facing computational statement is the live-state count above rather than a machine-specific RSS ratio.

## DSD interpretation

MATH-029 is a DSD transition-order refinement.

- `D`: the represented state is unchanged.
- `R`: exact endpoint and odd-count resolution are preserved.
- `S`: no candidate state is removed beyond the existing exact coefficient gate.
- `E`: no new mathematical exclusion is asserted.
- `T`: breadth-first enumeration is replaced by cut-frontier + DFS streaming.
- `C`: total branch attempts and all terminal finite outputs are regressed exactly against MATH-028.
- `N`: `COMPUTATIONAL MEMORY REDUCTION / FINITE ONLY`.
- `O`: the same finite calculation becomes substantially more memory-scalable.

## Prohibited upgrades

Do not infer:

- 41.49x live-state reduction ⇒ 41.49x mathematical pruning;
- streaming enumeration ⇒ stronger Collatz theorem;
- finite agreement at `r<=10^9` ⇒ arbitrary-domain equivalence without the exact transition proof;
- MATH-028/029 endpoint-coupling exclusion ⇒ first-cell emptiness.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_streaming_cut24_lifting_rolling_certificate.cpp`

Certificate commit:

`5bc66d76b3e256dbc53c18edfc3be845e6f9e4a8`
