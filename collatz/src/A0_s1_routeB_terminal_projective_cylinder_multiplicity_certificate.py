#!/usr/bin/env python3
"""Exact formation-width bound for terminal projective exponent cylinders.

Upstream projective carry theory gives the exponent period at remaining ternary
precision m>=1:

    lambda_m = ord_(3^m)(2) = 2*3^(m-1).

For a fixed ranked candidate one-position b_r under target dominance,

    r-1 <= b_r <= a_r,

where a_r is the target r-th one-position.

On the current full A0 s=1 target the total word length is t0 and the total
one-count is j0.  Purely from strict ordering of the j0 target one-positions,

    a_r <= t0-1-(j0-r).

Therefore every rank has the uniform formation-capacity bound

    a_r-(r-1) <= t0-j0 = D_MAX.

An arithmetic progression beta + lambda_m Z can meet any interval of width at
most D_MAX in at most

    floor(D_MAX/lambda_m)+1

points.  Hence this is an exact universal upper bound on the multiplicity of a
projective exponent cylinder inside the dominance interval.

For the current constants

    D_MAX = 38,530,419,209,
    lambda_23 = 62,762,119,218 > D_MAX,
    lambda_22 = 20,920,706,406 < D_MAX.

Thus m=23 is the sharp precision threshold from this uniform width bound:
all projective exponent cylinders are singleton-or-empty for every m>=23.

Consequences:

* L=28 terminal observation: precisions 28..23, i.e. the first six backward
  one-gates, have no internal exponent multiplicity;
* L=24: precisions 24..23, the first two gates, are singleton-or-empty;
* L=47: precisions 47..23, the first twenty-five gates, are singleton-or-empty.

This does NOT say that the complete carry/suffix branch is unique.  Different
carry/predecessor states can still select different exponent residue cylinders.
It only removes multiplicity *inside one already-specified projective cylinder*.
"""

T0 = 104_398_605_910
J0 = 65_868_186_701
D_MAX = T0 - J0

assert D_MAX == 38_530_419_209


def period(m: int) -> int:
    assert m >= 1
    return 2 * (3 ** (m - 1))


def multiplicity_bound(m: int) -> int:
    return D_MAX // period(m) + 1


# ---------------------------------------------------------------------------
# 1. Sharp singleton threshold from the global formation width.
# ---------------------------------------------------------------------------

assert period(23) == 62_762_119_218
assert period(22) == 20_920_706_406
assert period(23) > D_MAX
assert period(22) < D_MAX

singleton_threshold = min(m for m in range(1, 60) if period(m) > D_MAX)
assert singleton_threshold == 23

for m in range(23, 60):
    assert multiplicity_bound(m) == 1
assert multiplicity_bound(22) == 2


# ---------------------------------------------------------------------------
# 2. Exact local interval-count formula regression.
# ---------------------------------------------------------------------------

interval_checks = 0
for lam in range(1, 40):
    for width in range(0, 80):
        for beta in range(lam):
            # Shifted intervals are enough to test the exact arithmetic count.
            for lo in (0, 3, 11):
                hi = lo + width
                pts = [b for b in range(lo, hi + 1) if (b - beta) % lam == 0]
                assert len(pts) <= width // lam + 1
                interval_checks += 1


# ---------------------------------------------------------------------------
# 3. Current terminal-resolution gate counts.
# ---------------------------------------------------------------------------

expected_singleton_gates = {
    24: 2,
    28: 6,
    47: 25,
}

for Lobs, expected in expected_singleton_gates.items():
    count = sum(1 for m in range(1, Lobs + 1) if m >= singleton_threshold)
    assert count == expected


# Useful local multiplicity table for the first lower-precision gates.
expected_table = {
    28: 1,
    27: 1,
    26: 1,
    25: 1,
    24: 1,
    23: 1,
    22: 2,
    21: 6,
    20: 17,
    19: 50,
    18: 150,
    17: 448,
    16: 1343,
    15: 4028,
}

for m, expected in expected_table.items():
    assert multiplicity_bound(m) == expected


print("PASS A0 s=1 Route-B terminal projective cylinder multiplicity certificate")
print("t0", T0)
print("j0", J0)
print("uniform_formation_width", D_MAX)
print("singleton_threshold_precision", singleton_threshold)
print("lambda_23", period(23))
print("lambda_22", period(22))
print("interval_checks", interval_checks)
for Lobs, count in expected_singleton_gates.items():
    print("terminal_precision", Lobs, "singleton_or_empty_initial_one_gates", count)
for m in sorted(expected_table, reverse=True):
    print("precision", m, "period", period(m), "max_points_per_projective_cylinder", multiplicity_bound(m))
print(
    "formation_bound",
    "every ranked dominance interval has width <= t0-j0, by reserving one distinct position for each later target one",
)
print(
    "projective_bound",
    "a residue class beta mod lambda_m meets such an interval at most floor((t0-j0)/lambda_m)+1 times",
)
print(
    "dsd_audit",
    "singleton cylinder does not imply singleton carry path; carry-state branching and within-cylinder exponent multiplicity remain distinct layers",
)
print(
    "status",
    "uniform projective-cylinder multiplicity bound CLOSED; compressed backward H-suffix branch count remains OPEN",
)
