# MATH-103 — one-paid macro depth 10 compact-carry closure

Date: 2026-09-13

Status: `EXACT FINITE t=10 CLOSURE / ONE-PAID FRONTIER 7<=t<=9 OPEN`

The universal one-paid bound `p>1/9` gives the necessary Bellman-danger condition

\[
\boxed{z=h-R\ge30}
\]

at `t=10`.

The exact phase-danger automaton yields `300` actual initial danger roots. Independent compact-carry replay of all roots gives:

- terminal danger-edge attempts with `z>=30`: `882,659,777`;
- address-compatible danger edges: `0`;
- terminal-parent occurrences: `30,581,400`;
- largest within-root compact-state peak: `5,537,363`;
- global minimum rejected residue gap: `548 > 0`.

Hence

\[
\boxed{t=10\text{ CLOSED}}.
\]

The detailed unresolved one-paid band is now

\[
\boxed{7\le t\le9}.
\]

Stage A: `collatz/src/2026_09_13_math103_t10_phase_automaton_export.py`.
Stage B: use `collatz/src/2026_09_13_math102_generic_compact_carry_shard.cpp` with `PREFIX=t10`, `TARGET=10`, `ZMIN=30`.

This is Bellman/address closure only, not paid-count `r=10`, first-cell emptiness, or a Collatz proof.
