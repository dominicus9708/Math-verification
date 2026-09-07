# Internal-boundary endpoint exclusion through depth 75 — MATH-016

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `FINITE ONLY / EXACT DEPTH-75 INTERNAL-BOUNDARY EXCLUSION`
- New universal Collatz exclusion: **none**

## 1. Continuation of MATH-015

MATH-015 proved that no universal-spine candidate pair on opposite sides of any of the 339 internal `2^61` block boundaries merges at a common shortcut-map depth `k<=72`.

The same fixed-depth correction-credit envelope was then extended without changing the proof discipline.

For a same-endpoint candidate pair at depth k, MATH-004 gives common q and

\[
d<2^{k-q}\left(1-\left(\frac23\right)^q\right)<2^{k-q}.
\]

Coefficient survival gives the complete integer halo needed at each depth.

## 2. Incremental checkpoints

### Depth 73

\[
q_{\min}(73)=47,
\qquad
73-47=26,
\]

so the complete halo remains

\[
D_{73}=2^{26}-1.
\]

Exact scan over all 339 internal boundaries:

\[
\boxed{\text{collision count}=0.}
\]

Depth-73 surviving boundary evaluations:

- right: `20,193,949`;
- left: `19,985,263`.

### Depth 74

\[
q_{\min}(74)=47,
\qquad
74-47=27,
\]

so the complete halo doubles to

\[
D_{74}=2^{27}-1=134{,}217{,}727.
\]

After including the entire new outer shell:

\[
\boxed{\text{collision count}=0.}
\]

Depth-74 surviving boundary evaluations:

- right: `40,290,262`;
- left: `39,979,477`.

### Depth 75

\[
q_{\min}(75)=48,
\qquad
75-48=27,
\]

so the same complete halo is sufficient:

\[
D_{75}=2^{27}-1.
\]

The lower-61 universal-spine halo contains

\[
\boxed{241{,}066}
\]

right states and

\[
\boxed{240{,}441}
\]

left states.

Across all 339 boundaries, exact depth-75 surviving evaluations are

\[
37{,}619{,}431
\]

on the right and

\[
37{,}318{,}039
\]

on the left.

Exact endpoint intersection:

\[
\boxed{0}.
\]

Therefore

\[
\boxed{
\text{no internal adjacent-block endpoint merger occurs at any common depth }k\le75.
}
\]

The deterministic-map argument is the same as MATH-015: any earlier merger would persist to depth 75.

## 3. What changed computationally

The important point is not merely three additional depths. The calculation crossed a halo-growth threshold at depth74:

\[
2^{26}-1\longrightarrow2^{27}-1,
\]

included the entire new shell, and still found no internal endpoint coupling.

Thus the zero-collision result is not an artifact of reusing the old depth-72 search radius.

## 4. Scope

This is an exact finite statement through depth75 only.

It does **not** imply that the MATH-005 full-first-cell halos are empty, because at depth76

\[
q_{\min}(76)=48,
\qquad
76-48=28,
\]

and the complete halo grows again to

\[
2^{28}-1.
\]

The next shell must be explicitly included before making a depth76 statement.

## 5. DSD interpretation

- `D`: depth, q-minimum, halo radius, boundary address, and endpoint are separate state components.
- `R`: complete displacement halo at each audited depth; all 339 internal boundaries.
- `S`: universal-spine candidates only.
- `E`: all endpoint equalities through depth75 excluded in the complete finite envelope.
- `T`: exact 61-bit local state plus address-dependent tail propagation.
- `C`: zero collisions persisted after the depth74 halo doubled.
- `N`: `FINITE ONLY / ESTABLISHED_WITHIN_SCOPE`.
- `O`: current internal endpoint-coupling-free window extended from 72 to 75.

## 6. Prohibited upgrades

- No merger through75 does not imply no merger at depth76 or later.
- Do not infer full first-cell halo emptiness.
- Do not infer Collatz closure.
- Do not treat the finite zero-collision sequence as an asymptotic law without a separate theorem.

## Reproducibility

Primary depth75 certificate:

`collatz/src/2026_09_08_depth75_internal_boundary_endpoint_exclusion_certificate.cpp`

Certificate commit:

`76ba15fe7eb9521fa17f554e912c7f6a155e08f0`

Prior depth72 certificate:

`collatz/src/2026_09_08_depth72_internal_boundary_endpoint_exclusion_certificate.cpp`

Prior commit:

`656509a9ad6eb83ca7fb3f97174d0d12096e8855`

## Next target

Depth76 is the next genuine shell expansion:

\[
D_{76}=2^{28}-1.
\]

Before brute-force doubling again, reuse the DSD complete-descriptor approach to generate only universal-spine local residues in the new shell and test whether the high fixed binary lift bits admit a smaller exact generator than scanning every integer offset.
