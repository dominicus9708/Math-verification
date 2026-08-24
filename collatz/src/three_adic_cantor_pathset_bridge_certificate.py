# Exact finite regression certificate for the 3-adic path-set bridge used in
# the current Collatz Stage-4 audit.
#
# This script does NOT prove the missing selector-repair implication.  It
# certifies the arithmetic pieces that would be used once that implication is
# established:
#   * carry automata for intersections of multiplicative translates of the
#     3-adic Cantor set (digits 0/1);
#   * exact zero-entropy examples C(1,8) and C(1,4,16);
#   * Fibonacci automaton for C(1,4);
#   * Beatty plateau-start gaps 2 or 3, with no consecutive 2-gaps, on a large
#     exact regression range;
#   * the exact common-depth inverse-dyadic relation
#         lambda' == 2^g lambda (mod 3^q).
#
# The finite automaton construction is the elementary carry construction used
# in the 3-adic path-set literature of Abram--Lagarias.

from collections import deque, defaultdict


def carry_automaton(multipliers):
    """Reachable carry graph for x and M_i x all having ternary digits 0/1."""
    start = tuple(0 for _ in multipliers)
    states = [start]
    index = {start: 0}
    edges = defaultdict(list)
    work = deque([start])

    while work:
        state = work.popleft()
        i = index[state]
        for digit in (0, 1):
            nxt = []
            ok = True
            for M, carry in zip(multipliers, state):
                value = M * digit + carry
                out_digit = value % 3
                if out_digit not in (0, 1):
                    ok = False
                    break
                nxt.append((value - out_digit) // 3)
            if not ok:
                continue
            nxt = tuple(nxt)
            if nxt not in index:
                index[nxt] = len(states)
                states.append(nxt)
                work.append(nxt)
            edges[i].append((index[nxt], digit))
    return states, edges


def edge_matrix(states, edges):
    A = [[0] * len(states) for _ in states]
    for i, out in edges.items():
        for j, _ in out:
            A[i][j] += 1
    return A


# C(1,4): Fibonacci graph, Perron root phi, dimension log_3(phi).
st, ed = carry_automaton((1, 4))
A = edge_matrix(st, ed)
assert st == [(0, 0), (0, 1)]
assert A == [[1, 1], [1, 0]]

# If M == 2 (mod 3), every nonzero x in the 0/1 Cantor set has its least
# nonzero ternary digit changed from 1 to 2 in Mx.  M=8 is the first relevant
# power-of-two example: the only infinite path is x=0.
st8, ed8 = carry_automaton((1, 8))
assert st8 == [(0, 0)]
assert edge_matrix(st8, ed8) == [[1]]

# Two even power-of-two constraints can already collapse the entropy to zero.
# The reachable graph has one recurrent zero loop and one terminal one-edge
# state, hence spectral radius exactly 1.
st416, ed416 = carry_automaton((1, 4, 16))
assert st416 == [(0, 0, 0), (0, 1, 5)]
assert edge_matrix(st416, ed416) == [[1, 1], [0, 0]]

# A published nontrivial example: C(1,4,256) has ten reachable carry states.
# (Its essential characteristic factor is x^6-x^5-1; the graph-size check is
# enough here to guard the construction without a symbolic algebra dependency.)
st4256, ed4256 = carry_automaton((1, 4, 256))
assert len(st4256) == 10


def barriers(H):
    out = [0] * (H + 1)
    p2 = 1
    p3 = 1
    q = 0
    for j in range(1, H + 1):
        p2 *= 2
        while p3 < p2:
            p3 *= 3
            q += 1
        out[j] = q
    return out


# Exact integer regression of the plateau-gap theorem.  The symbolic proof is:
#   1/2 < alpha=log_3 2 < 2/3, so no 00 increments and no 111 increments;
#   alpha > 3/5, so 01010 cannot be a length-5 factor.
# Hence plateau-start gaps are 2 or 3 and two 2-gaps cannot be consecutive.
B = barriers(10000)
P = [j for j in range(9999) if B[j + 1] == B[j]]
gaps = [b - a for a, b in zip(P, P[1:])]
assert set(gaps) == {2, 3}
assert all(not (gaps[i] == gaps[i + 1] == 2) for i in range(len(gaps) - 1))


def inv_mod(a, m):
    return pow(a, -1, m)


# Common-depth inverse-dyadic relation.  If remaining dyadic depths differ by
# g, then -2^{-m'} = 2^g(-2^{-m}) in every common 3-adic truncation.
for q in range(1, 15):
    mod = 3 ** q
    for m in range(5, 30):
        lam = (-inv_mod(pow(2, m, mod), mod)) % mod
        for g in (2, 3):
            if m <= g:
                continue
            mp = m - g
            lamp = (-inv_mod(pow(2, mp, mod), mod)) % mod
            assert lamp == (pow(2, g, mod) * lam) % mod

print("3-adic Cantor path-set bridge certificate: PASS")
