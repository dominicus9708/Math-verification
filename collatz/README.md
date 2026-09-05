# Collatz proof-attempt workspace

This directory is the audited Collatz proof-attempt workspace in `Math-verification`.

The repository records exact lemmas, certified finite arithmetic, safe necessary pruning, rejected proof routes, and open obligations separately.  Nothing in this directory should be read as a proof of the Collatz conjecture unless the complete proof map and all global obligations are explicitly closed.

## Start here

1. [`PROOF_MAP.md`](PROOF_MAP.md) — global module map and proof obligations.
2. [`CANONICAL_PROOF_STACK.md`](CANONICAL_PROOF_STACK.md) — shortest current live implication chain.
3. [`status/CURRENT_STATUS.md`](status/CURRENT_STATUS.md) — current stopping point.
4. [`status/OPEN_GATES.md`](status/OPEN_GATES.md) — unresolved gates only.
5. [`frontier/A0_S1_ROUTEB.md`](frontier/A0_S1_ROUTEB.md) — active computation frontier.
6. [`status/DEPENDENCY_LEDGER.md`](status/DEPENDENCY_LEDGER.md) — dependency order and non-retroactivity rules.

## Current high-level position

The active branch is the Stage-4 `A0, s=1, Route-B` reduction.

The currently retained long-search object is an exact 14-root arithmetic forest with first threshold disagreement

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

The present mathematical frontier is not flat parity-word enumeration.  It is the compressed long-membership problem built from:

- exact source cylinders and interval refinement;
- H/L ballot grammar and target hierarchy;
- projective dyadic/ternary observation states;
- monotone normalized correction defect;
- min-plus / physical-risk lower-bound propagation;
- checkpoint and tail compatibility when those predicates become active.

No remaining 14-root family is currently declared globally closed.

## Directory roles

### Canonical control layer

- `README.md` — entry point only.
- `PROOF_MAP.md` — global modules `C0..C6`.
- `CANONICAL_PROOF_STACK.md` — current live theorem chain only.
- `status/` — current status, open gates, dependency ledger, status semantics.
- `frontier/` — only the currently active unresolved calculations.

### Mathematical record layer

- `notes/` — legacy chronological research record.  Existing paths are intentionally preserved during the non-disruptive reorganization.
- `src/` — legacy executable certificate/source location.  Existing Python paths are preserved because many certificates import one another directly.
- `results/` — generated or recorded result data.
- `wolfram/` — Wolfram-language material.

### Role indexes added by the reorganization

- `theorems/` — index of reusable exact mathematical statements.
- `certificates/` — index of executable verification certificates and execution policy.
- `audits/` — DSD scope/dependency/overclaim/counterexample audit index.
- `experiments/` — exploratory calculations that are not promoted to proof objects.
- `archive/` — rejected, superseded, or historical-route policy and migration index.

These role directories initially index existing `notes/` and `src/` files instead of physically moving them.  This avoids breaking imports and historical links.  New work should follow the new classification first; physical migration of legacy files is a separate audited maintenance phase.

## Status vocabulary

Use only the meanings defined in [`status/STATUS_LEGEND.md`](status/STATUS_LEGEND.md).

The important separation is:

- **EXACT / CLOSED** — proved algebraically within the stated domain;
- **CERTIFIED ARITHMETIC** — finite exact computation with a certificate;
- **SAFE NECESSARY PRUNING** — necessary restriction only;
- **REGRESSION ONLY** — implementation guard, never the proof;
- **REJECTED** — invalid proof step or abandoned search strategy, retained for audit;
- **OPEN** — unresolved obligation.

## Non-disruptive reorganization rule

During this first reorganization phase:

- do not delete historical research records;
- do not move Python files that are imported by path/name until import dependencies are audited;
- do not silently rewrite an old status into a stronger one;
- canonical documents point to legacy evidence rather than duplicating mathematical claims;
- a later migration may physically relocate files only with redirects/import fixes and a dependency check.
