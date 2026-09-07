#!/usr/bin/env python3
from fractions import Fraction

B0 = 1 << 71
CAP = Fraction(1364, 1024) * B0
KMAX = 195


def min_q_survival(k: int) -> int:
    """Least q with 3^q >= 2^k, exact integer arithmetic."""
    q = 0
    p3 = 1
    target = 1 << k
    while p3 < target:
        p3 *= 3
        q += 1
    return q


def correction_envelope(k: int, q: int) -> Fraction:
    """S=R/3^q <= 2^(k-q)*(1-(2/3)^q)."""
    assert 1 <= q <= k
    return Fraction(1 << (k - q), 1) * (Fraction(1) - Fraction(2, 3) ** q)


def main():
    worst = Fraction(0)
    worst_pair = None

    # For coefficient-surviving q, the normalized-correction envelope is
    # decreasing in q, so checking the least surviving q at every k suffices.
    for k in range(1, KMAX + 1):
        q = min_q_survival(k)
        env = correction_envelope(k, q)
        assert env < B0
        if env > worst:
            worst = env
            worst_pair = (k, q)

    assert worst_pair == (195, 124)

    # Candidate first-cell starts now lie in
    #   B0 < N < (1364/1024) B0.
    # Hence for any candidate start N and any coefficient-surviving prefix
    # through k<=195, N+S < CAP+B0 < 3 B0.
    assert CAP + B0 < 3 * B0

    # Equal endpoint y for two length-k prefixes gives
    #   3^q1 (N1+S1) = 3^q2 (N2+S2).
    # If q1>q2 then N2+S2 = 3^(q1-q2)(N1+S1) > 3 B0,
    # contradicting the uniform upper bound CAP+B0 < 3 B0.
    # Therefore equal-endpoint candidate starts have q1=q2 through depth195.

    # With q locked, equal endpoints imply
    #   R1-R2 = 3^q (N2-N1).
    # Thus N1<N2 iff R1>R2: the smallest start is the largest correction
    # representative among candidate-window members of that endpoint group.

    print("PASS")
    print("first-cell cap = (1364/1024)*2^71")
    print("endpoint q-lock depth =", KMAX)
    print("worst correction envelope occurs at (k,q) =", worst_pair)
    print("all coefficient-surviving S envelopes through depth195 are < 2^71")
    print("equal endpoint inside current candidate window => equal odd count")
    print("with equal q: smaller start <=> larger correction")


if __name__ == "__main__":
    main()
