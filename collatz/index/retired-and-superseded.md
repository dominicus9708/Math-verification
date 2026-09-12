# Retired, superseded, redundant, and insufficient routes

This ledger records **what is no longer used and why**. Raw files are not deleted.

Important: retiring a strategy, quotient, filter interpretation, or implementation does not imply that every theorem inside the old file is false.

## Status vocabulary

- `SATURATED`: further use of this route cannot provide the required new exclusion.
- `INSUFFICIENT QUOTIENT`: the compressed state forgets information required to distinguish real same-integer paths from fictitious ones.
- `REDUNDANT`: a purported independent filter carries information already present elsewhere.
- `SUPERSEDED`: a later stronger result replaces the old result as the active calculation input.
- `INVALID INFERENCE`: a valid local result had been at risk of being promoted beyond its scope.
- `IMPLEMENTATION SUPERSEDED`: the mathematical object is retained but represented more efficiently or safely.

## 1. Scalar correction-only route at the 340-block frontier

Status: `SATURATED / RETIRED AS CLOSURE ROUTE`.

The first universal cell contains exactly 340 top-address blocks `a=1024,...,1363`. Scalar correction alone does not produce a universal block exclusion beyond this frontier.

Replacement: exact same-integer address transduction and dyadic carry compatibility.

## 2. Phase-forgetting right-congruence quotient — MATH-007

Status: `INSUFFICIENT QUOTIENT`.

Distinct exact 340-label masks retain essentially the full endpoint phase information in the low-surplus range. A nontrivial exact coarse quotient that forgets phase cannot provide the needed pruning.

Replacement: preserve phase.

## 3. Fixed block exclusion from phase sparsity — MATH-008

Status: `SATURATED`.

All 2048 lower-61 endpoint phases actually occur wherever the MATH-006 address transducer can reject labels (`q61=39..45`).

Retired inference:

```text
per-phase surviving-label cap -> fixed globally excluded address labels
```

Replacement: phase-specific same-integer address tracking.

## 4. Independent endpoint-ordering and root-Hensel-ordering filters — MATH-009

Status: `REDUNDANT`.

Within one fixed `(k,q,E)` endpoint fiber, the two orderings are the same affine order in opposite coordinates.

Retired object: treating them as two independent pruning mechanisms.

Preserved object: the affine identity itself.

## 5. Re-applying the address lift

Status: `INVALID REPRESENTATION`, blocked by MATH-010.

`BASE_ENDPOINT -> ADDRESS_LIFTED` is permitted exactly once. Applying the top-address affine term to an already lifted state double-counts the address contribution.

Replacement: typed representation gate.

## 6. Promoting arithmetic-credit failure to Collatz-candidate failure

Status: `INVALID INFERENCE`.

MATH-012 proves that one specific frozen-floor Hensel arithmetic-credit predicate is exactly equivalent to

```text
k-q <= 71.
```

The implication

```text
k-q > 71 -> Collatz candidate excluded
```

is prohibited.

Preserved object: the exact arithmetic-credit descriptor and its use as a cheap gate for that mechanism.

## 7. Scalar paid-macro slope as a final closure mechanism — MATH-058 route

Status: `SUPERSEDED AS FINAL MECHANISM`.

MATH-058's exact accounting

```text
K <= 72P + 89
```

and cumulative penalty bound remain valid in their audited scope. They are preserved as a historical mainline pivot.

What is retired is the expectation that a single scalar worst-case macro length/slope is sufficient to close the first universal cell.

Replacement: weighted/exact macro transitions with same-integer carry/address state.

## 8. Boolean phase danger kernel without address — MATH-094

Status: `SATURATED / INSUFFICIENT QUOTIENT`.

The address-forgotten resolution/phase danger kernel saturates and cannot distinguish fictitious phase paths from same-integer paths.

Replacement: exact carry/address compatibility.

## 9. Bellman state `(R, phase, accumulated penalty)` — MATH-095

Status: `EXACT NEGATIVE ABSTRACTION RESULT / INSUFFICIENT QUOTIENT`.

All 857 actual initial states retain a negative path in the address-forgotten Bellman envelope even after exact phase transport and complete accumulated positive penalty are retained.

This does **not** prove existence of a bad Collatz trajectory. Forgetting the address enlarges the language and creates fictitious paths.

Retired proof-facing state:

```text
(R, phase, accumulated penalty)
```

Required replacement:

```text
(R, phase, exact finite 2-adic carry/address descriptor, ...)
```

## 10. Carrying unnecessary infinite/high 2-adic precision

Status: `IMPLEMENTATION SUPERSEDED BY MATH-096`.

For current source resolution `R=ceil(log2 M)`, MATH-096 proves that

```text
P(R)=73+R
```

2-adic bits suffice for every future one-paid address decision.

Replacement compact state:

```text
X mod 2^(73+R)
G=3^{-Q} mod 2^(73+R)
```

plus exact source multiplicity, phase, and source-modulus depth information.

## 11. Historical frontier snapshots

Status: `SUPERSEDED STATUS ONLY`.

The unresolved detailed one-paid band changed as finite closures accumulated:

```text
7..16
7..15
...
7..10
7..9
```

Older statements that a wider band is open are preserved as historically correct snapshots at their commit time. They must not be read as the current state.

## Not automatically retired

The following are not placed in the retired set merely because they are not current terminal dependencies:

- exact negative results and countermodels;
- historical structural calculations whose later role has not been fully classified;
- computational acceleration certificates;
- representation-safety checks;
- intermediate lemmas absorbed by later results.

Those remain in `side-branches.md` unless an explicit retirement/supersession reason is documented here.
