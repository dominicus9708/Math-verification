# MATH-233 — complete-boundary odd clock and 25-odd multi-source horizon after r=10

Date: 2026-09-19

Status: EXACT DEPTH-AXIS ELIMINATION / FUTURE MULTI-SOURCE ODD COUNT <=25 / r=10 OPEN

## 1. Complete boundary block

For one complete boundary factor, MATH-207 proves

3^Q / 2^H = omega / omega',

where Q is the total odd-step count of the full zero-cost-prefix + paid-cluster factor, H is its total shortcut depth, and omega,omega' are the normalized boundary phases in (1/2,1].

Put

theta = log2(3/2),
x = -log2 omega in [0,1).

Then

x' - x = Q log2 3 - H.

Modulo one, because H and Q are integers,

boxed: x' = {x + Q theta}.

This is the complete-boundary analogue of the paid-cluster rotation. The rotation amount uses total factor odd count Q, not paid count r alone.

## 2. Arbitrary complete boundary chain

For factors i=0,...,n-1 define

Q_tot = sum Q_i,
H_tot = sum H_i.

Telescope gives

3^Q_tot / 2^H_tot = omega_0 / omega_n.

Therefore

boxed: x_n = {x_0 + Q_tot theta}.

Writing x_0+Q_tot theta = m+x_n with integer m gives

boxed: H_tot = Q_tot + floor(x_0 + Q_tot theta).

So the entire depth/phase history of a complete boundary chain is determined by

- initial boundary phase;
- cumulative total odd count.

Macro segmentation is not an independent clock.

## 3. r=10 output multi-source horizon

MATH-225/MATH-232 prove that after the frozen r=10 output, every continuation that is still multi-source has accumulated future dyadic factor depth

H_tot <= R_0 <= 40.

Suppose Q_tot>=26.

MATH-051 already certifies the exact coefficient inequality

3^26 > 2^41.

Hence for H_tot<=40,

3^Q_tot / 2^H_tot >= 3^26 / 2^40 > 2.

But the boundary telescope requires

1/2 < 3^Q_tot / 2^H_tot < 2.

Contradiction.

Therefore

boxed: every still-multi-source continuation after r=10 has Q_tot <=25.

## 4. Consequences

Because every nonempty complete boundary factor has at least one odd shortcut, the number of future complete factors before singletonization is also at most 25.

The sum of future paid counts is at most Q_tot, so it too is at most 25.

This includes arbitrary mixtures of one-paid and multi-paid safe factors; no per-r outer loop is used.

## 5. State compression

Along the multi-source safe prefix:

- future total depth H_tot is derived from Q_tot and x_0;
- future boundary phase is derived from Q_tot and x_0;
- normalized inverse G=3^(-Q_global) is updated by multiplication by 3^(-Q_tot), so relative future G is also determined by Q_tot.

Therefore these quantities are not independent history coordinates.

The still-independent proof channels are

- finite normalized intercept/address X;
- source resolution R;
- inherited relative Bellman debt/credit;
- synchronized correction / terminal-defect data.

## 6. Executor consequence

The post-r10 symbolic executor may use cumulative future odd count q_fut as its only boundary clock:

0 <= q_fut <=25.

Depth and phase are derived; emitted paid count r remains an event tag at first return, not an outer loop.

This is a stronger form of the intended architecture

one recurrence + emitted r + derived depth.

## Claim boundary

Established:
- exact complete-boundary circle rotation by total odd count;
- exact cumulative depth formula;
- <=25 future odd steps in every post-r10 continuation that remains multi-source;
- <=25 complete factors and <=25 future paid events before singletonization.

Not established:
- smallness of the remaining finite address/debt state set;
- closure after singleton handoff;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.