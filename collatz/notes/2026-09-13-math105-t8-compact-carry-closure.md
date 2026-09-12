# MATH-105 — one-paid macro depth 8 compact-carry closure

Date: 2026-09-13

Status: `EXACT FINITE t=8 CLOSURE / ONE-PAID FRONTIER t=7 OPEN`

Using the same exact compact-carry/address state as MATH-096--104, the universal one-paid penalty floor `p>1/9` gives the necessary Bellman-danger condition

\[
\boxed{z=h-R\ge24}
\]

at `t=8`.

The exact phase-danger automaton yields:

- actual initial danger roots: `428`;
- phase-danger transitions: `41,916`;
- terminal phase rows: `35,844`;
- phase IDs: `155`.

Independent compact-carry replay of every root gives:

- terminal danger-edge attempts with `z>=24`: `358,489,331`;
- address-compatible danger edges: `0`;
- terminal-parent occurrences: `11,364,281`;
- largest within-root compact-state peak: `1,526,834`;
- global minimum rejected residue gap: `30 > 0`.

Hence

\[
\boxed{t=8\text{ CLOSED}}.
\]

The only remaining depth in the formerly unresolved detailed one-paid band is `t=7`.

Stage A: `collatz/src/2026_09_13_math104_106_t7_t9_phase_automaton_export.py --target 8`.

Stage B: `collatz/src/2026_09_13_math102_generic_compact_carry_shard.cpp` with `PREFIX=t8`, `TARGET=8`, `ZMIN=24`.

Summary totals: `collatz/results/2026-09-13-math104-106-onepaid-t7-t9-closure.tsv`.

This is Bellman/address closure of the audited one-paid depth only. It is not paid-count closure, first-cell emptiness, or a proof of the Collatz conjecture.
