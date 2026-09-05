# Experiment index

This directory is for calculations that help discover structure but are not yet canonical proof objects.

During reorganization phase 1, most historical experiments remain in dated `../notes/`, `../src/`, and `../results/`.  New exploratory work should be classified here before promotion.

## What belongs here

- small-horizon enumerations used to guess a recurrence;
- performance/state-growth measurements;
- alternative search strategies not yet justified mathematically;
- diagnostic decimal estimates;
- candidate invariants without a proof of preservation;
- counterexample searches against a proposed lemma;
- implementation prototypes.

## What does not belong here

- a general proved theorem → `../theorems/` index;
- an executable exact certificate for a canonical claim → `../certificates/` index;
- a proof-scope/counterexample conclusion → `../audits/`;
- the current unresolved calculation → `../frontier/`;
- rejected/superseded material no longer under active investigation → `../archive/`.

## Promotion pipeline

`experiment`
→ `candidate claim`
→ `DSD audit / counterexample search`
→ `general proof and/or exact certificate`
→ `theorem/certificate index`
→ `proof map if it changes a module`.

A result does not skip the audit stage because its finite data look regular.

## Required metadata for new experiments

Record:

- date;
- branch / upstream commit;
- exact input domain;
- arithmetic mode (integer/rational/fixed-point/floating diagnostic);
- purpose;
- observed result;
- whether the result is theorem evidence, diagnostic only, or a counterexample;
- next promotion test.

## Current strategic experiments

The next planned experiment is not an unconstrained parity enumeration.  It is the exact 14-root family scan described by `../frontier/A0_S1_ROUTEB.md`.  Once its state transition and closure logic are fully certified, that object should live as a frontier/search certificate rather than remain an experiment.
