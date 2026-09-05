#!/usr/bin/env python3
"""Exact phase-covariant ballot summary for A0 s=1 Route-B.

Let alpha=log_3(2), F(n)=floor(alpha*n), and for a binary block B define

    Q_B(u) = number of ones in the first u positions,
    d_B(u) = Q_B(u)-F(u),
    m(B)   = min_{0<=u<=|B|} d_B(u).

Among prefixes attaining m(B), let a(B) be one whose fractional part
{alpha*a} is maximal.  If no positive prefix is needed to represent the
minimum, a(B)=None.

At absolute start phase h, the exact shifted ballot margin is

    mu_h(B)
      = min_u [Q_B(u) - (F(h+u)-F(h))].

Since

    F(h+u)-F(h)-F(u) in {0,1},

write kappa(h,u) for this carry.  Every non-minimizing prefix has
 d_B(u)>=m(B)+1, so it cannot produce a shifted value below m(B).  A shifted
value m(B)-1 occurs iff some minimizing prefix has kappa=1.  The carry is
monotone in the fractional part {alpha*u}; hence it is enough to test the
single maximal-fractional minimizer a(B).  Therefore

    mu_h(B) = m(B) - kappa(h,a(B)),

with kappa=0 when a(B)=None.

CONSEQUENCE.
The intrinsic summary

    (length, ones, base_min, critical_prefix)

is sufficient to recover exact pure-ballot legality at *every* absolute phase
h.  The phase h is an external placement argument; it does not need to be
stored on every reused Christoffel/Stern-Brocot DAG node.  Hence a gigantic
block may retain one intrinsic summary, be composed/run-powered recursively,
and be evaluated at a placement by one exact phase-carry test.

This closes the phase-sensitive PURE-BALLOT part of the compressed decoder.
It does not close correction-language membership, formation semantics, or the
full deterministic long-orbit Route-B predicate.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

NLOG = 90
PHASE_MAX = 63
BLOCK_MAX = 10
COMPOSITION_MAX = 9


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


@lru_cache(None)
def floor_alpha(n: int) -> int:
    assert n >= 0
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi, ("increase NLOG", n, flo, fhi)
    return flo


def phase_carry(h: int, u: int) -> int:
    c = floor_alpha(h + u) - floor_alpha(h) - floor_alpha(u)
    assert c in (0, 1)
    return c


def frac_compare(a: int, b: int) -> int:
    """Compare {alpha*a} and {alpha*b} exactly."""
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


@dataclass(frozen=True)
class BallotSummary:
    length: int
    ones: int
    base_min: int
    critical_prefix: int | None


def direct_summary(bits) -> BallotSummary:
    q = 0
    m = 0
    critical = None
    for u, bit in enumerate(bits, 1):
        assert bit in (0, 1)
        q += bit
        d = q - floor_alpha(u)
        if d < m:
            m = d
            critical = u
        elif d == m:
            if critical is None or frac_compare(u, critical) > 0:
                critical = u
    return BallotSummary(len(bits), q, m, critical)


def max_fractional(candidates):
    vals = [x for x in candidates if x is not None]
    if not vals:
        return None
    best = vals[0]
    for x in vals[1:]:
        if frac_compare(x, best) > 0:
            best = x
    return best


def compose(a: BallotSummary, b: BallotSummary) -> BallotSummary:
    if a.length == 0:
        return b
    if b.length == 0:
        return a

    endpoint_a = a.ones - floor_alpha(a.length)
    right_min = endpoint_a + b.base_min - (
        phase_carry(a.length, b.critical_prefix)
        if b.critical_prefix is not None
        else 0
    )
    parent_min = min(a.base_min, right_min)

    left_candidate = a.critical_prefix if a.base_min == parent_min else None
    right_candidate = None
    if right_min == parent_min:
        right_candidate = a.length + (
            b.critical_prefix if b.critical_prefix is not None else 0
        )

    return BallotSummary(
        a.length + b.length,
        a.ones + b.ones,
        parent_min,
        max_fractional((left_candidate, right_candidate)),
    )


def direct_phase_margin(h: int, bits) -> int:
    q = 0
    out = 0
    fh = floor_alpha(h)
    for u, bit in enumerate(bits, 1):
        q += bit
        required = floor_alpha(h + u) - fh
        out = min(out, q - required)
    return out


def phase_margin_from_summary(h: int, s: BallotSummary) -> int:
    if s.critical_prefix is None:
        return s.base_min
    return s.base_min - phase_carry(h, s.critical_prefix)


def legal_direct(h: int, entering_slack: int, bits) -> bool:
    return entering_slack + direct_phase_margin(h, bits) >= 0


def legal_from_summary(h: int, entering_slack: int, s: BallotSummary) -> bool:
    return entering_slack + phase_margin_from_summary(h, s) >= 0


# ---------------------------------------------------------------------------
# 1. Intrinsic summary remains exactly compositional.
# ---------------------------------------------------------------------------
composition_checks = 0
for n in range(COMPOSITION_MAX + 1):
    for mask in range(1 << n):
        bits = tuple((mask >> i) & 1 for i in range(n))
        direct = direct_summary(bits)
        for cut in range(n + 1):
            left = direct_summary(bits[:cut])
            right = direct_summary(bits[cut:])
            assert compose(left, right) == direct
            composition_checks += 1

assert composition_checks == 9_217


# ---------------------------------------------------------------------------
# 2. New theorem regression: one critical prefix recovers every phase margin.
# ---------------------------------------------------------------------------
phase_checks = 0
legality_checks = 0
for n in range(BLOCK_MAX + 1):
    for mask in range(1 << n):
        bits = tuple((mask >> i) & 1 for i in range(n))
        s = direct_summary(bits)
        for h in range(PHASE_MAX + 1):
            direct = direct_phase_margin(h, bits)
            recovered = phase_margin_from_summary(h, s)
            assert recovered == direct
            phase_checks += 1

            for slack in range(3):
                assert legal_from_summary(h, slack, s) == legal_direct(h, slack, bits)
                legality_checks += 1

assert phase_checks == 131_008
assert legality_checks == 393_024


# A concrete placement witness: the same local block may change margin with h,
# but the intrinsic summary itself is unchanged and the external carry explains
# the difference exactly.
block = (0,)
s = direct_summary(block)
witness = None
for h1 in range(PHASE_MAX + 1):
    for h2 in range(h1 + 1, PHASE_MAX + 1):
        m1 = phase_margin_from_summary(h1, s)
        m2 = phase_margin_from_summary(h2, s)
        if m1 != m2:
            witness = (h1, m1, h2, m2)
            break
    if witness is not None:
        break
assert witness is not None

print("PASS A0 s=1 Route-B phase-covariant ballot summary certificate")
print("state", "(length,ones,base_min,critical_prefix)")
print("formula", "mu_h=base_min-phase_carry(h,critical_prefix)")
print("composition_checks", composition_checks)
print("phase_checks", phase_checks)
print("legality_checks", legality_checks)
print("placement_witness", witness)
print(
    "compression_consequence",
    "absolute phase is an external placement argument; it need not be copied into every reused DAG node",
)
print(
    "dsd_audit",
    "phase-sensitive pure-ballot semantics is exactly reconstructed from one intrinsic block state plus the defined external phase",
)
print(
    "status",
    "compressed phase-sensitive PURE-BALLOT decoder CLOSED; full deterministic Route-B semantic renewal remains OPEN",
)
