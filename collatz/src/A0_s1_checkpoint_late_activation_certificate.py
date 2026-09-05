#!/usr/bin/env python3
"""Regression certificate for predicate-relative checkpoint activation.

Exact theorem under audit:

Let W=AB and suppose B contains exactly the final K one-events of W, so
q(B)=K.  With accelerated-Collatz correction

    C(W)=sum_r 3^(q-r) 2^a_r

and checkpoint Z=T^|W|(X),

    2^|W| Z = 3^q(W) X + C(W).

Correction composition gives

    C(W)=3^K C(A)+2^|A| C(B),

hence modulo 3^K

    Z = 2^(-|B|) C(B)  (mod 3^K).

Thus Z mod 3^K depends only on the suffix containing the final K ones.
For the current Route-B seam K=28.

Separately, a post-checkpoint parity prefix of length L determines the unique
starting residue Z mod 2^L by the standard parity-address bijection.  The
current seam uses L=27.

The exhaustive checks below are regression guards only; the theorem is the
algebraic congruence above.
"""

from itertools import product

K_TARGET = 28
L_TARGET = 27


def correction(bits):
    pos = [i for i, b in enumerate(bits) if b]
    q = len(pos)
    return sum((3 ** (q-r-1)) * (1 << a)
               for r, a in enumerate(pos))


def parity_address(bits):
    h = len(bits)
    if h == 0:
        return 0
    q = sum(bits)
    M = 1 << h
    C = correction(bits)
    return (-C * pow(3 ** q, -1, M)) % M


def accelerated_step(x):
    return (3*x + 1)//2 if x & 1 else x//2


def orbit_bits_and_endpoint(x, n):
    bits = []
    for _ in range(n):
        bits.append(x & 1)
        x = accelerated_step(x)
    return tuple(bits), x


def terminal_k_one_suffix(bits, K):
    ones = [i for i, b in enumerate(bits) if b]
    assert 1 <= K <= len(ones)
    start = ones[-K]
    suffix = bits[start:]
    assert sum(suffix) == K
    return suffix


# Exhaustive terminal-locality regression for every small parity word and
# every possible K up to its total one-count.
checked_terminal = 0
for n in range(1, 12):
    for bits in product((0, 1), repeat=n):
        q = sum(bits)
        if q == 0:
            continue

        X = parity_address(bits)
        got_bits, Z = orbit_bits_and_endpoint(X, n)
        assert got_bits == bits

        # Direct affine identity.
        assert (1 << n) * Z == (3 ** q) * X + correction(bits)

        for K in range(1, q + 1):
            B = terminal_k_one_suffix(bits, K)
            M3 = 3 ** K
            rhs = (
                correction(B)
                * pow(pow(2, len(B), M3), -1, M3)
            ) % M3
            assert Z % M3 == rhs
            checked_terminal += 1


# Exhaustive post-checkpoint dyadic address regression on small prefixes.
checked_dyadic = 0
for L in range(1, 12):
    seen = set()
    for bits in product((0, 1), repeat=L):
        Z = parity_address(bits)
        got, _ = orbit_bits_and_endpoint(Z, L)
        assert got == bits
        assert Z not in seen
        seen.add(Z)
        checked_dyadic += 1
    assert len(seen) == (1 << L)


# Current activation constants.
assert K_TARGET == 28
assert L_TARGET == 27
assert K_TARGET > 0 and L_TARGET > 0

print("PASS A0 s=1 checkpoint late-activation certificate")
print("terminal_locality", "Z mod 3^K = 2^(-|B|) C(B) mod 3^K")
print("terminal_suffix_condition", "q(B)=K and B contains the final K one-events")
print("current_terminal_K", K_TARGET)
print("post_checkpoint_address", "first L bits determine Z mod 2^L")
print("current_post_checkpoint_L", L_TARGET)
print("small_terminal_cases_checked", checked_terminal)
print("small_dyadic_cases_checked", checked_dyadic)
print("global_prebridge_checkpoint_state_needed", False)
print("status", "EXACT locality theorem; finite checks are regression evidence")
