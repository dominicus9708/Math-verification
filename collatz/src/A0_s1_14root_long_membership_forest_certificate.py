#!/usr/bin/env python3
"""Exact 14-root arithmetic forest for the remaining A0 s=1 Route-B search.

Upstream results give:

* every survivor has first-75 Hamming distance >= 8;
* first-defect shells f>=40 are now finitely closed;
* the remaining first disagreement is therefore one of 14 values below 40;
* each remaining shell has a shell-specific SAFE X upper bound;
* a parity prefix channel has the exact form

      X = r + 2^h m,
      T^h(X) = y + 3^q m.

For each remaining first-defect position f, the prefix is exactly the threshold
through positions <f followed by the forced 0->1 disagreement at f.  Hence the
entire remaining ordinary-X set is represented by 14 disjoint arithmetic
root cylinders at depth h=f+1, each with a finite integer m interval.

Refining one root by the next parity bit merely selects one parity of m,
writing m=m0+2k.  The child k intervals exactly partition the parent m
interval.  Thus future search can operate on channel intervals rather than
restarting individual Collatz orbits from X.

This file constructs the exact forest.  It does not claim that any root or
child extends through the full t0 pre bridge; correction-language membership
and C4F remain open gates.
"""

import A0_s1_prefix_channel_transducer_certificate as transducer
import A0_s1_prefix_defect_membership_pruning_certificate as pruning

TH = pruning.TH
X_TH = pruning.X_TH
X_MIN = pruning.X_MIN

REMAINING_FIRST = (
    2, 5, 8, 10, 13, 16, 18,
    21, 24, 27, 29, 32, 35, 37,
)
ELIMINATED_FIRST = (40, 43, 46, 48, 51, 54, 56, 59, 62, 65)

assert tuple(f for f in pruning.EXPECTED_FIRST if f < 40) == REMAINING_FIRST
assert tuple(f for f in pruning.EXPECTED_FIRST if f >= 40) == ELIMINATED_FIRST

shell_by_f = {
    f: (eta, xmax, before, after, flips)
    for f, eta, xmax, before, after, flips in pruning.shell_rows
}


def build_channel(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = transducer.refine_channel(state, bit)
    return state


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def parameter_interval(r: int, h: int, lo: int, hi: int):
    """m interval for lo <= r+2^h m <= hi."""
    modulus = 1 << h
    m_lo = ceil_div(lo - r, modulus)
    m_hi = (hi - r) // modulus
    return m_lo, m_hi


def child_parameter_interval(m_lo: int, m_hi: int, m0: int):
    """If m=m0+2k, return the exact integer k interval."""
    assert m0 in (0, 1)
    k_lo = ceil_div(m_lo - m0, 2)
    k_hi = (m_hi - m0) // 2
    return k_lo, k_hi


def interval_count(lo: int, hi: int) -> int:
    return max(0, hi - lo + 1)


roots = []
for f in REMAINING_FIRST:
    assert TH[f] == 0
    eta_floor, xmax, before, after, witness_flips = shell_by_f[f]

    # First mismatch is threshold prefix + forced 1 at position f.
    bits = TH[:f] + (1,)
    h, r, y, q = build_channel(bits)
    assert h == f + 1
    assert q == sum(bits)

    modulus = 1 << h
    expected_residue = (X_TH + (1 << f)) % modulus
    assert r == expected_residue

    m_lo, m_hi = parameter_interval(r, h, X_MIN, xmax)
    assert m_lo >= 0
    assert interval_count(m_lo, m_hi) == after

    # The two possible next bits choose opposite parities of m and therefore
    # partition the parent parameter interval exactly.
    child_counts = 0
    seen_m0 = set()
    for bit in (0, 1):
        m0 = (bit - (y & 1)) & 1
        seen_m0.add(m0)
        k_lo, k_hi = child_parameter_interval(m_lo, m_hi, m0)
        child_counts += interval_count(k_lo, k_hi)

        child = transducer.refine_channel((h, r, y, q), bit)
        h2, r2, y2, q2 = child
        assert h2 == h + 1

        # Endpoint affine identity for the first and last available child
        # parameters (when that child is nonempty).
        if k_lo <= k_hi:
            for kval in {k_lo, k_hi}:
                X = r2 + (1 << h2) * kval
                bits_actual, endpoint = transducer.orbit_prefix(X, h2)
                assert bits_actual == bits + (bit,)
                assert endpoint == y2 + (3 ** q2) * kval

    assert seen_m0 == {0, 1}
    assert child_counts == after

    roots.append({
        "f": f,
        "h": h,
        "r": r,
        "y": y,
        "q": q,
        "m_lo": m_lo,
        "m_hi": m_hi,
        "count": after,
        "eta75_floor": eta_floor,
        "xmax": xmax,
    })


# Distinct first-defect roots are disjoint already at the shallower of their
# two depths: the earlier root flips there, while every later root still
# agrees with the threshold.
for i, a in enumerate(roots):
    for b in roots[i + 1:]:
        assert a["f"] < b["f"]
        mod = 1 << a["h"]
        assert a["r"] != (b["r"] % mod)

retained = sum(root["count"] for root in roots)
assert retained == 125_072_439_875_999_947_649
assert pruning.retained_after - retained == 455_010_884

# Deepest remaining first disagreement is now zero-based position 37.
assert roots[-1]["f"] == 37
assert roots[-1]["h"] == 38

print("PASS A0 s=1 14-root long-membership forest certificate")
print("remaining_first_defect_positions", REMAINING_FIRST)
print("root_count", len(roots))
print("deepest_first_defect_position", 37)
print("deepest_initial_channel_depth", 38)
print("remaining_integer_parameter_count", retained)
for root in roots:
    print("root", root["f"],
          "h", root["h"],
          "r", root["r"],
          "y", root["y"],
          "q", root["q"],
          "m_lo", root["m_lo"],
          "m_hi", root["m_hi"],
          "count", root["count"])
print("child_rule", "m=m0+2k; exact interval partition")
print("status", "EXACT search forest over SAFE-pruned roots; full membership remains OPEN")
