# Collatz proof map

This file is the module-level map for the Collatz proof attempt.  It is intentionally stricter than the chronological research notes: a module is closed only when its stated obligation is closed, not merely when supporting calculations exist.

Two proof paths are now tracked separately where necessary:

- **internal/self-contained path** — uses only the repository's own DSD/source/formation machinery;
- **external-dependency path** — may invoke audited published finite-range Collatz results as lemmas.

The two paths must not be conflated.

## C0 — Global branch specification and completeness

**Purpose:** state exactly which Collatz counterexample classes must be eliminated for the global conjecture and prove that the branch decomposition covers them.

**Status:** OPEN / partially structured.

Required closure:

- exact branch partition;
- no omitted surplus/formation class;
- translation from local branch closure to the ordinary Collatz conjecture.

No `A0` calculation by itself closes C0.

---

## C1 — A0 and minimal-surplus (`s=1`) formation

**Purpose:** define the A0 checkpoint, pre/tail split, minimal-surplus constraints, and the exact formation language used downstream.

**Status:** substantial exact structure CLOSED locally; global scope remains dependent on C0.

Representative evidence:

- `notes/2026-08-27-A0-s1-Xi-Minkowski-factorization.md`;
- checkpoint / pre-tail formation certificates in `src/`;
- exact cross-checkpoint ordering and `s=1` product factorization results.

Important scope rule: `s=1` statements are not promoted to `s>=2`.

---

## C2 — Near-threshold closure and finite 14-root reduction

**Purpose:** replace the original physical A0 shell by a finite exact family of long-search source cylinders.

**Status:** CLOSED as a SAFE reduction.

Established chain includes:

- radius `0..7` finite closure;
- every survivor has first-75 Hamming distance at least `8`;
- monotone prefix defect and refined physical X bound;
- late first-defect shell elimination;
- exact remaining 14-root arithmetic forest.

Canonical evidence includes:

- `src/A0_s1_radius7_defect_christoffel_real_envelope_certificate.py`;
- `src/A0_s1_prefix_defect_membership_pruning_certificate.py`;
- `src/A0_s1_14root_long_membership_forest_certificate.py`.

C2 output is the input family for the internal C3–C5 path.

---

## C3 — Exact structural compression

**Purpose:** represent the huge long candidate families without literal parity-word enumeration.

**Status:** major components CLOSED; combined adaptive membership state remains partly OPEN on the internal path.

Closed structural components include:

- exact source-cylinder affine transducer;
- fixed-count ballot/dominance reductions;
- exact dual H/L canonical grammar;
- target H/L–Stern-Brocot alignment only after target specialization;
- dyadic prefix localization;
- ternary suffix-carry/projective locality;
- interval four-state payload compression;
- fixed-resolution correction-family quotients;
- projective carry → position/displacement cylinder interface;
- terminal defect → right-H projective observation state reduction;
- source terminal-descriptor endpoint lattice.

Scope restrictions:

- arbitrary H/L members are not declared Christoffel;
- target-collision coordinates are not membership rejection predicates;
- fixed-resolution compactness is not automatically adaptive/global compactness;
- derived `F_28` and `z_H` are not independent filters.

---

## C4 — Defect accumulation and physical closure functional

**Purpose:** convert structural/projective restrictions into a monotone lower bound on actual correction defect and compare it with the physical source interval.

**Status:** ACTIVE only for the self-contained internal Route-B path.

Closed ingredients include:

- normalized defect semiring;
- exact projective-cylinder defect floors;
- displaced-rank and phase-weighted defect bounds;
- inverse physical defect budget;
- min-plus merging principles;
- exact integer defect numerator / physical-risk scalar reductions;
- horizon-51 `D_51>=6` and the resulting `eta_future>1/2` floor.

The internal path still lacks a complete family-level closure mechanism before source singleton expansion.

---

## C5 — A0 `s=1` Route-B long-membership closure

**Purpose:** eliminate or exactly classify every candidate represented by the 14-root forest through the complete pre bridge and required tail/checkpoint conditions.

### External-dependency path

**Status: CLOSED for counterexample-source rejection.**

The internally certified source corridor is

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33}.
\]

Bařina's finite verification through `2^71`, combined with Ansari's 2025 recursive-sufficiency interval extension at `n=44`, covers every positive integer up to

\[
4\,3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526,
\]

which strictly exceeds the current Route-B source upper bound.

Therefore the current physical `A0,s=1,Route-B` source corridor contains no genuine Collatz counterexample source if those published finite-range results are accepted as lemmas.

Canonical dependencies:

- `theorems/EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CORRIDOR_CLOSURE.md`;
- `src/A0_s1_external_recursive_sufficiency_source_corridor_closure_certificate.py`;
- `audits/S10_EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CLOSURE_AUDIT.md`;
- `frontier/A0_S1_ROUTEB_EXTERNAL_CLOSURE.md`.

### Internal/self-contained path

**Status: OPEN as an independent reconstruction.**

The remaining internal objective is still the source-preserving late-activation / exact terminal-descriptor construction followed by the local membership obligations.

This path remains useful as a DSD-method test and may yield reusable theorems for sectors not covered by the same external finite interval.

---

## C6 — Route-A, `s>=2`, and remaining global branches

**Purpose:** close every branch not covered by the current A0 `s=1` Route-B analysis and reconnect the local results to C0.

**Status:** OPEN / now the principal global path after external Route-B closure.

Includes at minimum:

- Route-A independent lower-bound obligation;
- all-surplus `s>=2` sectors;
- any remaining A/non-A or formation branches required by C0;
- final global completeness audit.

The next global-progress task is to recover the exact branch definitions and source domains for these sectors before transferring any Route-B theorem to them.

---

# Current critical paths

## External-dependency path

`C0 scope` → `C1 A0 s=1` → `C2 source corridor` → **`C5 Route-B externally CLOSED`** → **`C6 remaining branches`** → `C0 global closure`.

This is now the shortest live route toward wider Collatz coverage.

## Internal/self-contained path

`C0 scope` → `C1 A0 s=1` → `C2 14 roots` → `C3 compressed state` → `C4 defect/min-plus` → **`C5 internal Route-B membership OPEN`**.

This remains a research/audit path, not the shortest closure path for the current finite Route-B source interval.

# Proof-interface audit rules

1. A finite regression may validate code but cannot close an algebraic theorem by itself.
2. A SAFE necessary bound may prune candidates but cannot establish membership of survivors.
3. A target-collision mismatch is an observation unless an independent membership gate requires it.
4. Endpoint exposure does not imply same-orbit connectivity.
5. Marginal cardinalities/residue densities are never multiplied without a proved independence/product theorem.
6. An exact theorem is used only inside its stated formation domain.
7. Dependency order is recorded in `status/DEPENDENCY_LEDGER.md`; later stronger bounds cannot be used retroactively to justify earlier computations unless a new certificate explicitly reruns that dependency.
8. An external finite-range theorem may close a finite source corridor, but it is not relabeled as an internally derived DSD theorem.
9. Local branch closure is never promoted to global Collatz while C0 or C6 remains open.
