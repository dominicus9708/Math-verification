#!/usr/bin/env python3
"""Exact anchored Christoffel/Farey DAG certificate for the first resonance.

The first-resonance mechanical gap bits are
    m_n = floor((n+1)P/Q) - floor(nP/Q),
with P=A-Q and gcd(P,Q)=1.

For every reduced 0<p<q, define the lower Farey parent by
    q_- = p^{-1} mod q,
    p_- = (p*q_- - 1)/q,
and the upper parent by subtraction.  The accompanying note proves
algebraically that the anchored lower mechanical word factors as
    C(p,q) = C(p_-,q_-) C(p_+,q_+).

This script certifies the entire first-resonance factor DAG without ever
materializing the 72-billion-letter root word.  Small nodes are materialized
only as exact regressions of the factorization identity.
"""

from functools import lru_cache
from math import gcd

A = 114_208_327_604
Q = 72_057_431_991
P = A - Q


def parents(p: int, q: int):
    assert 0 < p < q and gcd(p, q) == 1
    qm = pow(p, -1, q)
    pm = (p * qm - 1) // q
    pp, qp = p - pm, q - qm

    assert pm * q < p * qm                 # p_-/q_- < p/q
    assert p * qp < pp * q                 # p/q < p_+/q_+
    assert p * qm - pm * q == 1
    assert pp * q - p * qp == 1
    assert pm + pp == p and qm + qp == q
    assert gcd(pm, qm) == 1 and gcd(pp, qp) == 1
    return (pm, qm), (pp, qp)


def word(p: int, q: int) -> str:
    return ''.join(
        str(((n + 1) * p) // q - (n * p) // q)
        for n in range(q)
    )


nodes = {}


def build(p: int, q: int):
    key = (p, q)
    if key in nodes:
        return
    if (p, q) in ((0, 1), (1, 1)):
        nodes[key] = None
        return
    lo, hi = parents(p, q)
    nodes[key] = (lo, hi)
    build(*lo)
    build(*hi)


@lru_cache(None)
def depth(node):
    ch = nodes[node]
    if ch is None:
        return 0
    return 1 + max(depth(ch[0]), depth(ch[1]))


@lru_cache(None)
def expanded_length(node):
    ch = nodes[node]
    if ch is None:
        return 1
    return expanded_length(ch[0]) + expanded_length(ch[1])


@lru_cache(None)
def expanded_ones(node):
    p, q = node
    ch = nodes[node]
    if ch is None:
        return p
    return expanded_ones(ch[0]) + expanded_ones(ch[1])


def main() -> None:
    assert gcd(P, Q) == 1
    build(P, Q)

    # The full 72-billion-letter word is represented by only 138 distinct DAG
    # nodes (including the two one-letter bases).
    assert len(nodes) == 138
    assert expanded_length((P, Q)) == Q
    assert expanded_ones((P, Q)) == P
    assert depth((P, Q)) == 136

    root_lo, root_hi = nodes[(P, Q)]
    assert root_lo == (38_297_853_692, 65_470_613_321)
    assert root_hi == (3_853_041_921, 6_586_818_670)

    # Every internal DAG node preserves length and number of ones under the
    # ordered Farey-parent factorization.
    for (p, q), ch in nodes.items():
        if ch is None:
            assert (p, q) in ((0, 1), (1, 1))
            continue
        lo, hi = ch
        assert lo[0] + hi[0] == p
        assert lo[1] + hi[1] == q

    # Exact materialized regressions for all small nodes.  These check the
    # anchored order C_low C_high, not merely conjugacy.
    checked = 0
    for (p, q), ch in nodes.items():
        if ch is None or q > 10_000:
            continue
        lo, hi = ch
        assert word(p, q) == word(*lo) + word(*hi)
        checked += 1
    assert checked > 20

    # The mechanical Collatz gap is g=1+m_n, so this same DAG is an exact
    # anchored grammar for the first-resonance gap word after relabel 0->1,
    # 1->2.
    print("PASS first-resonance anchored Christoffel DAG")
    print("P", P)
    print("Q", Q)
    print("unique_DAG_nodes", len(nodes))
    print("DAG_depth", depth((P, Q)))
    print("root_lower_parent", root_lo)
    print("root_upper_parent", root_hi)
    print("small_exact_factor_regressions", checked)
    print("expanded_length", expanded_length((P, Q)))
    print("expanded_ones", expanded_ones((P, Q)))


if __name__ == "__main__":
    main()
