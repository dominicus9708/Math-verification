# Current Collatz frontier after MATH-109

Date: 2026-09-13

## Exact finite status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=13                     CLOSED
Multi-paid 2<=r<=12                  OPEN
```

MATH-109 closes `r=13` from the exact MATH-107 source by combining:

1. a disjoint/exhaustive 16-shard partition certificate;
2. total source size `1,959,535` AP cylinders;
3. total represented occurrence mass `76,391,629,325`;
4. successful exact AP-union closure for all 16 shards in workflow run `34731274347`.

## Remaining mainline obligations

### Stage A — descend the multi-paid frontier

Nominal unresolved layers:

```text
r = 12,11,10,9,8,7,6,5,4,3,2
```

There are 11 nominal layers. They must not be assumed to require identical workloads. For each new `r`, first audit the exact phase/address classification and multiplicity distribution, then select the representation/sharding schedule.

Per-layer acceptance sequence:

```text
exact classifier / workload
-> exact source coverage
-> disjoint/exhaustive partition if sharding is needed
-> exact AP-union or equivalent same-integer propagation closure
-> independent accounting invariant
-> claim-boundary audit
```

The immediate next layer is `r=12`.

### Stage B — paid-layer coverage audit

After every remaining layer is discharged, prove that the closed one-paid and multi-paid families actually cover every paid-count case required by the first-cell reduction.

This audit must explicitly check:

- no missing `r=0` or `r=1` semantic case is hidden by notation;
- the one-paid `t` chain and the multi-paid `r` chain are complementary where claimed;
- every relevant ordinary-integer address lineage is represented exactly once or with harmless overlap;
- no phase/address state was lost by a coarse quotient;
- every use of MATH-091 and MATH-096 stays inside its proved scope.

### Stage C — first universal-cell implication-chain audit

Reconstruct the implication chain from the original 340 top-address blocks to the closed paid-layer certificates.

Required checks include:

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

If that universal propagation theorem is already present in the archive, it must be re-audited against the final definitions. If it is not complete, proving it remains a separate theorem obligation.

## Claim boundary

The current result is substantial finite structural progress, not a proof of Collatz. The project must continue to distinguish:

- exact finite closure;
- coverage of a proof partition;
- first-cell emptiness;
- universal reduction;
- full Collatz proof.
