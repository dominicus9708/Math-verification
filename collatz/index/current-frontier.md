# Current Collatz frontier after MATH-111 closure

Date: 2026-09-14

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=12                     CLOSED
Multi-paid r=11                      OPEN — MATH-116 exact closure running
Multi-paid r=10                      OPEN — MATH-117 execution-ready, not launched
Multi-paid 2<=r<=9                   OPEN
```

No finite layer closure is promoted to first-cell emptiness or to the Collatz conjecture without the separate coverage and universal-reduction audits below.

## Latest certified closure — MATH-111 / r=12

MATH-110 froze the exact `r=12` source:

```text
classification                1013 = 126 safe + 457 singleton + 430 critical
branch-and-bound nodes        8,278,602
AP cylinders                  1,053,555
represented occurrence mass  580,472,268,528
max multiplicity              12,976,298,271
```

MATH-111 certified an exact disjoint/exhaustive 128-way source-record partition and executed the unchanged generalized exact AP-union engine in workflow run `34764316089`.

The full jobs API was audited as `100 + 28 = 128` jobs. At final audit:

```text
workflow status      completed
workflow conclusion  success
queued jobs           0
failed jobs           0
successful jobs       128
```

Every shard's `Run exact shard closure` step concluded `success` and is gated on the engine output `PASS generalized exact AP-union audit`.

Therefore:

```text
r=12 CLOSED
r>=12 CLOSED
```

The first universal Farey cell and Collatz conjecture remain `OPEN`.

## Current execution gate — MATH-116 / r=11

MATH-112 froze the exact `r=11` workload:

```text
classification                1013 = 119 safe + 414 singleton + 480 critical
branch-and-bound nodes        3,994,436
AP source cylinders           605,972
represented occurrence mass  3,419,719,061,560
max unsplit multiplicity      51,905,193,085
```

MATH-114 supplies the exact consecutive-parameter AP split identity

```text
AP(a,b,m) = disjoint union_j AP(a+b*s_j,b,m_j)
```

and a deterministic 128-way mass-balanced schedule. For `r=11`:

```text
source records     605,972
exact split pieces 605,977
total mass         3,419,719,061,560
cap                26,716,555,169
min shard mass     26,716,555,168
max shard mass     26,716,555,169
```

MATH-116 workflow run `34768752143` has now passed its preparation certificate. The first shard wave is executing the exact closure step; later shards are queued behind the configured parallelism limit.

Therefore:

```text
r=11 OPEN — exact closure execution in progress
```

No queued/resource state is interpreted as a mathematical counterexample.

## Next execution-ready layer — MATH-117 / r=10

MATH-113/MATH-115 freeze the `r=10` source as:

```text
classification                994 = 91 safe + 396 singleton + 507 critical
branch-and-bound nodes        1,994,258
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
max unsplit multiplicity      830,483,089,363
```

MATH-114's exact 128-way representation is:

```text
exact split pieces 278,739
cap                215,291,123,465
min shard mass     215,291,123,463
max shard mass     215,291,123,465
max pieces/shard   2,448
u64 per shard      safe
```

A manual-only workflow is prepared at `.github/workflows/collatz-math117-r10-mass-balanced-sharded-closure.yml`. It is not launched while the `r=11` gate is actively consuming runner capacity.

## Structural point for lower-layer generalization

The MATH-065 generator does not define the `r` layers as nested source families. Its exact state machine accepts a completed `r`-paid cluster only at

```text
j = r and u = 0,
```

and explicitly discards `u=0` at `j<r` as an **earlier return, not an r-paid cluster**.

Hence `r` is a first-return paid-count label. Distinct `r` layers represent distinct first-return cases rather than a monotone inclusion chain. Consequently:

```text
r=12 CLOSED  !=>  r=11 CLOSED
```

by set inclusion alone.

A useful common theorem, if one exists, must therefore be uniform in the paid-count parameter `r` or in an invariant preserved by all such first-return families; it cannot rely merely on `S_{r-1} subset S_r`.

This observation is being separated into the next coverage/structure audit because it directly constrains how the remaining `r=11..2` layers may be unified.

## Remaining mainline obligations

### Stage A — descend the multi-paid frontier

Uncertified layers are now:

```text
r = 11,10,9,8,7,6,5,4,3,2
```

MATH-113 has already frozen exact workloads for `r=10..2`, and MATH-114 provides an exact mass-balanced representation that keeps downstream engine invocations inside the audited count domain, including the low-`r` uint64 cases.

Per-layer acceptance sequence:

```text
exact classifier / workload
-> exact source coverage
-> exact disjoint/exhaustive representation
-> exact AP-union or equivalent same-integer propagation closure
-> independent occurrence-mass accounting invariant
-> claim-boundary audit
```

### Stage B — paid-layer coverage audit

After the remaining layers are discharged, prove that the one-paid and multi-paid families cover every paid-count case required by the first-cell reduction.

The audit must explicitly check:

- whether `r=0` or `r=1` are absent by exact semantics rather than notation;
- the exact relation between the one-paid `t` chain and multi-paid first-return `r` chain;
- uniqueness or harmless overlap of ordinary-integer address lineage;
- that no phase/address state was lost by a coarse quotient;
- that every use of MATH-091 and MATH-096 remains within proved scope.

### Stage C — first universal-cell implication-chain audit

```text
first-cell candidate geometry
-> exact address lift
-> macro decomposition
-> paid-count classification
-> exact carry/address propagation
-> closed terminal families
-> contradiction / descent below B_pub
```

Only exhaustive coverage permits promotion of the first universal Farey cell from `OPEN` to `CLOSED`.

### Stage D — universal Collatz reduction audit

The final theorem layer must verify the exact reduction from

```text
published finite baseline B_pub = 2^71
+ first universal-cell closure
+ recursive / inductive / cell-propagation theorem
```

to every positive integer.

## Claim boundary

The project continues to distinguish:

- exact finite workload and representation;
- exact finite layer closure;
- coverage of a proof partition;
- first-cell emptiness;
- universal reduction;
- full Collatz proof.
