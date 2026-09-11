# MATH-069 — exact closure of the r=16 layer by hybrid AP / ordinary-state union

Date: 2026-09-11

Status: `EXACT r=16 CLOSURE / r>=16 CLOSED / r<=15 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-068 closes `r=17`.
- This note applies the same ordinary-target equality principle to `r=16`, but separates multiplicity bands because a single all-purpose AP representation causes avoidable state explosion.

## 1. Exact r=16 branch workload

The unchanged MATH-065 phase/dyadic branch-and-bound at `r=16` gives

\[
\boxed{
1061=229\text{ cost-safe}+557\text{ singleton-only}+275\text{ critical cells}.
}
\]

The exact branch traversal visits

\[
\boxed{37\,173\,746}
\]

states and leaves

\[
\boxed{2\,417\,129}
\]

completed negative-candidate AP cylinders representing, with lineage multiplicity,

\[
\boxed{213\,006\,896}
\]

ordinary target occurrences.

This count is far too large for ordinary target materialization, but it is not the size of the future dynamical state after exact equality merging.

## 2. Why one global representation is inefficient

Putting every multiplicity into one AP sorting structure causes an intermediate representation peak above nine million states around depth 10--16.

This is a computational representation problem, not a mathematical obstruction.

The correct hybrid representation is:

- non-singleton ordinary target sets: exact finite AP intervals;
- singleton ordinary targets: canonical integer values only.

Singletons are deduplicated by integer equality rather than sent through the more expensive AP-grid sort.

## 3. Band partition

The exact completed workload partitions as

| multiplicity band | raw cylinders | lineage-counted occurrences |
|---:|---:|---:|
| `m<=64` | 2,238,071 | 12,763,331 |
| `65<=m<=1023` | 154,255 | 39,692,496 |
| `m>=1024` | 24,803 | 160,551,069 |

The three rows sum exactly to the full MATH-069 workload.

The partition is computational only.  Every band is audited by the same exact ordinary-target dynamics.

## 4. Small band: m<=64

Exact same-grid AP union plus singleton equality merge gives the initial normalized state

\[
\boxed{898\,392\text{ non-singleton APs}+612\,619\text{ singleton integers}}
\]

representing a summed multiplicity

\[
\boxed{10\,471\,444}.
\]

By depth 6 every unresolved state is an ordinary singleton.

The unique last survivor above the frozen floor at depth 325 is

\[
\boxed{4\,078\,779\,061\,073\,975\,415\,814>2^{71}}.
\]

Its next shortcut value is

\[
\boxed{2\,039\,389\,530\,536\,987\,707\,907<2^{71}}.
\]

Therefore

\[
\boxed{m\le64\text{ closes within at most }326\text{ additional shortcut steps}.}
\]

## 5. Medium band: 65<=m<=1023

The raw band

\[
154\,255\text{ APs},\qquad39\,692\,496\text{ occurrences}
\]

normalizes by exact grid union to

\[
\boxed{136\,542\text{ APs}}
\]

with summed represented multiplicity

\[
\boxed{35\,768\,873}.
\]

At depth 11 every unresolved state is singleton.

The last value above the frozen floor at depth 313 is

\[
\boxed{2\,844\,034\,437\,459\,965\,374\,174>2^{71}},
\]

and its next value is

\[
\boxed{1\,422\,017\,218\,729\,982\,687\,087<2^{71}}.
\]

Hence

\[
\boxed{65\le m\le1023\text{ closes within }314\text{ steps}.}
\]

## 6. Large band: m>=1024

The raw band

\[
24\,803\text{ APs},\qquad160\,551\,069\text{ occurrences}
\]

normalizes to

\[
\boxed{23\,103\text{ APs}}
\]

with summed represented multiplicity

\[
\boxed{155\,249\,446}.
\]

The last above-floor value at depth 346 is

\[
\boxed{2\,401\,457\,543\,131\,136\,922\,308>2^{71}}.
\]

The next value is

\[
\boxed{1\,200\,728\,771\,565\,568\,461\,154<2^{71}}.
\]

Therefore

\[
\boxed{m\ge1024\text{ closes within }347\text{ steps}.}
\]

This is the longest of the three r=16 bands.

## 7. r=16 verdict

Every completed negative-candidate target in every multiplicity band reaches the frozen verification floor.

Thus

\[
\boxed{r=16\text{ is closed for the current first-cell minimal-counterexample calculation}.}
\]

Combining MATH-065, MATH-068, and MATH-069 gives

\[
\boxed{r\ge16\text{ is closed}.}
\]

The remaining detailed multi-paid frontier is now

\[
\boxed{2\le r\le15.}
\]

## 8. DSD audit

### SAFE

1. MATH-065 exact dyadic lineage is retained until each macro completes.
2. After completion, only literal ordinary-target set equality is used for merging.
3. Non-singleton APs merge only on identical grids and overlapping/adjacent parameter intervals.
4. Singleton states merge only by integer equality.
5. Every shortcut transition is exact.
6. A state is removed only when its ordinary value is at or below the frozen published floor.
7. All three multiplicity bands close; therefore the entire `r=16` layer closes.

### OPEN

- `2<=r<=15`;
- the complete mixed one-paid / multi-paid Bellman problem;
- first universal cell emptiness;
- later Farey cells;
- Collatz conjecture.

### PROHIBITED UPGRADES

- computational band partition `=>` a mathematical distinction among multiplicities;
- `r>=16` closure `=>` first-cell closure;
- ordinary-target equality merge `=>` pre-completion symbolic states may be merged.

## 9. Reproducibility

Stage A — exact branch export:

`collatz/src/2026_09_11_math069_r16_leaf_export.py`

Stage B — hybrid AP/singleton union and descent:

`collatz/src/2026_09_11_math069_r16_hybrid_union_engine.cpp`

A typical run is

```text
python 2026_09_11_math069_r16_leaf_export.py | ./math069_r16_hybrid_union_engine
```

The C++ engine uses explicit overflow guards on every fixed-width arithmetic operation; an overflow risk aborts rather than silently wrapping.
