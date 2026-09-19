# MATH-243 — post-r10 first-coefficient-failure bridge removes the depth-183 sign cutoff

Date: 2026-09-19

Status: EXACT SYNCHRONIZED FIRST-FAILURE BRIDGE / POST-J r=10 / r=10 OPEN

## 1. Starting branch

MATH-235 retains only frozen r=10 full factors with

3^Q > 2^H.

The MATH-065/MATH-206 factor generator constructs these factors inside the coefficient-surviving boundary language: every internal prefix remains coefficient-valid, and the completed factor is still coefficient-expanding.

Therefore a proof-facing survivor entering the post-r10 continuation has not yet experienced its first coefficient failure.

## 2. Continue in the same synchronized origin

Use the MATH-188 synchronized source coordinates

N=A+2^H s,
Y=T^H(N)=B+3^Q s.

Future shortcut refinement increments the same global H and Q. The source N is not rebased.

As long as

3^Q > 2^H,

the coefficient still survives.

The first later prefix satisfying

3^Q < 2^H

is therefore exactly the first coefficient failure of that same synchronized source.

## 3. MATH-196 closes every such first failure before A0

MATH-196 proves that the first scalar-hard first-coefficient failure occurs only at

(A0,q0)=(114208327604,72057431991).

Hence every first coefficient failure with

H < A0

is source-independently strict descent for every source above the frozen floor.

Consequently, on a post-MATH-235 synchronized r=10 continuation,

boxed: first later coefficient contraction with H<A0 => CLOSED.

This uses the same original source N. It does not reset the origin at a later boundary anchor.

## 4. Entire multi-source r=10 horizon lies far below A0

MATH-235 survivors have source resolution R<=38.

MATH-236 gives at most 38 additional dyadic refinement bits while the continuation remains multi-source.

The frozen r=10 full factors have H<=89, and the actual post-J range is smaller; the conservative bound is sufficient:

H <= 89+38 = 127.

Since

127 << A0,

every coefficient contraction that can occur before post-r10 singletonization is automatically a scalar-safe first failure.

Therefore:

boxed:
while the post-r10 continuation remains multi-source,
either it remains coefficient-expanding or it closes immediately at its first coefficient contraction.

## 5. Stronger executable rule

For the synchronized post-J r=10 executor there is no need to stop coefficient-sign pruning at H=183.

The exact rule is:

- if 3^Q>2^H, propagate;
- if 3^Q<2^H and this is the first failure, close by MATH-196, provided H<A0.

The MATH-235 input guarantees the executor begins before any failure, so the first observed sign flip is the required first failure.

Any practical exact continuation capped at 1000 extra shortcut steps remains enormously below A0.

## 6. Relation to MATH-239

MATH-239 remains a valuable stronger statement of sign equivalence for arbitrary contracting prefixes through depth 183, including prefixes that are not necessarily first failures.

MATH-243 is different:

- it applies only to the first contraction of the synchronized post-r10 survivor;
- but for that first contraction it inherits MATH-196's enormous depth range H<A0.

This is exactly the condition needed by MATH-241.

## 7. Claim boundary

Established:
- every post-MATH-235 coefficient contraction before singletonization is a synchronized first failure;
- every such contraction occurs below H<=127 and is closed by MATH-196;
- MATH-241 may safely prune the first coefficient contraction without the depth-183 cutoff.

Not established:
- closure of a path that remains coefficient-expanding through singletonization;
- closure of every singleton tail;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.