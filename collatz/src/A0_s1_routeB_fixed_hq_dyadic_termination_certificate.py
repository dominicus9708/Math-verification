#!/usr/bin/env python3
"""Universal finite-block dyadic termination for fixed (h,q).

Let w be a parity block of length h with q odd symbols and correction C(w):

    T^h(X) = (3^q X + C(w))/2^h.

Its canonical source residue is

    r(w) == -C(w) * (3^q)^(-1)  (mod 2^h),   0 <= r < 2^h.

The exact prefix-channel transducer proves that length-h parity words are in
bijection with canonical residues modulo 2^h: the two children of a prefix
have residues differing exactly by 2^h at the newly exposed binary digit.

The theorem certified here is stronger than mere injectivity at full h:

THEOREM.
If u != v have the same length h and the same odd count q, then

    v_2(C(u)-C(v)) <= h-2,

hence their correction bridge states are distinguished dyadically by

    K_* = v_2(C(u)-C(v)) + 1 <= h-1.

Proof.
Suppose instead that 2^(h-1) divides Delta=C(u)-C(v). Because u and v have
the same q and 3^q is odd,

    r(u) == r(v) (mod 2^(h-1)).

By the prefix-channel bijection, their first h-1 parity symbols are equal.
Their total one-counts q are also equal, so their final symbols are equal.
Thus u=v, a contradiction.

Consequences.
1. The adaptive correction decoder always terminates on every finite block
   once h and q are fixed; it may always fall back to dyadic refinement.
2. No h-independent finite resolution bound is implied.
3. This theorem identifies a finite parity block; it does NOT prove that the
   block belongs to the remaining Route-B long correction language.

The exhaustive regression below checks the prefix-residue bijection, fixed-q
correction injectivity, and the sharp valuation bound through h=12.
"""

from collections import Counter, defaultdict
from itertools import product

MAX_H = 12


def correction_summary(bits):
    h = q = C = 0
    for bit in bits:
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


def canonical_residue(bits):
    h, q, C = correction_summary(bits)
    mod = 1 << h
    return (-C * pow(pow(3, q), -1, mod)) % mod


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


# Exact affine one-step map, used independently to reconstruct the same
# canonical residue map as the closed prefix-channel certificate.
def refine_channel(state, bit):
    h, r, y, q = state
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)
    if bit == 0:
        y2 = (y + (3 ** q) * m0) // 2
        q2 = q
    else:
        y2 = (3 * y + (3 ** (q + 1)) * m0 + 1) // 2
        q2 = q + 1
    return h + 1, r2, y2, q2


prefix_bijection_checks = 0
fixed_q_pair_checks = 0
sharp_witnesses = {}
length_stats = {}

states = {(0, 0, 0, 0): ()}
for h in range(1, MAX_H + 1):
    next_states = {}
    for state, prefix in states.items():
        for bit in (0, 1):
            child = refine_channel(state, bit)
            bits = prefix + (bit,)
            assert child[0] == h
            assert child[1] == canonical_residue(bits)
            assert child[3] == sum(bits)
            assert child not in next_states
            next_states[child] = bits
            prefix_bijection_checks += 1

    assert len(next_states) == (1 << h)
    residues = [state[1] for state in next_states]
    assert len(set(residues)) == (1 << h)
    assert set(residues) == set(range(1 << h))

    by_q = defaultdict(list)
    for bits in product((0, 1), repeat=h):
        _, q, C = correction_summary(bits)
        by_q[q].append((bits, C))

    first_K_hist = Counter()
    max_v = -1
    witness = None

    for q, entries in by_q.items():
        # Fixed-(h,q) correction is injective.
        assert len({C for _, C in entries}) == len(entries)
        for i in range(len(entries)):
            u, Cu = entries[i]
            for j in range(i):
                v, Cv = entries[j]
                Delta = Cu - Cv
                val = v2(Delta)

                # The universal theorem's exact bound.
                assert val <= h - 2

                # Check the proof mechanism directly: equality mod 2^(h-1)
                # would force the same first h-1 parity prefix.
                ru = canonical_residue(u)
                rv = canonical_residue(v)
                assert (ru - rv) % (1 << (h - 1)) != 0

                Kstar = val + 1
                assert 1 <= Kstar <= h - 1
                first_K_hist[Kstar] += 1
                fixed_q_pair_checks += 1

                if val > max_v:
                    max_v = val
                    witness = (u, v, q, Cu, Cv, Delta, Kstar)

    if h == 1:
        assert fixed_q_pair_checks >= 0
        assert not first_K_hist
    else:
        # Sharpness: the h-1 upper bound is actually attained at every
        # audited h>=2, so it cannot be lowered uniformly from this theorem.
        assert max_v == h - 2
        assert witness is not None
        assert witness[-1] == h - 1
        sharp_witnesses[h] = witness

    length_stats[h] = (
        sum(first_K_hist.values()),
        max_v,
        dict(sorted(first_K_hist.items())),
    )
    states = next_states

assert prefix_bijection_checks == (1 << (MAX_H + 1)) - 2
assert fixed_q_pair_checks == 1_826_175
assert length_stats[12][0] == 1_350_030
assert length_stats[12][1] == 10
assert length_stats[12][2] == {
    1: 646_646,
    2: 335_920,
    3: 175_032,
    4: 91_520,
    5: 48_048,
    6: 25_344,
    7: 13_440,
    8: 7_168,
    9: 3_840,
    10: 2_048,
    11: 1_024,
}

print("PASS A0 s=1 Route-B fixed-(h,q) dyadic termination certificate")
print("max_h", MAX_H)
print("prefix_bijection_checks", prefix_bijection_checks)
print("fixed_q_pair_checks", fixed_q_pair_checks)
print("h12_pair_checks", length_stats[12][0])
print("h12_first_K_hist", length_stats[12][2])
print("universal_bound", "distinct same-(h,q) blocks satisfy v2(Delta C)<=h-2, hence K*<=h-1")
print("sharpness", "K*=h-1 attained for every audited h=2..12")
print(
    "formation_audit",
    "each added parity symbol forms exactly one new dyadic residue digit through the prefix-channel refinement",
)
print(
    "axis_audit",
    "K is an external resolution axis; the theorem gives a block-relative stopping bound K<=h-1, not a global fixed K",
)
print(
    "dsd_audit",
    "finite-block identification terminates universally for fixed h,q; long-language admissibility and universal Route-B membership remain separate obligations",
)
print(
    "status",
    "G4 finite-block adaptive identification TERMINATION CLOSED; target-aware long-language decoder remains OPEN",
)
