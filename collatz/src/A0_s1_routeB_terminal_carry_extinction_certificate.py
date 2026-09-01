#!/usr/bin/env python3
"""Exact certificate for terminal carry extinction in the backward chart.

For

    z_i = 3*z_(i+1) - 2^A_i + 2^B_i,

unrolling k gates gives

    z_0 = 3^k*z_k + sum_i 3^i(2^B_i-2^A_i).

Modulo 3^L, once k>=L the unresolved base carry and every term i>=L
vanish.  Thus an L-trit terminal observation depends only on the first L
right-indexed gates.

Finite examples are implementation guards only; the proof kernel is exact
factor divisibility by 3^L.
"""


def direct_backward(z_tail: int, A, B):
    assert len(A) == len(B)
    z = z_tail
    for a, b in zip(reversed(A), reversed(B)):
        z = 3 * z - (1 << a) + (1 << b)
    return z


def unrolled(z_tail: int, A, B):
    k = len(A)
    return (3 ** k) * z_tail + sum((3 ** i) * ((1 << B[i]) - (1 << A[i])) for i in range(k))


# Symbolic arithmetic facts needed by the current terminal windows.
for L in (1, 2, 3, 24, 28, 47):
    mod = 3 ** L
    assert (3 ** L) % mod == 0
    for i in (L, L + 1, L + 7):
        assert (3 ** i) % mod == 0

# Deterministic finite guards for the unrolling orientation and tail extinction.
for L in (1, 2, 5, 8):
    k = L + 3
    A = [7 + 2 * i for i in range(k)]
    B = [6 + 2 * i + (i % 2) for i in range(k)]

    for z_tail in (0, 1, 2, 17, 12345):
        z_direct = direct_backward(z_tail, A, B)
        z_formula = unrolled(z_tail, A, B)
        assert z_direct == z_formula

        mod = 3 ** L
        terminal_L = sum((3 ** i) * ((1 << B[i]) - (1 << A[i])) for i in range(L))
        assert z_direct % mod == terminal_L % mod

        # Changing the unresolved deeper carry cannot alter the L-trit result.
        z_other = direct_backward(z_tail + 987654321, A, B)
        assert z_other % mod == z_direct % mod

        # Changing only gates at indices >=L cannot alter the L-trit result.
        B2 = list(B)
        for i in range(L, k):
            B2[i] += 3
        assert direct_backward(z_tail, A, B2) % mod == z_direct % mod

# Current right-H numerical gate counts.
Q_R = 397_573_380
assert Q_R > 47
assert Q_R - 28 == 397_573_352

print("PASS A0 s=1 terminal carry extinction certificate")
print("checkpoint_precision", 28)
print("checkpoint_relevant_rightmost_one_events", 28)
print("right_H_total_one_events", Q_R)
print("right_H_deeper_one_events_invisible_to_28_trits", Q_R - 28)
print("terminal_precisions_closed", (24, 28, 47))
print("status", "EXACT residue locality; 28-gate formation quotient remains OPEN")
