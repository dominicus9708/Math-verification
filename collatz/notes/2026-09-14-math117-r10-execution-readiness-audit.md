# MATH-117 — r=10 exact execution-readiness audit

Status: `MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=10 CLOSURE CLAIM`

Date: 2026-09-14

## Purpose

The MATH-111 `r=12` and MATH-116 `r=11` workflows are currently GitHub Actions runner-queued. MATH-117 advances the proof engineering without adding more runnable jobs to that queue: it freezes the exact `r=10` inputs, checks the MATH-114 representation against the MATH-108 engine's actual resource semantics, and prepares a manually-dispatched closure workflow.

## Frozen r=10 workload

From the MATH-113 exact workload audit and the assertion-backed MATH-115 generic exporter:

```text
classification:             994 total
safe:                        91
singleton:                  396
critical:                   507
branch-and-bound nodes: 1,994,258
AP source cylinders:       278,725
represented occurrence mass: 27,557,263,803,397
max unsplit multiplicity:      830,483,089,363
```

## Exact MATH-114 128-way representation

```text
source records:       278,725
exact split pieces:   278,739
piece cap:             215,291,123,465
min shard mass:        215,291,123,463
max shard mass:        215,291,123,465
min pieces/shard:      1
max pieces/shard:      2,448
u64 per-shard safe:    yes
```

The split adds only 14 pieces relative to the unsplit source-record count. This is an exact consecutive-parameter partition, not pruning.

## Engine-resource audit

The unchanged MATH-108 engine does **not** iterate once per represented ordinary occurrence. For each AP record, one `advance` emits at most the two parity subsequences `rho=0,1`. Resource overflow is keyed to the number of AP/singleton state records against `STATE_CAP = 1,000,000`, not directly to AP multiplicity mass.

If a state becomes too large, the engine exactly bisects either:

1. the original source-record list; or
2. a single AP parameter interval.

The acceptance invariant is additive occurrence mass, not raw partition-record count.

Therefore the approximately 8.06x larger total occurrence mass of `r=10` relative to `r=11` does **not** imply approximately 8.06x runtime. Conversely, no runtime improvement is claimed: closure depth and intermediate state expansion remain empirical execution properties.

The source-side representation is favorable in record-count terms:

```text
r=11 exact split pieces: 605,977
r=10 exact split pieces: 278,739
r=11 max pieces/shard:   4,931
r=10 max pieces/shard:   2,448
```

This supports execution readiness but is not a closure theorem.

## Acceptance gate for future execution

`r=10` may be promoted to `CLOSED` only if a later execution verifies all of:

1. MATH-115 exporter reproduces the frozen MATH-113 `r=10` totals;
2. MATH-114/115 preparation reproduces the exact 128-way partition above;
3. all 128 shards execute the unchanged MATH-108 engine;
4. every shard reports `PASS generalized exact AP-union audit`;
5. total source occurrence mass is exactly `27,557,263,803,397`;
6. any job/resource failure is audited before mathematical interpretation.

## Claim boundary

Current theorem state is unchanged:

```text
r>=13 CLOSED
r=12 OPEN
r=11 OPEN
r=10 OPEN — execution-ready, not launched
r=2..9 OPEN
First universal Farey cell OPEN
Collatz conjecture OPEN
```
