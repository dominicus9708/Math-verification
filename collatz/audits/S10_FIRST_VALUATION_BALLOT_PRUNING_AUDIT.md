# S10 first valuation-ballot pruning audit

Date: 2026-09-03

Status: **SAFE additional pruning / Route-B remains OPEN**

## Input

The existing retained 14-root forest contains exactly

\[
125{,}072{,}439{,}875{,}999{,}947{,}649
\]

integer source parameters after the previously certified SAFE inputs.

Each root has exact form

\[
X=r+2^h m,
\qquad
Y=T^h(X)=y+3^q m,
\]

and every root begins this stage with pure-ballot surplus

\[
S=q-Q(h)=1.
\]

## Predicate

Partition each root by the exact next-state valuation

\[
a=v_2(Y).
\]

Because the lift coefficient `3^q` is odd, every valuation class is one exact parameter cylinder modulo `2^(a+1)`.

The next parity block is forced to be

\[
0^a1.
\]

The entire block is pure-ballot valid iff

\[
S\ge Q(h+a)-Q(h)
\]

and

\[
S+1\ge Q(h+a+1)-Q(h).
\]

No endpoint information is used.

## Result

Allowed next valuations are:

- roots `f = 2,5,10,13,18,21,24,29,32,37`: `a in {0,1}`;
- roots `f = 8,16,27,35`: `a in {0,1,2}`.

After the exact first jump, the retained count is

\[
\boxed{94{,}018{,}492{,}189{,}951{,}139{,}878}.
\]

Additional exact SAFE rejection:

\[
\boxed{31{,}053{,}947{,}686{,}048{,}807{,}771}.
\]

This is approximately `24.8287694050%` of the previous 14-root population.

## DSD audit

### Domain

Only the already certified A0 `s=1` Route-B retained roots are used.

### Resolution

Parameter counts and valuation cylinders are exact integer arithmetic.

### Independence

No density multiplication is used. The removed set is explicitly counted as a disjoint union of exact valuation residue classes.

### Future-state preservation

The pruning predicate is only pure ballot. Surviving children still require H/L/C4F/checkpoint/tail controls before any merge or closure claim.

### Closure classification

- first valuation-cylinder partition: **EXACT**;
- pure-ballot block rejection: **EXACT**;
- application after upstream SAFE root pruning: **SAFE additional pruning**;
- S10 family realization: **OPEN**;
- Route-B: **OPEN**;
- Collatz: **OPEN**.

## Certificate

- `../src/A0_s1_14root_first_valuation_ballot_pruning_certificate.py`
