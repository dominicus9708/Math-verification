#!/usr/bin/env python3
"""Finite regression for the finite-address deterministic-tail lemma.

The all-depth proof is in
  collatz/notes/2026-08-24-finite-address-deterministic-tail.md.

This certificate checks the binary-step canonical transition exactly on small
thresholds and records the current m=44/m=45 address depths.  It uses integer
arithmetic only and does not claim a Collatz proof.
"""


def step(state, bit):
    k, q, r, y = state
    carry = bit ^ (y & 1)
    r2 = r + (carry << k)
    y2 = y + (3**q if carry else 0)
    if bit == 0:
        assert y2 % 2 == 0
        y2 //= 2
        q2 = q
    else:
        assert y2 % 2 == 1
        y2 = (3*y2 + 1)//2
        q2 = q + 1
    return (k+1, q2, r2, y2), carry


def direct_T(x):
    return x//2 if x % 2 == 0 else (3*x+1)//2


def audit_small_thresholds():
    # Exhaustively build all canonical states to L, then verify that under a
    # sub-B threshold every surviving continuation after L has carry zero and
    # is exactly the ordinary deterministic Collatz tail.
    for L in range(2, 11):
        for B in (2**(L-1)+1, 2**L-1, 2**L):
            states = [(0, 0, 0, 0)]
            for _ in range(L):
                nxt = []
                for s in states:
                    for bit in (0, 1):
                        t, _ = step(s, bit)
                        if t[2] < B:
                            nxt.append(t)
                states = nxt

            # Canonical residues are unique modulo 2^L.
            rs = [s[2] for s in states]
            assert len(rs) == len(set(rs))

            for s0 in states:
                s = s0
                # Ten more steps must be uniquely forced under r<B.
                for _ in range(10):
                    k, q, r, y = s
                    assert k >= L and r < B
                    forced = y & 1
                    good = []
                    for bit in (0, 1):
                        t, carry = step(s, bit)
                        if t[2] < B:
                            good.append((bit, t, carry))
                    assert len(good) == 1
                    bit, t, carry = good[0]
                    assert bit == forced
                    assert carry == 0
                    assert t[2] == r
                    assert t[3] == direct_T(y)
                    s = t


def audit_current_layers():
    expected = {
        44: (73, 5_908_625_413_101_667_397_287),
        45: (74, 17_725_876_239_305_002_191_859),
    }
    for m, (L, want_max) in expected.items():
        nmax = 6 * 3**m + 1
        assert nmax == want_max
        assert nmax < 2**L
        assert nmax >= 2**(L-1)


def main():
    audit_small_thresholds()
    audit_current_layers()
    print("finite-address deterministic-tail regression: PASS")
    print("m44 address depth=73")
    print("m45 address depth=74")


if __name__ == "__main__":
    main()
