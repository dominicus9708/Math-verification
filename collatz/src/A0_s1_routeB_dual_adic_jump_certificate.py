#!/usr/bin/env python3
"""Exact dual-adic localization for the A0 s=1 Route-B block decoder.

For a parity block W of length h and q odd symbols,

    2^h Y = 3^q X + C(W).

Define the start-facing dyadic projection

    D_K(W) = -C(W) * (3^q)^(-1) mod 2^K,   1 <= K <= h,

and the end-facing ternary projection

    E_L(W) = C(W) * (2^h)^(-1) mod 3^L,    1 <= L <= q.

For W = U V, correction composition gives

    C(UV) = 3^q(V) C(U) + 2^h(U) C(V).

Therefore the two boundary coordinates localize in opposite directions:

    D_K(UV) = D_K(U)  if K <= h(U),
    E_L(UV) = E_L(V)  if L <= q(V).

The first identity says low dyadic information at the start ignores the suffix
once the left block is at least K symbols long.  The second says low ternary
information at the end ignores the prefix once the right block contains at
least L odd symbols.

This certificate checks the identities independently in three ways:
  1. exhaustive arbitrary parity words through depth 9;
  2. actual Collatz channel lifts of those words;
  3. every parent of the 129-node Christoffel/Stern-Brocot DAG at several
     dyadic and ternary resolutions, including the repository exposure widths
     27 dyadic bits and 28 ternary trits.

Scope:
  * exact dual-adic block localization: CLOSED;
  * exact compatibility with compressed Christoffel composition: CLOSED;
  * target-aware recursive/right-congruence decoder: OPEN.
"""

from functools import lru_cache
from math import gcd

MAX_DEPTH = 9

J0 = 10_439_860_591
R0 = 6_586_818_670

# Include the boundary resolutions currently exposed elsewhere in the Route-B
# audit (27 dyadic + 28 ternary), together with nearby regression resolutions.
K_VALUES = (1, 2, 4, 8, 16, 24, 27, 32, 39, 64)
L_VALUES = (1, 2, 4, 8, 16, 24, 28, 32, 47)
MATERIALIZE_MAX = 100_000


def direct_summary(bits):
    """Return (length, odd_count, correction) for a chronological parity word."""
    h = q = C = 0
    for bit in bits:
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


def compose(A, B):
    """Exact correction summary of concatenation A B."""
    hu, qu, Cu = A
    hv, qv, Cv = B
    return (
        hu + hv,
        qu + qv,
        pow(3, qv) * Cu + (1 << hu) * Cv,
    )


def start_dyadic(A, K):
    """D_K: canonical start/cylinder residue modulo 2^K."""
    h, q, C = A
    assert 1 <= K <= h
    mod = 1 << K
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def end_ternary(A, L):
    """E_L: endpoint residue modulo 3^L, independent of incoming X."""
    h, q, C = A
    assert 1 <= L <= q
    mod = pow(3, L)
    return (C * pow(pow(2, h, mod), -1, mod)) % mod


def T(x):
    return (3 * x + 1) // 2 if x & 1 else x // 2


def orbit_bits_and_endpoint(x, h):
    bits = []
    for _ in range(h):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits), x


# ---------------------------------------------------------------------------
# 1. Exhaustive arbitrary-word proof regression.
# ---------------------------------------------------------------------------

word_count = 0
summary_composition_checks = 0
dyadic_projection_checks = 0
ternary_projection_checks = 0
dyadic_localization_checks = 0
ternary_localization_checks = 0
actual_dyadic_lift_checks = 0
actual_ternary_lift_checks = 0
actual_orbit_checks = 0

for h in range(1, MAX_DEPTH + 1):
    for address in range(1 << h):
        # Low address bit is the first chronological parity symbol.  This is
        # only an exhaustive enumeration convention; no address theorem is
        # assumed here.
        bits = tuple((address >> i) & 1 for i in range(h))
        W = direct_summary(bits)
        _, qW, CW = W
        word_count += 1

        # Projective consistency at both adic ends.
        for K in range(1, h):
            assert start_dyadic(W, K + 1) % (1 << K) == start_dyadic(W, K)
            dyadic_projection_checks += 1

        for L in range(1, qW):
            assert end_ternary(W, L + 1) % pow(3, L) == end_ternary(W, L)
            ternary_projection_checks += 1

        # Canonical cylinder start and the corresponding exact endpoint.
        rW = start_dyadic(W, h)
        yW = (pow(3, qW) * rW + CW) // (1 << h)
        assert (pow(3, qW) * rW + CW) % (1 << h) == 0

        # Use a positive representative in the same 2^h cylinder to check the
        # parity word against the actual Collatz map independently.
        test_bits, test_y = orbit_bits_and_endpoint(rW + (1 << h), h)
        assert test_bits == bits
        assert test_y == yW + pow(3, qW)
        actual_orbit_checks += 1

        for split in range(1, h):
            U = direct_summary(bits[:split])
            V = direct_summary(bits[split:])
            assert compose(U, V) == W
            summary_composition_checks += 1

            # Left/start localization.
            for K in range(1, U[0] + 1):
                DK = start_dyadic(U, K)
                assert start_dyadic(W, K) == DK
                dyadic_localization_checks += 1

                # Every member of the full cylinder has the same low K bits.
                for lift in range(4):
                    X = rW + (1 << h) * lift
                    assert X % (1 << K) == DK
                    actual_dyadic_lift_checks += 1

            # Right/end localization.  No canonical start for V is required:
            # q(V) >= L makes the incoming 3^q(V) term vanish modulo 3^L.
            for L in range(1, V[1] + 1):
                EL = end_ternary(V, L)
                assert end_ternary(W, L) == EL
                ternary_localization_checks += 1

                for lift in range(4):
                    Y = yW + pow(3, qW) * lift
                    assert Y % pow(3, L) == EL
                    actual_ternary_lift_checks += 1


assert word_count == sum(1 << h for h in range(1, MAX_DEPTH + 1))
assert word_count == 1022
assert summary_composition_checks == 7172
assert dyadic_projection_checks == 7172
assert ternary_projection_checks == 3084
assert dyadic_localization_checks == 29692
assert ternary_localization_checks == 14846
assert actual_dyadic_lift_checks == 118768
assert actual_ternary_lift_checks == 59384
assert actual_orbit_checks == 1022


# ---------------------------------------------------------------------------
# 2. 129-node Christoffel DAG: dual modular correction tables.
# ---------------------------------------------------------------------------

def build_stern_brocot_dag(p, q):
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


def build_cmod_table(mod):
    out = []
    for node in nodes:
        if node["left"] is None:
            C = node["p"] % mod  # leaf 0 -> 0, leaf 1 -> 1
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


CDYAD = {K: build_cmod_table(1 << K) for K in K_VALUES}
CTERN = {L: build_cmod_table(pow(3, L)) for L in L_VALUES}


def dag_start_dyadic(i, K):
    mod = 1 << K
    q = nodes[i]["p"]
    C = CDYAD[K][i]
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def dag_end_ternary(i, L):
    mod = pow(3, L)
    h = nodes[i]["q"]
    C = CTERN[L][i]
    return (C * pow(pow(2, h, mod), -1, mod)) % mod


dag_dyadic_parent_checks = 0
dag_ternary_parent_checks = 0
dag_left_localization_checks = 0
dag_right_localization_checks = 0

for K in K_VALUES:
    mod = 1 << K
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        ri = node["right"]
        left = nodes[li]
        right = nodes[ri]
        recomposed = (
            pow(3, right["p"], mod) * CDYAD[K][li]
            + pow(2, left["q"], mod) * CDYAD[K][ri]
        ) % mod
        assert recomposed == CDYAD[K][i]
        dag_dyadic_parent_checks += 1

        if K <= left["q"]:
            assert dag_start_dyadic(i, K) == dag_start_dyadic(li, K)
            dag_left_localization_checks += 1

for L in L_VALUES:
    mod = pow(3, L)
    for i, node in enumerate(nodes):
        if node["left"] is None:
            continue
        li = node["left"]
        ri = node["right"]
        left = nodes[li]
        right = nodes[ri]
        recomposed = (
            pow(3, right["p"], mod) * CTERN[L][li]
            + pow(2, left["q"], mod) * CTERN[L][ri]
        ) % mod
        assert recomposed == CTERN[L][i]
        dag_ternary_parent_checks += 1

        if L <= right["p"]:
            assert dag_end_ternary(i, L) == dag_end_ternary(ri, L)
            dag_right_localization_checks += 1


assert dag_dyadic_parent_checks == 127 * len(K_VALUES)
assert dag_ternary_parent_checks == 127 * len(L_VALUES)
assert dag_left_localization_checks == 1216
assert dag_right_localization_checks == 1080


# ---------------------------------------------------------------------------
# 3. Direct materialization regression on short DAG nodes.
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def materialize(i):
    node = nodes[i]
    if node["left"] is None:
        return (node["p"],)
    return materialize(node["left"]) + materialize(node["right"])


materialized_nodes = tuple(
    i for i, node in enumerate(nodes) if node["q"] <= MATERIALIZE_MAX
)
materialized_dyadic_checks = 0
materialized_ternary_checks = 0

for i in materialized_nodes:
    bits = materialize(i)
    h, q, C = direct_summary(bits)
    assert h == nodes[i]["q"]
    assert q == nodes[i]["p"]

    for K in K_VALUES:
        assert C % (1 << K) == CDYAD[K][i]
        materialized_dyadic_checks += 1

    for L in L_VALUES:
        assert C % pow(3, L) == CTERN[L][i]
        materialized_ternary_checks += 1


assert len(materialized_nodes) == 45
assert sum(nodes[i]["q"] for i in materialized_nodes) == 457_063
assert materialized_dyadic_checks == 45 * len(K_VALUES)
assert materialized_ternary_checks == 45 * len(L_VALUES)


# ---------------------------------------------------------------------------
# 4. Width-specific audit: the 27 x 28 boundary resolutions are valid exact
#    coordinates of the same block state.  This does NOT by itself prove that
#    any particular checkpoint or bridge belongs to the correction language.
# ---------------------------------------------------------------------------

root_D27 = dag_start_dyadic(root, 27)
root_E28 = dag_end_ternary(root, 28)

assert 0 <= root_D27 < (1 << 27)
assert 0 <= root_E28 < pow(3, 28)


print("PASS A0 s=1 Route-B exact dual-adic jump certificate")
print("arbitrary_word_max_depth", MAX_DEPTH)
print("arbitrary_words", word_count)
print("summary_composition_checks", summary_composition_checks)
print("dyadic_projection_checks", dyadic_projection_checks)
print("ternary_projection_checks", ternary_projection_checks)
print("dyadic_localization_checks", dyadic_localization_checks)
print("ternary_localization_checks", ternary_localization_checks)
print("actual_orbit_checks", actual_orbit_checks)
print("actual_dyadic_lift_checks", actual_dyadic_lift_checks)
print("actual_ternary_lift_checks", actual_ternary_lift_checks)
print("dag_nodes", len(nodes))
print("dag_dyadic_parent_checks", dag_dyadic_parent_checks)
print("dag_ternary_parent_checks", dag_ternary_parent_checks)
print("dag_left_localization_checks", dag_left_localization_checks)
print("dag_right_localization_checks", dag_right_localization_checks)
print("materialized_nodes", len(materialized_nodes))
print("materialized_total_bits", sum(nodes[i]["q"] for i in materialized_nodes))
print("materialized_dyadic_checks", materialized_dyadic_checks)
print("materialized_ternary_checks", materialized_ternary_checks)
print("checkpoint_resolution_pair", (27, 28))
print("root_D27", root_D27)
print("root_E28", root_E28)
print(
    "formation_audit",
    "dual boundary state is formed from exact child correction summaries + concatenation boundary",
)
print(
    "axis_audit",
    "dyadic start and ternary end are opposite-facing boundary coordinates, not an absolute placement axis",
)
print(
    "dsd_audit",
    "exact localization is closed; target-specific long membership/right-congruence closure remains open",
)
print(
    "status",
    "EXACT dual-adic block localization CLOSED; G4 target-aware lazy decoder remains OPEN",
)
