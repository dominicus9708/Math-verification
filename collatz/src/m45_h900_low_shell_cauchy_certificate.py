#!/usr/bin/env python3
"""Exact H=900 low-shell Cauchy certificate for one m=45 affine block.

Dependencies already certified elsewhere in the repository:

  * the fixed-b 44-selector multiplicity table modulo 2^26 satisfies
        c(r) <= 264167;
  * at every binary parent through that Y-depth,
        160*|c0-c1| < c0+c1.

Those are proved by m45_depth28_local_mass_transport_certificate.cpp.

For one fixed affine block b, there are A=2^44 selectors.  This script combines
those selector bounds with the exact coefficient-survivor valuation-shell energy
identity from survivor_fourier_shell_energy_certificate.py.

At final depth H=900 it proves, using integer arithmetic and ceiling integer
square roots, that

  zero-frequency contribution
  + all Fourier shells with effective depth K<=28

is strictly less than 1/1024 for ONE affine block.  Hence the corresponding
contribution from both b=0,1 blocks is below 1/512.

This does not control K>=29 and therefore does not yet prove extinction of the
m=45 layer or Collatz.
"""

from collections import defaultdict
from math import isqrt

H = 900
A = 1 << 44
CMAX26 = 264_167


def barriers(H: int) -> list[int]:
    b = [0] * (H + 1)
    q = 0
    p3 = 1
    for j in range(1, H + 1):
        while p3 < (1 << j):
            q += 1
            p3 *= 3
        b[j] = q
    return b


def forward_levels(H: int, b: list[int]):
    levels = [{0: 1}]
    cur = {0: 1}
    for j in range(1, H + 1):
        th = b[j]
        nxt = defaultdict(int)
        for q, c in cur.items():
            if q >= th:
                nxt[q] += c
            if q + 1 >= th:
                nxt[q + 1] += c
        cur = dict(nxt)
        levels.append(cur)
    return levels


def tail_counts(H: int, K: int, b: list[int]) -> dict[int, int]:
    f = {q: 1 for q in range(b[H], H + 1)}
    for j in range(H - 1, K - 1, -1):
        th = b[j + 1]
        nf: dict[int, int] = {}
        for q in range(max(0, b[j] - 1), j + 1):
            z = 0
            if q >= th:
                z += f.get(q, 0)
            if q + 1 >= th:
                z += f.get(q + 1, 0)
            if z:
                nf[q] = z
        f = nf
    return f


def survivor_boundary_square_sum(
    H: int, K: int, b: list[int], levels
) -> int:
    """Return sum_q C_(K-1)(q) D_(H,K)(q)^2."""
    F = tail_counts(H, K, b)
    a = b[K]
    s = 0
    for q, c in levels[K - 1].items():
        even = F.get(q, 0) if q >= a else 0
        odd = F.get(q + 1, 0) if q + 1 >= a else 0
        d = even - odd
        s += c * d * d
    return s


def ceil_sqrt(n: int) -> int:
    r = isqrt(n)
    return r if r * r == n else r + 1


def main() -> None:
    b = barriers(H)
    levels = forward_levels(H, b)
    P = sum(levels[H].values())

    # Fourier inversion zero mode for one fixed b block.
    numerator = A * P

    # K=1,2: every fixed-b selector N is congruent to one residue modulo 4,
    # so the selector shell energies are exactly 2^(K-1) A^2.
    for K in (1, 2):
        sb = survivor_boundary_square_sum(H, K, b, levels)
        E_selector = (1 << (K - 1)) * A * A
        E_survivor = (1 << (K - 1)) * sb
        numerator += ceil_sqrt(E_selector * E_survivor)

    # K=3,...,28 correspond to Y effective depths d=K-2 <=26.
    # At depth d, a child mass is a fold of at most 2^(26-d) depth-26 cells.
    # Therefore each sibling-pair mass is at most
    #     2^(27-d) * CMAX26.
    # The certified strict imbalance 160*diff<pair_mass implies
    #     diff <= floor((pair_mass-1)/160).
    for K in range(3, 29):
        d = K - 2
        parent_count = 1 << (d - 1)
        max_child_mass = (1 << (26 - d)) * CMAX26
        max_pair_mass = 2 * max_child_mass
        max_diff = (max_pair_mass - 1) // 160

        selector_diff_square_sum_bound = parent_count * max_diff * max_diff
        E_selector_bound = (1 << (K - 1)) * selector_diff_square_sum_bound

        sb = survivor_boundary_square_sum(H, K, b, levels)
        E_survivor = (1 << (K - 1)) * sb

        numerator += ceil_sqrt(E_selector_bound * E_survivor)

    denominator = 1 << H

    assert numerator * 1024 < denominator

    print("m45 H900 low-shell Cauchy certificate: PASS")
    print("one-block zero+K<=28 numerator", numerator)
    print("denominator 2^900")
    print("one-block contribution < 1/1024")
    print("two-block contribution < 1/512")
    print("remaining uncontrolled shells: K=29,...,900")


if __name__ == "__main__":
    main()
