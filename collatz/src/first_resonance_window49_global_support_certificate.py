#!/usr/bin/env python3
"""Exact arithmetic certificate for the global support consequence of the
first-resonance 49-odd-state local exclusion.

Computational input (separate exact C++ certificate): every 49-consecutive
odd-state window of a hypothetical first-resonance counterexample contains at
least seven positive displacement states.

This file certifies only the finite-to-global double-counting consequence.
It does not prove the Collatz conjecture.
"""

Q = 72_057_431_991
L = 49
M = 7

# There are Q-L+1 ordinary (non-cyclic) length-L windows.  Each positive
# displacement ordinal belongs to at most L of them.  Therefore
#     L r_* >= M (Q-L+1).
num = M * (Q - L + 1)
r_lower = (num + L - 1) // L

assert r_lower == 10_293_918_849
assert L * r_lower >= num
assert L * (r_lower - 1) < num

# Every positive displacement pays normalized Christoffel defect > 1/12.
# Hence E/3^Q > r_*/12.
assert r_lower / 12 > 857_826_570

print("PASS window-49 global support certificate")
print("Q", Q)
print("window_length", L)
print("minimum_positive_per_window", M)
print("global_positive_support_lower", r_lower)
print("support_fraction_lower", r_lower / Q)
print("coarse_defect_lower", r_lower / 12)
