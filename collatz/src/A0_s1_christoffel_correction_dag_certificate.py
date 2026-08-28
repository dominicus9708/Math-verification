#!/usr/bin/env python3
"""Exact Stern-Brocot/Christoffel DAG certificate for the A0 s=1 base block.

The ten-block certificate reduces the threshold correction to K=C(L), where

    L[r] = floor((r+1)R0/J0) - floor(r R0/J0),

with coprime
    R0=6_586_818_670, J0=10_439_860_591.

For Farey neighbours a/b < c/d with bc-ad=1, the lower mechanical
(Christoffel) word at their mediant satisfies

    L_{a+c,b+d} = L_{a,b} L_{c,d}.

Starting from 0/1 -> "0" and 1/1 -> "1", the Stern-Brocot path therefore
constructs L exactly as a concatenation DAG.  The target here needs only
127 mediant nodes rather than J0 individual bits.

Each DAG node carries the exact Collatz correction transfer

    C(uv) = 3^{q(v)} C(u) + 2^{|u|} C(v).

The script intentionally stores this as an arithmetic circuit; it does not
materialize C(L), whose binary size is enormous.

The finite small-denominator regressions check the mechanical-word and
correction recurrences independently of the target-size proof.
"""

from math import gcd

R0 = 6_586_818_670
J0 = 10_439_860_591


def lower_mechanical_word(p, q):
    assert 0 <= p <= q and gcd(p, q) == 1
    return tuple(((i + 1) * p // q) - (i * p // q) for i in range(q))


def correction_from_bits(bits):
    positions = [i for i, b in enumerate(bits) if b]
    q = len(positions)
    return sum((3 ** (q - r - 1)) * (1 << a)
               for r, a in enumerate(positions))


def build_stern_brocot_dag(p, q):
    """Return nodes and root for the reduced fraction p/q in [0,1].

    A node is
        {"p": ones, "q": length, "left": id|None, "right": id|None}.
    For non-base nodes, its exact word is word(left)+word(right).
    """
    assert 0 <= p <= q and gcd(p, q) == 1

    nodes = [
        {"p": 0, "q": 1, "left": None, "right": None},  # "0"
        {"p": 1, "q": 1, "left": None, "right": None},  # "1"
    ]

    if p == 0:
        return nodes, 0
    if p == q:
        return nodes, 1

    left = (0, 1, 0)
    right = (1, 1, 1)

    while True:
        # Farey-neighbour invariant.
        assert left[1] * right[0] - left[0] * right[1] == 1

        mp = left[0] + right[0]
        mq = left[1] + right[1]
        mid_id = len(nodes)
        nodes.append(
            {"p": mp, "q": mq, "left": left[2], "right": right[2]}
        )

        cmp = p * mq - mp * q
        if cmp == 0:
            assert (mp, mq) == (p, q)
            return nodes, mid_id
        if cmp < 0:
            right = (mp, mq, mid_id)
        else:
            left = (mp, mq, mid_id)


def expand_small(nodes, root):
    memo = {}

    def rec(i):
        if i in memo:
            return memo[i]
        n = nodes[i]
        if n["left"] is None:
            w = (0,) if n["p"] == 0 else (1,)
        else:
            w = rec(n["left"]) + rec(n["right"])
        memo[i] = w
        return w

    return rec(root)


def correction_dag_small(nodes, root):
    """Materialize only for the small regression cases."""
    memo = {}

    def rec(i):
        if i in memo:
            return memo[i]
        n = nodes[i]
        if n["left"] is None:
            C = 0 if n["p"] == 0 else 1
        else:
            L = nodes[n["left"]]
            R = nodes[n["right"]]
            C_left = rec(n["left"])
            C_right = rec(n["right"])
            C = (3 ** R["p"]) * C_left + (1 << L["q"]) * C_right
        memo[i] = C
        return C

    return rec(root)


# Exhaustive small-denominator regression of the Farey concatenation DAG
# and the Collatz correction transfer.
for q in range(1, 41):
    for p in range(q + 1):
        if gcd(p, q) != 1:
            continue
        nodes, root = build_stern_brocot_dag(p, q)
        word = expand_small(nodes, root)
        assert word == lower_mechanical_word(p, q)
        assert len(word) == q
        assert sum(word) == p
        assert correction_dag_small(nodes, root) == correction_from_bits(word)

# Target-size exact DAG: no target word or correction integer is expanded.
nodes, root = build_stern_brocot_dag(R0, J0)
root_node = nodes[root]

assert root_node["p"] == R0
assert root_node["q"] == J0
assert len(nodes) == 129
assert root == 128

# Every non-base node is a legal Farey mediant and its length/odd count
# are exactly the sums of its children.
for i, n in enumerate(nodes[2:], start=2):
    l = nodes[n["left"]]
    r = nodes[n["right"]]
    assert l["q"] * r["p"] - l["p"] * r["q"] == 1
    assert n["p"] == l["p"] + r["p"]
    assert n["q"] == l["q"] + r["q"]

print("PASS A0 s=1 Christoffel correction DAG certificate")
print("target_slope", f"{R0}/{J0}")
print("target_length", J0)
print("target_odd_count", R0)
print("dag_nodes_total", len(nodes))
print("dag_mediant_nodes", len(nodes) - 2)
print("root_id", root)
print("word_expansion", "not materialized")
print("correction_expansion", "not materialized")
print("node_transfer", "C(uv)=3^q(v)C(u)+2^|u|C(v)")
