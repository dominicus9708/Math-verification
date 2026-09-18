# MATH-222 — weighted carry saturation for arbitrary low-paid danger sequences

Date: 2026-09-19

Status: EXACT NESTED-SELECTOR SATURATION / VARIABLE-r / r=10 NONZERO CARRY OPEN

## 1. Initial singleton carry budget

After MATH-217, consider a singleton boundary anchor Y with 0<Y<2^73 and a dangerous zero-cost prefix of length L0.

Write Y=A0+2^L0 d0 with 0<=A0<2^L0. On the remaining nonzero branch:

1 <= d0 < 2^(73-L0).

Thus the initial ordinary carry has fewer than 73-L0 binary magnitude bits.

## 2. Nested selector

For a fixed legal sequence of later dangerous factors, MATH-205 gives

2^Z_m d_m = 3^Q_m d0 + K_m

where Z_m is the sum of the later overshoot depths.

Hence continuation through the fixed factor sequence selects exactly one residue class

d0 = -3^(-Q_m) K_m  (mod 2^Z_m).

MATH-202 gives z_i >= z_min(r_i) for every dangerous emitted paid count r_i. Therefore

Z_m >= sum_i z_min(r_i).

## 3. Weighted saturation theorem

If

sum_i z_min(r_i) >= 73-L0,

then 2^Z_m >= 2^(73-L0), while 1<=d0<2^(73-L0).

Therefore the selected residue class contains at most one admissible ordinary carry d0.

In formula:

sum_i z_min(r_i) >= 73-L0  =>  at most one ordinary d0 for the fixed symbolic factor sequence.

This is exact nested dyadic selection, not a density or probability claim.

## 4. r=10 consequence

For r=10, z_min(10)=13. Since the first dangerous r=10 prefix already has L0>=13,

73-L0 <= 60.

Hence five later dangerous r=10 continuations force

Z >= 5*13 = 65 > 60.

So any fixed chain consisting of an initial singleton r=10 danger factor plus five further dangerous r=10 continuations has at most one admissible initial nonzero carry.

Equivalently, after at most six r=10 dangerous factor occurrences in one fixed symbolic lineage, the original singleton boundary anchor is exact rather than an AP family.

## 5. Common low-r consequence

For an arbitrary sequence r_i in {2,...,10}, define the remaining carry budget

B = 73-L0 - sum_i z_min(r_i).

Every dangerous continuation decreases this budget by at least z_min(r_i).

Once B<=0, the ordinary initial carry is unique.

The same scalar budget handles all remaining paid counts; r is an emitted tag, not an outer loop.

## 6. Relation to zero carry

If the unique selected residue is d0=0, MATH-221 closes that branch.

If it is nonzero, the exact singleton source is

Y=A0+2^L0 d0

and may be passed to the synchronized Hensel/global-defect terminal gate.

## 7. Claim boundary

Established:
- one weighted carry-bit budget for arbitrary mixed low-paid danger sequences;
- uniqueness of ordinary initial carry once the accumulated z_min budget reaches 73-L0;
- at most five later r=10 danger continuations are needed after the first singleton r=10 danger factor.

Not established:
- that every unique nonzero carry candidate descends;
- emptiness of all saturated symbolic factor sequences;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.