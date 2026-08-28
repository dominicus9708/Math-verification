#!/usr/bin/env python3
"""Monotone prefix-defect pruning for the A0 s=1 unique-target gate.

This is a downstream certificate.  It imports the already-certified
radius-seven/Christoffel real-envelope constants and keeps exactly the same
normalization:

    eta(w) = (C_threshold - C(w)) / 3^j0
           = sum_r 3^(-r) (2^t_r - 2^a_r)

at fixed total odd count j0, where t_r is the threshold r-th odd position.
For a pure-ballot word a_r<=t_r, so every summand is nonnegative.
Consequently a defect already accumulated by a prefix can never be repaired
by any future suffix.  This gives a monotone SAFE rejection oracle.

The finite part below conditions the first-75 d75>=8 defect calculation on the
24 already-certified first-disagreement dyadic shells.  Each shell receives
its own minimum irreversible defect and hence its own rigorous physical X
upper bound.  No independence or probability multiplication is used.

This is pruning only.  Surviving cylinders are NOT promoted to full
correction-language membership, C4F, or same-orbit connectivity.
"""

from fractions import Fraction

import A0_s1_radius7_defect_christoffel_real_envelope_certificate as upstream

REQ = upstream.REQ
TH = upstream.TH
TPOS = upstream.TPOS
QFP = upstream.QFP
mW_lo = upstream.mW_lo
cW_hi = upstream.cW_hi
delta_lo = upstream.delta_lo
mul_lo = upstream.mul_lo
L_MAX = upstream.L_MAX
GLOBAL_ETA_MIN = upstream.eta_min
GLOBAL_X_MAX = upstream.new_x_max

X_TH = 4_697_939_311_072_332_635_131
X_MIN = (1 << 71) + 1

EXPECTED_FIRST = (
    2, 5, 8, 10, 13, 16, 18, 21,
    24, 27, 29, 32, 35, 37, 40, 43,
    46, 48, 51, 54, 56, 59, 62, 65,
)


def defect_atom(rank: int, actual_pos: int) -> Fraction:
    """Irreversible eta contribution of one already-seen odd event."""
    assert rank >= 1
    threshold_pos = TPOS[rank - 1]
    assert actual_pos <= threshold_pos
    return Fraction(
        (1 << threshold_pos) - (1 << actual_pos),
        3 ** rank,
    )


def prefix_eta(bits) -> Fraction:
    q = 0
    eta = Fraction(0)
    for pos, bit in enumerate(bits):
        if bit:
            q += 1
            eta += defect_atom(q, pos)
    return eta


def x_upper_from_eta(eta: Fraction) -> int:
    """SAFE physical X upper bound inherited from the same directed intervals."""
    assert eta >= 0
    eta_lo = (eta.numerator * QFP) // eta.denominator
    defect_effect_lo = mul_lo(mW_lo, eta_lo)
    candidate_c_hi = cW_hi - defect_effect_lo
    return (L_MAX * QFP + candidate_c_hi) // delta_lo


def count_congruence(lo: int, hi: int, residue: int, modulus: int) -> int:
    if hi < lo:
        return 0
    first = lo + ((residue - lo) % modulus)
    if first > hi:
        return 0
    return (hi - first) // modulus + 1


# ---------------------------------------------------------------------------
# 1. Exact theorem audit: prefix defect is monotone under pure-ballot extension.
# ---------------------------------------------------------------------------
# The theorem follows termwise from nonnegativity.  Exhaustive small-prefix
# regressions independently audit the implementation and rank conventions.

for h in range(1, 13):
    # Enumerate all binary words at this small depth.
    for mask in range(1 << h):
        bits = tuple((mask >> i) & 1 for i in range(h))
        q = 0
        valid = True
        for pos, bit in enumerate(bits):
            q += bit
            if q < REQ[pos + 1]:
                valid = False
                break
        if not valid:
            continue

        eta = prefix_eta(bits)
        assert eta >= 0

        # Append either legal next bit and verify nondecrease.
        if h < 12:
            for bit in (0, 1):
                bits2 = bits + (bit,)
                q2 = sum(bits2)
                if q2 < REQ[h + 1]:
                    continue
                eta2 = prefix_eta(bits2)
                assert eta2 >= eta


# ---------------------------------------------------------------------------
# 2. First-75 shell-conditioned minimum irreversible defect.
# ---------------------------------------------------------------------------
# State = (odd count, Hamming distance capped at 8, first disagreement).
# Cost only depends on current rank/position, so keeping the least eta per
# state is an exact dynamic program.

dp = {(0, 0, None): (Fraction(0), "")}
for pos in range(75):
    tbit = TH[pos]
    nxt = {}
    for (q, dcap, first), (eta, word) in dp.items():
        for bit in (0, 1):
            nq = q + bit
            if nq < REQ[pos + 1]:
                continue

            nd = min(8, dcap + (bit != tbit))
            nf = first
            if nf is None and bit != tbit:
                nf = pos

            add = defect_atom(nq, pos) if bit else Fraction(0)
            val = eta + add
            key = (nq, nd, nf)
            if key not in nxt or val < nxt[key][0]:
                nxt[key] = (val, word + str(bit))
    dp = nxt

shell_min = {}
for (q, dcap, first), (eta, word) in dp.items():
    if dcap != 8 or first is None:
        continue
    item = (eta, q, word)
    if first not in shell_min or eta < shell_min[first][0]:
        shell_min[first] = item

assert tuple(sorted(shell_min)) == EXPECTED_FIRST
assert shell_min[8][0] == GLOBAL_ETA_MIN
assert min(v[0] for v in shell_min.values()) == GLOBAL_ETA_MIN
assert all(v[1] == 48 for v in shell_min.values())

# Every minimum witness begins with the stated first disagreement and has at
# least eight first-75 disagreements.
for f, (eta, q, word) in shell_min.items():
    bits = tuple(int(c) for c in word)
    flips = tuple(i for i in range(75) if bits[i] != TH[i])
    assert flips[0] == f
    assert len(flips) >= 8
    assert prefix_eta(bits) == eta


# ---------------------------------------------------------------------------
# 3. Convert each shell defect to a rigorous shell-specific X upper bound.
# ---------------------------------------------------------------------------

shell_rows = []
retained_before = 0
retained_after = 0
for f in EXPECTED_FIRST:
    eta, q, word = shell_min[f]
    xmax = min(x_upper_from_eta(eta), (1 << 72) - 1)
    modulus = 1 << (f + 1)
    residue = (X_TH + (1 << f)) % modulus

    before = count_congruence(X_MIN, GLOBAL_X_MAX, residue, modulus)
    after = count_congruence(X_MIN, xmax, residue, modulus)
    assert after <= before

    retained_before += before
    retained_after += after
    flips = tuple(i for i in range(75) if int(word[i]) != TH[i])
    shell_rows.append((f, eta, xmax, before, after, flips))

assert retained_before == 125_072_439_876_495_812_978
assert retained_after == 125_072_439_876_454_958_533
assert retained_before - retained_after == 40_854_445

# The late shell remains nonempty: this oracle is a pruning primitive, not a
# contradiction by itself.
assert shell_rows[-1][0] == 65
assert shell_rows[-1][4] > 0

print("PASS A0 s=1 monotone prefix-defect membership-pruning certificate")
print("normalization", "eta=(C_th-C)/3^j0; normalized correction loss=lambda*eta")
print("first75_shell_count", len(shell_rows))
for f, eta, xmax, before, after, flips in shell_rows:
    print("shell", f, "eta_min", eta, "X_max", xmax,
          "count_before", before, "count_after", after,
          "witness_flips", flips)
print("dyadic_shell_count_before", retained_before)
print("dyadic_shell_count_after", retained_after)
print("additional_integer_pruning", retained_before - retained_after)
print("complete_shell_eliminations", 0)
print("oracle", "prune a prefix cylinder when its physical minimum X exceeds x_upper_from_eta(prefix_eta)")
print("status", "SAFE monotone necessary pruning; unique-target membership remains OPEN")
