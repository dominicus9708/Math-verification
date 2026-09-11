# MATH-068 — exact closure of the r=17 medium core by global AP union

Date: 2026-09-11

Status: `EXACT r=17 CLOSURE / GLOBAL ORDINARY-TARGET UNION / r<=16 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-065 closes every multi-paid layer `r>=18`.
- MATH-067 leaves only the `r=17` multiplicity band `65<=m<=1023` open.

## 1. Starting exact workload

MATH-067 leaves

\[
\boxed{76\,866}
\]

negative-candidate arithmetic-progression cylinders representing, with lineage multiplicity,

\[
\boxed{14\,980\,075}
\]

ordinary target occurrences.

Each completed cylinder has the form

\[
P(a,b,m)=\{a+bk:0\le k<m\},
\]

where `b` is an odd power of `3`.

At this point the macro has already completed and its reduced-cost qualification has already been audited.  Future exclusion depends only on the ordinary integer targets.  Historical macro lineage may therefore be forgotten **only when two states represent the same ordinary target set**.

## 2. Exact set-union compression

For `m>1`, write

\[
a=r+bk_0,
\qquad 0\le r<b.
\]

Two APs with the same `(b,r)` live on the same integer grid.  Their parameter intervals can therefore be unioned exactly whenever they overlap or touch.

Applying only this identity to the initial medium core gives

\[
76\,866\text{ AP representations}
\longrightarrow
\boxed{70\,426}\text{ grid intervals}.
\]

The summed grid-interval multiplicity falls from

\[
14\,980\,075
\]

to

\[
\boxed{13\,995\,185}.
\]

The difference

\[
\boxed{984\,890}
\]

is duplicate/overlapping representation on identical grids, not a probabilistic reduction.

Cross-grid overlaps are not guessed at this stage.

## 3. AP semigroup under the shortcut map

Because `b` is odd, parameter parity fixes value parity.

For

\[
k=\rho+2s,
\qquad \rho\in\{0,1\},
\]

we have

\[
a+bk=(a+b\rho)+2bs.
\]

If the branch is even,

\[
\boxed{
T(a+bk)=\frac{a+b\rho}{2}+bs.
}
\]

If the branch is odd,

\[
\boxed{
T(a+bk)=\frac{3(a+b\rho)+1}{2}+3bs.
}
\]

Thus finite APs are closed under one exact shortcut step after at most a two-way parameter-parity split.

After each step the calculation:

1. removes the initial AP segment already at or below `2^71`;
2. performs both exact parity branches;
3. unions overlapping/adjacent intervals on identical `(b,r)` grids.

No member is sampled or discarded by density.

## 4. Singleton canonicalization

When `m=1`, the set

\[
P(a,b,1)=\{a\}
\]

contains no information about `b` relevant to its future Collatz orbit.

Therefore the exact canonical representation is

\[
\boxed{P(a,b,1)\equiv P(a,1,1).}
\]

This permits states from different macro/AP lineages that have reached the **same ordinary integer** to merge exactly.

This is not state compression by similarity.  It is literal equality of the future state.

By depth 10 every remaining AP has become a singleton.  After canonical equality merging the unresolved ordinary-integer set has size

\[
\boxed{1\,259\,308}.
\]

## 5. Exact descent checkpoints

The exact union evolution contains the following checkpoints.

| additional shortcut depth | states | represented multiplicity | singleton states |
|---:|---:|---:|---:|
| 0 | 70,426 | 13,995,185 | 0 |
| 1 | 140,852 | 13,995,185 | 0 |
| 2 | 145,410 | 7,208,877 | 0 |
| 10 | 1,259,308 | 1,259,308 | 1,259,308 |
| 120 | 1,929 | 1,929 | 1,929 |
| 307 | 2 | 2 | 2 |
| 315 | 1 | 1 | 1 |
| 333 | 1 | 1 | 1 |
| 334 | 1 | 1 | 1 |
| 335 | 0 | 0 | 0 |

The last survivor still above the frozen floor at depth 333 is

\[
\boxed{3\,359\,879\,092\,251\,977\,200\,580>2^{71}}.
\]

After one more shortcut step it is

\[
\boxed{1\,679\,939\,546\,125\,988\,600\,290<2^{71}}.
\]

Therefore the exact maximum additional shortcut length needed to **reach** the verified floor is

\[
\boxed{334}.
\]

The empty state at sweep 335 merely removes the value that already reached the floor at depth 334.

## 6. Independent representation cross-check

The calculation was run in two equivalent ways:

1. first perform the same-grid union `76,866 -> 70,426`, then propagate;
2. begin with all `76,866` raw APs and allow the first global union after one shortcut step.

Both calculations reach the same depth-1 state count and the same subsequent exact checkpoints, including the unique final tail and the depth-334 floor entry.

Hence the initial same-grid union is not responsible for the closure result.

## 7. r=17 verdict

MATH-067 already closes

\[
m\le64
\]

and

\[
m\ge1024.
\]

MATH-068 closes the only remaining band

\[
65\le m\le1023.
\]

Therefore

\[
\boxed{
r=17\text{ is closed for the current first-cell minimal-counterexample calculation.}
}
\]

Combining with MATH-065 gives

\[
\boxed{
r\ge17\text{ is closed.}
}
\]

The detailed multi-paid frontier is now

\[
\boxed{2\le r\le16.}
\]

## 8. DSD audit

### SAFE

- completed macro targets may be unioned by exact ordinary-integer set equality;
- same-grid interval union preserves every target;
- the AP shortcut formulas are exact;
- values at or below the frozen verification floor may be removed;
- singleton step normalization is safe because `P(a,b,1)` is literally the one-element set `{a}`;
- identical singleton integers have identical future Collatz trajectories and may be merged;
- all medium-core targets reach the frozen floor;
- together with MATH-067, the whole `r=17` layer is closed.

### OPEN

- `2<=r<=16` multi-paid layers;
- one-paid / remaining multi-paid mixed Bellman organization;
- first universal Farey cell emptiness;
- later Farey cells;
- full Collatz conjecture.

### PROHIBITED UPGRADES

- `r>=17` paid-layer closure `=>` first-cell closure;
- equality merging of completed ordinary targets `=>` arbitrary symbolic states may be merged;
- finite first-cell descent certificates `=>` a universal descent theorem for all positive integers.

## 9. Next target

Apply the same global target-union method to `r=16`.

The raw `r=16` branch-and-bound is already substantially larger, so the important object is no longer target occurrence count.  The next audit should measure how quickly the 2.4-million completed AP representations collapse under exact ordinary-target union before deciding whether a direct continuation or a stronger Bellman quotient is preferable.

## Reproducibility

`collatz/src/2026_09_11_math068_r17_global_ap_union_certificate.py`
