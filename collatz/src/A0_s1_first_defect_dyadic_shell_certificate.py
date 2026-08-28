#!/usr/bin/env python3
"""Exact first-defect dyadic-shell sieve for the A0 s=1 branch.

Inputs already certified upstream:

    d_75 >= 8,
    2^71 < X <= NEW_X_MAX,
    X_th = A_72(threshold[:72]).

For a pure-ballot first-75 word, the first disagreement from the threshold
cannot be a threshold 1 -> candidate 0: before that position the prefixes are
identical, so removing the new threshold odd event would violate the ballot
lower bound immediately. Hence the first disagreement is 0 -> 1.

The parity-address map is triangular. If two parity words first disagree at
zero-based position f, their addresses agree modulo 2^f and disagree modulo
2^(f+1). Therefore

    v2(X-X_th) = f

for a physical A0 word, because the first 72 bits expose the ordinary X.

An exact finite DP determines which first-disagreement positions can still
accumulate at least eight Hamming disagreements by depth 75 while remaining
pure ballot. This yields 24 disjoint dyadic valuation shells.

The same audit records a channel-separation fact: an integer correction-defect
term attached to any of the first 75 odd ranks contains 3^(j0-r), hence is
zero modulo 3^47. Thus the early defect is visible dyadically but its early
component is invisible to the terminal 3^47 window. No claim is made about
later correction-defect terms.
"""

J0 = 10_439_860_591
R0 = 6_586_818_670
J_ODD = 10 * R0 + 1

X_TH = 4_697_939_311_072_332_635_131
NEW_X_MAX = 3_234_977_022_306_677_631_165
X_MIN = (1 << 71) + 1


def threshold_requirements(nmax: int):
    q = [0]
    p2 = 1
    p3 = 1
    k = 0
    for _ in range(nmax):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


REQ = threshold_requirements(75)
TH = tuple(REQ[i + 1] - REQ[i] for i in range(75))
assert REQ[75] == 48


def can_finish_from_first_mismatch(f: int) -> bool:
    """Pure ballot + first mismatch at f + eventual d_75>=8."""
    assert 0 <= f < 75

    # Prefixes agree before f. Flip the threshold bit at f.
    q = sum(TH[:f])
    bit = 1 - TH[f]
    q += bit
    if q < REQ[f + 1]:
        return False

    states = {(q, 1)}
    for pos in range(f + 1, 75):
        nxt = set()
        for cq, d in states:
            for b in (0, 1):
                nq = cq + b
                if nq < REQ[pos + 1]:
                    continue
                nxt.add((nq, min(8, d + (b != TH[pos]))))
        states = nxt

    return any(d == 8 for _, d in states)


FIRST_DEFECT_POSITIONS = tuple(
    f for f in range(75) if can_finish_from_first_mismatch(f)
)

EXPECTED = (
    2, 5, 8, 10, 13, 16, 18, 21,
    24, 27, 29, 32, 35, 37, 40, 43,
    46, 48, 51, 54, 56, 59, 62, 65,
)
assert FIRST_DEFECT_POSITIONS == EXPECTED
assert all(TH[f] == 0 for f in FIRST_DEFECT_POSITIONS)

# The first mismatch of any pure-ballot word must indeed be 0->1.
# If TH[f]=1 and all earlier bits agree, the candidate prefix count at f+1
# would be REQ[f+1]-1 and therefore fail ballot.
for f in range(75):
    if TH[f] == 1:
        assert sum(TH[:f]) + 0 < REQ[f + 1]


# ---------------------------------------------------------------------------
# Ordinary dyadic-shell count in the newly certified X interval.
#
# v2(X-X_TH)=f is equivalent to
#
#   X == X_TH + 2^f (mod 2^(f+1)).
#
# Distinct f give disjoint residue shells.
# ---------------------------------------------------------------------------

def count_congruence(lo: int, hi: int, residue: int, modulus: int) -> int:
    assert lo <= hi
    first = lo + ((residue - lo) % modulus)
    if first > hi:
        return 0
    return (hi - first) // modulus + 1


shell_counts = {}
for f in FIRST_DEFECT_POSITIONS:
    modulus = 1 << (f + 1)
    residue = (X_TH + (1 << f)) % modulus
    shell_counts[f] = count_congruence(X_MIN, NEW_X_MAX, residue, modulus)

retained = sum(shell_counts.values())
interval_count = NEW_X_MAX - X_MIN + 1

assert retained == 125_072_439_876_495_812_978
assert interval_count == 873_793_780_871_855_024_317
assert retained < interval_count

# The first possible defect is f=2, recovering the known X == 3 (mod 4)
# necessary condition because X_TH == 3 (mod 4).
assert FIRST_DEFECT_POSITIONS[0] == 2
assert X_TH % 4 == 3

# Even the latest shell is populated, so the valuation sieve is pruning,
# not a complete contradiction by itself.
assert shell_counts[65] == 12


# ---------------------------------------------------------------------------
# Channel-separation theorem for the EARLY correction-defect component.
#
# For fixed total j0, a rank-r correction-defect atom is
#
#   3^(j0-r) * (2^t_r - 2^a_r).
#
# Any rank occurring among the first 75 positions has r<=75. Therefore every
# such early atom is divisible by 3^(j0-75), far beyond 3^47.
# This says only that the early component vanishes modulo 3^47; later defect
# atoms may still contribute to the terminal residue.
# ---------------------------------------------------------------------------

assert J_ODD - 75 == 65_868_186_626
assert J_ODD - 75 > 47

print("PASS A0 s=1 first-defect dyadic-shell certificate")
print("first_defect_positions", FIRST_DEFECT_POSITIONS)
print("first_defect_position_count", len(FIRST_DEFECT_POSITIONS))
print("dyadic_condition", "v2(X-X_th) in first_defect_positions")
print("X_interval_count", interval_count)
print("dyadic_shell_retained_count", retained)
print("dyadic_shell_retained_fraction", retained / interval_count)
print("latest_shell_f65_count", shell_counts[65])
print("early_defect_mod_3^47", 0)
print("warning", "only early defect component vanishes mod 3^47; later terms remain")
print("status", "SAFE necessary dyadic sieve; no C4F claim")
