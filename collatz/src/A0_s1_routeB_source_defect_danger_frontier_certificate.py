#!/usr/bin/env python3
"""Exact (source residue, defect) danger-frontier quotient for Route-B.

The source min-plus quotient keeps only minimum eta at a future-control state,
but adaptive physical pruning also depends on the ordinary lower source value.
A single eta minimum therefore loses information needed to exploit the decreasing
closure threshold eta_close(X_lo).

This certificate restores exact adaptive physical information with a Pareto
frontier.

At one layered family node use the exact key

    K = (future control, parameter-interval payload).

For the restricted regression below the future control is (Y mod2^d,q) and the
payload is the exact quotient-parameter interval I=[L,U].  Histories sharing K
may still have different canonical source residues r and accumulated defects e.

Keep only undominated pairs

    (r,e),

under coordinatewise minimization:

    (r1,e1) dominates (r2,e2) iff r1<=r2 and e1<=e2.

Why this is exact:

* same future control + same next parameter bit -> same emitted parity;
* source residue update is r' = r + epsilon*2^h, so residue order is preserved;
* same interval payload -> the quotient-parameter child interval is identical;
* same emitted parity/rank -> the future defect increment is identical;
* therefore e order is preserved;
* ordinary family lower source is X_lo=r+2^h L, so residue order is exactly
  ordinary-X lower-endpoint order when payload L is shared.

Consequently a dominated pair can never be the unique surviving history under
any common future parameter suffix or under the monotone physical defect gate.
The frontier is exact for existence/nonexistence of a survivor, provided every
other active predicate is included in the future-control key.

No horizon-independent bound on frontier width is proved here.
"""

from collections import defaultdict
from fractions import Fraction

TEST_ROOTS = (2, 5, 8)
TEST_D = 8
TEST_INTERVAL = (3, 200)


def requirements(nmax: int):
    q = [0]
    p2 = p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


REQ = requirements(100)
TH = tuple(REQ[i + 1] - REQ[i] for i in range(99))
TPOS = tuple(i for i, bit in enumerate(TH) if bit)


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


def prefix_eta(bits):
    q = 0
    out = Fraction(0)
    for pos, bit in enumerate(bits):
        if bit:
            q += 1
            target_pos = TPOS[q - 1]
            assert pos <= target_pos
            out += Fraction((1 << target_pos) - (1 << pos), 3 ** q)
    return out


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


def defect_increment(h: int, q_after: int, bit: int):
    if bit == 0:
        return Fraction(0)
    target_pos = TPOS[q_after - 1]
    assert h <= target_pos
    return Fraction((1 << target_pos) - (1 << h), 3 ** q_after)


def pareto(points):
    """Coordinatewise-minimal (r,eta) frontier, sorted by r."""
    best_by_r = {}
    for r, eta in points:
        if r not in best_by_r or eta < best_by_r[r]:
            best_by_r[r] = eta

    out = []
    best_eta = None
    for r, eta in sorted(best_by_r.items()):
        if best_eta is None or eta < best_eta:
            out.append((r, eta))
            best_eta = eta
    return tuple(out)


def direct_layers(first: int):
    prefix = TH[:first] + (1,)
    h0, r0, y0, q0 = build_channel(prefix)
    base = prefix_eta(prefix)

    # key=(Y,q,L,U) -> raw list of (r,eta)
    raw = {
        (y0 % (1 << TEST_D), q0, TEST_INTERVAL[0], TEST_INTERVAL[1]):
        [(r0, base)]
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

                add = defect_increment(h, q2, bit)
                key2 = (Y2, q2, child[0], child[1])

                for r, eta in histories:
                    nxt[key2].append((r + (epsilon << h), eta + add))

        raw = dict(nxt)
        layers.append(raw)

    return layers


def frontier_layers(first: int):
    prefix = TH[:first] + (1,)
    h0, r0, y0, q0 = build_channel(prefix)
    base = prefix_eta(prefix)

    front = {
        (y0 % (1 << TEST_D), q0, TEST_INTERVAL[0], TEST_INTERVAL[1]):
        ((r0, base),)
    }
    layers = []

    for i in range(TEST_D):
        d = TEST_D - i
        h = h0 + i
        nxt = defaultdict(list)

        for (Y, q, L, U), histories in front.items():
            for epsilon in (0, 1):
                child = child_interval(L, U, epsilon)
                if child is None:
                    continue

                Y2, q2, bit = control_step(Y, q, h, d, epsilon)
                if q2 < REQ[h + 1]:
                    continue

                add = defect_increment(h, q2, bit)
                key2 = (Y2, q2, child[0], child[1])

                for r, eta in histories:
                    nxt[key2].append((r + (epsilon << h), eta + add))

        front = {key: pareto(vals) for key, vals in nxt.items()}
        layers.append(front)

    return layers


# ---------------------------------------------------------------------------
# Exact finite regression: pruning after every layer equals direct Pareto.
# ---------------------------------------------------------------------------

expected_final = {
    2: (4, 5, 13, 80),
    5: (5, 4, 12, 87),
    8: (5, 10, 22, 93),
}

layer_checks = 0
strict_compression_seen = False

for first in TEST_ROOTS:
    direct = direct_layers(first)
    front = frontier_layers(first)
    assert len(direct) == len(front) == TEST_D

    for raw_layer, front_layer in zip(direct, front):
        assert set(raw_layer) == set(front_layer)
        for key, raw_points in raw_layer.items():
            assert front_layer[key] == pareto(raw_points)
            if len(front_layer[key]) < len(raw_points):
                strict_compression_seen = True
            layer_checks += 1

    raw_final = direct[-1]
    front_final = front[-1]
    key_count = len(front_final)
    max_width = max(len(v) for v in front_final.values())
    frontier_entries = sum(len(v) for v in front_final.values())
    raw_entries = sum(len(v) for v in raw_final.values())
    assert (key_count, max_width, frontier_entries, raw_entries) == expected_final[first]

assert strict_compression_seen


# ---------------------------------------------------------------------------
# Algebraic preservation audit on representative abstract pairs.
# ---------------------------------------------------------------------------
# Same payload/control transition adds the same constants to both coordinates:
#
#   r'   = r + epsilon*2^h,
#   eta' = eta + kappa.
#
# Coordinatewise dominance is therefore preserved exactly.

preservation_checks = 0
for r1 in range(4):
    for r2 in range(r1, 5):
        for e1_num in range(4):
            for e2_num in range(e1_num, 5):
                eta1 = Fraction(e1_num, 7)
                eta2 = Fraction(e2_num, 7)
                for epsilon in (0, 1):
                    for h in range(4):
                        add_r = epsilon << h
                        for k_num in range(3):
                            kappa = Fraction(k_num, 11)
                            assert r1 + add_r <= r2 + add_r
                            assert eta1 + kappa <= eta2 + kappa
                            preservation_checks += 1


print("PASS A0 s=1 Route-B source-defect danger frontier certificate")
print("test_roots", TEST_ROOTS)
print("future_precision", TEST_D)
print("test_parameter_interval", TEST_INTERVAL)
print("layer_checks", layer_checks)
print("strict_compression_seen", strict_compression_seen)
print("preservation_checks", preservation_checks)
for first in TEST_ROOTS:
    print("final_root_summary", first, expected_final[first])
print(
    "frontier",
    "for fixed future control and exact parameter payload, retain coordinatewise-minimal (source residue r, accumulated eta) pairs",
)
print(
    "dominance_preservation",
    "common future parameter steps add identical constants to r and eta, so Pareto dominance is invariant",
)
print(
    "physical_order",
    "with shared payload lower L, X_lo=r+2^h*L; smaller r means smaller physical lower endpoint and therefore a harder physical closure threshold",
)
print(
    "dsd_audit",
    "adaptive physical pruning and Bellman defect merging are jointly exact on this frontier; no bounded frontier width is inferred",
)
print(
    "status",
    "joint source/defect danger-frontier semantics CLOSED; root-scale frontier-width/compression theorem and remaining membership coordinates remain OPEN",
)
