#!/usr/bin/env python3
"""Exact phase-critical ballot compression for A0 s=1 Route-B.

Let alpha = log_3(2), F(n)=floor(n*alpha), and for a finite parity block B
let Q_B(u) be the number of odd symbols in its first u positions.  Define

    d_B(u) = Q_B(u) - F(u),
    m_B    = min_{0<=u<=|B|} d_B(u).

For h>=1 the exact threshold requirement satisfies

    REQ(h+u)-REQ(h) = F(h+u)-F(h),

so the phase-sensitive ballot margin is

    mu_h(B) = min_u [d_B(u) - carry(h,u)],

where

    carry(h,u) = F(h+u)-F(h)-F(u) in {0,1}.

Only a prefix with d_B(u)=m_B can lower the minimum to m_B-1.  Among the
positive prefixes attaining m_B, let a_B be the one with largest fractional
part {u*alpha}.  Since carry(h,u)=1 iff {h*alpha}+{u*alpha}>=1,

    mu_h(B) = m_B - carry(h,a_B)      (h>=1),

with the carry term omitted if no positive minimizer exists.  At h=0,
REQ(0)=0 and REQ(u)=F(u)+1 for u>0, hence

    mu_0(B) = m_B-1 if a_B exists, else 0.

Thus the entire placement response of a block is represented by the finite
parametric summary

    S(B) = (length, ones, m_B, a_B),

without storing an absolute phase h in every reused DAG occurrence.

The summary is compositionally closed.  For B=UV, let

    e_U = q(U)-F(|U|).

The minimum over prefixes entering V is

    r = e_U + m_V - carry(|U|,a_V),

again omitting the carry when a_V is absent.  Therefore

    m_{UV} = min(m_U,r).

The critical prefix of UV is the maximum-fraction candidate among the left
critical prefix (when the left side attains the parent minimum) and the
shifted right critical prefix |U|+a_V.  If V has no positive base minimizer,
its right critical candidate is the boundary |U| itself.

All comparisons involving alpha are certified with rational log intervals;
no floating-point value participates in an assertion.

Formation-Axiom lens:
  parent ballot state is formed only from child states plus the explicit
  concatenation boundary |U|.

Axis-property lens:
  absolute threshold location is an external evaluation coordinate, not an
  intrinsic DAG-node axis.  The intrinsic placement-response state reduces to
  (m,a), in addition to ordinary block metadata (length,ones).

Scope:
  * exact parametric phase compression: CLOSED;
  * exact two-block summary composition: CLOSED;
  * universal/right-congruence correction-language membership: still OPEN.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd
from typing import Optional

J0 = 10_439_860_591
R0 = 6_586_818_670
NLOG = 90
MATERIALIZE_MAX = 100_000
ARBITRARY_WORD_MAX_DEPTH = 11


def log_bounds(z: Fraction, n: int = NLOG):
    """Rigorous bounds for 2*atanh(z)=log((1+z)/(1-z))."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / (
        (2 * n + 3) * (1 - z * z)
    )
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))  # ln 2
L3, U3 = log_bounds(Fraction(1, 2))  # ln 3
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3
assert ALPHA_LO < ALPHA_HI


@lru_cache(maxsize=None)
def floor_alpha(n: int) -> int:
    """Return floor(n*log_3(2)), certified by the rational interval."""
    assert n >= 0
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi, ("insufficient log interval", n, flo, fhi)
    return flo


def requirement(n: int) -> int:
    # alpha is irrational: if ln2/ln3=a/b then 2^b=3^a, impossible.
    # Hence the least k with 3^k>2^n is floor(n*alpha)+1 for n>0.
    return 0 if n == 0 else floor_alpha(n) + 1


def phase_carry(a: int, b: int) -> int:
    c = floor_alpha(a + b) - floor_alpha(a) - floor_alpha(b)
    assert c in (0, 1)
    return c


def frac_compare(a: int, b: int) -> int:
    """Compare {a*alpha} and {b*alpha} exactly; return -1,0,+1."""
    if a == b:
        return 0
    if a > b:
        # (a-b)*alpha > F(a)-F(b) iff F(a-b) >= F(a)-F(b).
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


@dataclass(frozen=True)
class BallotSummary:
    length: int
    ones: int
    base_min: int
    critical_prefix: Optional[int]


def direct_summary(bits) -> BallotSummary:
    q = 0
    m = 0  # u=0 gives d(0)=0
    critical = None
    for u, bit in enumerate(bits, 1):
        q += bit
        d = q - floor_alpha(u)
        if d < m:
            m = d
            critical = u
        elif d == m:
            if critical is None or frac_compare(u, critical) > 0:
                critical = u
    return BallotSummary(len(bits), q, m, critical)


def margin_from_summary(h: int, s: BallotSummary) -> int:
    if h == 0:
        return s.base_min - 1 if s.critical_prefix is not None else 0
    return s.base_min - (
        phase_carry(h, s.critical_prefix)
        if s.critical_prefix is not None
        else 0
    )


def delta_from_summary(h: int, s: BallotSummary) -> int:
    return s.ones - (requirement(h + s.length) - requirement(h))


def compose(a: BallotSummary, b: BallotSummary) -> BallotSummary:
    assert a.length >= 1 and b.length >= 1

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
        # If b has no positive base minimizer, v=0 is its unique base-minimum
        # prefix; after placement its parent prefix is exactly |a|.
        right_candidate = a.length + (
            b.critical_prefix if b.critical_prefix is not None else 0
        )

    critical = max_fractional((left_candidate, right_candidate))
    return BallotSummary(
        a.length + b.length,
        a.ones + b.ones,
        parent_min,
        critical,
    )


def direct_margin(h: int, bits) -> int:
    q = 0
    ans = 0
    for u, bit in enumerate(bits, 1):
        q += bit
        ans = min(ans, q - (requirement(h + u) - requirement(h)))
    return ans


# ---------------------------------------------------------------------------
# 1. Generic exhaustive regression: arbitrary binary words.
# ---------------------------------------------------------------------------
DIRECT = {}
for n in range(1, ARBITRARY_WORD_MAX_DEPTH + 1):
    for bits in product((0, 1), repeat=n):
        DIRECT[bits] = direct_summary(bits)

arbitrary_composition_checks = 0
arbitrary_phase_checks = 0
for bits, exact in DIRECT.items():
    for split in range(1, len(bits)):
        got = compose(DIRECT[bits[:split]], DIRECT[bits[split:]])
        assert got == exact
        arbitrary_composition_checks += 1

    if len(bits) <= 9:
        for h in range(33):
            assert margin_from_summary(h, exact) == direct_margin(h, bits)
            arbitrary_phase_checks += 1

assert arbitrary_composition_checks == 36_868
assert arbitrary_phase_checks == 33_726


# ---------------------------------------------------------------------------
# 2. Existing 129-node Stern-Brocot/Christoffel DAG.
# ---------------------------------------------------------------------------
def build_stern_brocot_dag(p: int, q: int):
    assert 0 <= p <= q and gcd(p, q) == 1
    nodes = [
        {"p": 0, "q": 1, "left": None, "right": None},
        {"p": 1, "q": 1, "left": None, "right": None},
    ]
    if p == 0:
        return nodes, 0
    if p == q:
        return nodes, 1

    left = (0, 1, 0)
    right = (1, 1, 1)
    while True:
        assert left[1] * right[0] - left[0] * right[1] == 1
        mp = left[0] + right[0]
        mq = left[1] + right[1]
        mid = len(nodes)
        nodes.append({"p": mp, "q": mq, "left": left[2], "right": right[2]})
        cmp = p * mq - mp * q
        if cmp == 0:
            return nodes, mid
        if cmp < 0:
            right = (mp, mq, mid)
        else:
            left = (mp, mq, mid)


nodes, root = build_stern_brocot_dag(R0, J0)
assert len(nodes) == 129
assert root == 128

summaries = []
dag_parent_composition_checks = 0
for node in nodes:
    if node["left"] is None:
        # leaf 0 has positive minimal prefix u=1; leaf 1 does not.
        summary = BallotSummary(1, node["p"], 0, 1 if node["p"] == 0 else None)
    else:
        summary = compose(summaries[node["left"]], summaries[node["right"]])
        dag_parent_composition_checks += 1
    assert summary.length == node["q"]
    assert summary.ones == node["p"]
    summaries.append(summary)

assert dag_parent_composition_checks == 127


# ---------------------------------------------------------------------------
# 3. Independent materialization checks on every small enough DAG node.
# ---------------------------------------------------------------------------
@lru_cache(maxsize=None)
def materialize(i: int):
    node = nodes[i]
    if node["left"] is None:
        return (node["p"],)
    return materialize(node["left"]) + materialize(node["right"])


materialized_nodes = tuple(
    i for i, node in enumerate(nodes) if node["q"] <= MATERIALIZE_MAX
)
materialized_direct_summary_checks = 0
for i in materialized_nodes:
    assert direct_summary(materialize(i)) == summaries[i]
    materialized_direct_summary_checks += 1

assert len(materialized_nodes) == 45
assert materialized_direct_summary_checks == 45


# ---------------------------------------------------------------------------
# 4. Independent phase-response regression on directly expanded nodes.
# ---------------------------------------------------------------------------
PHASES = tuple(range(65)) + (
    75,
    128,
    255,
    256,
    511,
    1024,
    J0 - 1,
    J0,
    J0 + 1,
)

dag_phase_response_checks = 0
for i, node in enumerate(nodes):
    if node["q"] > 4096:
        continue
    bits = materialize(i)
    for h in PHASES:
        assert margin_from_summary(h, summaries[i]) == direct_margin(h, bits)
        dag_phase_response_checks += 1

assert dag_phase_response_checks == 1_628


# ---------------------------------------------------------------------------
# 5. Root/base-block headline state.
# ---------------------------------------------------------------------------
root_summary = summaries[root]
assert root_summary == BallotSummary(
    J0,
    R0,
    0,
    9_809_721_694,
)
assert margin_from_summary(0, root_summary) == -1
assert margin_from_summary(1, root_summary) == -1
assert margin_from_summary(J0, root_summary) == 0


print("PASS A0 s=1 Route-B exact phase-critical ballot certificate")
print("arbitrary_word_max_depth", ARBITRARY_WORD_MAX_DEPTH)
print("arbitrary_word_composition_checks", arbitrary_composition_checks)
print("arbitrary_word_phase_checks", arbitrary_phase_checks)
print("dag_nodes", len(nodes))
print("dag_parent_composition_checks", dag_parent_composition_checks)
print("materialized_nodes", len(materialized_nodes))
print("materialized_direct_summary_checks", materialized_direct_summary_checks)
print("dag_phase_response_checks", dag_phase_response_checks)
print("root_length", root_summary.length)
print("root_ones", root_summary.ones)
print("root_base_min", root_summary.base_min)
print("root_critical_prefix", root_summary.critical_prefix)
print("root_mu_h0", margin_from_summary(0, root_summary))
print("root_mu_h1", margin_from_summary(1, root_summary))
print("root_mu_hJ0", margin_from_summary(J0, root_summary))
print("floor_alpha_cache_entries", floor_alpha.cache_info().currsize)
print("formation_audit", "parent ballot response is formed from child summaries + concatenation boundary")
print("axis_audit", "absolute phase is external; intrinsic response reduces to base_min + one critical prefix")
print("status", "EXACT parametric ballot phase compression CLOSED; universal membership remains OPEN")
