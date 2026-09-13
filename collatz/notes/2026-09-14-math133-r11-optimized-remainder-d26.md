# MATH-133 — optimized exact cyclic-remainder scan through D=26

Status: `MAINLINE FINITE AUDIT / IMPLEMENTATION REPAIR / EXACT LOWER-BOUND STRENGTHENING / r=11 OPEN`

Date: 2026-09-14

## Motivation

MATH-132's direct scanner is mathematically exact but recomputes every depth-`D` parity count by simulating `D` shortcut steps for each residue modulo `2^D`. The first direct `D=26` attempt hit the execution-resource limit.

This was not a failed floor gate. MATH-133 replaces the expensive parity simulation by the exact dyadic recursion

```text
q_D(2s)   = q_{D-1}(s),
q_D(2s+1) = 1 + q_{D-1}(3s+2 mod 2^(D-1)).
```

The previous best threshold is inherited from the lower residue:

```text
B_{D-1}(r) = B_{D-1}(r mod 2^(D-1)).
```

Thus the full depth-`D` innovation predicate is built in `O(2^D)` exact arithmetic rather than `O(D 2^D)` repeated shortcut simulation.

The 32 observed odd-step classes are then scanned in parallel. Threshold-index lookups are precomputed per class, while the cyclic remainder intervals remain exact.

## Regression

Before using the optimized path at `D=26`, it was replayed at `D=23` and reproduced MATH-132 exactly:

```text
complete increment   3,151,665,357
remainder increment    147,454,842
exact increment      3,299,120,199
```

Therefore the optimized representation changes execution cost, not the mathematical source set or floor-safe predicate.

## D=26 exact result

```text
complete-cycle increment   5,512,456,558
exact remainder increment    907,778,775
exact D=26 increment        6,420,235,333
```

Combining the MATH-131 complete-cycle lower bound with exact remainder increments at depths 23 through 26 gives

```text
cumulative exact remainder increment: 4,118,791,545
certified safe mass >= 3,290,266,127,590
uncertified tail   <=   129,452,933,970
safe fraction      >= 96.21451553067209%
```

## Next resource boundary

The same implementation was attempted at `D=27`, but the `2^27` address-sensitive residue scan did not complete inside the current execution window. This is again a resource boundary of the direct residue-order remainder method, not evidence against the gate.

The mathematical next step is therefore either:

1. further compress the exact remainder counting so that `D>=27` does not scan every residue for every odd-step class; or
2. hand the remaining exact tail to MATH-124 direct-address propagation / the unchanged MATH-108 AP-union engine.

## Claim boundary

MATH-133 does not close `r=11`. The remaining `129,452,933,970` source occurrences are uncertified by this gate, not counterexamples. The certified multi-paid frontier remains `r>=12 CLOSED`, `r=11 OPEN` until MATH-116 or an equivalent complete exact certificate finishes the layer.
