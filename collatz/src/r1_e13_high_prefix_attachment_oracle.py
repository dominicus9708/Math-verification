#!/usr/bin/env python3
"""Exact attachment oracle for one proposed E=13 G13 high prefix h.

The current proof architecture reduces an ordinary G13 entrance X to its
73-bit high prefix

    h = floor((X+1)/2^879).

For E=13, the channel-conditioned formation theorem gives a generic correction
bound epsilon_13 < 114.  Since

    X+1 = h*2^879 + ell,  0<=ell<2^879,
    lambda = 2^2418 / 3^1526 < 1,

any original start N compatible with the proposed h must satisfy

    lambda*h - 115 < N < lambda*(h+1) - 1.

That interval has width <115, so at most 115 ordinary integers need to be
checked.  The oracle then verifies each integer exactly against:

- the current m=44 ternary core and numerical window;
- one of the six surviving first-defect channels;
- no first descent during the 1539-step pre-G13 segment;
- exactly 13 forward-even events;
- the actual time-1539 endpoint high prefix.

Thus a G13 search never needs to retain all 879 low entrance bits merely to
ask whether a proposed high prefix can attach to the current R1 core.

The file also records the deterministic support-cardinality cap.  The existing
necessary hard-channel masses sum to 556,222,489,419.  Since one ordinary root
has exactly one actual time-1539 endpoint and hence one actual h, the true
E=13 attachment support contains at most that many high prefixes, less than
1.8e-10 of the full E=13 high-prefix band.

This oracle is an exact query mechanism, not an exhaustive enumeration of all
h and not a Collatz proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction

T = 1539
E = 13

N0 = 3_939_105_844_976_711_153_619
NMAX = 5_908_625_413_101_667_397_287

H_MIN = 6_193_025_058_704_856_278_260
H_MAX = 9_289_485_148_641_721_970_895
H_BAND_COUNT = 3_096_460_089_936_865_692_636

LAM = Fraction(1 << 2418, 3**1526)
GENERIC_EPS_UPPER = 114  # strict upper bound: epsilon_13 < 114

H19 = "1101101101011011010"
MECH73 = (H19 * 4)[:73]
SURVIVING_FIRST_DEFECTS = {2, 5, 8, 10, 13, 16}

HARD_COUNTS = {
    2: 456_566_092_589,
    5: 80_911_487_383,
    8: 14_667_776_602,
    10: 3_349_620_432,
    13: 615_721_246,
    16: 111_791_167,
}
ACTUAL_H_SUPPORT_CAP = sum(HARD_COUNTS.values())


def floor_fraction(q: Fraction) -> int:
    return q.numerator // q.denominator


def ceil_fraction(q: Fraction) -> int:
    return -((-q.numerator) // q.denominator)


def accelerated_step(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def in_current_m44_core(N: int) -> bool:
    if N < N0 or N > NMAX or N % 4 != 3:
        return False
    y = (N - 3) // 4
    for _ in range(44):
        d = y % 3
        if d > 1:
            return False
        y //= 3
    return y == 1


def first_defect(N: int, limit: int = 24) -> int | None:
    x = N
    for t in range(limit):
        actual = 1 if (x & 1) else 0
        mech = 1 if MECH73[t] == "1" else 0
        if actual != mech:
            return t
        x = accelerated_step(x)
    return None


def generic_root_interval_for_h(h: int) -> tuple[int, int]:
    """Safe integer interval containing every E=13 root compatible with h.

    epsilon<114 and 0<=eta<lambda imply

        N+1 = lambda*h + eta - epsilon,

    hence

        lambda*h - 115 < N < lambda*(h+1)-1.
    """
    lower_exclusive = LAM * h - 115
    upper_exclusive = LAM * (h + 1) - 1

    lo = floor_fraction(lower_exclusive) + 1
    hi = ceil_fraction(upper_exclusive) - 1

    if lo < N0:
        lo = N0
    if hi > NMAX:
        hi = NMAX
    return lo, hi


def audit_pregate(N: int) -> tuple[bool, int, int, int | None]:
    """Return (survives, even_count, X, first_descent_step)."""
    x = N
    evens = 0
    first_descent = None

    for t in range(1, T + 1):
        if x & 1:
            x = (3 * x + 1) // 2
        else:
            x //= 2
            evens += 1

        if first_descent is None and x < N:
            first_descent = t

    return first_descent is None, evens, x, first_descent


def compatible_roots_for_h(h: int) -> list[tuple[int, int, int]]:
    """Return exact compatible triples (N, first_defect, X) for one h."""
    if h < H_MIN or h > H_MAX:
        return []

    lo, hi = generic_root_interval_for_h(h)
    if lo > hi:
        return []

    # Width <115, so there are at most 115 ordinary integers before filters.
    assert hi - lo + 1 <= 115

    out = []
    for N in range(lo, hi + 1):
        if not in_current_m44_core(N):
            continue

        p = first_defect(N)
        if p not in SURVIVING_FIRST_DEFECTS:
            continue

        survives, evens, X, _tau = audit_pregate(N)
        if not survives or evens != E:
            continue

        # The existing E=13 entrance theorem forces exactly 952 bits.
        assert X.bit_length() == 952

        actual_h = (X + 1) >> 879
        if actual_h != h:
            continue

        out.append((N, p, X))

    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("h", type=int, nargs="?", help="73-bit G13 entrance high prefix")
    args = parser.parse_args()

    assert LAM < 1
    assert H_MAX - H_MIN + 1 == H_BAND_COUNT
    assert ACTUAL_H_SUPPORT_CAP == 556_222_489_419
    assert Fraction(ACTUAL_H_SUPPORT_CAP, H_BAND_COUNT) < Fraction(18, 100_000_000_000)

    # The broad h-only root interval is always shorter than 115 real units.
    for h in (H_MIN, (H_MIN + H_MAX) // 2, H_MAX):
        lo, hi = generic_root_interval_for_h(h)
        if lo <= hi:
            assert hi - lo + 1 <= 115

    print("R1 E=13 high-prefix attachment oracle: READY")
    print("actual deterministic h-support cap =", ACTUAL_H_SUPPORT_CAP)
    print("actual support fraction < 18/10^11 (<1.8e-10)")
    print("actual support percent < 0.000000018%")

    if args.h is not None:
        lo, hi = generic_root_interval_for_h(args.h)
        roots = compatible_roots_for_h(args.h)
        print(f"h={args.h}")
        print(f"generic_root_interval=[{lo},{hi}]")
        print(f"compatible_roots={len(roots)}")
        for N, p, X in roots:
            print(f"N={N} first_defect={p} X={X}")


if __name__ == "__main__":
    main()
