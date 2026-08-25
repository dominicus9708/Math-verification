#!/usr/bin/env python3
"""Numerical/exact consistency certificate for the 2026-08-26 DSD Stage-4 audit.

This certificate checks that the branch-local Stage-4 thresholds remain
separate from the global coefficient-formation budget, and reproduces the
key finite-address and automatic-height threshold comparisons.

It is an audit certificate, not a proof of the Collatz conjecture.
"""

import math

WINDOW = 28
DYADIC_WINDOW = 2**WINDOW

# --- Finite-address thresholds -------------------------------------------------
NMAX_44 = 6 * 3**44 + 1
NMAX_45 = 6 * 3**45 + 1
assert NMAX_44 < 2**73
assert NMAX_45 < 2**74

# --- Original Stage-4 universal threshold ------------------------------------
# log2(15)/28 < 7/50, checked exactly as 15^25 < 2^98.
assert 15**25 < 2**98

# High-height automatic boundary: z=4 fails the selector-free K=15 test,
# while z=5 passes it.
M_Z4_HIGH = 15_918_777
M_Z5_HIGH = 18_633_853
assert 15 * M_Z4_HIGH < DYADIC_WINDOW
assert 15 * M_Z5_HIGH > DYADIC_WINDOW

# --- Reduced recurrent-state thresholds --------------------------------------
# Five-state core: z=4 is automatic at K=25.
assert 25 * 12_076_300 > DYADIC_WINDOW

# Three-state core: z=2 is automatic at K=56.
assert 56 * 4_867_480 > DYADIC_WINDOW

# Two-state L7 core: neither z=0 nor z=1 is automatic at K=117.
M_Z0_L7 = 405_550
M_Z1_L7 = 1_513_565
assert 117 * M_Z0_L7 < DYADIC_WINDOW
assert 117 * M_Z1_L7 < DYADIC_WINDOW

# Two-state simultaneous L7/L14 core: neither state is automatic at K=150.
M_Z0_L714 = 317_231
M_Z1_L714 = 1_192_543
assert 150 * M_Z0_L714 < DYADIC_WINDOW
assert 150 * M_Z1_L714 < DYADIC_WINDOW

# --- Global coefficient-formation budget -------------------------------------
alpha = math.log(2.0, 3.0)
H2 = -alpha * math.log2(alpha) - (1.0 - alpha) * math.log2(1.0 - alpha)
delta_form = 1.0 - H2
rho = math.log2(3.0) / (1.0 - alpha)
safe_budget = delta_form * rho
global_two_exponent_rhs = math.log2(3.0) * delta_form

# The known linear safe horizon does not repay one selector bit per ternary depth.
assert safe_budget < 1.0

# Crucial audit separation: the Stage-4 K=15 local repair exponent is not the
# global formation exponent beta budget and is numerically much larger.
stage4_k15_rate = math.log2(15.0) / WINDOW
assert stage4_k15_rate < 7.0 / 50.0
assert stage4_k15_rate > delta_form

# Reproduce the strengthened two-state sufficient selector losses.
loss_z0 = 1.0 - 150.0 * M_Z0_L714 / DYADIC_WINDOW
loss_z1 = 1.0 - 150.0 * M_Z1_L714 / DYADIC_WINDOW
assert 0.822 < loss_z0 < 0.823
assert 0.333 < loss_z1 < 0.334

print("DSD Stage-4 budget separation certificate: PASS")
print("Nmax(44) < 2^73:", NMAX_44)
print("Nmax(45) < 2^74:", NMAX_45)
print("Stage-4 K=15 rate:", stage4_k15_rate)
print("global delta_form:", delta_form)
print("safe-horizon slope rho:", rho)
print("formation budget delta_form*rho:", safe_budget)
print("two-exponent RHS log2(3)*delta_form:", global_two_exponent_rhs)
print("strengthened two-state selector loss z=1:", loss_z1)
print("strengthened two-state selector loss z=0:", loss_z0)
