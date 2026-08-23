#!/usr/bin/env python3
"""Exact arithmetic certificate for unconditional m=45 root maximality to H=200.

For a length-H q-odd parity word, the maximum possible affine correction is

    R_max(H,q) = 2^(H-q) (3^q - 2^q),

obtained by placing all q odd events in the final q positions.  Hence any
same-q complete-Hensel correction difference R'-R=3^q d satisfies

    0 < d < R_max/3^q < 2^(H-q).

Coefficient survival through H forces 3^q >= 2^H.  The m=45 recursively
sufficient roots all satisfy 2^73 < N < 2^74.  Therefore whenever H-q <= 73,
any positive complete-prefix sibling credit automatically satisfies d<N and
is a valid smaller-root predecessor.

This script proves exactly that the worst coefficient-surviving q has
H-q <=73 for every H<=200, while H=201 is the first horizon where the crude
uniform bound reaches H-q=74.

This is a finite root-maximality range theorem, not a proof of Collatz.
"""


def qmin(H: int) -> int:
    q = 0
    p3 = 1
    p2 = 1 << H
    while p3 < p2:
        p3 *= 3
        q += 1
    return q


def main() -> None:
    m = 45
    n_min = 4 * 3**m + 3
    n_max = 4 * (3**m + (3**44 - 1)//2) + 3

    assert 2**73 < n_min < n_max < 2**74

    last_safe = 0
    for H in range(1, 400):
        q = qmin(H)
        slack = H - q
        if slack <= 73:
            last_safe = H
            # Every same-q positive whole-prefix credit obeys d<2^slack.
            assert 2**slack <= 2**73 < n_min
        elif H == last_safe + 1:
            first_unsafe = H
            first_unsafe_q = q
            first_unsafe_slack = slack
            break

    assert last_safe == 200
    assert first_unsafe == 201
    assert qmin(200) == 127
    assert 200 - qmin(200) == 73
    assert first_unsafe_q == 127
    assert first_unsafe_slack == 74

    print("m45 N range:", n_min, n_max)
    print("2^73 < N < 2^74: PASS")
    print("last uniformly root-maximality-safe horizon:", last_safe)
    print("H=200 qmin=127 slack=73")
    print("H=201 qmin=127 slack=74 (crude uniform guarantee ends)")
    print("m45 root maximality horizon-200 certificate: PASS")


if __name__ == "__main__":
    main()
