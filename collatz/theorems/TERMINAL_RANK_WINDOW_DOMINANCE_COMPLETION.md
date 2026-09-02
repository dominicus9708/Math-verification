# Terminal ranked-one window and dominance completion

Status: **EXACT / CLOSED for equal-count target-dominance residue existence**

## Setup

Let target and candidate one positions be

\[
a_1<\cdots<a_q,
\qquad
b_1<\cdots<b_q,
\qquad
b_r\le a_r.
\]

For fixed equal count `q`, the correction difference has the ranked-one form

\[
\Delta
=
\sum_{r=1}^{q}3^{q-r}\left(2^{a_r}-2^{b_r}\right).
\]

Consider a terminal residue predicate modulo `3^L`, with `L<=q`.

## Terminal rank-window theorem

Every term with

\[
q-r\ge L
\]

vanishes modulo `3^L`.

Therefore

\[
\boxed{
\Delta\bmod3^L
=
\sum_{r=q-L+1}^{q}3^{q-r}
\left(2^{a_r}-2^{b_r}\right)
\bmod3^L.
}
\]

Thus only the final `L` ranked one-events can affect the terminal `3^L` residue.

For the current synchronized checkpoint predicate `L=28`, only the final 28 ranked one-events of the right H factor are residue-observable.

## Dominance completion theorem

Suppose candidate positions have been chosen only for the final `L` ranks,

\[
b_{q-L+1}<\cdots<b_q,
\]

and satisfy

\[
b_r\le a_r
\]

for those ranks, together with enough room for the omitted prefix:

\[
b_{q-L+1}\ge q-L.
\]

Then define the earlier candidate positions by the packed prefix

\[
\boxed{b_r=r-1\qquad(1\le r\le q-L).}
\]

Because every increasing target sequence satisfies

\[
a_r\ge r-1,
\]

we have `b_r<=a_r` on the packed prefix. Also

\[
b_{q-L}=q-L-1<b_{q-L+1},
\]

so the full candidate sequence is strictly increasing.

Hence every locally legal final-rank window satisfying the standard slack lower bound extends to a complete equal-count target-dominant candidate.

In right-indexed slack coordinates

\[
B_t=(q-t-1)+s_t,
\qquad
s_t\ge0,
\]

the final processed gate `t=L-1` automatically has

\[
B_{L-1}=q-L+s_{L-1}\ge q-L,
\]

which is exactly the required room condition.

## Current right-H consequence

For

\[
q_H=397{,}573{,}380
\]

and terminal precision

\[
L=28,
\]

pure target-dominance acceptance of a prescribed checkpoint ternary residue is equivalent to existence in a finite **28-gate ordered-slack/projective suffix problem**.

The earlier

\[
q_H-28=397{,}573{,}352
\]

one-events do not need to be enumerated for this residue-existence predicate.

The current last-28 target capacities are obtained from

\[
a_r=\left\lceil\frac{(r-1)J_0}{R_0}\right\rceil-1
\]

for the right-H target word and are checked by the companion certificate.

## Scope restriction

This theorem closes **target-dominance residue existence**, not every possible boundary label of the full H/L grammar.

If a later join asks for an additional H-grammar boundary/control state, that state must be intersected with the 28-gate accepted suffix set separately.

Likewise, physical defect/cost and full pre-bridge correction-language membership remain separate predicates.

## Canonical certificate

- `../src/A0_s1_routeB_terminal_rank_window_dominance_completion_certificate.py`

## DSD audit classification

### EXACT / CLOSED

- terminal `3^L` residue depends only on final `L` ranked one-events;
- packed-prefix completion of every locally legal suffix under target dominance;
- current `L=28` right-H dominance acceptance is a 28-gate problem.

### OPEN

- compact execution of the actual 28-gate accepted `z_H` set;
- additional H-grammar boundary/control intersection if required;
- synchronized 14-root join;
- full membership.

### NOT CLAIMED

- uniqueness of the 28-gate path;
- small accepted-set cardinality;
- root closure;
- Route-B or Collatz closure.
