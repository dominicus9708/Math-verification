#!/usr/bin/env python3
"""Exact certificate for the 5-step phase/height renormalization used by the
minimal-survivor sparse-tail program.

For b_k = ceil(k log_3 2), define S_{s,h}(J) to be the positive integers x
whose first J accelerated Collatz parity steps satisfy

    q_j(x) >= b_{s+j} - b_s - h   for every 1 <= j <= J.

A length-5 parity cylinder w has canonical positive representative r_w in
{1,...,32}, odd count q_w, and endpoint c_w=T^5(r_w).  Every positive integer
in the cylinder is uniquely

    x = r_w + 32 t,  t >= 0,

and the affine parity-vector identity gives

    T^5(x) = c_w + 3^q_w t.

Writing Q_s=b_{s+5}-b_s and h'=h+q_w-Q_s, the exact set recursion is

    x in S_{s,h}(J+5)
      iff
    w is admissible for the first five steps and
    c_w+3^q_w t in S_{s+5,h'}(J).

The certificate verifies this exhaustively for s=0,...,10, h=0,1,2 and
J=10 over all canonical positive representatives 1,...,2^10.  It also checks
the four ordinary depth-five survivor cylinders and their affine maps.

This is an exact decomposition lemma.  Taking only the minimum endpoint of a
suffix loses the required ternary congruence c_w mod 3^q_w; therefore the
result is not, by itself, an asymptotic lower bound for mu(K).
"""


def barrier_table(n: int) -> list[int]:
    b = [0] * (n + 1)
    p2 = p3 = 1
    q = 0
    for j in range(1, n + 1):
        p2 *= 2
        while p3 < p2:
            p3 *= 3
            q += 1
        b[j] = q
    return b


B = barrier_table(64)


def T(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def survives(x: int, s: int, h: int, J: int) -> bool:
    y = x
    q = 0
    for j in range(1, J + 1):
        if y & 1:
            q += 1
        y = T(y)
        if q < B[s + j] - B[s] - h:
            return False
    return True


def block_data(r: int) -> tuple[tuple[int, ...], int, int]:
    assert 1 <= r <= 32
    y = r
    q = 0
    bits = []
    for _ in range(5):
        bit = y & 1
        bits.append(bit)
        if bit:
            q += 1
        y = T(y)
    return tuple(bits), q, y


def verify_affine_cylinder(r: int) -> None:
    bits, q, c = block_data(r)
    for t in (0, 1, 2, 7, 19):
        x = r + 32 * t
        y = x
        got = []
        for _ in range(5):
            got.append(y & 1)
            y = T(y)
        assert tuple(got) == bits
        assert y == c + (3 ** q) * t


def verify_recursion(s: int, h: int, J: int = 10) -> None:
    assert J >= 5
    Qs = B[s + 5] - B[s]
    for x in range(1, (1 << J) + 1):
        direct = survives(x, s, h, J)

        # Canonical positive representative of x modulo 32.
        r = (x - 1) % 32 + 1
        t = (x - r) // 32
        _, q, c = block_data(r)
        first = survives(r, s, h, 5)
        h2 = h + q - Qs
        endpoint = c + (3 ** q) * t
        via_block = first and survives(endpoint, s + 5, h2, J - 5)
        assert direct == via_block, (s, h, J, x, r, t, q, c, h2)


def main() -> None:
    for r in range(1, 33):
        verify_affine_cylinder(r)

    ordinary = []
    for r in range(1, 33):
        if survives(r, 0, 0, 5):
            ordinary.append((r, block_data(r)))

    expected = [
        (7,  ((1, 1, 1, 0, 1), 4, 20)),
        (15, ((1, 1, 1, 1, 0), 4, 40)),
        (27, ((1, 1, 0, 1, 1), 4, 71)),
        (31, ((1, 1, 1, 1, 1), 5, 242)),
    ]
    assert ordinary == expected
    assert B[5] == 4

    # Thus the first three branches enter phase 5 with h=0, while 31 mod 32
    # enters with one unit of surplus h=1.
    for r, (_, q, _) in ordinary:
        h2 = q - B[5]
        if r == 31:
            assert h2 == 1
        else:
            assert h2 == 0

    for s in range(11):
        for h in range(3):
            verify_recursion(s, h, 10)

    print("phase-height five-block renormalization certificate: PASS")
    print("ordinary_depth5_residues", [r for r, _ in ordinary])
    print("ordinary_affine_maps", [(r, q, c) for r, (_, q, c) in ordinary])
    print("exhaustive_recursion_grid", "s=0..10 h=0..2 J=10")


if __name__ == "__main__":
    main()
