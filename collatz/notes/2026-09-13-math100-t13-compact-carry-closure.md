# MATH-100 — one-paid macro depth 13 compact-carry closure

Date: 2026-09-13

Status: `EXACT FINITE t=13 CLOSURE / ONE-PAID FRONTIER 7<=t<=12 OPEN`

## 1. Scope

This certificate closes the remaining one-paid Bellman terminal candidates at macro depth

\[
\boxed{t=13}.
\]

It does not prove the Collatz conjecture, first-cell emptiness, or the paid-count layers `2<=r<=13`.

## 2. Danger threshold

Every one-paid macro contributes

\[
p>\frac19.
\]

For `t=13`, a negative terminal reduced cost therefore requires

\[
\frac{13}{9}-\frac{19}{503}z<0,
\]

hence the necessary integer condition

\[
\boxed{z=h-R\ge39}.
\]

Only terminal edges satisfying this condition are audited.

## 3. Exact state

For a multi-source family of size `M`, let

\[
R=\lceil\log_2M\rceil.
\]

MATH-096/097 allow the future-complete compact address state

\[
\boxed{
(M,\ X\bmod2^{73+R},\ G=3^{-Q}\bmod2^{73+R})
}
\]

together with accumulated source modulus depth and exact phase-cell ID.

Every multi-edge uses the exact MATH-092 normalized 2-adic transition. No probabilistic, density, or heuristic address pruning is used.

## 4. Phase-danger corridor

The exact address-forgotten lower-envelope backward corridor contains

- `157` actual initial danger roots;
- `22,868` phase-corridor transitions;
- `19,927` terminal phase-edge records;
- `155` phase IDs.

The 157 roots are processed as independent exact shards. Cross-root duplicates are intentionally not merged; this can only duplicate work.

## 5. Complete shard result

Summing all 157 root shards gives

\[
\boxed{622\,022\,028}
\]

phase-compatible terminal danger-edge attempts with `z>=39`.

Exact dyadic carry/address testing gives

\[
\boxed{0\text{ address-compatible danger edges}}.
\]

The total terminal-parent occurrence count across independent root shards is

\[
26\,061\,131,
\]

and the largest within-root compact-state peak is

\[
7\,256\,405.
\]

Among all rejected danger edges, the global minimum exact residue gap is

\[
\boxed{r-M=83\,441>0}.
\]

Therefore no phase-danger terminal edge is compatible with the same-integer source family.

## 6. Conclusion

\[
\boxed{t=13\text{ CLOSED}}.
\]

Together with the earlier results, the detailed unresolved one-paid macro-depth band is now

\[
\boxed{7\le t\le12}.
\]

## 7. Reproducibility

- stage A: `collatz/src/2026_09_13_math100_t13_phase_automaton_export.py`
- stage B: `collatz/src/2026_09_13_math100_t13_compact_carry_shard.cpp`

The stage-B verifier may be run root-by-root or on disjoint root ranges. Summing all 157 roots gives the totals above.
