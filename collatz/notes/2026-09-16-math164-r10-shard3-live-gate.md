# MATH-164 — original r=10 shard 3 exact microclosure gate

Date: 2026-09-16

Status: MAINLINE / RUNNING / NO ORIGINAL-SHARD CLOSURE CLAIM YET

## Structural role

Original shards `0..2` are independently certified members of the giant boundary family with step `3^19`. Original shard 3 is the first frozen MATH-114 giant AP with the distinct step

```text
3^20 = 3,486,784,401.
```

MATH-164 is therefore the first independent execution gate for the `3^20` giant family. Success on shards `0..2` is not transferred by analogy.

## Exact source and launch

```text
original shard           3
source start             3029143697738121110222
source step              3486784401 = 3^20
source occurrence mass   215291123465
microshards              64
workflow run             35015125184
source artifact          10414579719
```

Preparation job `104536517400` passed exact r=10 source regeneration, original shard-3 identity audit, MATH-156 exact 64-way microsharding, and source preservation.

The micro mass certificate is

```text
215291123465 = 9 * 3363923805 + 55 * 3363923804.
```

Every micro retains exact step `3486784401`. Each is audited by unchanged MATH-108 with explicit `source_chunk=1`.

Original shard 3 may be promoted to CLOSED only if all 64 micro jobs PASS and the dependent `certify-original-shard3` job verifies complete exact coverage and total mass `215291123465`.

Current claim:

```text
ORIGINAL r=10 SHARD 3  OPEN — MATH-164 running
r=10 LAYER             OPEN
First universal cell   OPEN
Collatz conjecture      OPEN
```
