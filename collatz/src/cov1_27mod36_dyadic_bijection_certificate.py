#!/usr/bin/env python3
"""Regression certificate for the dyadic-suffix barrier of 36*k+27.

The theorem is algebraic:
  N=36k+27=4(9k+6)+3,
and multiplication by 9 is a bijection modulo every 2^r.  Hence the progression
covers every reduced dyadic class after the fixed leading shortcut parity bits 11.

For every L>=2, solving 9k == -7 (mod 2^(L-2)) gives N == -1 (mod 2^L),
so the first L shortcut parity bits are all 1.  Along an all-odd prefix,
T^j(N)=(3/2)^j*(N+1)-1>N, so no fixed finite forward-descent depth can
certify the whole progression.

Finite loops below are regressions only; the proof is the modular algebra above.
"""


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def main():
    # Verify the affine reduced-coordinate bijection for representative small r.
    for r in range(1, 13):
        M = 1 << r
        vals = {(9 * k + 6) % M for k in range(M)}
        assert vals == set(range(M))

    # Verify the exact all-ones cylinder construction for representative L.
    rows = []
    for L in range(2, 25):
        M = 1 << (L - 2)
        inv9 = pow(9, -1, M) if M > 1 else 0
        k0 = ((-7) * inv9) % M if M > 1 else 0
        N = 36 * k0 + 27
        assert (N + 1) % (1 << L) == 0

        x = N
        for j in range(1, L + 1):
            assert x % 2 == 1
            x = T(x)
            assert x > N
            # Closed form for an all-odd prefix.
            assert x * (1 << j) == (3**j) * (N + 1) - (1 << j)
        rows.append((L, k0, N))

    print("SAFE algebraic barrier regression")
    print("k -> 9k+6 is bijective mod 2^r for tested r=1..12")
    print("all-ones cylinders verified for L=2..24")
    print("sample final row:", rows[-1])
    print("Conclusion: no fixed finite forward-descent parity depth can cover 36N0+27.")


if __name__ == "__main__":
    main()
