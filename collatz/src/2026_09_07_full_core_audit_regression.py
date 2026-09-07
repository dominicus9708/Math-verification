#!/usr/bin/env python3
"""Lightweight exact regression for the 2026-09-07 Collatz full audit.

This certificate intentionally checks only the small, exact core claims that the
current proof architecture treats as foundational.  It does not claim or test a
complete proof of the Collatz conjecture.
"""

from fractions import Fraction
from math import gcd

B_PUBLISHED = 1 << 71
B_LIVE_SNAPSHOT = 2075 * (1 << 60)  # official project page snapshot, 2026-09-07 audit

PL, QL = 6_586_818_670, 10_439_860_591
PU, QU = 65_470_613_321, 103_768_467_013
FIRST = (114_208_327_604, 72_057_431_991)
SECOND = (217_976_794_617, 137_528_045_312)

BLOCK = 1024
BLOCK_CAP = Fraction(361, 500)
START_CAP_RATIO = Fraction(1365, 1024)


def ln_interval(x: Fraction, n: int = 260):
    assert x >= 1
    if x == 1:
        return Fraction(0), Fraction(0)

    z = (x - 1) / (x + 1)
    z2 = z * z
    term = z
    total = Fraction(0)
    for k in range(n + 1):
        total += term / (2 * k + 1)
        term *= z2

    lo = 2 * total
    tail = 2 * (z ** (2 * n + 3)) / ((2 * n + 3) * (1 - z2))
    return lo, lo + tail


def ratio_interval(num, den):
    nl, nu = num
    dl, du = den
    assert dl > 0
    return nl / du, nu / dl


LN2 = ln_interval(Fraction(2), 200)
LN3 = ln_interval(Fraction(3), 260)
ALPHA = ratio_interval(LN2, LN3)


def beta_interval(floor: int):
    lnc = ln_interval(Fraction(3 * floor + 1, floor), 260)
    return ratio_interval(LN2, lnc)


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    p2 = 1 << k
    while p3 < p2:
        p3 *= 3
        q += 1
    return q


def root_credit_lt_floor(k: int, q: int, floor: int) -> bool:
    # 2^(k-q)*(1-(2/3)^q) < floor, checked without floating point.
    num = (1 << (k - q)) * (3**q - 2**q)
    den = 3**q
    return num < floor * den


def root_safe_depth(floor: int):
    last_safe = 0
    first_fail = None
    for k in range(1, 300):
        q = min_q_survival(k)
        if root_credit_lt_floor(k, q, floor):
            last_safe = k
        else:
            first_fail = (k, q)
            break
    return last_safe, first_fail


def phase_power(j: int) -> Fraction:
    """Exact 2^{fractional_part(j*log2(3/2))}."""
    if j == 0:
        return Fraction(1)
    p3 = 3**j
    floor_log2_p3 = p3.bit_length() - 1
    floor_jtheta = floor_log2_p3 - j
    return Fraction(p3, 1 << (j + floor_jtheta))


def exact_block_max(m: int):
    """Exact max of sum_j 2^{-frac(x+j*theta)} over x in [0,1)."""
    us = [phase_power(j) for j in range(m)]
    bs = [Fraction(1, 1) / u for u in us]
    base = sum(bs, Fraction(0))
    best = base
    witness = ("x=0", -1)

    pairs = sorted(zip(us, bs, range(m)), key=lambda z: z[0], reverse=True)
    wrapped = Fraction(0)
    for u, b, j in pairs:
        wrapped += b
        if u == 1:
            continue
        candidate = u * (base + wrapped) / 2
        if candidate > best:
            best = candidate
            witness = ("wrap", j)
    return best, witness


def main():
    # 1. Published-floor Farey isolation.
    beta_pub = beta_interval(B_PUBLISHED)
    rL = Fraction(PL, QL)
    rU = Fraction(PU, QU)
    assert rL < beta_pub[0]
    assert beta_pub[1] < ALPHA[0]
    assert ALPHA[1] < rU
    assert PU * QL - PL * QU == 1

    A0 = QL + QU
    q0 = PL + PU
    assert (A0, q0) == FIRST
    r0 = Fraction(q0, A0)
    assert beta_pub[1] < r0 < ALPHA[0]

    cells = []
    limit = SECOND[0]
    for a in range(1, limit // QL + 1):
        for b in range(1, limit // QU + 1):
            A = a * QL + b * QU
            if A > limit or gcd(a, b) != 1:
                continue
            q = a * PL + b * PU
            f = Fraction(q, A)
            if beta_pub[1] < f < ALPHA[0]:
                cells.append((A, q, a, b))
    assert cells == [
        (114_208_327_604, 72_057_431_991, 1, 1),
        (217_976_794_617, 137_528_045_312, 1, 2),
    ]

    # 2. Root-Hensel safe-depth transition.
    assert root_safe_depth(B_PUBLISHED) == (195, (196, 124))

    # 3. Exact 1024-block correction bound.
    hmax, witness = exact_block_max(BLOCK)
    assert hmax < BLOCK_CAP * BLOCK

    blocks, remainder = divmod(q0, BLOCK)
    assert remainder == 951
    s_upper = (blocks * (BLOCK_CAP * BLOCK) + remainder) / 3

    delta = (A0 * LN2[0] - q0 * LN3[1], A0 * LN2[1] - q0 * LN3[0])
    ncap = START_CAP_RATIO * B_PUBLISHED
    rhs = ln_interval(Fraction(1) + s_upper / ncap, 180)
    assert delta[0] > rhs[1]

    assert START_CAP_RATIO - 1 == Fraction(341, 1024)
    assert 2 - START_CAP_RATIO == Fraction(683, 1024)
    assert START_CAP_RATIO * B_PUBLISHED == 1365 * (1 << 61)

    # 4. Current live-frontier sensitivity snapshot.  This is not promoted to
    # the frozen paper-facing baseline; it only records that the current
    # official project frontier does not change the first Farey cell or the
    # 195-bit root-safe transition at this audit date.
    assert B_LIVE_SNAPSHOT > B_PUBLISHED
    beta_live = beta_interval(B_LIVE_SNAPSHOT)
    assert beta_live[1] < r0 < ALPHA[0]
    assert root_safe_depth(B_LIVE_SNAPSHOT) == (195, (196, 124))

    print("PASS")
    print("published floor = 2^71")
    print("first universal cell =", FIRST)
    print("cells through second resonance =", [(A, q) for A, q, _, _ in cells])
    print("root-safe depth = 195; first envelope failure = (196,124)")
    print("1024-block maximum < (361/500)*1024; witness =", witness)
    print("first-cell cap = 1365*2^61; remaining 11-bit blocks = 341")
    print("live frontier snapshot = 2075*2^60; first cell and root-safe depth unchanged")
    print("NO COMPLETE COLLATZ PROOF CLAIM")


if __name__ == "__main__":
    main()
