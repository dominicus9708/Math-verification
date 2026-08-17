#!/usr/bin/env python3
"""Cutoff-free terminal 3-adic formation automaton for E=13 pre-G13 relations.

For the last eight even-event ranks j=5,...,12 write

    e_j = Q - p_j + j,

so p_5<...<p_12 is equivalent to

    e_5 >= e_6 >= ... >= e_12 >= 0.

After division by the 3-adic unit 2^Q, the terminal code is

    S(e) = sum_{j=5}^{12} 2^(j-e_j) 3^e_j.

Allow e_j=infinity to represent ranks invisible at every finite terminal
3-adic depth.  A right-boundary credit d is terminally liftable iff

    -2^13 d in S_8 - S_8   in Z_3.

At one ternary level let a,b in {0,...,8} be the numbers of still-unassigned
terminal ranks on the actual and alternate sides.  Choosing a'<=a,b'<=b
assigns suffixes with block sum

    A(a',a)=2^(5+a)-2^(5+a').

For scaled carry c, the next state exists exactly when

    c + A(b',b) - A(a',a) == 0 (mod 3),

with

    c'=(2/3)[c + A(b',b) - A(a',a)].

A no-assignment step keeps a,b fixed but strictly decreases |c| unless c=0;
every other step decreases a+b.  The recursion is therefore well-founded and
contains no depth cutoff.

Exact outputs:

* d=1..397: 247 terminal survivors, matching the earlier K=30..36 plateau;
* d=1..6859: 403 terminal survivors.

The second range covers the full positive parent-credit envelope of the
survival-conditioned G13 transition section.  It is only a terminal necessary
set; the two-ended run-feasibility certificate removes the remaining 403.
"""

from __future__ import annotations

from functools import lru_cache
import hashlib

BOUNDED_MAX = 397
TRANSITION_MAX = 6859
EXPECTED_397_COUNT = 247
EXPECTED_397_SHA256 = "44fee8803323a1e29d6759ecad1ebd07a1e3a4f19ce9413500faa353eec37ae9"
EXPECTED_6859_COUNT = 403
EXPECTED_6859_SHA256 = "70e31292340274d7a39b283851671f6675e3b94eeeb682f24b5ca37eb3339302"

EARLY_MAX = (72, 186, 365, 647, 1093)
Q = 1526


def assigned_block_sum(remaining_after: int, remaining_before: int) -> int:
    assert 0 <= remaining_after <= remaining_before <= 8
    return (1 << (5 + remaining_before)) - (1 << (5 + remaining_after))


@lru_cache(maxsize=None)
def accepts(a: int, b: int, carry: int) -> bool:
    assert 0 <= a <= 8 and 0 <= b <= 8
    if carry == 0:
        return True

    if carry % 3 == 0:
        next_carry = 2 * (carry // 3)
        assert abs(next_carry) < abs(carry)
        if accepts(a, b, next_carry):
            return True

    for a2 in range(a + 1):
        actual = assigned_block_sum(a2, a)
        for b2 in range(b + 1):
            if a2 == a and b2 == b:
                continue
            alternate = assigned_block_sum(b2, b)
            numerator = carry + alternate - actual
            if numerator % 3:
                continue
            if accepts(a2, b2, 2 * (numerator // 3)):
                return True
    return False


def survivor_list(limit: int) -> list[int]:
    return [d for d in range(1, limit + 1) if accepts(8, 8, (1 << 13) * d)]


def digest(values: list[int]) -> str:
    return hashlib.sha256(",".join(map(str, values)).encode()).hexdigest()


def first_visibility_depth(rank: int) -> int:
    return Q - EARLY_MAX[rank] + rank + 1


def main() -> None:
    s397 = survivor_list(BOUNDED_MAX)
    assert len(s397) == EXPECTED_397_COUNT
    assert digest(s397) == EXPECTED_397_SHA256

    s6859 = survivor_list(TRANSITION_MAX)
    assert len(s6859) == EXPECTED_6859_COUNT
    assert digest(s6859) == EXPECTED_6859_SHA256

    assert not accepts(8, 8, (1 << 13) * 4096)

    activation = [first_visibility_depth(j) for j in range(5)]
    assert activation == [1455, 1342, 1164, 883, 438]

    print("E13 terminal inverse-limit automaton: PASS")
    print("1..397 survivors =", len(s397), "sha256 =", digest(s397))
    print("1..6859 survivors =", len(s6859), "sha256 =", digest(s6859))
    print("4096 terminally liftable = False")
    print("early-rank first visibility K (j=0..4) =", activation)


if __name__ == "__main__":
    main()
