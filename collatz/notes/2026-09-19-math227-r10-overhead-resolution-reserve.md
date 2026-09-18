# MATH-227 — 89-step overhead absorbs the full r=10 factor plus all unresolved source bits

Date: 2026-09-19

Status: PARTIAL EXACT GEOMETRY / H+R<=73 VALID / LOCAL 89-RESET WITHDRAWN

## 1. Purpose

MATH-060 proves that the first cell is closed if the cumulative penalty satisfies

P_K >= lambda (K-89),   lambda=19/503.

MATH-197 proves that while source multiplicity is >1, each exact parity decision is Bellman-safe after adding the resolution potential -lambda R.

This note shows that for every unresolved frozen r=10 factor, the 89-step allowance is already large enough to absorb both

1. the entire initial r=10 factor length, and
2. every unresolved source bit that remains in its output family.

## 2. Geometry of one exact full factor

Write an exact full r=10 factor as

source = A + 2^H s,
target = B + 3^Q s,
0 <= s < M.

Let R=ceil(log2 M), with R=0 for M=1.

Every source boundary anchor in the current first-cell scope is <2^73 by MATH-057.

Assume M>=2. Since R=ceil(log2 M),

M-1 >= 2^(R-1).

Also

A + 2^H(M-1) < 2^73.

Hence

2^(H+R-1) <= 2^H(M-1) < 2^73,

so

boxed: H+R <= 73.

This is independent of shard geometry and ordinary occurrence mass.

## 3. Resolution-consumption budget

Starting from the output family, follow exact shortcut decisions until the source family first reaches R_t=0.

Let t be the number of additional shortcut steps and P_fut their accumulated penalty.

MATH-197 gives at each step

p_i - lambda + lambda(R_i-R_(i+1)) >= 0.

Summing to singletonization gives

P_fut - lambda t + lambda R >= 0,

hence

P_fut >= lambda(t-R).

The initial r=10 factor penalty is nonnegative, so for total depth K=H+t,

P_total >= lambda(t-R).

Subtract the MATH-060 target:

P_total - lambda(K-89)
>= lambda(t-R) - lambda(H+t-89)
= lambda(89-H-R).

Using H+R<=73:

boxed: P_total - lambda(K-89) >= 16 lambda.

Thus every multi-source frozen r=10 output reaches the exact singleton regime with at least sixteen step-equivalents of global Bellman reserve.

## 4. Initial singleton factors

If M=1, then no resolution budget is needed.

For the still-unresolved part after MATH-224 we have L<=53. The r=10 paid first-return cluster has h_10<=17, so

H=L+h_10 <=70.

Hence already at the end of the initial factor

P_total - lambda(H-89) >= lambda(89-H) >=19 lambda.

If instead L>=54, MATH-224 closes the exact boundary source directly.

Therefore every r=10 branch not already closed by MATH-224 enters the singleton continuation with at least

boxed: 16 lambda

of conservative MATH-060 reserve.

## 5. Consequence

The unresolved r=10 problem does not have to pay again for converting the 27.5-trillion represented AP mass into a singleton.

The 89-step first-cell overhead pays for the entire initial factor plus the source-resolution collapse.

After singletonization, only later negative Bellman transfers can consume the >=16 lambda reserve.

Any later transfer with nonnegative local Bellman increment preserves or increases this reserve.

## 6. Correct remaining problem

The remaining obstruction is therefore:

an exact singleton path, starting with >=16 lambda reserve, that after zero or more locally Bellman-safe transfers reaches a later negative transfer large enough to exhaust the reserve before terminal descent.

This is strictly narrower than arbitrary continuation from the full r=10 AP workload.

## Claim boundary

Established:
- H+R<=73 for every multi-source exact r=10 factor in the current first-cell boundary window;
- resolution collapse to singleton cannot violate the MATH-060 global slope;
- every unresolved r=10 continuation enters singleton with at least 16 lambda global reserve.

Not established:
- closure of an arbitrary later negative transfer after intervening safe transfers;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.

## Scope correction — 2026-09-19

The geometric statement

[
H+Rle73
]

for the local frozen r=10 factor family is exact and retained.

However the subsequent use of

[
89-H-R
]

as a fresh Bellman reserve at an interior r=10 boundary is not a valid global MATH-060 inference.

The constant 89 is a one-time additive allowance for the complete synchronized first-cell path. It cannot be reset at each imported local macro origin.

Therefore the following claims from the original version are withdrawn from the proof mainline:

- every r=10 continuation receives at least (16lambda) fresh reserve;
- the local factor plus its resolution collapse may be paid from a newly restarted 89-step allowance;
- any later danger may be compared against that locally restarted reserve.

Correct use:

- retain (H+Rle73) as local source-geometry information;
- carry Bellman reduced cost from the synchronized MATH-188 origin;
- use only edge increments
  [
  p-lambdaell+lambda(R-R')
  ]
  locally, as in MATH-074/197.

The companion certificate remains a regression of the valid (H+Rle73) geometry only.
