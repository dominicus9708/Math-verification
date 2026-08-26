#!/usr/bin/env python3
Q = 72_057_431_991
L = 49
M = 9
num = M * (Q - L + 1)
r_lower = (num + L - 1) // L
assert r_lower == 13_235_038_521
assert L * r_lower >= num
assert L * (r_lower - 1) < num
assert r_lower / 12 > 1_102_919_876
print("PASS window-49 support-9 global certificate")
print("global_positive_support_lower", r_lower)
print("support_fraction_lower", r_lower / Q)
print("coarse_defect_lower", r_lower / 12)
