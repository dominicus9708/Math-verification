# 2026-09-02 — A0 s=1 Route-B dyadic checkpoint-index / right-H isometry

## Goal

Reduce the synchronized join state after the right-H side has specified a residue cylinder, without enumerating ordinary checkpoints or a flat `3^28` residue space.

## Exact coordinate

Fix

`z2 = Z mod 2^27`

and write

`Z = z2 + 2^27 n`.

The already-certified right-H affine observation becomes

`zH(n) = A(z2) + u*n mod 3^28`,

where

`u = 2^(s+27) mod 3^28 = 15,139,992,122,704`

is a unit with inverse

`u^-1 = 13,299,776,895,097 mod 3^28`.

Therefore for every `ell<=28`,

`zH(n1)=zH(n2) mod 3^ell`

iff

`n1=n2 mod 3^ell`.

A prescribed right-H cylinder thus pulls back to one arithmetic progression in the checkpoint-index coordinate `n`.

## SAFE slice size

For fixed `z2`, the ordinary checkpoint corridor becomes one consecutive integer interval `I_z2` in `n`.

The maximum number of integers in any such slice is

`17,592,186,046,876`,

strictly below

`3^28 = 22,876,792,454,961`.

Hence the full 28-trit right-H observation is injective on each SAFE dyadic checkpoint slice.

## Consequence

The already-closed one-dimensional ternary interval quotient `Pi3` can be reused directly on `I_z2`.

This turns the G2 -> G3 handoff into

`fixed z2 × checkpoint-index Pi3 × exported right-H residue cylinder`

instead of a flat checkpoint/residue enumeration.

## DSD classification

### EXACT / CLOSED

- affine checkpoint-index map;
- unit/isometry theorem;
- unique cylinder pullback at every precision `ell<=28`;
- exact SAFE index interval;
- uniform slice cardinality `<3^28`;
- compatibility with `Pi3`.

### CERTIFICATE / execution

`../src/A0_s1_routeB_dyadic_checkpoint_index_rightH_isometry_certificate.py`

was also executed as standalone exact-integer arithmetic on 2026-09-02 and returned `PASS`.

This local execution is separate from GitHub Actions; no Actions run is claimed here.

### STILL OPEN

The theorem does not construct the admissible multi-gate right-H carry/formation paths. It only compresses their exported residue-cylinder interface.

### REJECTED

- discard carry base because checkpoint-index is 1D;
- prescribed cylinder -> unique carry path;
- `Pi3` -> full right-H language membership;
- one checkpoint -> source/orbit membership;
- marginal ratio multiplication.

## Canonical objects

- `../theorems/DYADIC_CHECKPOINT_INDEX_RIGHT_H_ISOMETRY.md`
- `../src/A0_s1_routeB_dyadic_checkpoint_index_rightH_isometry_certificate.py`
