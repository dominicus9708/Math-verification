# MATH-151 — `r=3` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=3 CLOSURE CLAIM`

## Frozen exact workload

```text
classification                944 = 9 safe + 152 singleton + 783 critical
branch-and-bound nodes        12,133
AP source cylinders           1,873
represented occurrence mass  13,093,636,650,601,823,230
maximum multiplicity          1,816,563,049,738,599,228
```

The full occurrence mass still fits unsigned 64-bit, as does the maximum unsplit multiplicity.

## Exact 128-way mass-balanced representation

```text
source records                1,873
split pieces                  1,972
only additional pieces        99
128-shard cap                 102,294,036,332,826,744
minimum shard mass            102,285,013,362,167,651
maximum shard mass            102,424,247,400,287,058
maximum pieces per shard      72
```

Every split-piece multiplicity and shard-local mass fits `uint64_t`, so the unchanged MATH-108 exact AP-union engine remains representation-compatible.

## Resource bound

By MATH-148,

```text
ceil(102294036332826744 / 2^37) = 744288 < 1000000 = STATE_CAP.
```

Thus after isolation, at most 37 exact parameter-half bisections eliminate a pure state-record-cap obstruction. The separate `MAX_DEPTH = 1000` closure obligation remains empirical.

## Claim boundary

This is an exact execution preflight only. It does not prove `r=3 CLOSED`, paid-layer coverage, first-cell emptiness, or the Collatz conjecture.

## Execution policy

Keep the workflow manual-only and unlaunched while higher frontier layers are running.
