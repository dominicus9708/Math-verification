# Current Collatz frontier through MATH-116 candidate gates

Date: 2026-09-14

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=13                     CLOSED
Multi-paid r=12                      OPEN — MATH-111 final shard completion pending
Multi-paid r=11                      OPEN — MATH-116 exact gate launched
Multi-paid 2<=r<=10                  OPEN
```

No finite layer closure is promoted to first-cell emptiness or to the Collatz conjecture without the separate coverage and universal-reduction audits below.

## Last certified closure — MATH-109 / r=13

MATH-109 closes `r=13` from the exact MATH-107 source by combining:

1. a disjoint/exhaustive 16-shard partition certificate;
2. total source size `1,959,535` AP cylinders;
3. total represented occurrence mass `76,391,629,325`;
4. successful exact AP-union closure for all 16 shards in workflow run `34731274347`.

Therefore the currently certified multi-paid closure frontier remains

```text
r >= 13 CLOSED.
```

## Current execution gates

### MATH-110 / MATH-111 — r=12

MATH-110 froze the exact workload:

```text
classification                1013 = 126 safe + 457 singleton + 430 critical
branch-and-bound nodes        8,278,602
AP cylinders                  1,053,555
represented occurrence mass  580,472,268,528
max multiplicity              12,976,298,271
```

MATH-111 certified an exact disjoint/exhaustive 128-way source-record partition and launched exact AP-union closure workflow run `34764316089`.

At the latest audit the remaining jobs were still GitHub Actions runner-queued and no failure had been identified. Consequently:

```text
r=12 OPEN
```

until all 128 shard closures are confirmed `PASS generalized exact AP-union audit`.

### MATH-112 / MATH-114 / MATH-115 / MATH-116 — r=11

MATH-112 froze the exact workload:

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

and a deterministic 128-way mass-balanced schedule. For `r=11` its audited partition values are:

```text
source records     605,972
exact split pieces 605,977
total mass         3,419,719,061,560
cap                26,716,555,169
min shard mass     26,716,555,168
max shard mass     26,716,555,169
```

MATH-115 generalizes the exact `r=2..12` source exporter and one-shot shard preparation while preserving the MATH-065 classifier/generator and MATH-114 partition semantics.

MATH-116 connects those components to the unchanged MATH-108 generalized exact AP-union engine. Workflow run `34768752143` has been created; the prepare job was runner-queued at the latest audit.

Therefore:

```text
r=11 OPEN
```

until the exact preparation certificate and all 128 shard closures pass.

The mass-balanced scheduler is an exact resource representation, not a theorem-strengthening step.

## Remaining mainline obligations

### Stage A — descend the multi-paid frontier

Uncertified layers are currently:

```text
r = 12,11,10,9,8,7,6,5,4,3,2
```

MATH-113 has already frozen exact workload landscapes for `r=10..2`, and MATH-114 provides an exact mass-balanced representation that keeps every downstream engine invocation inside its audited count domain, including the low-`r` uint64 barrier cases.

Per-layer acceptance sequence remains:

```text
exact classifier / workload
-> exact source coverage
-> exact disjoint/exhaustive representation
-> exact AP-union or equivalent same-integer propagation closure
-> independent occurrence-mass accounting invariant
-> claim-boundary audit
```

A queued or resource-failed workflow job is not a mathematical counterexample; job logs must be audited before classification.

### Stage B — paid-layer coverage audit

After all remaining layers are discharged, prove that the closed one-paid and multi-paid families actually cover every paid-count case required by the first-cell reduction.

This audit must explicitly check:

- whether `r=0` or `r=1` are absent by exact semantics rather than merely omitted by notation;
- that the one-paid `t` chain and multi-paid `r` chain are complementary where claimed;
- that every relevant ordinary-integer address lineage is represented exactly once or with harmless overlap;
- that no phase/address state was lost by a coarse quotient;
- that every use of MATH-091 and MATH-096 stays inside its proved scope.

### Stage C — first universal-cell implication-chain audit

Reconstruct the implication chain from the original 340 top-address blocks to the closed paid-layer certificates:

```text
first-cell candidate geometry
-> exact address lift
-> macro decomposition
-> paid-count classification
-> exact carry/address propagation
-> closed terminal families
-> contradiction / descent below the frozen baseline
```

Only if every first-cell candidate is covered may the first universal Farey cell be promoted from `OPEN` to `CLOSED`.

### Stage D — universal Collatz reduction audit

First-cell closure is still not automatically the full Collatz conjecture.

The final theorem layer must verify the exact reduction from:

```text
published finite baseline B_pub = 2^71
+ first universal-cell closure
+ any recursive / inductive / cell-propagation theorem
```

to every positive integer.

If that universal propagation theorem is already present in the archive, it must be re-audited against the final definitions. If incomplete, proving it remains a separate theorem obligation.

## Claim boundary

The project continues to distinguish:

- exact finite workload and representation;
- exact finite layer closure;
- coverage of a proof partition;
- first-cell emptiness;
- universal reduction;
- full Collatz proof.
