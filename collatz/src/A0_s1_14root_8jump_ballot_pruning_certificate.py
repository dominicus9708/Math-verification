#!/usr/bin/env python3
"""Eight exact valuation-jump pure-ballot pruning rounds on the 14-root forest.

This iterates the exact affine valuation-cylinder transition and the exact
pure-ballot jump control.  No endpoint, H/L, C4F, physical-score density, or
probabilistic assumption is used.

A state is

    Y = y + A m,  A odd,
    m_lo <= m <= m_hi,
    absolute depth h,
    pure-ballot surplus S.

For every ballot-allowed valuation a=v2(Y), the exact child is obtained from

    m = rho + 2^(a+1) k,
    Y' = y' + 3A k,

and the whole forced parity block 0^a1 is consumed in one transition.

The resulting cylinders remain disjoint descendants of their original root,
so summing their exact integer interval sizes gives the exact surviving source
count under these necessary conditions.
"""

from dataclasses import dataclass

import A0_s1_14root_long_membership_forest_certificate as forest
import A0_s1_valuation_jump_ballot_control_certificate as ballot


MAX_JUMPS = 8


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


@dataclass(frozen=True)
class State:
    y: int
    A: int
    lo: int
    hi: int
    h: int
    S: int
    root_f: int

    @property
    def count(self):
        return self.hi - self.lo + 1


def valuation_child(st: State, a: int):
    ok, S2 = ballot.jump_ballot(st.h, st.S, a)
    if not ok:
        return None

    M = 1 << (a + 1)
    rho = (((1 << a) - st.y) * pow(st.A, -1, M)) % M
    k_lo = ceil_div(st.lo - rho, M)
    k_hi = (st.hi - rho) // M
    if k_lo > k_hi:
        return None

    numer = 3 * (st.y + st.A * rho) + (1 << a)
    assert numer % M == 0
    y2 = numer // M
    A2 = 3 * st.A
    assert A2 & 1

    return State(
        y=y2,
        A=A2,
        lo=k_lo,
        hi=k_hi,
        h=st.h + a + 1,
        S=S2,
        root_f=st.root_f,
    )


def children(st: State):
    out = []
    # Once the jump-ballot condition fails, all larger a fail as well because
    # Q(h+a) is nondecreasing; a final-one failure becomes a zero-run failure
    # at the next a.
    for a in range(256):
        ok, _ = ballot.jump_ballot(st.h, st.S, a)
        if not ok:
            break
        child = valuation_child(st, a)
        if child is not None:
            out.append(child)
    return out


states = [
    State(
        y=root["y"],
        A=3 ** root["q"],
        lo=root["m_lo"],
        hi=root["m_hi"],
        h=root["h"],
        S=root["q"] - ballot.Q[root["h"]],
        root_f=root["f"],
    )
    for root in forest.roots
]

assert all(st.S == 1 for st in states)

EXPECTED = {
    # jump: (cylinder_count, surviving_integer_count)
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
    surviving = sum(st.count for st in states)
    assert (cylinders, surviving) == EXPECTED[jump]
    rows.append((jump, cylinders, surviving))

    if jump == MAX_JUMPS:
        break

    nxt = []
    for st in states:
        nxt.extend(children(st))
    states = nxt

initial = EXPECTED[0][1]
final = EXPECTED[MAX_JUMPS][1]
pruned = initial - final
assert pruned == 98_212_602_507_154_868_463

print("PASS A0 s=1 14-root eight-jump ballot pruning certificate")
for jump, cylinders, surviving in rows:
    print("jump", jump, "cylinders", cylinders, "surviving", surviving)
print("initial", initial)
print("after_8_jumps", final)
print("additional_pruned", pruned)
print("survival_fraction", f"{final/initial:.12f}")
print("endpoint_used", False)
print("H_L_used", False)
print("C4F_used", False)
print("status", "SAFE exact pure-ballot prefix pruning; family state growth now needs quotienting")
