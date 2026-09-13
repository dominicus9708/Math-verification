# Current Collatz frontier through MATH-133

Date: 2026-09-14

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=12                     CLOSED
Multi-paid r=11                      OPEN — MATH-116 exact closure incomplete
Multi-paid r=10                      OPEN — MATH-117 execution-ready, not launched
Multi-paid 2<=r<=9                   OPEN
```

No finite safe subset is promoted to a layer closure, first-cell emptiness, or the Collatz conjecture.

## Latest certified layer closure — MATH-111 / r=12

MATH-111 closed `r=12` using an exact disjoint/exhaustive 128-way partition and 128 successful generalized exact AP-union shard jobs. Therefore

```text
r>=12 CLOSED
```

within the audited multi-paid framework.

## Current complete gate — MATH-116 / r=11

Frozen source:

```text
classification                1013 = 119 safe + 414 singleton + 480 critical
AP source cylinders           605,972
prepared split pieces         605,977
represented occurrence mass  3,419,719,061,560
```

MATH-116 has a successful preparation certificate and multiple successful exact AP-union shards. Later shards have remained runner-queued; no mathematical failure has been observed. `r=11` therefore remains `OPEN` until all exact shards pass or an equivalent complete exact certificate is obtained.

## MATH-121 through MATH-125 — common structural chain

- MATH-121: normalized floor margin alone cannot supply the required unconstrained monotone rank.
- MATH-122: `V=(N+1)m^2` strictly decreases on every non-singleton exact AP branch.
- MATH-123: stronger lexicographic resolution rank `((N+1)m,m)`.
- MATH-124: exact parity-word/source-parameter address formula.
- MATH-125: sharp correction envelope and sufficient frozen-floor gate.

These results separate finite AP resolution from actual floor descent and retain exact address information where required.

## MATH-129 — exact prefix union through depth 22

Over the complete prepared r=11 source:

```text
exact d<=22 safe mass        3,209,065,424,947
uncertified tail              210,653,636,613
safe fraction                  93.840030925905822%
```

This is an exact finite subset certificate, not a density argument.

## MATH-131 — complete-cycle parity-word DP through depth 34

MATH-124 implies a bijection between length-`D` parity words and source residues modulo `2^D`. Since every prepared AP has odd step, every complete `2^D` parameter block also contains every length-`D` parity word exactly once.

MATH-131 therefore replaces explicit residue enumeration on complete blocks by an exact DP on

```text
(q, best_threshold).
```

The depth-23 value exactly reproduces MATH-130. Pairwise-disjoint new complete-cycle safe mass at depths 23 through 34 totals

```text
77,081,911,098.
```

Thus before restoring incomplete remainders:

```text
certified safe mass >= 3,286,147,336,045
uncertified tail   <=   133,571,725,515
safe fraction      >= 96.094073135526301%
```

The prepared maximum piece multiplicity is `26,716,555,169`, so no full `2^35` parameter block exists. MATH-131 therefore exhausts the complete-cycle-only extension.

## MATH-132 — exact cyclic remainders at D=23..25

Exact address counting on the incomplete cyclic remainders adds:

```text
D=23 remainder      147,454,842
D=24 remainder    1,221,965,686
D=25 remainder    1,841,592,242
```

After these exact remainders:

```text
certified safe mass >= 3,289,358,348,815
uncertified tail   <=   130,360,712,745
safe fraction      >= 96.18797011104378%
```

The first direct D=26 scan hit an implementation/resource limit, not a mathematical counterexample or gate failure.

## MATH-133 — optimized exact remainder scan at D=26

MATH-133 replaces repeated `D`-step simulation by the exact dyadic recursion

```text
q_D(2s)   = q_{D-1}(s)
q_D(2s+1) = 1 + q_{D-1}(3s+2 mod 2^(D-1)).
```

The optimized implementation first reproduces the MATH-132 D=23 exact result, then obtains at D=26:

```text
complete-cycle increment   5,512,456,558
exact remainder increment    907,778,775
exact D=26 increment        6,420,235,333
```

Combining MATH-131 with all exact remainder increments through D=26 gives the current strongest finite lower bound:

```text
cumulative remainder increment D=23..26  4,118,791,545
certified safe mass >=                 3,290,266,127,590
uncertified tail   <=                     129,452,933,970
safe fraction      >=                     96.21451553067209%
```

Important boundary:

```text
96.2145155% exact safe lower bound != r=11 CLOSED
```

The remaining tail is not a counterexample set. It is the source mass not discharged by the current envelope/address certificates.

The optimized D=27 direct residue-order scan still exceeds the current execution window. The next mathematical/computational target is therefore to compress the address-sensitive remainder counting beyond D=26, or hand the remaining exact tail to MATH-124 direct-address propagation / the unchanged MATH-108 AP-union engine.

## Next layer — MATH-117 / r=10

MATH-117 remains execution-ready but unlaunched while the r=11 complete gate consumes runner capacity.

## Remaining obligations

1. Discharge the remaining exact r=11 tail or complete MATH-116.
2. Descend `r=10,9,...,2` using the frozen exact workloads and mass-balanced representation.
3. Audit that one-paid and multi-paid families exhaust every required paid-count/address case, including `r=0/1` semantics.
4. Audit the full first-cell implication chain.
5. Separately prove or re-audit the universal reduction from the frozen baseline plus first-cell closure to every positive integer.

## Claim boundary

The project continues to distinguish exact finite workload, exact finite safe subsets, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.
