# MATH-098 — one-paid macro depth 15 closed by root-sharded compact carry

Date: 2026-09-13

Status: `EXACT FINITE t=15 BELLMAN CLOSURE / ONE-PAID FRONTIER 7<=t<=14`

## 1. Why root sharding is used

A single Python set of all depth-15 danger-corridor carry states is a poor representation because the state count becomes large even though every initial danger root can be verified independently.

MATH-098 therefore keeps the exact MATH-096 compact state but partitions the computation by the 84 actual first-macro danger roots.  Each root is carried independently to macro depth 14 and its possible depth-15 danger edges are tested.

Cross-root deduplication is deliberately omitted.  If two roots later represent the same compact state, that state is simply checked twice.  This can add work but cannot remove a candidate.

## 2. Exact phase-danger automaton

Stage A uses the address-forgotten MATH-086 lower-envelope language to construct the backward phase corridor leading to a negative depth-15 terminal crossing.  It then restores the actual first-macro states intersecting that corridor.

The exact number of initial compact danger roots is

\[
\boxed{84}.
\]

Only phase-state transitions remaining inside the backward corridor are exported to the binary verifier.

## 3. Compact carry state

Each state uses

\[
R=\lceil\log_2 M\rceil,
\qquad
P=73+R,
\]

\[
X=3^{-Q}B\pmod{2^P},
\qquad
G=3^{-Q}\pmod{2^P},
\]

plus exact source multiplicity `M`, accumulated source-modulus depth `H`, and a phase-state identifier.

MATH-096 proves that this precision is sufficient for the entire remaining one-paid future, and MATH-092 gives the exact transition.

## 4. Universal terminal threshold

Every one-paid macro pays strictly more than `1/9`.  Therefore a 15-macro chain has

\[
\mathcal P>\frac{15}{9}.
\]

A negative terminal after the resolution potential would require

\[
\frac{15}{9}-\frac{19}{503}z<0.
\]

Since

\[
44<\frac{15/9}{19/503}=\frac{7545}{171}<45,
\]

only terminal edges with

\[
\boxed{z=h-R\ge45}
\]

need exact address testing.

## 5. Complete shard result

All 84 roots were processed independently.  The aggregated number of phase-compatible terminal edge attempts satisfying `z>=45` is

\[
\boxed{145,075,745}.
\]

The number satisfying exact same-integer compatibility

\[
r<M
\]

is

\[
\boxed{0}.
\]

The smallest strict residue gap over all nonempty shards is

\[
\boxed{r-M=25,366,468>0}.
\]

For reproducibility diagnostics, the sum of terminal-parent occurrences across root shards is

\[
\boxed{7,165,074},
\]

where cross-root duplicates are intentionally counted more than once.  The largest within-shard compact-state population observed at any intermediate level is

\[
\boxed{3,707,240}.
\]

Of the 84 root shards, 72 reach at least one final danger-edge attempt and 12 die before the terminal scan.

## 6. Verdict

No same-integer terminal at macro depth 15 can realize a Bellman-negative edge that escapes the universal `1/9` penalty lower bound.

Hence

\[
\boxed{t=15\text{ is Bellman-safe}.}
\]

Combining MATH-097 and the earlier high-depth certificates, the unresolved detailed one-paid macro-depth band becomes

\[
\boxed{7\le t\le14.}
\]

This is not an ordinary Collatz descent theorem and does not by itself close the first universal Farey cell.

## Reproducibility

Stage A:

`collatz/src/2026_09_13_math098_t15_phase_automaton_export.py`

Stage B:

`collatz/src/2026_09_13_math098_t15_compact_carry_shard.cpp`
