# Critical-cut terminal precision absorption

Status: **EXACT / CLOSED for terminal ternary predicates**

## Statement

Consider an equal-count block split

\[
T=AB,\qquad W=A'B',
\]

where the corresponding right blocks `B,B'` contain exactly `q_B` one-events.
For correction difference

\[
\Delta(T,W)=3^{q_B}\Delta(A,A')+2^{|A|}\Delta(B,B'),
\]

and an incoming right-side projective carry `z`, define

\[
G_B(z)=\Delta(B,B')+2^{|B|}z.
\]

For a terminal predicate modulo `3^L`, the projective block-carry law says:

- if `L <= q_B`, the full divisibility/residue predicate is decided entirely inside the right block;
- only when `L > q_B` can a residual carry of precision `L-q_B` cross the cut.

Equivalently, the exact ternary precision exported across the cut is

\[
\boxed{L_{cut}=\max(0,L-q_B).}
\]

Hence when `q_B >= L`, no ternary residue coordinate is observable across the cut for that terminal predicate.

## Current A0 s=1 Route-B cut

At the certified critical cut,

\[
q_B=397{,}573{,}380.
\]

The active terminal precisions are

\[
L\in\{24,28,47\}.
\]

Therefore

\[
L_{cut}=0
\]

for all three.

In particular, for the synchronized checkpoint predicate at `L=28`, a prescribed

\[
z_H\pmod{3^{28}}
\]

is an **input observation to the right-H filter**. After the right H factor has accepted or rejected that observation, no `mod 3^k` projective carry from this predicate remains to be joined to the left/source front.

## Exact export state consequence

For this predicate, the right-H cut export need retain only:

1. the exact boundary/grammar control coordinates queried by subsequent formation membership;
2. an exact feasibility/acceptance state for the prescribed terminal observation;
3. any independent cost/defect coordinate that a later predicate genuinely queries.

It need **not** retain the terminal checkpoint projective residue itself after the right block has consumed all `L` digits.

Within one identical surviving boundary/control class, histories that differ only in the already-consumed terminal ternary carry are indistinguishable to this downstream checkpoint predicate and may forget that residue coordinate.

## Scope restriction

This is predicate-relative state forgetting.

It does **not** prove that two histories with different:

- boundary grammar controls,
- formation-language obligations,
- physical defect/cost data,
- or other independent residue predicates

may be merged.

It also does not enumerate which `z_H` observations are accepted by the right-H language.

## Dependency

This theorem uses only the already closed projective block-carry law and the certified critical-cut one-count.

Canonical executable guard:

- `../src/A0_s1_routeB_critical_cut_terminal_precision_absorption_certificate.py`

## DSD audit classification

### EXACT / CLOSED

- precision consumption `L -> max(0,L-q_B)`;
- zero terminal-ternary residue dimension at the current cut for `L=24,28,47`;
- predicate-relative forgetting of the consumed residue coordinate.

### OPEN

- compressed exact right-H acceptance representation over prescribed `z_H`;
- actual accepted synchronized observations;
- checkpoint-conditioned 14-root join;
- full pre-bridge membership.

### NOT CLAIMED

- unique right-H path;
- merge across different boundary controls;
- root closure;
- Route-B or Collatz closure.
