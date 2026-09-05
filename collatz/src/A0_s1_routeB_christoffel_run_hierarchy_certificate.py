#!/usr/bin/env python3
"""Christoffel run-hierarchy and scale obstruction for A0 s=1 Route-B.

Fixed low-resolution source/endpoint residues are exact but non-separating.
This certificate measures why, then replaces the failed fixed-resolution
quotient by the natural Stern-Brocot run hierarchy.

For the target slope R0/J0, the 127 mediant nodes arise from only 20
alternating Stern-Brocot runs.  The continued fraction has 22 coefficients.
Because the already-certified Route-B block state composes associatively,
a whole run can be evaluated by block powering instead of one mediant at a
time.

The final run has an especially sharp obstruction.  Let A be node 112 and B
node 111.  The final nodes are

    W_n = A^n B,  1 <= n <= 16,

with root W_16.  Since lcp(A,B)=|B|-1,

    lcp(W_n,W_{n-1}) = |W_{n-1}|-1.

Also W_{n-1} is an exact suffix of W_n.  Therefore:
  * no source dyadic resolution K<|W_{n-1}| distinguishes the pair;
  * no endpoint ternary resolution R<=q(W_{n-1}) distinguishes the pair.

For root vs predecessor, the first distinguishing source resolution is
K=9,809,721,694, nearly the entire block.  This proves a linear scale
obstruction for fixed-resolution boundary discrimination on this ray.

Positive result: the same family is represented by the single integer run
exponent n.  For the actual root, the exact combined state
(length, ones, C mod 2^128, ballot base minimum, ballot critical prefix)
is reconstructed from the 20-run hierarchy and agrees with the 129-node DAG.
The ballot critical prefix of every final-run W_n equals |W_{n-1}|, including
the root.  Thus the previously derived ballot critical coordinate already
points to the exact separating hierarchical cut on this run.

Formation-Axiom lens:
  low-resolution boundary projections do not reconstruct formation, while
  the run hierarchy does retain the explicit child-formation rule.

Axis-property lens:
  fixed dyadic/ternary boundary axes are non-separating; scale/hierarchy is
  a necessary structural coordinate.  It may be stored recursively as run
  data rather than as a raw absolute position.

Scope:
  * fixed-resolution boundary quotient: structurally rejected on this ray;
  * recursive run-hierarchy generation of the current target block: CLOSED;
  * target-aware universal membership/right-congruence decoder: OPEN.
"""

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd

J0 = 10_439_860_591
R0 = 6_586_818_670
K_STATE = 128
MOD = 1 << K_STATE
MATERIALIZE_MAX = 100_000

EXPECTED_CF = (
    0, 1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 16
)
EXPECTED_RUNS = (
    ("L", 1), ("R", 1), ("L", 2), ("R", 2), ("L", 3),
    ("R", 1), ("L", 5), ("R", 2), ("L", 23), ("R", 2),
    ("L", 2), ("R", 1), ("L", 1), ("R", 55), ("L", 1),
    ("R", 4), ("L", 3), ("R", 1), ("L", 1), ("R", 15),
)


def build_stern_brocot_dag(p: int, q: int):
    assert 0 <= p <= q and gcd(p, q) == 1
    nodes = [
        {"p": 0, "q": 1, "left": None, "right": None},
        {"p": 1, "q": 1, "left": None, "right": None},
    ]
    if p == 0:
        return nodes, 0

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


def continued_fraction(p: int, q: int):
    out = []
    while q:
        a = p // q
        out.append(a)
        p, q = q, p - a * q
    return tuple(out)


CF = continued_fraction(R0, J0)
assert CF == EXPECTED_CF
assert sum(CF) == 128


def stern_brocot_directions(p: int, q: int):
    left = (0, 1)
    right = (1, 1)
    directions = []
    while True:
        mp = left[0] + right[0]
        mq = left[1] + right[1]
        cmp = p * mq - mp * q
        if cmp == 0:
            return tuple(directions)
        if cmp < 0:
            directions.append("R")
            right = (mp, mq)
        else:
            directions.append("L")
            left = (mp, mq)


def run_length_encode(seq):
    if not seq:
        return ()
    out = []
    cur = seq[0]
    count = 1
    for x in seq[1:]:
        if x == cur:
            count += 1
        else:
            out.append((cur, count))
            cur = x
            count = 1
    out.append((cur, count))
    return tuple(out)


DIRECTIONS = stern_brocot_directions(R0, J0)
RUNS = run_length_encode(DIRECTIONS)
assert len(DIRECTIONS) == 126
assert RUNS == EXPECTED_RUNS
assert len(RUNS) == 20
assert sum(n for _, n in RUNS) == 126
assert tuple(n for _, n in RUNS[:-1]) == CF[2:-1]
assert RUNS[-1][1] + 1 == CF[-1]


# ---------------------------------------------------------------------------
# Exact ballot arithmetic reused independently here.
# ---------------------------------------------------------------------------
def log_bounds(z: Fraction, n: int = 90):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / (
        (2 * n + 3) * (1 - z * z)
    )
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


@lru_cache(maxsize=None)
def floor_alpha(n: int) -> int:
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi, ("insufficient log interval", n, flo, fhi)
    return flo


def phase_carry(a: int, b: int) -> int:
    c = floor_alpha(a + b) - floor_alpha(a) - floor_alpha(b)
    assert c in (0, 1)
    return c


def frac_compare(a: int, b: int) -> int:
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


def max_fractional(candidates):
    vals = [x for x in candidates if x is not None]
    if not vals:
        return None
    best = vals[0]
    for x in vals[1:]:
        if frac_compare(x, best) > 0:
            best = x
    return best


@dataclass(frozen=True)
class State:
    length: int
    ones: int
    cmod: int
    base_min: int
    critical_prefix: int | None


def compose(a: State, b: State) -> State:
    cmod = (
        pow(3, b.ones, MOD) * a.cmod
        + pow(2, a.length, MOD) * b.cmod
    ) % MOD

    endpoint_a = a.ones - floor_alpha(a.length)
    right_min = endpoint_a + b.base_min - (
        phase_carry(a.length, b.critical_prefix)
        if b.critical_prefix is not None
        else 0
    )
    parent_min = min(a.base_min, right_min)

    left_candidate = (
        a.critical_prefix if a.base_min == parent_min else None
    )
    right_candidate = None
    if right_min == parent_min:
        right_candidate = a.length + (
            b.critical_prefix if b.critical_prefix is not None else 0
        )

    critical = max_fractional((left_candidate, right_candidate))
    return State(
        a.length + b.length,
        a.ones + b.ones,
        cmod,
        parent_min,
        critical,
    )


STATE0 = State(1, 0, 0, 0, 1)
STATE1 = State(1, 1, 1, 0, None)


# Full 129-node reference state.
dag_states = [STATE0, STATE1]
for node in nodes[2:]:
    dag_states.append(
        compose(dag_states[node["left"]], dag_states[node["right"]])
    )
assert len(dag_states) == 129


power_compositions = 0


def state_power(s: State, n: int) -> State:
    global power_compositions
    assert n >= 1
    if n == 1:
        return s
    half = state_power(s, n // 2)
    square = compose(half, half)
    power_compositions += 1
    if n % 2 == 0:
        return square
    power_compositions += 1
    return compose(square, s)


# ---------------------------------------------------------------------------
# Run-compressed reconstruction.
# ---------------------------------------------------------------------------
left = STATE0
right = STATE1
cumulative_decisions = 0
run_endpoint_checks = 0

for direction, count in RUNS:
    if direction == "L":
        left = compose(left, state_power(right, count))
        current = left
    else:
        right = compose(state_power(left, count), right)
        current = right

    cumulative_decisions += count
    node_index = cumulative_decisions + 1
    assert current == dag_states[node_index]
    run_endpoint_checks += 1

assert cumulative_decisions == 126
assert run_endpoint_checks == 20

run_root = compose(left, right)
assert run_root == dag_states[root]
assert run_root.length == J0
assert run_root.ones == R0
assert run_root.base_min == 0
assert run_root.critical_prefix == 9_809_721_694


# ---------------------------------------------------------------------------
# Exact compressed LCP on the straight-line grammar.
# ---------------------------------------------------------------------------
def lcp_nodes(i: int, j: int):
    a_queue = deque([i])
    b_queue = deque([j])
    common = 0
    expansions = 0

    while a_queue and b_queue:
        a = a_queue[0]
        b = b_queue[0]

        if a == b:
            a_queue.popleft()
            b_queue.popleft()
            common += nodes[a]["q"]
            continue

        na = nodes[a]
        nb = nodes[b]
        if na["left"] is None and nb["left"] is None:
            return common, expansions

        la = na["q"]
        lb = nb["q"]
        expanded = False

        if na["left"] is not None and (nb["left"] is None or la >= lb):
            a_queue.popleft()
            a_queue.appendleft(na["right"])
            a_queue.appendleft(na["left"])
            expansions += 1
            expanded = True

        if nb["left"] is not None and (na["left"] is None or lb >= la):
            b_queue.popleft()
            b_queue.appendleft(nb["right"])
            b_queue.appendleft(nb["left"])
            expansions += 1
            expanded = True

        assert expanded

    return common, expansions


@lru_cache(maxsize=None)
def materialize(i: int):
    node = nodes[i]
    if node["left"] is None:
        return (node["p"],)
    return materialize(node["left"]) + materialize(node["right"])


small_nodes = tuple(i for i, n in enumerate(nodes) if n["q"] <= MATERIALIZE_MAX)
lcp_materialized_regression_checks = 0
for i in small_nodes:
    wi = materialize(i)
    for j in small_nodes:
        wj = materialize(j)
        direct = 0
        for x, y in zip(wi, wj):
            if x != y:
                break
            direct += 1
        compressed, _ = lcp_nodes(i, j)
        assert compressed == direct
        lcp_materialized_regression_checks += 1

assert len(small_nodes) == 45
assert lcp_materialized_regression_checks == 2_025


# ---------------------------------------------------------------------------
# Final Christoffel ray W_n=A^n B and linear separating scale.
# ---------------------------------------------------------------------------
A = 112
B = 111
assert nodes[A]["p"] * nodes[B]["q"] - nodes[B]["p"] * nodes[A]["q"] == -1

base_lcp, base_lcp_expansions = lcp_nodes(A, B)
assert base_lcp == nodes[B]["q"] - 1

# W_0=B, W_n=node(112+n) for 1<=n<=16.
final_ray_checks = 0
final_ray_ballot_checks = 0
max_lcp_expansions = base_lcp_expansions

for n in range(1, 17):
    current = 112 + n
    previous = B if n == 1 else 111 + n

    # Exact formation W_n=A W_{n-1}; for n=1 this is A B.
    assert nodes[current]["left"] == A
    assert nodes[current]["right"] == previous

    expected_length = n * nodes[A]["q"] + nodes[B]["q"]
    expected_ones = n * nodes[A]["p"] + nodes[B]["p"]
    assert nodes[current]["q"] == expected_length
    assert nodes[current]["p"] == expected_ones

    lcp, expansions = lcp_nodes(current, previous)
    max_lcp_expansions = max(max_lcp_expansions, expansions)
    assert lcp == nodes[previous]["q"] - 1
    final_ray_checks += 1

    # The exact phase-critical ballot summary picks the preceding ray word.
    assert dag_states[current].critical_prefix == nodes[previous]["q"]
    final_ray_ballot_checks += 1

assert final_ray_checks == 16
assert final_ray_ballot_checks == 16

PREDECESSOR = 127
ROOT = 128
root_predecessor_lcp, _ = lcp_nodes(ROOT, PREDECESSOR)
first_distinguishing_dyadic_K = root_predecessor_lcp + 1
assert first_distinguishing_dyadic_K == nodes[PREDECESSOR]["q"]
assert first_distinguishing_dyadic_K == 9_809_721_694

# Since root=A*predecessor, predecessor is an exact suffix of root.  By the
# exact rear-screening identity y_R(UV)=y_R(V), every endpoint residue
# available to the shorter word is identical.
endpoint_indistinguishable_through_R = nodes[PREDECESSOR]["p"]
assert endpoint_indistinguishable_through_R == 6_189_245_291

# The critical ballot prefix equals the exact first source-separating scale.
assert dag_states[ROOT].critical_prefix == first_distinguishing_dyadic_K


# ---------------------------------------------------------------------------
# Ballot critical-prefix provenance is the reverse run hierarchy.
# ---------------------------------------------------------------------------
def critical_trace(i: int):
    directions = []
    steps = 0
    while nodes[i]["left"] is not None:
        a = dag_states[i].critical_prefix
        assert a is not None
        li = nodes[i]["left"]
        ri = nodes[i]["right"]
        left_length = nodes[li]["q"]

        if a == left_length:
            return tuple(directions), i, steps

        if a < left_length:
            # Parent critical prefix came from the left child unchanged.
            assert dag_states[li].critical_prefix == a
            directions.append("L")
            i = li
        else:
            # Parent critical prefix came from the shifted right child.
            local = a - left_length
            assert dag_states[ri].critical_prefix == local
            directions.append("R")
            i = ri
        steps += 1

    return tuple(directions), i, steps


CRITICAL_DIRECTIONS, CRITICAL_STOP_NODE, critical_trace_steps = critical_trace(root)
CRITICAL_RUNS = run_length_encode(CRITICAL_DIRECTIONS)
assert critical_trace_steps == 126
assert CRITICAL_STOP_NODE == 2
assert CRITICAL_RUNS == tuple(reversed(RUNS))
assert len(CRITICAL_RUNS) == 20


print("PASS A0 s=1 Route-B Christoffel run-hierarchy certificate")
print("continued_fraction_terms", len(CF))
print("continued_fraction", CF)
print("stern_brocot_one_step_decisions", len(DIRECTIONS))
print("run_groups", len(RUNS))
print("runs", RUNS)
print("run_endpoint_state_checks", run_endpoint_checks)
print("state_power_compositions", power_compositions)
print("root_length", run_root.length)
print("root_ones", run_root.ones)
print("root_cmod_2^128", run_root.cmod)
print("root_ballot_base_min", run_root.base_min)
print("root_ballot_critical_prefix", run_root.critical_prefix)
print("lcp_materialized_regression_checks", lcp_materialized_regression_checks)
print("final_ray_A_length", nodes[A]["q"])
print("final_ray_A_ones", nodes[A]["p"])
print("final_ray_B_length", nodes[B]["q"])
print("final_ray_B_ones", nodes[B]["p"])
print("final_ray_pair_checks", final_ray_checks)
print("final_ray_ballot_checks", final_ray_ballot_checks)
print("critical_trace_steps", critical_trace_steps)
print("critical_trace_run_groups", len(CRITICAL_RUNS))
print("critical_trace_runs", CRITICAL_RUNS)
print("base_lcp_A_B", base_lcp)
print("max_compressed_lcp_expansions", max_lcp_expansions)
print("root_predecessor_length", nodes[PREDECESSOR]["q"])
print("root_predecessor_ones", nodes[PREDECESSOR]["p"])
print("root_predecessor_lcp", root_predecessor_lcp)
print("first_distinguishing_dyadic_K", first_distinguishing_dyadic_K)
print("endpoint_indistinguishable_through_R", endpoint_indistinguishable_through_R)
print("formation_audit", "20 run formations reconstruct the same exact root state as the 129-node DAG")
print("axis_audit", "boundary resolution scales linearly on the final ray; hierarchy/run exponent is the compact structural coordinate")
print("status", "FIXED boundary quotient REJECTED on final ray; recursive run hierarchy CLOSED for current target; universal membership OPEN")
