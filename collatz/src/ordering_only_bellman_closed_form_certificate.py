#!/usr/bin/env python3
"""Exact certificate for the ordering-only Bellman relaxation.

This file proves, by exact rational regression, the closed form derived from
only the ordering recurrence.  It intentionally uses no Hensel congruence,
near-root budget, A0/J0 macro-contraction claim, or ternary selector.

For a gap word w=(g_1,...,g_n), g_i in {1,2}, put

    lambda_i = 3^i / 2^(g_1+...+g_i),
    p_i      = max(0, p - N_2(i)),

where N_2(i) counts the gap-2 letters among the first i positions.  The
ordering-only Bellman cost is

    B_w(p) = sum_i 2 lambda_i (1 - 2^(-p_i)),

with zero contribution when p_i=0.

If m_w(p) is the last active index, then

    B_w(p)
      = 2 A_m
        - 6 * 2^(-p) * ((3/2)^m - 1),

where A_m=sum_{i=1}^m lambda_i.  This follows from the exact cancellation

    lambda_i * 2^N_2(i) = (3/2)^i.

The exhaustive checks below use fractions.Fraction only.
"""

from fractions import Fraction
from itertools import product


def prefix_weights(word):
    out = []
    gap_sum = 0
    for i, gap in enumerate(word, start=1):
        assert gap in (1, 2)
        gap_sum += gap
        out.append(Fraction(3**i, 2**gap_sum))
    return out


def direct_cost(word, p):
    assert p >= 0
    weights = prefix_weights(word)
    state = p
    total = Fraction(0, 1)
    for gap, weight in zip(word, weights):
        state = max(0, state - gap + 1)
        if state:
            total += 2 * weight * (1 - Fraction(1, 2**state))
    return total


def last_active_index(word, p):
    """Return m_w(p), using 1-based positions and m=0 if inactive."""
    if p == 0:
        return 0
    two_seen = 0
    for i, gap in enumerate(word, start=1):
        if gap == 2:
            two_seen += 1
            if two_seen == p:
                return i - 1
    return len(word)


def closed_form_cost(word, p):
    assert p >= 0
    m = last_active_index(word, p)
    if m == 0:
        return Fraction(0, 1)

    weights = prefix_weights(word)
    A_m = sum(weights[:m], Fraction(0, 1))
    geometric_term = Fraction(3, 2) ** m - 1
    return 2 * A_m - 6 * Fraction(1, 2**p) * geometric_term


def terminal_state(word, p):
    return max(0, p - sum(gap == 2 for gap in word))


def composed_cost(u, v, p):
    return direct_cost(u, p) + prefix_multiplier(u) * direct_cost(v, terminal_state(u, p))


def prefix_multiplier(word):
    return Fraction(3 ** len(word), 2 ** sum(word))


def check_closed_form(max_len=12, max_p=16):
    checked = 0
    for n in range(max_len + 1):
        for word in product((1, 2), repeat=n):
            previous = None
            for p in range(max_p + 1):
                direct = direct_cost(word, p)
                closed = closed_form_cost(word, p)
                assert direct == closed, (word, p, direct, closed)

                # Monotonicity in the initial ordering displacement.
                if previous is not None:
                    assert direct >= previous, (word, p, previous, direct)
                previous = direct
                checked += 1
    return checked


def check_composition(max_total_len=8, max_p=10):
    checked = 0
    for total_len in range(max_total_len + 1):
        for word in product((1, 2), repeat=total_len):
            for cut in range(total_len + 1):
                u, v = word[:cut], word[cut:]
                for p in range(max_p + 1):
                    lhs = direct_cost(word, p)
                    rhs = composed_cost(u, v, p)
                    assert lhs == rhs, (word, cut, p, lhs, rhs)
                    checked += 1
    return checked


def check_cancellation_identity(max_len=12):
    checked = 0
    for n in range(max_len + 1):
        for word in product((1, 2), repeat=n):
            two_seen = 0
            gap_sum = 0
            for i, gap in enumerate(word, start=1):
                gap_sum += gap
                two_seen += gap == 2
                lam = Fraction(3**i, 2**gap_sum)
                assert lam * (2**two_seen) == Fraction(3, 2) ** i
                checked += 1
    return checked


def main():
    c1 = check_closed_form()
    c2 = check_composition()
    c3 = check_cancellation_identity()
    print("PASS ordering-only Bellman closed-form certificate")
    print(f"closed-form/monotonicity states: {c1}")
    print(f"composition states:            {c2}")
    print(f"cancellation identities:       {c3}")
    print("SAFE dependency: ordering relaxation -> closed form -> Hensel lower bound")
    print("NOT USED: near-root budget, A0/J0 macro contraction, Cantor-core selector")


if __name__ == "__main__":
    main()
