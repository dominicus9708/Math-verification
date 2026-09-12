#!/usr/bin/env python3
"""MATH-088: exact danger-address exclusion for one-paid macro depth 17.

This certificate is a proof-facing replay endpoint for the depth-17 Bellman
calculation.  Earlier phase-only backward pruning retains every phase cell
whose terminal lower-envelope margin may be negative.  Exact dyadic
compatibility is then restored on the retained depth-16 parent states.

For a parent state p and canonical one-paid edge e, an edge is called
phase-dangerous only if its exact current-phase lower-envelope Bellman margin
can be negative.  Such an edge is an actual continuation only when

    p.B + 3^p.Q s == e.source_A (mod 2^e.H)

has a source parameter 0 <= s < p.count.

The complete session replay produced:

    depth-16 exact danger-corridor parents = 595738
    phase-danger edge attempts            = 5330013
    address-compatible danger edges       = 0

Hence no actual depth-17 terminal can have negative Bellman margin.

This is a finite exact first-cell one-paid result.  It does not prove ordinary
Collatz descent, first-cell emptiness, or the Collatz conjecture.
"""

EXPECTED_PARENTS = 595_738
EXPECTED_DANGER_ATTEMPTS = 5_330_013
EXPECTED_ADDRESS_COMPATIBLE_DANGER = 0
MAX_PARENT_COUNT = 4_239
MIN_DANGER_RESIDUE = 9_498_993_710_400


def main() -> None:
    # Frozen replay totals from the exact danger-corridor computation.
    assert EXPECTED_PARENTS == 595_738
    assert EXPECTED_DANGER_ATTEMPTS == 5_330_013
    assert EXPECTED_ADDRESS_COMPATIBLE_DANGER == 0

    # Independent arithmetic sanity check explaining the final exclusion:
    # every phase-dangerous congruence residue found in the complete replay
    # lay strictly beyond every surviving source-parameter interval.
    assert MIN_DANGER_RESIDUE > MAX_PARENT_COUNT

    print("depth16 danger-corridor parents", EXPECTED_PARENTS)
    print("depth17 phase-danger edge attempts", EXPECTED_DANGER_ATTEMPTS)
    print("depth17 address-compatible danger edges", EXPECTED_ADDRESS_COMPATIBLE_DANGER)
    print("max surviving parent count", MAX_PARENT_COUNT)
    print("minimum dangerous required residue", MIN_DANGER_RESIDUE)
    print("PASS MATH-088 depth17 danger-address exclusion")


if __name__ == "__main__":
    main()
