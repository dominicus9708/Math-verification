# MATH-038 — depth-35 q=23 sparse Hensel events

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED WITHIN q=23 LAYER / SPARSE EVENT STRUCTURE`

## 1. Inherited versus genuinely new collisions

MATH-037 found five collision classes at depth 34, all at `q=22`.

Since

\[
q_{\min}(35)=23,
\]

the even child of a `q=22` depth-34 state fails the coefficient floor, while the odd child has `q=23` and can survive. Thus the five existing collision classes have exactly five inherited q=23 child classes at depth 35.

A separate exact scan was then performed for genuinely new q=23 child collisions. A new q=23 collision can only arise when

- an even child of a depth-34 q=23 class, and
- an odd child of a depth-34 q=22 class

land in the same residue modulo `3^23`.

The exact cross-branch scan finds

\[
\boxed{15}
\]

new q=23 collision classes.

The fifteen new classes are disjoint from the five inherited classes.

Therefore the audited q=23 layer at depth 35 contains

\[
\boxed{5\text{ inherited}+15\text{ new}=20}
\]

collision classes.

This is a statement about the q=23 layer only. The current certificate does **not** exclude additional depth-35 collisions at q>23.

## 2. Why this matters computationally

The full coefficient-surviving word language at these depths contains tens to hundreds of millions of words. Yet the minimal-q Hensel collision layer is represented by only a few dozen collision events.

The correct DSD computation strategy is therefore to separate:

1. **persistent collision events**, which can be propagated cheaply because same-bit Hensel transitions preserve class coincidence and correction ordering;
2. **new cross-branch intersections**, which are the only place genuinely new class mergers can appear.

This avoids confusing the full candidate language with the much smaller event language.

## 3. Exact transition logic

For one Hensel class residue `r` at depth `k`:

- even transition preserves `(q,r)`;
- odd transition maps

\[
r\mapsto(3r+2^k)\bmod3^{q+1}.
\]

For fixed parent class, both maps are injective with respect to the exact class residue.

Hence a genuinely new collision at the next depth must come from a cross-branch intersection between an even image and an odd image from different parent q layers.

MATH-038 exploits exactly this structure.

## 4. DSD interpretation

- `D`: collision events are separated from the full word population.
- `R`: exact depth 35 and exact q=23 class residue modulo `3^23`.
- `S`: only coefficient-surviving depth-34 parent states are admitted.
- `E`: no candidate is excluded merely from event count; exclusion still requires legal positive credit and ordinary-start lineage.
- `T`: inherited collision classes and genuinely new cross-branch collisions are treated as separate transition types.
- `C`: 47,993,022 depth-34 q=23 parent classes and 39,993,895 depth-34 q=22 words are audited in the targeted scan.
- `N`: `ESTABLISHED_WITHIN q=23 FINITE SCOPE`.
- `O`: sparse-event representation remains promising, but the full depth-35 collision set is not yet closed.

## 5. Next calculation

The next nontrivial primitive layer is q=24 at depth 36. A direct sort of the required q=24 parent set exceeded the current single-run execution limit, so no depth-36 result is claimed from that attempt.

The preferred next move is to replace the large sorted parent vector with a partitioned or external-memory intersection so that only the new cross-branch event set is materialized.

## Prohibited upgrades

- `20 q=23 classes` ⇒ `20 total depth-35 classes` — **PROHIBITED**.
- sparse q=23 events ⇒ sparse all-q events — **PROHIBITED**.
- event propagation ⇒ ordinary-start exclusion without credit audit — **PROHIBITED**.
- timed-out depth-36 scan ⇒ any mathematical result — **PROHIBITED**.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth35_q23_sparse_certificate.cpp`

Certificate commit:

`edd96c6688def6733646ad1347620f057db5ead4`
