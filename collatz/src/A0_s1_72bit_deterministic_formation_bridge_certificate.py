#!/usr/bin/env python3
"""Exact 72-bit deterministic formation bridge for the A0 s=1 shell.

The physical A0 input shell satisfies

    2^71 < X <= X_MAX < 2^72.

For a finite parity word w=(b_0,...,b_{n-1}), define the standard 2-adic
starting address

    A_K(w) = - sum_{b_a=1} 2^a 3^{-r(a)}  (mod 2^K),

where r(a) is the rank of that 1 among the ones of w.

Facts certified/regressed here:

1. For K=n, A_n(w) is the unique residue modulo 2^n realizing w.
2. Therefore a length >=72 word has at most one physical A0 integer start:
       X = A_72(w[:72]).
3. If that X lies in the A0 shell, every later parity bit is determined by
   the actual Collatz orbit of X. No extra finite-parity "formation memory"
   is needed after the 72-bit address has been exposed.
4. Endpoint-odd formation is also already contained in the same address:
       rho(w) = A_{n+1}(w+[1])
              = A_{n+1}(w) - 2^n 3^{-(q+1)} (mod 2^{n+1}).

This does NOT identify or certify the separate predicate called C4F in the
working notes. Any renewal/gap/global condition carried by C4F remains a
separate gate.
"""

from itertools import product

X_MAX = 3_295_414_002_074_039_191_016
X_LO = 1 << 71
X_HI = 1 << 72
K_A0 = 72


def address_mod(bits, K: int) -> int:
    M = 1 << K
    q = 0
    x = 0
    for a, bit in enumerate(bits):
        assert bit in (0, 1)
        if bit:
            q += 1
            x = (x - (1 << a) * pow(pow(3, q, M), -1, M)) % M
    return x


def collatz_bits(x: int, n: int):
    out = []
    for _ in range(n):
        bit = x & 1
        out.append(bit)
        x = (3 * x + 1) // 2 if bit else x // 2
    return tuple(out)


def endpoint_odd_residue(bits):
    n = len(bits)
    q = sum(bits)
    M = 1 << (n + 1)
    direct = address_mod(tuple(bits) + (1,), n + 1)
    formula = (
        address_mod(bits, n + 1)
        - (1 << n) * pow(pow(3, q + 1, M), -1, M)
    ) % M
    assert direct == formula
    return direct


# Exhaustive finite-word regression.
for n in range(1, 10):
    M = 1 << n
    seen = set()
    for w in product((0, 1), repeat=n):
        a = address_mod(w, n)
        assert 0 <= a < M
        assert a not in seen
        seen.add(a)
        assert collatz_bits(a, n) == w
        endpoint_odd_residue(w)
    assert len(seen) == M


# A0 target threshold word constructed exactly from 3^q > 2^n.
def threshold_requirements(nmax: int):
    q = [0]
    p2 = 1
    p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


REQ = threshold_requirements(500)
TH = tuple(REQ[n + 1] - REQ[n] for n in range(500))
X_TH = address_mod(TH[:K_A0], K_A0)
assert X_LO < X_TH < X_HI
assert X_TH == 4_697_939_311_072_332_635_131
assert X_TH > X_MAX

actual = collatz_bits(X_TH, 500)
first_disagreement = next(i for i, (a, b) in enumerate(zip(actual, TH)) if a != b)
assert first_disagreement == 74
assert actual[:72] == TH[:72]
assert actual[72:75] == (1, 0, 0)
assert TH[72:75] == (1, 0, 1)

print("PASS A0 s=1 72-bit deterministic formation bridge certificate")
print("shell", "2^71 < X <= X_MAX < 2^72")
print("X_MAX", X_MAX)
print("threshold_address_72", X_TH)
print("threshold_address_exceeds_X_MAX", True)
print("threshold_first_actual_disagreement_zero_index", first_disagreement)
print("finite_parity_formation_after_72", "deterministic from X=A_72")
print("endpoint_odd_residue", "A_(n+1)(w+[1])")
print("C4F_identified", False)
print("status", "SAFE finite-parity/address determinization; C4F separate")
