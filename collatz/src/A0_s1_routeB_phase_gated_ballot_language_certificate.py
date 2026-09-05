#!/usr/bin/env python3
"""Exact phase-gated characterization of the Route-B ballot summary.

The existing ballot summary stores

    (h, q, base_min, critical_prefix).

This certificate characterizes the important base_min=0 sector without a
history list of zero-touch prefixes.

Let

    d_W(u) = q_W(u) - floor(alpha*u),   alpha = log_3(2).

For a finite critical prefix c, the condition

    base_min = 0, critical_prefix = c

is equivalent to:

  1. d_W(u) >= 0 for every nonempty prefix u;
  2. d_W(c) = 0;
  3. whenever d_W(u) = 0, frac(alpha*u) <= frac(alpha*c).

Because alpha is irrational, equality of fractional phases occurs only for
u=c.  Equivalently,

    d_W(u) >= 1_{ frac(alpha*u) > frac(alpha*c) }

for all u, together with d_W(c)=0.

For critical_prefix=None, the equivalent condition is simply

    d_W(u) >= 1 for every nonempty prefix u.

Thus the earlier strict threshold/dominance language is the `critical=None`
special case of one phase-gated counter language.  The long Christoffel root,
whose existing certificate has base_min=0 and a finite critical prefix, belongs
to the same general framework without assuming dominance relative to the
length-18 threshold target.

Scope:
  * exact language characterization of (base_min=0, critical): CLOSED;
  * compressed evaluation of the phase gate over the gigantic hierarchy: OPEN;
  * correction-language membership / Collatz: OPEN.
"""

from fractions import Fraction
from functools import lru_cache

MAX_DEPTH = 11


def log_bounds(z: Fraction, n: int = 90):
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
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    return flo


def frac_compare(a: int, b: int) -> int:
    """Compare frac(alpha*a) and frac(alpha*b) exactly."""
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


def max_fractional(candidates):
    vals = [x for x in candidates if x is not None]
    if not vals:
        return None
    best = vals[0]
    for x in vals[1:]:
        if frac_compare(x, best) > 0:
            best = x
    return best


def ballot_summary(bits):
    q = 0
    base_min = 0
    critical = None
    for u, bit in enumerate(bits, 1):
        q += bit
        d = q - floor_alpha(u)
        if d < base_min:
            base_min = d
            critical = u
        elif d == base_min:
            critical = max_fractional((critical, u))
    return len(bits), q, base_min, critical


def phase_gate_accepts(bits, critical):
    """Recognize exactly the base_min=0, critical-prefix sector."""
    q = 0
    d_at_critical = None

    for u, bit in enumerate(bits, 1):
        q += bit
        d = q - floor_alpha(u)

        if d < 0:
            return False

        if critical is None:
            if d == 0:
                return False
            continue

        if u == critical:
            d_at_critical = d

        if d == 0 and frac_compare(u, critical) > 0:
            return False

    if critical is None:
        return True

    if not (1 <= critical <= len(bits)):
        return False
    return d_at_critical == 0


def phase_lower_bound(u: int, critical):
    """Required integer lower bound on d_W(u) in the base_min=0 sector."""
    if critical is None:
        return 1
    return 1 if frac_compare(u, critical) > 0 else 0


# ---------------------------------------------------------------------------
# 1. Exhaustive equivalence against the existing ballot summary.
# ---------------------------------------------------------------------------

summary_checks = 0
requested_critical_checks = 0

for h in range(1, MAX_DEPTH + 1):
    requested = (None,) + tuple(range(1, h + 1))

    for mask in range(1 << h):
        bits = tuple((mask >> i) & 1 for i in range(h))
        _, _, base_min, actual_critical = ballot_summary(bits)

        for c in requested:
            direct = base_min == 0 and actual_critical == c
            gated = phase_gate_accepts(bits, c)
            assert direct == gated
            requested_critical_checks += 1

        if base_min == 0:
            assert phase_gate_accepts(bits, actual_critical)
            summary_checks += 1

            # Local lower-bound form.
            q = 0
            for u, bit in enumerate(bits, 1):
                q += bit
                d = q - floor_alpha(u)
                assert d >= phase_lower_bound(u, actual_critical)
            if actual_critical is not None:
                q_c = sum(bits[:actual_critical])
                assert q_c - floor_alpha(actual_critical) == 0


# ---------------------------------------------------------------------------
# 2. Strict threshold language is exactly critical=None.
# ---------------------------------------------------------------------------


def requirement(n: int) -> int:
    return 0 if n == 0 else floor_alpha(n) + 1


def threshold_word(n: int):
    return tuple(requirement(i + 1) - requirement(i) for i in range(n))


strict_checks = 0
for h in range(1, MAX_DEPTH + 1):
    target = threshold_word(h)
    target_prefix = 0

    for mask in range(1 << h):
        bits = tuple((mask >> i) & 1 for i in range(h))
        _, q, base_min, critical = ballot_summary(bits)

        if q != sum(target):
            continue

        # critical=None iff every candidate prefix has at least the threshold
        # requirement.  At equal final one-count this is the prefix-dominance
        # language used by the previous target-family certificates.
        candidate_prefix = 0
        target_prefix = 0
        dominates = True
        for cb, tb in zip(bits, target):
            candidate_prefix += cb
            target_prefix += tb
            if candidate_prefix < target_prefix:
                dominates = False
                break

        expected = base_min == 0 and critical is None
        assert expected == dominates
        strict_checks += 1


print("PASS A0 s=1 Route-B phase-gated ballot language certificate")
print("max_depth", MAX_DEPTH)
print("base_min_zero_summary_checks", summary_checks)
print("requested_critical_equivalence_checks", requested_critical_checks)
print("strict_threshold_dominance_checks", strict_checks)
print(
    "finite_critical_rule",
    "d(u)>=0, d(c)=0, and zero-touch prefixes may only have fractional phase <= phase(c)",
)
print(
    "local_gate",
    "d(u) >= 1_{frac(alpha*u)>frac(alpha*c)} with anchor d(c)=0",
)
print(
    "none_rule",
    "critical=None iff d(u)>=1 for every nonempty prefix",
)
print(
    "dsd_audit",
    "the strict dominance model is identified as a special case rather than being assumed for finite-critical Christoffel states",
)
print(
    "status",
    "base_min=0 ballot language characterization CLOSED; hierarchical phase-gate compression remains OPEN",
)
