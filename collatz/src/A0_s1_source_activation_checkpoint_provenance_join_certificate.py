#!/usr/bin/env python3
"""Exact regression certificate for SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.

The large Route-B application is symbolic: q=j0-28 is far too large to
materialize naively.  This certificate independently checks the algebraic
kernel on exhaustive small ordinary Collatz segments.

The theorem is:

  source channel: X=r+2^h k, T^h(X)=y+3^q k
  terminal word B: |B|=n, q(B)=M, correction C_B
  checkpoint Z with 2^n Z = 3^M Y + C_B

Then the source and terminal records have the same ordinary-orbit provenance
iff

  Y_B=(2^n Z-C_B)/3^M
  Y_B-y is divisible by 3^q
  k_*=(Y_B-y)/3^q lies in the source parameter interval.

For fixed records the source parameter is unique.
"""

from itertools import product


def T(x: int) -> int:
    assert x > 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def iterate(x: int, n: int) -> int:
    for _ in range(n):
        x = T(x)
    return x


def parity_word(x: int, n: int):
    out = []
    for _ in range(n):
        out.append(x & 1)
        x = T(x)
    return tuple(out)


def correction(bits) -> int:
    C = 0
    for i, b in enumerate(bits):
        if b:
            C = 3 * C + (1 << i)
    return C


def full_address(bits) -> int:
    n = len(bits)
    if n == 0:
        return 0
    q = sum(bits)
    mod = 1 << n
    return (-correction(bits) * pow(pow(3, q, mod), -1, mod)) % mod


def channel_from_prefix(bits):
    """Return exact (r,y,h,q) for the parity cylinder defined by bits."""
    h = len(bits)
    q = sum(bits)
    if h == 0:
        return 0, 0, 0, 0
    r = full_address(bits)
    C = correction(bits)
    num = (3 ** q) * r + C
    assert num % (1 << h) == 0
    y = num // (1 << h)
    return r, y, h, q


def terminal_start(n: int, Cb: int, M: int, Z: int):
    num = (1 << n) * Z - Cb
    if num % (3 ** M):
        return None
    return num // (3 ** M)


def source_parameter_for_terminal(r, y, h, q, lo, hi, n, Cb, M, Z):
    Y = terminal_start(n, Cb, M, Z)
    if Y is None or Y <= 0:
        return None
    diff = Y - y
    A = 3 ** q
    if diff % A:
        return None
    k = diff // A
    if not (lo <= k <= hi):
        return None
    X = r + (1 << h) * k
    if X <= 0:
        return None
    return k, X, Y


positive_checks = 0
excluded_interval_checks = 0
wrong_checkpoint_checks = 0
post_prefix_checks = 0
uniqueness_checks = 0

# Generate genuine source -> activation -> exact-M suffix -> checkpoint records.
for X in range(1, 500):
    for h in range(0, 6):
        u = parity_word(X, h)
        r, y, hh, q = channel_from_prefix(u)
        assert hh == h
        assert X >= r
        assert (X - r) % (1 << h) == 0
        k = (X - r) // (1 << h)
        Y = iterate(X, h)
        assert Y == y + (3 ** q) * k

        # Use short suffixes but require at least one odd event.
        for n in range(1, 7):
            b = parity_word(Y, n)
            M = sum(b)
            if M == 0:
                continue
            Z = iterate(Y, n)
            Cb = correction(b)

            # Exact terminal affine identity and residue/integrality gate.
            assert (1 << n) * Z == (3 ** M) * Y + Cb
            assert Z % (3 ** M) == (
                Cb * pow(pow(2, n, 3 ** M), -1, 3 ** M)
            ) % (3 ** M)

            got = source_parameter_for_terminal(
                r, y, h, q, k, k, n, Cb, M, Z
            )
            assert got == (k, X, Y)
            positive_checks += 1

            # The fixed record cannot select two source parameters.
            got_wide = source_parameter_for_terminal(
                r, y, h, q, max(0, k - 2), k + 2, n, Cb, M, Z
            )
            assert got_wide == (k, X, Y)
            uniqueness_checks += 1

            # Removing the true parameter from the interval rejects the join.
            got_excluded = source_parameter_for_terminal(
                r, y, h, q, k + 1, k + 3, n, Cb, M, Z
            )
            assert got_excluded is None
            excluded_interval_checks += 1

            # Same terminal descriptor at the wrong 3-adic checkpoint class
            # fails integrality whenever we shift by one ordinary integer.
            if (Z + 1) % (3 ** M) != Z % (3 ** M):
                assert terminal_start(n, Cb, M, Z + 1) is None
                wrong_checkpoint_checks += 1

            # A post-checkpoint K-bit word is fixed by Z mod 2^K.
            for K in range(1, 5):
                v = parity_word(Z, K)
                assert full_address(v) == Z % (1 << K)
                got_v = parity_word(Z, K)
                assert got_v == v
                post_prefix_checks += 1


# Independent correction-injectivity guard at fixed (n,M) on small words.
# This supports using (n,C_B) instead of raw B after validity is certified.
injectivity_checks = 0
for n in range(1, 9):
    buckets = {}
    for bits in product((0, 1), repeat=n):
        M = sum(bits)
        key = (M, correction(bits))
        assert key not in buckets
        buckets[key] = bits
        injectivity_checks += 1


assert positive_checks > 10_000
assert uniqueness_checks == positive_checks
assert excluded_interval_checks == positive_checks
assert post_prefix_checks == 4 * positive_checks

print("PASS A0 s=1 source-activation/checkpoint provenance join certificate")
print("positive_same_orbit_checks", positive_checks)
print("unique_parameter_checks", uniqueness_checks)
print("excluded_interval_checks", excluded_interval_checks)
print("wrong_checkpoint_integrality_checks", wrong_checkpoint_checks)
print("post_checkpoint_address_checks", post_prefix_checks)
print("fixed_length_count_correction_injectivity_checks", injectivity_checks)
print("exact", "Y_B(Z) in y+3^q[lo,hi] iff the fixed terminal record belongs to that source activation fiber")
print("exact", "successful membership gives T^(h+n)(X_*)=Z and a unique source parameter k_*")
print("safe", "(n,C_B) replaces raw B only after fixed-(n,M) correction-language validity is certified")
print("rejected", "debit-corridor fiber localization alone is not same-orbit provenance")
print("open", "export/enumeration of actual q=j0-28 activation records on the current 14,224 source families")
