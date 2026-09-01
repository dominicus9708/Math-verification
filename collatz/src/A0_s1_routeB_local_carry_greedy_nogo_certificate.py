#!/usr/bin/env python3
"""Exact counterexample to a tempting but invalid local carry greedy rule.

Invalid proposed rule:

  While processing a prescribed ternary target-relative residue from right to
  left, at each gate choose the largest currently legal candidate one-position
  b satisfying the mod-3 gate and the current ordering cap.

This local rule is NOT globally defect-minimizing because the chosen b also
changes the successor carry, which changes future/earlier residue cylinders.

Counterexample:

    target positions a = (0,1,3,4,6)
    required correction difference D = 27 mod 3^4 = 81.

The dominance candidate

    b = (0,1,2,3,4)

is feasible and has

    C(a)-C(b) = 108 == 27 mod81,
    eta = 108/3^5 = 4/9.

But the local largest-b rule begins from z0=-D mod81=54 and chooses the
rightmost positions 6,4,3,0 before the final ordering constraint becomes
impossible.  Thus it reports failure even though a feasible candidate exists.

This does not affect the separate ordered-cylinder greedy theorem.  That theorem
assumes the complete arithmetic cylinder sequence is already fixed.  The
counterexample shows only that the carry-state sequence itself cannot be chosen
by myopic largest-b decisions.
"""

from fractions import Fraction

TARGET = (0, 1, 3, 4, 6)
CANDIDATE = (0, 1, 2, 3, 4)
L = 4
D = 27


def correction_positions(pos):
    q = len(pos)
    return sum(3 ** (q - i - 1) * 2 ** a for i, a in enumerate(pos))


def eta(target, candidate):
    return Fraction(
        correction_positions(target) - correction_positions(candidate),
        3 ** len(target),
    )


def local_greedy_trace(target, L, D):
    q = len(target)
    z = (-D) % (3 ** L)
    cap = None
    trace = []
    remaining = L

    for t in range(L):
        idx = q - 1 - t
        a = target[idx]
        upper = a if cap is None else min(a, cap - 1)

        rhs = (z + pow(2, a, 3)) % 3
        if rhs == 0:
            return trace, False
        parity = 0 if rhs == 1 else 1

        b = upper if upper % 2 == parity else upper - 1
        if b < idx:
            return trace, False

        modulus = 3 ** remaining
        numer = (z + pow(2, a, modulus) - pow(2, b, modulus)) % modulus
        assert numer % 3 == 0
        z_next = (numer // 3) % (3 ** (remaining - 1)) if remaining > 1 else 0

        trace.append((idx, a, z, parity, b, z_next))
        z = z_next
        cap = b
        remaining -= 1

    # Unprocessed earlier ranks still need positions below cap.  The smallest
    # possible rank-i position is i, so cap<=0 blocks the remaining rank here.
    for idx in range(q - L - 1, -1, -1):
        b = min(target[idx], cap - 1)
        if b < idx:
            return trace, False
        cap = b

    return trace, True


Ct = correction_positions(TARGET)
Cb = correction_positions(CANDIDATE)
Delta = Ct - Cb

assert all(CANDIDATE[i] <= TARGET[i] for i in range(len(TARGET)))
assert all(CANDIDATE[i] < CANDIDATE[i + 1] for i in range(len(TARGET) - 1))
assert Delta == 108
assert Delta % (3 ** L) == D
assert eta(TARGET, CANDIDATE) == Fraction(4, 9)

trace, success = local_greedy_trace(TARGET, L, D)
assert not success
assert tuple(row[4] for row in trace) == (6, 4, 3, 0)

print("PASS A0 s=1 Route-B local carry greedy no-go certificate")
print("target", TARGET)
print("candidate", CANDIDATE)
print("required_residue", D, "mod", 3 ** L)
print("exact_difference", Delta)
print("eta", eta(TARGET, CANDIDATE))
print("local_greedy_selected_right_to_left", tuple(row[4] for row in trace))
print("local_greedy_success", success)
print(
    "rejected_rule",
    "choose the largest currently legal b at each carry gate before the successor carry sequence is fixed",
)
print(
    "preserved_rule",
    "once all arithmetic cylinders are fixed, right-to-left componentwise greedy still gives the exact minimum defect",
)
print(
    "dsd_audit",
    "carry-state choice and ordered-cylinder minimization are distinct layers and must not be conflated",
)
