# Chronological research notes

This directory is the chronological evidence/history layer of the Collatz proof attempt.

It is intentionally **not** the canonical resume point anymore.

Start from:

- `../README.md`
- `../PROOF_MAP.md`
- `../CANONICAL_PROOF_STACK.md`
- `../status/CURRENT_STATUS.md`
- `../frontier/A0_S1_ROUTEB.md`

## What remains here

- dated derivations;
- intermediate theorem drafts;
- scope audits;
- negative results;
- historical stopping-point records;
- detailed calculations supporting later canonical summaries.

Existing filenames are preserved for reproducibility and dependency history.

## Status warning

A dated note may describe the best-known state **at its date**, but later notes may have strengthened, rejected, or narrowed it.

Therefore do not infer current status from filename date alone.  Current classification is controlled by the top-level proof map and `status/` documents.

## New note rule

New dated notes are still allowed for detailed derivations, but every note that changes the active proof state should also update the corresponding canonical file in the same work cycle.

Examples:

- new exact theorem → update `../theorems/README.md`;
- new proof-interface rejection → update `../audits/README.md`;
- current bottleneck changes → update `../frontier/A0_S1_ROUTEB.md` and `../status/CURRENT_STATUS.md`;
- module closes/opens → update `../PROOF_MAP.md` and `../status/OPEN_GATES.md`.
