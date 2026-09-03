#!/usr/bin/env python3
"""Re-evaluate the exact directed physical P_min gate on valuation cylinders.

This combines the exact 14-root source forest, pure-ballot valuation jumps, and
the already-certified scalar physical danger score

    P = mW_lo*N + delta_lo*3^q*X_lo,

where

    N = 3^q * eta

is the exact integer defect numerator of the realized prefix and X_lo is the
ordinary lower endpoint of the exact source cylinder.

A whole source cylinder is physically rejected when

    P > (L_MAX*QFP + cW_hi) * 3^q.

No Bellman merging is used here: every exact valuation cylinder is evaluated
individually.  Therefore a zero-closure result cannot be an artifact of an
aggressive merge.

The finite execution is evidence only. It does not prove that P_min can never
close a later descendant or that any surviving cylinder is realizable through
the full Route-B language.
"""

from dataclasses import dataclass

import A0_s1_14root_long_membership_forest_certificate as forest
import A0_s1_valuation_jump_ballot_control_certificate as ballot
import A0_s1_prefix_defect_membership_pruning_certificate as pruning


MAX_JUMPS = 8

M_LO = pruning.mW_lo
DELTA_LO = pruning.delta_lo
BARRIER = pruning.L_MAX * pruning.QFP + pruning.cW_hi
TPOS = pruning.TPOS
TH = pruning.TH


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def target_correction(q: int) -> int:
    return sum(
        (3 ** (q-r-1)) * (1 << TPOS[r])
        for r in range(q)
    )


def correction(bits) -> int:
    C = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3*C + (1 << h)
    return C


def numerator(bits) -> int:
    q = sum(bits)
    return target_correction(q) - correction(bits)


@dataclass(frozen=True)
class State:
    r: int
    y: int
    lo: int
    hi: int
    h: int
    q: int
    S: int
    N: int
    root_f: int

    @property
    def count(self):
        return self.hi - self.lo + 1

    @property
    def X_lo(self):
        return self.r + (1 << self.h) * self.lo


def physical_score(st: State) -> int:
    return (
        M_LO * st.N
        + DELTA_LO * (3 ** st.q) * st.X_lo
    )


def physically_closed(st: State) -> bool:
    return physical_score(st) > BARRIER * (3 ** st.q)


def valuation_child(st: State, a: int):
    ok, S2 = ballot.jump_ballot(st.h, st.S, a)
    if not ok:
        return None

    A = 3 ** st.q
    M = 1 << (a + 1)
    rho = (((1 << a) - st.y) * pow(A, -1, M)) % M

    k_lo = ceil_div(st.lo - rho, M)
    k_hi = (st.hi - rho) // M
    if k_lo > k_hi:
        return None

    h2 = st.h + a + 1
    q2 = st.q + 1

    # Source payload is preserved exactly.
    r2 = st.r + (rho << st.h)

    numer_y = 3 * (st.y + A * rho) + (1 << a)
    assert numer_y % M == 0
    y2 = numer_y // M

    # Exact defect-numerator update at the new one-event.  Pure ballot ensures
    # the actual one-position is not later than the target one-position.
    target_pos = TPOS[q2 - 1]
    actual_pos = h2 - 1
    assert actual_pos <= target_pos
    N2 = 3 * st.N + (1 << target_pos) - (1 << actual_pos)
    assert N2 >= 0

    return State(
        r=r2,
        y=y2,
        lo=k_lo,
        hi=k_hi,
        h=h2,
        q=q2,
        S=S2,
        N=N2,
        root_f=st.root_f,
    )


def children(st: State):
    out = []
    for a in range(256):
        ok, _ = ballot.jump_ballot(st.h, st.S, a)
        if not ok:
            break
        child = valuation_child(st, a)
        if child is not None:
            out.append(child)
    return out


states = []
for root in forest.roots:
    f = root["f"]
    bits = TH[:f] + (1,)
    N0 = numerator(bits)
    assert N0 >= 0
    assert root["q"] == sum(bits)
    states.append(State(
        r=root["r"],
        y=root["y"],
        lo=root["m_lo"],
        hi=root["m_hi"],
        h=root["h"],
        q=root["q"],
        S=root["q"] - ballot.Q[root["h"]],
        N=N0,
        root_f=f,
    ))

assert all(st.S == 1 for st in states)

EXPECTED = {
    0: (14,     125_072_439_875_999_947_649),
    1: (32,      94_018_492_189_951_139_878),
    2: (74,      78_277_356_063_975_556_852),
    3: (174,     59_912_679_889_581_873_141),
    4: (374,     50_489_422_254_631_626_671),
    5: (986,     44_710_237_164_104_400_785),
    6: (2_192,   36_555_835_392_716_456_688),
    7: (5_752,   32_306_978_271_327_268_319),
    8: (14_224,  26_859_837_368_845_079_186),
}

rows = []
for jump in range(MAX_JUMPS + 1):
    cylinders = len(states)
    population = sum(st.count for st in states)
    assert (cylinders, population) == EXPECTED[jump]

    closed = [st for st in states if physically_closed(st)]
    closed_population = sum(st.count for st in closed)

    # Exact finite finding of this certificate.
    assert len(closed) == 0
    assert closed_population == 0

    rows.append((jump, cylinders, population, len(closed), closed_population))

    if jump == MAX_JUMPS:
        break
    states = [child for st in states for child in children(st)]

print("PASS A0 s=1 14-root eight-jump P_min recheck certificate")
for row in rows:
    print(
        "jump", row[0],
        "cylinders", row[1],
        "population", row[2],
        "Pmin_closed_cylinders", row[3],
        "Pmin_closed_population", row[4],
    )
print("bellman_merging_used", False)
print("jump8_cylinders", EXPECTED[8][0])
print("jump8_population", EXPECTED[8][1])
print("whole_fiber_closures_through_jump8", 0)
print("status", "EXACT finite negative execution evidence; P_min theorem remains valid")
