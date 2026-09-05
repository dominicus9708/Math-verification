#!/usr/bin/env python3
"""Exact algebra certificate for the growing-Q Gate-F reduction.

This program does NOT prove the moving low-height strip theorem.
It certifies the finite integer identities and exponent arithmetic used in
`2026-09-06-gate-F-growing-Q-compatibility-reduction.md`.
"""

from fractions import Fraction


def active_height(Q: int) -> int:
    """H_Q=max{H>=0: 2^(H+Q) <= 3^Q}, using integer arithmetic only."""
    assert Q >= 1
    H = 0
    while (1 << (H + 1 + Q)) <= 3**Q:
        H += 1
    assert (1 << (H + Q)) <= 3**Q
    assert (1 << (H + 1 + Q)) > 3**Q
    return H


def healing_valuation(v0: int, Q: int, steps: int) -> int:
    """Valuation lower bound under one exact +1 gain per common odd event."""
    assert 0 <= v0 <= Q
    assert steps >= 0
    return min(Q, v0 + steps)


def admissible_beta(gamma: Fraction, A: int) -> Fraction:
    assert gamma < 1
    assert A >= 0
    return Fraction(1 - gamma, A + 1)


def main() -> None:
    # Finite-Q healing arithmetic: worst-case v3 defect starts at 0.
    for Q in range(1, 257):
        assert healing_valuation(0, Q, Q) == Q
        for v0 in range(Q + 1):
            need = Q - v0
            assert healing_valuation(v0, Q, need) == Q

    # Exact active-height characterization for a substantial finite range.
    previous = -1
    for Q in range(1, 2001):
        H = active_height(Q)
        assert H >= previous
        # H_Q/Q is bounded above by 1 because (3/2)<2.
        assert 0 <= H <= Q
        previous = H

    # Conditional polynomial-height exponent arithmetic.
    gamma = Fraction(1, 9)
    expected = {
        0: Fraction(8, 9),
        1: Fraction(4, 9),
        2: Fraction(8, 27),
        3: Fraction(2, 9),
        4: Fraction(8, 45),
    }
    for A, target in expected.items():
        beta_star = admissible_beta(gamma, A)
        assert beta_star == target
        # At beta=beta_star the q exponent is exactly zero;
        # strict inequality beta<beta_star is therefore required for o(1).
        exponent = beta_star * (A + 1) + gamma - 1
        assert exponent == 0

    print("Gate F growing-Q algebra certificate: PASS")
    print("finite-Q healing: exact for every tested Q<=256")
    print("active-height integer characterization: exact for Q<=2000")
    print("conditional exponent table for gamma=1/9:")
    for A in range(5):
        print(f"  A={A}: beta < {admissible_beta(gamma, A)}")
    print()
    print("THEOREM STATUS")
    print("  F_heal: pointwise algebra closed for arbitrary finite Q")
    print("  F_map: OPEN")
    print("  F_unif: OPEN")
    print("  required moving-strip target:")
    print("    (Q(q)+2) * N_q(H_{Q(q)}+1) = o(q)")


if __name__ == "__main__":
    main()
