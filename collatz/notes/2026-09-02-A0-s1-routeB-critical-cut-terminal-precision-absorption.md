# A0 s=1 Route-B — critical-cut terminal precision absorption audit

Date: 2026-09-02

## Question

Does the synchronized 28-trit checkpoint predicate require a ternary projective carry coordinate to cross the existing critical cut?

## Exact answer

No.

The certified projective block-carry law consumes exactly one ternary digit per one-event in the processed right block. Therefore a terminal precision `L` leaves

\[
L_{cut}=\max(0,L-q_R)
\]

digits at the cut.

For the current right H factor,

\[
q_R=397{,}573{,}380.
\]

Hence for `L=24,28,47`,

\[
L_{cut}=0.
\]

The synchronized checkpoint observation `z_H mod 3^28` must be tested inside the right H factor, but after that test its ternary carry coordinate is fully consumed and must not be carried into the left/source join merely because it existed at the terminal boundary.

## State consequence

The canonical G2 state is reduced from the previous conceptual form

`right-H carry/projective state × boundary control`

at the cut to

`right-H acceptance/feasibility × exact boundary control`

for this specific terminal checkpoint predicate, plus only independent coordinates later predicates genuinely query.

This does not eliminate the problem of representing the accepted family of terminal observations `z_H`; it eliminates only the unnecessary residual ternary state after the right block has decided one such observation.

## DSD audit

### EXACT / CLOSED

- precision absorption `L -> max(0,L-q_R)`;
- zero checkpoint ternary residue dimension at the cut;
- predicate-relative forgetting after observation discharge.

### REJECTED

- carrying the consumed `z_H` residue through the cut as if still observable;
- using zero residual precision to claim a unique right-H history;
- merging different boundary/grammar controls.

### OPEN

- compact representation of the set of accepted prescribed `z_H` observations;
- actual synchronized checkpoint/source joins;
- pre-bridge membership.

## Canonical objects

- `../theorems/CRITICAL_CUT_TERMINAL_PRECISION_ABSORPTION.md`;
- `../src/A0_s1_routeB_critical_cut_terminal_precision_absorption_certificate.py`.
