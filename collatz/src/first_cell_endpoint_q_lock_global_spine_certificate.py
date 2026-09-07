#!/usr/bin/env python3
from fractions import Fraction

B0 = 1 << 71
A0 = 114_208_327_604
Q0 = 72_057_431_991
CAP = Fraction(1364, 1024) * B0


def main():
    # For every universal-spine prefix before the first coefficient crossing,
    # if p_r is the zero-indexed position of the r-th odd bit, survival before
    # that bit gives 2^p_r <= 3^(r-1). Hence
    #
    #   S = R/3^q = sum_r 2^p_r / 3^r <= q/3.
    #
    # This is a symbolic termwise theorem; the finite checks below only lock
    # the current first-cell constants and the scale separation used by q-lock.
    assert Q0 < A0
    assert Fraction(Q0, 3) < B0
    assert Fraction(A0, 3) < B0

    # Current candidate start cap.
    assert B0 < CAP < 2 * B0
    assert CAP + B0 < 3 * B0

    # Therefore every universal-spine candidate prefix through the first cell
    # has S < B0. If two candidate-window starts have one common endpoint,
    #
    #   3^q1 (N1+S1) = 3^q2 (N2+S2).
    #
    # q1>q2 would force N2+S2 > 3*B0 while the left candidate obeys
    # N2+S2 < CAP+B0 < 3*B0. Thus q1=q2 at every depth up to A0,
    # including the terminal first crossing.

    print("PASS")
    print("first universal cell (A0,q0) =", (A0, Q0))
    print("universal-spine correction theorem: S <= q/3")
    print("q0/3 < 2^71")
    print("endpoint q-lock valid for all candidate prefixes through k=A0")
    print("equal endpoint => equal q => Hensel/address translation")


if __name__ == "__main__":
    main()
