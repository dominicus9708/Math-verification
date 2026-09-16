# MATH-178 — cross-shard runtime non-portability

Date: 2026-09-16

Status: `SUPPORT / RESOURCE-SCHEDULING BARRIER / NO PROOF CLAIM`

## Scope

This note concerns only proof-neutral execution scheduling for exact MATH-108 jobs. It does not change the frozen Collatz source, exact AP partitions, closure criterion, theorem-facing state, or any mathematical claim.

## Finite exact counterexamples

The current exact runtime records already rule out two naive scheduling assumptions.

### 1. Occurrence mass alone does not determine measured closure geometry

The following exact jobs all have occurrence mass `3,363,923,805`, but their measured MATH-108 closure geometry differs:

```text
sample                 leaves  splits  max_depth  wall_seconds
MATH161 sub34              77      76        416      443.493
MATH164 shard3 micro4     128     127        421      298.106
MATH168 shard4 micro4      64      63        475      339.922484
MATH168 shard5 micro4      64      63        430      404.675691
```

Therefore the scalar occurrence mass is not a sufficient descriptor for the measured exact-engine workload on the observed audited jobs.

### 2. A prior giant shard's micro-index runtime order is not portable to the next giant shard

For original shards 4 and 5, micros `0..7` have the same occurrence mass and the same 64/63 closure-leaf/split count, but the measured runtime order changes substantially.

```text
micro   shard4 seconds   shard5 seconds
0       430.337160       378.894897
1       433.626896       379.898769
2       433.230444       377.953444
3       435.020778       208.326559
4       339.922484       404.675691
5       434.319327       387.154900
6       240.819767       398.356334
7       439.773596       398.428168
```

In shard 4, micro 6 is much cheaper than micro 3. In shard 5, micro 3 is much cheaper than micro 6. Thus the observed index ranking itself reverses across exact giant shards.

This is sufficient to reject the specific scheduling rule "reuse the previous giant shard's micro-index runtime ranking" as an exact reusable predictor.

## Consequence

The project must not treat either of the following as a certified scheduling model:

```text
predicted cost = f(occurrence mass only)
predicted cost = previous-shard runtime for the same micro index
```

A future resource predictor would need additional exact source information, for example start/address/residue geometry, and must be validated independently before it affects scheduling policy.

Until such a predictor exists, generic proof-neutral scheduling remains the safe default. Reordering jobs, if later used, may change only resource scheduling; it may not alter source coverage, exact partitions, the unchanged MATH-108 engine, or closure conditions.

## Claim boundary

MATH-178 is a finite resource-scheduling barrier supported by exact observed jobs. It does **not** claim a universal formula for runtime, does **not** prove that any particular residue variable is sufficient, and does **not** strengthen or weaken any Collatz closure result.
