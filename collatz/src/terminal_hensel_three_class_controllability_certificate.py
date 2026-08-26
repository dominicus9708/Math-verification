#!/usr/bin/env python3
"""Exact local controllability audit for zero-target terminal Hensel lifts.

This certificate proves that after the required displacement parity is fixed,
the three same-parity residue classes d,d+2,d+4 modulo 6 produce all three
possible next ternary carry digits.  Therefore a sign-only discrepancy theorem
cannot be valid without also using ordering/cost/boundary information.

This is a structural audit, not a proof of the Collatz conjecture.
"""


def invpow2(d: int, mod: int) -> int:
    return pow(pow(2, d, mod), -1, mod)


def next_digit(K9: int, e: int, d: int) -> int:
    """Return K' mod 3 for K'=(K+2^(e-d))/3 in Z_3.

    K9 is K modulo 9 and must be a unit modulo 3.  The action d must satisfy
    divisibility modulo 3.  Computation modulo 9 is enough for the next digit.
    """
    u = (pow(2, e, 9) * invpow2(d, 9)) % 9
    z = (K9 + u) % 9
    assert z % 3 == 0
    return (z // 3) % 3


def required_parity(K9: int, e: int) -> int:
    good = []
    for d in (0, 1):
        u3 = (pow(2, e, 3) * invpow2(d, 3)) % 3
        if (K9 + u3) % 3 == 0:
            good.append(d)
    assert len(good) == 1
    return good[0]


def main() -> None:
    for e in (0, 1):
        for K9 in range(9):
            if K9 % 3 == 0:
                continue
            p = required_parity(K9, e)

            # Any three consecutive same-parity classes modulo 6 exhaust the
            # three units having the required residue modulo 3.  Hence their
            # quotients exhaust the next carry digits 0,1,2.
            vals = [next_digit(K9, e, p + 2*r) for r in range(3)]
            assert sorted(vals) == [0, 1, 2]

            # Rotating the starting representative by any even amount preserves
            # the same statement.
            for shift in range(0, 18, 2):
                d0 = p + shift
                vals2 = [next_digit(K9, e, d0 + 2*r) for r in range(3)]
                assert sorted(vals2) == [0, 1, 2]

    # Ordering lower bound audit: if L is the smallest allowed displacement
    # and p the required parity, let d0 be the first d>=L with d==p mod2.
    # Among d0,d0+2,d0+4 exactly one dies (next digit 0), and the other two
    # realize next carry 1 and 2.  Thus survival is always locally possible by
    # d<=d0+2, and either desired nonzero next carry by d<=d0+4.
    for L in range(20):
        for p in (0, 1):
            d0 = L if L % 2 == p else L + 1
            assert d0 >= L and d0 % 2 == p

    print("PASS terminal Hensel three-class controllability")
    print("same-parity actions d,d+2,d+4 exhaust next carry digits {0,1,2}")
    print("sign-only correlation is not a standalone obstruction")
    print("ordering + displacement cost + two-boundary state must be retained")


if __name__ == "__main__":
    main()
