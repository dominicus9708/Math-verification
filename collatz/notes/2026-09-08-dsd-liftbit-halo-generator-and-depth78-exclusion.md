# DSD lift-bit halo generator and internal-boundary exclusion through depth 78 — MATH-017

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED COMPUTATIONAL ACCELERATION + FINITE ONLY DEPTH-78 EXCLUSION`
- New universal Collatz exclusion: **none**

## 1. Why the depth-76 shell needed a new representation

MATH-016 closed all internal adjacent-block endpoint mergers through depth75. At depth76,

\[
q_{\min}(76)=48,
\qquad
76-q_{\min}=28,
\]

so the complete fixed-depth displacement halo becomes

\[
D=2^{28}-1=268{,}435{,}455.
\]

A direct integer scan would double the already large depth75 local range. Instead of scaling the old loop, the halo was re-described by its binary lift structure.

## 2. Exact lift-bit recurrence

Let `x_k` be the canonical lower residue modulo `2^k`, and let

\[
y=T^k(x_k),
\qquad q=q_k.
\]

Choose the next binary lift bit

\[
e\in\{0,1\},
\qquad x_{k+1}=x_k+e2^k.
\]

After k shortcut steps, the lifted endpoint is exactly

\[
\boxed{z=y+e3^q.}
\]

Therefore the next parity bit is

\[
\boxed{b=z\bmod2,}
\]

and

\[
y'=T(z),
\qquad q'=q+b.
\]

This gives an exact generator directly in binary-lift coordinates. No integer in the halo needs to be iterated from scratch.

## 3. Halo high-bit constraints

Let

\[
W=2^{61},
\qquad D=2^m-1.
\]

### Right side

For

\[
0\le r<D,
\]

the lift bits in positions

\[
m,\ldots,60
\]

are all zero. The first m bits branch, after which the generator is deterministic.

### Left side

Write

\[
x=W-\ell,
\qquad1\le\ell\le D.
\]

Then the lift bits in positions

\[
m,\ldots,60
\]

are all one. Again only the first m bits branch.

Coefficient survival is applied during generation, so failing states are never expanded further.

## 4. Regression against earlier brute-force halos

Before using the generator at the new shell, it was checked against previously exhaustive integer scans.

| m | right survivors | left survivors |
|---:|---:|---:|
| 22 | 7,376 | 7,741 |
| 26 | 120,566 | 120,071 |
| 27 | 241,066 | 240,441 |

All counts matched the prior brute-force results exactly.

This confirms that the lift-bit generator preserves the complete local universal-spine state set in those audited ranges.

## 5. New m=28 state set

For the depth76–78 shell,

\[
m=28.
\]

The exact generated lower-61 state counts are

\[
\boxed{481{,}570}
\]

on the right and

\[
\boxed{481{,}645}
\]

on the left.

Compared with the ambient `2^28` local offsets, this is roughly a factor-557 state reduction before the block-dependent tail is evaluated.

The reduction is exact pruning by the universal-spine condition, not sampling.

## 6. Endpoint scan through depth78

At depth78,

\[
q_{\min}(78)=50,
\qquad
78-50=28,
\]

so the same `m=28` complete halo is sufficient.

The generated lower-61 states were lifted through all 339 internal block boundaries and propagated through the 17-step tail from depth61 to depth78.

Exact surviving evaluations:

\[
64{,}370{,}400
\]

on the right and

\[
64{,}259{,}236
\]

on the left.

Exact same-q endpoint intersections:

\[
\boxed{0}.
\]

MATH-004 supplies equal q for candidate states sharing an endpoint. Therefore

\[
\boxed{
\text{no internal adjacent-block endpoint merger occurs at any common depth }k\le78.
}
\]

The deterministic-map argument again promotes the zero depth78 intersection to the whole finite prefix window.

## 7. Next shell size

At depth79,

\[
q_{\min}(79)=50,
\qquad
79-50=29,
\]

so the halo grows to

\[
D_{79}=2^{29}-1.
\]

The same exact generator already gives the new lower-61 state counts

\[
\boxed{964{,}227\text{ right},\qquad963{,}422\text{ left}.}
\]

Thus the next shell approximately doubles the generated state count. This is a computational planning fact only; no depth79 endpoint verdict is claimed yet.

## 8. DSD interpretation

- `D`: raw integer offset is replaced by the exact binary-lift state `(k,y,q,e)` needed by the transition.
- `R`: complete `2^m-1` halo; no sampling.
- `S`: universal-spine gate is applied before child expansion.
- `E`: impossible lift states are discarded immediately and permanently.
- `T`: exact affine lift `y -> y+e3^q` followed by one shortcut-map step.
- `C`: m=22,26,27 generator counts reproduce prior brute-force scans exactly; m=28 is then used for the new audit.
- `N`: acceleration is exact within the finite halo; endpoint exclusion remains finite in depth.
- `O`: halo generation is accelerated and the internal endpoint-coupling-free window is extended through depth78.

## 9. Prohibited upgrades

- Do not interpret the factor-557 local-state reduction as a Collatz density theorem.
- Do not extrapolate zero collisions through78 to arbitrary depth.
- Do not infer that the m=29 shell is collision-free before it is scanned.
- Do not infer first-cell or Collatz closure.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_dsd_liftbit_halo_generator_depth78_certificate.cpp`

Certificate commit:

`a39c5b6ce7b00aeea37bc33a8e978b8f86874760`

## Next target

Use the same lift-bit generator at `m=29`, but reduce the block-dependent endpoint comparison layer before scanning all 339 boundaries. The state-generation bottleneck has been removed; the next bottleneck is now the repeated exact tail-endpoint set construction for each boundary.
