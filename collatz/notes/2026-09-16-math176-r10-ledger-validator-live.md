# MATH-176 — permanent r=10 original-shard ledger validator

Date: 2026-09-16

Status: SUPPORT / REPRODUCIBILITY INFRASTRUCTURE / PARTIAL LEDGER AUDIT PASS / NO r=10 LAYER CLOSURE CLAIM

## Implemented files

```text
collatz/src/2026_09_16_math176_r10_original_shard_ledger_validator.py
collatz/results/2026-09-16-math176-r10-original-shard-ledger.tsv
.github/workflows/collatz-math176-r10-original-shard-ledger-audit.yml
```

The validator does not reimplement the r=10 arithmetic. It invokes the canonical MATH-115 r=10 exporter and MATH-114 128-way mass-balanced partitioner, reconstructs the frozen original-shard masses, and compares the permanent CLOSED ledger against that exact source.

For each ledger row it requires:

1. original shard ID in `0..127`;
2. no duplicate shard ID;
3. `status=CLOSED`;
4. valid MATH identifier and workflow run ID;
5. ledger certified mass exactly equal to regenerated MATH-114 shard mass;
6. permanent certificate note present in the repository.

`--require-complete` additionally requires the exact ID set `0..127` and total certified mass `27,557,263,803,397`. Without that flag, a valid partial ledger emits only a PARTIAL pass and explicitly makes no r=10 layer-closure claim.

## First live audit

Workflow run `35042686972`, job `104625729723`, completed with `success`.

The audited permanent CLOSED set is:

```text
{0,1,2,3,18}
```

Count and certified mass:

```text
closed original shards   5 / 128
certified closed mass    1,076,455,617,324
r=10 layer               OPEN
```

This closes a bookkeeping/reproducibility obligation only. It does not replace any original-shard closure certificate and does not promote r=10, the first universal cell, or the Collatz conjecture.
