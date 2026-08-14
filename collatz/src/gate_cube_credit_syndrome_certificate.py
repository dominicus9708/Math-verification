#!/usr/bin/env python3
"""Exact systematic-Hensel syndrome verifier for first-return gate cubes.

For every integer credit 1 <= delta <= 397, the low J Hensel digits determine
one unique balanced cube-difference vector.  The verifier checks whether that
vector also matches the remaining F=q-J high Hensel digits of the full target.

Expected result: no nonzero full lift in the four explicit G81/G82 neutral and
one-slack cubes.  It also records how many high syndrome trits match before the
first failure.
"""

from collections import Counter

CASES = (
    ("G81-neutral", 404, 567,
     {0: 254, 1: 97, 2: 32, 3: 9, 4: 3, 5: 2}),
    ("G81-one-slack", 402, 568,
     {0: 266, 1: 89, 2: 30, 3: 8, 4: 4}),
    ("G82-neutral", 409, 574,
     {0: 259, 1: 90, 2: 35, 3: 8, 4: 3, 6: 2}),
    ("G82-one-slack", 407, 575,
     {0: 263, 1: 95, 2: 25, 3: 10, 5: 3, 6: 1}),
)


def v3(x: int) -> int:
    if x == 0:
        return 10**9
    n = 0
    while x % 3 == 0:
        x //= 3
        n += 1
    return n


def audit(name: str, F: int, J: int, expected: dict[int, int]) -> None:
    q = F + J
    mod_q = 3**q
    mod_J = 3**J

    # After dividing D by 2^F, the full target is
    # -2^(L-F) delta = -2^(2J+1) delta mod 3^q.
    target_scale = pow(2, 2 * J + 1, mod_q)

    # Exact integer powers 4^j are used in the balanced lifting recurrence.
    p4 = [1]
    for _ in range(1, J):
        p4.append(4 * p4[-1])

    distribution = Counter()
    full_lifts = []
    max_extra = -1
    maximizers = []

    for delta in range(1, 398):
        target = (-target_scale * delta) % mod_q
        r = target % mod_J
        eps = [0] * J

        # Low-Hensel balanced lift.  Work from the latest pair coordinate to
        # the earliest because its 3-adic valuations are 0,1,...,J-1.
        for j in range(J - 1, -1, -1):
            z = r % 3
            e = 0 if z == 0 else (1 if z == 1 else -1)
            eps[j] = e
            numerator = r - e * p4[j]
            assert numerator % 3 == 0
            r = numerator // 3

        # Horner evaluation of Z=sum eps_j 3^(J-1-j) 4^j.
        Z = 0
        for j, e in enumerate(eps):
            Z = 3 * Z + e * p4[j]

        assert (Z - target) % mod_J == 0
        valuation = v3(Z - target)

        if valuation >= q:
            full_lifts.append(delta)
            extra = F
        else:
            extra = valuation - J
            assert extra >= 0

        distribution[extra] += 1
        if extra > max_extra:
            max_extra = extra
            maximizers = [delta]
        elif extra == max_extra:
            maximizers.append(delta)

    assert not full_lifts
    assert dict(sorted(distribution.items())) == expected

    print(name)
    print("  q", q, "J", J, "F", F)
    print("  full_lifts", len(full_lifts))
    print("  extra_high_trit_distribution", dict(sorted(distribution.items())))
    print("  max_extra", max_extra, "maximizers", maximizers)


def main() -> None:
    for case in CASES:
        audit(*case)


if __name__ == "__main__":
    main()
