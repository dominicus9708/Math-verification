#!/usr/bin/env python3
"""MATH-073 regression for the exact dyadic-resolution Bellman lemma.

Universal content is algebraic and stated/proved in the companion note.
This script checks the discrete resolution inequality for all source counts
2 <= M <= 1,000,000.

It does not prove first-cell emptiness or Collatz.
"""

MAX_M = 1_000_000
LAMBDA_NUM = 19
LAMBDA_DEN = 503


def R(M: int) -> int:
    assert M >= 1
    return (M - 1).bit_length()  # ceil(log2 M)


def main():
    for M in range(2, MAX_M + 1):
        r = R(M)
        # The two children of a dyadic residue refinement have floor/ceil(M/2)
        # lifts.  Empty children are irrelevant.
        for child in (M // 2, (M + 1) // 2):
            if child == 0:
                continue
            rp = R(child)
            assert rp <= r - 1

            # Worst penalty increment is p=0.  For H_R=-lambda R,
            # p-lambda + H'-H >= -lambda + lambda(R-R') >= 0.
            assert r - rp >= 1

    print("PASS MATH-073 resolution Bellman regression", MAX_M)


if __name__ == "__main__":
    main()
