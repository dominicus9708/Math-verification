#!/usr/bin/env python3
"""Root-scale source/defect Pareto audit at the exact 8-jump frontier.

The previously certified source-defect danger-frontier theorem permits a
proof-level permanent merge only when histories share the SAME complete future
control and SAME exact parameter interval payload.  Within such a key,
coordinatewise domination in

    (source residue r, accumulated defect eta)

is preserved by every common future parameter refinement and by the monotone
physical defect gate.

At the current first-75-tightened 8-jump frontier use the exact key

    K_exact = (h,S,D,y,m_lo,m_hi),

where D is the capped first-75 Hamming count.  q=Q(h)+S is derived.  This key
contains every currently active future coordinate needed by source/parity,
pure-ballot, and first-75 defect evolution.  The historical first-defect label
is deliberately omitted because after (r,eta,D) and the exact future state are
retained, none of these active predicates observes it separately.

Result: all 14,224 current states have distinct K_exact.  Hence the exact
source-defect Pareto theorem has no permanent merge opportunity at this
frontier.

For comparison only, the file also measures finite-horizon keys

    K_d=(h,S,D,m_lo,m_hi,y mod 2^d,3^q mod 2^d).

These do admit Pareto deletions over the next d source bits, but they are NOT
permanent merges: after d bits their exact source controls may separate again.
They are recorded only as execution/block-DP diagnostics.
"""

from collections import defaultdict

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


states = tuple(tail.states)
assert len(states) == 14_224
assert sum(st.count for st in states) == 26_859_837_368_588_270_254


def exact_key(st):
    return (st.h, st.S, st.D, st.y, st.lo, st.hi)


def finite_key(st, d: int):
    M = 1 << d
    return (
        st.h,
        st.S,
        st.D,
        st.lo,
        st.hi,
        st.y % M,
        st.A % M,
    )


def pareto(states_in):
    """Coordinatewise-minimal (r,eta) representatives."""
    best_by_r = {}
    for st in states_in:
        old = best_by_r.get(st.r)
        if old is None or st.eta < old.eta:
            best_by_r[st.r] = st

    out = []
    best_eta = None
    for r, st in sorted(best_by_r.items()):
        if best_eta is None or st.eta < best_eta:
            out.append(st)
            best_eta = st.eta
    return tuple(out)


# ---------------------------------------------------------------------------
# 1. Exact indefinite-future key: no current collisions, therefore no
#    proof-level permanent Pareto merge at this frontier.
# ---------------------------------------------------------------------------

exact_groups = defaultdict(list)
for st in states:
    exact_groups[exact_key(st)].append(st)

assert len(exact_groups) == len(states) == 14_224
assert max(len(v) for v in exact_groups.values()) == 1
assert sum(len(pareto(v)) for v in exact_groups.values()) == len(states)


# ---------------------------------------------------------------------------
# 2. Finite-horizon diagnostic only.
# ---------------------------------------------------------------------------

EXPECTED = {
    # d: (finite-key groups, Pareto entries, finite-horizon dominated entries,
    #     strict groups, max Pareto width)
    2:  (6_530,  8_555, 5_669, 795, 15),
    4:  (8_647, 10_991, 3_233, 1_223, 10),
    6:  (11_418, 12_890, 1_334, 942, 5),
    8:  (13_271, 13_730, 494, 447, 4),
    10: (14_020, 14_100, 124, 124, 2),
    12: (14_194, 14_210, 14, 14, 2),
}

rows = []
for d, expected in EXPECTED.items():
    groups = defaultdict(list)
    for st in states:
        groups[finite_key(st, d)].append(st)

    frontiers = {k: pareto(v) for k, v in groups.items()}
    entries = sum(len(v) for v in frontiers.values())
    dominated = len(states) - entries
    strict_groups = sum(
        1 for k, vals in groups.items()
        if len(frontiers[k]) < len(vals)
    )
    max_width = max(len(v) for v in frontiers.values())

    got = (len(groups), entries, dominated, strict_groups, max_width)
    assert got == expected
    rows.append((d,) + got)


print("PASS A0 s=1 Route-B 8-jump source-defect Pareto frontier audit")
print("frontier_states", len(states))
print("tightened_integer_population", sum(st.count for st in states))
print("exact_future_control_groups", len(exact_groups))
print("permanent_pareto_merges", 0)
for row in rows:
    d, groups, entries, dominated, strict_groups, max_width = row
    print(
        "finite_horizon", d,
        "groups", groups,
        "pareto_entries", entries,
        "finite_horizon_dominated", dominated,
        "strict_groups", strict_groups,
        "max_frontier_width", max_width,
    )
print(
    "exact_audit",
    "the Pareto theorem is valid but has no permanent merge opportunity because every current exact future-control/payload key is unique",
)
print(
    "finite_horizon_audit",
    "temporary Pareto compression exists under Q_d control but must not be retained after its precision is consumed unless a new continuation theorem is supplied",
)
print(
    "dsd_audit",
    "the distinction between exact future equivalence and finite-resolution transition equivalence is enforced explicitly",
)
print(
    "status",
    "root-scale exact danger-frontier merge yield ZERO at 8 jumps; whole-family rejection or a stronger invariant remains required",
)
