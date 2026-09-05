#!/usr/bin/env python3
"""Exact arithmetic regression for the DSD parallel gate reorganization.

This certificate does NOT prove the first-crossing theorem or Collatz.
It checks only arithmetic consequences of the already-recorded bound

    x < sigma^(14.3) = sigma^(143/10)

for recursively sufficient starts x >= 4*3^m+3, together with the
published 2^71 external verification cutoff and the existing finite
coherent-ballot horizon 301,993.
"""

from math import log2

P_NUM = 143
P_DEN = 10
FINITE_GATE = 301_993


def n_min(m: int) -> int:
    return 4 * 3**m + 3


def n_max(m: int) -> int:
    return 6 * 3**m + 1


def rhin_gate(m: int) -> int:
    """Largest integer H with H^(143/10) <= N_min(m), exactly.

    Equivalently H^143 <= N_min(m)^10.
    """
    rhs = n_min(m) ** P_DEN
    lo, hi = 0, 1
    while hi**P_NUM <= rhs:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**P_NUM <= rhs:
            lo = mid
        else:
            hi = mid
    return lo


def main() -> None:
    # External finite-base split at 2^71.
    cutoff = 2**71
    assert n_max(43) < cutoff
    assert n_min(44) > cutoff

    # Current difficult layers are governed by the much stronger finite gate.
    assert rhin_gate(44) == 32
    assert rhin_gate(45) == 34
    assert rhin_gate(44) < FINITE_GATE
    assert rhin_gate(45) < FINITE_GATE

    # Exact crossover of the global Rhin gate with the 301,993 finite gate.
    assert rhin_gate(162) < FINITE_GATE
    assert rhin_gate(163) >= FINITE_GATE

    # Monotonicity over a broad regression range.
    prev = rhin_gate(1)
    for m in range(2, 501):
        cur = rhin_gate(m)
        assert cur >= prev
        prev = cur

    kappa_143 = log2(3) / 14.3
    kappa_8616 = log2(3) / 8.616

    print("Nmax(43) =", n_max(43))
    print("2^71      =", cutoff)
    print("Nmin(44) =", n_min(44))
    print("H_Rhin(44) =", rhin_gate(44))
    print("H_Rhin(45) =", rhin_gate(45))
    print("H_Rhin(162) =", rhin_gate(162))
    print("H_Rhin(163) =", rhin_gate(163))
    print("kappa_14.3 =", format(kappa_143, ".15f"))
    print("kappa_8.616 =", format(kappa_8616, ".15f"))
    print("all exact gate assertions passed")


if __name__ == "__main__":
    main()
