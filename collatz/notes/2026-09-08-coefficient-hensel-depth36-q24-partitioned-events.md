# MATH-039 — depth-36 q=24 partitioned Hensel events

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED WITHIN q=24 LAYER / EXTERNAL-PARTITION SPARSE EVENT AUDIT`

## 1. Why partitioning was required

A monolithic in-memory sort of the depth-36 q=24 child population exceeded the session execution budget. DSD analysis showed that this was a representation/scheduling problem rather than a mathematical barrier.

The calculation was therefore rewritten as an exact 128-way partition by child Hensel residue modulo `3^24`. Each bucket is sorted independently and discarded after audit.

No mathematical state is merged across unequal residues.

## 2. Complete q=24 child construction

A depth-36 q=24 child can arise only from:

1. an **even** child of a depth-35 q=24 parent;
2. an **odd** child of a depth-35 q=23 parent.

The full child record count is

\[
\boxed{169{,}991{,}585}.
\]

After exact grouping by Hensel residue modulo `3^24`, the number of distinct classes is

\[
\boxed{169{,}991{,}555}.
\]

Hence the complete q=24 layer contains

\[
\boxed{30}
\]

collision classes, all of multiplicity exactly two.

## 3. Source decomposition

Source tagging splits those 30 classes exactly as follows:

- even/even duplicate inherited from an already-colliding depth-35 q=24 class: `0`;
- odd/odd duplicate inherited from the twenty depth-35 q=23 collision classes: `20`;
- one even + one odd, i.e. a genuinely new cross-branch merger: `10`.

Thus

\[
\boxed{30=20\text{ inherited}+10\text{ new cross}}.
\]

This also proves that the depth-35 q=24 parent layer itself is injective in its Hensel class residue: otherwise an even/even duplicate would appear.

## 4. Sparse-event interpretation

The event calculation now has a clean recursive structure:

- MATH-037: five primitive q=22 collisions at depth 34;
- MATH-038: q=23 layer at depth 35 contains five inherited plus fifteen new events;
- MATH-039: q=24 layer at depth 36 contains twenty inherited plus ten new events.

This does **not** yet establish a global recurrence for all q layers or arbitrary depth. It does show that the event language can be audited without retaining every full Hensel class in one monolithic memory object.

## 5. DSD interpretation

- `D`: collision-event state and parent source are explicitly represented.
- `R`: exact depth 36, q=24, residue modulo `3^24`.
- `S`: only depth-35 q=23 and q=24 coefficient-surviving parents are generated because no other q can feed child q=24.
- `E`: partitioning changes storage only; no residue class is dropped.
- `T`: inherited same-source collision versus new cross-source merger is detected by source tags.
- `C`: 169,991,585 records collapse to 169,991,555 classes with exactly 30 multiplicity-2 collisions.
- `N`: `ESTABLISHED_WITHIN q=24 FINITE SCOPE`.
- `O`: sparse event engine survives the first external-memory scaling test.

## 6. Next target

At depth 37 the minimal coefficient-surviving q is 24. A direct partition run without sufficiently early selection pruning exceeded the execution limit and was discarded. Even after early q-range pruning, the one-shot 258M-record q=24 child job remained too large for the current single-run budget.

The next implementation step should split the depth-37 q=24 cross-layer calculation into independently auditable residue super-buckets or use a two-pass parent-class representation, rather than reverting to the full symbolic DP.

## Prohibited upgrades

- q=24 layer closed ⇒ full depth-36 Hensel set closed — **PROHIBITED**.
- event counts 5→20→30 ⇒ asymptotic recurrence — **PROHIBITED**.
- partitioned exact finite computation ⇒ universal theorem — **PROHIBITED**.
- event existence ⇒ candidate exclusion without positive-credit audit — **PROHIBITED**.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth36_q24_partition_certificate.cpp`

Certificate commit:

`0a8e40dc2bffd978f8020edefc590b949608ad83`
