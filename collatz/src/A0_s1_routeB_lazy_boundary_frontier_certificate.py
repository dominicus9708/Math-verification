#!/usr/bin/env python3
"""Exact lazy boundary-frontier decoder for A0 s=1 Route-B.

The dual-adic localization theorem gives, for W = U V,

    D_K(W) = D_K(U)  if K <= h(U),
    E_L(W) = E_L(V)  if L <= q(V).

A decoder should therefore descend only while the selected child still has
enough intrinsic capacity to carry the full requested resolution.  The first
node where the next child is too small is the exact boundary frontier.

This script certifies that:
  * every left/start dyadic constraint is preserved along the legal left path;
  * every right/end ternary constraint is preserved along the legal right path;
  * descent stops before resolution would be truncated;
  * the gigantic base block L exposes its K=27 and L=28 coordinates on tiny
    frontier nodes (length 27 and length 84 respectively).

A matching pair of boundary projections is still only a necessary boundary
compatibility condition.  It is not correction-language membership.
"""

from math import gcd

J0 = 10_439_860_591
R0 = 6_586_818_670

K_VALUES = (1, 2, 4, 8, 16, 24, 27, 32, 39, 64)
L_VALUES = (1, 2, 4, 8, 16, 24, 28, 32, 47)


def build_stern_brocot_dag(p, q):
    assert 0 <= p <= q and gcd(p, q) == 1
    nodes = [
        {"p": 0, "q": 1, "left": None, "right": None},
        {"p": 1, "q": 1, "left": None, "right": None},
    ]
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


def build_cmod_table(mod):
    out = []
    for node in nodes:
        if node["left"] is None:
            C = node["p"] % mod
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


def start_dyadic(i, K):
    node = nodes[i]
    assert 1 <= K <= node["q"]
    mod = 1 << K
    return (
        -CDYAD[K][i] * pow(pow(3, node["p"], mod), -1, mod)
    ) % mod


def end_ternary(i, L):
    node = nodes[i]
    assert 1 <= L <= node["p"]
    mod = pow(3, L)
    return (
        CTERN[L][i] * pow(pow(2, node["q"], mod), -1, mod)
    ) % mod


def left_frontier(i, K):
    """Deepest legal left descendant that still carries all K dyadic bits."""
    assert 1 <= K <= nodes[i]["q"]
    path = [i]
    while nodes[i]["left"] is not None:
        li = nodes[i]["left"]
        if K > nodes[li]["q"]:
            break
        i = li
        path.append(i)
    return i, tuple(path)


def right_frontier(i, L):
    """Deepest legal right descendant that still carries all L ternary trits."""
    assert 1 <= L <= nodes[i]["p"]
    path = [i]
    while nodes[i]["right"] is not None:
        ri = nodes[i]["right"]
        if L > nodes[ri]["p"]:
            break
        i = ri
        path.append(i)
    return i, tuple(path)


left_frontier_checks = 0
right_frontier_checks = 0
left_minimality_checks = 0
right_minimality_checks = 0
left_gate_checks = 0
right_gate_checks = 0
max_left_descent = 0
max_right_descent = 0

for i, node in enumerate(nodes):
    for K in K_VALUES:
        if K > node["q"]:
            continue

        j, path = left_frontier(i, K)
        assert start_dyadic(i, K) == start_dyadic(j, K)
        left_frontier_checks += 1

        # The frontier retains the entire requested width.
        assert K <= nodes[j]["q"]
        # But its next left child, if any, cannot retain all K bits.
        if nodes[j]["left"] is not None:
            assert nodes[nodes[j]["left"]]["q"] < K
        left_minimality_checks += 1

        # Exact and deliberately wrong target residues give the same gate
        # verdict at the parent and at its frontier.  Since the residues are
        # equal, this represents all possible target values algebraically; the
        # explicit mismatch is a regression guard against inverted predicates.
        exact = start_dyadic(i, K)
        wrong = (exact + 1) % (1 << K)
        assert (start_dyadic(i, K) == exact) == (start_dyadic(j, K) == exact)
        assert (start_dyadic(i, K) == wrong) == (start_dyadic(j, K) == wrong)
        left_gate_checks += 2

        max_left_descent = max(max_left_descent, len(path) - 1)

    for L in L_VALUES:
        if L > node["p"]:
            continue

        j, path = right_frontier(i, L)
        assert end_ternary(i, L) == end_ternary(j, L)
        right_frontier_checks += 1

        assert L <= nodes[j]["p"]
        if nodes[j]["right"] is not None:
            assert nodes[nodes[j]["right"]]["p"] < L
        right_minimality_checks += 1

        exact = end_ternary(i, L)
        wrong = (exact + 1) % pow(3, L)
        assert (end_ternary(i, L) == exact) == (end_ternary(j, L) == exact)
        assert (end_ternary(i, L) == wrong) == (end_ternary(j, L) == wrong)
        right_gate_checks += 2

        max_right_descent = max(max_right_descent, len(path) - 1)


assert left_frontier_checks == 1228
assert right_frontier_checks == 1098
assert left_minimality_checks == left_frontier_checks
assert right_minimality_checks == right_frontier_checks
assert left_gate_checks == 2 * left_frontier_checks
assert right_gate_checks == 2 * right_frontier_checks
assert max_left_descent == 43
assert max_right_descent == 85


# ---------------------------------------------------------------------------
# Route-B boundary resolutions already certified by the closure-status audit.
# ---------------------------------------------------------------------------

D24_node, D24_path = left_frontier(root, 24)
D27_node, D27_path = left_frontier(root, 27)
D39_node, D39_path = left_frontier(root, 39)
E24_node, E24_path = right_frontier(root, 24)
E28_node, E28_path = right_frontier(root, 28)

assert D24_node == 8
assert D27_node == 8
assert D39_node == 9
assert E24_node == 11
assert E28_node == 11

assert nodes[D27_node]["q"] == 27
assert nodes[D27_node]["p"] == 17
assert nodes[E28_node]["q"] == 84
assert nodes[E28_node]["p"] == 53

assert len(D27_path) - 1 == 39
assert len(E28_path) - 1 == 81

# Exact root/frontier residues.
assert start_dyadic(root, 27) == start_dyadic(D27_node, 27)
assert end_ternary(root, 28) == end_ternary(E28_node, 28)

ROOT_D27 = start_dyadic(root, 27)
ROOT_E28 = end_ternary(root, 28)

assert ROOT_D27 == 87_757_810
assert ROOT_E28 == 2_158_791_402_581


print("PASS A0 s=1 Route-B exact lazy boundary-frontier certificate")
print("dag_nodes", len(nodes))
print("left_frontier_checks", left_frontier_checks)
print("right_frontier_checks", right_frontier_checks)
print("left_minimality_checks", left_minimality_checks)
print("right_minimality_checks", right_minimality_checks)
print("left_gate_checks", left_gate_checks)
print("right_gate_checks", right_gate_checks)
print("max_left_descent", max_left_descent)
print("max_right_descent", max_right_descent)
print(
    "D27_frontier",
    {
        "node": D27_node,
        "length": nodes[D27_node]["q"],
        "ones": nodes[D27_node]["p"],
        "descent": len(D27_path) - 1,
        "residue": ROOT_D27,
    },
)
print(
    "E28_frontier",
    {
        "node": E28_node,
        "length": nodes[E28_node]["q"],
        "ones": nodes[E28_node]["p"],
        "descent": len(E28_path) - 1,
        "residue": ROOT_E28,
    },
)
print(
    "D39_frontier",
    {
        "node": D39_node,
        "length": nodes[D39_node]["q"],
        "ones": nodes[D39_node]["p"],
        "descent": len(D39_path) - 1,
    },
)
print(
    "E24_frontier",
    {
        "node": E24_node,
        "length": nodes[E24_node]["q"],
        "ones": nodes[E24_node]["p"],
        "descent": len(E24_path) - 1,
    },
)
print(
    "formation_audit",
    "decoder descends only through a child that retains the complete requested boundary coordinate",
)
print(
    "axis_audit",
    "start and end constraints travel on opposite directed boundary axes; unresolved width is retained at the parent frontier",
)
print(
    "dsd_audit",
    "localized mismatch pruning is exact; matching frontiers remain necessary rather than sufficient for long membership",
)
print(
    "status",
    "G4 lazy boundary descent primitive CLOSED; target-specific interior/right-congruence decoder remains OPEN",
)
