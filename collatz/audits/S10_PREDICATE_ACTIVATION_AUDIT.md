# S10 predicate activation audit

Date: 2026-09-03

Status: **SAFE state reduction / S10 family realization remains OPEN**

## Audited question

Which coordinates must be carried persistently through the enormous A0 `s=1` Route-B pre-bridge, and which coordinates can be derived, used transiently, or activated only near the predicate that actually observes them?

Canonical theorem:

- `../theorems/PREDICATE_ACTIVATION_SCHEDULE.md`.

## D — Domain

The audit applies only to the current certified A0 `s=1` Route-B source-family representation and the already proved checkpoint-locality interfaces.

It does not define missing predicates by inference from their names.

## R — Resolution

Persistent early/middle S10 source state:

\[
(r,y,[m_{lo},m_{hi}],h,S).
\]

This resolution preserves both:

- the ordinary source family `X=r+2^h m`;
- the current orbit-state family `T^h(X)=y+3^q m`.

With pure-ballot surplus

\[
S=q-Q(h),
\]

one has

\[
q=Q(h)+S,
\]

so `q` and `3^q` are derived coordinates.

## S — State sufficiency

### Persistent

- source residue `r`;
- current affine offset `y`;
- exact parameter interval;
- absolute prefix depth `h`;
- pure-ballot surplus `S`;
- any separately defined predicate label whose future observation is already proved to require persistence.

### Derived

- current one-count `q=Q(h)+S`;
- coefficient `3^q`;
- block-affine coefficient obtainable from certified block metadata.

### Transient

- H/L or other block-grammar labels when used only to generate a certified next block `(length, one-count, correction)`;
- historical correction values after residual recursion has discharged them.

### Late-activated

- `Z mod3^28` only upon entering the suffix containing the final 28 pre-checkpoint one-events;
- `Z mod2^27` only from the first 27 post-checkpoint parity symbols;
- local same-orbit splice status only after coherent CRT observations exist.

### Not admitted without definition

- a working-label `C4F` coordinate whose exact predicate/state requirement is not yet fixed in the active Route-B stack.

## E — Equivalence / merging

This audit does not license source-payload merging merely because two states share the same active-control tuple or future ballot signature.

Two histories may be merged only after proving equality of all future realization sets for every still-active predicate.

Predicate inactivity is not the same as source equivalence.

## T — Transition

The exact multibit source-channel transducer already supplies the correct interface for a certified fixed block with metadata

\[
(b,p,\gamma=C(B)).
\]

Therefore a block grammar can remain outside the persistent state when its only role is to emit the next certified block and no future predicate inspects the discarded grammar history.

The valuation-cylinder jump is one special compressed block transition of this kind.

## C — Checkpoint locality closure

For a suffix `B` containing exactly the final `K` pre-checkpoint one-events,

\[
Z\equiv2^{-|B|}C(B)\pmod{3^K}.
\]

Hence for the current `K=28`, all earlier pre-bridge history exports zero required ternary checkpoint digits.

The post-checkpoint dyadic coordinate is separately local to the first 27 right-side parity symbols.

This closes the *activation schedule*, not checkpoint existence.

## N — Non-independence

The following must not be multiplied or counted as independent pruning information merely because they have separate representations:

- source prefix and its equivalent dyadic correction address;
- H/L representation and the same underlying formation-language membership;
- terminal target-dominance existence and the automatic genuine-checkpoint mod-3 condition;
- an exposed checkpoint residue and same-orbit provenance before the local splice hypotheses are checked.

## O — Outstanding obligations

1. continue source-family realization using the minimized persistent state;
2. locate or formally define the exact Route-B meaning of `C4F` before adding any corresponding coordinate;
3. use H/L/Christoffel block structure only where its exact admissibility semantics are certified;
4. reach the final-28-one suffix and actually expose `Z mod3^28` for surviving families;
5. obtain the post-checkpoint `Z mod2^27` observation and synchronize the CRT seam;
6. discharge debit, positivity/local splice, tail first-passage, and any separately defined renewal obligation;
7. close all 14 roots before claiming A0 `s=1` Route-B closure.

## Result

The S10 state is reduced rather than enlarged:

\[
\boxed{
(r,y,[m_{lo},m_{hi}],h,S)
}
\]

is the currently justified persistent core, with later predicates activated only when their supporting observations exist.

This prevents state explosion caused by carrying redundant or not-yet-observable coordinates through the entire `10^11`-scale pre-bridge.
