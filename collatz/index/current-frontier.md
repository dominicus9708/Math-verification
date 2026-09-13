# Current Collatz frontier through MATH-138

Date: 2026-09-14

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=12                     CLOSED
Multi-paid r=11                      OPEN — complete closure still incomplete
Multi-paid r=10                      OPEN — MATH-117 execution-ready, not launched
Multi-paid 2<=r<=9                   OPEN
```

No finite safe subset is promoted to a layer closure, first-cell emptiness, or the Collatz conjecture.

## Latest certified layer closure — MATH-111 / r=12

MATH-111 closed `r=12` using an exact disjoint/exhaustive 128-way partition and 128 successful generalized exact AP-union shard jobs. Therefore `r>=12 CLOSED` within the audited multi-paid framework.

## Current complete gate — MATH-116 / r=11

Frozen source:

```text
classification                1013 = 119 safe + 414 singleton + 480 critical
AP source cylinders           605,972
prepared split pieces         605,977
represented occurrence mass  3,419,719,061,560
```

MATH-116 has a successful preparation certificate and many successful exact AP-union shards. Later shards remain runner-queued; no mathematical failure has been observed. `r=11` therefore remains `OPEN` until all exact shards pass or an equivalent complete exact certificate is obtained.

## Common structural chain

- MATH-121: normalized floor margin alone is not a sufficient monotone rank.
- MATH-122: `V=(N+1)m^2` strictly decreases on every non-singleton exact AP branch.
- MATH-123: stronger lexicographic resolution rank `((N+1)m,m)`.
- MATH-124: exact parity-word/source-parameter address formula.
- MATH-125: sharp correction envelope and sufficient frozen-floor gate.

## q-gate deepening through D=35

MATH-129 gave the exact union through depth 22:

```text
safe  = 3,209,065,424,947
tail  =   210,653,636,613
```

MATH-131 through MATH-135 extended the exact address calculation through depth 35, including complete-cycle DP where available and exact cyclic remainder handling thereafter. The cumulative depth-35 state is:

```text
safe  = 3,332,624,019,800
tail  =    87,095,041,760
safe fraction = 97.4531521393%
```

## MATH-136 — 33-profile exact address compression at D=36

The prepared source has only 33 distinct q-safe threshold profiles through depth 36. Relative to those source profiles, only 23 final-depth crossing types can discharge any prepared source mass.

The resulting profile-address DFS enumerates only source residues that cross at least one actual prepared-source threshold. Exact audit:

```text
profiles                 33
crossing patterns        23
new address support      250,945,398
D=36 new safe mass       5,656,350,703
```

The largest class `b=3^24` independently reproduces `1,254,908,728`. Small `b=3^45..3^53` classes were independently cross-checked by direct ordinary-occurrence replay.

Cumulative state:

```text
safe  = 3,338,280,370,503
tail  =    81,438,691,057
safe fraction = 97.61855609800153%
```

## MATH-137 — exact D=37 continuation

The same compressed state remains exact at depth 37:

```text
profiles                 34
crossing patterns        20
new address support      595,269,450
D=37 new safe mass       3,461,477,451
```

Large and medium classes were handled by the profile-address calculation; `b=3^37..3^53` were independently direct-replayed.

Cumulative state:

```text
safe  = 3,341,741,847,954
tail  =    77,977,213,606
safe fraction = 97.71977720384936%
```

## MATH-138 — exact D=38 continuation

Depth 38 again gives a positive pairwise-disjoint increment:

```text
profiles                 34
crossing patterns        21
new address support    1,031,508,005
D=38 new safe mass       7,480,161,028
```

Cumulative strongest q-gate certificate:

```text
safe  = 3,349,222,008,982
tail  =    70,497,052,578
safe fraction = 97.93851333080441%
```

The remaining `70,497,052,578` occurrences are not counterexamples. They are exactly source occurrence mass not discharged by the current sufficient q-gate/address certificate through depth 38.

Important boundary:

```text
97.9385% exact safe subset != r=11 CLOSED
```

## Next calculation

1. Continue the profile-address gate to depth 39 while the finite-state arithmetic still fits the current exact implementation.
2. In parallel, inspect the remaining tail by source profile and exact correction, because the q-only sharp envelope is sufficient but not necessary.
3. Continue checking MATH-116 job-level completion; a full 128-shard pass would independently close `r=11`.
4. Only after complete `r=11` closure descend to the MATH-117 `r=10` complete gate.

## Remaining proof obligations after layer closures

1. Audit one-paid/multi-paid coverage, including `r=0/1` semantics.
2. Audit the entire first-cell implication chain.
3. Separately prove or re-audit the universal reduction from frozen baseline plus first-cell closure to every positive integer.

## Claim boundary

The project continues to distinguish exact finite workload, exact finite safe subsets, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.