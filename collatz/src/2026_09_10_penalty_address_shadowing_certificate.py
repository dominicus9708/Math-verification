#!/usr/bin/env python3
"""
MATH-054 exact certificate for the mechanical-reference / slack / address bridge.

Finite exact algebra only. Collatz remains OPEN.

Definitions for odd-event index n:
    M_n = floor(n log_2 3)
    m(n) = M_n - n = floor(n log_2(3/2))
    p_n = actual odd position
    u_n = M_n - p_n >= 0 for coefficient-surviving prefixes.

For a word with q odd events,
    S = sum 2^p_n / 3^(n+1)
    S_* = sum 2^M_n / 3^(n+1)
    P = S_* - S
      = sum 2^p_n (2^u_n - 1) / 3^(n+1).

The canonical dyadic start address is N == -S (mod 2^K), so
    N - N_* == P (mod 2^K),
where odd denominators are interpreted by modular inverses.

The first differing odd event has exact 2-adic address-displacement valuation
    v_2(N-N_*) = p_n0.

For the current first-cell 72-bit start window, the mechanical address label is
2037, while allowed labels are 1024..1363. Even if all low 61 bits are matched,
the largest possible common 2-adic valuation is 69. Parity ordering sharpens
the latest possible first deviation to position 67.
"""
from fractions import Fraction
from itertools import combinations
import random

K_ADDR = 72
LOW_BITS = 61
ALLOWED_LABELS = range(1024, 1364)


def M(n: int) -> int:
    # exact floor(n log_2 3)
    return (3 ** n).bit_length() - 1


def m(n: int) -> int:
    return M(n) - n


def v2(x: int) -> int:
    if x == 0:
        raise ValueError("v2(0)")
    x = abs(x)
    return (x & -x).bit_length() - 1


def mechanical_positions_below(K: int) -> list[int]:
    out = []
    n = 0
    while True:
        p = M(n)
        if p >= K:
            return out
        out.append(p)
        n += 1


def address_from_odd_positions(K: int, pos: tuple[int, ...] | list[int]) -> int:
    mod = 1 << K
    total = 0
    for n, p in enumerate(pos):
        total = (total + (1 << p) * pow(pow(3, n + 1, mod), -1, mod)) % mod
    return (-total) % mod


def real_S(pos: tuple[int, ...] | list[int]) -> Fraction:
    return sum((Fraction(1 << p, 3 ** (n + 1)) for n, p in enumerate(pos)), Fraction())


def penalty(pos: tuple[int, ...] | list[int]) -> Fraction:
    q = len(pos)
    mech = [M(n) for n in range(q)]
    return real_S(mech) - real_S(pos)


def penalty_mod(K: int, P: Fraction) -> int:
    mod = 1 << K
    return (P.numerator * pow(P.denominator, -1, mod)) % mod


def first_deviation_valuation(pos: tuple[int, ...] | list[int]) -> int | None:
    for n, p in enumerate(pos):
        if p != M(n):
            assert p < M(n)
            return p
    return None


def coefficient_surviving(pos: tuple[int, ...] | list[int]) -> bool:
    # Equivalent odd-position deadline p_n <= M_n.
    return all(p <= M(n) for n, p in enumerate(pos))


def selftest() -> None:
    rng = random.Random(20260910)

    # Exact identity m(n)=floor(n log2(3/2)) encoded without floating point.
    for n in range(1, 300):
        mn = m(n)
        assert (1 << (mn + n)) <= 3 ** n < (1 << (mn + n + 1))

    # Random finite coefficient-surviving words: real penalty equals dyadic
    # address displacement modulo 2^K; first deviation gives exact v2.
    for K in range(12, 30):
        mech_all = mechanical_positions_below(K)
        qmax = len(mech_all)
        for _ in range(100):
            q = rng.randrange(2, qmax + 1)
            # Build a strictly increasing p_n <= M_n greedily/randomly.
            pos = []
            prev = -1
            for n in range(q):
                lo = prev + 1
                hi = M(n)
                if lo > hi:
                    break
                p = rng.randint(lo, hi)
                pos.append(p)
                prev = p
            if len(pos) != q or not coefficient_surviving(pos):
                continue
            mech = [M(n) for n in range(q)]
            N = address_from_odd_positions(K, pos)
            Ns = address_from_odd_positions(K, mech)
            P = penalty(pos)
            assert (N - Ns) % (1 << K) == penalty_mod(K, P)
            fd = first_deviation_valuation(pos)
            if fd is not None and fd < K:
                diff = (N - Ns) % (1 << K)
                assert diff != 0
                assert v2(diff) == fd

    # Current first-cell mechanical 72-bit address.
    mech72 = mechanical_positions_below(K_ADDR)
    Nstar72 = address_from_odd_positions(K_ADDR, mech72)
    label_star = Nstar72 >> LOW_BITS
    assert label_star == 2037

    # Low 61 bits may be chosen freely. For an allowed top label a, after
    # matching those low bits exactly, v2 of the full address difference is
    # 61 + v2(a-label_star). The maximum is 69.
    best = max((v2(a - label_star), a) for a in ALLOWED_LABELS)
    assert best == (8, 1269)
    max_address_match = LOW_BITS + best[0]
    assert max_address_match == 69

    # If a coefficient-surviving word first deviates at odd event n, strict
    # parity ordering requires M_(n-1) < p_n < M_n. Among such possible first
    # deviations with p_n <= 69, the latest realizable p_n is 67.
    latest = -1
    witness = None
    for n in range(1, 100):
        for p in range(M(n - 1) + 1, M(n)):
            if p <= max_address_match and p > latest:
                latest = p
                witness = (n, p, M(n))
    assert latest == 67
    assert witness == (43, 67, 68)

    print("PASS MATH-054 penalty/address/shadowing certificate")
    print("mechanical_72bit_address", Nstar72)
    print("mechanical_top11_label", label_star)
    print("max_allowed_address_match_v2", max_address_match)
    print("latest_possible_first_deviation_position", latest)


if __name__ == "__main__":
    selftest()
