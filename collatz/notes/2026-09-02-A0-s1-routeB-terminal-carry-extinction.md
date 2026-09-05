# 2026-09-02 — A0 s=1 Route-B terminal carry extinction

## Goal

Determine how much of the critical-cut right-H factor can actually affect the synchronized terminal observation modulo `3^L`.

## Exact chart

The already-certified backward exponential carry chart is

`z_i = 3 z_(i+1) - 2^A_i + 2^B_i`.

After `k` right-indexed one-gates,

`z_0 = 3^k z_k + sum_(i=0)^(k-1) 3^i(2^B_i-2^A_i) mod 3^L`.

If `k>=L`, both the unresolved deeper carry term and every gate term with index `i>=L` vanish modulo `3^L`.

Therefore

`z_0 = sum_(i=0)^(L-1) 3^i(2^B_i-2^A_i) mod 3^L`.

## Current consequence

For the synchronized checkpoint precision `L=28`, only the first 28 right-indexed one-gates of the right H block can affect `z_H mod 3^28`.

The right H factor contains `397,573,380` one-events, so exactly

`397,573,352`

deeper one-events are invisible to this 28-trit export.

Likewise:

- 24-trit terminal observation -> first 24 right-indexed one-gates;
- 28-trit checkpoint observation -> first 28;
- 47-trit terminal observation -> first 47.

## DSD audit

### EXACT / CLOSED

- `3^L` extinction of the unresolved deeper carry after L gates;
- invisibility of all gates at indices `i>=L` modulo `3^L`;
- finite-gate locality for the current 24/28/47-trit predicates.

### EXECUTION GUARD

`../src/A0_s1_routeB_terminal_carry_extinction_certificate.py`

was executed locally using exact integer arithmetic on 2026-09-02 and returned `PASS`. The finite examples in that file check implementation/orientation only; the theorem is the algebraic divisibility statement.

No GitHub Actions run is claimed by this note.

### OPEN

The remaining G2 object is the legal ordered 28-gate slack/carry chart and its compact exact quotient/export. Residue locality does not by itself prove that an arbitrary 28-gate vector extends through the complete right-H formation language.

### REJECTED

- carry/base can always be discarded before L gates have been absorbed;
- 28-gate residue locality -> unique 28-gate carry path;
- prescribed singleton cylinder -> unique whole path;
- terminal residue agreement -> full correction-language membership.

## Canonical objects

- `../theorems/TERMINAL_CARRY_EXTINCTION_AND_FINITE_GATE_LOCALITY.md`
- `../src/A0_s1_routeB_terminal_carry_extinction_certificate.py`
