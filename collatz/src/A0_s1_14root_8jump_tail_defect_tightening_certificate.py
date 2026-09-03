#!/usr/bin/env python3
"""Eight-jump valuation pruning plus exact first-75 defect-tail tightening.

For each exact source-preserving valuation-jump prefix, carry:

* current source cylinder X=r+2^h m;
* exact current prefix defect eta;
* first-75 Hamming distance D capped at 8;
* exact pure-ballot control.

A finite DP computes the minimum additional normalized defect required from the
current prefix to reach first-75 Hamming distance >=8 while staying pure
ballot.  Adding that tail floor to the already accumulated exact prefix defect
and reusing the certified physical real-envelope converts it to a SAFE source
upper bound.

The result is logically valid but numerically weak at the current eight-jump
frontier; the certificate records that negative/low-yield result explicitly.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

import A0_s1_14root_long_membership_forest_certificate as forest
import A0_s1_prefix_defect_membership_pruning_certificate as defect
import A0_s1_valuation_jump_ballot_control_certificate as ballot

MAX_JUMPS = 8
X72_MAX = (1 << 72) - 1


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


@lru_cache(None)
def min_tail_eta(h: int, q: int, D: int):
    """Minimum additional eta from positions h..74 to end with D>=8."""
    D = min(D, 8)
    if h >= 75:
        return Fraction(0) if D >= 8 else None

    best = None
    tb = defect.TH[h]
    for bit in (0, 1):
        q2 = q + bit
        if q2 < defect.REQ[h + 1]:
            continue
        D2 = min(8, D + (bit != tb))
        add = defect.defect_atom(q2, h) if bit else Fraction(0)
        tail = min_tail_eta(h + 1, q2, D2)
        if tail is None:
            continue
        val = add + tail
        if best is None or val < best:
            best = val
    return best


@dataclass(frozen=True)
class State:
    r: int
    y: int
    lo: int
    hi: int
    h: int
    S: int
    D: int
    eta: Fraction
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


def tighten(st: State):
    if st.h < 75:
        tail = min_tail_eta(st.h, st.q, min(st.D, 8))
        if tail is None:
            return None
        eta_floor = st.eta + tail
    else:
        if st.D < 8:
            return None
        eta_floor = st.eta

    xmax = min(defect.x_upper_from_eta(eta_floor), X72_MAX)
    hi2 = min(st.hi, (xmax - st.r) // (1 << st.h))
    if hi2 < st.lo:
        return None
    return State(st.r, st.y, st.lo, hi2, st.h, st.S,
                 st.D, st.eta, st.root_f)


def child(st: State, a: int):
    ok, S2 = ballot.jump_ballot(st.h, st.S, a)
    if not ok:
        return None

    A = st.A
    M = 1 << (a + 1)
    rho = (((1 << a) - st.y) * pow(A, -1, M)) % M
    lo2 = ceil_div(st.lo - rho, M)
    hi2 = (st.hi - rho) // M
    if lo2 > hi2:
        return None

    pos = st.h + a
    rank = st.q + 1
    h2 = pos + 1
    r2 = st.r + (rho << st.h)
    y2 = (3 * (st.y + A * rho) + (1 << a)) // M

    D2 = st.D
    # Forced zero part inside the first-75 comparison window.
    for p in range(st.h, min(st.h + a, 75)):
        if defect.TH[p] == 1:
            D2 = min(8, D2 + 1)
    # Final forced one.
    if pos < 75 and defect.TH[pos] == 0:
        D2 = min(8, D2 + 1)

    eta2 = st.eta + defect.defect_atom(rank, pos)
    return tighten(State(r2, y2, lo2, hi2, h2, S2,
                         D2, eta2, st.root_f))


def children(st: State):
    out = []
    for a in range(256):
        ok, _ = ballot.jump_ballot(st.h, st.S, a)
        if not ok:
            break
        ch = child(st, a)
        if ch is not None:
            out.append(ch)
    return out


states = []
for root in forest.roots:
    bits = defect.TH[:root["f"]] + (1,)
    eta = defect.prefix_eta(bits)
    D = sum(bit != defect.TH[i] for i, bit in enumerate(bits))
    assert D == 1

    st = State(
        r=root["r"],
        y=root["y"],
        lo=root["m_lo"],
        hi=root["m_hi"],
        h=root["h"],
        S=root["q"] - ballot.Q[root["h"]],
        D=D,
        eta=eta,
        root_f=root["f"],
    )

    # Regression: at the first-defect root, the conditional tail DP exactly
    # reconstructs the previously certified shell-specific eta floor.
    tail = min_tail_eta(st.h, st.q, st.D)
    shell_eta = next(row[1] for row in defect.shell_rows if row[0] == root["f"])
    assert st.eta + tail == shell_eta

    tightened = tighten(st)
    assert tightened is not None
    assert tightened.hi == st.hi
    states.append(tightened)


EXPECTED = {
    0: (14,     125_072_439_875_999_947_649),
    1: (32,      94_018_492_189_880_642_552),
    2: (74,      78_277_356_063_840_069_353),
    3: (174,     59_912_679_889_432_947_690),
    4: (374,     50_489_422_254_452_357_530),
    5: (986,     44_710_237_163_869_155_113),
    6: (2_192,   36_555_835_392_481_501_574),
    7: (5_752,   32_306_978_271_064_351_252),
    8: (14_224,  26_859_837_368_588_270_254),
}

for jump in range(MAX_JUMPS + 1):
    got = (len(states), sum(st.count for st in states))
    assert got == EXPECTED[jump]
    if jump == MAX_JUMPS:
        break
    states = [ch for st in states for ch in children(st)]

PURE_BALLOT_8 = 26_859_837_368_845_079_186
TIGHT_8 = EXPECTED[8][1]
EXTRA = PURE_BALLOT_8 - TIGHT_8
assert EXTRA == 256_808_932

print("PASS A0 s=1 eight-jump first75 defect-tail tightening certificate")
print("pure_ballot_eight_jump", PURE_BALLOT_8)
print("defect_tightened_eight_jump", TIGHT_8)
print("additional_pruned", EXTRA)
print("relative_extra_pruning", f"{EXTRA/PURE_BALLOT_8:.12e}")
print("cylinder_count_changed", False)
print("status", "SAFE but low-yield secondary pruning; not a principal S10 engine")
