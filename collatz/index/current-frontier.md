# Current Collatz frontier through MATH-129

Date: 2026-09-14

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=12                     CLOSED
Multi-paid r=11                      OPEN — MATH-116 exact closure still incomplete
Multi-paid r=10                      OPEN — MATH-117 execution-ready, not launched
Multi-paid 2<=r<=9                   OPEN
```

No finite layer closure is promoted to first-cell emptiness or to the Collatz conjecture without the separate coverage and universal-reduction audits below.

## Latest certified layer closure — MATH-111 / r=12

MATH-111 executed the unchanged generalized exact AP-union engine on an exact disjoint/exhaustive 128-way partition of the MATH-110 source.

```text
AP cylinders                  1,053,555
represented occurrence mass  580,472,268,528
successful shard jobs         128
queued jobs at final audit    0
failed jobs at final audit    0
```

Therefore

```text
r=12 CLOSED
r>=12 CLOSED
```

within the audited multi-paid framework.

## Current executable gate — MATH-116 / r=11

Frozen r=11 source:

```text
classification                1013 = 119 safe + 414 singleton + 480 critical
branch-and-bound nodes        3,994,436
AP source cylinders           605,972
represented occurrence mass  3,419,719,061,560
max unsplit multiplicity      51,905,193,085
```

MATH-114/MATH-115 prepare an exact 128-way mass-balanced representation:

```text
exact split pieces 605,977
cap                26,716,555,169
min shard mass     26,716,555,168
max shard mass     26,716,555,169
```

Workflow run `34768752143` has a successful preparation certificate and multiple successful exact AP-union shard closures. At the latest audit, page 1 of the jobs API had no queued or failed jobs, while page 2 still contained runner-queued later shards and no observed failures.

Therefore:

```text
r=11 OPEN — exact closure execution incomplete
```

Queued/resource state is not interpreted as a mathematical counterexample.

## MATH-121 through MATH-129 — uniform r=11 structural pruning chain

### MATH-121 — scalar rank barrier

For the normalized MATH-120 state

```text
z=2^d/3^q,
u=c/3^q,
F=z*2^71-N-u,
```

`F>=0` is exact frozen-floor closure, but `F` alone is not monotone and `-F/z` is merely the branch value excess above the frozen floor. A useful universal rank therefore needs parity/address information in addition to the normalized scalar state.

### MATH-122 / MATH-123 — exact AP resolution ranks

For a non-singleton AP branch with current maximum `N` and multiplicity `m>=2`, parity refinement satisfies

```text
m' <= ceil(m/2) < m.
```

MATH-122 proves strict decrease of

```text
V=(N+1)m^2.
```

MATH-123 strengthens this to the lexicographic well-founded rank

```text
W=(N+1)m,
rank=(W,m).
```

This proves finite AP resolution, but not by itself eventual frozen-floor descent after singleton resolution.

### MATH-124 — exact direct parity-word address

For feasible parity word `w` of length `d`, odd count `q`, and correction `c_w`,

```text
r_w = -c_w*(3^q)^(-1) mod 2^d.
```

For odd-step AP `n=a+bk`,

```text
k = (r_w-a)b^(-1) mod 2^d.
```

Thus parity-word address can be mapped directly to exact AP source-parameter residue.

### MATH-125 — sharp correction envelope and q-gate

For every length-`d` parity word with `q` odd steps,

```text
3^q-2^q <= c_w <= 2^(d-q)(3^q-2^q).
```

Hence all such words are frozen-floor safe for source maximum `N` whenever

```text
(3^q/2^d)N + (3/2)^q - 1 <= 2^71.
```

This is an exact sufficient gate, not an average-drift argument.

### MATH-126 / 127 / 128 — intermediate exact safe-subset audits

These remain valid but are superseded as the active r=11 pruning bound by MATH-129.

```text
MATH-126  ~82.2133% exact safe source mass
MATH-127  ~84.930482% exact safe source mass
MATH-128  ~87.3529468% exact safe source mass
```

### MATH-129 — current strongest exact r=11 q-gate union

For each source residue `r mod 2^22`, define

```text
N_*(r)=max_{1<=d<=22} L(d,q_d(r)),
L(d,q)=floor((2^d*2^71-c_max(d,q))/3^q).
```

The logical union of every safe prefix gate through depth 22 is counted exactly over the prepared AP source.

```text
prepared split pieces              605,977
total source occurrence mass       3,419,719,061,560
threshold levels                   275
exact multi-depth safe mass        3,209,065,424,947
exact uncertified tail mass        210,653,636,613
safe source-mass fraction          93.840030925905822%
```

The earlier adaptive complete-block method through depth 34 beats MATH-129 on zero AP pieces. MATH-129 wins on 601,534 pieces and ties on 4,443.

Authoritative artifacts:

```text
collatz/src/2026_09_14_math129_r11_multidepth_qgate_audit.cpp
collatz/results/2026-09-14-math129-r11-multidepth-qgate.tsv
collatz/notes/2026-09-14-math129-r11-exact-multidepth-qgate.md
collatz/index/2026-09-14-math121-129-r11-closeout.md
```

Important claim boundary:

```text
93.8400% exact safe subset != r=11 CLOSED
```

The remaining `210,653,636,613` source occurrences are an uncertified high-odd-count/address-sensitive tail, not counterexamples.

## Next execution-ready layer — MATH-117 / r=10

MATH-113/MATH-115 freeze:

```text
classification                994 = 91 safe + 396 singleton + 507 critical
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
max unsplit multiplicity      830,483,089,363
```

MATH-114's exact 128-way representation has `278,739` split pieces and remains `uint64` safe per shard. The manual-only MATH-117 workflow remains unlaunched while r=11 consumes runner capacity.

## Remaining mainline obligations

### Stage A — discharge r=11 down through r=2

For r=11 the clean next mathematical target is only the MATH-129 tail. Valid routes are:

```text
deeper exact multi-depth gates
or MATH-124 exact source-address/correction evaluation
or completion of MATH-116 unchanged exact AP-union closure
```

After r=11, descend `r=10,9,...,2` using the already-frozen workloads and exact mass-balanced representation.

### Stage B — paid-layer coverage audit

After all layers are discharged, prove that the one-paid and multi-paid families exhaust every paid-count case required by the first-cell reduction. Explicitly audit `r=0/1`, one-paid/multi-paid complementarity, ordinary-integer address lineage, quotient losses, and MATH-091/MATH-096 scope.

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

### Stage D — universal Collatz reduction audit

First-cell closure is not automatically the full Collatz conjecture. A separate theorem must connect

```text
B_pub = 2^71
+ first-cell closure
+ recursive/inductive/cell propagation
```

to every positive integer.

## Claim boundary

The project continues to distinguish exact finite workload, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.