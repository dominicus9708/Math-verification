#!/usr/bin/env python3
"""
Exact finite certificate for macro lift-digit concatenation and the phase-height
state invariant in the coefficient-survivor sparse-tail representation.

This is a structural certificate only.  It does not prove coefficient stopping
or the Collatz conjecture.
"""


def barrier_table(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        p2 = 1 << k
        while p3 < p2:
            p3 *= 3
            q += 1
        out[k] = q
    return out


BARRIER = barrier_table(256)


def T(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def block_data(x: int, B: int):
    y = x
    bits = []
    q = 0
    for _ in range(B):
        bit = y & 1
        bits.append(bit)
        q += bit
        y = T(y)
    r = x % (1 << B)
    if r == 0:
        r = 1 << B
    return tuple(bits), q, r, y


def coefficient_survival_length(x: int, s: int, h: int, limit: int = 500) -> int:
    y = x
    q = 0
    for j in range(1, limit + 1):
        bit = y & 1
        q += bit
        y = T(y)
        required = BARRIER[s + j] - BARRIER[s] - h
        if q < required:
            return j - 1
    return limit


def main() -> None:
    B = 5
    blocks = 4
    starts = 0
    transitions = 0

    # Start only after a positive-depth prefix, where the normalized affine
    # base satisfies 0 < rho < 3^a and e=0.  For every chosen phase s and
    # surplus h, a is NOT independent: a = b_s + h.
    for s0 in range(5, 11):
        for h0 in range(3):
            a0 = BARRIER[s0] + h0
            modulus = 3 ** a0
            for rho0 in range(1, min(modulus, 41)):
                for t0 in range(128):
                    starts += 1
                    s, h, a, rho, t = s0, h0, a0, rho0, t0
                    x = rho + (3 ** a) * t
                    reconstructed = 0

                    for n in range(blocks):
                        _, q, r, endpoint = block_data(x, B)

                        # The macro Hensel/lift digit is exactly the next
                        # base-2^B digit of the affine progression parameter t.
                        J = ((r - rho) * pow(3 ** a, -1, 1 << B)) % (1 << B)
                        assert J == t % (1 << B)
                        reconstructed += J << (n * B)

                        t_next = (t - J) // (1 << B)
                        seed = rho + (3 ** a) * J
                        _, q_seed, _, rho_next = block_data(seed, B)
                        assert q_seed == q

                        # Exact affine progression transport.
                        assert endpoint == rho_next + (3 ** (a + q)) * t_next

                        # Exact state redundancy: h = a - b_s is invariant.
                        s_next = s + B
                        h_next = h + q - (BARRIER[s_next] - BARRIER[s])
                        a_next = a + q
                        assert a_next == BARRIER[s_next] + h_next

                        s, h, a, rho, t, x = (
                            s_next,
                            h_next,
                            a_next,
                            rho_next,
                            t_next,
                            endpoint,
                        )
                        transitions += 1

                    # Exact digit concatenation after four macro blocks.
                    assert t0 == reconstructed + (t << (blocks * B))

    assert starts == 92160
    assert transitions == 368640

    # Exact zero-lift calibration for the four ordinary first-five-step
    # surviving branches (rho,s,h).
    expected = {
        (20, 5, 0): 1,
        (40, 5, 0): 1,
        (71, 5, 0): 53,
        (242, 5, 1): 50,
    }
    for state, want in expected.items():
        got = coefficient_survival_length(*state)
        assert got == want, (state, got, want)

    print(f"starts={starts}")
    print(f"macro_transitions={transitions}")
    for state, want in expected.items():
        print(
            f"state={state} zero_lift_survival_steps={want} "
            f"full_zero_5blocks={want // 5}"
        )
    print("macro lift-digit concatenation certificate: PASS")


if __name__ == "__main__":
    main()
