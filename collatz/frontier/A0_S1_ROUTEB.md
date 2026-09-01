# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation.  Chronological notes remain evidence/history; new calculation should start from this file.

## Input family

Exact retained first-defect roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary input certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

Each root is an exact source cylinder

`X = r + 2^h m`

with a finite integer parameter interval and exact parity-bit refinement.

## Active state philosophy

Carry only the coordinates queried by an unresolved predicate.

Base active state for the next scan:

`source transition control × interval payload × minimum physical-risk/defect label`.

Candidate additional coordinates are activated lazily:

- ballot state if not already discharged by target dominance;
- checkpoint dyadic/ternary observation;
- ternary suffix carry/projective cylinder;
- tail first-passage state;
- renewal/C4F/global formation state only after an explicit invariant theorem.

Transition control must not be discarded merely because one observation predicate has been discharged.

## Current closed primitives to use

### Source / interval

- exact affine source-cylinder transducer;
- exact bit refinement `m = m0 + 2k`;
- finite interval payload compression / four-state cylinder theorem;
- reduced source+ballot control where its hypotheses apply.

### Ballot / grammar

- fixed-count ballot future cone;
- target strict-prefix dominance / surplus representation;
- exact dual H/L canonical grammar;
- target-only H/L–Stern-Brocot hierarchy alignment;
- critical-cut product factorization.

### Correction / projective

- fixed `(h,q)` correction injectivity;
- dyadic prefix localization;
- ternary suffix locality and carry recurrence;
- projective block carry law;
- projective successor carry → exponent/displacement cylinder.

### Membership-relevant defect

- monotone normalized defect;
- exact projective-cylinder defect floor;
- fixed-cylinder ordering-aware minimum;
- displaced-rank / phase-weighted lower bounds;
- normalized-defect semiring;
- inverse physical defect budget;
- integer/min-plus physical-risk reductions from the latest frontier work.

## Next executable objective

For each of the 14 roots:

1. initialize the exact source/control state and finite parameter interval;
2. attach the minimum admissible physical-risk/defect label;
3. refine by exact source parameter bits;
4. merge histories only under the certified exact future-control equivalence;
5. close any entire node whose certified defect/physical inequality excludes its full X interval;
6. for unresolved nodes, identify which additional predicate actually blocks closure;
7. activate only that predicate and continue;
8. record exact closed/unresolved family counts and state counts by depth.

Do not report marginal survival ratios as probabilities.

## Success criteria for this frontier

The first root-scan milestone is complete when there is a reproducible table for all 14 roots showing:

- initial integer count;
- explored/merged exact family-state counts;
- families closed by physical defect;
- families requiring checkpoint/projective/tail state;
- deepest unresolved depth;
- no use of singleton enumeration except where mathematically unavoidable and explicitly recorded.

This milestone is not yet C5 closure.  It is the audited execution of the C4 family-closure engine.

## Known failure modes to avoid

- local carry greedy before a cylinder sequence is fixed;
- target-collision mismatch treated as rejection;
- use of exact completion-defect DP as an uncompressed binary-tree search engine;
- forgetting source transition coordinates after an observation is discharged;
- double counting local defect floors;
- using later refined bounds retroactively.

## Frontier output

When the root scan is completed, update in the same cycle:

- `../status/CURRENT_STATUS.md`;
- `../status/OPEN_GATES.md`;
- `../CANONICAL_PROOF_STACK.md`;
- this file;
- relevant certificate/audit indexes.
