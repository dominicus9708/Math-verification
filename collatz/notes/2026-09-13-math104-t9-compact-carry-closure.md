# MATH-104 — one-paid macro depth 9 compact-carry closure

Date: 2026-09-13

Status: `EXACT FINITE t=9 CLOSURE / ONE-PAID FRONTIER 7<=t<=8 OPEN`

The universal one-paid penalty floor `p>1/9` gives the necessary Bellman-danger condition

\[
\boxed{z=h-R\ge27}
\]

at `t=9`.

Before extending below MATH-103, the recreated exact stage-A/stage-B implementation was regression-tested at `t=10` and reproduced all five MATH-103 audit totals exactly:

- attempts `882,659,777`;
- address-compatible `0`;
- terminal-parent occurrences `30,581,400`;
- maximum within-root compact-state peak `5,537,363`;
- minimum rejected residue gap `548`.

The exact `t=9` phase-danger automaton then yields:

- actual initial danger roots: `373`;
- phase-danger transitions: `39,902`;
- terminal phase rows: `32,732`;
- phase IDs: `155`.

Independent compact-carry replay of every root gives:

- terminal danger-edge attempts with `z>=27`: `628,901,495`;
- address-compatible danger edges: `0`;
- terminal-parent occurrences: `20,807,725`;
- largest within-root compact-state peak: `3,272,272`;
- global minimum rejected residue gap: `7 > 0`.

Hence

\[
\boxed{t=9\text{ CLOSED}}.
\]

The detailed unresolved one-paid band becomes

\[
\boxed{7\le t\le8}.
\]

Stage A: `collatz/src/2026_09_13_math104_106_t7_t9_phase_automaton_export.py --target 9`.

Stage B: `collatz/src/2026_09_13_math102_generic_compact_carry_shard.cpp` with `PREFIX=t9`, `TARGET=9`, `ZMIN=27`.

Summary totals: `collatz/results/2026-09-13-math104-106-onepaid-t7-t9-closure.tsv`.

This is Bellman/address closure of the audited one-paid depth only. It is not paid-count closure, first-cell emptiness, or a proof of the Collatz conjecture.
