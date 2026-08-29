#!/usr/bin/env python3
"""
Exact certificate: local ordinary-orbit splice across the A0 s=1 checkpoint.

Let b be a pre-checkpoint parity word of length n with EXACTLY M odd bits,
and let v be a post-checkpoint parity word of length K. Define

    z3 = R_M(b) = 2^(-n) C(b) mod 3^M,
    z2 = A_K(v) mod 2^K.

Let Z be any ordinary positive integer satisfying both congruences. Then

    Y = (2^n Z - C(b)) / 3^M

is an integer. If Y>0, then the actual accelerated-Collatz orbit of Y has
parity prefix b, reaches Z after n steps, and the actual orbit of Z has
parity prefix v. Thus b|v is a genuine local ordinary orbit segment.

For the current M=28 checkpoint corridor, positivity is automatic for every
binary b with q(b)=28 because

    C(b)/2^n < (3^28-1)/2 << Z_min.

This closes the LOCAL same-checkpoint provenance gate once a CRT lift Z is
found. It does NOT prove that arbitrary left/right marginal words satisfy
all nonlocal long-language, ballot, correction, renewal, or C4F conditions.

No global Collatz conclusion is claimed.
"""

from __future__ import annotations

from itertools import product
from typing import Sequence, Tuple

M_CURRENT = 28
K_CURRENT = 27
Z_MIN = 7_083_549_723_369_539_339_554
Z_MAX = 9_444_732_965_739_290_427_391

MOD3_CURRENT = 3 ** M_CURRENT
MOD2_CURRENT = 1 << K_CURRENT
CRT_MOD_CURRENT = MOD2_CURRENT * MOD3_CURRENT

EXPECTED_POSITIVITY_BOUND = 11_438_396_227_480
EXPECTED_CRT_MOD = 3_070_471_107_232_407_748_608


def T(x: int) -> int:
    assert x > 0
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def parity_word_and_end(x: int, n: int) -> Tuple[Tuple[int, ...], int]:
    assert x > 0 and n >= 0
    out = []
    for _ in range(n):
        out.append(x & 1)
        x = T(x)
    return tuple(out), x


def odd_count(w: Sequence[int]) -> int:
    assert all(bit in (0, 1) for bit in w)
    return sum(w)


def correction(w: Sequence[int]) -> int:
    C = 0
    for i, bit in enumerate(w):
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << i)
    return C


def full_address(w: Sequence[int]) -> int:
    """The unique start residue modulo 2^|w| producing parity word w."""
    n = len(w)
    assert n >= 1
    mod = 1 << n
    p = odd_count(w)
    return (-correction(w) * pow(pow(3, p, mod), -1, mod)) % mod


def address_K(v: Sequence[int], K: int) -> int:
    assert K >= 1 and len(v) >= K
    return full_address(v[:K])


def terminal_residue_exact_M(b: Sequence[int], M: int) -> int:
    assert M >= 1
    assert odd_count(b) == M
    mod = 3 ** M
    return correction(b) * pow(pow(2, len(b), mod), -1, mod) % mod


def crt_pair(z2: int, K: int, z3: int, M: int) -> Tuple[int, int]:
    m2 = 1 << K
    m3 = 3 ** M
    assert 0 <= z2 < m2
    assert 0 <= z3 < m3
    t = ((z3 - z2) * pow(m2, -1, m3)) % m3
    z = z2 + m2 * t
    N = m2 * m3
    assert z % m2 == z2
    assert z % m3 == z3
    return z, N


def splice_start(b: Sequence[int], M: int, Z: int) -> int:
    """Construct the unique immediate left start Y for word b ending at Z."""
    assert odd_count(b) == M
    n = len(b)
    numerator = (1 << n) * Z - correction(b)
    assert numerator % (3 ** M) == 0
    return numerator // (3 ** M)


def verify_local_splice(b: Sequence[int], v: Sequence[int], M: int, K: int, Z: int) -> int:
    """
    Verify the exact local theorem and return Y.

    Preconditions:
      q(b)=M,
      Z == R_M(b) mod 3^M,
      Z == A_K(v) mod 2^K,
      Y>0.
    """
    assert odd_count(b) == M
    assert len(v) >= K
    assert Z > 0
    assert Z % (3 ** M) == terminal_residue_exact_M(b, M)
    assert Z % (1 << K) == address_K(v, K)

    Y = splice_start(b, M, Z)
    assert Y > 0

    # Integrality plus the affine equation forces the exact start address.
    assert Y % (1 << len(b)) == full_address(b)

    wb, end = parity_word_and_end(Y, len(b))
    assert wb == tuple(b)
    assert end == Z

    wv, _ = parity_word_and_end(Z, K)
    assert wv == tuple(v[:K])
    return Y


def correction_ratio_upper_bound(p: int) -> int:
    """
    For any word b of length n with p odd bits,

      C(b) < 2^n * sum_{j=0}^{p-1} 3^j
           = 2^n * (3^p-1)/2.

    Return the integer geometric-sum factor.
    """
    assert p >= 1
    return (3 ** p - 1) // 2


def check_current_positivity() -> None:
    bound = correction_ratio_upper_bound(M_CURRENT)
    assert bound == EXPECTED_POSITIVITY_BOUND
    assert Z_MIN > bound
    assert Z_MAX > Z_MIN

    # Therefore for every b with q(b)=M_CURRENT and every Z>=Z_MIN:
    # 2^n Z > C(b), so the reconstructed Y is positive.


def check_small_exhaustive_splices() -> None:
    for M in range(1, 4):
        for n in range(M, 7):
            for b in product((0, 1), repeat=n):
                if odd_count(b) != M:
                    continue
                z3 = terminal_residue_exact_M(b, M)
                C = correction(b)
                for K in range(1, 4):
                    for v in product((0, 1), repeat=K):
                        z2 = address_K(v, K)
                        Z0, N = crt_pair(z2, K, z3, M)

                        # Choose the first positive CRT lift large enough to
                        # make the reconstructed left start positive.
                        Z = Z0
                        while (1 << n) * Z <= C:
                            Z += N

                        Y = verify_local_splice(b, v, M, K, Z)
                        assert Y > 0


def check_no_false_claim_for_q_gt_M() -> None:
    """
    Modulo 3^M only proves divisibility by 3^M. If q(b)>M it does not, by
    itself, prove divisibility by 3^q(b). The local splice theorem therefore
    intentionally uses the canonical exact-M-odd suffix.
    """
    b = (1, 1)
    M = 1
    assert odd_count(b) > M
    z3 = correction(b) * pow(pow(2, len(b), 3 ** M), -1, 3 ** M) % (3 ** M)
    # Search a representative satisfying only mod 3^M but not the stronger
    # endpoint condition modulo 3^q.
    found = False
    for Z in range(z3, z3 + 100 * (3 ** M), 3 ** M):
        num = (1 << len(b)) * Z - correction(b)
        if num % (3 ** M) == 0 and num % (3 ** odd_count(b)) != 0:
            found = True
            break
    assert found


def main() -> None:
    assert CRT_MOD_CURRENT == EXPECTED_CRT_MOD
    check_current_positivity()
    check_small_exhaustive_splices()
    check_no_false_claim_for_q_gt_M()

    print("A0 s=1 CHECKPOINT LOCAL SPLICE CERTIFICATE: PASS")
    print(f"current M={M_CURRENT}, K={K_CURRENT}")
    print(f"3^M={MOD3_CURRENT}")
    print(f"2^K={MOD2_CURRENT}")
    print(f"CRT modulus={CRT_MOD_CURRENT}")
    print(f"universal C(b)/2^|b| upper factor for q(b)=28: {correction_ratio_upper_bound(M_CURRENT)}")
    print(f"checkpoint Z_min={Z_MIN}")
    print("EXACT: exact-M left suffix + K-bit right word + positive CRT lift constructs a genuine local orbit segment")
    print("EXACT: positivity is automatic in the current corridor for M=28")
    print("SAFE: local same-checkpoint provenance can be certified arithmetically")
    print("REJECTED: using only mod 3^M when the chosen left suffix has q>M")
    print("OPEN: nonlocal left/right language compatibility and C4F/global Collatz")


if __name__ == "__main__":
    main()
