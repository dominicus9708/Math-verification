# DSD complete descriptor and cyclic-window acceleration — MATH-011

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Scope of this result: exact finite `61+11` coefficient-survival transducer only
- Result: `CONFIRMED WITHIN SCOPE / COMPUTATIONAL ACCELERATION`

## Motivation

MATH-010 showed that DSD stage tracking can prevent semantic double counting, but by itself did not reduce the mathematical state space. The next goal was therefore not to add more descriptors, but to ask whether the exact survival predicate can be compressed into a smaller complete state and whether that state can reduce repeated computation.

## 1. Complete tail descriptor

For one lifted residue `r mod 2048`, let `s_j(r)` be the number of odd shortcut steps in its first `j` tail bits, `1 <= j <= 11`.

The MATH-006 coefficient-survival condition through depth 72 is

\[
q_{61}+s_j(r)\ge q_{\min}(61+j)
\qquad(1\le j\le11).
\]

Therefore define

\[
\boxed{
H(r)=\max_{1\le j\le11}
\bigl(q_{\min}(61+j)-s_j(r)\bigr).
}
\]

Then the whole 11-step Boolean predicate is exactly equivalent to

\[
\boxed{
r\text{ survives through depth }72
\iff q_{61}\ge H(r).}
\]

Thus `H(r)` is a **complete descriptor within this finite predicate**: once it is known, the 11 parity steps do not have to be replayed for every `q61`.

Exact distribution over all 2048 lifted residues:

| `H(r)` | residue count |
|---:|---:|
| 39 | 247 |
| 40 | 554 |
| 41 | 570 |
| 42 | 406 |
| 43 | 195 |
| 44 | 63 |
| 45 | 12 |
| 46 | 1 |

The counts sum to 2048. In particular, `q61 >= 46` makes every lifted residue survive this coefficient-only depth-72 test, matching MATH-006.

## 2. Exact cyclic-window transform

For fixed `q=q61`, put

\[
m=3^q\pmod{2048}.
\]

Since `m` is odd, it has an inverse modulo 2048.

MATH-006 counts, for each base endpoint phase `y`, the surviving addresses

\[
C_q(y)
=
\sum_{a=1024}^{1363}
\mathbf 1\!\left[H(y+am\bmod2048)\le q\right].
\]

Let

\[
z=m^{-1}y\pmod{2048}
\]

and define

\[
g_q(t)=\mathbf1\!\left[H(mt\bmod2048)\le q\right].
\]

Then

\[
\boxed{
C_q(y)=\sum_{a=1024}^{1363}g_q(z+a).
}
\]

The 340-address arithmetic progression has therefore become a **cyclic contiguous window of length 340**.

All 2048 values of `C_q(y)` can be obtained by one initial length-340 sum followed by a sliding-window update. No approximation, averaging, or probabilistic step is used.

Because `y -> z` is a permutation, the theorem-facing minimum and maximum survivor counts can be read directly from those cyclic windows without restoring the original `y` order.

## 3. Exact regression

The accelerated calculation reproduces the complete legacy MATH-006 count vector for every `y mod 2048` and every `q61=39..61`.

The familiar min/max table is unchanged:

| `q61` | min | max |
|---:|---:|---:|
| 39 | 36 | 47 |
| 40 | 124 | 141 |
| 41 | 221 | 235 |
| 42 | 288 | 303 |
| 43 | 320 | 333 |
| 44 | 336 | 340 |
| 45 | 339 | 340 |
| 46–61 | 340 | 340 |

So this is an acceleration of an existing exact calculation, not a new block-exclusion theorem.

## 4. Deterministic work reduction

The original all-phase/all-address aggregation performs

\[
23\cdot2048\cdot340
=
\boxed{16{,}015{,}360}
\]

address-survival predicate lookups for `q61=39..61`.

After the `H(r)` compression, each q-level needs only 2048 threshold evaluations to build the cyclic indicator array:

\[
23\cdot2048
=
\boxed{47{,}104}.
\]

Thus the expensive address-predicate evaluation count is reduced by the exact factor

\[
\boxed{340}.
\]

There remains cheap integer work for the initial window and sliding updates. The one-time construction of `H` uses exactly

\[
2048\cdot11=22{,}528
\]

tail-bit steps.

A session-local Python benchmark also showed a large wall-clock reduction, but runtime ratios are hardware/interpreter dependent and are therefore diagnostic only, not part of the mathematical claim.

## 5. DSD interpretation

This is the first current Collatz example where DSD is used not only to audit a calculation but to identify a **complete computational descriptor** and an **exact safe reparameterization** that reduce repeated work.

The roles are:

- `D`: the target predicate is explicitly the depth-72 coefficient-survival predicate;
- `R`: resolution is fixed at 61 root bits + 11 tail bits;
- `S/E`: survival/exclusion is represented exactly by `q61 >= H(r)`;
- `T`: the address lift and inverse-multiplier coordinate change are explicit;
- `C`: exact vector equality with the legacy MATH-006 calculation is asserted;
- `N`: `ESTABLISHED_WITHIN_SCOPE`; no universal upgrade;
- `O`: computational acceleration, with unchanged theorem-facing survivor bounds.

This is closer to a DSD-native computational method than MATH-010 because the descriptor is now used to avoid work, not merely to label it.

## 6. What this does not prove

It does not prove that any of the surviving 340 address blocks are globally empty.

It does not strengthen the current 47/141/235/etc. pointwise caps.

It does not extend the finite 61+11 descriptor to arbitrary depth without a new proof.

It does not close the first universal cell or the Collatz conjecture.

## Certificate

`collatz/src/2026_09_08_dsd_complete_descriptor_cyclic_window_acceleration.py`

Commit: `03f4c5bc86bbea3a27dbdf509da79d15dd70492d`

## Next computational target

The useful lesson is now concrete: search for a new exact finite predicate whose continuation condition can again be collapsed to a complete descriptor, rather than adding metadata that does not reduce work.

The strongest next candidate is the depth-72+ same-integer continuation/Hensel eligibility predicate. If an analogue of `H(r)` exists there, it could reduce the next state expansion before the search tree grows.
