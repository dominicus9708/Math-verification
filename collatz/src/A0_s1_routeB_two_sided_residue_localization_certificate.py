#!/usr/bin/env python3
"""Exact two-sided residue localization for A0 s=1 Route-B.

For a parity block B of length h, q odd symbols, and correction C(B),

    2^h Y = 3^q X + C(B).

At dyadic resolution K<=h, its canonical source cylinder is

    x_K(B) = -C(B) * (3^q)^(-1) mod 2^K.

At ternary resolution R<=q, its canonical endpoint cylinder is

    y_R(B) = C(B) * (2^h)^(-1) mod 3^R.

For W=UV, exact correction composition gives

    C(UV)=3^q(V) C(U)+2^h(U) C(V).

Hence the two boundaries screen independently:

    x_K(UV)=x_K(U)   when K<=h(U),
    y_R(UV)=y_R(V)   when R<=q(V).

At the internal cut Z=T^h(U)(X), the adjacent child requirements are

    Z = y_R(U) mod 3^R,
    Z = x_K(V) mod 2^K,

which form a unique CRT class modulo 2^K 3^R.

The certificate proves these localization identities by exact arithmetic and
regression, then audits whether fixed low-resolution external or internal
boundary signatures distinguish nodes of the existing 129-node Christoffel
DAG.  They do not: at the relevant Route-B resolutions all eligible large
nodes collapse to a single signature.  Thus two-sided boundary screening is
an exact recursive primitive, but a boundary-only quotient is rejected.

Formation-Axiom lens:
  boundaries are projections/consequences of the formed block and do not
  determine the internal formation tree at fixed low resolution.

Axis-property lens:
  source dyadic and endpoint ternary coordinates are valid oriented boundary
  axes, but they are not jointly separating; a hierarchical interior/scale
  coordinate remains necessary.

Scope:
  * exact two-sided boundary localization: CLOSED;
  * boundary-only finite quotient at tested Route-B exposures: REJECTED;
  * scale-aware/hierarchical lazy decoder: OPEN.
"""

from functools import lru_cache
from itertools import product
from math import gcd

J0 = 10_439_860_591
R0 = 6_586_818_670
T0 = 10 * J0
J_ODD = 10 * R0 + 1
X_TH = 4_697_939_311_072_332_635_131

K_VALUES = (1, 2, 4, 8, 16, 27, 32, 39, 64, 72, 74, 75, 128)
R_VALUES = (1, 2, 4, 8, 16, 24, 28, 32, 40, 64)
MATERIALIZE_MAX = 100_000
ARBITRARY_WORD_MAX_DEPTH = 12


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
assert nodes[root]["q"] == J0
assert nodes[root]["p"] == R0


def correction(bits):
    h = q = C = 0
    for b in bits:
        if b:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


def compose_c(Cu: int, hu: int, Cv: int, qv: int) -> int:
    return (3 ** qv) * Cu + (1 << hu) * Cv


def x_residue(C: int, q: int, K: int) -> int:
    mod = 1 << K
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def y_residue(C: int, h: int, R: int) -> int:
    mod = 3 ** R
    return (C * pow(pow(2, h, mod), -1, mod)) % mod


# ---------------------------------------------------------------------------
# 1. Exhaustive arbitrary-word regression through depth 12.
# ---------------------------------------------------------------------------
arbitrary_composition_checks = 0
arbitrary_front_screening_checks = 0
arbitrary_rear_screening_checks = 0

for n in range(2, ARBITRARY_WORD_MAX_DEPTH + 1):
    for bits in product((0, 1), repeat=n):
        h, q, C = correction(bits)
        for split in range(1, n):
            ub = bits[:split]
            vb = bits[split:]
            hu, qu, Cu = correction(ub)
            hv, qv, Cv = correction(vb)

            assert h == hu + hv
            assert q == qu + qv
            assert C == compose_c(Cu, hu, Cv, qv)
            arbitrary_composition_checks += 1

            for K in range(1, hu + 1):
                assert x_residue(C, q, K) == x_residue(Cu, qu, K)
                arbitrary_front_screening_checks += 1

            for R in range(1, qv + 1):
                assert y_residue(C, h, R) == y_residue(Cv, hv, R)
                arbitrary_rear_screening_checks += 1

assert arbitrary_composition_checks == 81_924
assert arbitrary_front_screening_checks == 458_748
assert arbitrary_rear_screening_checks == 229_374


# ---------------------------------------------------------------------------
# 2. Exact correction projections on the 129-node DAG.
# ---------------------------------------------------------------------------
def cmod_table(mod: int):
    out = []
    for node in nodes:
        if node["left"] is None:
            c = node["p"] % mod
        else:
            li = node["left"]
            ri = node["right"]
            left = nodes[li]
            right = nodes[ri]
            c = (
                pow(3, right["p"], mod) * out[li]
                + pow(2, left["q"], mod) * out[ri]
            ) % mod
        out.append(c)
    return tuple(out)


CMOD2 = {K: cmod_table(1 << K) for K in K_VALUES}
CMOD3 = {R: cmod_table(3 ** R) for R in R_VALUES}

dyadic_parent_composition_checks = 0
for K, table in CMOD2.items():
    mod = 1 << K
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        ri = node["right"]
        recomposed = (
            pow(3, nodes[ri]["p"], mod) * table[li]
            + pow(2, nodes[li]["q"], mod) * table[ri]
        ) % mod
        assert recomposed == table[i]
        dyadic_parent_composition_checks += 1

ternary_parent_composition_checks = 0
for R, table in CMOD3.items():
    mod = 3 ** R
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        ri = node["right"]
        recomposed = (
            pow(3, nodes[ri]["p"], mod) * table[li]
            + pow(2, nodes[li]["q"], mod) * table[ri]
        ) % mod
        assert recomposed == table[i]
        ternary_parent_composition_checks += 1

assert dyadic_parent_composition_checks == 1_651
assert ternary_parent_composition_checks == 1_270


def node_x(i: int, K: int):
    node = nodes[i]
    if node["q"] < K:
        return None
    mod = 1 << K
    return (
        -CMOD2[K][i]
        * pow(pow(3, node["p"], mod), -1, mod)
    ) % mod


def node_y(i: int, R: int):
    node = nodes[i]
    if node["p"] < R:
        return None
    mod = 3 ** R
    return (
        CMOD3[R][i]
        * pow(pow(2, node["q"], mod), -1, mod)
    ) % mod


# ---------------------------------------------------------------------------
# 3. DAG screening identities.
# ---------------------------------------------------------------------------
dag_front_screening_checks = 0
for K in K_VALUES:
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        if nodes[li]["q"] >= K:
            assert node_x(i, K) == node_x(li, K)
            dag_front_screening_checks += 1

dag_rear_screening_checks = 0
for R in R_VALUES:
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        ri = node["right"]
        if nodes[ri]["p"] >= R:
            assert node_y(i, R) == node_y(ri, R)
            dag_rear_screening_checks += 1

assert dag_front_screening_checks == 1_560
assert dag_rear_screening_checks == 1_191


# ---------------------------------------------------------------------------
# 4. Direct materialization regression on all small DAG nodes.
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
materialized_projection_checks = 0
for i in materialized_nodes:
    bits = materialize(i)
    h, q, C = correction(bits)
    assert h == nodes[i]["q"]
    assert q == nodes[i]["p"]
    for K in K_VALUES:
        assert C % (1 << K) == CMOD2[K][i]
        materialized_projection_checks += 1
    for R in R_VALUES:
        assert C % (3 ** R) == CMOD3[R][i]
        materialized_projection_checks += 1

assert len(materialized_nodes) == 45
assert sum(nodes[i]["q"] for i in materialized_nodes) == 457_063
assert materialized_projection_checks == 1_035


# ---------------------------------------------------------------------------
# 5. Giant threshold block W_th = U L^9 without materializing L.
# ---------------------------------------------------------------------------
def compose_mod(Cu: int, hu: int, Cv: int, qv: int, mod: int) -> int:
    return (
        pow(3, qv, mod) * Cu
        + pow(2, hu, mod) * Cv
    ) % mod


def threshold_cmod(mod: int, CL: int):
    # Existing Route-B identity: C(U)=C(L)+3^R0.
    CU = (CL + pow(3, R0, mod)) % mod
    C = CU
    h = J0
    q = R0 + 1
    for _ in range(9):
        C = compose_mod(C, h, CL, R0, mod)
        h += J0
        q += R0
    assert h == T0
    assert q == J_ODD
    return C


def threshold_x(K: int):
    mod = 1 << K
    CW = threshold_cmod(mod, CMOD2[K][root])
    return (-CW * pow(pow(3, J_ODD, mod), -1, mod)) % mod


def threshold_y(R: int):
    mod = 3 ** R
    CW = threshold_cmod(mod, CMOD3[R][root])
    return (CW * pow(pow(2, T0, mod), -1, mod)) % mod


assert threshold_x(27) == X_TH % (1 << 27)
assert threshold_x(39) == X_TH % (1 << 39)
assert threshold_x(74) == X_TH % (1 << 74)
assert threshold_x(75) != X_TH % (1 << 75)

# Rear screening says W_th has the same low ternary endpoint cylinder as its
# final copy of L.
assert threshold_y(24) == node_y(root, 24)
assert threshold_y(28) == node_y(root, 28)

X27 = threshold_x(27)
X39 = threshold_x(39)
X74 = threshold_x(74)
X75 = threshold_x(75)
Y24 = threshold_y(24)
Y28 = threshold_y(28)

assert X27 == 29_252_603
assert X39 == 188_068_289_531
assert X74 == 4_697_939_311_072_332_635_131
assert X75 == 23_587_405_242_550_913_489_915
assert Y24 == 181_784_647_214
assert Y28 == 2_158_791_402_581


# ---------------------------------------------------------------------------
# 6. Candidate-quotient audit: fixed low-resolution boundaries are not
#    separating on the Christoffel path.
# ---------------------------------------------------------------------------
def boundary_collision_stats(K: int, R: int):
    eligible = [
        i for i, node in enumerate(nodes)
        if node["q"] >= K and node["p"] >= R
    ]
    sigs = {(node_x(i, K), node_y(i, R)) for i in eligible}
    return len(eligible), len(sigs)


def interface_collision_stats(K: int, R: int):
    # Parent P=UV.  The interface Z must simultaneously lie in the endpoint
    # cylinder of U mod 3^R and the source cylinder of V mod 2^K.
    eligible = []
    sigs = set()
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        ri = node["right"]
        if nodes[li]["p"] >= R and nodes[ri]["q"] >= K:
            eligible.append(i)
            sigs.add((node_y(li, R), node_x(ri, K)))
    return len(eligible), len(sigs)


def full_boundary_interface_stats(K: int, R: int):
    eligible = []
    sigs = set()
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        ri = node["right"]
        if (
            node["q"] >= K
            and node["p"] >= R
            and nodes[li]["p"] >= R
            and nodes[ri]["q"] >= K
        ):
            eligible.append(i)
            sigs.add(
                (
                    node_x(i, K),
                    node_y(i, R),
                    node_y(li, R),
                    node_x(ri, K),
                )
            )
    return len(eligible), len(sigs)


COLLISION_CASES = ((27, 28), (39, 28), (74, 28))
collision_results = {}
for K, R in COLLISION_CASES:
    b = boundary_collision_stats(K, R)
    z = interface_collision_stats(K, R)
    f = full_boundary_interface_stats(K, R)
    collision_results[(K, R)] = (b, z, f)

assert collision_results[(27, 28)] == ((120, 1), (117, 1), (117, 1))
assert collision_results[(39, 28)] == ((120, 1), (117, 1), (117, 1))
assert collision_results[(74, 28)] == ((118, 1), (117, 1), (117, 1))


print("PASS A0 s=1 Route-B exact two-sided residue localization certificate")
print("arbitrary_word_max_depth", ARBITRARY_WORD_MAX_DEPTH)
print("arbitrary_correction_composition_checks", arbitrary_composition_checks)
print("arbitrary_front_dyadic_screening_checks", arbitrary_front_screening_checks)
print("arbitrary_rear_ternary_screening_checks", arbitrary_rear_screening_checks)
print("dag_nodes", len(nodes))
print("dag_dyadic_parent_projection_checks", dyadic_parent_composition_checks)
print("dag_ternary_parent_projection_checks", ternary_parent_composition_checks)
print("dag_front_screening_checks", dag_front_screening_checks)
print("dag_rear_screening_checks", dag_rear_screening_checks)
print("materialized_nodes", len(materialized_nodes))
print("materialized_total_bits", sum(nodes[i]["q"] for i in materialized_nodes))
print("materialized_projection_checks", materialized_projection_checks)
print("threshold_x27", X27)
print("threshold_x39", X39)
print("threshold_x74", X74)
print("threshold_x75", X75)
print("threshold_y24", Y24)
print("threshold_y28", Y28)
for key in COLLISION_CASES:
    b, z, f = collision_results[key]
    print("collision_case", key, "boundary", b, "interface", z, "full", f)
print("formation_audit", "fixed boundary projections do not determine the internal Christoffel formation")
print("axis_audit", "dyadic/ternary boundary axes orient correctly but are not jointly separating")
print("status", "EXACT two-sided boundary screening CLOSED; boundary-only quotient REJECTED; scale-aware interior decoder OPEN")
