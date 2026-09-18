# MATH-223 — r=10 factor language is Hensel-hard through depth 41

Date: 2026-09-19

Status: EXACT FINITE NEGATIVE DIAGNOSTIC / NO PRUNING THROUGH DEPTH 41 / r=10 OPEN

## Purpose

The root-safe Hensel theorem implies that a minimal first-cell counterexample must be full-Hensel class-maximal through every root depth k<=73.

Before extending the Hensel machinery, audit whether the frozen r=10 negative-factor language is actually removed by this condition at already-controlled depths.

## Candidate compression

The 278,725 frozen r=10 leaf records collapse to 258,242 exact full factor types.

At selected root-prefix depths, the number of distinct candidate prefixes is:

| k | distinct r=10 candidate prefixes |
|---:|---:|
| 13 | 9 |
| 22 | 74 |
| 26 | 246 |
| 31 | 1,043 |
| 35 | 3,240 |
| 41 | 11,817 |

Thus the audit is performed on shared prefix signatures, not ordinary source members.

## Exact Hensel test

For each candidate prefix, group even ranks by odd-gap level G_j=e_j-j and propagate the exact MATH-051 reverse carry

h_(r-1) = 2(h_r + Delta a_r)/3,

requiring divisibility by 3 at every level.

A candidate is terminally dominated iff at least one competitor completion ends with positive integer Hensel credit.

## Result

At every audited depth above:

dominated r=10 candidate prefixes = 0.

In particular, all 11,817 distinct r=10 candidate prefixes reaching depth 41 are still full-Hensel class-maximal.

## Consequence

Hensel is not the missing primary pruning mechanism for the r=10 frontier in the currently audited range.

The mainline should therefore keep Hensel as a legality/extremality channel but place the closure burden on address/carry plus Bellman/terminal defect.

This prevents an expensive but structurally unpromising extension of the complete MATH-051 depth ledger solely for r=10.

## Claim boundary

This is finite through depth 41 only. It does not prove arbitrary-depth Hensel maximality of r=10 candidates and does not close r=10.