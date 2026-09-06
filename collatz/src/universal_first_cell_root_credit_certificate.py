#!/usr/bin/env python3

B0 = 1 << 71
Q0 = 72_057_431_991


def min_q_survival(k: int) -> int:
    """Least q with 3^q >= 2^k, using exact integers."""
    q = 0
    p3 = 1
    p2 = 1 << k
    while p3 < p2:
        p3 *= 3
        q += 1
    return q


def credit_lt_floor(k: int, q: int, floor: int = B0) -> bool:
    """
    Check exactly
        2^(k-q) * (1-(2/3)^q) < floor.
    This is the fixed-(k,q) upper envelope for normalized root Hensel credit.
    """
    num = (1 << (k - q)) * (3**q - 2**q)
    den = 3**q
    return num < floor * den


def main():
    last_safe = 0
    first_fail = None
    for k in range(1, 300):
        q = min_q_survival(k)
        if credit_lt_floor(k, q):
            last_safe = k
        else:
            first_fail = (k, q)
            break

    assert last_safe == 195
    assert first_fail == (196, 124)

    # Regression around the transition.
    expected = {
        192: (122, True),
        193: (122, True),
        194: (123, True),
        195: (124, True),
        196: (124, False),
        197: (125, False),
    }
    for k, (q_expected, ok_expected) in expected.items():
        q = min_q_survival(k)
        assert q == q_expected
        assert credit_lt_floor(k, q) == ok_expected

    # For the first universal first-crossing cell, the elementary mechanical
    # pair bound S*(q) <= (7q+1)/24 is tiny compared with B0.  Hence among
    # first-crossing-admissible words in one full-Hensel class, any larger
    # correction gives a positive root credit Delta < B0 < N.
    assert 7 * Q0 + 1 < 24 * B0

    print("PASS")
    print("root-safe coefficient-surviving depth =", last_safe)
    print("first envelope failure =", first_fail)
    print("first-cell admissible-class credit bound < B0")


if __name__ == "__main__":
    main()
