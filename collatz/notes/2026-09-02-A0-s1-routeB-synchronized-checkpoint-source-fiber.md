# 2026-09-02 — A0 s=1 Route-B synchronized checkpoint source fiber

## Question

After the synchronized dyadic/right-H pair exposes at most one ordinary checkpoint `Z`, how much of each retained 14-root source family can still be compatible with that checkpoint before running the full long pre-bridge membership test?

## Exact reduction

For one root

`X = r + 2^h m`

and the independent debit corridor

`75*2^33 < 3X-Z < 112*2^33`,

substitution gives an open interval for `m` of width

`37*2^33 / (3*2^h)`.

Therefore one exposed checkpoint can intersect the root in at most

`K_h = ceil(37*2^33/(3*2^h))`

integer source parameters.

## 14-root result

`f : K_h`

- `2 : 13,242,815,830`
- `5 : 1,655,351,979`
- `8 : 206,918,998`
- `10 : 51,729,750`
- `13 : 6,466,219`
- `16 : 808,278`
- `18 : 202,070`
- `21 : 25,259`
- `24 : 3,158`
- `27 : 395`
- `29 : 99`
- `32 : 13`
- `35 : 2`
- `37 : 1`

Deep-root cumulative caps per exposed `Z`:

- `f>=24 : 3,668`
- `f>=27 : 510`
- `f>=29 : 115`
- `f>=32 : 16`
- `f>=35 : 3`
- `f>=37 : 1`

## Interpretation

This is a structural join compression, not a membership result.

The previous plan implicitly treated forward source compression and checkpoint exposure as mostly separate until a late boundary. The new exact fiber bound permits a hybrid execution: once one synchronized observation exposes `Z`, immediately intersect each relevant source root with its exact debit-compatible `m` interval.

For the deep roots, singleton expansion becomes cheap only after this synchronization. In particular, `f=37` has at most one source integer for any exposed `Z` and the three roots `f>=32` have at most sixteen source parameters in total per exposed checkpoint.

For shallow roots, the fiber remains too large for naive enumeration, so the `P_min`/source quotient remains necessary.

## DSD audit

### EXACT / CLOSED

- source-cylinder substitution into the ordinary debit identity;
- open interval width;
- lattice cardinality cap;
- all listed root-specific values.

### REGRESSION ONLY

A standalone exact-integer certificate was executed locally on 2026-09-02 and printed `PASS`; its endpoint samples are implementation guards, not the proof of the general theorem.

The corresponding GitHub certificate is committed, but this note does not claim GitHub Actions execution unless a workflow result is separately recorded.

### REJECTED

- treating a small fiber as proof of correction-language membership;
- treating one `(X,Z)` pair as same-orbit connectivity without the long word check;
- multiplying the fiber cap by independent-looking dyadic/ternary ratios;
- retroactively inserting the later defect-derived X bound into this theorem.

## Canonical objects

- `../theorems/SYNCHRONIZED_CHECKPOINT_SOURCE_FIBER_BOUND.md`
- `../src/A0_s1_routeB_synchronized_checkpoint_source_fiber_certificate.py`

## Next computation

Use the hybrid join.

1. keep shallow roots compressed;
2. obtain synchronized right-H/dyadic checkpoint observations;
3. expose `Z` by the closed CRT seam;
4. intersect source roots with exact checkpoint fibers;
5. directly enumerate the deep-root fibers when small;
6. continue exact compressed refinement for shallow unresolved fibers.
