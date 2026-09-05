def cent_mod(x: int, modulus: int) -> int:
    r = x % modulus
    if r > modulus // 2:
        r -= modulus
    return r


def reverse_orbit(u: int, resolution: int, depth: int):
    modulus = 1 << resolution
    inv3 = pow(3, -1, modulus)
    state = cent_mod(u, modulus)
    out = [state]
    for _ in range(depth):
        state = cent_mod(state * inv3, modulus)
        out.append(state)
    return out


def certify_projection_tower() -> None:
    for R in range(6, 12):
        M = 1 << R
        for u in range(1, M, 2):
            full = reverse_orbit(u, R, 8)
            for r in range(3, R + 1):
                low = reverse_orbit(u, r, 8)
                modulus = 1 << r
                for i in range(9):
                    assert low[i] == cent_mod(full[i], modulus)


def certify_resolution_carries() -> None:
    for R in range(6, 11):
        M = 1 << R
        for u in range(1, M, 2):
            full = reverse_orbit(u, R, 6)
            for r in range(3, R + 1):
                modulus = 1 << r
                projected = [cent_mod(x, modulus) for x in full]
                for i in range(6):
                    num = 3 * projected[i + 1] - projected[i]
                    assert num % modulus == 0
                    digit = num // modulus
                    assert digit in (-1, 0, 1)


if __name__ == "__main__":
    certify_projection_tower()
    certify_resolution_carries()
    print("nested dyadic-resolution carry tower: PASS")
