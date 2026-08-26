#!/usr/bin/env python3
"""Exact arithmetic consequence of the support-7 local exclusion.

Input theorem: every 49-consecutive odd-state window contains at least eight
positive displacement states.  This script certifies the resulting global
support and coarse normalized-defect lower bounds.
"""

Q = 72_057_431_991
L = 49
M = 8

num = M * (Q - L + 1)
r_lower = (num + L - 1) // L

assert r_lower == 11_764_478_685
assert L * r_lower >= num
assert L * (r_lower - 1) < num

# Each positive displacement pays normalized defect >1/12.
defect_lower = r_lower / 12
assert defect_lower > 980_373_223

print("PASS window-49 support-8 global certificate")
print("global_positive_support_lower", r_lower)
print("support_fraction_lower", r_lower / Q)
print("coarse_defect_lower", defect_lower)
