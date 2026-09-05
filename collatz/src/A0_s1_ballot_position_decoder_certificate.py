#!/usr/bin/env python3
"""Exact position-form ballot certificate for A0 s=1.

Let alpha=log_3(2).  For a binary word of length h with odd positions

    0 <= a_1 < ... < a_q < h,

write Q(n) for the number of odd positions in the first n symbols.  The
pure lower-ballot condition is

    Q(n) >= ceil(alpha*n)     for every 0 <= n <= h.

The r-th odd event of the lower threshold word occurs at

    d_r = floor((r-1)/alpha).

Hence the following are equivalent:

  (A) Q(n) >= ceil(alpha*n) for every prefix n;
  (B) a_r <= d_r for every r;
  (C) 2^a_r <= 3^(r-1) for every r.

(A)->(B): by prefix d_r+1 the threshold has r odd events, so an admissible
word must already have its r-th odd event.

(B)->(A): if k=ceil(alpha*n), then the threshold k-th odd event occurs
before n; the actual k-th odd event occurs no later.

(B)<->(C): since a_r is an integer,

    a_r <= floor((r-1)/alpha)
    <=> alpha*a_r <= r-1
    <=> a_r*ln2 <= (r-1)*ln3
    <=> 2^a_r <= 3^(r-1).

This turns a prefix-language constraint into a deterministic check on the
odd positions returned by the already-certified injective correction
decoder.  It does NOT remove additional C4F formation predicates.

The script also gives an exact 72-prefix cardinality bound.  The parity-word
to start-address map is a bijection modulo 2^h at fixed h (certified in
A0_s1_correction_language_injective_decoder_certificate.py).  Therefore the
number of 72-bit start residues whose first 72 parity symbols satisfy the
pure ballot condition equals the number of admissible 72-bit words.
"""

from fractions import Fraction
from itertools import product

H_PHYSICAL = 72
EXPECTED_COUNT_72 = 4_650_657_914_809_371_340


def ceil_alpha_n(n: int) -> int:
    """Exact ceil(n*log_3 2) using only integer powers.

    For n>0, 2^n is never a power of 3, so the answer is the least k with
    3^k > 2^n.
    """
    assert n >= 0
    if n == 0:
        return 0
    target = 1 << n
    p3 = 1
    k = 0
    while p3 <= target:
        p3 *= 3
        k += 1
    return k


def threshold_position(r: int) -> int:
    """Small-regression helper: least a with ceil(alpha*(a+1)) >= r."""
    assert r >= 1
    a = 0
    while ceil_alpha_n(a + 1) < r:
        a += 1
    return a


def prefix_ballot(bits) -> bool:
    q = 0
    for n, b in enumerate(bits, start=1):
        q += b
        if q < ceil_alpha_n(n):
            return False
    return True


def position_ballot(bits) -> bool:
    positions = [i for i, b in enumerate(bits) if b]
    for r, a in enumerate(positions, start=1):
        # Exact power form of a <= floor((r-1)/alpha).
        if (1 << a) > 3 ** (r - 1):
            return False
    # The position inequalities alone control every prefix only when the
    # terminal odd count reaches the terminal threshold.
    return len(positions) >= ceil_alpha_n(len(bits))


def ballot_word_count(h: int) -> int:
    """O(h^2) dynamic count; no 2^h word enumeration."""
    dp = {0: 1}  # current odd count -> number of valid prefixes
    for n in range(1, h + 1):
        threshold = ceil_alpha_n(n)
        nxt = {}
        for q, count in dp.items():
            # Append even.
            if q >= threshold:
                nxt[q] = nxt.get(q, 0) + count
            # Append odd.
            if q + 1 >= threshold:
                nxt[q + 1] = nxt.get(q + 1, 0) + count
        dp = nxt
    return sum(dp.values())


# Exact threshold-position identity on a finite regression range.
for r in range(1, 80):
    a = threshold_position(r)
    assert (1 << a) <= 3 ** (r - 1)
    if a + 1 < 200:
        assert (1 << (a + 1)) > 3 ** (r - 1)

# Exhaustive equivalence regression through depth 14.
for h in range(1, 15):
    for bits in product((0, 1), repeat=h):
        assert prefix_ballot(bits) == position_ballot(bits)

# Immediate exact forced prefix.
# ceil(2*alpha)=2, hence every admissible word begins 11.
assert ceil_alpha_n(1) == 1
assert ceil_alpha_n(2) == 2
assert threshold_position(1) == 0
assert threshold_position(2) == 1

# For the accelerated Collatz map, parity prefix 11 corresponds to start
# address X == 3 (mod 4).  Direct two-step residue regression:
def actual_parity_prefix(x: int, h: int):
    out = []
    for _ in range(h):
        b = x & 1
        out.append(b)
        x = (3 * x + 1) // 2 if b else x // 2
    return tuple(out)

for x in range(4):
    if prefix_ballot(actual_parity_prefix(x, 2)):
        assert x == 3
assert actual_parity_prefix(3, 2) == (1, 1)

# Exact 72-prefix cardinality certificate.
count72 = ballot_word_count(H_PHYSICAL)
assert count72 == EXPECTED_COUNT_72

# The strict physical shell is 2^71 < X < 2^72, hence its exact integer
# cardinality is 2^71-1.  Even without resolving how the accepted residues
# distribute inside that shell, the intersection has cardinality <=count72.
shell_size = (1 << 71) - 1
shell_fraction_upper = Fraction(count72, shell_size)

print("PASS A0 s=1 ballot position-decoder certificate")
print("equivalence", "prefix ballot <=> a_r<=floor((r-1)/alpha) <=> 2^a_r<=3^(r-1)")
print("forced_prefix", "11")
print("forced_start_residue", "X == 3 (mod 4)")
print("valid_pure_ballot_words_depth_72", count72)
print("all_72bit_residue_fraction", float(Fraction(count72, 1 << 72)))
print("strict_physical_shell_size", shell_size)
print("physical_shell_cardinality_fraction_upper", float(shell_fraction_upper))
print("status", "SAFE necessary condition; C4F still OPEN")
