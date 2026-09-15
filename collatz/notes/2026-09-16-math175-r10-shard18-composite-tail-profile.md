# MATH-175 — r=10 shard18 composite-tail static profile

Date: 2026-09-16

## Classification

`SIDE / SUPPORT ONLY`

This audit profiles the first MATH-161 composite tail, subshards `47..63`, using the exact preserved recursive64 source artifact. It does not execute MATH-108 and does not close shard 18, r=10, the first universal cell, or Collatz.

## Live boundary at the time of profiling

The complete single-AP front `0..46` had already passed unchanged MATH-108. Its certified partial occurrence mass is

```text
158,104,418,835 / 215,291,123,464
≈ 73.4375000191%
```

This is partial exact closure only. Original shard 18 remains OPEN until all 64 subshards and the final original-shard certificate pass.

## Composite-tail geometry

For subshards `47..63`:

```text
pieces/job              136 .. 146
mass/job          3,363,923,801 .. 3,363,923,802
small AP rows m<=1e6   121 .. 123
singleton AP rows        15 .. 16
step exponents            21 .. 49   (every odd step is an exact power of 3)
```

The front is highly skewed rather than uniformly heavy. In subshard 47, one AP has multiplicity

```text
3,302,008,528
```

which is about `98.1594%` of the whole subshard mass. The dominant-AP share then decreases through the tail, reaching about `32.7198%` in subshard 63.

## Pure STATE_CAP depth descriptor

Using the same finite state-count interpretation as MATH-148, define for one input AP multiplicity `m`

```text
d(m) = min d >= 0 such that ceil(m / 2^d) <= 1,000,000.
```

The maximum descriptor over each composite subshard is

```text
47..52 : dmax = 12
53..63 : dmax = 11
```

This is only a sufficient pure state-count partition depth. It is not a wall-time prediction and does not replace unchanged MATH-108 execution.

Under the MATH-171 recursive256 source cap

```text
m <= 840,980,952,
```

the same descriptor is uniformly at most

```text
dmax <= 10.
```

Hence the exact 256-way fallback removes at least two pure multiplicity-bisection levels from the heaviest `47..52` inputs and at least one from `53..63`, before any trajectory-specific merging or splitting behavior is considered.

## Why composite-tail execution is not 136–146 coupled APs

MATH-174 audited unchanged MATH-108 with `source_chunk=1`: every input AP row is sent to a separate `audit()` call and the chunk is cleared before the next row. Therefore a 136-piece composite job is 136 independent exact AP audits executed sequentially inside one GitHub job, not one 136-AP coupled dynamical state.

The practical resource risk is therefore the sum of independent per-AP runtimes, with the largest AP often dominating the first tail jobs.

## Exact table

Recorded at

```text
collatz/results/2026-09-16-math175-r10-shard18-composite-tail-profile.tsv
```

Reproducer:

```text
collatz/src/2026_09_16_math175_r10_shard18_composite_tail_profile.py
```

## Scheduling consequence

The policy remains selective escalation:

```text
healthy recursive64 composite job
    -> keep running unchanged

resource timeout with no mathematical FAIL
    -> rerun that original shard through exact recursive256 fallback

unexecuted fallback
    -> no closure claim
```

MATH-175 strengthens only the resource rationale for that fallback. It makes no theorem-facing closure claim.
