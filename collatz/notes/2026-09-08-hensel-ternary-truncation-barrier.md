# Hensel ternary truncation barrier — MATH-014

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / EXACT INFORMATION BARRIER`
- New universal Collatz exclusion: **none**

## 1. Question after MATH-013

MATH-013 showed that exact root-Hensel translation classes use

\[
\kappa=(q,r),\qquad r=C\bmod3^q,
\]

and that one maximum correction quotient `h` per exact class is enough for class-max computation.

The next compression attempt was to ask whether the full ternary residue could be replaced uniformly by a shorter one,

\[
C\bmod3^m,\qquad m<q.
\]

The answer is **no** for the unrestricted length-k competitor language whenever `q<k`.

## 2. Constructive alias pair

Fix any

\[
q\ge1,
\qquad k\ge q+1.
\]

Take two length-k parity words whose odd positions are

\[
P_w=\{0,2,3,\ldots,q\},
\]

\[
P_u=\{1,2,3,\ldots,q\}.
\]

Both contain exactly `q` odd bits. All positions after `q` may be padded with zeros.

For a parity word with odd positions `p_1<\cdots<p_q`, its shortcut correction is

\[
C=\sum_{j=1}^q 2^{p_j}3^{q-j}.
\]

The two constructed words share their final `q-1` odd positions, so every shared contribution cancels. The only difference is the first odd position:

\[
\boxed{C(w)-C(u)=(2^0-2^1)3^{q-1}=-3^{q-1}.}
\]

Therefore

\[
C(w)\equiv C(u)\pmod{3^{q-1}},
\]

but

\[
C(w)\not\equiv C(u)\pmod{3^q}.
\]

Thus the two states are aliased by every truncation

\[
C\bmod3^m,
\qquad m\le q-1,
\]

while remaining distinct exact Hensel classes.

## 3. Exact barrier theorem

Hence, for every `q>=1` and every depth `k>=q+1`,

\[
\boxed{
C\bmod3^m\ (m<q)
\text{ is not a complete descriptor of the exact Hensel translation class}
}
\]

on the unrestricted parity-word language.

Equivalently, the MATH-013 exact key

\[
(q,C\bmod3^q)
\]

cannot be replaced by a uniformly shorter power-of-three residue without imposing additional downstream restrictions that are proved separately.

This is stronger than a depth-24 finite collision: it is a constructive all-q family.

## 4. Computational consequence

The Hensel compression line now has a clean stop rule.

- `d=k-q` remains complete for the MATH-012 arithmetic-credit gate.
- `(q,C mod 3^q)` remains the exact class descriptor for MATH-013 class-max dominance.
- a naive fixed ternary truncation is prohibited by MATH-014.

Therefore the primary calculation line should move to the address-local boundary halo unless a new restriction gives a genuinely smaller exact quotient.

## 5. DSD audit

- `D`: exact Hensel class and truncated ternary observations are separated.
- `R`: arbitrary finite parity words with `q<k`; theorem is constructive for all such q/k.
- `S`: explicit two-word witness family.
- `E`: every `m<q` truncation is excluded as a uniform exact class descriptor.
- `T`: zero padding preserves the witness at every larger depth.
- `C`: algebraic identity plus exact integer regression through `q=512`.
- `N`: `ESTABLISHED_WITHIN_SCOPE`.
- `O`: information barrier / strategy pruning; no Collatz candidate is excluded.

## 6. Prohibited upgrades

Do not infer that every possible non-ternary descriptor must have size `3^q`.

Do not infer that a problem-specific restricted language cannot admit a smaller quotient.

Do not infer that failure of this compression proves or disproves Collatz.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_hensel_ternary_truncation_barrier_certificate.py`

Certificate commit:

`74738fa7c875077c2e58aa370185dbe85507c2fc`

Expected output begins:

```text
PASS
constructive witness family regressed for q=1..512
```

## Next target

Use the exact fixed-depth correction-credit envelope to shrink the MATH-005 internal halos, canonicalize the boundary computation, and test cross-boundary endpoint collisions directly through the current 61+11 depth-72 window.
