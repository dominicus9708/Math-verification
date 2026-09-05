#!/usr/bin/env python3
"""Source-preserving valuation-jump / ballot-control factorization.

This rebuilds the eight-jump frontier while carrying the exact ordinary source
cylinder

    X = r + 2^h m

as well as

    T^h(X) = y + 3^q m.

The pure-ballot surplus S=q-Q(h) makes q and A=3^q derived coordinates.
The certificate verifies that adding r and removing stored A leaves all
previous eight-jump counts unchanged, while preserving the exact source and
endpoint affine identities.
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
    r: int
    y: int
    lo: int
    hi: int
    h: int
    S: int
    root_f: int

    @property
    def q(self):
        return ballot.Q[self.h] + self.S

    @property
    def A(self):
        return 3 ** self.q

    @property
    def count(self):
        return self.hi - self.lo + 1


def valuation_child(st: State, a: int):
    ok, S2 = ballot.jump_ballot(st.h, st.S, a)
    if not ok:
        return None

    A = st.A
    M = 1 << (a + 1)
    rho = (((1 << a) - st.y) * pow(A, -1, M)) % M

    k_lo = ceil_div(st.lo - rho, M)
    k_hi = (st.hi - rho) // M
    if k_lo > k_hi:
        return None

    h2 = st.h + a + 1
    r2 = st.r + (rho << st.h)
    assert 0 <= r2 < (1 << h2)

    numer = 3 * (st.y + A * rho) + (1 << a)
    assert numer % M == 0
    y2 = numer // M

    child = State(
        r=r2,
        y=y2,
        lo=k_lo,
        hi=k_hi,
        h=h2,
        S=S2,
        root_f=st.root_f,
    )

    # q increases by one exactly across 0^a1, so the derived affine
    # coefficient becomes 3*A without storing A as an independent state axis.
    assert child.q == st.q + 1
    assert child.A == 3 * A
    return child


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


states = [
    State(
        r=root["r"],
        y=root["y"],
        lo=root["m_lo"],
        hi=root["m_hi"],
        h=root["h"],
        S=root["q"] - ballot.Q[root["h"]],
        root_f=root["f"],
    )
    for root in forest.roots
]

assert all(st.q == ballot.Q[st.h] + st.S for st in states)
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
    got = (len(states), sum(st.count for st in states))
    assert got == EXPECTED[jump]
    rows.append((jump,) + got)

    # Exact source/orbit endpoint identity on both interval ends.  This also
    # audits the canonical source residue r after variable-length jumps.
    for st in states:
        for m in {st.lo, st.hi}:
            X = st.r + (1 << st.h) * m
            bits, endpoint = forest.transducer.orbit_prefix(X, st.h)
            assert sum(bits) == st.q
            assert endpoint == st.y + st.A * m

    if jump == MAX_JUMPS:
        break
    states = [child for st in states for child in children(st)]

controls = {(st.h, st.S) for st in states}
assert len(states) == 14_224
assert len(controls) == 90
assert min(st.h for st in states) == 11
assert max(st.h for st in states) == 51

print("PASS A0 s=1 source-payload/control factorization certificate")
for row in rows:
    print("jump", row[0], "cylinders", row[1], "surviving", row[2])
print("reusable_state", "(r,y,lo,hi,h,S; predicate labels)")
print("stored_A_needed", False)
print("A_formula", "3^(Q(h)+S)")
print("source_residue_preserved", True)
print("eight_jump_control_states_hS", len(controls))
print("status", "EXACT source-preserving pure-ballot jump interface; downstream predicates still separate")
