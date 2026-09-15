# MATH-156 — generic exact giant-AP microsharder

Date: 2026-09-15

## Status

`SUPPORT / EXACT REPRESENTATION INFRASTRUCTURE / REGRESSION-PASSED / NO r=10 CLOSURE CLAIM`

MATH-153 initially encoded the exact 64-way split inline for original `r=10` shard 0. MATH-156 factors that operation into a reusable source primitive:

```text
collatz/src/2026_09_15_math156_exact_single_ap_microsharder.py
```

For a one-row AP source

```text
P(a,b,m) = {a + b*k : 0 <= k < m}
```

and requested part count `K`, the script writes consecutive exact micro-APs

```text
P(a+b*s_j, b, m_j)
```

with disjoint consecutive parameter intervals, `sum_j m_j=m`, and `max m_j-min m_j <= 1`.

## r=10 giant-regime regression

MATH-143 shows original prepared shards `0..13` are each one AP of mass

```text
215291123465.
```

The new microsharder was regression-tested locally against preserved MATH-117 prepared artifacts for original shard 0 and original shard 13, using `K=64` and an exact expected-mass assertion.

Both produced:

```text
parts          64
source mass    215291123465
minimum mass   3363923804
maximum mass   3363923805
large pieces   9
small pieces   55
sum            215291123465
```

which matches the MATH-153 pilot partition exactly.

## Role

The primitive allows later giant-shard pilots to share one audited partition implementation rather than copying inline splitting code. It changes resource scheduling only and leaves MATH-108 theorem-facing transition arithmetic unchanged.

## Claim boundary

Regression success does not close any new ordinary-integer set. MATH-156 proves only the exact representation identity implemented by the microsharder and its reproduction on two preserved giant-shard inputs.
