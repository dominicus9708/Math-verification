#!/usr/bin/env python3
"""Exact finite diagnostic for the Rhin logarithmic dangerous-core bound.

At a first coefficient crossing put

    sigma = ceil(q log_2 3),
    D = 2^sigma - 3^q > 0.

A dangerous odd-position coordinate i satisfies

    3^(q-i) >= D.

Rozier--Terracol quote Rhin's effective linear-form estimate

    |sigma log 2 - q log 3| >= sigma^(-13.3).

Since D = 3^q (exp(Lambda)-1) > 3^q Lambda for Lambda>0,
any dangerous i obeys

    3^(-i) > sigma^(-13.3).

Writing 13.3=133/10 and raising to the tenth power gives the exact
integer consequence

    3^(10 i) < sigma^133.

Thus the dangerous dimension is O(log sigma)=O(log q).  The transcendental
input is Rhin's theorem; this script only verifies the exact Collatz gap and
the integer consequence over a large finite range.

This is not a proof of the Collatz conjecture.
"""

LIMIT = 200_000
EXPECTED_RECORDS = [
    (1, 2, 1),
    (5, 8, 2),
    (29, 46, 3),
    (41, 65, 4),
    (253, 401, 5),
    (306, 485, 6),
    (8951, 14187, 7),
    (13606, 21565, 8),
    (15601, 24727, 9),
    (47468, 75235, 10),
    (79335, 125743, 11),
    (190537, 301994, 15),
]


def main() -> None:
    p3 = 1
    records = []
    record_h = 0

    for q in range(1, LIMIT + 1):
        p3 *= 3
        # 3^q is never a power of two, so bit_length is exactly
        # ceil(log_2(3^q)).
        sigma = p3.bit_length()
        D = (1 << sigma) - p3
        assert D > 0

        # Count dangerous i=1,2,... exactly.  In all observed cases h is tiny,
        # so only a few big-integer divisions are needed.
        p = p3 // 3  # 3^(q-1)
        h = 0
        while p >= D:
            h += 1
            p //= 3

        if h:
            # Exact rational-exponent-free consequence of Rhin's 13.3 bound.
            assert 3 ** (10 * h) < sigma ** 133

        if h > record_h:
            record_h = h
            records.append((q, sigma, h))

    assert records == EXPECTED_RECORDS
    print("records:")
    for row in records:
        print(*row)
    print("Rhin logarithmic dangerous-core finite diagnostic: PASS")


if __name__ == "__main__":
    main()
