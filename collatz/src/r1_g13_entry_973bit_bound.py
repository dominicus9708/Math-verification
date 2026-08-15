#!/usr/bin/env python3
"""Exact universal ordinary-state bound at the internal G13 entrance.

The current m=44 R1 core obeys
    N <= 6*3^44 + 1.
The accelerated Collatz map satisfies T(x)+1 <= 3(x+1)/2 for every positive
integer x.  Therefore after 1539 steps,
    x_1539 + 1 <= 3^1539 (N+1) / 2^1539.
This script certifies that the right side is < 2^973, but not < 2^972.

This is a necessary finite-natural bound, not a Collatz proof.
"""

NMAX = 6 * 3**44 + 1
T0 = 1539

numerator = 3**T0 * (NMAX + 1)
denominator = 2**T0

# Exact rational comparisons; no floating point.
assert numerator < (2**973) * denominator
assert numerator >= (2**972) * denominator

print("Nmax", NMAX)
print("G13_entry_time", T0)
print("certified_x1539_lt_2^973", True)
print("2^972_not_certified_by_this_universal_bound", True)
print("G13_length", 20026)
print("forced_zero_high_address_bits_at_least", 20026 - 973)
