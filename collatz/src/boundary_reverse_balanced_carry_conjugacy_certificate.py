from math import cos, pi


def cent_mod(x: int, modulus: int) -> int:
    r = x % modulus
    if r > modulus // 2:
        r -= modulus
    return r


def reverse_orbit(k: int, L: int, ell: int):
    M = 1 << L
    inv3 = pow(3, -1, M)
    b = [cent_mod(k, M)]
    d = []
    for _ in range(ell):
        nxt = cent_mod(b[-1] * inv3, M)
        num = 3 * nxt - b[-1]
        assert num % M == 0
        digit = num // M
        assert digit in (-1, 0, 1)
        d.append(digit)
        b.append(nxt)
    return b, d


def certify_small_grid() -> None:
    for L in range(4, 11):
        M = 1 << L
        for ell in range(1, 8):
            mod3 = 3 ** ell
            x = pow(3 ** ell, -1, M)
            inv_M_mod3 = pow(M, -1, mod3)

            for k in range(1, M, 2):
                b, d = reverse_orbit(k, L, ell)

                # Exact reverse carry expansion.
                D = sum(digit * (3 ** i) for i, digit in enumerate(d))
                assert b[0] == (3 ** ell) * b[ell] - M * D
                assert (D + b[0] * inv_M_mod3) % mod3 == 0

                # Exact boundary-factor conjugacy.
                lhs = abs(cos(pi * k * x / M))
                rhs = abs(cos(pi * b[ell] / M))
                assert abs(lhs - rhs) < 1e-12

                # Zero-suffix equivalence for every available suffix length.
                for s in range(1, ell + 1):
                    zero_suffix = all(d[j] == 0 for j in range(ell - s, ell))
                    central = 2 * (3 ** s) * abs(b[ell]) < M
                    assert zero_suffix == central


if __name__ == "__main__":
    certify_small_grid()
    print("boundary reverse balanced-carry conjugacy: PASS")
