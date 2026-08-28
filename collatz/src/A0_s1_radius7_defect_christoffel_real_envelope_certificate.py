#!/usr/bin/env python3
"""A0 s=1 radius-seven defect + Christoffel real-envelope certificate.

This certificate combines three already-safe ingredients:

1. radius-seven closure -> every survivor has first-75 Hamming distance >= 8;
2. pure lower-ballot order -> every odd position is no later than the
   threshold odd position, so the threshold correction is maximal;
3. the 129-node Stern-Brocot/Christoffel DAG for the base block L.

It proves an exact finite lower bound on the normalized correction defect
forced by d_75 >= 8, evaluates a rigorous real interval for the gigantic
threshold correction without materializing the 10^11-bit word, and derives
a stronger necessary upper bound on the physical A0 start X.

No floating-point value is used in an assertion.
"""

from fractions import Fraction
from math import gcd

J0 = 10_439_860_591
R0 = 6_586_818_670
T0 = 10 * J0
J_ODD = 10 * R0 + 1
L_MAX = 934_928_480_993
OLD_X_MAX = 3_295_414_002_074_039_191_016

NLOG = 90
BFP = 256
QFP = 1 << BFP
NEXP = 90


def threshold_requirements(nmax: int):
    q = [0]
    p2 = 1
    p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


# ---------------------------------------------------------------------------
# 1. Exact first-75 normalized-defect DP.
# ---------------------------------------------------------------------------

REQ = threshold_requirements(200)
TH = tuple(REQ[n + 1] - REQ[n] for n in range(200))
TPOS = tuple(i for i, b in enumerate(TH) if b)
assert len(TPOS) >= 75
assert REQ[75] == 48

# If the candidate r-th one is at a_r and the threshold r-th one is at t_r,
# pure ballot gives a_r <= t_r. Therefore its normalized correction defect
# contribution is 3^{-r}(2^{t_r}-2^{a_r}) >= 0. Future terms only add.
# Cap the Hamming state at 8, so d=8 means "at least 8".
dp = {(0, 0): (Fraction(0), "")}
for pos in range(75):
    tbit = TH[pos]
    nxt = {}
    for (q, dcap), (eta, word) in dp.items():
        for bit in (0, 1):
            nq = q + bit
            if nq < REQ[pos + 1]:
                continue
            nd = min(8, dcap + (bit != tbit))
            add = Fraction(0)
            if bit:
                r = nq
                add = Fraction((1 << TPOS[r - 1]) - (1 << pos), 3 ** r)
                assert add >= 0
            val = eta + add
            key = (nq, nd)
            if key not in nxt or val < nxt[key][0]:
                nxt[key] = (val, word + str(bit))
    dp = nxt

eta_min, q_min, witness = min(
    (val, q, word)
    for (q, dcap), (val, word) in dp.items()
    if dcap == 8
)

ETA_EXPECTED = Fraction(
    150_621_601_264_545_747_200,
    328_256_967_394_537_077_627,
)
assert eta_min == ETA_EXPECTED
assert q_min == 48

wbits = tuple(int(c) for c in witness)
flips = tuple(i for i in range(75) if wbits[i] != TH[i])
assert flips == (8, 9, 27, 28, 46, 47, 65, 66)
assert sum(wbits) == 48
assert eta_min == (
    Fraction(1 << 8, 3 ** 7)
    + Fraction(1 << 27, 3 ** 19)
    + Fraction(1 << 46, 3 ** 31)
    + Fraction(1 << 65, 3 ** 43)
)

# Maximal possible first disagreement among pure-ballot prefixes with
# Hamming distance >=8. This implies v2(eta)<=65 for every such word.
def can_finish_from_first_difference(f: int) -> bool:
    q = sum(TH[:f])
    bit = 1 - TH[f]
    q += bit
    if q < REQ[f + 1]:
        return False
    states = {(q, 1)}
    for pos in range(f + 1, 75):
        ns = set()
        for cq, d in states:
            for b in (TH[pos], 1 - TH[pos]):
                nq = cq + b
                if nq < REQ[pos + 1]:
                    continue
                ns.add((nq, min(8, d + (b != TH[pos]))))
        states = ns
    return any(d == 8 for _, d in states)


possible_first = [f for f in range(75) if can_finish_from_first_difference(f)]
assert max(possible_first) == 65


# ---------------------------------------------------------------------------
# 2. Exact Stern-Brocot DAG for lower mechanical base block L.
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
assert nodes[root]["p"] == R0
assert nodes[root]["q"] == J0


# ---------------------------------------------------------------------------
# 3. Rigorous log and fixed-point exponential intervals.
# ---------------------------------------------------------------------------

def log_bounds(z: Fraction, n: int = NLOG):
    # 2*atanh(z), with positive tail bounded geometrically.
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / (
        (2 * n + 3) * (1 - z * z)
    )
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))  # ln 2
L3, U3 = log_bounds(Fraction(1, 2))  # ln 3


def floor_scaled(x: Fraction) -> int:
    return (x.numerator * QFP) // x.denominator


def ceil_scaled(x: Fraction) -> int:
    n = x.numerator * QFP
    d = x.denominator
    return -((-n) // d)


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def exp_pos_fixed(Y: int):
    """Bounds exp(Y/QFP) for 0<=Y<QFP, on the same fixed-point scale."""
    assert 0 <= Y < QFP
    term_lo = term_hi = QFP
    sum_lo = sum_hi = QFP

    for k in range(1, NEXP + 1):
        term_lo = (term_lo * Y) // (QFP * k)
        term_hi = ceil_div(term_hi * Y, QFP * k)
        sum_lo += term_lo
        sum_hi += term_hi

    # Positive Taylor tail. All later term ratios are <= y/(NEXP+2).
    next_hi = ceil_div(term_hi * Y, QFP * (NEXP + 1))
    denom = QFP * (NEXP + 2) - Y
    tail_hi = ceil_div(next_hi * QFP * (NEXP + 2), denom)
    return sum_lo, sum_hi + tail_hi


def exp_point_fixed(X: int):
    if X >= 0:
        return exp_pos_fixed(X)

    lo_pos, hi_pos = exp_pos_fixed(-X)
    # Reciprocal interval with outward rounding.
    return (QFP * QFP) // hi_pos, ceil_div(QFP * QFP, lo_pos)


def multiplier_interval(p: int, q: int):
    # m = 3^p / 2^q = exp(p ln3 - q ln2).
    x_lo = p * L3 - q * U2
    x_hi = p * U3 - q * L2
    X_lo = floor_scaled(x_lo)
    X_hi = ceil_scaled(x_hi)
    m_lo, _ = exp_point_fixed(X_lo)
    _, m_hi = exp_point_fixed(X_hi)
    return m_lo, m_hi


def mul_lo(a: int, b: int) -> int:
    return (a * b) // QFP


def mul_hi(a: int, b: int) -> int:
    return ceil_div(a * b, QFP)


# Node state:
#   m = 3^ones / 2^length
#   c = C(word) / 2^length
# For uv: m(uv)=m(u)m(v), c(uv)=m(v)c(u)+c(v).
mints = []
cints = []
for node in nodes:
    mlo, mhi = multiplier_interval(node["p"], node["q"])
    mints.append((mlo, mhi))

    if node["left"] is None:
        cint = (0, 0) if node["p"] == 0 else (QFP // 2, QFP // 2)
    else:
        li = node["left"]
        ri = node["right"]
        cl_lo, cl_hi = cints[li]
        cr_lo, cr_hi = cints[ri]
        mr_lo, mr_hi = mints[ri]
        cint = (
            mul_lo(mr_lo, cl_lo) + cr_lo,
            mul_hi(mr_hi, cl_hi) + cr_hi,
        )
    cints.append(cint)

mL_lo, mL_hi = mints[root]
cL_lo, cL_hi = cints[root]

# Threshold decomposition W_th=U L^9, with
#   C(U)=C(L)+3^R0,
# so c(U)=c(L)+m(L), while m(U)=3m(L).
mW_lo, mW_hi = 3 * mL_lo, 3 * mL_hi
cW_lo, cW_hi = cL_lo + mL_lo, cL_hi + mL_hi

for _ in range(9):
    cW_lo, cW_hi = (
        mul_lo(mL_lo, cW_lo) + cL_lo,
        mul_hi(mL_hi, cW_hi) + cL_hi,
    )
    mW_lo, mW_hi = mul_lo(mW_lo, mL_lo), mul_hi(mW_hi, mL_hi)

assert 4_751_385_314 * QFP < cL_lo < cL_hi < 4_751_385_315 * QFP
assert 47_513_853_148 * QFP < cW_lo < cW_hi < 47_513_853_149 * QFP
assert 2 * QFP < mW_lo < mW_hi < 3 * QFP


# ---------------------------------------------------------------------------
# 4. Forced defect and stronger X pruning.
# ---------------------------------------------------------------------------

# eta >= eta_min and lambda=m(W_th) >= mW_lo/QFP.
eta_lo = (eta_min.numerator * QFP) // eta_min.denominator
defect_effect_lo = mul_lo(mW_lo, eta_lo)

# Every survivor has C/2^T0 <= c_threshold - lambda*eta.
candidate_c_hi = cW_hi - defect_effect_lo
assert candidate_c_hi < 47_513_853_147 * QFP

# delta = 3-lambda. Since lambda <= mW_hi/QFP,
# delta >= (3QFP-mW_hi)/QFP.
delta_lo = 3 * QFP - mW_hi
assert delta_lo > 0

# Bridge identity:
#   C/2^T0 = delta*X - L_-,  with L_- <= L_MAX.
# Therefore delta_lo*X <= L_MAX + candidate_c_hi/QFP.
new_x_max = (L_MAX * QFP + candidate_c_hi) // delta_lo

NEW_X_MAX_EXPECTED = 3_234_977_022_306_677_631_165
assert new_x_max == NEW_X_MAX_EXPECTED
assert 2 ** 71 < new_x_max < OLD_X_MAX < 2 ** 72

print("PASS A0 s=1 radius-seven defect + Christoffel real-envelope certificate")
print("eta75_min_fraction", eta_min)
print("eta75_min_witness_flips", flips)
print("earliest_defect_position_max", max(possible_first))
print("christoffel_dag_nodes", len(nodes))
print("cL_bracket", "4751385314 < C(L)/2^J0 < 4751385315")
print("threshold_c_bracket", "47513853148 < C(W_th)/2^T0 < 47513853149")
print("candidate_c_upper_integer_bracket", "< 47513853147")
print("old_X_max", OLD_X_MAX)
print("new_X_max", new_x_max)
print("X_max_reduction", OLD_X_MAX - new_x_max)
print("status", "SAFE necessary pruning; C4F not used")
