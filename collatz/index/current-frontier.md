# Current Collatz frontier through MATH-130

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

No finite layer closure is promoted to first-cell emptiness or to the Collatz conjecture without the separate coverage and universal-reduction audits.

## Latest certified layer closure — MATH-111 / r=12

MATH-111 closed `r=12` using an exact disjoint/exhaustive 128-way partition and 128 successful generalized exact AP-union shard jobs.

```text
AP cylinders                  1,053,555
represented occurrence mass  580,472,268,528
successful shard jobs         128
failed jobs                   0
```

Therefore `r>=12 CLOSED` within the audited multi-paid framework.

## Current complete gate — MATH-116 / r=11

Frozen exact r=11 source:

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

Workflow run `34768752143` has a successful preparation certificate and many successful exact AP-union shards. At the latest audit, later shards remained runner-queued and no mathematical failure was observed. Therefore `r=11` remains `OPEN` until all exact shards pass or an equivalent complete exact certificate is obtained.

## MATH-121 through MATH-125 — layer-independent structural chain

- **MATH-121:** normalized floor margin alone is not a sufficient monotone well-founded rank; exact parity/address information remains necessary.
- **MATH-122:** `V=(N+1)m^2` strictly decreases on every non-singleton exact AP branch.
- **MATH-123:** stronger lexicographic exact resolution rank `((N+1)m,m)`; proves finite AP resolution but not singleton floor descent.
- **MATH-124:** direct parity-word source address
  ```text
  r_w = -c_w(3^q)^(-1) mod 2^d,
  k = (r_w-a)b^(-1) mod 2^d.
  ```
- **MATH-125:** sharp correction envelope
  ```text
  3^q-2^q <= c_w <= 2^(d-q)(3^q-2^q)
  ```
  and exact sufficient frozen-floor gate
  ```text
  (3^q/2^d)N + (3/2)^q - 1 <= 2^71.
  ```

## MATH-126 through MATH-129 — exact r=11 q-gate pruning

MATH-126/127/128 are valid intermediate finite certificates but are superseded as the active bound by MATH-129.

MATH-129 constructs the exact logical union of all MATH-125 safe prefix gates through depth 22 over the prepared r=11 source:

```text
prepared split pieces              605,977
total source occurrence mass       3,419,719,061,560
exact d<=22 safe mass              3,209,065,424,947
exact d<=22 uncertified tail       210,653,636,613
safe fraction                      93.840030925905822%
```

This is an exact finite subset certificate, not a density argument and not an `r=11 CLOSED` claim.

## MATH-130 — disjoint depth-23 conservative increment

MATH-130 asks only for source residues that are **not** MATH-129-safe but become safe at depth 23.

For each source residue `r mod 2^23`, define

```text
L_old(r)=max_{1<=d<=22} L(d,q_d(r)),
L_23(r)=L(23,q_23(r)).
```

The new set is exactly the residue/source-maximum region

```text
L_old(r) < N <= L_23(r),
```

so it is disjoint from the MATH-129 safe union by construction.

Only complete `2^23` source-parameter cycles are counted; incomplete remainders are assigned zero extra safe mass. Therefore the result is a conservative exact lower bound.

```text
depth-23 modulus                         8,388,608
residues with stronger d=23 threshold    2,489,262
rows with complete d=23 cycles              13,702
complete-cycle mass examined       3,249,377,640,448
rows with positive new increment              2,135
new disjoint d=23 safe mass           3,151,665,357
```

Combining MATH-129 and the disjoint MATH-130 increment:

```text
certified safe mass >= 3,212,217,090,304
uncertified tail mass <=   207,501,971,256
certified safe fraction >= 93.93219245439003%
```

The remaining tail is not a counterexample set. It is only source mass not discharged by the current q-gate certificates.

Authoritative artifacts:

```text
collatz/src/2026_09_14_math129_r11_multidepth_qgate_audit.cpp
collatz/results/2026-09-14-math129-r11-multidepth-qgate.tsv
collatz/notes/2026-09-14-math129-r11-exact-multidepth-qgate.md
collatz/src/2026_09_14_math130_r11_d23_disjoint_increment.cpp
collatz/results/2026-09-14-math130-r11-d23-disjoint-increment.tsv
collatz/notes/2026-09-14-math130-r11-d23-disjoint-increment.md
collatz/index/2026-09-14-math121-129-r11-closeout.md
```

Important boundary:

```text
93.932192% exact safe lower bound != r=11 CLOSED
```

## Next layer — MATH-117 / r=10

MATH-117 remains execution-ready but unlaunched while the r=11 complete gate consumes runner capacity. Its exact source has `278,725` AP cylinders and total occurrence mass `27,557,263,803,397`.

## Remaining obligations

1. Discharge the remaining exact r=11 tail or complete MATH-116.
2. Descend `r=10,9,...,2` using the frozen workloads and exact mass-balanced representation.
3. Audit that one-paid and multi-paid families exhaust every required paid-count/address case, including `r=0/1` semantics.
4. Audit the full first-cell implication chain.
5. Separately prove or re-audit the universal reduction from frozen baseline plus first-cell closure to every positive integer.

## Claim boundary

The project continues to distinguish exact finite workload, exact finite safe subsets, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.