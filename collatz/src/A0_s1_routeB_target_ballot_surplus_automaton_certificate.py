#!/usr/bin/env python3
"""Exact surplus-counter automaton for the Route-B target ballot class.

The finite target-aware decoder uses metadata

    (h,q,base_min,critical) = (h,q_target,0,None).

For the threshold target TH with

    REQ(u) = floor(alpha*u)+1  (u>0),
    TH_i   = REQ(i+1)-REQ(i),

(base_min,critical)=(0,None) is EXACTLY equivalent to

    q_W(u) >= REQ(u) = q_TH(u)   for every nonempty prefix u.

Thus, among words with the same final one-count, define the surplus

    sigma(u) = q_W(u)-q_TH(u).

The target ballot class is precisely

    sigma(0)=0, sigma(u)>=0 for all u, sigma(h)=0,

with transition

    sigma(u+1)=sigma(u)+W_u-TH_u.

This is a one-counter DAG with O(h) states per layer and O(h^2) total layered
states, replacing 2^h word enumeration for the ballot/critical candidate
language.

For N=18 the DP count is exactly 2652, matching the existing exhaustive audit.
"""

from fractions import Fraction

N = 18


def log_bounds(z: Fraction, n: int = 90):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


def floor_alpha(n: int) -> int:
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    return flo


def requirement(n: int) -> int:
    return 0 if n == 0 else floor_alpha(n) + 1


def threshold_word(n: int):
    return tuple(requirement(i + 1) - requirement(i) for i in range(n))


TH = threshold_word(N)
Q_TARGET = sum(TH)
assert Q_TARGET == 12

# Layered surplus DP.  Counts all prefix-dominating words by current surplus;
# the same-final-q target class is the sigma=0 bucket at depth N.
dp = {0: 1}
layer_states = [1]
layer_edges = []
for tbit in TH:
    nxt = {}
    edges = 0
    for sigma, count in dp.items():
        for wbit in (0, 1):
            sigma2 = sigma + wbit - tbit
            if sigma2 < 0:
                continue
            nxt[sigma2] = nxt.get(sigma2, 0) + count
            edges += 1
    dp = nxt
    layer_states.append(len(dp))
    layer_edges.append(edges)

assert dp[0] == 2_652
assert max(layer_states) <= N + 1
assert sum(layer_states) <= (N + 1) * (N + 2) // 2

# Independent structural checks on every same-q ballot candidate at N=18 are
# feasible here and guard the equivalence used by the automaton.
def ballot_metadata(bits):
    q = 0
    base_min = 0
    critical = None
    for u, bit in enumerate(bits, 1):
        q += bit
        d = q - floor_alpha(u)
        if d < base_min:
            base_min = d
            critical = u
        elif d == base_min and critical is None:
            # For the equivalence (0,None), merely touching zero is sufficient
            # to make critical non-None; the exact tie-breaking index is not
            # needed here.
            critical = u
    return len(bits), q, base_min, critical


def surplus_accept(bits):
    if len(bits) != N or sum(bits) != Q_TARGET:
        return False
    sigma = 0
    for bit, tbit in zip(bits, TH):
        sigma += bit - tbit
        if sigma < 0:
            return False
    return sigma == 0


# Finite exhaustive guard only; the proof is the cumulative-sum equivalence.
metadata_count = 0
surplus_count = 0
for address in range(1 << N):
    bits = tuple((address >> i) & 1 for i in range(N))
    md = ballot_metadata(bits)
    md_accept = md == (N, Q_TARGET, 0, None)
    sp_accept = surplus_accept(bits)
    assert md_accept == sp_accept
    metadata_count += int(md_accept)
    surplus_count += int(sp_accept)

assert metadata_count == surplus_count == 2_652

print("PASS A0 s=1 Route-B target ballot surplus automaton certificate")
print("target_length", N)
print("target_ones", Q_TARGET)
print("candidate_count", dp[0])
print("layer_state_counts", layer_states)
print("total_layer_states", sum(layer_states))
print("quadratic_bound", (N + 1) * (N + 2) // 2)
print("exact_language", "same-q candidate iff sigma=q_W-q_TH stays nonnegative and returns to zero")
print("complexity", "O(h) surplus states per layer, O(h^2) layered ballot-candidate DAG")
print("dsd_audit", "finite N=18 exhaustive comparison is a regression guard; the surplus equivalence is algebraic")
