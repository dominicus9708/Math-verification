#!/usr/bin/env python3
"""CRT-lift / two-ended transition certificate for gate boundary sections.

This extends the scalar transition-band magnitude analysis by coupling the
3-adic lift index to the dyadic earliest-difference coordinate.

For a length-N=3h binary transition block with weight q=2h, let R(w) be the
affine correction.  For two distinct equal-weight words u,v, if p is their
first differing time position then

    v2(R(u)-R(v)) = p <= N-2.

The balanced-Hensel repair target has

    T_h(delta) = 2^(3h-2) x_(J-h)(delta)
               = 2^N y_(J-h)(delta),

because x_n is divisible by 4.  Hence v2(T_h)>=N.

If every allowed correction difference lies in one unique ternary congruence
representative, exact equality with T_h is impossible by the v2 mismatch.
After ternary wrap, every candidate is

    D = -T_h(delta) + k 3^(F+h),

and, while |k|<2^N,

    v2(D) = v2(k).

Thus the CRT lift index k is exactly the earliest differing dyadic position.
The low N dyadic bits are independent of delta:

    D == k 3^(F+h) (mod 2^N).

This file also contains an exact interval branch-and-bound certificate for the
G13-neutral transition section.  It over-approximates all delta=1..397 by the
entire integer interval between their universal Hensel quotients y=x/4.  Empty
interval state space therefore excludes all bounded credits at once.
"""

from dataclasses import dataclass

MAX_DELTA = 397

CASES = (
    ("G81-neutral", 404, 567, 248),
    ("G81-one-slack", 402, 568, 247),
    ("G82-neutral", 409, 574, 251),
    ("G82-one-slack", 407, 575, 250),
    ("G13-neutral", 5245, 7390, 3216),
    ("G13-one-slack", 5243, 7391, 3215),
    ("G14-neutral", 5648, 7958, 3464),
    ("G14-one-slack", 5646, 7959, 3462),
)


def hensel_step(x: int) -> int:
    return 4 * ((x + 1) // 3)


def hensel_x(delta: int, n: int) -> int:
    x = 8 * delta
    for _ in range(n):
        x = hensel_step(x)
    return x


def boundary_capacity(h: int) -> int:
    return (2**h - 1) * (9**h - 4**h)


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def v2(x: int) -> int:
    x = abs(x)
    n = 0
    while x and x % 2 == 0:
        x //= 2
        n += 1
    return n


def v3(x: int) -> int:
    x = abs(x)
    n = 0
    while x and x % 3 == 0:
        x //= 3
        n += 1
    return n


def target(F: int, J: int, h: int, delta: int) -> int:
    x = hensel_x(delta, J - h)
    return (1 << (3 * h - 2)) * x


def first_nonunique_representative(F: int, J: int) -> int:
    """First h where the full bounded-credit interval can reach another CRT lift.

    If M_h + max_delta T_h(delta) < 3^(F+h), then every D in [-M_h,M_h]
    congruent to the raw target must use k=0, and the v2 mismatch excludes it.
    """
    for h in range(1, min(F, J) + 1):
        M = boundary_capacity(h)
        Tmax = target(F, J, h, MAX_DELTA)
        modulus = 3 ** (F + h)
        if M + Tmax >= modulus:
            return h
    raise AssertionError("no nonunique width in search range")


def possible_k_union(F: int, J: int, h: int):
    """Safe union of lift indices over delta=1..MAX_DELTA using monotone T."""
    M = boundary_capacity(h)
    m = 3 ** (F + h)
    Tmin = target(F, J, h, 1)
    Tmax = target(F, J, h, MAX_DELTA)
    # D=-T+k m and |D|<=M.  Over all T in [Tmin,Tmax]:
    klo = ceil_div(-M + Tmin, m)
    khi = (M + Tmax) // m
    return klo, khi


class IntervalDifferenceSolver:
    """Exact correction-difference recursion with a continuous y over-interval.

    For N,q fixed, corrections satisfy

        R(0w)=2 R(w),
        R(1w)=3^(q-1)+2 R(w).

    The exact extremal correction values are

        R_min(N,q)=3^q-2^q,
        R_max(N,q)=2^(N-q)(3^q-2^q).

    We solve D=A-2^N y while y ranges over an integer interval.  This interval
    contains all bounded credits and generally many extra y values; therefore
    an empty result is a rigorous exclusion for the original discrete credits.
    """

    def __init__(self, N: int, q: int):
        self.N = N
        self.q = q
        self.A = [0] * (q + 1)
        self.P3 = [1] * (q + 1)
        p2 = p3 = 1
        for i in range(1, q + 1):
            p3 *= 3
            p2 *= 2
            self.P3[i] = p3
            self.A[i] = p3 - p2

    def solve(self, A0: int, ylo: int, yhi: int, cap: int = 100000):
        states = {(self.q, self.q, A0, ylo, yhi)}
        max_frontier = 1

        for s in range(self.N):
            Ncur = self.N - s
            nxt = set()

            for a, b, Acur, yl, yh in states:
                # The variable term is divisible by 2 while Ncur>=1, so parity
                # is controlled solely by Acur.
                bit_pairs = ((1, 0), (0, 1)) if Acur & 1 else ((0, 0), (1, 1))

                for e, f in bit_pairs:
                    if e > a or f > b:
                        continue
                    an, bn = a - e, b - f
                    if an > Ncur - 1 or bn > Ncur - 1:
                        continue

                    contribution = (self.P3[a - 1] if e else 0) - (self.P3[b - 1] if f else 0)
                    z = Acur - contribution
                    if z & 1:
                        continue
                    An = z // 2
                    Nn = Ncur - 1

                    amin = self.A[an]
                    amax = amin << (Nn - an)
                    bmin = self.A[bn]
                    bmax = bmin << (Nn - bn)
                    dlo, dhi = amin - bmax, amax - bmin

                    if Nn:
                        scale = 1 << Nn
                        nyl = max(yl, ceil_div(An - dhi, scale))
                        nyh = min(yh, (An - dlo) // scale)
                    else:
                        nyl = max(yl, An - dhi)
                        nyh = min(yh, An - dlo)

                    if nyl <= nyh:
                        nxt.add((an, bn, An, nyl, nyh))

            states = nxt
            max_frontier = max(max_frontier, len(states))
            if not states:
                return False, max_frontier, s + 1
            if len(states) > cap:
                return None, max_frontier, s + 1

        exists = any(a == 0 and b == 0 and yl <= Acur <= yh
                     for a, b, Acur, yl, yh in states)
        return exists, max_frontier, self.N


def g13_neutral_interval_audit():
    F, J = 5245, 7390

    # First ternary wrap: k=+-1 only.  Exclude the entire bounded-credit y interval.
    h = 3216
    N, q = 3 * h, 2 * h
    ylo = hensel_x(1, J - h) // 4
    yhi = hensel_x(MAX_DELTA, J - h) // 4
    m = 3 ** (F + h)
    solver = IntervalDifferenceSolver(N, q)
    for k in (-1, 1):
        result = solver.solve(k * m, ylo, yhi, cap=10000)
        assert result[0] is False, ("G13-neutral", h, k, result)
        assert result[1] == 1
        assert result[2] == 3216

    # Next width: k=+-1,...,+-6 are allowed by scalar range.  The near-extreme
    # lifts +-5,+-6 are still excluded uniformly for the entire bounded-credit interval.
    h = 3217
    N, q = 3 * h, 2 * h
    ylo = hensel_x(1, J - h) // 4
    yhi = hensel_x(MAX_DELTA, J - h) // 4
    m = 3 ** (F + h)
    solver = IntervalDifferenceSolver(N, q)
    expected_steps = {5: 3218, 6: 3217}
    for kabs in (5, 6):
        for k in (-kabs, kabs):
            result = solver.solve(k * m, ylo, yhi, cap=10000)
            assert result[0] is False, ("G13-neutral", h, k, result)
            assert result[1] == 1
            assert result[2] == expected_steps[kabs]

    return {
        "h3216_excluded_k": [-1, 1],
        "h3217_excluded_k": [-6, -5, 5, 6],
        "h3217_unresolved_k": [-4, -3, -2, -1, 1, 2, 3, 4],
    }


def main():
    print("unique-representative / v2 exclusion")
    for name, F, J, expected_first_nonunique in CASES:
        got = first_nonunique_representative(F, J)
        assert got == expected_first_nonunique, (name, got, expected_first_nonunique)
        print(name,
              "excluded_through_h", got - 1,
              "first_nonunique_h", got,
              "k_union_at_first", possible_k_union(F, J, got))

    print("G13-neutral exact interval branch-and-bound")
    print(g13_neutral_interval_audit())


if __name__ == "__main__":
    main()
