# MATH-172 — shard 18 recursive256 offline geometry audit

Date: 2026-09-16

## Classification

`SIDE / SUPPORT ONLY`

This audit estimates and cross-checks the resource geometry of the prepared MATH-171 256-way fallback using the already preserved MATH-161 shard-18 recursive source artifact. It does not close shard 18 and it is not a substitute for a MATH-171 final certificate.

## Artifact-consistent source reconstruction

The MATH-161 artifact contains `2,491` exact AP pieces with total occurrence mass

```text
215,291,123,464
```

and recursive64 cap

```text
3,363,923,805.
```

For pieces having the same AP step, connect one piece to another only when the first piece's exact terminal parameter value equals the second piece's exact start:

```text
next_start = start + step * multiplicity.
```

On the preserved artifact this produces:

```text
continuity edges             47
ambiguous continuations       0
connected AP components    2,444
```

The component count exactly matches the independently certified original shard-18 source-record count `2,444`. The reconstructed union also reproduces:

```text
total mass              215,291,123,464
maximum multiplicity    116,786,684,442
```

This is strong artifact-consistency evidence for the split-accounting interpretation in MATH-170. Because the recursive artifact does not preserve original MATH-114 `source_i` labels, this audit does not claim recovery of the original source-record ordering.

## 256-way invariant split geometry

For the reconstructed exact AP set,

```text
cap256 = ceil(215,291,123,464 / 256)
       = 840,980,952.
```

Splitting every reconstructed source AP into consecutive parameter intervals of length at most `cap256` gives the following order-independent counts:

```text
original AP components          2,444
full-cap prefix pieces            222
terminal remainder pieces       2,444
all emitted pieces              2,666
source APs requiring a split       26
maximum pieces from one source    139
```

No reconstructed source multiplicity is an exact multiple of `840,980,952`, so every original source AP contributes exactly one non-cap terminal remainder.

The largest source AP satisfies

```text
116,786,684,442
  = 138 * 840,980,952 + 731,313,066.
```

Thus its 256-way representation consists of `138` full-cap prefixes plus one terminal remainder.

## Illustrative LPT packing

Applying the unchanged MATH-114 LPT rule to one deterministic ordering of the reconstructed components produced:

```text
subshard mass range       840,980,944 .. 840,980,952
mass spread               8
pieces/subshard            1 .. 74
```

These particular per-subshard identities and piece counts are scheduling estimates only. Original `source_i` ordering was not preserved in the MATH-161 artifact, and stable tie-breaking in MATH-114 may therefore assign equal-mass pieces to different shard numbers in an authoritative MATH-171 execution.

The invariant conclusions are the exact global mass, cap, total split-piece count, full-cap-prefix count, terminal-remainder count, and maximum source split count stated above.

## Interpretation

Relative to recursive64:

```text
64-way cap     3,363,923,805
256-way cap      840,980,952
```

so MATH-171 reduces the maximum certified occurrence mass per matrix workload to approximately one quarter while preserving the same exact AP union.

The fallback therefore addresses scheduling granularity only. It does not weaken MATH-108 closure conditions and cannot convert a timeout into mathematical evidence.

## Authoritative result table

```text
collatz/results/2026-09-16-math172-shard18-recursive256-geometry.tsv
```

## Claim boundary

MATH-172 closes no new ordinary-integer mass. Original shard 18 remains `OPEN` until MATH-161 or an independently complete fallback run finishes all required exact closures and its final original-shard certificate passes.
