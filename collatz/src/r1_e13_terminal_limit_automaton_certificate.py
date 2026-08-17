#!/usr/bin/env python3
"""Cutoff-free terminal 3-adic formation automaton for the E=13 pre-G13 relation.

For the last eight even-event ranks j=5,...,12, write

    e_j = Q - p_j + j,

so p_5<...<p_12 is equivalent to

    e_5 >= e_6 >= ... >= e_12 >= 0.

After dividing the correction by the 3-adic unit 2^Q, the terminal code is

    S(e) = sum_{j=5}^{12} 2^(j-e_j) 3^e_j.

We also allow e_j=infinity, meaning that a rank remains invisible at every
finite 3-adic depth.  This is the exact inverse-limit over-family represented
by the K-adic terminal suffix sieves before the early ranks j=0,...,4 enter.

A right-boundary credit d is terminally liftable iff

    -2^13 d in S_8 - S_8   in Z_3.

The digit-by-digit condition has a cutoff-free finite recursion.  At one
3-adic level let a,b in {0,...,8} be the numbers of still-unassigned terminal
ranks on the actual and alternate sides.  Choosing a'<=a and b'<=b assigns a
suffix of the remaining ranks to the current exponent.  The corresponding
integer block sum is

    A(a',a) = 2^(5+a) - 2^(5+a').

If c is the scaled residual carry, the next state exists exactly when

    c + A(b',b) - A(a',a) == 0 (mod 3),

and then

    c' = (2/3) [c + A(b',b) - A(a',a)].

The no-assignment transition keeps a,b fixed but strictly decreases |c|
unless c=0.  Every other transition decreases a+b.  Hence the recursion is
well-founded and contains no depth cutoff.

For d=1,...,397 it accepts exactly 247 labels, identical to the K=30..36
plateau of r1_e13_bounded_credit_3adic_lift_sieve.cpp.  The other 150 labels
are therefore genuinely absent before any early event rank can enter.

This is an exact theorem for the terminal inverse-limit over-family, not a
closure of the complete physical E=13 path.  The first five even-event ranks
enter the 3-adic correction later and can only further restrict the 247
terminal survivors.
"""

from __future__ import annotations

from functools import lru_cache
import hashlib

MAX_CREDIT = 397
EXPECTED_COUNT = 247
EXPECTED_SHA256 = "44fee8803323a1e29d6759ecad1ebd07a1e3a4f19ce9413500faa353eec37ae9"

# Exact early-event maxima already certified by the E=13 run-cover analysis.
EARLY_MAX = (72, 186, 365, 647, 1093)
Q = 1526


def assigned_block_sum(remaining_after: int, remaining_before: int) -> int:
    """Sum 2^j over the suffix assigned at the current 3-adic exponent."""
    assert 0 <= remaining_after <= remaining_before <= 8
    return (1 << (5 + remaining_before)) - (1 << (5 + remaining_after))


@lru_cache(maxsize=None)
def accepts(a: int, b: int, carry: int) -> bool:
    """Exact inverse-limit reachability to zero carry."""
    assert 0 <= a <= 8 and 0 <= b <= 8

    if carry == 0:
        # All still-unassigned ranks may be sent to e=infinity.
        return True

    # Assign nothing on either side at this 3-adic level.
    # This transition is legal iff the current digit vanishes.  It strictly
    # shrinks |carry|, so it cannot form a nonzero recursion cycle.
    if carry % 3 == 0:
        next_carry = 2 * (carry // 3)
        assert abs(next_carry) < abs(carry)
        if accepts(a, b, next_carry):
            return True

    # At least one side assigns a nonempty suffix.  Then a+b strictly falls.
    for a2 in range(a + 1):
        actual = assigned_block_sum(a2, a)
        for b2 in range(b + 1):
            if a2 == a and b2 == b:
                continue
            alternate = assigned_block_sum(b2, b)
            numerator = carry + alternate - actual
            if numerator % 3:
                continue
            next_carry = 2 * (numerator // 3)
            if accepts(a2, b2, next_carry):
                return True

    return False


def first_visibility_depth(rank: int) -> int:
    """First K where rank j can affect C(P) modulo 3^K."""
    # e_j = Q-p_j+j.  A term affects mod 3^K iff e_j < K.
    return Q - EARLY_MAX[rank] + rank + 1


def main() -> None:
    survivors = [
        d for d in range(1, MAX_CREDIT + 1)
        if accepts(8, 8, (1 << 13) * d)
    ]

    assert len(survivors) == EXPECTED_COUNT
    digest = hashlib.sha256(",".join(map(str, survivors)).encode()).hexdigest()
    assert digest == EXPECTED_SHA256

    # 4096 is the specific G13 4096->1 entrance relation.  It is absent from
    # the terminal inverse-limit set, agreeing with the independent finite
    # obstruction that already dies modulo 3^28.
    assert not accepts(8, 8, (1 << 13) * 4096)

    activation = [first_visibility_depth(j) for j in range(5)]
    assert activation == [1455, 1342, 1164, 883, 438]

    # Therefore no early rank j=0..4 can alter any terminal conclusion through
    # K=437.  The previously certified 150 removals by K=30 are permanent for
    # the full physical E=13 problem.
    assert min(activation) == 438

    print("E13 terminal inverse-limit automaton: PASS")
    print("surviving bounded credits =", len(survivors))
    print("survivor sha256 =", digest)
    print("removed bounded credits =", MAX_CREDIT - len(survivors))
    print("4096 terminally liftable = False")
    print("early-rank first visibility K (j=0..4) =", activation)
    print("next physical activation order: j=4@438, j=3@883, j=2@1164, j=1@1342, j=0@1455")
    print("survivors:")
    print(",".join(map(str, survivors)))


if __name__ == "__main__":
    main()
