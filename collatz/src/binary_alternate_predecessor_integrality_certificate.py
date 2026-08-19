#!/usr/bin/env python3
"""Exact audit of the s<q alternate-predecessor integerization step.

For two length-L parity words u,w with the same odd count q and corrections
R_u>R_w, write

    R_u-R_w = 3^s C0,  0<s<q,
    d = q-s.

Let t_d be the time immediately after the d-th odd symbol of u and let R_d be
the correction accumulated by that prefix of u. If N is in the canonical
length-L cylinder of w, define

    m = (3^d N + R_d - C0) / 2^t_d.

The repository's integerization sieve uses m as an integer alternate start for
the remaining suffix of u. The divisibility is automatic, even though the old
code did not spell out the congruence proof:

    3^q N + R_w == 0 (mod 2^L),
    3^q r_u + R_u == 0 (mod 2^L)

imply

    3^d N - C0 == 3^d r_u (mod 2^L).

Therefore the numerator defining m is divisible by 2^t_d, and after division
m is congruent modulo 2^(L-t_d) to the actual state reached from r_u after the
same prefix. Hence m follows the remaining suffix of u as a genuine integer
Collatz trajectory.

This certificate exhaustively checks the congruence, divisibility, suffix
parity, and final endpoint equality for every qualifying pair through L=12.
It is a finite regression certificate supporting the general algebraic proof,
not a proof of the Collatz conjecture.
"""


def v3(x: int) -> int:
    s = 0
    while x and x % 3 == 0:
        x //= 3
        s += 1
    return s


def info(mask: int, L: int):
    R = 0
    q = 0
    odd_times = []
    prefix_R = []
    for i in range(L):
        if (mask >> i) & 1:
            R = 3 * R + (1 << i)
            q += 1
            odd_times.append(i + 1)
            prefix_R.append(R)
    return q, R, odd_times, prefix_R


def canonical(mask: int, L: int) -> int:
    r = 0
    y = 0
    p3 = 1
    for k in range(L):
        bit = (mask >> k) & 1
        carry = bit ^ (y & 1)
        if carry:
            r += 1 << k
            y += p3
        if bit:
            y = (3 * y + 1) // 2
            p3 *= 3
        else:
            y //= 2
    return r


def step(x: int, bit: int) -> int:
    assert (x & 1) == bit
    return (3 * x + 1) // 2 if bit else x // 2


def endpoint(x: int, mask: int, lo: int, hi: int) -> int:
    for i in range(lo, hi):
        x = step(x, (mask >> i) & 1)
    return x


def main():
    checked = 0
    for L in range(3, 13):
        data = [info(mask, L) for mask in range(1 << L)]
        residues = [canonical(mask, L) for mask in range(1 << L)]
        modL = 1 << L

        for w in range(1 << L):
            q, Rw, _, _ = data[w]
            N = residues[w]
            assert (pow(3, q, modL) * N + Rw) % modL == 0

            for u in range(1 << L):
                qu, Ru, odd_times, prefix_R = data[u]
                if qu != q or Ru <= Rw:
                    continue

                C = Ru - Rw
                s = v3(C)
                if not (0 < s < q):
                    continue

                d = q - s
                td = odd_times[d - 1]
                if (1 << td) <= 3**d:
                    continue

                C0 = C // (3**s)
                Rd = prefix_R[d - 1]
                ru = residues[u]

                # Full-cylinder congruence proof in finite form.
                assert (pow(3, d, modL) * N - C0 - pow(3, d, modL) * ru) % modL == 0

                numerator = 3**d * N + Rd - C0
                assert numerator % (1 << td) == 0
                m = numerator // (1 << td)

                # The divided congruence places m in the canonical suffix
                # cylinder of u.
                xu = endpoint(ru, u, 0, td)
                assert (m - xu) % (1 << (L - td)) == 0

                # Hence the suffix is a genuine integer Collatz trajectory.
                y_alt = endpoint(m, u, td, L)
                y_actual = endpoint(N, w, 0, L)
                assert y_alt == y_actual

                checked += 1

    assert checked == 829_734
    print("qualifying_pair_checks", checked)
    print("integer_divisibility_failures 0")
    print("suffix_parity_failures 0")
    print("endpoint_mismatch_failures 0")
    print("alternate predecessor integrality certificate: PASS")


if __name__ == "__main__":
    main()
