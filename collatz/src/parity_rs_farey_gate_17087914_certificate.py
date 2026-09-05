#!/usr/bin/env python3
"""Exact certificate for the Farey extension of the parity-RS coefficient gate.

External input (not reverified here): convergence of every positive integer
below 2^71, as reported by Barina.

Everything after that finite frontier is checked with exact Python integers.
"""

B = 1 << 71

# Lower rational wall used by the parity-RS theorem.
p = 190_537
q = 301_994

# An exact upper neighbour for alpha = log_3(2).
u = 10_590_737
v = 16_785_921

# Farey mediant / first possible intervening denominator.
P = p + u
Q = q + v


def main() -> None:
    # The parity-RS adjusted multiplier condition:
    # (3 + 1/B)^p < 2^q.
    assert pow(3 * B + 1, p) < (1 << q) * pow(B, p)

    # p/q < alpha < u/v, alpha=log_3(2), checked without floating point.
    assert pow(3, p) < (1 << q)
    assert pow(3, u) > (1 << v)

    # Farey-neighbour determinant.
    assert u * q - p * v == 1

    # The mediant is still below alpha; hence it produces the first floor split.
    assert P == 10_781_274
    assert Q == 17_087_915
    assert pow(3, P) < (1 << Q)

    # Determinants with the mediant.
    assert P * q - p * Q == 1
    assert u * Q - P * v == 1

    print("PASS parity-RS Farey coefficient gate")
    print(f"lower={p}/{q}")
    print(f"upper={u}/{v}")
    print(f"first_intervening_mediant={P}/{Q}")
    print(f"coefficient_survival_forced_through={Q-1}")
    print(f"first_possible_floor_split={Q}")


if __name__ == "__main__":
    main()
