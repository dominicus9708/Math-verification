# MATH-107 — exact r=13 workload and representation pivot

Date: 2026-09-13

Status: `EXACT FINITE r=13 WORKLOAD AUDIT / r=13 OPEN / REPRESENTATION PIVOT`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-071 and the intervening exact certificates close every multi-paid layer `r>=14` in the current first-cell calculation.
- MATH-104--106 close the previously open detailed one-paid depth band `7<=t<=9` on the audited compact carry/address criterion.
- The remaining multi-paid frontier is `2<=r<=13`.

## 1. Exact r=13 phase/address classification

Reusing the unchanged MATH-065 classifier gives

```text
1035 total phase/address cells
= 157 cost-safe
+ 483 singleton-resolution
+ 395 critical.
```

This reproduces the previously recorded r=13 support inventory and fixes the exact input population for the next calculation.

## 2. Exact negative-candidate stream

Applying the unchanged MATH-065 exact dyadic branch-and-bound to every r=13 singleton-resolution and critical cell gives:

```text
branch-and-bound nodes       15,364,524
negative AP cylinders         1,959,535
represented occurrences      76,391,629,325
maximum AP multiplicity         687,142,557
```

The occupied multiplicity values form exactly

```text
276 contiguous support intervals.
```

This is a representation fact about the exact source stream. It is not a heuristic partition and it is not a closure statement.

## 3. Heavy multiplicity tail

The source stream is strongly occurrence-heavy in a small number of high-multiplicity cylinders:

| threshold | cylinders with m >= threshold | represented occurrences |
|---:|---:|---:|
| 1,000 | 305,062 | 76,263,230,955 |
| 10,000 | 123,925 | 75,633,800,228 |
| 100,000 | 36,955 | 72,481,494,807 |
| 1,000,000 | 8,414 | 62,567,007,204 |
| 10,000,000 | 1,130 | 41,355,402,672 |
| 100,000,000 | 65 | 14,620,369,241 |

Thus only 8,414 cylinders already encode more than sixty-two billion ordinary occurrences.

## 4. Comparison with r=14

MATH-071 r=14 had:

```text
2,599,692 negative AP cylinders
10,691,937,078 represented occurrences
max multiplicity 171,785,639
five occupied multiplicity regions
```

At r=13 the cylinder count decreases, but represented multiplicity increases to 76,391,629,325 and the maximum multiplicity increases to 687,142,557. The occupied multiplicity support also fragments into 276 contiguous intervals rather than the five broad regions used to schedule MATH-071.

Therefore the MATH-071 five-band resource schedule cannot simply be assumed to remain an adequate proof-facing representation one layer lower.

This does **not** show that exact AP propagation fails mathematically. It shows that reuse of the r=14 representation/scheduling scheme requires a new exact audit.

## 5. DSD audit

### SAFE

1. The MATH-065 phase/address classifier is reused unchanged.
2. Every singleton-resolution and critical cell is enumerated by the same exact negative-candidate cylinder generator.
3. Cylinder multiplicity is the exact number of source parameters represented by that AP cylinder.
4. The totals are sums over the full exact generated stream; no sampling or density inference is used.
5. The multiplicity interval count is computed from exact occupied multiplicity values only.
6. Threshold tables count full cylinders and their exact represented occurrence multiplicity.

### REPRESENTATION PIVOT

The r=14 closure engine used a small number of broad multiplicity regions plus exact source/parameter sharding. At r=13 the exact support is more fragmented and the high-multiplicity tail carries most represented occurrences. The next proof-facing representation must therefore preserve exact AP identity/address information while handling this fragmentation explicitly.

Candidate continuation forms include:

- fragmentation-aware exact AP source sharding;
- exact common-coordinate grouping that is proven set-preserving before compression;
- compact carry/address information coupled to the AP family rather than an address-forgotten multiplicity quotient.

No coarse quotient is permitted merely to reduce the workload.

### OPEN

- exact propagation/closure of r=13;
- multi-paid layers `2<=r<=12`;
- exact dependency bridge between the multi-paid hierarchy and MATH-096--106 one-paid compact-carry closures;
- complete first universal cell implication-chain audit;
- first universal Farey cell emptiness;
- Collatz conjecture.

### PROHIBITED UPGRADES

- fewer AP cylinders than r=14 `=>` easier or closed r=13;
- high multiplicity `=>` dynamical danger by itself;
- fragmented multiplicity support `=>` impossibility of AP-union closure;
- a successful resource partition `=>` a new mathematical pruning theorem;
- finite r=13 workload enumeration `=>` r=13 closure;
- closure of one paid-count layer `=>` first-cell emptiness or Collatz proof.

## 6. Mainline consequence

MATH-107 changes the immediate next task from a blind `r=13` replay into an exact representation audit:

1. construct an exact fragmentation-aware r=13 AP propagation schedule or equivalent set-preserving representation;
2. regression-test it against MATH-071 r=14 before using it on r=13;
3. propagate the r=13 stream without dropping ordinary-integer address information;
4. only then decide whether r=13 can be certified closed or whether a further state variable is required.

The current mathematical status remains:

```text
r >= 14: CLOSED in the current audited multi-paid calculation
2 <= r <= 13: OPEN
r = 13: exact workload characterized by MATH-107
first universal Farey cell: OPEN
Collatz conjecture: OPEN
```

## Reproducibility

Audit script:

`collatz/src/2026_09_13_math107_r13_workload_audit.py`

Summary result:

`collatz/results/2026-09-13-math107-r13-workload-audit.tsv`
