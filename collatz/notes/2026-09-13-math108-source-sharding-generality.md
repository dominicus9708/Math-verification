# MATH-108 — exact source-sharding generality for the r=13 continuation

Date: 2026-09-13

Status: `EXACT REPRESENTATION LEMMA / IMPLEMENTATION GENERALIZATION / NO r=13 CLOSURE CLAIM`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- `r>=14` remains closed in the current audited multi-paid calculation.
- `2<=r<=13` remains open.
- MATH-107 fixes the exact `r=13` workload and shows that its multiplicity support is fragmented into 276 occupied contiguous intervals.

## 1. Question

MATH-071 closed `r=14` using five occupied multiplicity regions. MATH-107 shows that `r=13` no longer has such a simple five-region support. The question is whether the five-region organization was mathematically essential to the MATH-071 AP-union proof mechanism.

It is not.

## 2. Separation of mathematical state from ingestion schedule

The MATH-071 stage-B engine has two logically distinct layers.

### Exact dynamical layer

For a source AP

\[
P(a,b,m)=\{a+bk:0\le k<m\},\qquad b\text{ odd},
\]

`normalize`, `advance`, and `audit` use only exact set operations:

1. floor trimming removes only values already `<=2^71`;
2. parameter parity splits an AP exactly into its even/odd parameter subsequences;
3. the shortcut map sends each parity slice to an exact AP;
4. APs merge only on the identical `(b,a mod b)` arithmetic grid with overlapping or adjacent parameter intervals;
5. singleton ordinary integers deduplicate only by exact equality.

None of these operations refers to the five MATH-071 multiplicity regions.

### Resource/ingestion layer

The five `REGIONS` in the MATH-071 executable decide only how source records are batched before they are passed to `audit`.

When `STATE_CAP` is exceeded, `audit` does not prune a state. It bisects the ORIGINAL source-record list and audits both halves. If one source AP alone is too large, it uses the exact parameter identity

\[
P(a,b,m)
=P(a,b,m_1)\cup P(a+bm_1,b,m-m_1),
\qquad m_1+m_2=m.
\]

Therefore the resource split changes only representation and workload scheduling, not the represented ordinary-integer set.

## 3. General source-partition lemma

Let the complete exact source record family be

\[
\mathcal S=\{P_i\}_{i=1}^N.
\]

Let

\[
\mathcal S=\mathcal S_1\sqcup\cdots\sqcup\mathcal S_J
\]

be any partition of the SOURCE RECORDS. The ordinary integer sets represented by distinct source records may overlap; source-record disjointness is sufficient.

If every shard `S_j` is propagated by the exact MATH-071 set operations and every represented ordinary integer in that shard reaches the frozen floor, then every source record in `S` reaches the frozen floor.

Cross-shard overlap can only duplicate a proof obligation. It cannot remove an ordinary integer because no quotient or subtraction between shards is performed.

Hence the initial source partition may be chosen for computational tractability independently of multiplicity-region geometry.

## 4. Consequence for r=13

MATH-107 found:

```text
1,959,535 negative AP cylinders
76,391,629,325 represented occurrences
276 occupied contiguous multiplicity-support intervals
max multiplicity 687,142,557
```

The 276 intervals therefore do **not** need to become 276 mathematical states or 276 theorem cases.

A proof-safe r=13 scheduler may instead use, for example:

```text
fixed source-record chunks
    -> exact normalize/advance
    -> if STATE_CAP exceeded: exact source-record bisection
    -> if one AP is still too large: exact parameter bisection
```

The chunk size and state cap are resource parameters only. They have no pruning meaning and do not alter the theorem scope.

## 5. Relation to MATH-072, MATH-091, and MATH-096

MATH-072 identifies the analytic common coordinates

\[
S=1+\Sigma-\rho,
\qquad
\rho=2^{-u}\Omega,
\qquad
p=(\Omega-\rho)/3.
\]

But it explicitly retains an address-side coordinate `A_k`. MATH-091 and MATH-096 later make that requirement concrete through exact carry transfer and finite normalized 2-adic precision.

MATH-108 therefore does **not** replace the address channel by multiplicity. It only shows that the external scheduling of exact source APs need not follow the r=14 five-band multiplicity layout.

## 6. DSD audit

### SAFE

- source-record partition is bookkeeping, not a quotient;
- each source record is assigned to exactly one initial shard;
- ordinary target overlap across shards is permitted because closure is proved independently in each shard;
- recursive source bisection is exact union decomposition;
- single-AP parameter bisection is an exact set identity;
- all AP dynamics retain the exact base and odd step, hence ordinary-integer address lineage remains explicit.

### NOT ESTABLISHED

MATH-108 does not establish that a particular r=13 run will fit finite computational resources, terminate below a chosen depth, or close all r=13 sources. Those are the next certificate obligations.

### PROHIBITED UPGRADES

- safe arbitrary sharding `=>` r=13 closure;
- resource independence of the partition `=>` resource independence of runtime/memory;
- AP union representation `=>` an analytic invariant;
- MATH-072 common coordinate `=>` address information can be dropped;
- successful r=13 finite closure, if later obtained, `=>` first-cell or Collatz closure.

## 7. Next executable gate

The next implementation should remove the hard-coded five-region ingestion logic from the MATH-071 stage-B engine while leaving `normalize`, `advance`, and recursive `audit` semantics unchanged.

Validation order:

1. run the generalized engine on the original MATH-071 r=14 source stream;
2. require exact agreement with the r=14 source totals and closure status, and check the known maximum closure depth bound `<=479`;
3. only after this regression passes, feed the MATH-107 r=13 exact source stream;
4. any resource-driven split must remain an exact source or parameter partition.

MATH-108 is therefore the representation bridge from the fragmented r=13 workload to the already audited exact AP-union dynamics. It is not an r=13 closure certificate.
