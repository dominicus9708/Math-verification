# MATH-181 — joint r=1..21 first-return executor prototype

Date: 2026-09-17

Status: `PROTOTYPE / EXACT RECURRENCE IMPLEMENTED / CANONICAL REGRESSION PENDING`

This implements the MATH-180 recurrence in executable form.

## Implemented structure

For each paid-exit source, the prototype:

1. refines the source phase interval once by all next 21 exact phase cuts;
2. computes one fixed future epsilon/phase schedule on each common cell;
3. runs one exact dyadic first-return tree from slack `u=1`;
4. preserves the source congruence `t=a (mod 2^h)` exactly;
5. reconstructs the affine coefficient as `3^(q0+j)` instead of storing it;
6. tags every first-return terminal by paid count `r=j`;
7. applies the MATH-180 all-layer potential `Psi_j` only when every possible future target layer is rigorously safe;
8. emits or aggregates tagged AP cylinders for all `r=1..21` in one traversal.

Implementation:

`collatz/src/2026_09_17_math181_joint_r1_r21_first_return_executor.py`

## Structural regression performed during derivation

An independent exact-rational scratch regression compared the joint first-return tree against the original fixed-target recurrence on several exact phase/address cells for each target `r=1..5`.

For every tested target layer, the terminal affine cylinders matched exactly.

This checks the recurrence transformation itself, but it is not yet the canonical repository regression.

## Promotion requirements

Before MATH-181 may replace the target-specific executor, it must pass all of the following:

- full source-coverage audit for the common 21-cut phase partition;
- exact occurrence-mass conservation per tagged paid-count layer;
- same-integer address semantics regression;
- canonical comparison against MATH-115 layers `r=2..12`;
- downstream closure regression against already closed high-r layers;
- explicit audit of `r=1` semantics against the existing one-paid branch.

Because common phase refinement is finer than the canonical target-r partitions, raw AP row count is not itself an invariant. Required invariants are represented-set coverage, multiplicity mass, exact address semantics, and downstream closure.

No new paid layer, first universal Farey cell, or Collatz closure claim is made.
