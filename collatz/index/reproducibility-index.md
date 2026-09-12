# Reproducibility and certificate index

GitHub raw notes, source files, result tables, and commit history are the authoritative calculation record. This file is a proof-facing map, not a replacement for the certificates.

## Active / recent chain

| Date | ID | Role | Main reproducibility artifact(s) | Current status |
|---|---|---|---|---|
| 2026-09-11 | MATH-058 | paid-macro transition bound | `collatz/src/2026_09_11_paid_macro_transition_certificate.py`; `collatz/results/2026-09-11-paid-macro-transition-boundary.tsv` | exact historical pivot |
| 2026-09-12 | MATH-090 | dyadic carry-valuation compatibility | MATH-090 note/certificate in `collatz/` | mainline input |
| 2026-09-12 | MATH-091 | exact carry-transfer transducer | `collatz/notes/2026-09-12-math091-carry-transfer-transducer.md` | mainline reformulation |
| 2026-09-12 | MATH-092 | normalized 2-adic address transducer | MATH-092 note/source | mainline input |
| 2026-09-12 | MATH-093 | dyadic resolution envelope | MATH-093 note/source | mainline support |
| 2026-09-12/13 | MATH-094 | saturated danger kernel | MATH-094 note/source | exact negative barrier |
| 2026-09-13 | MATH-095 | phase-resolution Bellman negative result | `collatz/src/2026_09_12_math095_phase_resolution_bellman_value_certificate.py` | exact negative barrier |
| 2026-09-13 | MATH-096 | finite future precision | `collatz/src/2026_09_13_math096_hensel_quotient_precision_certificate.py` | mainline |
| 2026-09-13 | MATH-097 | `t=16` compact-carry closure | `collatz/src/2026_09_13_math097_onepaid_depth16_compact_carry_closure.py` | CLOSED |
| 2026-09-13 | MATH-098 | `t=15` compact-carry closure | MATH-098 exporter/verifier in `collatz/src/` | CLOSED |
| 2026-09-13 | MATH-099 | `t=14` compact-carry closure | MATH-099 exporter/verifier in `collatz/src/` | CLOSED |
| 2026-09-13 | MATH-100 | `t=13` compact-carry closure | `collatz/src/2026_09_13_math100_t13_phase_automaton_export.py`; `collatz/src/2026_09_13_math100_t13_compact_carry_shard.cpp` | CLOSED |
| 2026-09-13 | MATH-101 | `t=12` compact-carry closure | `collatz/src/2026_09_13_math101_t12_phase_automaton_export.py`; `collatz/src/2026_09_13_math101_t12_compact_carry_shard.cpp` | CLOSED |
| 2026-09-13 | MATH-102 | `t=11` compact-carry closure | `collatz/src/2026_09_13_math102_t11_phase_automaton_export.py`; `collatz/src/2026_09_13_math102_generic_compact_carry_shard.cpp` | CLOSED |
| 2026-09-13 | MATH-103 | `t=10` compact-carry closure | `collatz/src/2026_09_13_math103_t10_phase_automaton_export.py`; MATH-102 generic verifier with `PREFIX=t10`, `TARGET=10`, `ZMIN=30` | CLOSED |

Where a precise source filename is not repeated in this index, the corresponding dated MATH note is the authoritative pointer. Do not invent a filename from an ID when the exact repository path has not been verified.

## Finite closure audit figures

| ID | Macro depth | Necessary danger threshold | Danger-edge attempts | Address-compatible danger edges | Minimum rejected residue gap |
|---|---:|---:|---:|---:|---:|
| MATH-097 | 16 | `z>=48` | 45,094,414 | 0 | 197,239,627 |
| MATH-100 | 13 | `z>=39` | 622,022,028 | 0 | 83,441 |
| MATH-101 | 12 | `z>=36` | 886,709,993 | 0 | 1,794 |
| MATH-102 | 11 | `z>=33` | 991,302,455 | 0 | 514 |
| MATH-103 | 10 | `z>=30` | 882,659,777 | 0 | 548 |

The detailed totals for MATH-098 and MATH-099 remain in their original certificates. This index intentionally does not reconstruct unverified numbers from memory.

## Structural identities currently reused

### MATH-091 carry transfer

For current family

```text
Y' = B + 3^Q s,  0 <= s < M,
```

compatibility with a next edge gives residue `r`, exact carry `d`, and child family `(B',Q',M')`. This is the exact iterative same-integer channel.

### MATH-096 normalized Hensel quotient

For exact composed cylinder

```text
Y  = A + 2^H s
Y' = B + 3^Q s
2^H B = 3^Q A + C
S = C / 3^Q
X = 3^{-Q} B = (A+S)/2^H.
```

For `R=ceil(log2 M)`, finite future precision is

```text
P(R) = 73 + R.
```

Thus all future one-paid address decisions can be reproduced from the finite normalized 2-adic state together with exact multiplicity/phase/depth metadata.

## Historical archive policy

The existing directories keep their original roles:

```text
collatz/
├─ notes/    # mathematical notes, status documents, proof claims
├─ src/      # executable certificates / generators / verifiers
├─ results/  # finite result tables and outputs
├─ wolfram/  # independent symbolic/computational cross-checks where present
└─ index/    # classification and dependency layer only
```

No historical artifact is moved or deleted merely because its proof status changes.

## New-result checklist

Every new proof-facing result should record:

1. calendar date;
2. MATH ID or historical artifact name;
3. exact claim scope;
4. direct predecessor/dependency;
5. note path;
6. source/certificate path;
7. result-file path when applicable;
8. exact arithmetic / approximation status;
9. finite domain or depth;
10. classification (`MAINLINE`, `SIDE`, `BARRIER`, `REDUNDANT`, `SUPERSEDED`, `RETIRED`);
11. whether a later result supersedes only the mechanism/status or the mathematical bound itself.

## Current next slot

Candidate next record: `MATH-104`, intended for one-paid macro depth `t=9` compact-carry closure **if and only if** that result is actually produced and committed.

Until then, `MATH-104` is a candidate label, not an established result.
