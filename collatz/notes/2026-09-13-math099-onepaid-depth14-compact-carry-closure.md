# MATH-099 — one-paid macro depth 14 closed by root-sharded compact carry

Date: 2026-09-13

Status: `EXACT FINITE t=14 BELLMAN CLOSURE / ONE-PAID FRONTIER 7<=t<=13`

## 1. Architecture

MATH-099 repeats the audited MATH-098 architecture one macro earlier:

1. build the address-forgotten lower-envelope backward phase corridor for a negative depth-14 terminal;
2. restore every actual first-macro compact state intersecting that corridor;
3. process each first root independently with the MATH-096 state
   \((H,M,X,G,\text{phase-id})\);
4. test only terminal edges that can still defeat the universal `p>1/9` lower bound.

There are

\[
\boxed{125}
\]

actual first-macro danger roots.  Cross-root deduplication is intentionally omitted; overlap can duplicate verification but cannot remove a path.

## 2. Universal terminal threshold

At macro depth 14,

\[
\mathcal P>\frac{14}{9}.
\]

A Bellman-negative terminal with overshoot `z=h-R` would require

\[
\frac{14}{9}-\frac{19}{503}z<0.
\]

Since

\[
41<\frac{14/9}{19/503}=\frac{7042}{171}<42,
\]

only

\[
\boxed{z\ge42}
\]

needs exact address testing.

## 3. Complete finite result

All 125 root shards were processed independently.

The aggregate number of phase-compatible terminal danger-edge attempts with `z>=42` is

\[
\boxed{343,241,144}.
\]

The number satisfying exact same-integer address compatibility

\[
r<M
\]

is

\[
\boxed{0}.
\]

The global minimum strict residue gap is

\[
\boxed{r-M=4,352,816>0}.
\]

For resource diagnostics only, the sum of terminal-parent occurrences across independent root shards is

\[
\boxed{15,560,039},
\]

where cross-root duplicates may be counted repeatedly.  The largest compact-state population inside one shard is

\[
\boxed{5,957,209}.
\]

Of the 125 root shards, 102 reach at least one final danger-edge attempt and 23 die before the terminal scan.

## 4. Verdict

No actual same-integer depth-14 terminal can realize a negative Bellman edge that escapes the universal one-paid penalty lower bound.

Hence

\[
\boxed{t=14\text{ is Bellman-safe}.}
\]

The remaining detailed one-paid macro-depth band is now

\[
\boxed{7\le t\le13.}
\]

This remains a first-cell Bellman subproblem; it is not by itself an ordinary Collatz descent theorem or a proof of the full conjecture.

## Reproducibility

Stage A:

`collatz/src/2026_09_13_math099_t14_phase_automaton_export.py`

Stage B:

`collatz/src/2026_09_13_math099_t14_compact_carry_shard.cpp`
