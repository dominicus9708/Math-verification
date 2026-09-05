#!/usr/bin/env python3
"""Exact inverse of the certified normalized-defect -> physical-X pruning map.

The upstream real-envelope oracle is monotone:

    eta_floor  ->  X <= x_upper_from_eta(eta_floor).

For an exact source interval whose smallest ordinary source is X_lo, a family is
closed whenever its certified defect floor eta satisfies

    x_upper_from_eta(eta) < X_lo.

This certificate inverts the fixed-point implementation exactly.  It computes
the smallest fixed-point defect coordinate E/QFP that closes a whole source
interval with lower endpoint X_lo.

The result is intended to be paired with projective-cylinder defect floors.
It does not assert that the required defect floor is actually attained by the
current grammar state.
"""

from fractions import Fraction

import A0_s1_prefix_defect_membership_pruning_certificate as pruning
import A0_s1_14root_long_membership_forest_certificate as forest

QFP = pruning.QFP
mW_lo = pruning.mW_lo
cW_hi = pruning.cW_hi
delta_lo = pruning.delta_lo
L_MAX = pruning.L_MAX


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def closure_eta_grid_numerator(X_lo: int) -> int:
    """Smallest E>=0 for which eta=E/QFP gives x_upper(eta)<X_lo."""
    assert X_lo >= 0

    # x_upper(E/QFP) < X_lo iff
    #
    #   L_MAX*QFP + cW_hi - floor(mW_lo*E/QFP)
    #       < X_lo*delta_lo.
    #
    # Therefore floor(mW_lo*E/QFP) must be at least R+1.
    R = L_MAX * QFP + cW_hi - X_lo * delta_lo
    if R < 0:
        return 0
    return ceil_div((R + 1) * QFP, mW_lo)


def closure_eta(X_lo: int) -> Fraction:
    return Fraction(closure_eta_grid_numerator(X_lo), QFP)


# ---------------------------------------------------------------------------
# 1. Exact inverse/minimality checks on every current 14-root interval.
# ---------------------------------------------------------------------------

rows = []
for root in forest.roots:
    X_lo = root["r"] + (1 << root["h"]) * root["m_lo"]
    X_hi = root["r"] + (1 << root["h"]) * root["m_hi"]
    assert X_lo <= X_hi == root["xmax"] or X_hi <= root["xmax"]

    E = closure_eta_grid_numerator(X_lo)
    eta = Fraction(E, QFP)

    assert pruning.x_upper_from_eta(eta) < X_lo
    if E > 0:
        eta_prev = Fraction(E - 1, QFP)
        assert pruning.x_upper_from_eta(eta_prev) >= X_lo

    # The already known first-75 floor is far below the whole-root closure
    # threshold; this is a diagnostic fact about root-scale pruning, not a
    # statement about descendants after source refinement.
    eta75 = root["eta75_floor"]
    rows.append((root["f"], X_lo, X_hi, eta75, eta, E))


# ---------------------------------------------------------------------------
# 2. Monotonicity: later/higher source intervals need no larger defect floor.
# ---------------------------------------------------------------------------

sorted_x = sorted((X_lo, closure_eta_grid_numerator(X_lo)) for _f, X_lo, _X_hi, _eta75, _eta, _E in rows)
for (x1, e1), (x2, e2) in zip(sorted_x, sorted_x[1:]):
    assert x1 <= x2
    assert e1 >= e2


# ---------------------------------------------------------------------------
# 3. Generic interval regression around the current physical shell.
# ---------------------------------------------------------------------------

probe_points = [
    (1 << 71) + 1,
    (1 << 71) + (1 << 60),
    (1 << 71) + (1 << 68),
    pruning.GLOBAL_X_MAX if hasattr(pruning, "GLOBAL_X_MAX") else pruning.new_x_max,
]

inverse_checks = 0
for X_lo in probe_points:
    E = closure_eta_grid_numerator(X_lo)
    eta = Fraction(E, QFP)
    assert pruning.x_upper_from_eta(eta) < X_lo
    if E:
        assert pruning.x_upper_from_eta(Fraction(E - 1, QFP)) >= X_lo
    inverse_checks += 1


print("PASS A0 s=1 Route-B inverse defect-budget pruning certificate")
print("root_count", len(rows))
for f, X_lo, X_hi, eta75, eta_close, E in rows:
    print(
        "root",
        f,
        "X_lo",
        X_lo,
        "X_hi",
        X_hi,
        "eta75_floor",
        eta75,
        "eta_close_grid",
        eta_close,
        "eta_close_decimal_approx",
        float(eta_close),
        "E",
        E,
    )
print("inverse_checks", inverse_checks)
print(
    "inverse_theorem",
    "eta_close(X_lo) is the exact smallest QFP-grid defect floor that makes x_upper_from_eta < X_lo",
)
print(
    "monotonicity",
    "raising the source-interval lower endpoint can only lower the defect budget required for whole-family rejection",
)
print(
    "dsd_audit",
    "this is a decision-threshold inversion only; it does not promote local adic observations to a defect floor unless separately certified",
)
print(
    "status",
    "adaptive defect-budget threshold CLOSED; long-grammar accumulation sufficient to cross it remains OPEN",
)
