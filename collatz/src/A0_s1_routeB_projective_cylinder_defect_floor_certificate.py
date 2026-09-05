#!/usr/bin/env python3
"""Exact projective carry-cylinder -> normalized-defect floor bridge.

This certificate closes one proof interface in the A0 s=1 Route-B audit:

    projective ternary carry constraint
        -> exponent/displacement cylinder
        -> exact minimum normalized correction defect.

At remaining ternary precision m >= 1, put

    M = 3^m,
    lambda = ord_M(2) = 2*3^(m-1).

For fixed incoming carry z mod M, target one-position a, and candidate
one-position b, a legal one-step lift has

    z + 2^a - 2^b == 0 (mod 3),

with successor carry

    z' = (z + 2^a - 2^b)/3 (mod 3^(m-1)).

The already-certified one-step carry bijection implies that, unless the gate is
empty, every prescribed successor residue z' selects exactly one exponent
residue

    b == beta (mod lambda).

This file adds the order/dominance and physical-defect consequence.
Suppose a family restricts the ranked candidate one-position to

    lo <= b <= hi,   b <= a.

Then the z'-cylinder is either empty, or is exactly the arithmetic progression

    [lo, min(hi,a)] intersect (beta + lambda Z).

Its largest member b_max gives the smallest displacement a-b and therefore the
exact minimum contribution to the normalized dominance defect

    eta_r(a,b) = (2^a - 2^b)/3^r.

Hence

    eta_r >= (2^a - 2^b_max)/3^r,

with equality attained by b=b_max.  If b_max<a this is a strict positive gap;
if b_max=a the cylinder itself does not force a defect at this rank.

This is a membership-relevant lower-bound primitive, not a rule saying that an
adic target mismatch is automatically rejected.  The lower bound becomes a
physical pruning statement only after it is composed with the existing
normalized-defect/real-envelope machinery.
"""

from fractions import Fraction


def order_3_power(m: int) -> int:
    assert m >= 1
    return 2 * (3 ** (m - 1))


def successor_residue(m: int, z: int, a: int, b: int):
    """Return the projective successor residue, or None if the lift fails."""
    assert m >= 1
    modulus = 3 ** m
    next_modulus = 3 ** (m - 1)
    s = (z + pow(2, a, modulus) - pow(2, b, modulus)) % modulus
    if s % 3:
        return None
    return (s // 3) % next_modulus if next_modulus > 1 else 0


def cylinder_max(lo: int, hi: int, beta: int, period: int):
    """Largest integer in [lo,hi] congruent to beta mod period, or None."""
    assert period >= 1
    if lo > hi:
        return None
    out = hi - ((hi - beta) % period)
    return out if out >= lo else None


def defect_atom(a: int, b: int, rank: int) -> Fraction:
    assert rank >= 1
    assert 0 <= b <= a
    return Fraction((1 << a) - (1 << b), 3 ** rank)


# ---------------------------------------------------------------------------
# 1. Exact successor-cylinder regression.
# ---------------------------------------------------------------------------

cylinder_checks = 0
empty_gate_checks = 0
bijection_checks = 0

for m in range(1, 5):
    modulus = 3 ** m
    next_modulus = 3 ** (m - 1)
    period = order_3_power(m)

    for z in range(modulus):
        for a in range(min(2 * period, 18)):
            by_successor = {}
            for beta in range(period):
                nxt = successor_residue(m, z, a, beta)
                if nxt is not None:
                    by_successor.setdefault(nxt, []).append(beta)

            if (z + pow(2, a, modulus)) % 3 == 0:
                assert by_successor == {}
                empty_gate_checks += 1
                continue

            # Every successor carry class has one and only one exponent class.
            assert set(by_successor) == set(range(next_modulus))
            assert all(len(v) == 1 for v in by_successor.values())
            bijection_checks += next_modulus

            for nxt, residues in by_successor.items():
                beta = residues[0]

                # Ordering/dominance is represented by an ordinary interval.
                for lo in range(a + 1):
                    for hi in range(lo, a + 1):
                        b_max = cylinder_max(lo, hi, beta, period)
                        direct = [
                            b
                            for b in range(lo, hi + 1)
                            if successor_residue(m, z, a, b) == nxt
                        ]

                        if not direct:
                            assert b_max is None
                        else:
                            assert b_max == max(direct)
                            # Congruence class is exact, not merely necessary.
                            assert all((b - beta) % period == 0 for b in direct)
                            assert all(
                                successor_residue(m, z, a, b) == nxt
                                for b in direct
                            )

                            # The largest legal b is the exact minimum-defect
                            # representative for every positive global rank.
                            for rank in (1, 2, 4):
                                vals = [defect_atom(a, b, rank) for b in direct]
                                floor = defect_atom(a, b_max, rank)
                                assert min(vals) == floor
                                assert all(v >= floor for v in vals)

                        cylinder_checks += 1


assert cylinder_checks > 0
assert empty_gate_checks > 0
assert bijection_checks > 0


# ---------------------------------------------------------------------------
# 2. Direct displacement form.
# ---------------------------------------------------------------------------
# If b == beta mod lambda, then delta=a-b lies in one residue class modulo
# lambda as well.  The smallest legal delta is exactly a-b_max.

displacement_checks = 0
for m in range(1, 5):
    period = order_3_power(m)
    for a in range(15):
        for beta in range(period):
            for lo in range(a + 1):
                b_max = cylinder_max(lo, a, beta, period)
                if b_max is None:
                    continue
                deltas = [
                    a - b
                    for b in range(lo, a + 1)
                    if (b - beta) % period == 0
                ]
                assert deltas
                assert min(deltas) == a - b_max
                assert all((d - (a - beta)) % period == 0 for d in deltas)
                displacement_checks += 1

assert displacement_checks > 0

print("PASS A0 s=1 Route-B projective cylinder defect-floor certificate")
print("cylinder_checks", cylinder_checks)
print("empty_gate_checks", empty_gate_checks)
print("bijection_checks", bijection_checks)
print("displacement_checks", displacement_checks)
print(
    "cylinder",
    "fixed successor z' selects one b residue mod 2*3^(m-1); interval/order constraints give an exact arithmetic progression",
)
print(
    "defect_floor",
    "the maximal legal b is the exact minimum-defect representative of that projective cylinder",
)
print(
    "composition",
    "the floor may be accumulated directly by ranked defect atoms or through eta(UV)=eta(U)+mu(U)eta(V)",
)
print(
    "dsd_audit",
    "adic observation is converted to a membership-relevant eta lower bound without identifying target collision with membership rejection",
)
print(
    "status",
    "projective carry -> displacement cylinder -> eta floor CLOSED; shell-wide physical closure remains OPEN",
)
