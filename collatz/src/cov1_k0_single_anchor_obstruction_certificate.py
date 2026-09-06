#!/usr/bin/env python3
"""Exact finite certificate that k=0 (x=27) is not covered by the inverse
merge language anchored specifically at T(x)=41.

A smaller merge through this anchor would require some 1<=m<27 whose shortcut
Collatz orbit reaches 41.  We follow each m until it enters the 1-2 cycle; none
reaches 41.

This does NOT say 27 is non-recursive or nonconvergent.  In fact 27 has a later
forward iterate 23<27.  It only disproves completeness of the single anchor 41.
"""


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def first_below_27():
    x = 27
    for j in range(1, 1000):
        x = T(x)
        if x < 27:
            return j, x
    raise AssertionError("regression bound too short")


def main():
    for m in range(1, 27):
        x = m
        seen = set()
        while x not in seen:
            assert x != 41
            seen.add(x)
            x = T(x)
        # For all m<27, the repeated cycle is the usual 1<->2 shortcut cycle.
        assert x in (1, 2)

    j, x = first_below_27()
    assert (j, x) == (59, 23)

    print("SAFE finite anchor obstruction")
    print("No m in [1,26] reaches anchor 41.")
    print("Therefore k=0, x=27 is not in the T(x)-anchored inverse coverage set.")
    print("Separately, T^59(27)=23<27, so this is not a Collatz obstruction.")


if __name__ == "__main__":
    main()
