# MATH-126 — r=11 hybrid q-gate / exact-address tail audit

Status: `MAINLINE FINITE AUDIT / HYBRID REPRESENTATION PIVOT / r=11 STILL OPEN`

Date: 2026-09-14

## Input certificate

The audit uses the exact prepared MATH-116 r=11 shard artifact:

```text
artifact id:     10321272221
artifact digest: sha256:48ab3950d866925468d7745dca078ebf65adb50c65b82c4583e1e38ea1796b81
split pieces:    605,977
total mass:      3,419,719,061,560
```

Every row is an exact AP

```text
target0<TAB>odd_step<TAB>count.
```

The MATH-114 split pieces are exact consecutive parameter partitions. Ordinary-integer overlap between distinct historical source records remains possible, so all percentages below refer to **source occurrence mass**, not unique integers or natural density.

## Source maximum audit

For each piece

```text
P(a,b,m),
N=a+b(m-1),
```

was computed exactly.

Observed maximum:

```text
N_max = 6,290,339,729,165,775,182,359.
```

The frozen MATH-058 bound is

```text
YMAX = 6,290,339,729,182,995,389,049.
```

Thus every prepared r=11 AP satisfies

```text
N <= YMAX.
```

## Conservative complete-block q-gate

At depth `d`, every complete parameter block of length `2^d` contains each parameter residue modulo `2^d` exactly once. By MATH-124 this means it contains each length-d parity word exactly once.

For each AP piece, MATH-125 gives a largest safe odd count `Q_safe(d,N)` such that every parity word with `q<=Q_safe` reaches the frozen floor by depth `d`.

Only complete parameter blocks are credited in this audit. Incomplete remainders receive zero credit and are left for the exact-address tail. Therefore the credited mass is a rigorous lower bound, not a heuristic fraction.

## Best tested common depth

For `1<=d<=34`, the largest guaranteed safe source-occurrence mass occurs at

```text
d=22.
```

At this depth the exact AP-local safe thresholds are only:

```text
Q_safe=12:  27,420 pieces
Q_safe=13: 578,557 pieces
```

The corresponding safe parity-word counts are:

```text
q<=12: 3,096,514 of 2^22 words
q<=13: 3,593,934 of 2^22 words.
```

Summing only complete-block certified occurrences gives

```text
guaranteed safe mass:  2,811,463,801,368
uncertified tail mass:    608,255,260,192
```

or

```text
82.21329737202075% guaranteed safe source-occurrence mass.
```

## Interpretation

This is not a density argument and is not an r=11 closure claim.

It gives an exact decomposition strategy:

```text
r=11 exact source APs
-> depth-22 complete parameter blocks
-> MATH-125 low-q classes discharged without exact address
-> incomplete remainders + high-q classes retained
-> MATH-124 exact parameter residue
-> MATH-119/MATH-120 exact frozen-floor gate / existing MATH-108 closure.
```

Thus only at most the uncredited source-occurrence mass needs the expensive exact-address tail under this conservative common-depth decomposition. The actual exact-address tail may be smaller because:

- incomplete remainders can contain safe words;
- high-q words can still satisfy the exact correction/address floor gate;
- AP-specific depths can outperform the single common depth `d=22`.

None of those improvements are credited here.

## Main structural consequence

The common-formula route is no longer merely qualitative. On the exact r=11 source, the layer-independent MATH-125 envelope already discharges a certified majority of the source occurrence representation before exact-address propagation.

The remaining theorem-design problem has therefore narrowed to a relatively high-q/address-sensitive tail rather than the full r=11 occurrence mass.

## Claim boundary

`r=11` remains `OPEN` until MATH-116 or an equivalent complete exact certificate closes every source occurrence. The certified frontier remains `r>=12 CLOSED`.
