# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation.

## Input family

Exact retained roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary input certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

Each root is an exact source cylinder

\[
X=r+2^h m
\]

with a finite integer parameter interval and exact bit refinement.

## Closed tools relevant to the join

### Forward/source side

- exact source cylinder and parameter-bit refinement;
- finite interval payload compression;
- target ballot/dominance control;
- scalar physical score `P` and one `P_min` label per exact active source/payload key.

### Right-H/checkpoint side

- terminal ternary predicates `L=24,28,47` are right-local at the critical cut;
- one-dimensional projective interval payload;
- prescribed right-H cylinders are empty/singleton for `m>=18`;
- right-H observation is affine in the ordinary checkpoint;
- synchronized `2^27 × 3^28` CRT exposure gives at most one ordinary `Z` in the SAFE checkpoint corridor.

### New source-fiber bridge

For a supplied ordinary checkpoint `Z`, the independent debit corridor

\[
75\,2^{33}<3X-Z<112\,2^{33}
\]

turns each source root into an exact `m` interval.

For root depth `h`, the number of compatible integer parameters is at most

\[
K_h=\left\lceil\frac{37\,2^{33}}{3\,2^h}\right\rceil.
\]

Current caps:

| `f` | `h=f+1` | `K_h` |
|---:|---:|---:|
| 2 | 3 | 13,242,815,830 |
| 5 | 6 | 1,655,351,979 |
| 8 | 9 | 206,918,998 |
| 10 | 11 | 51,729,750 |
| 13 | 14 | 6,466,219 |
| 16 | 17 | 808,278 |
| 18 | 19 | 202,070 |
| 21 | 22 | 25,259 |
| 24 | 25 | 3,158 |
| 27 | 28 | 395 |
| 29 | 30 | 99 |
| 32 | 33 | 13 |
| 35 | 36 | 2 |
| 37 | 38 | 1 |

Deep-root totals per exposed checkpoint:

`f>=24 -> 3,668`

`f>=27 -> 510`

`f>=29 -> 115`

`f>=32 -> 16`

`f>=35 -> 3`

`f>=37 -> 1`.

Use:

- `../theorems/SYNCHRONIZED_CHECKPOINT_SOURCE_FIBER_BOUND.md`;
- `../src/A0_s1_routeB_synchronized_checkpoint_source_fiber_certificate.py`.

## Active architecture — hybrid synchronized join

The old plan of forcing every source root toward ordinary-X singleton depth before checkpoint synchronization is no longer canonical.

### Phase A — compressed right-H export

Construct only right-H projective/carry export states that can supply the actual synchronized observation required by the checkpoint join.

Do not enumerate a flat `3^28` carry space.

### Phase B — checkpoint exposure

For each coherent pair

`(Z mod 2^27, z_H mod 3^28)`,

use the closed CRT seam to obtain zero or one ordinary `Z` in the SAFE corridor.

### Phase C — checkpoint-conditioned source fiber

For every exposed `Z`, intersect each relevant root's original `[m_lo,m_hi]` with

\[
\frac{Z+75\,2^{33}-3r}{3\,2^h}<m<
\frac{Z+112\,2^{33}-3r}{3\,2^h}.
\]

Deep roots may then be enumerated exactly because their fibers are tiny.

Shallow roots remain compressed and continue with `P_min`/source refinement.

### Phase D — exact membership handoff

For every surviving `(source fiber, Z, right-H state)`, preserve the exact long pre-bridge correction-language obligation. A small fiber or singleton `(X,Z)` is not yet a membership theorem.

## Immediate computation target

The current principal target is the **compressed right-H synchronized export state**.

Required output:

1. exact state coordinates sufficient to produce `z_H mod 3^28` and the boundary/control data used by the join;
2. exact merge rule across multiple right-H histories;
3. no flat carry enumeration;
4. exact finite state counts clearly labeled as execution evidence;
5. exported synchronized observations fed immediately into the source-fiber intersection above.

## Forward execution policy

Forward `P_min` scans remain valid and useful, especially for shallow roots. They are now predicate-driven rather than an obligatory full precomputation for all roots.

A preliminary exact scan on the deepest root `f=37` showed strong Bellman merging but no physical-score closure through the tested ordinary-X exposure horizon. This finite observation is diagnostic execution evidence only and is not promoted to a theorem.

## Merge rules

Allowed:

- one `P_min` per exact future-control + source payload state for the directed physical gate;
- one-dimensional `Pi3_k` quotient under its certified carry-cylinder scope;
- max-slack merge only for the stated fixed-carry formation-existence predicate;
- direct source-fiber intersection after an ordinary `Z` is actually exposed.

Not allowed:

- merge histories with different future controls;
- discard carry base solely because interval payloads match;
- infer whole-path injectivity from one-step injectivity;
- singleton prescribed cylinder -> unique carry path;
- small source fiber -> membership;
- one `(X,Z)` pair -> same orbit without pre-bridge language verification;
- multiply marginal dyadic/ternary/source survival ratios;
- use later refined bounds retroactively.

## Next milestone success criterion

Produce a reproducible table of **actual right-H export states** and, for each exported synchronized observation that exposes a checkpoint, report:

- the ordinary `Z` or no-corridor result;
- root-wise exact source-fiber counts;
- exact deep-root candidates when the fiber is small enough to enumerate;
- shallow-root compressed states retained;
- closure reason or next unresolved predicate for every joined family.

Finite counts remain execution evidence unless a separate general theorem proves them.

## Global warning

Even complete closure of all current 14 Route-B roots would not prove Collatz. Route-A, `s>=2`, remaining formation sectors, and global branch completeness remain separate obligations.
