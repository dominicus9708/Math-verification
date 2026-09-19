# MATH-238 — affine-orientation coherence across every frozen low-paid layer r=2..12

Date: 2026-09-19

Status: EXACT CROSS-LAYER REGRESSION / NO INTERNAL J-CROSSING IN FROZEN FACTORS / SYMBOLIC THEOREM TARGET

## 1. Exact affine comparison

For every frozen negative-candidate full factor

N(s)=A+2^H s,
Y(s)=B+3^Q s,
0<=s<M,

the orbit gap is

Y(s)-N(s) = (B-A) + (3^Q-2^H)s.

An internal self-descent crossing could occur only if the intercept gap B-A and slope gap 3^Q-2^H have opposite signs.

## 2. Audit result

The unchanged MATH-065 exact factor generator was audited for every frozen layer r=2..12.

For every factor in every layer:

boxed: sgn(B-A)=sgn(3^Q-2^H).

There were zero opposite-sign factors and zero exact-zero cases.

Therefore every frozen factor cylinder is orientation coherent:

- B<A and 3^Q<2^H: every represented source self-descends;
- B>A and 3^Q>2^H: every represented source is above its start at that prefix.

No factor contains an internal J sign crossing.

## 3. Exact counts

| r | factor records | whole-descend | whole-survive |
|---:|---:|---:|---:|
| 12 | 1,053,555 | 728,442 | 325,113 |
| 11 | 605,972 | 191,117 | 414,855 |
| 10 | 278,725 | 183,189 | 95,536 |
| 9 | 141,002 | 59,287 | 81,715 |
| 8 | 65,811 | 36,989 | 28,822 |
| 7 | 29,342 | 17,337 | 12,005 |
| 6 | 15,133 | 6,074 | 9,059 |
| 5 | 6,525 | 4,381 | 2,144 |
| 4 | 3,675 | 1,244 | 2,431 |
| 3 | 1,873 | 1,076 | 797 |
| 2 | 1,116 | 578 | 538 |

## 4. Interpretation

MATH-235's r=10 all-or-none J split is not isolated numerical behavior. The same orientation coherence occurs across the entire frozen low-paid frontier.

This strongly points to a common coefficient-sign theorem rather than an r-specific terminal threshold table.

MATH-239 supplies exactly such a theorem through synchronized depth 183 for every source N>2^71, thereby explaining this frozen orientation audit without treating the factor records as proof premises.

## Claim boundary

The frozen cross-layer audit is exact. By itself it is regression evidence; the proof-facing generalization is MATH-239. No new paid layer is declared closed by MATH-238 alone.