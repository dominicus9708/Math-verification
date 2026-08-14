#!/usr/bin/env python3
"""Exact integer certificate for the gate-wide Hensel cubes.

For each certified Euclidean gate vector (L,q), the script checks the prefix-
power inequalities for the minimal all-01 vertices of

  neutral:    1^(2q-L+1) (01)^(L-q-1) 0
  one-slack:  1^(2q-L-1) (01)^(L-q)   0

The comparisons use Python arbitrary-precision integers only.
"""

GATES = (
    ("G81", 1539, 971, 567, 568),
    ("G82", 1558, 983, 574, 575),
    ("G13", 20026, 12635, 7390, 7391),
    ("G14", 21565, 13606, 7958, 7959),
)


def prefix_ones(L: int, q: int, J: int, t: int) -> int:
    """Prefix ones in 1^(q-J) (01)^J 0^(L-q-J)."""
    F = q - J
    if t <= F:
        return t
    if t <= F + 2 * J:
        return F + (t - F) // 2
    return q


def audit(name: str, L: int, q: int, J0: int, J1: int) -> None:
    E = L - q
    assert J0 == E - 1
    assert J1 == E

    # Neutral cube: q actual odds, endpoint relative height zero.
    for t in range(1, L):
        b = prefix_ones(L, q, J0, t)
        assert 3**b >= 2**t, (name, "neutral", t, b)
    assert prefix_ones(L, q, J0, L) == q

    # One-slack cube: q-1 actual odds, endpoint relative height -1.
    q1 = q - 1
    for t in range(1, L):
        b = prefix_ones(L, q1, J1, t)
        assert 3 ** (b + 1) >= 2**t, (name, "one-slack", t, b)
    assert prefix_ones(L, q1, J1, L) == q - 1

    F0 = q - J0
    F1 = (q - 1) - J1
    print(
        name,
        "L", L,
        "q", q,
        "E", E,
        "neutral_fixed1", F0,
        "neutral_J", J0,
        "one_slack_fixed1", F1,
        "one_slack_J", J1,
    )


def main() -> None:
    for args in GATES:
        audit(*args)


if __name__ == "__main__":
    main()
