#!/usr/bin/env python3
"""Exact E=13 channel-conditioned pre-G13 formation filter.

This certificate combines four previously established exact inputs for the
current isolated R1 branch:

1. the present m=44 numerical ceiling N<=NMAX;
2. total pre-G13 even count E=13;
3. the six surviving first-defect channels p in {2,5,8,10,13,16};
4. the current necessary Cantor masses after the depth-27 Hensel filters
   (and the targeted p=16 low-ternary reduction).

The key new step is a suffix-feasibility lower bound on the ordered even-event
positions p_j.  In U=x+1 coordinates an odd run of length r requires
r<=floor(log2 U).  The exact exchange O(E(U))-E(O(U))=1/4 implies that, for a
fixed number of steps and evens, pushing odd steps left maximizes the endpoint.
Likewise, repeatedly taking the longest currently admissible odd run before an
even maximizes the number of future steps coverable with a fixed even budget.

For E=13 this yields the exact necessary coordinate-wise lower bounds

    p_j >= [2,3,4,5,6,7,8,9,66,164,317,558,938].

Conditioning on the first-defect channel fixes the mechanical zeros before the
first mismatch and forces the mismatch bit itself to be odd.  Combining these
facts with the generic lower bounds gives channel-specific upper bounds on the
formation correction epsilon_13.

The resulting integer-root caps per fixed G13 entrance X are

    p=2  -> 76
    p=5  -> 34
    p=8  -> 16
    p=10 -> 11
    p=13 ->  6
    p=16 ->  4.

Using the high-prefix factorization

    X+1 = h*2^879 + ell,
    lambda = 2^2418 / 3^1526 < 1,

one current-core root touches at most ceil(1+epsilon/lambda) high-prefix values.
After weighting by the already-certified necessary channel masses, the union
of all E=13 current-R1-compatible high prefixes is at most

    59,690,623,368,480

inside the exact E=13 high-prefix band of size

    3,096,460,089,936,865,692,636.

Hence the compatible fraction is <193/10^10 = 1.93e-8, i.e. less than
0.00000193 percent of the full E=13 high-prefix band.

No floating-point arithmetic is used for assertions.  This is a finite
set-level necessary-condition certificate, not a proof of Collatz and not yet
an emptiness proof for the complete G13-natural relation set.
"""

from fractions import Fraction
from functools import lru_cache

T = 1539
E = 13
NMAX = 5_908_625_413_101_667_397_287
U0 = Fraction(NMAX + 1, 1)

MECH_ZEROS = [2, 5, 8, 10, 13, 16, 18, 21]
CHANNELS = [2, 5, 8, 10, 13, 16]

# Exact necessary current-core masses inherited from the existing first-defect
# / depth-27 Hensel certificates.  p=16 includes the later targeted Q=10
# low-ternary exclusion.
HARD_COUNTS = {
    2: 456_566_092_589,
    5: 80_911_487_383,
    8: 14_667_776_602,
    10: 3_349_620_432,
    13: 615_721_246,
    16: 111_791_167,
}

# Exact E=13 high-prefix band size from the pre-G13 formation bridge.
H_BAND_COUNT = 3_096_460_089_936_865_692_636
LAM = Fraction(1 << 2418, 3**1526)


def ceil_fraction(q: Fraction) -> int:
    return -((-q.numerator) // q.denominator)


def floor_log2(q: Fraction) -> int:
    n, d = q.numerator, q.denominator
    k = n.bit_length() - d.bit_length()
    while Fraction(1 << k, 1) > q:
        k -= 1
    while Fraction(1 << (k + 1), 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    assert 0 <= r <= floor_log2(U)
    return (Fraction(3, 2) ** r * U + 1) / 2


@lru_cache(None)
def greedy_max_final(steps: int, evens: int):
    """Exact relaxed maximum endpoint from U0 for fixed steps/even count.

    Odd steps are moved left until the current odd-run cap is saturated.  The
    exchange O(E(U))-E(O(U))=1/4 proves this ordering maximizes the endpoint.
    Returns None if the requested count/length is impossible even in the
    relaxed run-cap model.
    """
    U = U0
    rem_steps = steps
    rem_e = evens

    for _ in range(evens):
        if rem_steps < rem_e:
            return None
        r = min(floor_log2(U), rem_steps - rem_e)
        U = odd_run_then_even(U, r)
        rem_steps -= r + 1
        rem_e -= 1

    if rem_steps < 0 or rem_steps > floor_log2(U):
        return None
    return Fraction(3, 2) ** rem_steps * U


def can_cover(U: Fraction, evens: int, needed: int) -> bool:
    """Whether the maximal-run suffix can cover at least `needed` steps."""
    total = 0
    for _ in range(evens):
        r = floor_log2(U)
        if total + r + 1 >= needed:
            return True
        total += r + 1
        U = odd_run_then_even(U, r)
    return total + floor_log2(U) >= needed


def earliest_possible_position(j: int) -> int:
    """Necessary lower bound for the zero-based position of the j-th even."""
    rem_e = E - j - 1

    # Current starts are 3 mod 4, hence their first two accelerated bits are 11.
    for p in range(j + 2, T):
        # Through position p there are p+1 steps and j+1 even events.  The
        # unrestricted fixed-count endpoint maximum is a safe upper bound for
        # histories whose j-th even occurs exactly at p.
        Umax = greedy_max_final(p + 1, j + 1)
        if Umax is None:
            continue

        remaining_steps = T - p - 1
        if can_cover(Umax, rem_e, remaining_steps):
            return p

    raise AssertionError("no possible event position")


def epsilon_for_positions(pos: list[int]) -> Fraction:
    return sum(
        Fraction(3) ** j * Fraction(2, 3) ** p
        for j, p in enumerate(pos)
    )


def channel_position_lower_vector(first_defect: int, generic_lb: list[int]) -> list[int]:
    """Coordinate-wise lower vector inside one surviving first-defect channel."""
    # Before the first mismatch the candidate equals the mechanical word.
    # The mismatch itself is mechanical 0 -> actual 1, so every earlier
    # mechanical zero is a fixed even event and the defect position is not.
    fixed = [z for z in MECH_ZEROS if z < first_defect]
    pos = list(fixed)

    next_pos = first_defect + 1
    while len(pos) < E:
        j = len(pos)
        p = max(next_pos, generic_lb[j])
        pos.append(p)
        next_pos = p + 1

    return pos


def main() -> None:
    assert LAM < 1

    generic_lb = [earliest_possible_position(j) for j in range(E)]
    assert generic_lb == [2, 3, 4, 5, 6, 7, 8, 9, 66, 164, 317, 558, 938]

    generic_eps = epsilon_for_positions(generic_lb)
    assert generic_eps < 114
    assert ceil_fraction(Fraction(1, 1) + generic_eps / LAM) == 180

    expected = {
        2: (76, 120),
        5: (34, 55),
        8: (16, 26),
        10: (11, 19),
        13: (6, 11),
        16: (4, 7),
    }

    total_high_prefix_union_cap = 0
    rows = []

    for p in CHANNELS:
        pos = channel_position_lower_vector(p, generic_lb)
        eps = epsilon_for_positions(pos)

        # A fixed X has an N-window of width at most eps.
        root_cap = ceil_fraction(eps)

        # Solving the high-prefix interval for h gives at most this many h
        # values per one fixed current-core root.
        h_cap = ceil_fraction(Fraction(1, 1) + eps / LAM)

        assert (root_cap, h_cap) == expected[p]

        contribution = HARD_COUNTS[p] * h_cap
        total_high_prefix_union_cap += contribution
        rows.append((p, pos, eps, root_cap, h_cap, HARD_COUNTS[p], contribution))

    assert total_high_prefix_union_cap == 59_690_623_368_480

    compatible_fraction_cap = Fraction(
        total_high_prefix_union_cap,
        H_BAND_COUNT,
    )
    assert compatible_fraction_cap < Fraction(193, 10_000_000_000)

    print("R1 E=13 channel-conditioned formation filter: PASS")
    print("generic even-position lower bounds:", generic_lb)
    print("generic epsilon_13 < 114; generic high-prefix cap per root = 180")
    print()
    print("p root_cap h_cap hard_count high_prefix_union_contribution")
    for p, _pos, _eps, root_cap, h_cap, hard_count, contribution in rows:
        print(p, root_cap, h_cap, hard_count, contribution)
    print()
    print("total compatible high-prefix union cap =", total_high_prefix_union_cap)
    print("full E=13 high-prefix band =", H_BAND_COUNT)
    print("compatible fraction < 193/10^10 (<1.93e-8)")
    print("compatible percent < 0.00000193%")
    print("set-level removal > 99.99999807%")


if __name__ == "__main__":
    main()
