#!/usr/bin/env python3
"""Exact ordered arithmetic-cylinder minimum-defect theorem for Route-B.

Let target ranked-one positions be

    a_1 < ... < a_q.

For selected candidate ranks impose exact arithmetic-cylinder constraints

    b_r in [lo_r, hi_r] intersect (beta_r + lambda_r Z),
    b_r <= a_r,

along with the ordinary strict ordering

    b_1 < ... < b_q.

Every normalized dominance-defect atom

    d_r(b) = (2^a_r - 2^b)/3^r

is strictly decreasing in b.  Therefore the global minimum defect is obtained
by the componentwise greatest feasible position vector.

That vector is constructed greedily from right to left:

    g_q = max B_q,
    g_r = max {b in B_r : b < g_(r+1)}.

If one step is empty, the complete ordered cylinder family is empty.  Otherwise
backward induction proves that every feasible vector b satisfies b_r <= g_r at
every rank.  Hence g minimizes every coordinatewise decreasing separable cost,
in particular the exact normalized defect sum.

This theorem safely accumulates multiple projective-cylinder defect floors and
automatically includes extra displacement forced by rank ordering.  It does not
require independent-gap addition and therefore avoids double counting.
"""

from fractions import Fraction
from itertools import combinations, product

MAX_H = 7
PERIODS = (2, 6)


def cylinder_max(lo: int, hi: int, beta: int, period: int):
    assert period >= 1
    if lo > hi:
        return None
    out = hi - ((hi - beta) % period)
    return out if out >= lo else None


def greedy_max(target, specs):
    q = len(target)
    assert len(specs) == q
    out = [None] * q
    right_cap = None

    for i in range(q - 1, -1, -1):
        lo, hi, beta, period = specs[i]
        upper = min(hi, target[i])
        if right_cap is not None:
            upper = min(upper, right_cap - 1)

        b = cylinder_max(lo, upper, beta, period)
        if b is None:
            return None

        out[i] = b
        right_cap = b

    return tuple(out)


def admissible(target, specs, candidate):
    if len(target) != len(candidate):
        return False
    if not all(candidate[i] < candidate[i + 1] for i in range(len(candidate) - 1)):
        return False

    for i, b in enumerate(candidate):
        lo, hi, beta, period = specs[i]
        if not (lo <= b <= min(hi, target[i])):
            return False
        if (b - beta) % period:
            return False
    return True


def eta(target, candidate):
    return sum(
        (
            Fraction((1 << target[i]) - (1 << candidate[i]), 3 ** (i + 1))
        )
        for i in range(len(target))
    )


# ---------------------------------------------------------------------------
# Exact finite regression.
# ---------------------------------------------------------------------------
# Use target positions from all combinations through h<=7 and up to q<=3.
# Each rank receives a projective-style period 2 or 6 and every residue class.
# The lower bound i is the unavoidable rank-order floor b_i>=i.

family_checks = 0
empty_checks = 0
componentwise_checks = 0
defect_checks = 0

for h in range(1, MAX_H + 1):
    for q in range(1, min(3, h) + 1):
        for target in combinations(range(h), q):
            choices = []
            for i in range(q):
                rank_choices = []
                for period in PERIODS:
                    for beta in range(period):
                        rank_choices.append((i, target[i], beta, period))
                choices.append(tuple(rank_choices))

            for specs in product(*choices):
                greedy = greedy_max(target, specs)
                feasible = [
                    candidate
                    for candidate in combinations(range(h), q)
                    if admissible(target, specs, candidate)
                ]

                assert (greedy is None) == (not feasible)
                family_checks += 1

                if greedy is None:
                    empty_checks += 1
                    continue

                assert greedy in feasible

                for candidate in feasible:
                    assert all(
                        candidate[i] <= greedy[i]
                        for i in range(q)
                    )
                    componentwise_checks += 1

                greedy_eta = eta(target, greedy)
                direct_min = min(eta(target, candidate) for candidate in feasible)
                assert greedy_eta == direct_min
                assert all(eta(target, candidate) >= greedy_eta for candidate in feasible)
                defect_checks += 1


assert family_checks == 39_648
assert empty_checks == 34_185
assert componentwise_checks > 0
assert defect_checks == family_checks - empty_checks

print("PASS A0 s=1 Route-B ordered projective-cylinder min-defect certificate")
print("max_h", MAX_H)
print("periods", PERIODS)
print("family_checks", family_checks)
print("empty_checks", empty_checks)
print("componentwise_checks", componentwise_checks)
print("defect_checks", defect_checks)
print(
    "greedy",
    "right-to-left largest legal cylinder member gives the componentwise greatest feasible ranked-one vector",
)
print(
    "exact_minimum",
    "eta_min=sum_r (2^a_r-2^g_r)/3^r for the greedy vector g",
)
print(
    "ordering_gain",
    "a cylinder restriction at a later rank can lower earlier greedy caps and thereby force additional defect automatically",
)
print(
    "dsd_audit",
    "multiple local projective constraints are accumulated through one exact ordered family minimum; independent local gap addition is not assumed",
)
print(
    "status",
    "ordered multi-cylinder defect accumulation CLOSED; deriving the actual cylinder sequence forced by each 14-root/source endpoint state remains OPEN",
)
