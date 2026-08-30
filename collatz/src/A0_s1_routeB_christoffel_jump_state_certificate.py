#!/usr/bin/env python3
"""Exact modular jump state for the A0 s=1 Route-B Christoffel DAG.

The 129-node Stern-Brocot/Christoffel DAG compresses the lower-mechanical
base block L of length J0.  The full exact correction C(L) has billions of
bits, so it is the wrong object to materialize during target decoding.

For a parity block w of length h with q odd symbols define

    C_K(w) = C(w) mod 2^K.

The exact correction composition law

    C(uv) = 3^q(v) C(u) + 2^h(u) C(v)

therefore descends to every dyadic projection:

    C_K(uv) = 3^q(v) C_K(u) + 2^h(u) C_K(v)  (mod 2^K).

Moreover the canonical cylinder residue is recovered at the same resolution:

    r(w) mod 2^K = -C_K(w) * (3^q(w))^(-1) mod 2^K,

for K <= h.  Thus low-order target/cylinder discrimination can jump over an
entire Christoffel node without materializing its word or its gigantic C.

This certificate also audits an important placement-state obstruction.  If an
absolute ballot phase h were attached to every reused DAG occurrence, the
129-node DAG for L would expand to J0 leaf placements and 2*J0-1 total binary-
tree node placements.  Hence phase is not an intrinsic node coordinate and a
naive (node,h) lift destroys the compression.

Scope:
  * exact modular correction jump state: CLOSED;
  * exact low-resolution canonical-residue recovery: CLOSED;
  * exact target-threshold projection through the first disagreement: CLOSED;
  * compressed phase-sensitive ballot/right-congruence decoder: OPEN.
"""

from functools import lru_cache
from math import gcd

J0 = 10_439_860_591
R0 = 6_586_818_670
T0 = 10 * J0
J_ODD = 10 * R0 + 1
X_TH = 4_697_939_311_072_332_635_131

K_VALUES = (1, 2, 4, 8, 16, 32, 64, 72, 74, 75, 128, 256, 512, 1024)
MATERIALIZE_MAX = 100_000


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
assert sum(n["left"] is not None for n in nodes) == 127


# ---------------------------------------------------------------------------
# 1. Intrinsic modular correction state on all 129 DAG nodes.
# ---------------------------------------------------------------------------

def build_cmod_table(K: int):
    mod = 1 << K
    out = []
    for node in nodes:
        if node["left"] is None:
            C = node["p"]  # leaf 0 -> C=0, leaf 1 -> C=1
        else:
            li = node["left"]
            ri = node["right"]
            left = nodes[li]
            right = nodes[ri]
            C = (
                pow(3, right["p"], mod) * out[li]
                + pow(2, left["q"], mod) * out[ri]
            ) % mod
        out.append(C)
    return tuple(out)


CMOD = {K: build_cmod_table(K) for K in K_VALUES}

parent_composition_checks = 0
for K in K_VALUES:
    mod = 1 << K
    table = CMOD[K]
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        ri = node["right"]
        left = nodes[li]
        right = nodes[ri]
        recomposed = (
            pow(3, right["p"], mod) * table[li]
            + pow(2, left["q"], mod) * table[ri]
        ) % mod
        assert recomposed == table[i]
        assert node["p"] == left["p"] + right["p"]
        assert node["q"] == left["q"] + right["q"]
        parent_composition_checks += 1

assert parent_composition_checks == 127 * len(K_VALUES)

# Dyadic projections must be mutually consistent as K grows.
projection_consistency_checks = 0
for i in range(len(nodes)):
    for a, b in zip(K_VALUES, K_VALUES[1:]):
        assert CMOD[b][i] % (1 << a) == CMOD[a][i]
        projection_consistency_checks += 1

assert projection_consistency_checks == len(nodes) * (len(K_VALUES) - 1)


# ---------------------------------------------------------------------------
# 2. Direct materialization regression on every node short enough to expand.
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def materialize(i: int):
    node = nodes[i]
    if node["left"] is None:
        return (node["p"],)
    return materialize(node["left"]) + materialize(node["right"])


def direct_correction(bits):
    h = q = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


materialized_nodes = tuple(i for i, n in enumerate(nodes) if n["q"] <= MATERIALIZE_MAX)
materialized_checks = 0
for i in materialized_nodes:
    node = nodes[i]
    bits = materialize(i)
    assert len(bits) == node["q"]
    assert sum(bits) == node["p"]
    h, q, C = direct_correction(bits)
    assert h == node["q"] and q == node["p"]
    for K in K_VALUES:
        assert C % (1 << K) == CMOD[K][i]
        materialized_checks += 1

assert len(materialized_nodes) == 45
assert sum(nodes[i]["q"] for i in materialized_nodes) == 457_063
assert materialized_checks == len(materialized_nodes) * len(K_VALUES)


# ---------------------------------------------------------------------------
# 3. Canonical low-residue recovery, independently checked on small nodes.
# ---------------------------------------------------------------------------

def canonical_residue_mod(Cmod: int, ones: int, K: int) -> int:
    mod = 1 << K
    three = pow(3, ones, mod)
    return (-Cmod * pow(three, -1, mod)) % mod


def T(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def orbit_bits(x: int, h: int):
    out = []
    for _ in range(h):
        out.append(x & 1)
        x = T(x)
    return tuple(out)


residue_checks = 0
for i in materialized_nodes:
    h = nodes[i]["q"]
    if h > 4096:
        continue
    bits = materialize(i)
    _, q, C = direct_correction(bits)
    mod_h = 1 << h
    r_exact = (-C * pow(pow(3, q, mod_h), -1, mod_h)) % mod_h
    assert orbit_bits(r_exact, h) == bits
    for K in K_VALUES:
        if K > h:
            continue
        rK = canonical_residue_mod(CMOD[K][i], q, K)
        assert r_exact % (1 << K) == rK
        residue_checks += 1


# ---------------------------------------------------------------------------
# 4. Exact target-aware jump for the gigantic threshold word W_th = U L^9.
# ---------------------------------------------------------------------------
# Existing Christoffel envelope identity:
#   |U|=|L|=J0, ones(U)=R0+1, C(U)=C(L)+3^R0.
# Hence W_th has length T0 and J_ODD odd symbols.  Work only modulo 2^K.

def compose_mod(Cu: int, hu: int, Cv: int, qv: int, K: int) -> int:
    mod = 1 << K
    return (pow(3, qv, mod) * Cu + pow(2, hu, mod) * Cv) % mod


def threshold_word_cmod(K: int) -> int:
    mod = 1 << K
    CL = CMOD[K][root]
    CU = (CL + pow(3, R0, mod)) % mod
    C = CU
    h = J0
    q = R0 + 1
    for _ in range(9):
        C = compose_mod(C, h, CL, R0, K)
        h += J0
        q += R0
    assert h == T0 and q == J_ODD
    return C


def threshold_requirements(nmax: int):
    req = [0]
    p2 = p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        req.append(k)
    return req


# Test every dyadic resolution through 128, not only the cached K_VALUES.
target_projection_checks = 0
matching_depths = []
for K in range(1, 129):
    table = CMOD[K] if K in CMOD else build_cmod_table(K)
    mod = 1 << K
    CL = table[root]
    CU = (CL + pow(3, R0, mod)) % mod
    CW = CU
    h = J0
    q = R0 + 1
    for _ in range(9):
        CW = compose_mod(CW, h, CL, R0, K)
        h += J0
        q += R0
    rW = canonical_residue_mod(CW, J_ODD, K)
    if rW == X_TH % mod:
        matching_depths.append(K)
    target_projection_checks += 1

assert matching_depths == list(range(1, 75))

# Independent direct orbit audit at the finite physical target X_TH:
# it follows the threshold parity word for 74 steps and first differs at
# zero-based position 74 (the 75th parity symbol).
REQ = threshold_requirements(80)
TH = tuple(REQ[n + 1] - REQ[n] for n in range(80))
x_bits_75 = orbit_bits(X_TH, 75)
assert x_bits_75[:74] == TH[:74]
assert x_bits_75[74] == 0 and TH[74] == 1


# ---------------------------------------------------------------------------
# 5. Audit the cost of incorrectly internalizing the absolute phase h.
# ---------------------------------------------------------------------------
# Count occurrences in the fully expanded binary parse tree of L without
# actually expanding it.  Every occurrence of an internal node contributes
# one occurrence of each child.  Since the final parse tree has J0 leaves, it
# must have J0-1 internal occurrences; this is checked from the DAG exactly.
occ = [0] * len(nodes)
occ[root] = 1
for i in range(root, -1, -1):
    node = nodes[i]
    if node["left"] is not None:
        occ[node["left"]] += occ[i]
        occ[node["right"]] += occ[i]

leaf_placements = occ[0] + occ[1]
total_node_placements = sum(occ)
assert occ[0] == J0 - R0
assert occ[1] == R0
assert leaf_placements == J0
assert total_node_placements == 2 * J0 - 1


print("PASS A0 s=1 Route-B Christoffel modular jump-state certificate")
print("dag_nodes", len(nodes))
print("dag_internal_nodes", sum(n["left"] is not None for n in nodes))
print("root_length", nodes[root]["q"])
print("root_ones", nodes[root]["p"])
print("K_values", K_VALUES)
print("parent_composition_checks", parent_composition_checks)
print("projection_consistency_checks", projection_consistency_checks)
print("materialized_nodes", len(materialized_nodes))
print("materialized_total_bits", sum(nodes[i]["q"] for i in materialized_nodes))
print("materialized_mod_checks", materialized_checks)
print("small_node_residue_checks", residue_checks)
print("target_projection_checks", target_projection_checks)
print("target_match_depth", max(matching_depths))
print("target_first_mismatch_position_zero_based", 74)
print("base_block_leaf_phase_placements", leaf_placements)
print("base_block_total_node_phase_placements", total_node_placements)
print("formation_audit", "parent intrinsic correction state is formed from child states + boundary metadata")
print("axis_audit", "absolute ballot phase h is an external placement axis; naive node+h internalization destroys DAG compression")
print("status", "EXACT modular correction jump CLOSED; compressed phase-ballot/right-congruence decoder remains OPEN")
