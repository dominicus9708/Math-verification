# MATH-106 — one-paid macro depth 7 compact-carry closure

Date: 2026-09-13

Status: `EXACT FINITE t=7 CLOSURE / FORMERLY UNRESOLVED ONE-PAID BAND 7<=t<=9 CLOSED`

Using the same exact compact-carry/address state as MATH-096--105, the universal one-paid penalty floor `p>1/9` gives the necessary Bellman-danger condition

\[
\boxed{z=h-R\ge21}
\]

at `t=7`.

The exact phase-danger automaton yields:

- actual initial danger roots: `486`;
- phase-danger transitions: `42,151`;
- terminal phase rows: `39,121`;
- phase IDs: `155`.

Independent compact-carry replay of every root gives:

- terminal danger-edge attempts with `z>=21`: `161,189,096`;
- address-compatible danger edges: `0`;
- terminal-parent occurrences: `4,943,726`;
- largest within-root compact-state peak: `555,399`;
- global minimum rejected residue gap: `0`.

The zero gap is an exact boundary case, not a compatible edge.  The stage-B compatibility test is

\[
r<M.
\]

For the boundary witness the rejected residue satisfies exactly

\[
r=M,
\]

so it remains outside the source family.  Exactly one initial-root shard attains this zero rejected gap; no terminal danger edge satisfies `r<M`.

Therefore

\[
\boxed{t=7\text{ CLOSED}}.
\]

Together with MATH-104 and MATH-105, the previously unresolved detailed one-paid band

\[
7\le t\le9
\]

is closed on the audited Bellman/address criterion.

Stage A: `collatz/src/2026_09_13_math104_106_t7_t9_phase_automaton_export.py --target 7`.

Stage B: `collatz/src/2026_09_13_math102_generic_compact_carry_shard.cpp` with `PREFIX=t7`, `TARGET=7`, `ZMIN=21`.

Summary totals: `collatz/results/2026-09-13-math104-106-onepaid-t7-t9-closure.tsv`.

This does not close the remaining paid-count layers or the full implication chain for the first universal Farey cell.  The Collatz conjecture remains open.
