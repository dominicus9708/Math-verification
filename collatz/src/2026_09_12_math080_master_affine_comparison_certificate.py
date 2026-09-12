#!/usr/bin/env python3
"""MATH-080: master affine comparison defect regression.

Represent an exact affine Collatz state by X=(a,S,rho), with endpoint

    y=(a+S)/rho.

For two states define

    D(X1,X2)=rho2*(a1+S1)-rho1*(a2+S2).

Then identically

    D(X1,X2)=rho1*rho2*(y1-y2).

This single comparison contains endpoint compatibility/order and, against the
identity reference (N,0,1), the orbit-gap/descent test.

The finite regression checks all coefficient-surviving state pairs through
depth 14 plus every state's comparison with its own start reference. The
identity itself is algebraic.
"""

from fractions import Fraction

MAX_DEPTH = 14


def defect(a1, S1, rho1, a2, S2, rho2):
    return rho2 * (a1 + S1) - rho1 * (a2 + S2)


def main() -> None:
    states = [(0, 0, 0)]  # canonical r,y,q
    pair_checks = 0
    pair_failures = 0
    reference_checks = 0
    reference_failures = 0

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
        affine = []
        for r, y, q in states:
            rho = Fraction(p2, 3**q)
            S = rho * y - r
            affine.append((r, S, rho, y))

            # Compare the path endpoint with its own start r. This is the
            # canonical-state specialization of the general N-reference test.
            Dref = defect(r, S, rho, r, Fraction(0), Fraction(1))
            want = rho * (y - r)
            reference_checks += 1
            if Dref != want or Dref != S - r * (rho - 1):
                reference_failures += 1

        for i in range(len(affine)):
            a1, S1, rho1, y1 = affine[i]
            for j in range(i + 1, len(affine)):
                a2, S2, rho2, y2 = affine[j]
                got = defect(a1, S1, rho1, a2, S2, rho2)
                want = rho1 * rho2 * (y1 - y2)
                pair_checks += 1
                if got != want:
                    pair_failures += 1

    assert pair_failures == 0
    assert reference_failures == 0
    assert pair_checks == 372_731

    print("max_depth", MAX_DEPTH)
    print("pair_checks", pair_checks)
    print("pair_failures", pair_failures)
    print("reference_checks", reference_checks)
    print("reference_failures", reference_failures)
    print("PASS MATH-080 master affine comparison defect")


if __name__ == "__main__":
    main()
