#!/usr/bin/env python3
"""MATH-079: address-contrast / correction-credit separation identity.

At common depth k, order two canonical states so q_H=q_L+d. Define

    A_d = r_L - 3^d r_H                 (address contrast)
    C_d = 3^d S_H - S_L                 (correction credit)

with rho_L=2^k/3^q_L and S=rho*y-r. Then universally

    rho_L (y_L-y_H) = A_d - C_d.

Thus endpoint compatibility is exactly A_d=C_d. This explains why a Hensel
carry/credit state cannot replace exact dyadic address information: the credit
and the address contrast are the two sides of the compatibility equation.

The finite regression below checks every unordered pair of coefficient-
surviving canonical states through depth 14. The identity itself is algebraic.
"""

from fractions import Fraction

MAX_DEPTH = 14


def main() -> None:
    states = [(0, 0, 0)]  # r,y,q
    checked = 0
    failures = 0
    merge_equiv_failures = 0

    for parent_depth in range(MAX_DEPTH):
        v = 1 << parent_depth
        nxt = []
        for r, y, q in states:
            u = 3**q
            for p in (0, 1):
                lift = p ^ (y & 1)
                r2 = r + lift * v
                pre = y + lift * u
                y2 = (3 * pre + 1) // 2 if p else pre // 2
                q2 = q + p
                if 3**q2 >= 2 * v:
                    nxt.append((r2, y2, q2))
        states = nxt

        k = parent_depth + 1
        p2 = 1 << k
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                lo, hi = (a, b) if a[2] <= b[2] else (b, a)
                rL, yL, qL = lo
                rH, yH, qH = hi
                d = qH - qL

                rhoL = Fraction(p2, 3**qL)
                rhoH = Fraction(p2, 3**qH)
                SL = rhoL * yL - rL
                SH = rhoH * yH - rH

                A = rL - 3**d * rH
                C = 3**d * SH - SL
                lhs = rhoL * (yL - yH)
                rhs = A - C
                checked += 1
                if lhs != rhs:
                    failures += 1
                if ((yL == yH) != (Fraction(A, 1) == C)):
                    merge_equiv_failures += 1

    assert failures == 0
    assert merge_equiv_failures == 0
    print("max_depth", MAX_DEPTH)
    print("pair_checks", checked)
    print("identity_failures", failures)
    print("merge_equivalence_failures", merge_equiv_failures)
    print("PASS MATH-079 address-credit separation identity")


if __name__ == "__main__":
    main()
