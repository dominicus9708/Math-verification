# DSD audit index

This directory indexes proof-scope, dependency, counterexample, and overclaim audits for the Collatz work.

Existing dated audit notes remain in `../notes/` during phase 1.  New canonical audits should be linked here and should distinguish a mathematical rejection from a search-engine rejection.

## Audit axes

### A1 — Scope audit

Checks whether a theorem is being used outside its stated domain.

Recurring examples:

- `s=1` → `s>=2` over-promotion;
- target Christoffel hierarchy → arbitrary ballot candidate;
- fixed resolution → adaptive/global resolution;
- finite horizon → universal horizon.

### A2 — Proof-interface audit

Checks whether two different mathematical objects are being conflated.

Canonical example:

- target collision / adic observation **versus** actual correction-language membership / physical rejection.

Representative note:

- `../notes/2026-09-01-A0-s1-routeB-target-collision-vs-membership-scope-audit.md`.

### A3 — Dependency / non-retroactivity audit

Checks that later stronger bounds are not used to justify earlier computations without rerunning them.

Canonical ledger:

- `../status/DEPENDENCY_LEDGER.md`.

### A4 — Counterexample-to-method audit

Actively searches for counterexamples to proposed lemmas/algorithms before they enter the canonical stack.

Current retained example:

- local carry/cylinder greedy can fail if it is used to choose the carry sequence itself;
- right-to-left greedy is retained only after the admissible cylinder sequence is fixed.

### A5 — State-sufficiency audit

Checks whether a compressed state really determines every future predicate it claims to determine.

Recurring questions:

- is source transition control still needed after an observation is discharged? usually yes;
- is a local C4F Boolean state actually preserved? currently not assumed;
- does a residue state encode membership or merely observation? keep separate.

### A6 — Double-counting / independence audit

Checks whether defect floors, cardinalities, or residue constraints are combined legally.

Rejected patterns:

- adding overlapping defect floors without disjoint support/semiring proof;
- multiplying marginal survival ratios without independence;
- counting boundary exposures as independent language sparsity.

### A7 — Search-engine audit

Checks whether mathematically exact recursion is computationally suitable for the long problem.

Example:

- exact binary completion-defect DP is valid mathematics but rejected as an uncompressed long search engine.

## Canonical rejected implications

Keep these visible:

1. `interval inclusion => correction-language membership` — REJECTED.
2. `endpoint/address exposure => same-orbit connectivity` — REJECTED.
3. `adic target mismatch => membership rejection` — REJECTED unless an explicit active gate requires equality.
4. `terminal ternary saturation => contradiction with an early defect invisible mod 3^L` — REJECTED.
5. `pure-ballot quotient preserves complete C4F state` — NOT ESTABLISHED / do not assume.
6. `local carry greedy chooses globally minimal defect` — REJECTED; only fixed-cylinder greedy survives.
7. `finite regression agreement => universal theorem` — REJECTED.

## New audit-note template

Every new canonical audit should contain:

- claim under audit;
- exact hypotheses;
- attempted implication;
- counterexample or proof of safety;
- status: `EXACT / SAFE / REJECTED / OPEN`;
- downstream files affected;
- whether `PROOF_MAP`, `CANONICAL_PROOF_STACK`, or `OPEN_GATES` must change.

## Archive rule

Rejected ideas are not deleted.  Once they are no longer needed in the active chronological notes, index them under `../archive/` with the reason for rejection and the last valid scope, so the same path is not rediscovered as if new.
