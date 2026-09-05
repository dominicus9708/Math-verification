#!/usr/bin/env python3
"""Proof-control certificate for the A0 surplus formation-domain gap.

This certificate does not prove a Collatz theorem.  It checks the logical
scope relation used by the DSD audit: C4 emits all integer surplus sectors
s >= 1, whereas the current minimal-surplus Hensel calculation C6A covers
only s = 1.  Therefore C6A cannot be substituted for an all-surplus bridge.

Only Python's standard library is used.
"""

from fractions import Fraction


# Exact A0 decomposition data.
J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991
U = 9_809_721_694
P = 6_189_245_291


assert A0 == 10 * J0 + U
assert Q0 == 10 * R0 + P


def in_C4_surplus_domain(s: int) -> bool:
    """Abstract formation domain emitted by the C4 theorem."""
    return isinstance(s, int) and 1 <= s <= P


def in_C6A_minimal_domain(s: int) -> bool:
    """Current minimal-surplus Hensel subproblem."""
    return s == 1


def tail_odd_count(s: int) -> int:
    assert in_C4_surplus_domain(s)
    return P - s


def relative_prefix_factor(s: int) -> int:
    """C_pre(s+1)/C_pre(s) = 3 exactly; integer representation."""
    assert in_C4_surplus_domain(s)
    return 3 ** (s - 1)


def relative_tail_factor(s: int) -> Fraction:
    """C_tail(s)/C_tail(1) = 3^(1-s) exactly."""
    assert in_C4_surplus_domain(s)
    return Fraction(1, 3 ** (s - 1))


def main() -> None:
    # Witness that the C4 formation domain is strictly wider than C6A.
    witness = 2
    assert in_C4_surplus_domain(witness)
    assert not in_C6A_minimal_domain(witness)

    # Changing s changes actual terminal combinatorial data.
    assert tail_odd_count(1) == P - 1
    assert tail_odd_count(2) == P - 2
    assert tail_odd_count(1) != tail_odd_count(2)

    # Homogeneous prefix/tail changes cancel only multiplicatively.
    for s in range(1, 8):
        assert relative_prefix_factor(s) * relative_tail_factor(s) == 1

    print("DSD surplus scope-gap audit: PASS")
    print(f"A0 decomposition: ({A0},{Q0}) = 10*({J0},{R0}) + ({U},{P})")
    print("C4 formation domain: integer surplus 1 <= s <= P")
    print("C6A formation domain: s = 1 only")
    print("strict-scope witness: s=2 belongs to C4 but not C6A")
    print("tail odd count changes: P-1 != P-2")
    print("homogeneous s-dependence cancels, but this certificate makes no")
    print("claim that affine correction or Hensel admissibility is monotone in s")
    print("REQUIRED OPEN BRIDGE: C6B must cover every admissible s >= 1")
    print("NOTE: PASS certifies proof-scope separation only; Collatz remains open.")


if __name__ == "__main__":
    main()
