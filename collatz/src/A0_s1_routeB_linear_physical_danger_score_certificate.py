#!/usr/bin/env python3
"""Exact scalar danger score for the directed physical defect gate.

The source/defect Pareto frontier is the general exact representation when both
ordinary source lower endpoint X_lo and accumulated defect eta must remain
separately queryable.  For the specific certified real-envelope rejection gate,
those two coordinates enter through one positive linear form and can be
scalarized exactly.

Imported directed constants use the common fixed-point scale QFP:

    lambda >= mW_lo/QFP,
    delta  >= delta_lo/QFP,
    c_threshold <= cW_hi/QFP,
    L_minus <= L_MAX.

For any dominance candidate with normalized defect eta,

    delta * X <= L_MAX + c_threshold - lambda*eta.

Therefore every candidate in a source family X>=X_lo is impossible if

    (mW_lo/QFP)*eta + (delta_lo/QFP)*X_lo
        > L_MAX + cW_hi/QFP.

Equivalently, with B=L_MAX*QFP+cW_hi,

    mW_lo*eta + delta_lo*X_lo > B.

Using the integer defect numerator N=3^q*eta gives the all-integer test

    P := mW_lo*N + delta_lo*3^q*X_lo
    P > B*3^q  => whole family rejected.

Now fix one exact future-control state and one exact quotient-parameter interval
payload [L,U].  Histories in the state differ only in source residue r and
integer defect numerator N, with

    X_lo = r + 2^h L.

The score is

    P = mW_lo*N + delta_lo*3^q*(r+2^h L).

Under a common next parameter bit epsilon, the payload child lower endpoint is

    L' = ceil((L-epsilon)/2),

and

    X_lo' - X_lo = chi*2^h,
    chi = epsilon + 2L' - L in {0,1}.

If emitted parity bit is 0:

    q'=q, N'=N,
    P' = P + delta_lo*3^q*chi*2^h.

If emitted parity bit is 1 at new target rank q+1 and target position a:

    N'=3N+2^a-2^h,
    q'=q+1,

so

    P' = 3P
         + mW_lo*(2^a-2^h)
         + delta_lo*3^(q+1)*chi*2^h.

Thus every common child transition maps P by an affine function with positive
coefficient 1 or 3 and a history-independent constant.  The ordering of P is
preserved forever.  Consequently each exact control+payload key needs only its
minimum P label for existence/nonexistence under this physical defect gate.

This scalarization is predicate-specific.  If later logic needs eta and X_lo
separately for other predicates, the more general (r,N) frontier must be
retained or those predicate coordinates must be added separately.
"""

from collections import defaultdict

import A0_s1_prefix_defect_membership_pruning_certificate as pruning

TEST_ROOTS = (2, 5, 8)
TEST_D = 8
TEST_INTERVAL = (3, 200)

QFP = pruning.QFP
M_LO = pruning.mW_lo
DELTA_LO = pruning.delta_lo
BARRIER = pruning.L_MAX * QFP + pruning.cW_hi

REQ = pruning.REQ
TH = pruning.TH
TPOS = pruning.TPOS


def target_correction(q: int) -> int:
    return sum(
        3 ** (q - r - 1) * (1 << TPOS[r])
        for r in range(q)
    )


def correction(bits) -> int:
    C = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << h)
    return C


def numerator(bits) -> int:
    return target_correction(sum(bits)) - correction(bits)


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def child_interval(L: int, U: int, epsilon: int):
    lo = ceil_div(L - epsilon, 2)
    hi = (U - epsilon) // 2
    return None if lo > hi else (lo, hi)


def refine_channel(state, bit: int):
    h, r, y, q = state
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)
    if bit == 0:
        y2 = (y + (3 ** q) * m0) // 2
        q2 = q
    else:
        y2 = (3 * y + (3 ** (q + 1)) * m0 + 1) // 2
        q2 = q + 1
    return h + 1, r2, y2, q2


def build_channel(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def control_step(Y: int, q: int, h: int, d: int, epsilon: int):
    G = pow(3, q, 1 << d)
    bit = (Y + epsilon) & 1
    if bit == 0:
        numer = Y + G * epsilon
    else:
        numer = 3 * (Y + G * epsilon) + 1
    assert numer % 2 == 0
    Y2 = 0 if d == 1 else (numer // 2) % (1 << (d - 1))
    return Y2, q + bit, bit


def score(r: int, N: int, h: int, q: int, L: int) -> int:
    X_lo = r + (1 << h) * L
    return M_LO * N + DELTA_LO * (3 ** q) * X_lo


def direct_layers(first: int):
    prefix = TH[:first] + (1,)
    h0, r0, y0, q0 = build_channel(prefix)
    N0 = numerator(prefix)

    raw = {
        (y0 % (1 << TEST_D), q0, TEST_INTERVAL[0], TEST_INTERVAL[1]):
        [(r0, N0)]
    }
    layers = []

    for i in range(TEST_D):
        d = TEST_D - i
        h = h0 + i
        nxt = defaultdict(list)

        for (Y, q, L, U), histories in raw.items():
            for epsilon in (0, 1):
                child = child_interval(L, U, epsilon)
                if child is None:
                    continue

                Y2, q2, bit = control_step(Y, q, h, d, epsilon)
                if q2 < REQ[h + 1]:
                    continue

                for r, N in histories:
                    r2 = r + (epsilon << h)
                    if bit == 0:
                        N2 = N
                    else:
                        a = TPOS[q2 - 1]
                        assert h <= a
                        N2 = 3 * N + (1 << a) - (1 << h)
                    nxt[(Y2, q2, child[0], child[1])].append((r2, N2))

        raw = dict(nxt)
        layers.append(raw)

    return layers


def scalar_layers(first: int):
    prefix = TH[:first] + (1,)
    h0, r0, y0, q0 = build_channel(prefix)
    N0 = numerator(prefix)
    L0, U0 = TEST_INTERVAL

    states = {
        (y0 % (1 << TEST_D), q0, L0, U0):
        score(r0, N0, h0, q0, L0)
    }
    layers = []

    for i in range(TEST_D):
        d = TEST_D - i
        h = h0 + i
        nxt = {}

        for (Y, q, L, U), P in states.items():
            for epsilon in (0, 1):
                child = child_interval(L, U, epsilon)
                if child is None:
                    continue

                Y2, q2, bit = control_step(Y, q, h, d, epsilon)
                if q2 < REQ[h + 1]:
                    continue

                chi = epsilon + 2 * child[0] - L
                assert chi in (0, 1)
                dx = chi << h

                if bit == 0:
                    P2 = P + DELTA_LO * (3 ** q) * dx
                else:
                    a = TPOS[q2 - 1]
                    assert h <= a
                    P2 = (
                        3 * P
                        + M_LO * ((1 << a) - (1 << h))
                        + DELTA_LO * (3 ** q2) * dx
                    )

                key2 = (Y2, q2, child[0], child[1])
                if key2 not in nxt or P2 < nxt[key2]:
                    nxt[key2] = P2

        states = nxt
        layers.append(states)

    return layers


# ---------------------------------------------------------------------------
# Exact regression: scalar Bellman labels equal direct minimum physical score.
# ---------------------------------------------------------------------------

layer_checks = 0
strict_merging_seen = False
closure_consistency_checks = 0

for first in TEST_ROOTS:
    direct = direct_layers(first)
    scalar = scalar_layers(first)
    assert len(direct) == len(scalar) == TEST_D

    prefix_h = first + 1
    for i, (raw_layer, scalar_layer) in enumerate(zip(direct, scalar), 1):
        h = prefix_h + i
        assert set(raw_layer) == set(scalar_layer)

        for key, histories in raw_layer.items():
            _Y, q, L, _U = key
            direct_scores = [score(r, N, h, q, L) for r, N in histories]
            assert scalar_layer[key] == min(direct_scores)
            if len(histories) > 1:
                strict_merging_seen = True

            threshold = BARRIER * (3 ** q)
            all_closed = all(P > threshold for P in direct_scores)
            scalar_closed = scalar_layer[key] > threshold
            assert scalar_closed == all_closed
            closure_consistency_checks += 1
            layer_checks += 1

assert strict_merging_seen
assert layer_checks > 0
assert closure_consistency_checks == layer_checks


# ---------------------------------------------------------------------------
# Abstract order-preservation audit for the affine score transitions.
# ---------------------------------------------------------------------------

order_checks = 0
for P1 in range(8):
    for P2 in range(P1, 10):
        for coeff in (1, 3):
            for const in range(5):
                assert coeff * P1 + const <= coeff * P2 + const
                order_checks += 1


print("PASS A0 s=1 Route-B linear physical danger score certificate")
print("test_roots", TEST_ROOTS)
print("future_precision", TEST_D)
print("test_parameter_interval", TEST_INTERVAL)
print("layer_checks", layer_checks)
print("closure_consistency_checks", closure_consistency_checks)
print("strict_merging_seen", strict_merging_seen)
print("order_checks", order_checks)
print(
    "score",
    "P=mW_lo*N + delta_lo*3^q*X_lo; reject whole family when P>(L_MAX*QFP+cW_hi)*3^q",
)
print(
    "transition",
    "common child maps P -> P+const for bit0 or P -> 3P+const for bit1",
)
print(
    "scalarization",
    "one minimum P per exact future-control + exact interval-payload key is sufficient for the directed physical defect gate",
)
print(
    "state_bound",
    "with the four-state interval payload theorem, n_i <= min(2^i,4*2^(D-i)*(i+1)) for the restricted source/ballot/physical-defect predicate set",
)
print(
    "dsd_audit",
    "the earlier Pareto frontier is general; this single-score collapse is legal only because the active physical gate queries one positive linear form of source lower endpoint and defect",
)
print(
    "status",
    "joint adaptive source+defect physical gate scalarized EXACTLY; adding projective/checkpoint predicates and proving all 14 roots close remains OPEN",
)
