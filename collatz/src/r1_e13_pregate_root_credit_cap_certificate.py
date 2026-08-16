#!/usr/bin/env python3
"""Exact original-root predecessor-credit cap for the E=13 pre-G13 segment.

Suppose the actual current-R1 pre-G13 path has E=13 and a bounded G13 suffix
relation supplies terminal entrance displacement 1<=delta<=397.  Let an
alternate E=13 pre-G13 word produce an ordinary positive smaller root N'.

In U=x+1 coordinates,

    N - N' = mu*delta - epsilon + epsilon',
    mu = 2^1539 / 3^1526.

The actual correction epsilon is positive.  For the alternate path we do not
assume N'==3 mod 4, so there is no forced initial `11` prefix.  Nevertheless
N'<N<=NMAX and the exact run-cap/future-cover optimizer gives the necessary
even-position lower bounds

    p'_j >= [0,1,2,3,4,5,6,7,66,164,317,558,938].

Hence

    epsilon' < 256.

Also mu*397<1.  Therefore every positive integer predecessor credit satisfies

    0 < N-N' < 257,

and since it is integral,

    1 <= N-N' <= 256.

Thus the entire 1539-step E=13 pullback of every bounded G13 credit 1..397 can
only create an ordinary smaller predecessor within 256 of the actual original
start.  This is a necessary bound, not an existence theorem and not a proof of
Collatz.
"""

from fractions import Fraction
from functools import lru_cache

T = 1539
E = 13
MAX_GATE_CREDIT = 397
NMAX = 5_908_625_413_101_667_397_287
U0 = Fraction(NMAX + 1, 1)


def floor_log2(q: Fraction) -> int:
    n, d = q.numerator, q.denominator
    k = n.bit_length() - d.bit_length()
    while Fraction(1 << k, 1) > q:
        k -= 1
    while Fraction(1 << (k + 1), 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    assert 0 <= r <= floor_log2(U)
    return (Fraction(3, 2) ** r * U + 1) / 2


@lru_cache(None)
def greedy_max_final(steps: int, evens: int):
    U = U0
    rem_steps = steps
    rem_e = evens

    for _ in range(evens):
        if rem_steps < rem_e:
            return None
        r = min(floor_log2(U), rem_steps - rem_e)
        U = odd_run_then_even(U, r)
        rem_steps -= r + 1
        rem_e -= 1

    if rem_steps < 0 or rem_steps > floor_log2(U):
        return None
    return Fraction(3, 2) ** rem_steps * U


def can_cover(U: Fraction, evens: int, needed: int) -> bool:
    total = 0
    for _ in range(evens):
        r = floor_log2(U)
        if total + r + 1 >= needed:
            return True
        total += r + 1
        U = odd_run_then_even(U, r)
    return total + floor_log2(U) >= needed


def earliest_possible_position(j: int) -> int:
    rem_e = E - j - 1
    # No forced initial 11 prefix for the alternate ordinary root.
    for p in range(j, T):
        Umax = greedy_max_final(p + 1, j + 1)
        if Umax is None:
            continue
        if can_cover(Umax, rem_e, T - p - 1):
            return p
    raise AssertionError("no event position")


def epsilon_bound(pos: list[int]) -> Fraction:
    return sum(
        Fraction(3) ** j * Fraction(2, 3) ** p
        for j, p in enumerate(pos)
    )


def main() -> None:
    lower = [earliest_possible_position(j) for j in range(E)]
    assert lower == [0, 1, 2, 3, 4, 5, 6, 7, 66, 164, 317, 558, 938]

    eps_alt = epsilon_bound(lower)
    assert eps_alt < 256

    mu = Fraction(1 << 1539, 3**1526)
    assert mu * MAX_GATE_CREDIT < 1

    # Delta_root = mu*delta - epsilon_actual + epsilon_alt.
    # epsilon_actual>0, epsilon_alt<256, mu*delta<1.
    # Hence a positive integral Delta_root is at most 256.
    assert mu * MAX_GATE_CREDIT + eps_alt < 257

    print("R1 E=13 pre-gate root-credit cap: PASS")
    print("alternate even-position lower bounds:", lower)
    print("alternate formation correction epsilon' < 256")
    print("mu*397 < 1")
    print("every positive ordinary predecessor credit satisfies 1 <= Delta <= 256")


if __name__ == "__main__":
    main()
