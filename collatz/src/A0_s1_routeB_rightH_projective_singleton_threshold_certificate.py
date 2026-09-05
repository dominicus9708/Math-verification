#!/usr/bin/env python3
"""Exact right-H projective singleton-threshold certificate for A0 s=1 Route-B.

Let a binary block have length h and q ranked one-positions.  Index its ones
from the right by

    A_t = position of the (q-t)-th one from the left,

and define the standard target capacity

    D_t = A_t - (q-t-1).

There are t later one-events after A_t, so necessarily

    A_t <= h-t-1.

Therefore, universally,

    0 <= D_t <= h-q.

Any legal candidate slack satisfies

    0 <= s_t <= D_t,

so every prescribed projective slack cylinder is the intersection of an
interval of width at most h-q with one residue class modulo

    lambda_m = 2*3^(m-1).

If lambda_m > h-q, that intersection contains at most one integer.

For the current critical-cut right H block,

    h_R = 630,138,897
    q_R = 397,573,380
    h_R-q_R = 232,565,517.

Now

    lambda_17 = 86,093,442  <= h_R-q_R,
    lambda_18 = 258,280,326 >  h_R-q_R.

Hence m>=18 is a universal empty-or-singleton threshold for every prescribed
projective slack/exponent cylinder in the current right-H block.

This sharpens the older generic m>=23 threshold, which used a much larger legal
position interval.  It does NOT imply uniqueness of the complete carry path:
different outgoing carry/cylinder states may still exist.  It only says that
once one cylinder is prescribed, its legal slack choice is empty or singleton
through the high-precision range.

The finite regression below is only an implementation guard for the universal
capacity inequality and residue-spacing statement.
"""

from itertools import product

H_RIGHT = 630_138_897
Q_RIGHT = 397_573_380
CAP_MAX = H_RIGHT - Q_RIGHT


def period(m: int) -> int:
    assert m >= 1
    return 2 * (3 ** (m - 1))


def cylinder_members(U: int, beta: int, lam: int):
    assert U >= 0 and lam >= 1
    beta %= lam
    if beta > U:
        return ()
    return tuple(range(beta, U + 1, lam))


# Current exact threshold arithmetic.
assert CAP_MAX == 232_565_517
assert period(17) == 86_093_442
assert period(18) == 258_280_326
assert period(17) <= CAP_MAX < period(18)

for m in range(18, 60):
    assert period(m) > CAP_MAX

# Exhaustive small-word regression for D_t <= h-q.
capacity_checks = 0
for h in range(1, 9):
    for bits in product((0, 1), repeat=h):
        positions = tuple(i for i, bit in enumerate(bits) if bit)
        q = len(positions)
        if q == 0:
            continue
        for t in range(q):
            A_t = positions[q - t - 1]
            D_t = A_t - (q - t - 1)
            assert 0 <= D_t <= h - q
            capacity_checks += 1

assert capacity_checks == 1_793

# Generic interval-spacing regression: if lambda>U, every residue class has
# at most one representative in [0,U].
singleton_checks = 0
for U in range(0, 80):
    for lam in range(U + 1, U + 9):
        for beta in range(lam):
            assert len(cylinder_members(U, beta, lam)) <= 1
            singleton_checks += 1

assert singleton_checks > 0

HIGH_PRECISION_GATE_COUNTS = {
    24: 24 - 18 + 1,
    28: 28 - 18 + 1,
    47: 47 - 18 + 1,
}
assert HIGH_PRECISION_GATE_COUNTS == {24: 7, 28: 11, 47: 30}

print("PASS A0 s=1 Route-B right-H projective singleton-threshold certificate")
print("right_length", H_RIGHT)
print("right_one_count", Q_RIGHT)
print("max_slack_capacity", CAP_MAX)
print("lambda_17", period(17))
print("lambda_18", period(18))
print("singleton_threshold_precision", 18)
print("high_precision_gate_counts", HIGH_PRECISION_GATE_COUNTS)
print("capacity_checks", capacity_checks)
print("singleton_checks", singleton_checks)
print(
    "exact",
    "for every right-H rank, D_t<=h_R-q_R; therefore every prescribed projective slack cylinder is empty or singleton for m>=18",
)
print(
    "sharpening",
    "current right-H block improves the older generic m>=23 singleton threshold to m>=18",
)
print(
    "dsd_audit",
    "singleton cylinder does not mean singleton carry path; distinct prescribed carry/cylinder states are not merged by this theorem",
)
print(
    "status",
    "right-H prescribed-cylinder high-precision branching CLOSED through m>=18; compressed family of distinct carry states remains OPEN",
)
