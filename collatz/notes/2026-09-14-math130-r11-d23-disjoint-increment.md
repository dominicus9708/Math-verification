# MATH-130 — r=11 disjoint depth-23 complete-cycle increment

Status: `MAINLINE FINITE AUDIT / CONSERVATIVE EXACT INCREMENT / r=11 OPEN`

Date: 2026-09-14

## Purpose

MATH-129 constructs the exact logical union of every MATH-125 safe prefix gate through depth 22 and certifies

```text
safe mass  = 3,209,065,424,947
tail mass  =   210,653,636,613
```

on the exact MATH-116 prepared r=11 source.

MATH-130 asks one narrow question: does depth 23 certify any **new** source residue that was not already MATH-129-safe?

## Disjoint depth-23 increment

For each source residue `r mod 2^23`, let

```text
L_old(r) = max_{1<=d<=22} L(d,q_d(r)),
L_23(r)  = L(23,q_23(r)),
```

where MATH-125 defines

```text
L(d,q)=floor((2^d*2^71-c_max(d,q))/3^q).
```

A source maximum `N` belongs to the new depth-23-only safe set exactly when

```text
L_old(r) < N <= L_23(r).
```

Therefore the new set is disjoint from the MATH-129 depth-1..22 safe union by construction.

## Exact complete-cycle counting

For an odd-step AP `n=a+bk`, odd `b` makes

```text
k -> a+bk mod 2^23
```

a permutation on each complete `2^23`-parameter cycle.

MATH-130 counts only complete cycles. Incomplete remainders are deliberately assigned zero additional safe mass. Hence the result is a conservative exact lower bound and cannot overcount the new safe subset.

The residue interval condition `(L_old,L_23]` is counted by sorting all improving lower and upper thresholds. For an AP source maximum `N`, the exact number of newly safe residues in one complete cycle is

```text
# {r : L_old(r) < N <= L_23(r)}.
```

## Exact result

```text
prepared split pieces                         605,977
total source occurrence mass           3,419,719,061,560
depth-23 modulus                            8,388,608
residues with stronger d=23 threshold       2,489,262
rows with complete d=23 cycles                 13,702
complete-cycle mass examined          3,249,377,640,448
rows with positive new increment                 2,135
max new-safe residues / complete cycle          58,040
new disjoint d=23 safe mass              3,151,665,357
```

Combining the disjoint increment with MATH-129 gives the conservative certified bound

```text
safe mass >= 3,212,217,090,304
tail mass <=   207,501,971,256
safe fraction >= 93.93219245439003%
```

The uncounted incomplete depth-23 remainders can only increase the safe mass if audited later; they cannot invalidate this lower bound.

## Interpretation

MATH-130 proves that extending the exact q-gate beyond depth 22 yields genuine new certified source classes. It does not establish that repeated depth extension eventually exhausts the tail.

The remaining `207,501,971,256` is an upper bound on the still-uncertified source mass after this conservative increment, not a set of counterexamples.

## Claim boundary

```text
MATH-129 + MATH-130 safe mass >= 93.93219245439003%
```

does **not** imply `r=11 CLOSED`.

The exact full MATH-116 AP-union closure remains the independent complete gate, and exact address-sensitive/deeper-prefix work is still required if that workflow has not completed.

Authoritative artifacts:

```text
collatz/src/2026_09_14_math130_r11_d23_disjoint_increment.cpp
collatz/results/2026-09-14-math130-r11-d23-disjoint-increment.tsv
collatz/notes/2026-09-14-math130-r11-d23-disjoint-increment.md
```
