# MATH-127 — r=11 exact d=22 remainder-aware q-gate audit

Status: `MAINLINE FINITE AUDIT / STRICTLY STRONGER THAN MATH-126 COMMON-d COMPLETE-BLOCK CREDIT / r=11 OPEN`

Date: 2026-09-14

## Purpose

MATH-126 credited only complete parameter blocks of length `2^22` and assigned zero credit to every incomplete remainder. MATH-127 removes that conservatism by counting the remainder source residues exactly.

## Exact residue structure

For each prepared source AP

```text
P(a,b,m),  b odd,
```

the parameter map

```text
k -> a+bk mod 2^22
```

is a permutation on a complete period. The r=11 prepared artifact has only 32 distinct values of `b mod 2^22`.

For each such odd step class, MATH-127 constructs the exact length-`2^22` parity-weight sequence and circular prefix sums for the MATH-125 safe conditions `q<=12` and `q<=13`. An AP remainder is then an exact cyclic interval in that parameter sequence; no density approximation is used.

## Exact result

Input representation:

```text
split pieces:           605,977
total occurrence mass:  3,419,719,061,560
distinct b mod 2^22:    32
```

At depth `d=22`:

```text
Q_safe=12 pieces:       27,420
Q_safe=13 pieces:      578,557
exact safe mass:     2,904,383,883,175
exact tail mass:       515,335,178,385
safe fraction:          84.930482033517819%
```

The observed largest prepared source value is

```text
6,290,339,729,165,775,182,359.
```

## Claim scope

The safe mass consists of explicitly countable source-parameter residue classes whose length-22 parity words satisfy the sharp MATH-125 frozen-floor envelope. Those occurrences are exactly discharged.

The remaining `515,335,178,385` source occurrences are not declared surviving Collatz candidates. They are only the part not certified by this particular `d=22` q-gate and still require exact-address or longer-prefix treatment.

This is source occurrence mass in the exact MATH-116 representation, not natural density and not necessarily a count of unique ordinary integers across historical source records.

## Relation to MATH-126

MATH-126 guaranteed `2,811,463,801,368` safe occurrences by giving every incomplete remainder zero credit. MATH-127 raises the exact `d=22` certificate to `2,904,383,883,175` by resolving those remainders exactly.

No r=11 closure claim follows from the percentage alone.
