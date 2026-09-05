#!/usr/bin/env python3
"""Exact finite audit for Beatty parity / signed-skew coordinate identities.

The theorem being checked is algebraic and proved in the companion note:

  full parity-prefix coefficient survival
    <=> checkpoint inequalities q >= b_{A_q}
    <=> signed skew s_q >= 0 at every accelerated checkpoint.

This certificate exhausts valuation blocks v_q in {1,2,3,4} through depth 7
and uses integer powers only for all Beatty/barrier decisions.  It also checks
that checkpoint Beatty slack zero is equivalent to

  3^(q-1) < 2^(A_q) <= 3^q.

Finite exhaustion is an independent audit, not the proof of the general lemma.
"""

from itertools import product

MAX_Q = 7
MAX_V = 4


def barrier(L: int) -> int:
    """b_L=min{q:3^q>=2^L}, with no floating point."""
    assert L >= 0
    target = 1 << L
    q = 0
    p3 = 1
    while p3 < target:
        q += 1
        p3 *= 3
    return q


def floor_q_log2_3(q: int) -> int:
    """floor(q log_2 3)=floor(log_2(3^q)) exactly."""
    assert q >= 0
    return (3**q).bit_length() - 1


def audit_code(vs: tuple[int, ...]) -> None:
    # Half-step parity expansion of accelerated valuation blocks:
    # each v_q contributes 1 followed by v_q-1 zeros.
    bits: list[int] = []
    A = [0]
    for v in vs:
        assert v >= 1
        bits.append(1)
        bits.extend([0] * (v - 1))
        A.append(A[-1] + v)

    # q_L = number of odd/parity-1 states in the first L half-steps.
    prefix_ones = [0]
    running = 0
    for bit in bits:
        running += bit
        prefix_ones.append(running)

    full_survival = all(
        prefix_ones[L] >= barrier(L)
        for L in range(1, len(bits) + 1)
    )

    checkpoint_survival = True

    for q in range(1, len(A)):
        Aq = A[q]

        # Exact renewal/checkpoint identity.
        assert prefix_ones[Aq] == q

        # Signed skew s_q=floor(q log_2 3)-A_q.
        s_q = floor_q_log2_3(q) - Aq

        # Checkpoint coefficient inequality <=> nonnegative signed skew.
        assert (q >= barrier(Aq)) == (s_q >= 0)
        checkpoint_survival &= s_q >= 0

        # Exact Beatty slack and its integer-power boundary test.
        sigma_q = q - barrier(Aq)
        boundary_by_slack = sigma_q == 0
        boundary_by_powers = 3 ** (q - 1) < (1 << Aq) <= 3**q
        assert boundary_by_slack == boundary_by_powers

        if s_q >= 0:
            assert sigma_q >= 0

    # Checkpoints are sufficient for all intermediate prefix inequalities.
    assert full_survival == checkpoint_survival


def main() -> None:
    tested = 0
    for Q in range(1, MAX_Q + 1):
        for vs in product(range(1, MAX_V + 1), repeat=Q):
            audit_code(vs)
            tested += 1

    print("Beatty parity / signed-skew coordinate certificate: PASS")
    print("valuation codes tested", tested)
    print("max accelerated depth", MAX_Q)
    print("valuation alphabet", f"1..{MAX_V}")
    print("all Beatty comparisons used exact integer powers")
    print()
    print("THEOREM STATUS")
    print("  exact coordinate lemma: proved symbolically in companion note")
    print("  finite exhaustive certificate: independent audit only")
    print("  canonical lift t_q is NOT the Beatty parity bit")


if __name__ == "__main__":
    main()
