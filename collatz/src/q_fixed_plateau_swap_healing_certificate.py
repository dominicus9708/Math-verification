#!/usr/bin/env python3
"""
Exact regression for the fixed-Q plateau-swap healing lemma.

For the odd-event affine residue recurrence

    F_v(y) = (3 y + 1) 2^{-v}  (mod 3^Q),

a local time-expanded swap 01 <-> 10 changes two adjacent odd gaps

    (a,b) <-> (a+1,b-1),   b>=2.

After the two affected odd events, the residue difference is exactly

    2^{-b} (mod 3^Q)

(up to sign if the orientation is reversed), hence is a 3-adic unit.
Every subsequent common odd-event update multiplies the difference by
3 times a dyadic unit, so its 3-adic valuation increases by exactly one
until it vanishes modulo 3^Q after Q common odd events.

The algebraic identities are the proof.  This program is an implementation
regression over Q<=8, small local gaps, every starting residue, and a
nonconstant deterministic common suffix.
"""


def step(y: int, v: int, mod: int) -> int:
    return ((3 * y + 1) * pow(2, -v, mod)) % mod


def v3_mod(d: int, Q: int) -> int:
    """Truncated 3-adic valuation in Z/(3^Q)."""
    if d == 0:
        return Q
    t = 0
    while t < Q and d % 3 == 0:
        d //= 3
        t += 1
    return t


def main() -> None:
    cases = 0

    for Q in range(1, 9):
        mod = 3 ** Q

        for a in range(1, 7):
            for b in range(2, 7):
                inv2b = pow(2, -b, mod)

                for y in range(mod):
                    # Two adjacent odd-gap descriptions of the same total
                    # binary length, corresponding to moving the middle odd
                    # event by one binary step.
                    left = step(step(y, a, mod), b, mod)
                    right = step(step(y, a + 1, mod), b - 1, mod)

                    delta = (right - left) % mod
                    assert delta == inv2b
                    assert v3_mod(delta, Q) == 0

                    # Append an identical suffix.  The gap pattern is varied
                    # deterministically so the regression does not rely on a
                    # constant future exponent.
                    d = delta
                    for t in range(Q):
                        assert v3_mod(d, Q) == t
                        v = 1 + ((a + 2 * b + t) % 5)
                        d = (3 * d * pow(2, -v, mod)) % mod

                    assert d == 0
                    cases += 1

    assert cases == 295_200
    print(f"checked_cases {cases}")
    print("q-fixed plateau swap healing certificate: PASS")


if __name__ == "__main__":
    main()
