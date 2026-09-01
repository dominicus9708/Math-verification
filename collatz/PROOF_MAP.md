# Collatz proof map

This file is the module-level map for the Collatz proof attempt.  It is intentionally stricter than the chronological research notes: a module is closed only when its stated obligation is closed, not merely when supporting calculations exist.

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

**Status:** CLOSED as a SAFE reduction, not as global membership closure.

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

C2 output is the input family for C3–C5.

---

## C3 — Exact structural compression

**Purpose:** represent the huge long candidate families without literal parity-word enumeration.

**Status:** major components CLOSED; combined adaptive membership state remains partly OPEN.

Closed structural components include:

- exact source-cylinder affine transducer;
- fixed-count ballot/dominance reductions;
- exact dual H/L canonical grammar;
- target H/L–Stern-Brocot alignment only after target specialization;
- dyadic prefix localization;
- ternary suffix-carry/projective locality;
- interval four-state payload compression;
- fixed-resolution correction-family quotients;
- projective carry → position/displacement cylinder interface.

Scope restrictions:

- arbitrary H/L members are not declared Christoffel;
- target-collision coordinates are not membership rejection predicates;
- fixed-resolution compactness is not automatically adaptive/global compactness.

---

## C4 — Defect accumulation and physical closure functional

**Purpose:** convert structural/projective restrictions into a monotone lower bound on actual correction defect and compare it with the physical source interval.

**Status:** ACTIVE FRONTIER.

Closed ingredients include:

- normalized defect semiring;
- exact projective-cylinder defect floors;
- displaced-rank and phase-weighted defect bounds;
- inverse physical defect budget;
- min-plus merging principles;
- integer defect numerator / physical-risk scalar reductions developed in the current frontier.

Current target:

- run these states on the actual 14-root source forest;
- determine where family-level physical closure occurs before singleton expansion;
- add checkpoint/projective predicates lazily only when required.

C4 is the current computation module.

---

## C5 — A0 `s=1` Route-B long-membership closure

**Purpose:** eliminate or exactly classify every candidate represented by the 14-root forest through the complete pre bridge and required tail/checkpoint conditions.

**Status:** OPEN — principal local proof gate.

Necessary end state:

- every 14-root descendant either closes by a certified physical/membership failure or reaches an exact compatible realization that is then handled by the remaining predicates;
- correction-language membership, checkpoint/tail coherence, renewal/C4F/global formation conditions are not silently replaced by marginal observations;
- no unresolved infinite or unbounded family remains.

C4 supplies the intended family-level closure engine for C5.

---

## C6 — Route-A, `s>=2`, and remaining global branches

**Purpose:** close every branch not covered by the current A0 `s=1` Route-B analysis and reconnect the local results to C0.

**Status:** OPEN / later stage.

Includes at minimum:

- Route-A independent lower-bound obligation;
- all-surplus `s>=2` sectors;
- any remaining A/non-A or formation branches required by C0;
- final global completeness audit.

---

# Current critical path

The current live path is

`C0 scope` → `C1 A0 s=1` → `C2 14 roots` → `C3 compressed state` → **`C4 defect/min-plus`** → **`C5 long membership`** → `C6 remaining branches` → `C0 global closure`.

Work should not jump from C4/C5 to a global Collatz claim while C0 or C6 is open.

# Proof-interface audit rules

1. A finite regression may validate code but cannot close an algebraic theorem by itself.
2. A SAFE necessary bound may prune candidates but cannot establish membership of survivors.
3. A target-collision mismatch is an observation unless an independent membership gate requires it.
4. Endpoint exposure does not imply same-orbit connectivity.
5. Marginal cardinalities/residue densities are never multiplied without a proved independence/product theorem.
6. An exact theorem is used only inside its stated formation domain.
7. Dependency order is recorded in `status/DEPENDENCY_LEDGER.md`; later stronger bounds cannot be used retroactively to justify earlier computations unless a new certificate explicitly reruns that dependency.
