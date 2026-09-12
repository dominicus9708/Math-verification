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
| 2026-09-13 | MATH-104 | `t=9` compact-carry closure | `collatz/src/2026_09_13_math104_106_t7_t9_phase_automaton_export.py --target 9`; generic verifier `PREFIX=t9 TARGET=9 ZMIN=27` | CLOSED |
| 2026-09-13 | MATH-105 | `t=8` compact-carry closure | same exporter `--target 8`; generic verifier `PREFIX=t8 TARGET=8 ZMIN=24` | CLOSED |
| 2026-09-13 | MATH-106 | `t=7` compact-carry closure and exact boundary audit | same exporter `--target 7`; generic verifier `PREFIX=t7 TARGET=7 ZMIN=21` | CLOSED; one rejected `r=M` boundary witness |

Where a precise source filename is not repeated in this index, the corresponding dated MATH note is the authoritative pointer. Do not invent a filename from an ID when the exact repository path has not been verified.

## MATH-103 regression gate before frontier extension

Before accepting MATH-104--106, the recreated exact stage-A/stage-B implementation was run again at `t=10`. It reproduced the existing MATH-103 totals exactly:

- danger-edge attempts: `882,659,777`;
- address-compatible: `0`;
- terminal-parent occurrences: `30,581,400`;
- peak compact-state count within one root: `5,537,363`;
- minimum rejected residue gap: `548`.

This regression is an implementation-continuity check; it does not enlarge the theorem scope.

## Finite closure audit figures

| ID | Macro depth | Necessary danger threshold | Actual danger roots | Danger-edge attempts | Address-compatible danger edges | Terminal-parent occurrences | Peak | Minimum rejected residue gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| MATH-097 | 16 | `z>=48` | — | 45,094,414 | 0 | — | — | 197,239,627 |
| MATH-100 | 13 | `z>=39` | — | 622,022,028 | 0 | — | — | 83,441 |
| MATH-101 | 12 | `z>=36` | — | 886,709,993 | 0 | — | — | 1,794 |
| MATH-102 | 11 | `z>=33` | — | 991,302,455 | 0 | — | — | 514 |
| MATH-103 | 10 | `z>=30` | 300 | 882,659,777 | 0 | 30,581,400 | 5,537,363 | 548 |
| MATH-104 | 9 | `z>=27` | 373 | 628,901,495 | 0 | 20,807,725 | 3,272,272 | 7 |
| MATH-105 | 8 | `z>=24` | 428 | 358,489,331 | 0 | 11,364,281 | 1,526,834 | 30 |
| MATH-106 | 7 | `z>=21` | 486 | 161,189,096 | 0 | 4,943,726 | 555,399 | 0 (`r=M`, rejected) |

The detailed totals for MATH-098 and MATH-099 remain in their original certificates. This index intentionally does not reconstruct unverified numbers from memory.

The compact result table for the newly closed band is:

`collatz/results/2026-09-13-math104-106-onepaid-t7-t9-closure.tsv`.

## MATH-106 zero-gap boundary audit

The stage-B compatibility predicate is exactly `r < M`. For the single zero-gap boundary witness, `r-M=0`, hence `r=M`. This is the first excluded index immediately above the valid source-family range `0 <= r < M`; it is therefore rejected, not compatible. No terminal danger edge at `t=7` satisfies `r<M`.

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

The previously reserved MATH-104 slot is now occupied by the exact `t=9` closure, followed by MATH-105 (`t=8`) and MATH-106 (`t=7`).

No MATH-107 claim is assigned yet. The next step is first to isolate and audit the remaining paid-count layers and the complete first-cell implication chain. An ID should be assigned only after the exact next claim is stated.
