# MATH-224 — dyadic carry shell and exact closure of the high-L r=10 singleton branch

Date: 2026-09-19

Status: EXACT SHELL REDUCTION / L>=54 CLOSED / r=10 REMAINDER L=13..53

## 1. Exact shell identity

At singleton resolution write the current boundary anchor as

Y = A_L + 2^L d,   0 <= A_L < 2^L,   d >= 1.

The current first-cell hard window gives

2^71 < Y < 2^73.

Let b=bit_length(d), so 2^(b-1) <= d < 2^b.

From Y<2^73 we get b<=73-L.

From Y<2^L(d+1) and Y>2^71 we get d>=2^(71-L), hence b>=72-L.

Therefore

boxed: L + bit_length(d) is either 72 or 73.

Thus zero-cost prefix depth and carry magnitude are not independent state axes.

## 2. Consequences

For r=10 danger MATH-202 gives L>=13, hence bit_length(d)<=60.

Conversely, the high-L region L>=54 has carry bit length at most 19.

The zero-carry case d=0 is already closed by MATH-221.

## 3. Exact high-L support audit

Use the unchanged MATH-058R phase/address generator. For every paid-exit source cell with 54<=L<=72:

1. retain every lift t in the exact first-cell interval;
2. require the actual paid-exit opening endpoint to be odd;
3. form the exact boundary anchor Y=R+2^L t;
4. deduplicate Y;
5. iterate the exact shortcut map until Y<=2^71.

This deliberately audits a superset of r=10-danger states: no r=10 paid-cluster condition is needed. Therefore descent of the whole set closes the r=10 subbranch automatically.

## 4. Exact results

| L | unique paid-exit boundary anchors | max additional shortcut steps to <=2^71 |
|---:|---:|---:|
| 54 | 96,611 | 302 |
| 55 | 336,790 | 356 |
| 56 | 133,153 | 267 |
| 57 | 16,754 | 225 |
| 58 | 49,968 | 260 |
| 59 | 10,699 | 243 |
| 60 | 6,641 | 176 |
| 61 | 5,779 | 212 |
| 62 | 676 | 213 |
| 63 | 1,336 | 212 |
| 64 | 667 | 166 |
| 65 | 11 | 86 |
| 66 | 223 | 141 |
| 67 | 63 | 142 |
| 68 | 18 | 95 |
| 69 | 27 | 113 |
| 70 | 3 | 80 |
| 71 | 4 | 79 |
| 72 | 2 | 80 |

Total distinct-per-L audited anchors (counted separately by L) = 659,425.

Every one descends exactly to the frozen floor. No cycle or unresolved orbit occurs.

## 5. r=10 consequence

Every singleton r=10 danger state with L>=54 is closed, independently of the detailed r=10 paid-cluster continuation.

Together with MATH-221, the remaining r=10 singleton branch is

d != 0 and 13 <= L <= 53.

Equivalently, by the shell identity, the remaining carry has at least 19 binary magnitude bits.

## 6. Architectural role

This is a support closure of the small-carry shell, not the intended final architecture.

The theorem-facing state still uses the common formula L+bit_length(d) in {72,73}; no per-L loop is introduced into the main recurrence.

The finite audit is retained as an exact terminal certificate for the shell where the common carry state has become small.

## Claim boundary

L>=54 singleton paid-exit shell is CLOSED in the current first-cell scope. The remaining L=13..53 nonzero-carry branch and the full r=10 layer remain OPEN.