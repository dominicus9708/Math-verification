# MATH-101 — one-paid macro depth 12 compact-carry closure

Date: 2026-09-13

Status: `EXACT FINITE t=12 CLOSURE / ONE-PAID FRONTIER 7<=t<=11 OPEN`

Every one-paid macro has `p>1/9`. For `t=12`, any negative terminal reduced cost must satisfy

\[
\frac{12}{9}-\frac{19}{503}z<0,
\qquad\Rightarrow\qquad
\boxed{z=h-R\ge36}.
\]

The exact address-forgotten phase-danger automaton contains `193` actual initial danger roots. Each root is then replayed independently with the MATH-096/097 compact same-integer state

\[
(M,\ X\bmod2^{73+R},\ G=3^{-Q}\bmod2^{73+R}),
\qquad R=\lceil\log_2M\rceil.
\]

Across all 193 independent exact root shards:

- phase-compatible terminal danger-edge attempts with `z>=36`: `886,709,993`;
- address-compatible danger edges: `0`;
- terminal-parent occurrences: `34,377,245`;
- largest within-root compact-state peak: `7,960,428`;
- global minimum rejected residue gap: `1,794`.

Hence every phase-danger terminal edge fails exact same-integer address compatibility, and

\[
\boxed{t=12\text{ CLOSED}}.
\]

The detailed unresolved one-paid band is now

\[
\boxed{7\le t\le11}.
\]

Reproducibility:

- `collatz/src/2026_09_13_math101_t12_phase_automaton_export.py`
- `collatz/src/2026_09_13_math101_t12_compact_carry_shard.cpp`

This is a finite Bellman/address closure only; it is not first-cell closure, paid-count `r=12` closure, or a proof of Collatz.
