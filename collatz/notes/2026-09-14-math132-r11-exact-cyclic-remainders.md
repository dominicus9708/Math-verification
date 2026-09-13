# MATH-132 — r=11 exact cyclic-remainder extension

Status: `MAINLINE FINITE AUDIT / EXACT LOWER-BOUND STRENGTHENING / r=11 OPEN`

Date: 2026-09-14

## Purpose

MATH-131 exhausted the complete-cycle-only extension of the MATH-125 floor-safe gate through depth 34. Its lower bound intentionally assigned zero credit to every incomplete `2^D` parameter remainder for `D>=23`.

MATH-132 restores exact address information on those remainders. For a prepared AP piece

```text
P(a,b,m),  b odd,
```

and modulus `2^D`, write

```text
m = blocks * 2^D + rem.
```

The complete blocks are the MATH-131 contribution. The residual parameter interval is mapped exactly by

```text
k -> a + b k (mod 2^D).
```

Because `b` is odd, multiplication by `b` is invertible modulo `2^D`; each remainder is therefore an exact cyclic interval in the permuted residue order. The scanner counts only residues that were not safe at any earlier prefix depth but become MATH-125-safe exactly at depth `D`.

## Exact results

```text
D=23
complete-cycle increment   3,151,665,357
exact remainder increment    147,454,842
exact D=23 increment        3,299,120,199

D=24
complete-cycle increment  17,456,818,136
exact remainder increment  1,221,965,686
exact D=24 increment       18,678,783,822

D=25
complete-cycle increment  15,350,900,431
exact remainder increment  1,841,592,242
exact D=25 increment       17,192,492,673
```

These remainder increments are pairwise disjoint from all earlier prefix-depth safe classes by construction.

Combining MATH-131 with the new exact remainders through `D=25` gives

```text
certified safe mass >= 3,289,358,348,815
uncertified tail   <=   130,360,712,745
safe fraction      >= 96.18797011104378%
```

## Resource observation

The direct scanner stores the depth-`D` innovation predicate over all residues modulo `2^D` and then traverses the 32 observed odd-step classes. This remains practical through `D=25`, but the naive `D=26` run hit the execution-resource limit before completion.

This is an implementation/resource barrier, not a mathematical failure of the gate. MATH-133 replaces the repeated depth-by-depth parity simulation with an exact dyadic recursion and parallelized residue-order scan.

## Claim boundary

MATH-132 does not close `r=11`. It strengthens only the exact finite safe subset. The remaining tail is not a counterexample and is not asserted to survive the Collatz dynamics.
