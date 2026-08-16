#!/usr/bin/env python3
"""Exact 3-adic terminal-even forcing for pulling a G13 credit through E=13.

For one E=13 pre-G13 parity word with even-event positions

    0 <= p_0 < ... < p_12 < 1539,

write the U=x+1 affine correction as

    C(P) = sum_{j=0}^{12} 2^p_j 3^(1526-p_j+j).

Then

    2^1539 U_T = 3^1526 U_0 + C(P).

For an actual word P and an alternate word P' with the same length and odd
count, a terminal G13 entrance displacement delta pulls back to an ordinary
integer predecessor credit Delta only if

    3^1526 Delta = 2^1539 delta + C(P') - C(P),

hence

    C(P') - C(P) == -2^1539 delta  (mod 3^1526).

Let d=v_3(delta).  Since 2 is a 3-adic unit, the right target has exact
3-adic valuation d.  If both C(P) and C(P') were divisible by 3^(d+1), the
congruence would be impossible.

For one event code, all correction terms are divisible by 3^(d+1) whenever

    1526 - p_j + j >= d+1

for every j.  The quantity p_j-j is nondecreasing, so the weakest exponent is
at j=12.  Therefore a necessary condition for a successful integer pullback is

    max(p_12, p'_12) >= 1538-d.

For the complete bounded G13 integer-credit range 1<=delta<=397 we have d<=5,
so at least one of the two E=13 paths must put its final (13th) even event in
positions 1533..1538, the last six accelerated pre-G13 steps.

More sharply:

    v3(delta)=0 -> final even at 1538 on at least one path
    v3(delta)=1 -> >=1537
    v3(delta)=2 -> >=1536
    v3(delta)=3 -> >=1535
    v3(delta)=4 -> >=1534
    v3(delta)=5 -> >=1533.

No floating-point arithmetic is used.  This is a necessary pullback-channel
theorem; it does not establish that such an alternate word exists and does not
prove Collatz.
"""

from collections import Counter

T = 1539
E = 13
Q = T - E  # 1526
MAX_CREDIT = 397


def v3(n: int) -> int:
    if n <= 0:
        raise ValueError("positive integer required")
    d = 0
    while n % 3 == 0:
        n //= 3
        d += 1
    return d


def min_correction_3_exponent(last_even_position: int) -> int:
    """Smallest explicit 3-exponent among the 13 U-correction terms."""
    return Q - last_even_position + (E - 1)


def required_terminal_even_floor(delta: int) -> int:
    """At least one of the actual/alternate final evens must be >= this."""
    return Q + (E - 1) - v3(delta)


def main() -> None:
    assert Q == 1526

    # Every bounded positive credit has 3-adic valuation at most five because
    # 3^6=729>397.
    vals = [v3(d) for d in range(1, MAX_CREDIT + 1)]
    assert max(vals) == 5
    assert 3**6 > MAX_CREDIT

    counts = Counter(vals)
    assert counts == Counter({0: 265, 1: 88, 2: 30, 3: 10, 4: 3, 5: 1})

    expected_floor = {
        0: 1538,
        1: 1537,
        2: 1536,
        3: 1535,
        4: 1534,
        5: 1533,
    }

    for delta in range(1, MAX_CREDIT + 1):
        d = v3(delta)
        floor = required_terminal_even_floor(delta)
        assert floor == expected_floor[d]

        # If both final evens were below this floor, every correction term on
        # both sides would be divisible by 3^(d+1), contradicting the target
        # congruence whose valuation is exactly d.
        p = floor - 1
        assert min_correction_3_exponent(p) >= d + 1

    print("R1 E=13 pre-gate terminal-even forcing: PASS")
    print("credit valuation counts for 1..397:", dict(sorted(counts.items())))
    print("v3(delta)=0 -> one final even must be at 1538")
    print("v3(delta)=1 -> one final even must be >=1537")
    print("v3(delta)=2 -> one final even must be >=1536")
    print("v3(delta)=3 -> one final even must be >=1535")
    print("v3(delta)=4 -> one final even must be >=1534")
    print("v3(delta)=5 -> one final even must be >=1533")
    print("all credits 1..397 force one path's 13th even into the last six steps")


if __name__ == "__main__":
    main()
