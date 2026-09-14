# MATH-150 — `r=4` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=4 CLOSURE CLAIM`

## Frozen exact workload

```text
classification                944 = 14 safe + 172 singleton + 758 critical
branch-and-bound nodes        23,058
AP source cylinders           3,675
represented occurrence mass  1,845,330,088,960,999,169
maximum multiplicity          227,070,381,217,324,903
```

## Exact 128-way mass-balanced representation

```text
source records                3,675
split pieces                  3,761
only additional pieces        86
128-shard cap                 14,416,641,320,007,807
minimum shard mass            14,416,641,320,007,803
maximum shard mass            14,416,641,320,007,807
maximum pieces per shard      93
```

All split-piece multiplicities and shard-local masses fit `uint64_t`, so the unchanged MATH-108 exact AP-union engine remains representation-compatible.

## Resource bound

By MATH-148,

```text
ceil(14416641320007807 / 2^34) = 839159 < 1000000 = STATE_CAP.
```

Thus after isolation, at most 34 exact parameter-half bisections eliminate a pure state-record-cap obstruction. The separate `MAX_DEPTH = 1000` closure obligation remains.

## Claim boundary

This is an exact execution preflight only. It does not prove `r=4 CLOSED`, paid-layer coverage, first-cell emptiness, or the Collatz conjecture.

## Execution policy

Keep the workflow manual-only and unlaunched while higher frontier layers are running.
