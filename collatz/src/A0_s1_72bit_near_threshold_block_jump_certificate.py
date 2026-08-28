#!/usr/bin/env python3
"""Exact A0 s=1 72-bit closure and near-threshold block-jump certificate.

This certificate combines three exact facts.

1. 2-adic parity-address composition:
   for a parity word w with odd positions a_r,

       A(w) = - sum_r 3^{-r} 2^{a_r}  (mod 2^|w|).

   A length-h parity prefix is the actual prefix of an integer X iff
       X == A(w) (mod 2^h).

   Hence once h >= 72 and 0 < X < 2^72, the address residue itself must be
   the ordinary integer X; there are no further high address bits to choose.

2. The exact lower-ballot threshold word has a 72-bit address in the physical
   shell, but its 75-bit lift adds 2^74 and therefore lies above 2^72.
   Thus no physical 72-bit X can follow the exact threshold word through
   the first 75 parity positions.

3. Exhaust every pure-ballot length-75 word at Hamming distance <= 5 from
   that threshold prefix.  After imposing the strict physical shell and the
   previously certified A0 s=1 X upper bound, every remaining address loses
   the pure-ballot condition by prefix 378.

Therefore every full A0 s=1 survivor satisfying the earlier X bound must
 differ from the threshold word in at least six of the first 75 positions.

This is a finite necessary-condition certificate only.  It does not certify
 the full t0 bridge, C4F, or the Collatz conjecture.
"""

from collections import defaultdict

H = 75
MAX_SCAN = 400
MAX_DEV = 5

X_LO = 1 << 71
X_HI = 1 << 72

# Previously certified necessary upper bound from the ballot correction
# envelope/debit-corridor combination.
X_MAX = 3_295_414_002_074_039_191_016


def threshold_requirements(nmax: int):
    """Return q[n]=ceil(n log_3 2), n=0..nmax, exactly by integer powers."""
    q = [0]
    p2 = 1
    p3 = 1
    k = 0
    for _n in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


REQ = threshold_requirements(MAX_SCAN)
TH = tuple(REQ[n + 1] - REQ[n] for n in range(H))
assert all(b in (0, 1) for b in TH)
assert sum(TH) == REQ[H]


def address_from_bits(bits):
    """Universal 2-adic parity address modulo 2^len(bits)."""
    h = len(bits)
    M = 1 << h
    r = 0
    x = 0
    for a, b in enumerate(bits):
        if b:
            r += 1
            inv3r = pow(pow(3, r, M), -1, M)
            x = (x - inv3r * (1 << a)) % M
    return x


# Exact threshold lifts around the 72-bit physical closure boundary.
TH72 = TH[:72]
A72 = address_from_bits(TH72)
A73 = address_from_bits(TH[:73])
A74 = address_from_bits(TH[:74])
A75 = address_from_bits(TH)

assert A72 == 4_697_939_311_072_332_635_131
assert X_LO < A72 < X_HI
assert A73 == A72
assert A74 == A72
assert A75 == A72 + (1 << 74)
assert A75 > X_HI

# Direct orbit regression: A72 follows threshold through positions 0..73
# and first differs at zero-indexed position 74.
x = A72
first_mismatch = None
for i in range(H):
    b = x & 1
    if b != TH[i]:
        first_mismatch = i
        break
    x = (3 * x + 1) // 2 if b else x // 2
assert first_mismatch == 74


# Precompute universal address atoms in modulus 2^75.
M = 1 << H
INV3 = [0] + [pow(pow(3, r, M), -1, M) for r in range(1, H + 1)]


def first_ballot_failure(X: int):
    """Return first 1-indexed prefix n<=MAX_SCAN violating pure ballot."""
    x = X
    q = 0
    for n in range(1, MAX_SCAN + 1):
        b = x & 1
        q += b
        if q < REQ[n]:
            return n
        x = (3 * x + 1) // 2 if b else x // 2
    return None


# stats[d] = [ballot words, physical-shell addresses, <=X_MAX addresses,
#             latest first-failure prefix]
stats = defaultdict(lambda: [0, 0, 0, 0])
survivors = []


def dfs(pos: int, surplus: int, dev: int, rank: int, addr: int):
    """Generate exactly the ballot words within Hamming distance <=MAX_DEV.

    surplus is actual prefix odd count minus the exact threshold requirement.
    Matching TH leaves it unchanged.  Flipping a threshold 0 to 1 raises it;
    flipping a threshold 1 to 0 lowers it and is allowed only if nonnegative.
    """
    if pos == H:
        st = stats[dev]
        st[0] += 1

        if X_LO < addr < X_HI:
            st[1] += 1
            if addr <= X_MAX:
                st[2] += 1
                fail = first_ballot_failure(addr)
                if fail is None:
                    survivors.append(addr)
                else:
                    st[3] = max(st[3], fail)
        return

    tb = TH[pos]

    # Keep the threshold bit.
    b = tb
    rank2 = rank + b
    addr2 = addr
    if b:
        addr2 = (addr2 - INV3[rank2] * (1 << pos)) % M
    dfs(pos + 1, surplus, dev, rank2, addr2)

    # Flip the threshold bit, if the Hamming budget and ballot corridor allow.
    if dev < MAX_DEV:
        surplus2 = surplus + (1 if tb == 0 else -1)
        if surplus2 >= 0:
            b = 1 - tb
            rank2 = rank + b
            addr2 = addr
            if b:
                addr2 = (addr2 - INV3[rank2] * (1 << pos)) % M
            dfs(pos + 1, surplus2, dev + 1, rank2, addr2)


dfs(0, 0, 0, 0, 0)

expected = {
    0: (1, 0, 0, 0),
    1: (27, 1, 1, 88),
    2: (987, 62, 18, 110),
    3: (14_003, 916, 386, 161),
    4: (248_564, 15_560, 6_174, 222),
    5: (2_350_907, 147_027, 58_212, 378),
}
for d in range(MAX_DEV + 1):
    assert tuple(stats[d]) == expected[d]

assert not survivors

total_words = sum(stats[d][0] for d in range(MAX_DEV + 1))
total_physical = sum(stats[d][1] for d in range(MAX_DEV + 1))
total_bounded = sum(stats[d][2] for d in range(MAX_DEV + 1))
latest_failure = max(stats[d][3] for d in range(MAX_DEV + 1))

assert total_words == 2_614_489
assert total_physical == 163_566
assert total_bounded == 64_791
assert latest_failure == 378

print("PASS A0 s=1 72-bit closure and near-threshold block-jump certificate")
print("threshold_address_72", A72)
print("threshold_address_75", A75)
print("threshold_75_lift", "A75 = A72 + 2^74")
print("threshold_first_orbit_mismatch_zero_indexed", first_mismatch)
print("hamming_radius_closed", MAX_DEV)
print("ballot_words_radius_le_5", total_words)
print("physical_shell_words_radius_le_5", total_physical)
print("bounded_physical_words_radius_le_5", total_bounded)
print("all_bounded_candidates_fail_by_prefix", latest_failure)
print("necessary_first75_hamming_distance", ">= 6")
print("status", "SAFE finite necessary-condition closure")
