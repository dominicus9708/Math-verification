#!/usr/bin/env python3
"""Exact pre-G13 even-position formation bridge for the current R1 core.

This certificate replaces enumeration of sparse 1539-step parity words by an
exact affine identity in the ordered positions of the forward-even events.

For U=x+1 and T accelerated Collatz steps, let
    0 <= p_0 < ... < p_{E-1} < T
be the positions of the E forward-even events, and q=T-E. Then

    2^T U_T / 3^q
      = U_0 + sum_{j=0}^{E-1} 3^j (2/3)^{p_j}.

Current m=44 starts satisfy N == 3 mod 4, so the first two accelerated parity
symbols are odd. Hence p_j >= j+2 and

    0 < epsilon_E
      := sum 3^j (2/3)^{p_j}
      <= (4/9)(2^E-1).

For a fixed G13 entrance X=x_1539 this confines every E-event pre-gate root N
to a short exact interval. In particular E=13 gives at most 3641 ordinary
integer roots, rather than C(73,9) first-73 parity words.

The known finite-natural G13 sample is also rechecked: its E=14 root window
contains 7282 ordinary integers but zero members of the current m=44 core.

No floating-point arithmetic is used. This is a structural/candidate-specific
certificate; it does not close the full E=13 G13 natural section and does not
prove the Collatz conjecture.
"""

from fractions import Fraction

T = 1539
E13 = 13
E14 = 14

N0 = 3_939_105_844_976_711_153_619
NMAX = 5_908_625_413_101_667_397_287

X0 = int(
    "9311066934133191055179217771751644756458780835642375520644606697570370834878851085876330120952372828601875854086643506229770877868471756436379730259097164274868063513702695410370082518062231340901656195848133042167901156081765468572447679246085622583924868464925000059470402523777450879"
)


def accelerated_step(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def ceil_fraction(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def formation_epsilon(positions: list[int]) -> Fraction:
    return sum(
        (Fraction(3) ** j) * (Fraction(2, 3) ** p)
        for j, p in enumerate(positions)
    )


def exact_endpoint_from_positions(N: int, positions: list[int], total_steps: int) -> Fraction:
    """Endpoint U_T reconstructed from the formation identity."""
    E = len(positions)
    q = total_steps - E
    eps = formation_epsilon(positions)
    return Fraction(3**q, 2**total_steps) * (Fraction(N + 1) + eps)


def direct_endpoint_and_even_positions(N: int, total_steps: int) -> tuple[int, list[int]]:
    x = N
    positions: list[int] = []
    for t in range(total_steps):
        if not (x & 1):
            positions.append(t)
        x = accelerated_step(x)
    return x + 1, positions


def epsilon_max(E: int) -> Fraction:
    return Fraction(4 * (2**E - 1), 9)


def root_window(X: int, E: int) -> tuple[int, int]:
    """All integer N compatible with E even events and N == 3 mod 4 lie here.

    From N+1 = Y-epsilon, with
      Y = 2^T (X+1) / 3^(T-E)
      0 < epsilon <= epsilon_max(E),
    we get
      Y-epsilon_max(E)-1 <= N < Y-1.
    """
    q = T - E
    Y = Fraction((1 << T) * (X + 1), 3**q)
    lo = ceil_fraction(Y - epsilon_max(E) - 1)
    # Strict upper endpoint: largest integer N with N < Y-1.
    hi = ceil_fraction(Y - 1) - 1
    return lo, hi


def in_current_m44_core(N: int) -> bool:
    if N < N0 or N > NMAX or N % 4 != 3:
        return False
    y = (N - 3) // 4
    for _ in range(44):
        d = y % 3
        if d > 1:
            return False
        y //= 3
    return y == 1


def main() -> None:
    # Algebraic identity implementation audit on several ordinary starts.
    for N, steps in [(3, 20), (7, 30), (27, 50), (97, 60), (871, 80)]:
        direct_U, positions = direct_endpoint_and_even_positions(N, steps)
        reconstructed_U = exact_endpoint_from_positions(N, positions, steps)
        assert reconstructed_U.denominator == 1
        assert reconstructed_U.numerator == direct_U

    # Current m=44 formation condition N == 3 mod 4 forces parity prefix 11.
    # If N=4k+3, the first accelerated odd image is 6k+5, also odd.
    for k in range(32):
        N = 4 * k + 3
        assert N & 1
        assert accelerated_step(N) & 1

    # Ordered even-event positions therefore satisfy p_j >= j+2.
    # The extremal position set realizes the analytic upper bound exactly.
    for E in range(1, 21):
        extremal = list(range(2, E + 2))
        assert formation_epsilon(extremal) == epsilon_max(E)

    assert epsilon_max(E13) == Fraction(32764, 9)
    assert ceil_fraction(epsilon_max(E13)) == 3641
    assert epsilon_max(E14) == Fraction(21844, 3)
    assert ceil_fraction(epsilon_max(E14)) == 7282

    # High-prefix factorization for E=13.
    # X+1 = h*2^879 + ell, 0<=ell<2^879:
    # Y = lambda*h + eta, with 0<=eta<lambda<1.
    lam = Fraction(1 << 2418, 3**1526)
    assert (1 << 2418) < 3**1526
    assert lam < 1
    high_prefix_window_width = epsilon_max(E13) + lam
    assert high_prefix_window_width < Fraction(3642, 1)
    assert ceil_fraction(high_prefix_window_width) == 3642

    # Candidate-specific exact recheck for the known finite-natural G13 sample.
    lo13, hi13 = root_window(X0, E13)
    assert hi13 - lo13 + 1 <= 3641
    assert hi13 < N0  # E=13 cannot attach even to the current numeric interval.

    lo14, hi14 = root_window(X0, E14)
    assert (lo14, hi14) == (
        4_408_078_582_391_475_480_628,
        4_408_078_582_391_475_487_909,
    )
    assert hi14 - lo14 + 1 == 7282

    core_matches = [
        N for N in range(max(lo14, N0), min(hi14, NMAX) + 1)
        if in_current_m44_core(N)
    ]
    assert core_matches == []

    print("pre-G13 even-position formation bridge: PASS")
    print("identity: 2^T U_T / 3^(T-E) = U_0 + epsilon_E")
    print("current-core prefix: first two accelerated parity bits are 11")
    print("epsilon_13_max = 32764/9; integer root count <= 3641")
    print("E13 high-prefix low-879-bit uncertainty lambda < 1")
    print("high-prefix root window integer count <= 3642")
    print(f"known_X0 E13 root_window=[{lo13},{hi13}] outside current interval")
    print(f"known_X0 E14 root_window=[{lo14},{hi14}] count=7282")
    print("known_X0 E14 current_m44_core_matches=0")
    print("candidate-specific E14 attachment exclusion: PASS")


if __name__ == "__main__":
    main()
