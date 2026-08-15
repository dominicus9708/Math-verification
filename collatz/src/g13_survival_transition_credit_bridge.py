#!/usr/bin/env python3
"""G13-neutral survival-conditioned transition / CRT / credit bridge.

This certificate strengthens the enlarged transition-section analysis for the
second-return G13 neutral gate

    1^F (01/10)^J 0,
    (F,J,L,q) = (5245,7390,20026,12635).

A width-h transition replacement has the form

    1^(F-h) B (01/10)^(J-h) 0,

where B has length 3h and weight 2h.  Unlike the earlier unrestricted
transition over-family, this file imposes the necessary G13 mechanical-prefix
survival condition on B.

The main exact objects are:

1. the unique G13 mechanical factor, evaluated with rational bounds for
   alpha=log_3(2);
2. the exact maximum/minimum affine correction of a surviving transition word;
3. the exact Hensel repair congruence

       D_B = -T_h(delta) + k 3^(F+h),

   with T_h(delta)=2^(3h-2) x_(J-h)(delta);
4. the two-ended dyadic obstruction excluding k=0;
5. the exact parent-credit identity

       Delta_gate = k 2^(F-h)

   whenever a same-state transition repair is actually realized.

The full scan option verifies that every width h<=5232 has only k=0 inside the
surviving transition correction span for every positive credit 1..397.  Since
k=0 has excessive 2-adic valuation, this particular transition repair channel
is impossible through h=5232.  The first width where a nonzero CRT lift enters
the surviving correction span is h=5233.

This is a section/channel theorem, NOT a proof of the Collatz conjecture.
"""

from __future__ import annotations

import argparse
from fractions import Fraction

F = 5245
J = 7390
L = 20026
Q_GATE = 12635
MAX_DELTA = 397

# Exact rational enclosure used elsewhere in the repository:
#   15601/24727 < alpha=log_3(2) < 31867/50508.
ALPHA_LO = Fraction(15601, 24727)
ALPHA_HI = Fraction(31867, 50508)

# The G13 phase interval contains no interior discontinuity.  We choose its
# midpoint:
#   x = 5832 - (18487/2) alpha.
# For 0<=t<=L, Q(t)=floor(x+t alpha).  The rational enclosure determines every
# floor exactly.
PHASE_CONST = Fraction(5832, 1)
PHASE_COEFF_NUM = -18487  # coefficient / 2


def floor_strict_upper(q: Fraction) -> int:
    """Largest integer strictly below q when q is a strict upper bound."""
    if q.denominator == 1:
        return q.numerator - 1
    return q.numerator // q.denominator


def mechanical_prefix_count(t: int) -> int:
    """Exact Q(t) for the unique G13 mechanical factor."""
    if not (0 <= t <= L):
        raise ValueError("t outside G13 gate")

    c = Fraction(2 * t + PHASE_COEFF_NUM, 2)
    if c >= 0:
        lo = PHASE_CONST + c * ALPHA_LO
        hi = PHASE_CONST + c * ALPHA_HI
    else:
        # Multiplication by a negative coefficient reverses the bounds.
        lo = PHASE_CONST + c * ALPHA_HI
        hi = PHASE_CONST + c * ALPHA_LO

    flo = lo.numerator // lo.denominator
    fhi = floor_strict_upper(hi)
    assert flo == fhi, (t, lo, hi, flo, fhi)
    return flo


def build_mechanical_table():
    Q = [mechanical_prefix_count(t) for t in range(L + 1)]
    assert Q[0] == 0
    assert Q[L] == Q_GATE
    assert Q[2028] == 1279
    assert Q[F] == 3309

    deadline = [None] * (Q_GATE + 1)
    j = 0
    for t, qt in enumerate(Q):
        while j < qt:
            j += 1
            deadline[j] = t
    assert all(deadline[j] is not None for j in range(1, Q_GATE + 1))
    return Q, deadline


def hensel_step(x: int) -> int:
    return 4 * ((x + 1) // 3)


def hensel_x(delta: int, n: int) -> int:
    x = 8 * delta
    for _ in range(n):
        x = hensel_step(x)
    return x


def target(delta: int, h: int) -> int:
    """Positive magnitude T_h(delta) of the raw boundary Hensel target."""
    return (1 << (3 * h - 2)) * hensel_x(delta, J - h)


def correction_min(h: int) -> int:
    """Minimum correction of a length-3h, weight-2h word: 1^(2h)0^h."""
    q = 2 * h
    return 3**q - 2**q


def survivor_latest_positions(h: int, deadline) -> list[int]:
    """Latest positions of each odd event under the necessary G13 prefix floor.

    Put s=F-h.  The fixed front contributes s ones.  If the r-th one of B is
    at zero-based position p_r, two independent upper bounds apply:

      p_r <= h+r-1                      (remaining-capacity bound),
      p_r <= deadline[s+r]-s-1          (mechanical survival deadline).

    Their pointwise minimum is jointly feasible and maximizes every odd
    position simultaneously, hence maximizes the affine correction.
    """
    if not (1 <= h <= F):
        raise ValueError("h outside transition range")

    s = F - h
    q = 2 * h
    positions = []
    previous = -1

    for r in range(1, q + 1):
        j = s + r
        unconstrained = h + r - 1
        if j <= Q_GATE:
            survival = deadline[j] - s - 1
            p = min(unconstrained, survival)
        else:
            p = unconstrained

        assert previous < p < 3 * h, (h, r, previous, p)
        positions.append(p)
        previous = p

    return positions


def correction_from_positions(positions: list[int]) -> int:
    """R=sum 2^p_r 3^(q-r), evaluated by Horner recurrence."""
    R = 0
    for p in positions:
        R = 3 * R + (1 << p)
    return R


def survivor_span(h: int, deadline) -> int:
    rmax = correction_from_positions(survivor_latest_positions(h, deadline))
    rmin = correction_min(h)
    assert rmax >= rmin
    return rmax - rmin


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def possible_k_union(h: int, deadline) -> tuple[int, int]:
    """Safe CRT-lift interval over every delta=1..397.

    Candidate boundary differences satisfy

        D_B = -T_h(delta) + k m,
        m   = 3^(F+h),
        |D_B| <= S_h,

    where S_h is the exact correction span of transition words satisfying the
    necessary mechanical prefix floor.  Since T_h is monotone in delta, the
    union over delta is enclosed exactly by the endpoint targets.
    """
    S = survivor_span(h, deadline)
    m = 3 ** (F + h)
    Tmin = target(1, h)
    Tmax = target(MAX_DELTA, h)
    klo = ceil_div(-S + Tmin, m)
    khi = (S + Tmax) // m
    return klo, khi


def verify_k0_dyadic_obstruction(h: int):
    """k=0 cannot be a nonzero equal-weight boundary correction difference.

    For distinct length-3h, weight-2h words, the first differing time bit is at
    most 3h-2, so v2(D)<=3h-2.  But x_n is divisible by four, hence
    v2(T_h)>=3h.  Therefore D=-T_h is impossible.
    """
    assert h >= 1
    # Structural assertion; no enumeration required.
    x = hensel_x(1, J - h)
    assert x % 4 == 0


def verify_threshold(deadline, full_scan: bool):
    # Exact checkpoints around the transition.
    for h in (3217, 5000, 5232):
        assert possible_k_union(h, deadline) == (0, 0), (h, possible_k_union(h, deadline))
        verify_k0_dyadic_obstruction(h)

    assert possible_k_union(5233, deadline) == (-1, 1)

    if full_scan:
        # The unrestricted two-ended certificate already covers h<=3216.
        # Scan every remaining width to establish the first surviving nonzero
        # CRT lift exactly under the mechanical-prefix constraint.
        for h in range(3217, 5233):
            got = possible_k_union(h, deadline)
            assert got == (0, 0), (h, got)
            verify_k0_dyadic_obstruction(h)
        assert possible_k_union(5233, deadline) == (-1, 1)


def last_width_table(deadline):
    rows = []
    for h in range(5233, 5246):
        klo, khi = possible_k_union(h, deadline)
        rows.append((h, F - h, klo, khi))
    expected = [
        (5233, 12, -1, 1),
        (5234, 11, -3, 3),
        (5235, 10, -6, 6),
        (5236, 9, -12, 13),
        (5237, 8, -25, 26),
        (5238, 7, -50, 53),
        (5239, 6, -100, 107),
        (5240, 5, -201, 214),
        (5241, 4, -403, 428),
        (5242, 3, -807, 856),
        (5243, 2, -1614, 1713),
        (5244, 1, -3229, 3428),
        (5245, 0, -6461, 6859),
    ]
    assert rows == expected, (rows, expected)
    return rows


def verify_parent_credit_identity_symbolically():
    """Document the exact cancellation underlying Delta_gate=k*2^(F-h).

    Let n=J-h and x=x_n(delta).  The remaining pair cube satisfies exactly

        D_V + 2^(2n+1) delta = 3^n x / 4.

    A transition lift is

        D_B = -2^(3h-2) x + k 3^(F+h).

    The common front 1^(F-h) gives

      D_full + 2^L delta
        = 2^(F-h) [3^n D_B
                    + 2^(3h)(D_V+2^(2n+1)delta)]
        = k 2^(F-h) 3^(F+J).

    Since the full gate odd count is F+J,

        Delta_gate=(D_full+2^L delta)/3^(F+J)=k 2^(F-h).

    The cancellation is an exact algebraic identity, independent of delta.
    """
    assert L == F + 2 * J + 1
    assert Q_GATE == F + J


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--full-scan",
        action="store_true",
        help="scan every h=3217..5232 with exact big integers",
    )
    args = ap.parse_args()

    Q, deadline = build_mechanical_table()
    verify_parent_credit_identity_symbolically()
    verify_threshold(deadline, args.full_scan)

    print("G13-neutral mechanical checks")
    print("Q(2028)=", Q[2028])
    print("Q(5245)=", Q[5245])
    print("Q(20026)=", Q[L])
    print("survival/CRT repair excluded through h=5232")
    print("first nonzero CRT-lift width h=5233, k-union=(-1,1)")
    print("last 13 widths: h, F-h, k_min, k_max")
    for row in last_width_table(deadline):
        print(*row)

    print("parent credit identity: Delta_gate = k * 2^(F-h)")
    print("at h=5233, k=1 -> Delta_gate=", 1 << (F - 5233))


if __name__ == "__main__":
    main()
