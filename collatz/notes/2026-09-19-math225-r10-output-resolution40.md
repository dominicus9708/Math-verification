# MATH-225 — frozen r=10 output families have at most 40 unresolved source bits

Date: 2026-09-19

Status: EXACT RESOLUTION CEILING / 27.5-TRILLION MASS -> 40-BIT SOURCE UNCERTAINTY / r=10 OPEN

## 1. Frozen r=10 output multiplicity

MATH-113/MATH-206 give the exact frozen r=10 negative-candidate workload:

- leaf records: 278,725;
- represented occurrence mass: 27,557,263,803,397;
- maximum single cylinder multiplicity: 830,483,089,363.

Since

2^39 < 830,483,089,363 < 2^40,

every exact r=10 output cylinder has source-resolution height

R = ceil(log2 M) <= 40.

## 2. Atomic Bellman consequence

MATH-197 proves that whenever M>=2, every legal parity decision satisfies

R' <= R-1

and its resolution-adjusted Bellman increment is nonnegative.

Therefore no future Bellman deficit can occur while any of those at most 40 unresolved source bits remain.

Every frozen r=10 output lineage must, within at most 40 compatible future shortcut decisions, do one of:

1. descend / hit an already closed terminal;
2. fail coefficient survival and be handled by the synchronized terminal defect;
3. reach R=0 and become an exact singleton.

## 3. Proof-architecture consequence

The theorem-facing r=10 continuation state does not contain the represented occurrence mass 27.5 trillion.

It contains at most a 40-bit dyadic source-resolution budget plus the common phase/correction/address channels.

This is exact and independent of the 128 execution shards.

## 4. Relation to MATH-224

Once R=0, MATH-224 closes every singleton paid-exit state with L>=54.

Thus the unresolved terminal part of the r=10 continuation is localized to:

R=0, 13<=L<=53, d!=0, plus the MATH-220 nine-cell low-address gate and synchronized defect/Hensel state.

## Claim boundary

This does not prove that all 40-bit-resolution families reach a closed singleton state; it proves only that any possible negative Bellman behavior is delayed until the exact singleton regime and that the multiplicity axis is at most 40 bits.